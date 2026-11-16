# PEB-73

Consulta de solo lectura: 2026-11-16. https://alesalve.atlassian.net/browse/PEB-73

{
  "appliedContentFormat": "markdown",
  "id": "10104",
  "key": "PEB-73",
  "fields": {
    "summary": "T09 — Analizar, diseñar y registrar pruebas de registro, acceso y sesión",
    "description": "Investigar el formulario de registro, Login, Remember Me, Logout y el comportamiento al cambiar de cuenta. Identificar validaciones y condiciones necesarias para utilizar cuentas propias de prueba.\n\nElegir y justificar pruebas funcionales, no funcionales o ambas. Pueden considerarse corrección del acceso, seguridad de sesión, separación entre cuentas, claridad de mensajes, accesibilidad de formularios, compatibilidad y tiempos de respuesta desde el cliente.\n\nDefinir escenarios positivos y negativos, como datos admitidos, entradas inválidas y combinaciones de credenciales. Considerar particiones, tablas de decisión, transiciones de sesión y límites confirmados. No asumir políticas de contraseñas, bloqueos o cantidades de intentos sin fundamento.\n\nNingún tipo de prueba es obligatorio por defecto. Justificar qué se evalúa, qué riesgo se aborda y cómo se decidirá si el resultado es satisfactorio. Señalar para revisión del equipo los riesgos relevantes que queden sin cobertura.",
    "status": {
      "name": "En curso",
      "statusCategory": {
        "name": "In Progress"
      }
    },
    "assignee": {
      "accountId": "712020:21f8f433-c031-4d37-9878-522c5983eb5e",
      "displayName": "RICARDO ANDRE CADIMA MERCADO"
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
    "created": "2026-11-09T19:33:18.626-0400",
    "updated": "2026-11-15T14:48:52.058-0400",
    "labels": [],
    "subtasks": [],
    "comment": {
      "total": 0
    },
    "issuelinks": [],
    "customFields": {
      "Objetivo": {
        "id": "customfield_10076",
        "value": "Analizar los riesgos del registro y manejo de sesiones y diseñar pruebas que evalúen los aspectos funcionales o no funcionales seleccionados."
      },
      "Criterios de aceptación": {
        "id": "customfield_10077",
        "value": "- [ ] Se documentan reglas, validaciones y dudas de registro y sesión.\n- [ ] Se seleccionan y justifican los tipos de prueba.\n- [ ] Se precisa la cobertura elegida para acceso, cierre, Remember Me y separación de cuentas.\n- [ ] Se identifican escenarios positivos y negativos relevantes.\n- [ ] Las pruebas de seguridad o rendimiento seleccionadas tienen objetivos y resultados esperados concretos.\n- [ ] Los casos utilizan cuentas controladas y documentan los datos necesarios sin exponer credenciales personales.\n- [ ] Los casos se registran en TestLink y otro integrante los revisa.\n\n"
      },
      "Story point estimate": {
        "id": "customfield_10016",
        "value": 5
      },
      "Rank": {
        "id": "customfield_10019",
        "value": "0|hzzzzr:2"
      },
      "Development": {
        "id": "customfield_10000",
        "value": "{}"
      }
    }
  }
}

## Comentarios (0; isLast=true)
