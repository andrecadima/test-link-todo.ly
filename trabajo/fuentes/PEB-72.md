# PEB-72

Consulta de solo lectura: 2026-11-16. https://alesalve.atlassian.net/browse/PEB-72

{
  "appliedContentFormat": "markdown",
  "id": "10103",
  "key": "PEB-72",
  "fields": {
    "summary": "T08 — Analizar, diseñar y registrar pruebas de eliminación y papelera",
    "description": "Investigar eliminación individual, eliminación de completadas y operaciones disponibles en Recycle Bin. Precisar qué elementos pueden resultar afectados, incluyendo subtareas, y distinguir las acciones recuperables y definitivas que realmente existan.\n\nDeterminar si se diseñarán pruebas funcionales, no funcionales o ambas. Los objetivos posibles incluyen exactitud del alcance de la operación, claridad de sus consecuencias, facilidad para reconocer los elementos afectados, accesibilidad de controles, compatibilidad y protección de información.\n\nConsiderar escenarios positivos, negativos y alternativos: conjuntos vacíos, diferentes estados, elementos con hijos y cancelaciones cuando estén disponibles. Evaluar tablas de decisión, transiciones y casos de uso. Los casos deben utilizar datos desechables y describir claramente su preparación.\n\nNingún tipo de prueba es obligatorio por defecto. Justificar qué se evalúa, qué riesgo se aborda y cómo se decidirá si el resultado es satisfactorio. Señalar para revisión del equipo los riesgos relevantes que queden sin cobertura.",
    "status": {
      "name": "En curso",
      "statusCategory": {
        "name": "In Progress"
      }
    },
    "assignee": {
      "accountId": "712020:f80285fe-0020-4433-a221-382a514207e6",
      "displayName": "Alejandra Salinas Vega"
    },
    "reporter": {
      "accountId": "712020:f80285fe-0020-4433-a221-382a514207e6",
      "displayName": "Alejandra Salinas Vega"
    },
    "priority": {
      "name": "High"
    },
    "issuetype": {
      "id": "10017",
      "name": "Task"
    },
    "created": "2026-11-09T19:33:04.486-0400",
    "updated": "2026-11-11T00:51:48.779-0400",
    "labels": [],
    "subtasks": [],
    "comment": {
      "total": 0
    },
    "issuelinks": [],
    "customFields": {
      "Objetivo": {
        "id": "customfield_10076",
        "value": "Analizar los riesgos de las operaciones de eliminación y papelera y diseñar pruebas acordes con sus posibles consecuencias."
      },
      "Criterios de aceptación": {
        "id": "customfield_10077",
        "value": "- [ ] Se documentan las operaciones disponibles y su alcance conocido.\n- [ ] Se identifican las consecuencias potenciales sobre datos y jerarquías.\n- [ ] Se seleccionan y justifican los tipos de prueba.\n- [ ] Se contemplan diferentes estados y conjuntos de elementos según los objetivos elegidos.\n- [ ] Se documentan las técnicas y los escenarios positivos, negativos o alternativos pertinentes.\n- [ ] Los casos especifican datos desechables, estado inicial y resultados esperados.\n- [ ] Los casos se registran en TestLink y otro integrante los revisa.\n\n"
      },
      "Story point estimate": {
        "id": "customfield_10016",
        "value": 5
      },
      "Rank": {
        "id": "customfield_10019",
        "value": "0|hzzzzr:i"
      },
      "Development": {
        "id": "customfield_10000",
        "value": "{}"
      }
    }
  }
}

## Comentarios (0; isLast=true)
