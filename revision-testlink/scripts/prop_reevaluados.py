"""Reevaluación (18/11, 16:53) de los casos que la autora editó: T12 completo y TL-15, TL-16, TL-18, TL-19, TL-20.

Se parte de la versión ACTUAL. Se respeta lo que la autora ya mejoró:
- precondición «Credenciales Válidas: …» (sin verbo), conservada literalmente;
- texto del requerimiento sin el rótulo, conservado literalmente.
Se corrige lo que aún no cumple: pasos dentro del Summary, título, «Validar que…», postcondiciones,
precondiciones numeradas, sesión iniciada como estado y la línea «La cuenta no tiene…» (verbo conjugado).
"""
import copy
import json
import os
import re

from texto import html_a_texto
import prop_t12, prop_t13

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IDS = ["TL-40"] + [f"TL-{i}" for i in range(2, 15)] + ["TL-15", "TL-16", "TL-18", "TL-19", "TL-20"]
CODIGO = {"T12": "PEB-76 / T12", "T13": "PEB-77 / T13"}
CREDENCIALES = "**Credenciales Válidas:** correo: **camila@gmail.com** — contraseña: **123456** (sitio: https://todo.ly/)."
SIN_NOMBRES = "Ninguna tarea existente con los nombres que se crean en este caso, para que no se confundan entre sí."
SESION = "Sesión iniciada en Todo.ly con esa cuenta."
# Decisión pendiente del usuario: True = volver a anteponer PEB-XX / TXX (lo exige la rúbrica); False = texto de la autora tal cual.
CON_CODIGO = True


def requerimiento_actual(summary_html):
    """Primer párrafo del Summary actual (el texto de requerimiento que dejó la autora)."""
    t = html_a_texto(summary_html).split("\n")[0].strip()
    return re.sub(r"[_*]", "", t)


def casos(respaldo):
    by = {c["full_tc_external_id"]: c for c in json.load(open(respaldo, encoding="utf-8"))["casos"]}
    base = {c["id"]: c for c in prop_t12.CASOS + prop_t13.CASOS}
    out = []
    for k in IDS:
        c = copy.deepcopy(base[k])
        live = by[k]
        assert "Credenciales Válidas" in html_a_texto(live["preconditions"]), k
        assert "Requerimiento" not in html_a_texto(live["summary"]), k
        req_autora = requerimiento_actual(live["summary"])
        c["req"] = f"{CODIGO[c['ticket']]}. {req_autora}" if CON_CODIGO else req_autora
        extras = [x for x in c["pre"][2:-1]]  # Work, calendario, proyecto con tareas…
        c["pre"] = [CREDENCIALES, SESION] + extras + [SIN_NOMBRES]
        c["problemas"] = [p for p in c["problemas"] if p != "PV"] + ["PV"]
        c["reevaluado"] = True
        c["cambios"] = ["Se conservan «Credenciales Válidas: …» y el texto de requerimiento de la autora"] + \
                       (["Se vuelve a anteponer " + CODIGO[c["ticket"]] + " al requerimiento (rúbrica)"] if CON_CODIGO else []) + \
                       ["Precondiciones numeradas; se añade «Sesión iniciada…» como estado; «La cuenta no tiene…» pasa a «Ninguna tarea existente…»"] + \
                       [x for x in c.get("cambios", []) if "precisada" not in x]
        out.append(c)
    return out
