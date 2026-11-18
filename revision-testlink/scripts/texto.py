"""Conversión simple de HTML de TestLink a texto legible (listas numeradas, tablas por filas)."""
import html
import re
from html.parser import HTMLParser


class _P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = []
        self.stack = []  # list counters
        self.cell = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("ol", "ul"):
            self.stack.append([tag, 0])
        elif tag == "li":
            if self.stack:
                self.stack[-1][1] += 1
                mark = f"{self.stack[-1][1]}." if self.stack[-1][0] == "ol" else "-"
            else:
                mark = "-"
            self.out.append("\n" + "  " * max(0, len(self.stack) - 1) + mark + " ")
        elif tag in ("p", "div", "br"):
            self.out.append("\n")
        elif tag == "tr":
            self.out.append("\n| ")
            self.cell = 0
        elif tag in ("td", "th"):
            if self.cell:
                self.out.append(" | ")
            self.cell += 1
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag == "em":
            self.out.append("_")

    def handle_endtag(self, tag):
        if tag in ("ol", "ul") and self.stack:
            self.stack.pop()
            self.out.append("\n")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag == "em":
            self.out.append("_")
        elif tag == "p":
            self.out.append("\n")

    def handle_data(self, data):
        self.out.append(data.replace("\n", " "))


def html_a_texto(s):
    if not s:
        return ""
    p = _P()
    p.feed(html.unescape(s) if "&" in s and "<" not in s else s)
    t = "".join(p.out)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r" *\n *", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()
