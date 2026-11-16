# PEB-78

Consulta de solo lectura: 2026-11-16. https://alesalve.atlassian.net/browse/PEB-78

{
  "appliedContentFormat": "html",
  "id": "10109",
  "key": "PEB-78",
  "fields": {
    "summary": "T14 — Analizar, diseñar y registrar pruebas de prioridades y ordenamiento",
    "description": " Investigar la precedencia de prioridades y el significado de Order, Priority y Due Date. Considerar empates, tareas sin vencimiento, cambios entre criterios y relación con el orden manual.  Determinar si se realizarán pruebas funcionales, no funcionales o ambas. Pueden evaluarse conservación de prioridades, corrección del orden, comprensión del criterio activo, distinción de prioridades sin depender únicamente del color, navegación accesible, compatibilidad y tiempos de actualización.  Diseñar escenarios positivos, negativos y alternativos que correspondan a las operaciones disponibles. Considerar particiones, tablas de decisión y casos de uso. No aplicar valores límite únicamente porque las prioridades estén numeradas.  Ningún tipo de prueba es obligatorio por defecto. Justificar qué se evalúa, qué riesgo se aborda y cómo se decidirá si el resultado es satisfactorio. Señalar para revisión del equipo los riesgos relevantes que queden sin cobertura. ",
    "status": {
      "name": "Listo",
      "statusCategory": {
        "name": "Done"
      }
    },
    "assignee": {
      "accountId": "712020:61ec0a79-45ec-48f5-badd-cd0f438b92a5",
      "displayName": "Camila Adriana Carvajal Gusman"
    },
    "reporter": {
      "accountId": "712020:f80285fe-0020-4433-a221-382a514207e6",
      "displayName": "Alejandra Salinas Vega"
    },
    "priority": {
      "name": "Medium"
    },
    "issuetype": {
      "id": "10017",
      "name": "Task"
    },
    "created": "2026-11-09T19:33:50.381-0400",
    "updated": "2026-11-16T09:50:46.873-0400",
    "labels": [],
    "subtasks": [],
    "comment": {
      "total": 1
    },
    "issuelinks": [],
    "customFields": {
      "Objetivo": {
        "id": "customfield_10076",
        "value": " Analizar los riesgos de asignación de prioridades y ordenamiento y diseñar pruebas sobre sus aspectos de calidad relevantes. "
      },
      "Criterios de aceptación": {
        "id": "customfield_10077",
        "value": "    Se documentan las reglas de prioridad y ordenamiento utilizadas.    Se seleccionan y justifican los tipos de prueba.    Se consideran prioridades diferentes, empates, ausencia de fecha y cambios de criterio.    Se explica la cobertura sobre conservación de información y comprensión del orden presentado.    Se documentan los escenarios y las técnicas o procedimientos seleccionados.    Las comprobaciones no funcionales elegidas tienen condiciones y criterios verificables.    Los casos se registran en TestLink y otro integrante los revisa.  "
      },
      "Story point estimate": {
        "id": "customfield_10016",
        "value": 5
      },
      "Rank": {
        "id": "customfield_10019",
        "value": "0|i0001d:"
      },
      "Development": {
        "id": "customfield_10000",
        "value": "{}"
      }
    }
  }
}

## Comentarios (1; isLast=true)

### 10222 (2026-11-16T09:50:46.838-0400)

  Análisis y ejecución del ticket    PEB-78    — T14: prioridades y ordenamiento    Contexto del trabajo   Se analizó el alcance del ticket, se exploró la SUT https://todo.ly/ con la cuenta de práctica ([CUENTA AJENA OMITIDA]) y se diseñaron los casos de prueba en formato XML para TestLink, usando la estructura solicitada:  Name / Requirement / Preconditions / Steps / Expected results .   Correcciones aplicadas al conjunto de 39 casos     Las precondiciones ya no describen acciones: solo indican el inicio de sesión con correo  [CUENTA AJENA OMITIDA]  y contraseña  [CREDENCIAL OMITIDA] , más el estado necesario (por ejemplo, que exista el proyecto Work).    La creación de tareas, proyectos y datos de prueba se movió a la sección  Pasos , explicada paso a paso.    Se reescribió la redacción para que cualquier persona pueda ejecutar el caso sin conocimientos técnicos: se indica dónde hacer clic, qué escribir, qué esperar y cómo limpiar los datos al final.    Los casos y sus pasos quedaron ordenados por tema y en secuencia lógica de ejecución (TL-001 a TL-039).     Entregable     Archivo  PRACTICA3 CALIDAD 2026 - Todo.ly (PEB-76, PEB-77, PEB-78.xml  con raíz  &lt;testcases&gt;  para  Import Test Cases  en TestLink.    También disponible  testsuite_todo_ly.xml  con raíz  &lt;testsuite&gt;  para  Import Test Suite .    XML validado: 39 casos, sin identificadores ni nombres duplicados, codificación  UTF-8  sin BOM.     Cobertura diseñada (12 casos:  TL-028  a  TL-0139 )       TL-028: asignar prioridad 1 y comprobar su color.                TL-029: distinguir las cuatro prioridades entre sí.                TL-030: ordenar por  Order  y reordenar arrastrando.                TL-031: ordenar por  Priority .                TL-032: estabilidad del orden cuando hay prioridades empatadas.                TL-033: ordenar por  Due Date .                TL-034: ubicación de las tareas sin vencimiento al ordenar por fecha.                TL-035: cambiar entre criterios y reconocer el criterio activo.              TL-036: el arrastre para reordenar solo funciona con  Order .                TL-037: identificar la prioridad sin depender únicamente del color.                TL-038: cambiar la prioridad con la lista ordenada por  Priority .                TL-039: la prioridad no altera el filtro donde aparece la tarea.               Exploración funcional realizada   Se verificó que existen cuatro niveles de prioridad con estos colores:  1 rojo, 2 azul, 3 verde y 4 negro ; los niveles 1, 2 y 3 se muestran en negrita y el 4 sin negrita. Se comprobó que  Sort By  ofrece tres criterios ( Order ,  Priority ,  Due Date ), que el criterio se conserva al recargar y que el arrastre para reordenar solo está disponible en  Order ; en los otros criterios la tarea solo puede moverse a otro proyecto. Los datos de prueba se eliminaron al finalizar.   Hallazgos y observaciones     La prioridad se reconoce en la lista principalmente por color y negrita; el número solo se ve al abrir el menú  Priority . Se documentó como riesgo de accesibilidad en TL-037.    El orden entre tareas con la misma prioridad se mantiene estable, pero conviene confirmarlo con varias recargas (TL-032).    Al cambiar la prioridad con la lista ordenada por  Priority , la tarea se reubica sin recargar; se dejó verificado en TL-038.     Estado   Los 12 casos quedaron redactados y ordenados para importar en TestLink. La ejecución formal en TestLink queda pendiente de registro, con los pasos y resultados esperados ya definidos.
