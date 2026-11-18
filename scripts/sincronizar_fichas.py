"""Sincroniza fichas y borrador de Jira desde los dos conjuntos revisables."""

import argparse
import json
from pathlib import Path


def render(case):
    def cell(value):
        return value.replace("|", "\\|")

    rows = "\n".join(
        f"| {number}. {cell(action)} | {cell(expected)} |"
        for number, (action, expected) in enumerate(case["pasos"], 1)
    )
    preconditions = "\n".join(
        f"{number}. {value}" for number, value in enumerate(case["precondiciones"], 1)
    )
    return "\n\n".join([
        f"### {case['id']}. {case['titulo']}",
        f"**Importancia:** **{case['importancia']}**. {case['razon']}",
        f"**Requerimiento:** {case['requerimiento']}",
        "**Precondiciones:**\n" + preconditions,
        f"**Descripción:** {case['descripcion']}",
        "| Paso | Resultado esperado |\n|---|---|\n" + rows,
        f"**Postcondiciones:** {case['postcondiciones']}",
    ])


def synchronize(ticket):
    root = Path("trabajo") / ticket
    ready = json.loads((root / "casos-listos.json").read_text())
    pending = json.loads((root / "casos-pendientes.json").read_text())
    current = json.loads((root / "casos.json").read_text())
    merged = ready + pending
    ids = [case["id"] for case in merged]
    if len(set(ids)) != len(ids) or set(ids) != {case["id"] for case in current}:
        raise ValueError("Los conjuntos no conservan los identificadores del diseño")
    (root / "casos.json").write_text(
        json.dumps(sorted(merged, key=lambda case: case["id"]), ensure_ascii=False, indent=2) + "\n"
    )
    analysis = root / "analisis-diseno.md"
    marker = "<!-- FICHAS_GENERADAS -->"
    raw = analysis.read_text()
    if marker not in raw:
        raise ValueError("Falta el marcador de fichas: no se sobrescribe el análisis")
    prefix = raw.split(marker)[0]
    fichas = [render(case) for case in ready]
    if pending:
        fichas.append("## Candidatos pendientes — no registrar todavía")
        fichas.extend(render(case) for case in pending)
    analysis.write_text(prefix + marker + "\n\n" + "\n\n---\n\n".join(fichas) + "\n")
    # El borrador público conserva las nueve secciones, sin la metadata de trabajo.
    title = prefix.splitlines()[0]
    body = "## 1." + prefix.split("## 1.", 1)[1]
    body = body.split("## Fichas", 1)[0].rstrip()
    (root / "comentario-jira-borrador.md").write_text(
        "<!-- BORRADOR: publicar solo después de revisión y registro verificado. -->\n\n"
        + title + "\n\n" + body + "\n"
    )
    print(f"{ticket}: {len(ready)} fichas listas y {len(pending)} pendientes sincronizadas.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ticket", choices=["T09", "T10", "T11"])
    synchronize(parser.parse_args().ticket)
