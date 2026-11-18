"""Extrae los casos propios de una exportación real, conservando sus datos e IDs."""

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET


def extract(source, output_dir):
    raw = source.read_bytes()
    root = ET.fromstring(raw)
    grouped = {ticket: [] for ticket in ("T09", "T10", "T11")}
    for case in root.iter("testcase"):
        match = re.match(r"^(T09|T10|T11)-\d{2}(?:[.\s]|$)", case.get("name", ""))
        if match:
            grouped[match[1]].append(case)
    missing = [ticket for ticket, cases in grouped.items() if not cases]
    if missing:
        raise ValueError("La exportación no contiene casos de: " + ", ".join(missing))
    manifest = {
        "source": str(source),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "tickets": {},
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    for ticket, cases in grouped.items():
        target = ET.Element("testcases")
        for case in cases:
            target.append(copy.deepcopy(case))
        output = output_dir / f"{ticket}.xml"
        ET.ElementTree(target).write(output, encoding="utf-8", xml_declaration=True)
        actual = ET.parse(output).getroot().findall("testcase")
        if len(actual) != len(cases):
            raise ValueError(f"La extracción perdió casos de {ticket}")
        for original, extracted in zip(cases, actual):
            if ET.tostring(original) != ET.tostring(extracted):
                raise ValueError(f"La extracción alteró un caso de {ticket}")
        manifest["tickets"][ticket] = {
            "file": str(output),
            "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
            "count": len(actual),
            "cases": [
                {
                    "name": case.get("name"),
                    "internalid": case.get("internalid"),
                    "externalid": case.findtext("externalid"),
                }
                for case in actual
            ],
        }
    (output_dir / "origen-exportacion.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    )
    print("Extraídos sin cambiar IDs: " + "; ".join(
        f"{ticket}={len(cases)}" for ticket, cases in grouped.items()
    ))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    extract(args.source, args.output_dir)
