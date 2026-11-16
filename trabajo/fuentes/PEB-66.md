# PEB-66

Consulta de solo lectura: 2026-11-16. https://alesalve.atlassian.net/browse/PEB-66

{
  "appliedContentFormat": "html",
  "id": "10097",
  "key": "PEB-66",
  "fields": {
    "summary": "T02 — Realizar una exploración inicial de Todo.ly",
    "description": " Explorar la aplicación desde la perspectiva del usuario, siguiendo los lineamientos de clase. Definir los objetivos del recorrido, registrar las interacciones y elaborar un mapa funcional que sirva de base para la planificación. ",
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
    "created": "2026-11-09T13:26:54.743-0400",
    "updated": "2026-11-09T15:48:33.261-0400",
    "labels": [],
    "subtasks": [],
    "comment": {
      "total": 3
    },
    "issuelinks": [],
    "customFields": {
      "Objetivo": {
        "id": "customfield_10076",
        "value": " Comprender la aplicación e identificar sus funcionalidades, comportamientos y riesgos iniciales. "
      },
      "Criterios de aceptación": {
        "id": "customfield_10077",
        "value": "    Se identifica el objetivo, alcance y enfoque de la exploración.    Se registra el entorno, la fecha y las condiciones de acceso utilizadas.    Se recorren las áreas principales y se documentan las áreas no exploradas.    Se registran acciones, datos utilizados y resultados observados.    Se distingue entre controles identificados y comportamientos ejecutados.    Se elabora un mapa de funciones coherente con las observaciones.  "
      },
      "Story point estimate": {
        "id": "customfield_10016",
        "value": 5
      },
      "Rank": {
        "id": "customfield_10019",
        "value": "0|hzzzzr:"
      },
      "Development": {
        "id": "customfield_10000",
        "value": "{}"
      }
    }
  }
}

## Comentarios (3; isLast=true)

### 10215 (2026-11-09T14:23:31.189-0400)

 Realicé una prueba exploratoria guiada por funcionalidades (feature tour) de  http://Todo.ly  , con el objetivo de reconocer la aplicación, identificar sus opciones y construir el mapa funcional que servirá como base para el plan de pruebas.  Entorno y condiciones     Aplicación: versión web de  http://Todo.ly  .    Acceso: cuenta gratuita creada mediante Sign Up.    Entorno: Windows 11 y Google Chrome 156.0.8078.80.    Fecha de exploración: viernes 6 de noviembre.    Versiones del sistema operativo y navegador: no registradas durante esta exploración.     Áreas recorridas     Landing page, registro, formulario de Login y recuperación de contraseña.    Proyectos Work, Home, Study, Personal y Shopping List.    Sub Project y creación de proyectos.    Filtros Inbox, Today y Next.    Controles y menú de opciones de las tareas.    Settings: Profile, Default Settings, Share, Pro y Account.    Navegación superior, página de actualización a Pro y enlaces del footer.     Acciones y resultados comprobados     Completé el registro ingresando nombre, correo, contraseña y zona horaria; accedí a la aplicación con Work seleccionado.    Creé el proyecto  “Uni”  mediante Add New Project; apareció en la barra lateral y mostró los controles comunes de los proyectos.    Abrí Reset your Password; se desplegaron el campo de correo y el botón Send.    Accedí a See details y Upgrade to Pro; ambos llevaron a la misma página de actualización.    Seleccioné App; se abrió la página de  http://Todo.ly   para iPhone en App Store.    Ejecuté Logout; la sesión se cerró sin mostrar un mensaje.     Alcance de las observaciones   Distinguí entre  controles identificados  y  comportamientos ejecutados . Por ejemplo, identifiqué opciones de edición, notas, prioridad y eliminación de tareas, pero no comprobé individualmente todos sus efectos.  Quedaron pendientes de explorar en profundidad la papelera, las reglas de clasificación de los filtros, el ciclo completo de las tareas, las validaciones, la persistencia de cambios y el guardado de ajustes. Las funciones Pro y la eliminación completa de la cuenta no se ejecutaron.  Como resultado, elaboré un  mapa funcional jerárquico , con una caja por función y separación entre proyectos, subproyectos y subtareas. El mapa documenta el reconocimiento de la aplicación; no representa una validación completa de todas sus funciones.   Diagrama:   https://lucid.app/lucidchart/b23ff347-017f-4967-be36-f34ef3cfcc06/edit?viewport_loc=-10116%2C4960%2C28460%2C12266%2C.LmKmpU_~svs&amp;invitationId=inv_338949fa-843f-4f71-8871-ee506a9f616c

### 10216 (2026-11-09T14:24:50.573-0400)



### 10217 (2026-11-09T15:48:33.261-0400)

 Como complemento de la exploración, identifiqué que el menú  Sort By  corresponde al ordenamiento de tareas y ofrece tres opciones:  Sort by Order, Sort by Priority y Sort by Due Date . Durante el recorrido probé las tres opciones y observé cambios en el orden de presentación. La comprobación detallada de cada criterio queda para los casos de prueba.  También aclaré que  Notes: Shown / Hidden  controla la visualización de las notas asociadas a las tareas, no la visibilidad de las tareas completas.
