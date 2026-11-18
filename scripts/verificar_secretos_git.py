"""Impide commits con credenciales conocidas, sin imprimir sus valores."""

import argparse
import ast
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def private_values():
    secret = (ROOT / '.secrets/cuentas-prueba.local.md').read_text()
    values = [value.strip().strip('`') for value in re.findall(
        r'^.*Contraseña[^:\n]*:\s*(.+)$', secret, re.M) if len(value.strip()) >= 8]
    # El respaldo ajeno incluye una clave numérica corta que no coincide con A/B.
    # Se obtiene privadamente del original ignorado; nunca se guarda aquí.
    source = ROOT / 'revision-testlink/scripts/modelo.py'
    if source.exists():
        constants = {}
        for node in ast.parse(source.read_text()).body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if getattr(target, 'id', '') in {'CAMILA_PW', 'CAMILA_SIN_PW'}:
                        constants[target.id] = ast.literal_eval(node.value)
        if len(constants) == 2:
            without = set(re.findall(r'[A-Za-z0-9@!_.-]+', constants['CAMILA_SIN_PW']))
            values += [word for word in re.findall(r'[A-Za-z0-9@!_.-]+', constants['CAMILA_PW'])
                       if word not in without and len(word) >= 6 and word.isdigit()]
    return [value.encode() for value in set(values)]


def scan(tree=None):
    values = private_values()
    names = (git('ls-tree', '-r', '--name-only', tree) if tree else
             git('diff', '--cached', '--name-only', '--diff-filter=ACMR')).decode().splitlines()
    bad = []
    for name in names:
        if name.startswith('.secrets/'):
            bad.append(name)
            continue
        if Path(name).suffix in {'.png', '.jpg', '.heic', '.pdf', '.fernet'}:
            continue
        data = git('show', f'{tree}:{name}' if tree else ':' + name)
        if b'\x00' not in data and any(value in data for value in values):
            bad.append(name)
    print(f'Credenciales conocidas: {len(bad)} archivos con coincidencias; valores ocultos.')
    for name in bad:
        print(name)
    return not bad


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tree')
    args = parser.parse_args()
    raise SystemExit(0 if scan(args.tree) else 1)
