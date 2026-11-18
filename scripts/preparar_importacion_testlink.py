"""Prepara un XML local de casos; no conecta con TestLink ni es una exportación."""

import argparse
import html
import json
from pathlib import Path
import xml.etree.ElementTree as ET


def paragraph(value):
    return f"<p>{html.escape(value, quote=False)}</p>"


def prepare(source, output, ticket):
    cases = json.loads(source.read_text())
    importance = {"low": "1", "medium": "2", "high": "3"}
    # El destino lo elige Codex en la suite existente Todo.ly tests.
    # La entrada no crea suites ni contiene IDs que actualicen casos existentes.
    suite = ET.Element("testcases")
    ids = set()
    for position, case in enumerate(cases, 1):
        if case["id"] in ids or not case["id"].startswith(ticket + "-"):
            raise ValueError("Identificador duplicado o ajeno al ticket")
        ids.add(case["id"])
        if not case["pasos"] or "PENDIENTE:" in json.dumps(case, ensure_ascii=False):
            raise ValueError(f"Caso sin pasos o con resultado pendiente: {case['id']}")
        name = f"{case['id']}. {case['titulo']}"
        if len(name) > 100:
            raise ValueError(f"Nombre mayor al formato estándar de TestLink: {case['id']}")
        node = ET.SubElement(suite, "testcase", {"name": name})
        ET.SubElement(node, "node_order").text = str(position)
        ET.SubElement(node, "summary").text = "".join(
            paragraph(label + value)
            for label, value in [
                ("Importancia: ", case["importancia"] + ". " + case["razon"]),
                ("Requerimiento: ", case["requerimiento"]),
                ("Descripción: ", case["descripcion"]),
                ("Postcondiciones: ", case["postcondiciones"]),
            ]
        )
        ET.SubElement(node, "preconditions").text = "<ol>" + "".join(
            f"<li>{html.escape(value, quote=False)}</li>" for value in case["precondiciones"]
        ) + "</ol>"
        ET.SubElement(node, "execution_type").text = "1"
        ET.SubElement(node, "importance").text = importance[case["importancia"]]
        steps = ET.SubElement(node, "steps")
        for number, (action, expected) in enumerate(case["pasos"], 1):
            if not action or not expected:
                raise ValueError(f"Paso incompleto: {case['id']}, {number}")
            step = ET.SubElement(steps, "step")
            ET.SubElement(step, "step_number").text = str(number)
            ET.SubElement(step, "actions").text = paragraph(action)
            ET.SubElement(step, "expectedresults").text = paragraph(expected)
            ET.SubElement(step, "execution_type").text = "1"
    ET.indent(suite, space="  ")
    ET.ElementTree(suite).write(output, encoding="utf-8", xml_declaration=True)
    # Comprueba que el artefacto final puede abrirse y contiene el conjunto completo.
    actual = ET.parse(output).getroot()
    if len(actual.findall("testcase")) != len(cases):
        raise ValueError("El XML no contiene todos los casos")
    print(f"Propuesta local: {len(cases)} casos, {len(actual.findall('.//step'))} pasos; sin IDs asignados ni conexión externa.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--ticket", required=True)
    args = parser.parse_args()
    prepare(args.source, args.output, args.ticket)
