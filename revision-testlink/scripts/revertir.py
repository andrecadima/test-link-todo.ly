"""Restaura casos desde un respaldo JSON (nombre, summary, preconditions y pasos).

Uso:
  python3 revertir.py --respaldo ../respaldo-AAAAMMDD-HHMM.json --ids TL-41,TL-42      (simulación)
  python3 revertir.py --respaldo ../respaldo-AAAAMMDD-HHMM.json --todos               (simulación)
  python3 revertir.py --respaldo ... --ids TL-41 --aplicar                            (escribe)

Por defecto solo simula: lee el estado actual, lo compara con el respaldo y muestra qué cambiaría.
Con --aplicar escribe y vuelve a leer para confirmar que el caso coincide con el respaldo.
"""
import argparse
import json
import sys

import escritura


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--respaldo", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--ids", help="IDs externos separados por coma, p. ej. TL-41,TL-42")
    g.add_argument("--todos", action="store_true")
    ap.add_argument("--aplicar", action="store_true", help="escribir en TestLink (sin esto, solo simula)")
    a = ap.parse_args()

    data = json.load(open(a.respaldo, encoding="utf-8"))
    by_id = {c["full_tc_external_id"]: c for c in data["casos"]}
    ids = list(by_id) if a.todos else [x.strip() for x in a.ids.split(",") if x.strip()]
    modo = "APLICAR" if a.aplicar else "SIMULACIÓN"
    print(f"Modo: {modo} · respaldo: {a.respaldo} · casos: {len(ids)}")
    errores = 0
    for ext in ids:
        b = by_id.get(ext)
        if not b:
            print(f"{ext}: no está en el respaldo"); errores += 1; continue
        target = {"name": b["name"], "summary": b["summary"], "preconditions": b["preconditions"],
                  "steps": sorted(b.get("steps") or [], key=lambda s: int(s["step_number"]))}
        try:
            cur = escritura.read_case(ext, b["version"])
        except Exception as e:
            print(f"{ext}: error al leer: {e}"); errores += 1; continue
        diffs = escritura.compare(cur, target)
        if not diffs:
            print(f"{ext} v{b['version']}: ya coincide con el respaldo (nada que hacer)")
            continue
        if not a.aplicar:
            print(f"{ext} v{b['version']}: se restauraría -> {', '.join(diffs)}")
            continue
        try:
            escritura.write_case(ext, b["version"], target["name"], target["summary"],
                                 target["preconditions"], target["steps"])
            after = escritura.compare(escritura.read_case(ext, b["version"]), target)
            print(f"{ext}: {'RESTAURADO OK' if not after else 'RESTAURADO CON DIFERENCIAS: ' + ', '.join(after)}")
            errores += bool(after)
        except Exception as e:
            print(f"{ext}: ERROR al restaurar: {e}"); errores += 1
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
