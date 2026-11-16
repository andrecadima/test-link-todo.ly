# PEB-67

Consulta de solo lectura: 2026-11-16. https://alesalve.atlassian.net/browse/PEB-67

{
  "appliedContentFormat": "markdown",
  "id": "10098",
  "key": "PEB-67",
  "fields": {
    "summary": "T03 — Definir la base y el enfoque de pruebas",
    "description": "Analizar la documentación disponible y los resultados exploratorios para identificar reglas, restricciones y dudas relevantes. Determinar las funcionalidades que requieren mayor atención y establecer una orientación inicial para su evaluación mediante pruebas manuales de caja negra. Documentar los supuestos pendientes sin presentarlos como requisitos confirmados.",
    "status": {
      "name": "Listo",
      "statusCategory": {
        "name": "Done"
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
    "created": "2026-11-09T13:26:58.188-0400",
    "updated": "2026-11-09T16:14:45.725-0400",
    "labels": [],
    "subtasks": [],
    "comment": {
      "total": 1
    },
    "issuelinks": [],
    "customFields": {
      "Objetivo": {
        "id": "customfield_10076",
        "value": "Establecer la información y los comportamientos que servirán de referencia para diseñar las pruebas, e identificar las funcionalidades prioritarias según su importancia para el usuario y el impacto de una falla."
      },
      "Criterios de aceptación": {
        "id": "customfield_10077",
        "value": "- [x] Se identifican las fuentes utilizadas como base de pruebas.\n- [x] Cada regla registrada tiene una fuente o está marcada como supuesto.\n- [x] Se documentan las restricciones y límites conocidos.\n- [x] Se identifican contradicciones y vacíos de información.\n- [x] Se investigan las dudas que afectan a las funciones de mayor riesgo.\n\n"
      },
      "Story point estimate": {
        "id": "customfield_10016",
        "value": 3
      },
      "Rank": {
        "id": "customfield_10019",
        "value": "0|hzzzzj:"
      },
      "Development": {
        "id": "customfield_10000",
        "value": "{}"
      }
    }
  }
}

## Comentarios (1; isLast=true)

### 10218 (2026-11-09T16:14:38.860-0400)

http://Todo.ly  permite registrar tareas y organizar su seguimiento mediante proyectos, subtareas, prioridades, fechas y estados. Su utilidad depende tanto de ejecutar estas operaciones como de conservar la información y presentar correctamente el trabajo pendiente.

La base inicial de pruebas se obtuvo de la descripción pública de la AUT, los textos de la interfaz, las capturas y las anotaciones del recorrido exploratorio.

**Reglas y comportamientos identificados**

| Funcionalidad | Información identificada | Fundamento |
| --- | --- | --- |
| Proyectos y jerarquías | La aplicación permite organizar tareas en proyectos y establecer jerarquías de proyectos y tareas. | Descripción oficial y estructura observada. |
| Edición de tareas | La documentación indica que Enter guarda la edición y Escape la cancela. | Página oficial; pendiente de comprobar en detalle. |
| Movimiento de tareas | La aplicación anuncia movimiento entre proyectos y organización mediante arrastrar y soltar. | Página oficial y textos de las tareas de ejemplo. |
| Inbox | La descripción indica que las tareas nuevas permanecen allí hasta asignarles fecha o moverlas a un proyecto. | Página oficial; falta precisar las combinaciones y excepciones. |
| Vencimiento | Las fechas intervienen en Today y permiten ordenar las tareas por vencimiento. | Página oficial; reglas temporales completas pendientes. |

Fuente: información de la landing page de [Todo.ly](https://todo.ly/).

De la interfaz también se identificó que:

* El menú de prioridad ofrece los valores **1, 2, 3 y 4**.
* **Sort By** permite seleccionar **Order, Priority y Due Date**. Durante la exploración se observaron cambios de orden al utilizar estas opciones.
* Existen controles para completar tareas, consultar completadas y eliminar elementos.
* **Notes: Shown/Hidden** corresponde a la visualización de notas; no representa una función para ocultar tareas.
* El formulario identifica la creación de notas como una capacidad Pro.

Estas observaciones describen opciones disponibles y recorridos concretos; no demuestran que todas sus reglas funcionen correctamente.

**Funcionalidades prioritarias para diseñar las pruebas**

La siguiente prioridad es una decisión del equipo basada en el propósito del producto y el impacto potencial de una falla.

| Funcionalidad | Prioridad | Justificación |
| --- | --- | --- |
| Crear, editar y conservar tareas | Alta | Es la función principal. La pérdida o alteración de información compromete el seguimiento del usuario. |
| Completar y eliminar tareas | Alta | Determina qué trabajo permanece pendiente y qué información se retira. Debe evaluarse el alcance de cada acción. |
| Proyectos, movimientos y subtareas | Alta | Permiten organizar el trabajo. Un movimiento incorrecto puede perder, duplicar o desubicar tareas. |
| Fechas y filtros | Alta | Ayudan a identificar qué requiere atención. Una clasificación incorrecta puede hacer que el usuario omita tareas. |
| Prioridad y ordenamiento | Alta | Orientan la selección del trabajo que debe atenderse primero. |
| Acceso y sesión | Alta | Son necesarios para acceder a los datos y mantener su asociación con la cuenta correspondiente. |
| Configuración | Media | Modifica la experiencia y el comportamiento de la aplicación. La zona horaria requiere atención especial por su relación con las fechas. |
| Impresión y preferencias visuales | Baja | Son funciones complementarias respecto al registro y seguimiento de tareas. |

**Enfoque inicial**

Las pruebas se concentrarán primero en las operaciones principales y sus efectos sobre los datos. Se considerarán recorridos correctos, entradas inválidas relevantes, cancelaciones y cambios de estado.

Como expectativa de calidad propuesta por el equipo, se comprobará que los cambios guardados permanezcan y que modificar, mover u ordenar una tarea no altere información ajena a la operación.

Los controles compartidos se evaluarán en contextos representativos, conservando variantes cuando cambien las reglas o el riesgo. La selección específica de técnicas y casos se desarrollará posteriormente.

**Restricciones y dudas pendientes**

No se han confirmado límites de longitud, cantidades máximas ni todas las reglas de validación. Tampoco se conoce completamente:

* La clasificación de tareas vencidas, futuras y completadas en los filtros.
* La precedencia de las prioridades y el tratamiento de empates.
* El efecto de completar, mover o eliminar una tarea con subtareas.
* El alcance de las acciones de eliminación y la recuperación disponible.
* El tratamiento de horas y zona horaria.

Hasta este punto no se ha demostrado una contradicción concreta; se han identificado principalmente vacíos de información. Estas dudas requieren investigación focalizada antes de fijar los resultados esperados de los casos afectados.
