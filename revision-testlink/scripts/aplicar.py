"""Fase 3: aplica propuestas de ../propuestas.json a TestLink.

Uso:
  python3 aplicar.py --ids TL-50            (piloto)
  python3 aplicar.py --lote                 (todas las no bloqueadas y sin conflicto)

Protecciones:
- No aplica casos con bloqueado=true (T09/T10/T11) ni conflicto=true (editados por otra persona).
- Antes de escribir, compara el caso en vivo con el respaldo más reciente; si cambió, no lo toca.
- Después de escribir, vuelve a leer el caso y lo compara campo por campo con la propuesta.
Registra cada caso en ../aplicado.log (ID, versión, resultado), sin datos sensibles.
"""
import argparse
import datetime
import glob
import json
import os
import sys

import escritura

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG = os.path.join(RAIZ, "aplicado.log")


def log(msg):
    line = f"{datetime.datetime.now().isoformat(timespec='seconds')} {msg}"
    print(line)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def snapshot(c):
    return {"name": c["name"], "summary": c["summary"], "preconditions": c["preconditions"],
            "steps": sorted(c.get("steps") or [], key=lambda s: int(s["step_number"]))}


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--ids")
    g.add_argument("--lote", action="store_true")
    a = ap.parse_args()

    props = {p["id"]: p for p in json.load(open(os.path.join(RAIZ, "propuestas.json"), encoding="utf-8"))["casos"]}
    resp_path = sorted(glob.glob(os.path.join(RAIZ, "respaldo-*.json")))[-1]
    resp = {c["full_tc_external_id"]: c for c in json.load(open(resp_path, encoding="utf-8"))["casos"]}
    ids = [x.strip() for x in a.ids.split(",")] if a.ids else sorted(props, key=lambda x: int(x.split("-")[1]))
    log(f"INICIO {'lote' if a.lote else 'ids=' + a.ids} respaldo={os.path.basename(resp_path)}")
    res = {"OK": 0, "ERROR": 0, "OMITIDO": 0}
    for ext in ids:
        p = props.get(ext)
        if not p:
            log(f"{ext} OMITIDO sin propuesta"); res["OMITIDO"] += 1; continue
        if p.get("bloqueado"):
            log(f"{ext} OMITIDO bloqueado ({p['ticket']})"); res["OMITIDO"] += 1; continue
        if p.get("conflicto"):
            log(f"{ext} OMITIDO conflicto: editado por otra persona después del primer respaldo"); res["OMITIDO"] += 1; continue
        try:
            live = escritura.read_case(ext, p["version"])
            if escritura.compare(live, snapshot(resp[ext])):
                log(f"{ext} OMITIDO cambió en TestLink desde {os.path.basename(resp_path)}"); res["OMITIDO"] += 1; continue
            if p.get("solo_nombre"):
                import tl
                escritura._check(tl.call("tl.updateTestCase", testcaseexternalid=ext, version=int(p["version"]), testcasename=p["name"]), "updateTestCase")
            else:
                escritura.write_case(ext, p["version"], p["name"], p["summary"], p["preconditions"], p["steps"])
            after = escritura.read_case(ext, p["version"])
            d = escritura.compare(after, {"name": p["name"], "summary": p["summary"], "preconditions": p["preconditions"],
                                          "steps": p["steps"], "importance": live["importance"],
                                          "execution_type": live["execution_type"], "status": live["status"]})
            if d:
                log(f"{ext} v{p['version']} ERROR verificación: {', '.join(d)}"); res["ERROR"] += 1
            else:
                log(f"{ext} v{p['version']} OK ({'solo título' if p.get('solo_nombre') else str(len(p['steps'])) + ' pasos'})"); res["OK"] += 1
        except Exception as e:
            log(f"{ext} v{p.get('version')} ERROR {type(e).__name__}: {str(e)[:200]}"); res["ERROR"] += 1
    log(f"FIN {res}")
    sys.exit(1 if res["ERROR"] else 0)


if __name__ == "__main__":
    main()
