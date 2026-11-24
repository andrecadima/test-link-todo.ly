"""Registra resultados globales: solo los 15 casos del plan 2897, build 1.

Limitación comprobada en esta instancia: REST acepta el JSON de pasos, pero no
conserva sus notas en la vista Print. Completar y verificar los pasos mediante
la interfaz. Un HTTP exitoso no acredita el registro individual de los pasos.
"""

import json
from pathlib import Path
import sys
import urllib.request
import xmlrpc.client

ROOT = Path(__file__).resolve().parents[2]
IDS = [1389, 1398, 1407, 1416, 1425, 1434, 1443, 1452, 1461,
       1471, 1478, 1485, 1490, 1495, 1500]
BASE = "http://68.211.149.112"


def run(source):
    key = (ROOT / ".secrets/testlink-api-key.local").read_text().strip()
    rpc = xmlrpc.client.ServerProxy(BASE + "/lib/api/xmlrpc/v1/xmlrpc.php", allow_none=True)
    journal_path = Path(__file__).parent / "ejecucion.json"
    for record in json.loads(Path(source).read_text())["records"]:
        number = int(record["case"])
        if not 1 <= number <= 15:
            raise ValueError("Fuera del alcance de las dos suites")
        context = {"devKey": key, "testcaseid": IDS[number-1],
                   "testplanid": 2897, "buildid": 1}
        spec = rpc.tl.getTestCase({"devKey": key, "testcaseid": IDS[number-1]})[0]
        actual_steps = {int(s["step_number"]) for s in spec["steps"]}
        steps = record["steps"]
        if {s["stepNumber"] for s in steps} != actual_steps:
            raise ValueError("Faltan pasos o sobran pasos en TC-" + str(number))
        if any(s["statusCode"] not in {"p", "f", "b"} for s in steps):
            raise ValueError("Estado de paso no admitido")
        if record["status"] not in {"p", "f", "b"}:
            raise ValueError("Estado global no admitido")
        last = rpc.tl.getLastExecutionResult(context)[0]
        if record["marker"] not in last.get("notes", ""):
            body = {"testPlanID": 2897, "buildID": 1,
                    "testCaseExternalID": "TC-" + str(number),
                    "executionType": 1, "statusCode": record["status"],
                    "notes": record["marker"] + " — " + record["notes"],
                    "steps": steps}
            # Header estándar de Slim: mantiene POST y evita el parser obsoleto
            # de formularios en PHP. No se cambia configuración del servidor.
            request = urllib.request.Request(
                BASE + "/lib/api/rest/v2/executions",
                data=json.dumps(body).encode(), method="POST",
                headers={"APIKEY": key, "Content-Type": "application/json",
                         "X-HTTP-Method-Override": "POST"})
            with urllib.request.urlopen(request, timeout=30) as response:
                result = json.load(response)
            if result.get("status") != "ok" or int(result.get("id", -1)) < 1:
                raise RuntimeError("La API no confirmó el registro")
        saved = rpc.tl.getLastExecutionResult(context)[0]
        if (saved.get("status") != record["status"] or
                str(saved.get("execution_type")) != "1" or
                record["marker"] not in saved.get("notes", "")):
            raise RuntimeError("El registro no coincide con lo solicitado")
        journal = json.loads(journal_path.read_text())
        case = journal["casos"][number-1]
        if (case.get("execution_id") == int(saved["id"]) and
                case.get("notas_por_paso_verificadas")):
            print("TC-%s: registro nativo ya verificado; sin cambios" % number)
            continue
        case.update(resultado={"p":"passed", "f":"failed", "b":"blocked"}[saved["status"]],
                    execution_id=int(saved["id"]), numero_pasos=len(steps),
                    registro_testlink="API confirmó solo nota global, estado y modo Manual; pasos pendientes de registro/verificación nativa",
                    notas_por_paso_verificadas=False,
                    enlace_ejecucion=BASE + "/lib/execute/execPrint.php?id=" + str(saved["id"]),
                    pasos=[{"numero":s["stepNumber"],
                            "resultado":{"p":"passed","f":"failed","b":"blocked"}[s["statusCode"]],
                            "obtenido":s["notes"]} for s in steps])
        case.pop("correccion_testlink", None)
        journal_path.write_text(json.dumps(journal, ensure_ascii=False, indent=2) + "\n")
        print("TC-%s: %s, ejecución %s, Manual; verificar pasos en interfaz" %
              (number, saved["status"], saved["id"]))


if __name__ == "__main__":
    run(sys.argv[1])
