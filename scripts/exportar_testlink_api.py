"""Exporta en SOLO LECTURA la suite Todo.ly tests de TestLink mediante XML-RPC.

Uso (solo después del aviso explícito de Andre de que la revisión terminó):

    TESTLINK_API_KEY=... python3 scripts/exportar_testlink_api.py --revision-finalizada
    TESTLINK_API_KEY=... python3 scripts/exportar_testlink_api.py --revision-finalizada --extraer

Sin --revision-finalizada el script termina antes de leer la clave o abrir la red.

Procedencia del XML
-------------------
No se usa un método de exportación nativa por API: no está confirmado que el
servidor exponga uno. El archivo se RECONSTRUYE desde respuestas XML-RPC con los
nombres de elementos de la exportación nativa de TestLink 1.9 (testsuite,
testcase internalid/name, node_order, externalid, version, summary,
preconditions, execution_type, importance, steps/step/step_number/actions/
expectedresults/execution_type). El XML lleva un comentario de procedencia y
se acompaña de testlink-xml/todo-ly-tests.procedencia.json. No se debe
presentar como exportación hecha desde la interfaz de TestLink.

Métodos usados (todos de lectura, lista cerrada en METODOS_LECTURA):
  tl.checkDevKey, tl.getProjects, tl.getTestSuiteByID,
  tl.getTestSuitesForTestSuite, tl.getTestCasesForTestSuite (deep, full),
  tl.getTestCase (testcaseid; sin version).

Supuestos que se validan en tiempo de ejecución, sin inventar datos:
  * getTestCase sin "version" devuelve la última versión del caso (documentado
    así en la API 1.9). Si el listado deep/full informa una versión mayor para
    el mismo caso, se reporta como diferencia.
  * getTestSuitesForTestSuite puede devolver vacío, un único dict de suite o un
    dict indexado por id; se normalizan los tres formatos.
  * Los pasos llegan en "steps" con "expected_results"; en el XML se escriben
    como <expectedresults>, nombre usado por la exportación nativa.
  * El texto se escribe escapado (no CDATA); el contenido es equivalente.
  * Keywords, campos personalizados, requisitos y adjuntos NO se exportan.

Nunca se imprime la clave ni el contenido de summary/preconditions/pasos.
"""

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import sys
import xml.etree.ElementTree as ET

RAIZ = Path(__file__).resolve().parent.parent
URL_POR_DEFECTO = "http://68.211.149.112/lib/api/xmlrpc/v1/xmlrpc.php"
VARIABLE_CLAVE = "TESTLINK_API_KEY"
CASOS_PROPIOS_ESPERADOS = 29
REGISTROS = [
    RAIZ / "trabajo" / "T09" / "testlink-registro.json",
    RAIZ / "trabajo" / "T10" / "testlink-registro.json",
    RAIZ / "trabajo" / "T11" / "testlink-registro.json",
]
METODOS_LECTURA = frozenset({
    "tl.checkDevKey",
    "tl.getProjects",
    "tl.getTestSuiteByID",
    "tl.getTestSuitesForTestSuite",
    "tl.getTestCasesForTestSuite",
    "tl.getTestCase",
})
PATRON_PROPIO = re.compile(r"^(T09|T10|T11)-(\d{2})(?:[.\s]|$)")


class ErrorExportacion(Exception):
    pass


class ClienteLectura:
    """Envoltorio que solo permite métodos de lectura y oculta la clave."""

    def __init__(self, url, clave, timeout):
        import xmlrpc.client  # importación diferida: nada de red sin el flag

        socket.setdefaulttimeout(timeout)
        self._xmlrpc = xmlrpc.client
        self._proxy = xmlrpc.client.ServerProxy(url, allow_none=True)
        self._clave = clave

    def _limpiar(self, texto):
        return str(texto).replace(self._clave, "***") if self._clave else str(texto)

    def llamar(self, metodo, **params):
        if metodo not in METODOS_LECTURA:
            raise ErrorExportacion(f"Método no permitido (solo lectura): {metodo}")
        params["devKey"] = self._clave
        try:
            respuesta = getattr(self._proxy, metodo)(params)
        except self._xmlrpc.Fault as fallo:
            raise ErrorExportacion(
                f"{metodo}: fallo XML-RPC {fallo.faultCode}: {self._limpiar(fallo.faultString)}"
            ) from None
        except (self._xmlrpc.ProtocolError, OSError) as fallo:
            raise ErrorExportacion(f"{metodo}: error de conexión: {self._limpiar(fallo)}") from None
        if (
            isinstance(respuesta, list)
            and respuesta
            and isinstance(respuesta[0], dict)
            and "code" in respuesta[0]
            and "message" in respuesta[0]
        ):
            primero = respuesta[0]
            raise ErrorExportacion(
                f"{metodo}: TestLink devolvió error {primero['code']}: {self._limpiar(primero['message'])}"
            )
        return respuesta


