# Registro de exploración — T11

- Fecha: 17 de noviembre de 2026; horas mostradas por la AUT.
- Cuenta: A, identidad confirmada en Settings. Entorno: macOS/Chrome del inventario inicial, perfil QA aislado.
- Estado: parcial, sin ejecución formal ni registro en TestLink.

| Hora | Acción y datos | Resultado observado | Clasificación | Evidencia |
|---|---|---|---|---|
| 11:09 AM | Pulsar Add New Project | Aparecen un campo de nombre y Add debajo de la lista de proyectos. | Comportamiento observado | Consulta de interfaz |
| 11:09–11:10 AM | Introducir `Prueba T11 - proyecto temporal 1109` y pulsar Add | La vista original permanece con Loading; una nueva consulta GET muestra el proyecto creado una sola vez en la raíz. No se repitió el envío. | Comportamiento observado | `evidencias/2026-11-17_T11_creacion-en-proceso.png`, `evidencias/2026-11-17_T11_proyecto-creado-seleccionado.png` |
| 11:10 AM | Seleccionar el proyecto temporal | El área principal muestra su nombre y `There are no items to display`, con 0 Done Items. | Comportamiento observado | Captura del proyecto seleccionado |
| 11:10 AM | Abrir Options del proyecto | Se ofrecen Edit, Add item above, Add item below, Delete, Share. La presencia de Share no implica que se pruebe colaboración. | Comportamiento observado | Lectura de menú |
| 11:10 AM | Edit y cambiar nombre a `Prueba T11 - proyecto renombrado 1109`; pulsar icono Save | Una nueva consulta GET conserva el nombre nuevo en la raíz. La edición ofrece también Cancel Editing. | Comportamiento observado | `evidencias/2026-11-17_T11_renombrado-persiste-consulta.png` |
| 11:11 AM | Intentar iniciar arrastre del proyecto temporal sobre Home | La herramienta devolvió `noWindowsAvailable`. La consulta siguiente conserva el proyecto en la raíz. No se considera probada una restricción de Todo.ly ni realizada la transición a subproyecto. | Duda pendiente por herramienta | Lectura posterior del árbol |

## Fronteras y dudas

No hay longitud ni profundidad máxima confirmadas. No se infiere unicidad de nombres. Faltan Cancel Editing, subproyectos, reordenación y movimientos de tareas entre proyectos, incluida la posibilidad real de mover completadas. No se prueba eliminación de subproyectos (T08).

## Datos temporales pendientes de limpieza

En A permanece el proyecto raíz vacío `Prueba T11 - proyecto renombrado 1109`. Home de A y Home de B conservan los marcadores de aislamiento de T09; no se usaron como tareas de movimiento ni se alteraron los tutoriales.

## Retoma para cierre acotado — acceso visual pendiente

El 17/11 a las 23:47 UTC se intentó retomar T11 después de preparar T09. Chrome devolvió `cgWindowNotFound`; el intento de recuperar foco mediante Finder dio el mismo error. El inventario confirmó que ambos procesos seguían ejecutándose, pero no proporcionó ventanas utilizables y el host DOM continuó no disponible. Se reinició la conexión CUA y se consultó Chrome por su bundle ID; persistió el error. Un reintento después del trabajo documental volvió a fallar. No se pulsaron controles ni se crearon datos adicionales de T11 durante esta retoma.

Se pidió al usuario dejar el Mac desbloqueado y Chrome visible en el perfil QA, sin introducir credenciales ni cambiar datos. La exploración de Cancel Editing, anidación y movimientos sigue pendiente de recuperar esa superficie. No se considera que el fallo de herramienta pruebe una restricción de Todo.ly.

Como fuente independiente de resultados esperados se consultó la [portada oficial de Todo.ly](https://todo.ly/), que documenta arrastre de proyectos para anidar y movimiento de tareas entre proyectos. Se clasifica como **Regla documentada**, sin presentarlo como comportamiento observado en A/B. El texto no confirma un procedimiento de retorno a raíz ni la posibilidad específica de mover completadas. El criterio de conservar contenido, estado, atributos y relaciones procede expresamente del usuario.

Se preparó un diseño provisional con T11-01/02 basados en observación previa y persistencia solicitada, T11-04/05 basados en documentación y conservación solicitada, y T11-03/06 como candidatos pendientes. Los datos de esas fichas todavía no se crearon. La consulta pública no inicia sesión ni utiliza la API de Todo.ly.

## Fuente confirmada del equipo sobre completadas

La guía vigente §13 documenta expresamente: el usuario confirmó que las tareas de Done Items no se pueden arrastrar desde esa sección del proyecto. Clasificación: **Regla documentada / reporte previo del equipo**, no conclusión derivada de una falla de nuestra herramienta. No prueba que no exista otro mecanismo de movimiento ni sustituye observarlo en A. La guía §14 distingue ese comportamiento de la recuperación de completadas desde Recycle Bin, que pertenece a T08 y no se duplica aquí.
