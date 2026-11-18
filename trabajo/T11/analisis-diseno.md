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

Registro condicionado a diseño final y revisión independiente sin bloqueantes. Proyecto TL:Todo.ly, suite existente Todo.ly tests; entrada testcases, sin suites nuevas ni actualización de casos; nombres T11-NN, Importance individual, Manual, requerimiento/descripción/postcondiciones en Summary, Preconditions separado y pasos nativos. No hay IDs nuevos ni capturas de registro. La exportación real es `testlink-xml/todo-ly-tests.xml`; `testlink-xml/T11.xml` se extrae de ella después del registro verificado; el XML local propuesto no sustituye esa exportación.

## 8. Cobertura pendiente y límites

Pendientes: Cancel Editing; movimiento de completadas; regreso a raíz y reordenación; procedimiento observado de anidación y movimiento de pendientes; atributos que no estén visibles ni preparados; fronteras de nombres/profundidad. No se declara probada una restricción por `noWindowsAvailable`, `timeoutReached` o `cgWindowNotFound`.

El único dato temporal de T11 ya existente continúa en A: proyecto raíz vacío Prueba T11 - proyecto renombrado 1109. Los nombres y marcadores de las fichas siguientes son datos de diseño que todavía no se han creado. Los proyectos y tutoriales iniciales se conservan, y la limpieza de datos se realiza al terminar los tres tickets por instrucción del usuario.

## 9. Estado

Diseño provisional con cuatro fichas de resultado definido y dos candidatos pendientes; exploración adicional interrumpida por acceso visual. **Sin registro externo, sin publicación y sin ejecución formal.** No marcar estado ni revisión en Jira. La revisión y la ejecución comprobarán la implementación contra las reglas/oráculos declarados, sin asumir que una función documentada ya pasó la prueba.

## Fichas propuestas para TestLink

<!-- FICHAS_GENERADAS -->

### T11-01. Crear y seleccionar un proyecto raíz vacío

**Importancia:** **high**. Protege la creación y localización de un contenedor sin perder proyectos existentes.

**Requerimiento:** PEB-75 / T11. Un proyecto nuevo aparece una sola vez y puede seleccionarse conservando su identidad.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba A en un perfil dedicado.
3. No existe un proyecto llamado Prueba T11-01 - proyecto; proyectos iniciales de la cuenta conocidos.

**Descripción:** Comprobar creación, selección y conservación tras recarga de un proyecto propio vacío.

| Paso | Resultado esperado |
|---|---|
| 1. Consultar el árbol inicial, pulsar Add New Project e introducir Prueba T11-01 - proyecto; pulsar Add una vez. | Aparece una sola entrada con ese nombre en la raíz; los proyectos iniciales permanecen. |
| 2. Seleccionar Prueba T11-01 - proyecto. | El área principal muestra su nombre, There are no items to display y 0 Done Items. |
| 3. Recargar con F5 y volver a seleccionar el proyecto si fuera necesario. | La entrada raíz conserva el nombre y sigue vacía, sin duplicación; los proyectos iniciales permanecen. |
| 4. Conservar evidencia del árbol y del proyecto seleccionado. | La evidencia permite identificar el contenedor creado y su estado vacío. |

**Postcondiciones:** Proyecto raíz temporal vacío conservado para la limpieza final del lote; proyectos iniciales intactos.

---

### T11-02. Renombrar un proyecto propio y conservarlo tras recarga

**Importancia:** **medium**. Evita confundir o perder un proyecto al cambiar su nombre.

**Requerimiento:** PEB-75 / T11. Save aplica el nombre nuevo y conserva el proyecto y su contenido tras recarga.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba A en un perfil dedicado.
3. No existen los proyectos Prueba T11-02 - original ni Prueba T11-02 - renombrado.

**Descripción:** Comprobar el guardado del nombre sobre un proyecto temporal, sin imponer unicidad como regla del producto.

