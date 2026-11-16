# PEB-76

Consulta de solo lectura: 2026-11-16. https://alesalve.atlassian.net/browse/PEB-76

{
  "appliedContentFormat": "html",
  "id": "10107",
  "key": "PEB-76",
  "fields": {
    "summary": "T12 — Analizar, diseñar y registrar pruebas de vencimientos y configuración temporal",
    "description": " Investigar las formas de introducir vencimientos, formatos aceptados, precisión temporal, modificación o retiro de fechas y valores predeterminados. Analizar la relación con la zona horaria y la configuración de nuevas tareas.  Determinar si se diseñarán pruebas funcionales, no funcionales o ambas. Pueden evaluarse interpretación y conservación de fechas, claridad de su presentación, accesibilidad del selector, uso mediante teclado, compatibilidad entre navegadores y respuesta de los controles.  Definir escenarios positivos, negativos y alternativos basados en reglas identificadas. Considerar particiones, valores límite temporales, tablas de decisión y casos de uso. Las fechas pasadas o los campos sin hora no se considerarán inválidos automáticamente.  Ningún tipo de prueba es obligatorio por defecto. Justificar qué se evalúa, qué riesgo se aborda y cómo se decidirá si el resultado es satisfactorio. Señalar para revisión del equipo los riesgos relevantes que queden sin cobertura. ",
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
      "name": "High"
    },
    "issuetype": {
      "id": "10017",
      "name": "Task"
    },
    "created": "2026-11-09T19:33:41.546-0400",
    "updated": "2026-11-16T09:46:46.739-0400",
    "labels": [],
    "subtasks": [],
    "comment": {
      "total": 1
    },
    "issuelinks": [],
    "customFields": {
      "Objetivo": {
        "id": "customfield_10076",
        "value": " Analizar los riesgos asociados a fechas, horas y preferencias temporales y diseñar pruebas que permitan evaluar los aspectos seleccionados. "
      },
      "Criterios de aceptación": {
        "id": "customfield_10077",
        "value": "    Se documentan formatos, precisión, valores predeterminados y dudas.    Se seleccionan y justifican los tipos de prueba.    Se explica la cobertura elegida para vencimientos, zona horaria y configuración temporal.    Se contemplan datos válidos, inválidos y fronteras relevantes cuando correspondan.    Las técnicas y procedimientos están fundamentados.    Los casos especifican la fecha de referencia, hora, zona horaria y configuración necesarias.    Los casos se registran en TestLink y otro integrante los revisa.  "
      },
      "Story point estimate": {
        "id": "customfield_10016",
        "value": 5
      },
      "Rank": {
        "id": "customfield_10019",
        "value": "0|i0000b:"
      },
      "Development": {
        "id": "customfield_10000",
        "value": "{}"
      }
    }
  }
}

## Comentarios (1; isLast=true)

### 10220 (2026-11-16T09:46:46.706-0400)

  Análisis y ejecución del ticket    PEB-76    — T12: vencimientos y configuración temporal    Contexto del trabajo   Se analizó el alcance del ticket, se exploró la SUT https://todo.ly/ con la cuenta de práctica ([CUENTA AJENA OMITIDA]) y se diseñaron los casos de prueba en formato XML para TestLink, usando la estructura solicitada:  Name / Requirement / Preconditions / Steps / Expected results .   Correcciones aplicadas al conjunto de 39 casos     Las precondiciones ya no describen acciones: solo indican el inicio de sesión con correo  [CUENTA AJENA OMITIDA]  y contraseña  [CREDENCIAL OMITIDA] , más el estado necesario (por ejemplo, que exista el proyecto Work).    La creación de tareas, proyectos y datos de prueba se movió a la sección  Pasos , explicada paso a paso.    Se reescribió la redacción para que cualquier persona pueda ejecutar el caso sin conocimientos técnicos: se indica dónde hacer clic, qué escribir, qué esperar y cómo limpiar los datos al final.    Los casos y sus pasos quedaron ordenados por tema y en secuencia lógica de ejecución (TL-001 a TL-039).     Entregable     Archivo  PRACTICA3 CALIDAD 2026 - Todo.ly (PEB-76, PEB-77, PEB-78.xml  con raíz  &lt;testcases&gt;  para  Import Test Cases  en TestLink.    También disponible  testsuite_todo_ly.xml  con raíz  &lt;testsuite&gt;  para  Import Test Suite .    XML validado: 39 casos, sin identificadores ni nombres duplicados, codificación  UTF-8  sin BOM.     Cobertura diseñada (14 casos:  TL-001 a TL-014 )     TL-001: asignar un vencimiento con fecha y hora.            TL-002: interpretar la palabra  today .              TL-003: interpretar la palabra  tomorrow . TL-002                TL-004: usar el nombre de un día de la semana ( Friday ).                TL-005: modificar un vencimiento ya guardado y ver el cambio de filtro.                TL-006: quitar la fecha y volver a Inbox.                TL-007: aceptar una fecha pasada y marcarla como vencida.                TL-008: límites entre hoy 23:59 y mañana 00:00.                TL-009: postergar 1 día y 1 semana conservando la hora.                TL-010: fecha sin hora y hora por defecto.                TL-011: rechazar fechas inválidas.                TL-012: vencimiento por defecto de tareas nuevas ( New Task Due Date ).                TL-013: mostrar el año cuando la fecha es de otro año.                TL-014: coherencia con la zona horaria del perfil.               Exploración funcional realizada   Se inició sesión en la SUT y se crearon tareas de prueba con distintos vencimientos para verificar las reglas antes de redactar los casos. Se confirmó que la aplicación interpreta  today ,  tomorrow ,  yesterday  y nombres de días, asignando las  10:00 AM  cuando no se indica hora; que acepta fechas pasadas y las muestra como  1 day overdue ; que  Postpone  conserva la hora y suma días o semanas; y que una fecha de otro año se muestra con el año. Todos los datos creados se eliminaron al terminar y la cuenta quedó limpia.   Hallazgos y observaciones     Una fecha  solo de fecha  para mañana (sin hora) se etiqueta  Tomorrow  pero puede aparecer en  Today : se dejó documentado en el caso TL-010/TL-025 para revisión del equipo.    Un valor de zona horaria fuera de la lista puede romper el renderizado y el inicio de sesión (HTTP 500). Se restauró la zona de la cuenta de inmediato y se recomienda validar ese campo en el servidor.    Los formatos de fecha se interpretan en inglés y la hora por defecto es las 10:00 AM; conviene que la interfaz lo indique al usuario.     Estado   Los 14 casos quedaron redactados, ordenados y listos para importar en TestLink y ejecutar. La ejecución formal en TestLink queda pendiente de registro por parte del tester, con los pasos y resultados esperados ya definidos.
