"""Vuelca un respaldo JSON a texto legible para revisión."""
import json
import sys
from texto import html_a_texto

IMP = {"1": "low", "2": "medium", "3": "high"}


def main(path, out):
    d = json.load(open(path, encoding="utf-8"))
    with open(out, "w", encoding="utf-8") as f:
        for c in sorted(d["casos"], key=lambda c: int(c["tc_external_id"])):
            f.write(f"\n\n######## {c['full_tc_external_id']} v{c['version']} | imp={IMP.get(c['importance'])} | {c['name']}\n")
            f.write("== SUMMARY ==\n" + html_a_texto(c["summary"]) + "\n")
            f.write("== PRECONDITIONS ==\n" + html_a_texto(c["preconditions"]) + "\n")
            for s in c.get("steps") or []:
                f.write(f"== STEP {s['step_number']} ==\nA: {html_a_texto(s['actions'])}\nE: {html_a_texto(s['expected_results'])}\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
