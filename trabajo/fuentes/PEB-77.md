# PEB-77

Consulta de solo lectura: 2026-11-16. https://alesalve.atlassian.net/browse/PEB-77

{
  "appliedContentFormat": "html",
  "id": "10108",
  "key": "PEB-77",
  "fields": {
    "summary": "T13 — Analizar, diseñar y registrar pruebas de Inbox, Today y Next",
    "description": " Investigar las reglas de pertenencia a cada filtro y los efectos de modificar vencimiento, estado o proyecto. Considerar tareas sin fecha, vencidas, actuales, futuras y completadas, sin asumir su ubicación esperada.  Elegir y justificar pruebas funcionales, no funcionales o ambas. Los objetivos pueden incluir exactitud de clasificación, coherencia de información, comprensión de cada vista, accesibilidad de navegación, compatibilidad y rendimiento desde el cliente.  Seleccionar escenarios positivos, negativos y alternativos pertinentes. Considerar tablas de decisión, particiones y transiciones. Si se mide rendimiento, definir operación, volumen de datos, condiciones, repeticiones y criterio de evaluación.  Ningún tipo de prueba es obligatorio por defecto. Justificar qué se evalúa, qué riesgo se aborda y cómo se decidirá si el resultado es satisfactorio. Señalar para revisión del equipo los riesgos relevantes que queden sin cobertura. ",
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
    "created": "2026-11-09T19:33:45.506-0400",
    "updated": "2026-11-16T09:45:53.363-0400",
    "labels": [],
    "subtasks": [],
    "comment": {
      "total": 1
    },
    "issuelinks": [],
    "customFields": {
      "Objetivo": {
        "id": "customfield_10076",
        "value": " Analizar los riesgos de clasificación y consulta de tareas y diseñar pruebas apropiadas para las vistas Inbox, Today y Next. "
      },
      "Criterios de aceptación": {
        "id": "customfield_10077",
        "value": "    Se fundamentan las reglas de clasificación utilizadas en el diseño.    Se seleccionan y justifican los tipos de prueba.    Se consideran combinaciones relevantes de fecha, estado y ubicación.    Se explica cómo se abordará el riesgo de omitir o presentar incorrectamente tareas.    Se documentan las técnicas, escenarios y procedimientos seleccionados.    Los casos incluyen datos y referencias temporales reproducibles.    Los casos se registran en TestLink y otro integrante los revisa.  "
      },
      "Story point estimate": {
        "id": "customfield_10016",
        "value": 5
      },
      "Rank": {
        "id": "customfield_10019",
        "value": "0|i0000o:"
      },
      "Development": {
        "id": "customfield_10000",
        "value": "{}"
      }
    }
  }
}

## Comentarios (1; isLast=true)

### 10221 (2026-11-16T09:45:53.295-0400)

  Análisis y ejecución del ticket    PEB-77    — T13: Inbox, Today y Next    Contexto del trabajo   Se analizó el alcance del ticket, se exploró la SUT https://todo.ly/ con la cuenta de práctica ([CUENTA AJENA OMITIDA]) y se diseñaron los casos de prueba en formato XML para TestLink, usando la estructura solicitada:  Name / Requirement / Preconditions / Steps / Expected results .   Correcciones aplicadas al conjunto de 39 casos     Las precondiciones ya no describen acciones: solo indican el inicio de sesión con correo  [CUENTA AJENA OMITIDA]  y contraseña  [CREDENCIAL OMITIDA] , más el estado necesario (por ejemplo, que exista el proyecto Work).    La creación de tareas, proyectos y datos de prueba se movió a la sección  Pasos , explicada paso a paso.    Se reescribió la redacción para que cualquier persona pueda ejecutar el caso sin conocimientos técnicos: se indica dónde hacer clic, qué escribir, qué esperar y cómo limpiar los datos al final.    Los casos y sus pasos quedaron ordenados por tema y en secuencia lógica de ejecución ( TL-001  a  TL-039 ).     Entregable     Archivo  PRACTICA3 CALIDAD 2026 - Todo.ly (PEB-76, PEB-77, PEB-78.xml  con raíz  &lt;testcases&gt;  para  Import Test Cases  en TestLink.    También disponible  testsuite_todo_ly.xml  con raíz  &lt;testsuite&gt;  para  Import Test Suite .    XML validado: 39 casos, sin identificadores ni nombres duplicados, codificación  UTF-8  sin BOM.     Cobertura diseñada (13 casos:  TL-015 a TL-027 )     TL-015: una tarea nueva sin fecha aparece en Inbox.              TL-016: una tarea dentro de un proyecto no aparece en Inbox.                TL-017: al asignar la fecha de hoy la tarea pasa a Today.                TL-018: al asignar la fecha de mañana la tarea pasa a Next.                TL-019: una fecha pasada aparece en Today como vencida.                TL-020: al quitar la fecha la tarea vuelve a Inbox.                TL-021: mover una tarea de Inbox a un proyecto la saca de Inbox.                TL-022: completar una tarea la envía a Done Items y actualiza el contador.                TL-023: los contadores de los tres filtros coinciden con su contenido.                TL-024: mover una tarea entre Today y Next cambiando solo la fecha.                TL-025: coherencia entre la etiqueta de la tarea y el filtro donde aparece.                TL-026: el orden dentro de los filtros coincide con el criterio  Sort By .                TL-027: las tareas completadas dejan de contar en los filtros y pueden               reabrirse.     Exploración funcional realizada   Se verificó con datos reales la regla de pertenencia:  Inbox  agrupa las tareas sin proyecto y sin fecha;  Today  muestra las tareas que vencen hoy junto con las vencidas;  Next  muestra las tareas con fecha posterior a hoy. También se comprobó que al quitar la fecha la tarea regresa a Inbox, que al completarla desaparece de la lista principal y pasa a  Done Items , y que los contadores se recalculan. Los datos de prueba se eliminaron al finalizar.   Hallazgos y observaciones     Se observó que una tarea con fecha  solo de fecha  para mañana se etiqueta  Tomorrow  pero puede mostrarse en  Today ; se documentó en TL-025 como posible inconsistencia.    En los filtros, el orden visible no siempre coincidía con  Sort By: Due Date ; se dejó como verificación explícita en TL-026 para que el equipo lo confirme.    La papelera y los contadores respondieron correctamente durante la exploración, sin pérdida de tareas.     Estado   Los 13 casos quedaron redactados y ordenados para importar en TestLink. La ejecución formal en TestLink queda pendiente de registro, con los pasos y resultados esperados ya definidos.
