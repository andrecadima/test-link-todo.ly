# PEB-70

Consulta de solo lectura: 2026-11-16. https://alesalve.atlassian.net/browse/PEB-70

{
  "appliedContentFormat": "markdown",
  "id": "10101",
  "key": "PEB-70",
  "fields": {
    "summary": "T06 — Analizar, diseñar y registrar pruebas de creación y edición de tareas",
    "description": "Investigar los campos, controles y formas disponibles para crear, editar, guardar y cancelar modificaciones de tareas. Identificar las reglas conocidas, restricciones y dudas que afecten al diseño.\n\nDeterminar si se realizarán pruebas funcionales, no funcionales o ambas. La selección puede abordar corrección de operaciones, compatibilidad entre navegadores, facilidad de uso, accesibilidad de controles, tratamiento seguro de entradas o rendimiento percibido. Cada elección debe relacionarse con un objetivo y un riesgo concreto.\n\nIdentificar escenarios positivos, negativos y alternativos cuando correspondan. Considerar particiones de equivalencia, valores límite respaldados por restricciones y casos de uso. Para los objetivos no funcionales elegidos, definir procedimientos y criterios de evaluación adecuados.\n\nDesarrollar los casos y registrarlos en TestLink.\n\nNingún tipo de prueba es obligatorio por defecto. Justificar qué se evalúa, qué riesgo se aborda y cómo se decidirá si el resultado es satisfactorio. Señalar para revisión del equipo los riesgos relevantes que queden sin cobertura.",
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
    "created": "2026-11-09T19:32:56.233-0400",
    "updated": "2026-11-15T22:38:02.936-0400",
    "labels": [],
    "subtasks": [],
    "comment": {
      "total": 1
    },
    "issuelinks": [],
    "customFields": {
      "Objetivo": {
        "id": "customfield_10076",
        "value": "Analizar los riesgos de creación y edición de tareas y diseñar los casos de prueba pertinentes, justificando los tipos de prueba y las técnicas utilizadas."
      },
      "Criterios de aceptación": {
        "id": "customfield_10077",
        "value": "- [ ] Se documentan las reglas, restricciones y dudas relevantes.\n- [ ] Se justifica la elección de pruebas funcionales, no funcionales o ambas.\n- [ ] Se explica qué cobertura se dará al contenido, guardado, cancelación y conservación de cambios.\n- [ ] Se identifican escenarios positivos, negativos y alternativos pertinentes.\n- [ ] Se documentan las técnicas o procedimientos que originan los casos.\n- [ ] Los casos tienen precondiciones, datos, pasos, resultados esperados y configuración.\n- [ ] Los casos se registran en TestLink y otro integrante los revisa.\n\n"
      },
      "Story point estimate": {
        "id": "customfield_10016",
        "value": 5
      },
      "Rank": {
        "id": "customfield_10019",
        "value": "0|hzzzzt:"
      },
      "Development": {
        "id": "customfield_10000",
        "value": "{}"
      }
    }
  }
}

## Comentarios (1; isLast=true)

### 10223 (2026-11-15T22:38:02.936-0400)

**Análisis**
Una tarea podría aparentar estar guardada y después desaparecer, conservar otro contenido o duplicarse involuntariamente. También interesa comprobar que editar o cancelar afecte únicamente a la tarea seleccionada.
Para diseñar las pruebas, el área se descompone de la siguiente manera:

| Parte del área | Qué se analiza | Riesgo que orienta el diseño |
| --- | --- | --- |
| Creación | Contenido introducido, envío mediante Add y actualización de la lista. | Pérdida, alteración o duplicación involuntaria de una tarea. |
| Contexto inicial | Creación en un proyecto que ya contiene tareas y en uno vacío. | Que la primera tarea no se incorpore correctamente o que se alteren elementos existentes. |
| Entrada a la edición | Edición directa y acceso mediante el menú Edit. | Que una vía no permita editar o actúe sobre una tarea diferente. |
| Guardado | Confirmación con Enter y conservación del texto. | Que se guarde un valor diferente o se pierda la modificación. |
| Cancelación | Descartar un borrador válido, vacío o posterior a otro cambio guardado. | Que se conserve un cambio cancelado o se restaure una versión anterior incorrecta. |
| Integridad | Atributos de la tarea y otras tareas del proyecto. | Que cambiar el texto altere fechas, prioridades, estado o información ajena. |
| Persistencia | Lectura después de recargar y volver a iniciar sesión. | Que la información solo exista temporalmente en la interfaz. |
| Acceso mediante teclado | Alcanzar y operar los controles necesarios. | Que una persona que depende del teclado no pueda gestionar sus tareas. |

**Casos de prueba diseñados**

A partir del análisis de los riesgos de creación, edición y persistencia, se diseñaron los siguientes casos:

1. Crear una tarea mediante el botón Add.
2. Crear una tarea mediante Enter.
3. Editar directamente una tarea y guardar con Enter.
4. Acceder a la edición mediante la opción Edit del menú.
5. Guardar una edición al hacer clic fuera del campo.
6. Cancelar una modificación mediante Escape.
7. Conservar el contenido y los atributos de una tarea después de recargar y volver a iniciar sesión.
8. Evaluar la creación con el campo vacío y con espacios.
9. Comprobar el tratamiento de una entrada de código al crear una tarea.
10. Comprobar el tratamiento de una entrada de código al editar una tarea.
11. Comprobar la conservación y gestión de una tarea de gran extensión.
12. Crear y editar una tarea utilizando teclado.

El diseño utiliza principalmente casos de uso. Las comprobaciones de entradas se complementan con particiones de equivalencia cuando existe una regla que permita establecer el tratamiento esperado. Los objetivos de seguridad y accesibilidad incorporan procedimientos manuales específicos.
