<!-- BORRADOR: publicar solo después de revisión y registro verificado. -->

# T11 / PEB-75 — Proyectos, subproyectos y movimientos

## 1. Análisis del área

Se cubren creación y selección de proyectos, cambio de nombre (guardar y cancelar), anidación de proyectos (raíz → subproyecto) y movimiento de tareas entre proyectos. Se exploró con la cuenta A en macOS/Chrome, perfil QA aislado; no constituye ejecución formal.

Observado en A (17/11): **Add New Project** muestra un campo de nombre y **Add** debajo de la lista; el proyecto creado apareció una sola vez al final de la raíz (la vista original quedó en Loading con la herramienta y la entrada se comprobó en una nueva carga de la página); al seleccionarlo se muestran su título, **There are no items to display** y **0 Done Items**. El panel abrevia con «…» los nombres largos. El icono de opciones del proyecto ofrece **Edit**, **Add item above**, **Add item below**, **Delete** y **Share**; Edit ofrece el icono **Save** y **Cancel Editing**; el nombre guardado persistió en una nueva carga. Las capturas muestran un asa de puntos delante de cada proyecto y tarea, y la jerarquía inicial **Work → Sub Project**, con el hijo sangrado y un triángulo de despliegue en el padre.

Observado en A (18/11): **Cancel Editing** descartó `Prueba T11 - nombre descartado 1816` y la entrada volvió a mostrar `Prueba T11 - proyecto renombrado 1109`. La recarga posterior dejó la ventana gris, con causa sin determinar: **la persistencia tras F5 de esa cancelación no está observada**; en T11-03 es criterio del equipo.

