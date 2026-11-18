"""Lectura, escritura y comparación de casos de TestLink vía XML-RPC.

write_case() deja el caso exactamente con el nombre, summary, preconditions y pasos indicados:
1) borra los pasos actuales (tl.deleteTestCaseSteps), 2) actualiza nombre/summary/preconditions
(tl.updateTestCase) y 3) crea los pasos nuevos (tl.createTestCaseSteps).
No toca importancia, estado, tipo de ejecución, duración ni suite.
"""
import re
import tl
from texto import html_a_texto


def read_case(ext_id, version=None):
    args = {"testcaseexternalid": ext_id}
    if version:
        args["version"] = int(version)
    r = tl.call("tl.getTestCase", **args)
    return r[0] if isinstance(r, list) else r


def _check(resp, what):
    """La API devuelve una lista de dicts; los errores traen 'code' y 'message'."""
    items = resp if isinstance(resp, list) else [resp]
    for it in items:
        if isinstance(it, dict) and "code" in it and "message" in it and str(it.get("code")) not in ("0",):
            if not (isinstance(it.get("status_ok"), (bool, int)) and it.get("status_ok")):
                raise RuntimeError(f"{what}: [{it.get('code')}] {it.get('message')}")
    return resp


def _steps_payload(steps):
    out = []
    for i, s in enumerate(steps, 1):
        out.append({
            "step_number": i,
            "actions": s["actions"],
            "expected_results": s["expected_results"],
            "execution_type": int(s.get("execution_type", 1) or 1),
        })
    return out


def write_case(ext_id, version, name, summary, preconditions, steps):
    version = int(version)
    current = read_case(ext_id, version)
    cur_steps = current.get("steps") or []
    if cur_steps:
        nums = [int(s["step_number"]) for s in cur_steps]
        _check(tl.call("tl.deleteTestCaseSteps", testcaseexternalid=ext_id, version=version, steps=nums),
               "deleteTestCaseSteps")
    _check(tl.call("tl.updateTestCase", testcaseexternalid=ext_id, version=version,
                   testcasename=name, summary=summary, preconditions=preconditions),
           "updateTestCase")
    if steps:
        _check(tl.call("tl.createTestCaseSteps", testcaseexternalid=ext_id, version=version,
                       action="create", steps=_steps_payload(steps)),
               "createTestCaseSteps")


def _norm_html(s):
    s = (s or "").replace("\r\n", "\n").strip()
    return re.sub(r">\s+<", "><", s)


def compare(case, target):
    """Devuelve la lista de diferencias entre un caso leído y el objetivo (name/summary/preconditions/steps)."""
    diffs = []

    def same(a, b):
        if _norm_html(a) == _norm_html(b):
            return True
        return html_a_texto(a) == html_a_texto(b)

    for f in ("name", "summary", "preconditions"):
        if not same(case.get(f), target.get(f)):
            diffs.append(f)
    cs = case.get("steps") or []
    ts = target.get("steps") or []
    if len(cs) != len(ts):
        diffs.append(f"steps: {len(cs)} en TestLink vs {len(ts)} esperados")
    else:
        cs = sorted(cs, key=lambda s: int(s["step_number"]))
        for i, (a, b) in enumerate(zip(cs, ts), 1):
            if int(a["step_number"]) != i:
                diffs.append(f"paso {i}: número {a['step_number']}")
            if not same(a.get("actions"), b.get("actions")):
                diffs.append(f"paso {i}: actions")
            if not same(a.get("expected_results"), b.get("expected_results")):
                diffs.append(f"paso {i}: expected_results")
    for f in ("importance", "execution_type", "status"):
        if f in target and str(case.get(f)) != str(target.get(f)):
            diffs.append(f"{f}: {case.get(f)} vs {target.get(f)}")
    return diffs
