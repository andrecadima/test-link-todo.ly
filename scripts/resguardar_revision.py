"""Respalda archivos ajenos intactos con cifrado autenticado, sin publicar claves."""

import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tmp/python-crypto"))
from cryptography.fernet import Fernet

KEY = ROOT / ".secrets/resguardo-revision-git.key"
OUT = ROOT / "trabajo/resguardos-revision"
MANIFEST = OUT / "manifest.json"


def cipher(create=False):
    if not KEY.exists():
        if not create:
            raise FileNotFoundError("Falta la clave privada local del resguardo")
        key = Fernet.generate_key()
        with os.fdopen(os.open(KEY, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), "wb") as stream:
            stream.write(key)
    return Fernet(KEY.read_bytes().strip())


def archive(paths):
    box = cipher(create=True)
    records, pending = [], []
    for raw in paths:
        source = (ROOT / raw).resolve()
        if not source.is_relative_to(ROOT / "revision-testlink"):
            raise ValueError("El origen debe pertenecer a revision-testlink")
        data = source.read_bytes()
        if source.suffix == ".json":
            json.loads(data)
        elif source.suffix == ".py":
            ast.parse(data)
        encrypted = box.encrypt(data)
        if box.decrypt(encrypted) != data or source.read_bytes() != data:
            raise RuntimeError("El origen cambió durante la copia; reintentar cuando esté estable")
        relative = source.relative_to(ROOT).as_posix()
        target = OUT / (relative.replace("/", "__") + ".fernet")
        pending.append((target, encrypted))
        records.append({"source": relative, "encrypted": target.relative_to(ROOT).as_posix(),
                        "size": len(data), "cipher_sha256": hashlib.sha256(encrypted).hexdigest()})
    OUT.mkdir(parents=True, exist_ok=True)
    for target, data in pending:
        target.write_bytes(data)
    MANIFEST.write_text(json.dumps({"format": "Fernet", "key": ".secrets/resguardo-revision-git.key",
                                    "files": records}, ensure_ascii=False, indent=2) + "\n")
    print(f"{len(records)} copias cifradas; originales intactos y clave fuera de git.")


def restore(destination):
    destination = (ROOT / destination).resolve()
    if not any(destination.is_relative_to(ROOT / part) for part in ("tmp", ".secrets")):
        raise ValueError("La restauración debe quedar en tmp/ o .secrets/ para no publicar credenciales")
    box = cipher()
    records = json.loads(MANIFEST.read_text())["files"]
    outputs = []
    for record in records:
        source = (ROOT / record["encrypted"]).resolve()
        if not source.is_relative_to(OUT):
            raise ValueError("Ruta cifrada fuera del resguardo")
        payload = source.read_bytes()
        if hashlib.sha256(payload).hexdigest() != record["cipher_sha256"]:
            raise ValueError("El archivo cifrado no coincide con su manifiesto")
        target = (destination / record["source"]).resolve()
        if not target.is_relative_to(destination) or target.exists():
            raise ValueError("Destino no válido o existente; no se sobrescribe")
        outputs.append((target, box.decrypt(payload)))
    for target, data in outputs:
        target.parent.mkdir(parents=True, exist_ok=True)
        with os.fdopen(os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), "wb") as stream:
            stream.write(data)
    print(f"{len(outputs)} copias restauradas en un directorio ignorado; originales sin cambios.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", nargs="*")
    parser.add_argument("--restore", type=Path)
    args = parser.parse_args()
    if args.restore:
        restore(args.restore)
    elif args.sources:
        archive(args.sources)
    else:
        parser.error("Indica los orígenes o --restore")
