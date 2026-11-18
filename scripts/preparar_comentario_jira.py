"""Convierte el formato acotado de los comentarios QA a HTML de Jira."""

import argparse
import html
import json
import re
from pathlib import Path


def inline(text):
    def plain(value):
        value = html.escape(value, quote=False)
        return re.sub(r'(?<!\d)17/11(?!\d)', '<time datetime="2026-11-17">17/11</time>', value)

    token = re.compile(r"\[([^\]]+)\]\(([^\s)]+)\)|`([^`]+)`|\*\*([^*]+)\*\*")
    chunks, last = [], 0
    for match in token.finditer(text):
        chunks.append(plain(text[last:match.start()]))
        label, url, code, bold = match.groups()
        if url:
            chunks.append(f'<a href="{html.escape(url, quote=True)}">{inline(label)}</a>')
        elif code is not None:
            chunks.append('<code>' + html.escape(code, quote=False) + '</code>')
        else:
            chunks.append('<strong>' + inline(bold) + '</strong>')
        last = match.end()
    chunks.append(plain(text[last:]))
    return ''.join(chunks).replace('\\|', '|')


def media_blocks(items):
    return '\n'.join(
        '<figure data-type="media-single" data-layout="center" '
        'data-width="100" data-width-type="percentage">'
        '<div data-type="media" data-media-type="file" '
        f'data-id="{html.escape(item["fileId"], quote=True)}" '
        f'data-collection="{html.escape(item["collection"], quote=True)}" '
        f'data-alt="{html.escape(item["fileName"], quote=True)}"></div>'
        '<figcaption>' + inline(item['caption']) + '</figcaption></figure>'
        for item in items
    )


def render(source, media):
    lines = re.sub(r'<!--.*?-->', '', source, flags=re.S).splitlines()
    out, paragraph, i = [], [], 0

    def flush():
        if paragraph:
            out.append('<p>' + inline(' '.join(paragraph)) + '</p>')
            paragraph.clear()

    while i < len(lines):
        line = lines[i].strip()
        if not line:
            flush()
        elif line.startswith('|'):
            flush()
            table = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table.append(lines[i].strip())
                i += 1
            assert len(table) >= 2 and re.fullmatch(r'[| :\-]+', table[1])
            rows = [re.split(r'(?<!\\)\|', row.strip('|')) for row in table]
            width = len(rows[0])
            assert all(len(row) == width for row in rows), 'Tabla con columnas inconsistentes'
            widths = [280] + [140 if width >= 7 else 240] * (width - 1)
            if [cell.strip() for cell in rows[0]] == ['Escenario', 'Paso', 'Descripción']:
                widths = [100, 60, 420]
            elif [cell.strip() for cell in rows[0]] == ['Paso', 'Actor', 'Sistema']:
                widths = [90, 280, 340]
            out.append('<table data-layout="wide" data-display-mode="fixed"><thead><tr>' + ''.join(f'<th data-colwidth="{w}">' + inline(c.strip()) + '</th>' for c, w in zip(rows[0], widths)) + '</tr></thead><tbody>')
            out.extend('<tr>' + ''.join(f'<td data-colwidth="{w}">' + inline(c.strip()) + '</td>' for c, w in zip(row, widths)) + '</tr>' for row in rows[2:])
            out.append('</tbody></table>')
            continue
        elif heading := re.match(r'^(#{1,6}) (.+)$', line):
            flush()
            if heading[2].startswith('8. ') and media:
                out.append(media_blocks(media))
            level = len(heading[1])
            out.append(f'<h{level}>' + inline(heading[2]) + f'</h{level}>')
        elif line.startswith('- '):
            flush()
            items = []
            while i < len(lines) and lines[i].strip().startswith('- '):
                items.append(lines[i].strip()[2:])
                i += 1
            out.append('<ul>' + ''.join('<li><p>' + inline(x) + '</p></li>' for x in items) + '</ul>')
            continue
        else:
            assert not line.startswith('```'), 'Bloque no admitido en este formato acotado'
            paragraph.append(line)
        i += 1
    flush()
    body = '\n'.join(out)
    assert len(body) <= 32767, 'Comentario mayor al límite de Jira'
    assert 'BORRADOR' not in body
    return body


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--media-json', type=Path)
    args = parser.parse_args()
    items = json.loads(args.media_json.read_text()) if args.media_json else []
    body = render(args.source.read_text(), items)
    args.output.write_text(body + '\n')
    print(f'HTML local: {len(body)} caracteres, {body.count("<table ")} tablas, {len(items)} imágenes. Sin publicación.')