def entero(valor, campo):
    try:
        return int(valor)
    except (TypeError, ValueError):
        raise ErrorExportacion(f"Respuesta inesperada: {campo}={valor!r} no es entero") from None


def normalizar_suites(respuesta):
    if not respuesta:
        return []
    if isinstance(respuesta, list):
        return [s for s in respuesta if isinstance(s, dict)]
    if isinstance(respuesta, dict):
        if "id" in respuesta and "name" in respuesta:
            return [respuesta]
        return [s for s in respuesta.values() if isinstance(s, dict)]
    raise ErrorExportacion(f"getTestSuitesForTestSuite: formato inesperado {type(respuesta).__name__}")


def validar_suite_en_proyecto(cliente, suite_id, proyecto_id):
    suite = cliente.llamar("tl.getTestSuiteByID", testsuiteid=suite_id)
    if not isinstance(suite, dict) or entero(suite.get("id"), "suite.id") != suite_id:
        raise ErrorExportacion(f"getTestSuiteByID no devolvió la suite {suite_id}")
    actual = suite
    for _ in range(30):
        padre = entero(actual.get("parent_id"), "suite.parent_id")
        if padre == proyecto_id:
            return suite
        try:
            actual = cliente.llamar("tl.getTestSuiteByID", testsuiteid=padre)
        except ErrorExportacion:
            break
        if not isinstance(actual, dict):
            break
    raise ErrorExportacion(f"La suite {suite_id} no pertenece al proyecto {proyecto_id}")


def prefijo_proyecto(cliente, proyecto_id):
    proyectos = cliente.llamar("tl.getProjects")
    for proyecto in proyectos or []:
        if isinstance(proyecto, dict) and str(proyecto.get("id")) == str(proyecto_id):
            return proyecto.get("prefix") or ""
    raise ErrorExportacion(f"tl.getProjects no incluye el proyecto {proyecto_id}")


def arbol_suites(cliente, suite):
    """Devuelve {id: {"datos":..., "hijas":[ids]}} recorriendo la jerarquía."""
    arbol = {}
    pendientes = [suite]
    while pendientes:
        actual = pendientes.pop()
        sid = entero(actual.get("id"), "suite.id")
        if sid in arbol:
            raise ErrorExportacion(f"Ciclo o suite repetida en la jerarquía: {sid}")
        hijas = normalizar_suites(cliente.llamar("tl.getTestSuitesForTestSuite", testsuiteid=sid))
        completas = [cliente.llamar("tl.getTestSuiteByID", testsuiteid=entero(h.get("id"), "hija.id")) for h in hijas]
        for hija in completas:
            if entero(hija.get("parent_id"), "hija.parent_id") != sid:
                raise ErrorExportacion(f"La suite {hija.get('id')} no declara como padre a {sid}")
        arbol[sid] = {"datos": actual, "hijas": [entero(h.get("id"), "hija.id") for h in completas]}
        pendientes.extend(completas)
    return arbol


