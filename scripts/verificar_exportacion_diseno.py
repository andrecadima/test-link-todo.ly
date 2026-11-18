"""Compara casos propios de una exportación real con el diseño, sin conectar servicios."""

import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def normalize(value):
    parser = Text()
    parser.feed(value or "")
    return re.sub(r"\s+", "", html.unescape("".join(parser.parts)).replace("**", ""))


def compare(source, workspace):
    exported = ET.parse(source).getroot()
    report = {"source": str(source), "tickets": {}}
    for ticket in ("T09", "T10", "T11"):
        design = json.loads((workspace / "trabajo" / ticket / "casos-listos.json").read_text())
        nodes = [node for node in exported.iter("testcase")
                 if re.match(rf"^{ticket}-\d{{2}}(?:[.\s]|$)", node.get("name", ""))]
        rows = []
        for case in design:
            matches = [node for node in nodes if node.get("name", "").startswith(case["id"] + ".")]
            row = {"caso": case["id"], "coincidencias": len(matches), "diferencias": []}
            rows.append(row)
            if len(matches) != 1:
                row["diferencias"].append("Caso ausente o duplicado")
                continue
            node = matches[0]
            row["externalid"] = node.findtext("externalid")
            row["internalid"] = node.get("internalid")
            if normalize(node.get("name")) != normalize(case["id"] + ". " + case["titulo"]):
                row["diferencias"].append("Título")
            summary = normalize(node.findtext("summary"))
            for label, key in (("Descripción", "descripcion"), ("Requerimiento", "requerimiento"),
                               ("Postcondiciones", "postcondiciones")):
                if normalize(case[key]) not in summary:
                    row["diferencias"].append(label)
            preconditions = normalize(node.findtext("preconditions"))
            for number, value in enumerate(case["precondiciones"], 1):
                if normalize(value) not in preconditions:
                    row["diferencias"].append(f"Precondición {number}")
            steps = node.findall("./steps/step")
            if len(steps) != len(case["pasos"]):
                row["diferencias"].append("Cantidad de pasos")
            for number, (step, expected) in enumerate(zip(steps, case["pasos"]), 1):
                for tag, value in zip(("actions", "expectedresults"), expected):
                    if normalize(step.findtext(tag)) != normalize(value):
                        row["diferencias"].append(f"Paso {number}: {tag}")
                if step.findtext("execution_type") != "1":
                    row["diferencias"].append(f"Paso {number}: Manual")
            if node.findtext("execution_type") != "1":
                row["diferencias"].append("Execution type")
            if node.findtext("importance") != {"low": "1", "medium": "2", "high": "3"}[case["importancia"]]:
                row["diferencias"].append("Importance")
        report["tickets"][ticket] = {"disenados": len(design), "exportados": len(nodes), "casos": rows}
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    result = compare(args.source, Path(__file__).resolve().parents[1])
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    for ticket, data in result["tickets"].items():
        print(ticket, "casos", data["exportados"], "con diferencias",
              sum(bool(row["diferencias"]) for row in data["casos"]))