Documentación: la [portada oficial](https://todo.ly/) documenta el anidamiento de proyectos por arrastre y el movimiento de tareas entre proyectos. Las tareas de tutorial de la propia interfaz indican `Move items to different project using drag and drop. (Drag the small handler in front of the task)` y `Hover your mouse over a project or item and click the icon on the right side of the item for more options`. La guía §13 recoge el reporte previo expreso del usuario: las tareas de Done Items no se pueden arrastrar desde esa sección del proyecto. Este reporte no procede de un fallo de la herramienta y no demuestra que no exista otro mecanismo para mover completadas. La recuperación desde Recycle Bin es otra operación (guía §14, T08).

Fuera de alcance: tareas padre/subtareas (decisiones §5), eliminación de subproyectos (T08, casos 15–16), recuperación desde Recycle Bin (T08), orden de tareas y Sort By (T14), filtros (T13), colaboración/Share (decisiones §10).

## 2. Riesgos que orientan el diseño

Valoración cualitativa de diseño, no frecuencia medida: probabilidad P baja=1/media=2/alta=3; impacto I bajo=1/medio=2/alto=3; nivel P×I: alto=6–9, medio=3–4, bajo=1–2.

| Riesgo | Consecuencia para la persona usuaria | P y fundamento | I | Nivel | Casos |
|---|---|---|---|---|---|
| R1: mover una pendiente la pierde o la duplica | Tarea ausente o copias incoherentes entre proyectos | 2: cambio persistente entre dos contenedores, con ida y vuelta | 3 | 6, alto | T11-05 |
| R2: anidar pierde el proyecto o su relación | Proyecto inaccesible o bajo un padre incorrecto | 2: cambio de ubicación e interpretación del árbol | 3 | 6, alto | T11-04 |
| R3: un cambio de ubicación altera el contenido o el estado | Texto o estado distintos después de mover o recargar | 2: varios efectos deben conservarse en la transición | 3 | 6, alto | T11-04, 05, 06 |
| R4: crear/seleccionar duplica o identifica otro proyecto | Datos incorporados o consultados en el lugar equivocado | 2: coincidencia entre árbol, selección y título; Loading observado con la herramienta | 3 | 6, alto | T11-01 |
| R5: el nombre guardado no persiste o genera otra entrada | Proyecto difícil de identificar o duplicado | 2: edición, Save y consulta posterior | 2 | 4, medio | T11-02 |
| R6: Cancel Editing aplica o recupera el nombre descartado | Nombre modificado sin intención | 2: descarte observado; persistencia tras F5 sin observar | 2 | 4, medio | T11-03 |
| R7: el intento de arrastrar una completada desde Done Items la traslada parcialmente, la reactiva o la pierde | Completada fuera de lugar, reactivada o desaparecida | 1: restricción reportada por el equipo | 3 | 3, medio | T11-06 |
| R8: devolver un subproyecto a la raíz o reordenar la raíz lo pierde o lo coloca en otra posición | Proyecto desubicado o ausente | 2: procedimiento no confirmado | 3 | 6, alto | T11-07, pendiente |

## 3. Reglas, restricciones y dudas

| Regla o duda | Clasificación | Fundamento |
|---|---|---|
| Add New Project + Add crea una entrada raíz al final de Projects; al seleccionarla se muestran su título, There are no items to display y 0 Done Items | Comportamiento observado | `exploracion.md` 17/11; `evidencias/2026-11-17_T11_proyecto-creado-seleccionado.png` |
| La entrada nueva se muestra sin recargar, sin quedarse en Loading | Criterio del equipo | Con la herramienta, la vista quedó en Loading; se comprobó por nueva carga. T11-01 pide anotar el Loading sin repetir Add |
| El panel abrevia con «…» los nombres largos; el título completo se ve al seleccionar | Comportamiento observado | Capturas del 17/11 |
| El icono de opciones del proyecto ofrece Edit, Add item above, Add item below, Delete y Share; Edit ofrece Save y Cancel Editing | Comportamiento observado / Regla documentada en la interfaz | Lectura del menú (17/11) y tarea de tutorial `Hover your mouse over a project or item…` |
| Save aplica el nombre nuevo y este persiste en una nueva carga | Comportamiento observado | `evidencias/2026-11-17_T11_renombrado-persiste-consulta.png` |
| Cancel Editing descarta el nombre editado y vuelve a mostrar el original | Comportamiento observado | `exploracion.md` 18/11 (consulta AX) |
| El nombre original se conserva tras F5 después de Cancel Editing | Criterio del equipo | La recarga del 18/11 no cargó contenido (`evidencias/2026-11-18_T11_Cancel-tras-recarga-AX.txt`); no se declara observada |
| Un proyecto puede anidarse bajo otro por arrastre | Regla documentada | Portada oficial de Todo.ly |
| Un subproyecto se representa sangrado bajo su padre, con un triángulo de despliegue en el padre | Comportamiento observado | Jerarquía inicial Work → Sub Project en las capturas del 17/11 de A |
| Las tareas se mueven a otro proyecto arrastrando su asa y soltándola sobre el proyecto | Regla documentada | Portada oficial y tarea de tutorial `Move items to different project using drag and drop. (Drag the small handler in front of the task)` |
| Al mover o anidar se conservan texto, estado, unicidad y tareas preexistentes de origen y destino; la relación y la ubicación persisten tras F5 | Criterio del equipo | Criterio establecido expresamente por el equipo y riesgos de PEB-75 |
| Una tarea de Done Items no se puede arrastrar desde esa sección del proyecto | Regla documentada (reporte previo expreso del equipo) | Guía §13; no es una conclusión obtenida de un fallo de la herramienta |
| Existencia de otro mecanismo para mover completadas | Duda pendiente | No se concluye que no exista |
| Recuperación de completadas desde Recycle Bin | Fuera de alcance (T08) | Guía §14; la restricción de Done Items no se extiende a la papelera |
| Marcar el checkbox retira la tarea de pendientes; See all despliega las completadas | Regla documentada (guía, reglas de T07) | Guía §13; aquí se usa solo como preparación |
| Retorno de un subproyecto a la raíz y reordenación de proyectos | Duda pendiente | Procedimiento sin confirmar; T11-07 pendiente del reporte manual |
| Conservación de prioridad, vencimiento u otros atributos al mover | Duda pendiente | No se observaron en T11 los controles para prepararlos; queda separado y no bloquea la conservación de texto, estado y ubicación |
| Unicidad de nombres, longitud máxima, profundidad máxima y ciclos de anidación | Duda pendiente | Sin regla ni frontera; PEB-75 pide expresamente no imponerlas |
| Tareas padre/subtareas y eliminación de subproyectos | Fuera de alcance | Decisiones §5 y §9 |

## 4. Tipos de prueba y escenarios seleccionados

| Tipo | Objetivo y pertinencia | Procedimiento | Criterio observable |
|---|---|---|---|
| Funcional: creación, selección y nombre | Identificar y conservar el contenedor; R4–R6 | Projects, título del área principal, Edit/Save/Cancel Editing y F5 | Una sola entrada con el nombre esperado, en la raíz, que persiste tras F5 |
| Funcional: conservación al cambiar de ubicación | Evitar pérdida, duplicación, cambio de estado o ubicación incorrecta; R1–R3, R7 | Tarea marcadora con nombre único; contraste de origen y destino con tareas preexistentes consignadas; relación en el árbol; F5 | Destino y origen esperados; texto y checkbox conservados; tareas preexistentes sin cambios |

Positivos: crear y seleccionar un proyecto vacío (01), guardar un nombre (02), anidar bajo Home (04) y mover una pendiente Home ↔ Study (05). Alternativos: Cancel Editing (03) y retorno a la raíz/reordenación (07, pendiente). Negativo controlado: intentar arrastrar una completada desde Done Items, que no debe trasladarla, reactivarla ni perderla (06). No se diseñan negativos de nombre duplicado, ciclos o exceso de profundidad sin una regla. No se seleccionan pruebas no funcionales (facilidad de arrastre, accesibilidad, compatibilidad o tiempos de respuesta): no hay un procedimiento ni un criterio acordados, y los fallos de la herramienta no se atribuyen al producto. Queda señalado como riesgo sin cobertura.

## 5. Técnicas aplicadas y artefactos

Definiciones del original docente ya leídas en la fase 0: particiones pp. 8–19, transición de estados pp. 32–43 y casos de uso pp. 58–66. No se releyeron los PDF.

### 5.1 Flujos de casos de uso

**UC1 — Crear y seleccionar un proyecto.** Actor A: persona con sesión A.

| Paso | Actor | Sistema |
|---|---|---|
| 1 | Hace clic en Add New Project | Muestra el campo de nombre y Add |
| 2 | Escribe un nombre único y pulsa Add una vez | Incorpora una sola entrada al final de la raíz |
| 3 | Selecciona la entrada | Muestra el título, There are no items to display y 0 Done Items |
| 4 | Presiona F5 y vuelve a seleccionarla | Conserva entrada, ubicación y estado vacío |

Traza: flujo principal → **T11-01**. Creación en la raíz como preparación de UC2, UC3 y UC4.

**UC2 — Renombrar un proyecto.**

| Paso | Actor | Sistema |
|---|---|---|
| 1 | Selecciona el proyecto y abre el icono de opciones | Ofrece Edit, Add item above, Add item below, Delete y Share |
| 2 | Hace clic en Edit y sustituye el nombre | Muestra el campo editable con Save y Cancel Editing |
| 3a | Pulsa Save | Aplica el nombre nuevo en Projects |
| 3b (alternativa) | Pulsa Cancel Editing | Descarta la edición y muestra el nombre original |
| 4 | Presiona F5 y selecciona el proyecto | Conserva una sola entrada con el nombre resultante |

Traza: principal 3a → **T11-02**; alternativa 3b → **T11-03**.

**UC3 — Anidar un proyecto con contenido.**

| Paso | Actor | Sistema |
|---|---|---|
| 1 | Crea un proyecto raíz temporal y añade una tarea pendiente | Muestra el proyecto con la tarea, checkbox sin marcar |
| 2 | Arrastra el asa del proyecto y la suelta sobre Home | Muestra el proyecto sangrado bajo Home, con triángulo de despliegue |
| 3 | Selecciona el subproyecto | Muestra su título y su tarea pendiente |
| 4 | Presiona F5, consulta el subproyecto y Home | Conserva la relación, la tarea y las tareas iniciales de Home |
| A1 (alternativa) | Arrastra el subproyecto a la raíz entre Study y Personal | **Pendiente**: procedimiento sin confirmar |

Traza: principal → **T11-04**; A1 → **T11-07, pendiente**.

**UC4 — Mover una tarea entre proyectos.**

| Paso | Actor | Sistema |
|---|---|---|
| 1 | Consulta Study y Home y los compara con el registro | Muestra sus tareas iniciales |
| 2 | Crea una pendiente en Home | La muestra una sola vez, sin marcar |
| 3 | Arrastra su asa y la suelta sobre Study | La retira de Home |
| 4 | Consulta Study, recarga y consulta ambos proyectos | Muestra la tarea una sola vez en Study, pendiente, y conserva las preexistentes |
| 5 | La devuelve a Home y recarga | La muestra en Home; Study vuelve a su contenido inicial |
| A1 (alternativa) | Completa la tarea, despliega Done Items e intenta arrastrarla a Study | La tarea permanece completada en Home y no aparece en Study |

Traza: principal → **T11-05**; A1 → **T11-06**.

### 5.2 Transición de estados del proyecto

Estados: **—** sin proyecto; **R** proyecto raíz; **H** subproyecto bajo Home. Eventos: **E0** Add New Project + Add; **E1** soltar el asa sobre Home; **E2** F5 / nueva consulta; **E3** soltar el asa en la raíz entre Study y Personal. Formato docente: filas = estado actual, columnas = evento, celdas = estado siguiente. Fundamento: O = observación, D = documentación, C = criterio del equipo. «No aplica» indica un evento sin sentido en ese estado; «Pendiente» no significa que el producto lo prohíba.

| Estado actual | E0 | E1 | E2 | E3 |
|---|---|---|---|---|
| — | R (O) | No aplica | No aplica | No aplica |
| R | No aplica | H (D), datos conservados (C) | R (O) | R reordenado: Pendiente |
| H | No aplica | No ejercitado; sin fuente | H con relación y datos (C) | R: Pendiente |

| Secuencia | Caso | Fundamento |
|---|---|---|
| — →E0→ R →E2→ R | T11-01 | Creación y persistencia observadas; vista inmediata como criterio |
| R →(Edit/Save o Cancel Editing)→ R →E2→ R | T11-02, T11-03 | Cambio de nombre sin cambio de estado de ubicación |
| — →E0→ R →E1→ H →E2→ H | T11-04 | Anidación documentada y conservación como criterio |
| H →E3→ R →E2→ R | T11-07, pendiente | Procedimiento sin confirmar |

### 5.3 Particiones de equivalencia: situación de la tarea al arrastrarla

Se aplica solo porque la guía y la documentación fundamentan **tratamientos diferentes**. No se fuerza una tabla de decisión: hay una sola condición relevante.

| Variable | Clase | Tratamiento esperado | Fundamento | Representante | Caso |
|---|---|---|---|---|---|
| Situación de la tarea arrastrada hacia otro proyecto | Pendiente en la lista del proyecto | Se traslada al proyecto de destino con el mismo texto y estado | Portada, tutorial (D) y conservación (C) | Prueba T11-05 - mover pendiente, Home → Study → Home | T11-05 |
| Situación de la tarea arrastrada hacia otro proyecto | Completada en la sección Done Items | No se traslada desde esa sección; permanece completada en el origen | Guía §13, reporte del equipo (D) | Prueba T11-06 - completada en Done Items, Home → Study | T11-06 |
| — | Completada en Recycle Bin | Fuera de alcance | Guía §14, T08 | — | — |

### 5.4 Técnicas no aplicadas

No se aplican valores límite: no hay una frontera confirmada de longitud, profundidad ni cantidad. No se usa tabla de decisión para crear, guardar o cancelar (guía §7.4) ni para el movimiento, cuya única condición relevante ya se cubre con la partición anterior.

## 6. Lista resumida de casos

| Caso | Objetivo / riesgo | Fundamento de la técnica | Importancia | Situación |
|---|---|---|---|---|
| T11-01 Crear y seleccionar un proyecto raíz vacío | Identidad y unicidad del contenedor; R4 | UC1 principal; transición — →E0→ R →E2→ R | high | Listo para registro |
| T11-02 Renombrar con Save | Persistencia del nombre; R5 | UC2 principal | medium | Listo para registro |
| T11-03 Renombrar con Cancel Editing | Descarte del nombre; R6 | UC2 alternativa, descarte observado el 18/11; F5 como criterio | medium | Listo para registro |
| T11-04 Anidar bajo Home | Relación y contenido; R2, R3 | UC3 principal; transición R →E1→ H →E2→ H | high | Listo para registro; arrastre documentado, no observado |
| T11-05 Mover una pendiente Home ↔ Study | Pérdida, duplicación y ubicación; R1, R3 | UC4 principal; partición «pendiente» | high | Listo para registro; arrastre documentado, no observado |
| T11-06 Intento con una completada desde Done Items | Conservar proyecto y estado; R3, R7 | UC4 alternativa; partición «completada en Done Items» | high | Listo para registro; restricción reportada por el equipo |
| T11-07 Retorno a la raíz y reordenación | Ubicación y contenido del subproyecto; R8 | UC3 alternativa; transición H →E3→ R | high | Pendiente; no se registra |

## 7. Implementación en TestLink

Por registrar. Seis casos listos (T11-01 a T11-06) para la suite existente **Todo.ly tests** del proyecto TL:Todo.ly, como casos Manual con su Importance. **Sin IDs**, no publicados en Jira y sin ejecución formal. T11-07 no se importa.

## 8. Cobertura pendiente y límites

- **T11-07:** retorno de un subproyecto a la raíz y reordenación de proyectos, pendientes del reporte manual solicitado.
- **Atributos al mover:** la conservación de prioridad, vencimiento u otros atributos queda pendiente por separado, porque en T11 no se observaron controles para prepararlos. No bloquea la conservación de texto, estado y ubicación.
- **Mover completadas:** se desconoce si existe otro mecanismo además del arrastre desde Done Items. La recuperación desde Recycle Bin corresponde a T08.
- **Fronteras y validaciones de nombres:** unicidad, longitud, profundidad y ciclos quedan sin regla. No se diseñan casos sobre ellas.
- **Pruebas no funcionales:** facilidad del arrastre, accesibilidad de alternativas, compatibilidad y tiempos de respuesta quedan sin cobertura y se señalan al equipo.
- **Herramienta:** los errores `noWindowsAvailable` y `cgWindowNotFound` y la pantalla gris del 18/11 no demuestran restricciones ni fallos de Todo.ly.

Datos temporales actuales en A: el proyecto raíz `Prueba T11 - proyecto renombrado 1109`. Los nombres de las fichas son datos de diseño todavía no creados. Los datos del bloque manual, si el usuario lo realiza, se anotarán en `exploracion.md`. La limpieza se hace al terminar los tres tickets. El subproyecto temporal se retira mediante Delete únicamente como limpieza de datos propios, sin declarar ejecución de T08; sus tareas se retiran de Recycle Bin en el cierre. Las completadas de prueba se reactivan y eliminan según guía§17.

## 9. Estado

**Siete casos diseñados: seis listos para registro (T11-01 a T11-06) y uno pendiente (T11-07).** No hay casos registrados, publicados ni ejecutados formalmente, y la revisión de otro integrante sigue pendiente. Los arrastres de T11-04, 05 y 06 se basan en documentación y en el reporte del equipo, no en observación propia. La respuesta manual del 18/11 sigue pendiente.