def leer_casos(cliente, suite_id, suites):
    listado = cliente.llamar(
        "tl.getTestCasesForTestSuite", testsuiteid=suite_id, deep=True, details="full"
    )
    if not isinstance(listado, list):
        raise ErrorExportacion("getTestCasesForTestSuite no devolvió una lista")
    vistos = {}
    diferencias = []
    for fila in listado:
        if not isinstance(fila, dict):
            raise ErrorExportacion("getTestCasesForTestSuite devolvió una fila no válida")
        caso_id = entero(fila.get("id"), "caso.id")
        padre = entero(fila.get("parent_id"), "caso.parent_id")
        if padre not in suites:
            raise ErrorExportacion(f"El caso {caso_id} cuelga de una suite no recorrida ({padre})")
        version_listado = fila.get("version")
        if caso_id in vistos:
            # Si el listado repite el caso por versión, se conserva la mayor.
            previa = vistos[caso_id]["version_listado"]
            if version_listado is not None and (previa is None or int(version_listado) > int(previa)):
                vistos[caso_id]["version_listado"] = version_listado
            continue
        vistos[caso_id] = {
            "padre": padre,
            "node_order": fila.get("node_order"),
            "version_listado": version_listado,
        }
    casos = []
    for caso_id, meta in vistos.items():
        respuesta = cliente.llamar("tl.getTestCase", testcaseid=caso_id)
        if not isinstance(respuesta, list) or len(respuesta) != 1 or not isinstance(respuesta[0], dict):
            raise ErrorExportacion(f"getTestCase({caso_id}) no devolvió exactamente una versión")
        tc = respuesta[0]
        if entero(tc.get("testcase_id"), "testcase_id") != caso_id:
            raise ErrorExportacion(f"getTestCase({caso_id}) devolvió otro caso")
        for campo in ("name", "tc_external_id", "version", "importance", "execution_type"):
            if tc.get(campo) in (None, ""):
                raise ErrorExportacion(f"getTestCase({caso_id}) sin campo {campo}")
        if meta["version_listado"] is not None and int(meta["version_listado"]) > int(tc["version"]):
            diferencias.append(
                f"Caso interno {caso_id}: el listado informa v{meta['version_listado']} "
                f"y getTestCase devolvió v{tc['version']}"
            )
        pasos = tc.get("steps") or []
        if not isinstance(pasos, list):
            raise ErrorExportacion(f"getTestCase({caso_id}): steps con formato inesperado")
        tc["_padre"] = meta["padre"]
        tc["_node_order"] = meta["node_order"] if meta["node_order"] is not None else tc.get("node_order")
        tc["_pasos"] = sorted(pasos, key=lambda p: entero(p.get("step_number"), "step_number"))
        casos.append(tc)
    return casos, diferencias


def texto(padre, etiqueta, valor):
    elemento = ET.SubElement(padre, etiqueta)
    elemento.text = "" if valor is None else str(valor)
    return elemento


def orden(valor, respaldo):
    try:
        return (int(valor), respaldo)
    except (TypeError, ValueError):
        return (sys.maxsize, respaldo)


def construir_xml(suite_id, suites, casos, procedencia):
    por_suite = {}
    for caso in casos:
        por_suite.setdefault(caso["_padre"], []).append(caso)

    def suite_xml(sid, padre=None):
        datos = suites[sid]["datos"]
        atributos = {"id": str(sid), "name": str(datos.get("name", ""))}
        nodo = ET.Element("testsuite", atributos) if padre is None else ET.SubElement(padre, "testsuite", atributos)
        if padre is None:
            nodo.append(ET.Comment(procedencia))
        texto(nodo, "node_order", datos.get("node_order"))
        texto(nodo, "details", datos.get("details"))
        for tc in sorted(por_suite.get(sid, []), key=lambda c: orden(c["_node_order"], int(c["testcase_id"]))):
            caso = ET.SubElement(nodo, "testcase", {"internalid": str(tc["testcase_id"]), "name": str(tc["name"])})
            texto(caso, "node_order", tc["_node_order"])
            texto(caso, "externalid", tc["tc_external_id"])
            texto(caso, "version", tc["version"])
            texto(caso, "summary", tc.get("summary"))
            texto(caso, "preconditions", tc.get("preconditions"))
            texto(caso, "execution_type", tc["execution_type"])
            texto(caso, "importance", tc["importance"])
            for campo in ("status", "active", "is_open"):
                if tc.get(campo) not in (None, ""):
                    texto(caso, campo, tc[campo])
            pasos = ET.SubElement(caso, "steps")
            for paso in tc["_pasos"]:
                step = ET.SubElement(pasos, "step")
                texto(step, "step_number", paso.get("step_number"))
                texto(step, "actions", paso.get("actions"))
                texto(step, "expectedresults", paso.get("expected_results"))
                texto(step, "execution_type", paso.get("execution_type"))
        hijas = sorted(suites[sid]["hijas"], key=lambda h: orden(suites[h]["datos"].get("node_order"), h))
        for hija in hijas:
            suite_xml(hija, nodo)
        return nodo

    return ET.ElementTree(suite_xml(suite_id))