| Paso | Resultado esperado |
|---|---|
| 1. Crear una vez el proyecto raíz Prueba T11-02 - original mediante Add New Project y Add. | El árbol muestra el proyecto temporal una sola vez. |
| 2. Seleccionar el proyecto, abrir su menú Options y elegir Edit. | Aparece el campo editable con el nombre original y los controles Save y Cancel Editing. |
| 3. Introducir Prueba T11-02 - renombrado y pulsar el icono Save. | La entrada del proyecto y el título de la vista seleccionada muestran el nombre nuevo. |
| 4. Recargar con F5 y volver a seleccionar el proyecto. | El nombre renombrado persiste y no aparece una segunda entrada que represente la versión anterior. |
| 5. Conservar evidencia de nombre y ubicación. | Queda documentada la identidad del proyecto renombrado. |

**Postcondiciones:** Proyecto temporal conservado con el nombre renombrado para limpieza final; no se alteraron proyectos predeterminados.

---

### T11-04. Crear un subproyecto por arrastre y conservar su contenido

**Importancia:** **high**. Protege la relación padre/hijo de proyectos y los datos del contenedor movido.

**Requerimiento:** PEB-75 / T11. El arrastre documentado anida proyectos propios; la relación y los datos se conservan tras recarga.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba A en un perfil dedicado.
3. No existen Prueba T11-04 - padre ni Prueba T11-04 - hijo; no existen tareas con el marcador de este caso.

**Descripción:** Diseño basado en la función documentada de subproyectos y el criterio del equipo de conservar información; arrastre aún no comprobado en las cuentas.

| Paso | Resultado esperado |
|---|---|
| 1. Crear en la raíz Prueba T11-04 - padre y Prueba T11-04 - hijo mediante Add New Project / Add, una vez cada uno. | El árbol muestra ambos proyectos como raíces distintas. |
| 2. Seleccionar el hijo y crear una tarea pendiente Prueba T11-04 - dato del hijo mediante Add. | El hijo contiene el marcador con ese texto y estado pendiente. |
| 3. Arrastrar el manejador del proyecto hijo sobre el proyecto padre, usando los proyectos temporales del caso. | El hijo queda anidado bajo el padre según la función de subproyectos documentada; no desaparece ni se duplica ninguno. |
| 4. Seleccionar el hijo dentro del árbol. | Se mantiene el título del hijo y su marcador pendiente con el texto original; sigue asociado al hijo. |
| 5. Recargar con F5 y volver a seleccionar el hijo bajo el padre. | Se conserva la relación padre/hijo y el marcador con su contenido y estado. |
| 6. Conservar evidencia del árbol y de la vista del hijo. | La evidencia permite comprobar relación y datos. No se crean tareas padre/subtareas. |

**Postcondiciones:** Proyecto temporal padre con hijo y marcador pendiente conservados para limpieza final; proyectos predeterminados intactos. No incluye eliminación del subproyecto ni retorno a raíz.

---

### T11-05. Mover una tarea pendiente entre Home y Study conservando sus datos

**Importancia:** **high**. Detecta pérdida, duplicación, cambio de estado o ubicación incorrecta al mover.

**Requerimiento:** PEB-75 / T11. El movimiento documentado cambia de proyecto sin alterar el contenido ni el estado de la tarea.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba A en un perfil dedicado.
3. Home y Study son proyectos raíz independientes de la misma cuenta; su contenido inicial es conocido.
4. No existe una tarea llamada Prueba T11-05 - mover pendiente.

**Descripción:** Comprobar ida y vuelta entre proyectos y persistencia con F5. El contenido y estado son criterios del equipo; no se modifican fechas ni preferencias temporales.

