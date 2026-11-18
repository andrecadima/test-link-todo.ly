<!-- BORRADOR: pendiente revisión, OK, registro e IDs reales. -->

# T11 / PEB-75 — Proyectos, subproyectos y movimientos

Fecha: 17 de noviembre de 2026. **Diseño provisional: cuatro fichas con resultados definidos y dos candidatos pendientes.** No registrado en TestLink, no publicado en Jira y no ejecutado formalmente. El intento de retomar la exploración a las 23:47 UTC devolvió `cgWindowNotFound` con Chrome y Finder, también después de reiniciar CUA; se pidió recuperar la ventana. No se realizaron nuevas mutaciones de T11 durante ese bloqueo.

## 1. Análisis del área

Se cubren creación, selección, cambio de nombre y jerarquía de proyectos, y movimiento de tareas entre proyectos. La exploración anterior en A confirmó Add New Project, Add, selección del proyecto vacío, Options / Edit, Save, presencia de Cancel Editing y persistencia del nombre en una nueva consulta GET. La última sesión disponible era B en el perfil QA; no se usa el nombre del perfil como prueba de identidad ni se atribuyen a B las observaciones hechas con A.

La [portada oficial de Todo.ly](https://todo.ly/) documenta la creación de proyectos/subproyectos mediante arrastre de proyectos y el movimiento de tareas entre proyectos por arrastre. Se consultó como documentación pública para fundamentar resultados, sin iniciar sesión ni usar la API. Esa descripción no confirma que se puedan mover tareas completadas, un procedimiento para volver a raíz ni un límite finito de profundidad.

El criterio de conservación de contenido, atributos y relaciones procede del encargo y del alcance de PEB-75. Es el oráculo de diseño para esos efectos, distinto de afirmar que la implementación ya los cumple. T11-04/05 se apoyan en función documentada y criterio de conservación; su procedimiento no fue ejecutado todavía en las cuentas. Se utilizan Home y Study como raíces independientes para el movimiento de pendientes y proyectos temporales propios para anidar. No se usan tareas padre/subtareas ni se repite eliminación de subproyectos de T08.

## 2. Riesgos que orientan el diseño

Valoración cualitativa de diseño: P baja=1/media=2/alta=3; I bajo=1/medio=2/alto=3; nivel P×I, alto=6–9, medio=3–4 y bajo=1–2. No representa una frecuencia medida.

| Riesgo | Consecuencia | P y fundamento | I | Nivel | Casos |
|---|---|---|---|---|---|
| R1: movimiento pierde o duplica una tarea | Información ausente o copias incoherentes | 2: cambio persistente entre dos contenedores | 3 | 6, alto | T11-05; T11-06 pendiente |
| R2: anidación pierde el proyecto o su relación | Datos en contenedor o padre incorrectos | 2: cambio de ubicación e interpretación del árbol | 3 | 6, alto | T11-04 |
| R3: cambio de ubicación altera contenido/estado/atributos | Información distinta después de mover o recargar | 2: varios efectos deben conservarse durante la transición | 3 | 6, alto | T11-04/05; T11-06 pendiente |
| R4: creación/selección identifica otro proyecto | Datos consultados o incorporados en lugar equivocado | 2: coincidencia entre árbol, selección y título | 3 | 6, alto | T11-01 |
| R5: renombrar no persiste o genera otra entrada | Proyecto difícil de identificar o duplicado | 2: edición, Save y consulta posterior | 2 | 4, medio | T11-02 |
| R6: Cancel Editing aplica el cambio descartado | Nombre modificado sin intención de guardarlo | 2: alternativa de edición aún no contrastada | 2 | 4, medio | T11-03 pendiente |

## 3. Reglas, restricciones y dudas

| Regla / duda | Clasificación | Fundamento |
|---|---|---|
| Add New Project + Add crea una entrada raíz; selección del proyecto vacío muestra su nombre y ausencia de tareas | Comportamiento observado | `exploracion.md`, cuenta A, capturas de creación/selección |
| Options ofrece Edit y la edición ofrece Save y Cancel Editing | Comportamiento observado | Lectura de interfaz de A; no se confunde presencia de Cancel Editing con efecto comprobado |
| Save conserva el nombre nuevo en una consulta GET posterior | Comportamiento observado | Captura de nombre renombrado persistente |
| Cancel Editing descarta el nombre editado | Duda pendiente | Control visible, efecto aún sin contraste; T11-03 excluido del registro propuesto |
| Proyectos pueden anidarse por arrastre y tareas pueden moverse entre proyectos | Regla documentada | Portada oficial, apartados de proyectos y arrastre |
| Un movimiento conserva contenido, estado y atributos visibles; no duplica datos ni altera los previos de otro proyecto | Criterio del equipo | Encargo expreso del usuario y riesgos de PEB-75 |
| Una relación creada y los datos guardados se conservan tras F5 | Criterio del equipo | Encargo de persistencia y conservación; no se presenta F5 como ya ejecutado en T11 |
| Movimiento de una tarea completada sin reactivarla | Duda pendiente | La documentación pública no lo distingue y la interfaz concreta no se pudo consultar; T11-06 excluido |
| Reordenación de proyectos y regreso de subproyecto a raíz | Duda pendiente | Sin procedimiento concreto confirmado; no se inventa un destino o comando |
| Unicidad de nombres, longitud máxima y profundidad máxima | Duda pendiente | Sin frontera ni validación confirmadas; no se impone una restricción arbitraria |
| La eliminación de subproyectos y las tareas padre/subtareas quedan fuera | Regla documentada / decisión vigente | Decisiones §5/9 y encargo |

## 4. Tipos de prueba y escenarios

| Tipo | Objetivo | Procedimiento | Criterio observable |
|---|---|---|---|
| Funcional | Crear, localizar y renombrar contenedores propios | Árbol, título, contenido y consulta tras recarga | Una entrada identificable; nombre y datos coherentes y persistentes |
| Funcional de conservación | Evitar pérdida, duplicación o alteración al cambiar ubicación | Marcador único, origen/destino, relación padre/hijo y F5 | Contenido, estado y atributos visibles conservados; origen/destino y relación esperados |

Positivos: proyecto vacío nuevo, nombre guardado, anidación documentada y movimiento de una pendiente entre Home y Study con regreso. Alternativas pendientes: Cancel Editing y movimiento manteniendo completado. No se diseñan negativos de nombre duplicado, ciclos o exceso de profundidad sin una regla confirmada. Los problemas de facilidad de arrastre o accesibilidad no se convierten en pruebas no funcionales del producto a partir de fallos de la herramienta.

## 5. Técnicas aplicadas y artefactos

Definiciones ya recuperadas del original docente: transición de estados pp. 32–43 y casos de uso pp. 58–66. No se releen los PDF completos.

### 5.1 Flujos de casos de uso

**UC1 — Crear y seleccionar un proyecto.** A consulta el árbol, solicita Add New Project e informa el nombre; S incorpora una entrada; A la selecciona; S muestra ese contenedor vacío; A recarga; S conserva entrada y contenido. Deriva **T11-01**. Es un flujo observado de creación/selección más la comprobación de persistencia solicitada.

**UC2 — Renombrar proyecto.** A selecciona un proyecto temporal y usa Options / Edit; S ofrece nombre editable, Save y Cancel Editing; A guarda un nombre nuevo; S conserva el nombre al consultar nuevamente. Deriva **T11-02**. Alternativa Cancel Editing: **T11-03 pendiente**, porque la lectura anterior solo acreditó el control.

**UC3 — Anidar un proyecto con datos.** A crea padre e hijo temporales inicialmente raíz y un marcador pendiente dentro del hijo; A arrastra el proyecto hijo sobre el padre; S lo presenta bajo el padre; A selecciona el hijo y recarga; S conserva relación, marcador y estado. Deriva **T11-04**. El permiso de anidar es documentado; la conservación es criterio del equipo. El regreso a raíz no forma parte de este flujo confirmado.

**UC4 — Mover una pendiente.** A registra Home y Study iniciales; prepara un marcador pendiente en Home y su referencia; lo arrastra por su manejador sobre Study; S lo ubica en destino; A contrasta los dos proyectos y recarga; S conserva datos sin duplicación; A lo devuelve a Home y recarga. Deriva **T11-05**. La preparación de la tarea no vuelve a probar la creación de tareas de T06. La variante completada queda en **T11-06 pendiente**, sin suponer que deba reactivarse.

### 5.2 Transición de estados de proyecto

Estados: **R** proyecto raíz; **H** subproyecto bajo un padre identificado. Los mismos datos del proyecto deben conservarse al cambiar su ubicación. Matriz en formato docente: filas estado actual, columnas evento. D=documentación oficial; C=criterio de conservación del equipo; O=observación de consulta de raíz. `Pendiente` no representa prohibición del producto.

| Estado actual | Arrastrar raíz sobre padre propio | Consultar / recargar | Volver a raíz |
|---|---|---|---|
| R | H (D), conservando datos (C) | R (O/C) | — |
| H | Otro traslado no ejercitado | H, relación y datos conservados (C) | Pendiente de procedimiento |

| Secuencia generada | Caso | Fundamento |
|---|---|---|
| R con marcador → arrastre al padre → H → consulta/F5 → H | T11-04 | Anidación documentada y conservación solicitada |
| Proyecto raíz creado → selección → consulta/F5 → misma raíz | T11-01 | Creación/selección observadas y persistencia solicitada |

### 5.3 Técnicas no forzadas

No se aplica BVA: no hay frontera confirmada. La mención comercial a jerarquías amplias no proporciona un máximo finito para inventar casos en su borde. No se fuerza tabla de decisión sobre crear/guardar/cancelar. Pendiente/completada son condiciones relevantes para explorar, pero no se presenta una partición formal de tratamientos distintos mientras la operación sobre completadas siga desconocida.

## 6. Lista resumida de casos

| Caso | Objetivo / riesgo | Fundamento de la técnica | Importancia | Situación |
|---|---|---|---|---|
| T11-01 Crear/seleccionar raíz vacía | Identidad y persistencia; R4 | UC1 y permanencia del estado raíz | high | Resultado definido por observación y criterio de persistencia |
| T11-02 Renombrar y recargar | Nombre persistente; R5 | UC2 principal | medium | Resultado definido por observación y criterio de persistencia |
| T11-03 Cancel Editing | Descartar nombre; R6 | Alternativa candidata UC2 | medium | Pendiente, excluido |
| T11-04 Anidar y conservar datos | Relación y contenido; R2/R3 | UC3 y transición R→H→H | high | Resultado definido por documentación/criterio; procedimiento no ejecutado |
| T11-05 Mover pendiente Home↔Study | Evitar pérdida/duplicación; R1/R3 | UC4 de ida y vuelta con referencia y F5 | high | Resultado definido por documentación/criterio; procedimiento no ejecutado |
| T11-06 Mover completada | Mantener estado y ubicación; R1/R3 | Variante candidata UC4 | high | Pendiente, excluido |

## 7. Implementación propuesta en TestLink

Pendiente de revisión del diseño y OK. Proyecto TL:Todo.ly, suite T11; nombres T11-NN, Importance individual, Manual, requerimiento/descripción/postcondiciones en Summary, Preconditions separado y pasos nativos. No hay IDs nuevos ni capturas de registro. La exportación real `testlink-xml/T11.xml` se obtiene después del registro verificado; el XML local propuesto no sustituye esa exportación.

## 8. Cobertura pendiente y límites

Pendientes: Cancel Editing; movimiento de completadas; regreso a raíz y reordenación; procedimiento observado de anidación y movimiento de pendientes; atributos que no estén visibles ni preparados; fronteras de nombres/profundidad. No se declara probada una restricción por `noWindowsAvailable`, `timeoutReached` o `cgWindowNotFound`.

El único dato temporal de T11 ya existente continúa en A: proyecto raíz vacío Prueba T11 - proyecto renombrado 1109. Los nombres y marcadores de las fichas siguientes son datos de diseño que todavía no se han creado. Los proyectos y tutoriales iniciales se conservan, y la limpieza de datos se realiza al terminar los tres tickets por instrucción del usuario.

## 9. Estado

Diseño provisional con cuatro fichas de resultado definido y dos candidatos pendientes; exploración adicional interrumpida por acceso visual. **Sin registro externo, sin publicación y sin ejecución formal.** No marcar estado ni revisión en Jira. La revisión y la ejecución comprobarán la implementación contra las reglas/oráculos declarados, sin asumir que una función documentada ya pasó la prueba.