def contrastar_registros(casos, prefijo):
    """Contrasta solo IDs y códigos de caso; nunca redacción (cambiada por la revisión)."""
    esperados = []
    for ruta in REGISTROS:
        datos = json.loads(ruta.read_text(encoding="utf-8"))
        esperados.extend(datos["casos"])
    diferencias = []
    if len(esperados) != CASOS_PROPIOS_ESPERADOS:
        diferencias.append(f"Los registros locales suman {len(esperados)} casos, no {CASOS_PROPIOS_ESPERADOS}")
    por_interno = {int(c["testcase_id"]): c for c in casos}
    vistos = set()
    for esperado in esperados:
        interno = int(esperado["id_interno"])
        vistos.add(interno)
        tc = por_interno.get(interno)
        if tc is None:
            diferencias.append(f"{esperado['caso']} ({esperado['id_testlink']}, interno {interno}) no está en la exportación")
            continue
        externo = f"{prefijo}-{tc['tc_external_id']}" if prefijo else str(tc["tc_external_id"])
        if externo != esperado["id_testlink"]:
            diferencias.append(f"{esperado['caso']}: ID externo exportado {externo}, registrado {esperado['id_testlink']}")
        coincidencia = PATRON_PROPIO.match(str(tc["name"]))
        if not coincidencia or f"{coincidencia[1]}-{coincidencia[2]}" != esperado["caso"]:
            diferencias.append(f"{esperado['caso']} ({externo}): el título exportado no empieza con {esperado['caso']}")
    for tc in casos:
        interno = int(tc["testcase_id"])
        if interno not in vistos and PATRON_PROPIO.match(str(tc["name"])):
            diferencias.append(f"Caso interno {interno} con prefijo T09/T10/T11 no figura en los registros locales")
    propios = sum(1 for tc in casos if int(tc["testcase_id"]) in vistos)
    return propios, diferencias


def escribir_atomico(ruta, contenido_bytes):
    temporal = ruta.with_name(ruta.name + ".tmp")
    temporal.write_bytes(contenido_bytes)
    os.replace(temporal, ruta)