| Paso | Resultado esperado |
|---|---|
| 1. Consultar Home y Study y registrar sus contenidos iniciales y cantidades visibles de pendientes. | Queda una referencia del contenido previo de cada proyecto, sin modificarlo. |
| 2. Seleccionar Home y crear Prueba T11-05 - mover pendiente mediante Add; registrar su estado y atributos que estén visibles. | Home contiene el nuevo marcador pendiente una sola vez; su texto y atributos visibles quedan como referencia. |
| 3. Arrastrar el pequeño manejador de esa tarea sobre Study en el árbol de proyectos, sin soltarla sobre otra tarea. | La tarea queda en Study, con el texto, estado pendiente y atributos visibles conservados; no se crea una subtarea. |
| 4. Seleccionar Study y después Home para comprobar origen y destino. | Study muestra una copia del marcador; Home deja de mostrarlo. Los datos previos de ambos proyectos permanecen. |
| 5. Recargar con F5 y consultar de nuevo Study y Home. | Se conserva la pertenencia a Study y la ausencia en Home, sin pérdida, duplicación ni cambio del contenido/estado. |
| 6. Seleccionar Study y arrastrar el mismo marcador de vuelta a Home; recargar y consultar Home. | El marcador vuelve a Home con el contenido y estado iniciales; Study recupera sus datos previos. |
| 7. Conservar evidencia de origen, destino y consulta posterior. | La evidencia permite reconocer el mismo marcador y los datos conservados. |

**Postcondiciones:** Marcador temporal pendiente en Home para limpieza final; Study y datos previos de ambos proyectos conservados. Atributos no visibles ni preparados quedan fuera de la comprobación, explícitamente pendientes de cobertura.

---

## Candidatos pendientes — no registrar todavía

---

### T11-03. Investigar Cancel Editing al renombrar un proyecto

**Importancia:** **medium**. Detecta aplicación de un nombre que se decidió descartar.

**Requerimiento:** PEB-75 / T11. Cancel Editing debería conservar el nombre anterior; efecto pendiente de contraste.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba A en un perfil dedicado.
3. No existe un proyecto llamado Prueba T11-03 - original.

**Descripción:** Candidato pendiente: el control fue observado, pero todavía no se contrastó su efecto al cancelar.

| Paso | Resultado esperado |
|---|---|
| 1. Crear y seleccionar el proyecto raíz Prueba T11-03 - original; abrir Options / Edit. | Se presenta el nombre original y Cancel Editing. |
| 2. Introducir Prueba T11-03 - descartado y pulsar Cancel Editing. | PENDIENTE: contrastar que el control descarta el valor editado y conserva el original antes de fijarlo como regla. |
| 3. Consultar el árbol y recargar con F5. | PENDIENTE: confirmar el nombre conservado y actualizar el resultado esperado con ese fundamento. |

**Postcondiciones:** Candidato fuera del registro propuesto; efecto de cancelación y estado posterior pendientes de contraste.

---

### T11-06. Investigar el movimiento de una tarea completada entre proyectos

**Importancia:** **high**. Protege el estado completado y la información si el producto permite esa operación.

**Requerimiento:** PEB-75 / T11. Disponibilidad y procedimiento para mover completadas pendientes de confirmar.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba A en un perfil dedicado.
3. Home y Study disponibles; no existe Prueba T11-06 - mover completada.

**Descripción:** Candidato pendiente: no se presupone que el mecanismo de pendientes permita mover completadas sin reactivarlas.

| Paso | Resultado esperado |
|---|---|
| 1. Crear Prueba T11-06 - mover completada en Home y marcar su checkbox para completar; abrir Done Items / See all. | El marcador aparece como completado en Home; la acción se usa solo como preparación. |
| 2. Consultar los controles o el arrastre ofrecidos para esa tarea completada, sin reactivarla. | PENDIENTE: comprobar si existe un mecanismo para moverla manteniendo su estado. |
| 3. Si la operación se confirma, documentar su procedimiento concreto, destino Study y contraste tras F5 antes de cerrar la ficha. | PENDIENTE: fijar el resultado sobre ubicación y conservación de completado con la regla y controles confirmados. |

**Postcondiciones:** Candidato fuera del registro propuesto; disponibilidad del movimiento y localización final pendientes. No se usa completar/reactivar como sustituto de mover completadas.
