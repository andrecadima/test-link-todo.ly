# PEB-69

Consulta de solo lectura: 2026-11-16. https://alesalve.atlassian.net/browse/PEB-69

{
  "appliedContentFormat": "markdown",
  "id": "10100",
  "key": "PEB-69",
  "fields": {
    "summary": "T05 -- Analizar los riesgos del producto y priorizar las áreas de prueba",
    "description": "Analizar las funcionalidades y los comportamientos identificados durante la exploración y la definición de la base de pruebas. Para cada área relevante, describir qué podría fallar y qué consecuencias tendría.\n\nEstimar cualitativamente la probabilidad de ocurrencia y el impacto de cada riesgo, utilizando niveles alto, medio y bajo y justificando las valoraciones con la información disponible. A partir de esta evaluación, establecer las áreas que deben recibir mayor atención durante el diseño y la ejecución de pruebas.",
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
    "created": "2026-11-09T18:10:10.801-0400",
    "updated": "2026-11-09T18:31:29.599-0400",
    "labels": [],
    "subtasks": [],
    "comment": {
      "total": 1
    },
    "issuelinks": [],
    "customFields": {
      "Objetivo": {
        "id": "customfield_10076",
        "value": "Identificar y evaluar los riesgos asociados a las funcionalidades de http://Todo.ly  para concentrar el esfuerzo de pruebas en las áreas cuya falla pueda afectar más al usuario."
      },
      "Criterios de aceptación": {
        "id": "customfield_10077",
        "value": "- [ ] Se identifican riesgos concretos relacionados con las funcionalidades de la aplicación.\n- [ ] Cada riesgo describe qué podría fallar y cuál sería la consecuencia para el usuario.\n- [ ] Se estima la probabilidad de ocurrencia utilizando una escala acordada por el equipo.\n- [ ] Se evalúa el impacto considerando pérdida de información, resultados incorrectos, interrupción del uso y posibilidades de recuperación.\n- [ ] Las valoraciones incluyen una justificación y señalan la incertidumbre cuando no existe evidencia suficiente.\n- [ ] Se establece un criterio consistente para combinar probabilidad e impacto y determinar el nivel de riesgo.\n- [ ] Se priorizan las áreas de prueba y se explica qué riesgos justifican esa prioridad.\n- [ ] Se indican los comportamientos que las pruebas deberán evaluar para abordar los riesgos prioritarios.\n\n- [ ] El equipo revisa la evaluación y registra los acuerdos obtenidos.\n\n**Resultado esperado**\n\nUna matriz que contenga:\n\n| Funcionalidad | Posible falla | Consecuencia | Probabilidad | Impacto | Nivel de riesgo | Orientación de pruebas |\n| --- | --- | --- | --- | --- | --- | --- |\n| Edición de tareas | El cambio aparenta guardarse, pero desaparece al recargar. | El usuario pierde información que consideraba conservada. | Por estimar | Por evaluar | Por determinar | Comprobar guardado y persistencia. |\n"
      },
      "Story point estimate": {
        "id": "customfield_10016",
        "value": 3
      },
      "Rank": {
        "id": "customfield_10019",
        "value": "0|hzzzzb:"
      },
      "Development": {
        "id": "customfield_10000",
        "value": "{}"
      }
    }
  }
}

## Comentarios (1; isLast=true)

### 10219 (2026-11-09T18:31:29.599-0400)

**Áreas de riesgo alto**

| Área | Qué podría fallar y cómo afectaría al usuario | Qué deben abordar las pruebas |
| --- | --- | --- |
| **Creación, edición y persistencia** | Una tarea parece guardada, pero desaparece, cambia de contenido o se duplica involuntariamente. | Contenido guardado, cancelación, cantidad de elementos y permanencia después de recargar y volver a acceder. |
| **Completar tareas** | Se completa otra tarea o se presenta como terminado trabajo pendiente. | Elemento afectado, estado resultante y coherencia entre pendientes y completadas. |
| **Eliminación individual y masiva** | Se eliminan pendientes, elementos de otros proyectos o más información de la prevista. | Alcance exacto de cada acción y conservación de los elementos ajenos a ella. |
| **Papelera** | Los elementos eliminados no pueden localizarse o una operación afecta información adicional. | Destino de los eliminados, acciones disponibles y diferencia entre eliminación recuperable y definitiva. |
| **Movimientos entre proyectos** | La tarea se pierde, se duplica o queda en una ubicación incorrecta. | Origen, destino, conservación de atributos y persistencia. |
| **Tareas y proyectos anidados** | Una acción sobre un padre modifica incorrectamente sus hijos. | Reglas de propagación al mover, completar o eliminar; conservación de relaciones. |
| **Vencimientos y filtros** | Se guarda otra fecha o una tarea urgente queda fuera de la vista correspondiente. | Fechas, horas, tareas sin fecha, vencidas, futuras y actualización de filtros. |
| **Zona horaria y fechas predeterminadas** | Un ajuste general cambia inesperadamente el seguimiento temporal de varias tareas. | Qué modifica la preferencia y cómo afecta los vencimientos y filtros. |
| **Registro, acceso y recuperación** | El usuario no puede utilizar o recuperar su cuenta. | Validaciones pertinentes, acceso posterior y recuperación con un buzón controlado. |
| **Perfil y credenciales** | Un cambio de correo o contraseña deja al usuario sin acceso o con datos inconsistentes. | Guardado, cancelación, acceso posterior y conservación de información. |
| **Separación entre cuentas** | Al cambiar de usuario aparecen o se modifican datos de otra cuenta. | Comprobaciones funcionales con dos cuentas propias y sin proyectos compartidos. |

**Áreas de riesgo medio**

| Área | Riesgo principal | Orientación |
| --- | --- | --- |
| **Prioridades** | El valor seleccionado no se conserva o su representación resulta incorrecta. | Aclarar significado de los niveles y comprobar asignación y conservación. |
| **Ordenamiento** | Las tareas se presentan en un orden que no corresponde al criterio seleccionado. | Investigar precedencia, empates, tareas sin fecha y relación con el orden manual. |
| **Completadas y contadores** | Los indicadores no representan los elementos reales. | Aclarar qué cuentan y contrastarlos después de operaciones relevantes. |
| **Creación y selección de proyectos** | El proyecto no aparece correctamente o la selección establece un contexto equivocado. | Nombre, presencia, selección y permanencia. |
