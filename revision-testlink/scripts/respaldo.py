"""Fase 1: descarga todos los casos del proyecto Todo.ly (última versión, con pasos) a un JSON de respaldo."""
import datetime
import json
import os
import tl

OUT_DIR = os.path.join(os.path.dirname(__file__), "..")


def suites_recursive(suite):
    yield suite
    try:
        children = tl.call("tl.getTestSuitesForTestSuite", testsuiteid=suite["id"])
    except Exception:
        children = {}
    if isinstance(children, dict):
        if "id" in children and "name" in children:
            children = [children]
        else:
            children = list(children.values())
    for c in children or []:
        if isinstance(c, dict) and "id" in c:
            yield from suites_recursive(c)


def main():
    proj = tl.call("tl.getTestProjectByName", testprojectname=tl.PROJECT_NAME)
    if isinstance(proj, list):
        proj = proj[0]
    first = tl.call("tl.getFirstLevelTestSuitesForTestProject", testprojectid=proj["id"])
    suites = []
    for s in first:
        suites.extend(suites_recursive(s))
    cases = []
    for s in suites:
        lst = tl.call("tl.getTestCasesForTestSuite", testsuiteid=s["id"], deep=False, details="simple")
        for item in lst or []:
            tc = tl.call("tl.getTestCase", testcaseid=item["id"])
            tc = tc[0] if isinstance(tc, list) else tc
            tc["_suite"] = {"id": s["id"], "name": s["name"]}
            cases.append(tc)
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    path = os.path.abspath(os.path.join(OUT_DIR, f"respaldo-{stamp}.json"))
    data = {
        "generado": datetime.datetime.now().isoformat(timespec="seconds"),
        "proyecto": {"id": proj["id"], "name": proj["name"], "prefix": proj.get("prefix")},
        "suites": [{"id": s["id"], "name": s["name"], "parent_id": s.get("parent_id")} for s in suites],
        "casos": cases,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(path, "suites:", len(suites), "casos:", len(cases))


if __name__ == "__main__":
    main()