def principal():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--revision-finalizada", action="store_true",
                        help="Obligatorio: confirma el aviso de Andre de que la revisión por API terminó.")
    parser.add_argument("--url", default=URL_POR_DEFECTO)
    parser.add_argument("--proyecto-id", type=int, default=1)
    parser.add_argument("--suite-id", type=int, default=3)
    parser.add_argument("--salida", type=Path, default=RAIZ / "testlink-xml" / "todo-ly-tests.xml")
    parser.add_argument("--sobrescribir", action="store_true",
                        help="Permite reemplazar la exportación o los XML por ticket si ya existen.")
    parser.add_argument("--extraer", action="store_true",
                        help="Tras exportar sin diferencias, ejecuta scripts/extraer_xml_por_ticket.py.")
    parser.add_argument("--timeout", type=float, default=60.0)
    args = parser.parse_args()

    # Barrera previa a cualquier lectura de clave o acceso a red.
    if not args.revision_finalizada:
        print("Rechazado: falta --revision-finalizada. Esperar el aviso explícito de Andre. "
              "No se leyó la clave ni se abrió la red.", file=sys.stderr)
        return 3

    salida = args.salida.resolve()
    destinos_ticket = [salida.parent / f"{t}.xml" for t in ("T09", "T10", "T11")]
    if salida.exists() and not args.sobrescribir:
        print(f"Rechazado: {salida} ya existe; usar --sobrescribir de forma consciente.", file=sys.stderr)
        return 3
    if args.extraer and not args.sobrescribir and any(d.exists() for d in destinos_ticket):
        print("Rechazado: ya existen XML por ticket; usar --sobrescribir de forma consciente.", file=sys.stderr)
        return 3

    clave = os.environ.get(VARIABLE_CLAVE, "").strip()
    if not clave:
        print(f"Falta la variable de entorno {VARIABLE_CLAVE}.", file=sys.stderr)
        return 3

    try:
        cliente = ClienteLectura(args.url, clave, args.timeout)
        if cliente.llamar("tl.checkDevKey") is not True:
            raise ErrorExportacion("tl.checkDevKey no confirmó la clave")
        prefijo = prefijo_proyecto(cliente, args.proyecto_id)
        suite = validar_suite_en_proyecto(cliente, args.suite_id, args.proyecto_id)
        suites = arbol_suites(cliente, suite)
        casos, diferencias = leer_casos(cliente, args.suite_id, suites)
    except ErrorExportacion as error:
        print(f"Exportación abortada sin escribir archivos: {error}", file=sys.stderr)
        return 1

    if not casos:
        print("Exportación abortada: la suite no devolvió casos.", file=sys.stderr)
        return 1

    propios, diferencias_registro = contrastar_registros(casos, prefijo)
    diferencias.extend(diferencias_registro)

    momento = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    host = re.sub(r"^(https?://[^/]+).*$", r"\1", args.url)
    procedencia = (
        f" Reconstruido desde la API XML-RPC de TestLink ({host}) el {momento}; "
        f"proyecto {args.proyecto_id}, suite {args.suite_id}, última versión de cada caso. "
        "No es una exportación nativa de la interfaz. "
    )
    arbol = construir_xml(args.suite_id, suites, casos, procedencia)
    if hasattr(ET, "indent"):  # Python 3.9+; solo afecta espacios entre elementos
        ET.indent(arbol, space="  ")
    contenido = ET.tostring(arbol.getroot(), encoding="utf-8", xml_declaration=True)

    # Comprobación de ida y vuelta antes de escribir.
    releido = ET.fromstring(contenido)
    if len(releido.findall(".//testcase")) != len(casos):
        print("Exportación abortada: el XML reconstruido no contiene todos los casos.", file=sys.stderr)
        return 1

    salida.parent.mkdir(parents=True, exist_ok=True)
    escribir_atomico(salida, contenido)
    manifiesto = {
        "procedencia": "Reconstrucción desde XML-RPC (no exportación nativa)",
        "url_api": host + "/lib/api/xmlrpc/v1/xmlrpc.php",
        "metodos": sorted(METODOS_LECTURA),
        "fecha_utc": momento,
        "proyecto_id": args.proyecto_id,
        "prefijo": prefijo,
        "suite_id": args.suite_id,
        "suites": len(suites),
        "casos_total": len(casos),
        "casos_propios": propios,
        "casos_propios_esperados": CASOS_PROPIOS_ESPERADOS,
        "diferencias": diferencias,
        "archivo": str(salida.relative_to(RAIZ)) if salida.is_relative_to(RAIZ) else str(salida),
        "sha256": hashlib.sha256(contenido).hexdigest(),
        "casos": [
            {
                "internalid": int(tc["testcase_id"]),
                "externalid": f"{prefijo}-{tc['tc_external_id']}" if prefijo else str(tc["tc_external_id"]),
                "version": int(tc["version"]),
                "pasos": len(tc["_pasos"]),
            }
            for tc in sorted(casos, key=lambda c: int(c["testcase_id"]))
        ],
    }
    escribir_atomico(
        salida.with_name(salida.stem + ".procedencia.json"),
        (json.dumps(manifiesto, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
    )

    print(f"Exportados {len(casos)} casos en {len(suites)} suite(s); propios T09–T11: "
          f"{propios}/{CASOS_PROPIOS_ESPERADOS}. SHA-256 {manifiesto['sha256'][:12]}…")
    if diferencias:
        print("DIFERENCIAS (no se corrigió nada en TestLink ni en local):")
        for linea in diferencias:
            print(" - " + linea)
        if args.extraer:
            print("No se extrajeron XML por ticket: resolver o aceptar antes las diferencias.")
        return 2

    if args.extraer:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from extraer_xml_por_ticket import extract

        extract(salida, salida.parent)
    return 0


if __name__ == "__main__":
    sys.exit(principal())
