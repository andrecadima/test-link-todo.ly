# T11 / PEB-75 — Proyectos, subproyectos y movimientos

Fecha:18/11/2026. Siete casos registrados TL-88 a TL-94,77 pasos;208 textos y campos nativos cotejados sin diferencias. Revisiones10/12 APTO, observaciones resueltas; revisión de integrante y ejecución formal pendientes. Evidencias manuales y de TestLink conservadas; comentario PEB-75/10228 publicado y leído por MCP.

## 1. Análisis del área

Se cubren creación y selección de proyectos, cambio de nombre (guardar y cancelar), anidación de proyectos (raíz → subproyecto) y movimiento de tareas entre proyectos. Se exploró con la cuenta A en macOS/Chrome, perfil QA aislado; no constituye ejecución formal.

Observado en A (17/11): **Add New Project** muestra un campo de nombre y **Add** debajo de la lista; el proyecto creado apareció una sola vez al final de la raíz (la vista original quedó en Loading con la herramienta y la entrada se comprobó en una nueva carga de la página); al seleccionarlo se muestran su título, **There are no items to display** y **0 Done Items**. El panel abrevia con «…» los nombres largos. El icono de opciones del proyecto ofrece **Edit**, **Add item above**, **Add item below**, **Delete** y **Share**; Edit ofrece el icono **Save** y **Cancel Editing**; el nombre guardado persistió en una nueva carga. Las capturas muestran un asa de puntos delante de cada proyecto y tarea, y la jerarquía inicial **Work → Sub Project**, con el hijo sangrado y un triángulo de despliegue en el padre.

Observado en A (18/11): **Cancel Editing** descartó `Prueba T11 - nombre descartado 1816` y la entrada volvió a mostrar `Prueba T11 - proyecto renombrado 1109`. La recarga posterior dejó la ventana gris, con causa sin determinar: **la persistencia tras F5 de esa cancelación no está observada**; en T11-03 es criterio del equipo.

Documentación: la [portada oficial](https://todo.ly/) documenta el anidamiento de proyectos por arrastre y el movimiento de tareas entre proyectos. Las tareas de tutorial de la propia interfaz indican `Move items to different project using drag and drop. (Drag the small handler in front of the task)` y `Hover your mouse over a project or item and click the icon on the right side of the item for more options`. La guía §13 recoge el reporte previo expreso del usuario: las tareas de Done Items no se pueden arrastrar desde esa sección del proyecto. Este reporte no procede de un fallo de la herramienta y no demuestra que no exista otro mecanismo para mover completadas. La recuperación desde Recycle Bin es otra operación (guía §14, T08).

Fuera de alcance: tareas padre/subtareas (decisiones §5), eliminación de subproyectos (T08, casos 15–16), recuperación desde Recycle Bin (T08), orden de tareas y Sort By (T14), filtros (T13), colaboración/Share (decisiones §10).

### Contraste manual del18/11

La pendiente Home→Study persistió tras F5 y quedó fuera de Home. Desde Done Items de Study la completada no se dejó arrastrar a Home, conforme al reporte previo de la guía; no se generaliza a mecanismos distintos. El usuario reporta anidación bajo Home tras F5; la captura4 muestra además una posición intermedia bajo Work/Sub Project. La última captura confirma el proyecto devuelto a raíz entre Study y Personal. T11-07 se completa con esa fuente; conservar su tarea es criterio del equipo, no una observación sobre el temporal vacío. No se repiten estos recorridos.

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
| R8: devolver un subproyecto a una posición raíz concreta lo pierde o lo coloca en otra posición | Proyecto desubicado o ausente | 2: cambio de ubicación con destino concreto; retorno confirmado por reporte y captura | 3 | 6, alto | T11-07 |

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
| Retorno del subproyecto a la raíz entre Study y Personal | Comportamiento observado por reporte y captura | manual-5-50528.png y confirmación del usuario; la captura4 es una posición intermedia bajo Work/Sub Project |
| Conservación de prioridad, vencimiento u otros atributos al mover | Duda pendiente | No se observaron en T11 los controles para prepararlos; queda separado y no bloquea la conservación de texto, estado y ubicación |
| Unicidad de nombres, longitud máxima, profundidad máxima y ciclos de anidación | Duda pendiente | Sin regla ni frontera; PEB-75 pide expresamente no imponerlas |
| Tareas padre/subtareas y eliminación de subproyectos | Fuera de alcance | Decisiones §5 y §9 |

## 4. Tipos de prueba y escenarios seleccionados

| Tipo | Objetivo y pertinencia | Procedimiento | Criterio observable |
|---|---|---|---|
| Funcional: creación, selección y nombre | Identificar y conservar el contenedor; R4–R6 | Projects, título del área principal, Edit/Save/Cancel Editing y F5 | Una sola entrada con el nombre esperado, en la raíz, que persiste tras F5 |
| Funcional: conservación al cambiar de ubicación | Evitar pérdida, duplicación, cambio de estado o ubicación incorrecta; R1–R3, R7 | Tarea marcadora con nombre único; contraste de origen y destino con tareas preexistentes consignadas; relación en el árbol; F5 | Destino y origen esperados; texto y checkbox conservados; tareas preexistentes sin cambios |

Positivos: crear y seleccionar un proyecto vacío (01), guardar un nombre (02), anidar bajo Home (04) y mover una pendiente Home ↔ Study (05). Alternativos: Cancel Editing (03) y retorno a raíz entre Study y Personal (07). Negativo controlado: intentar arrastrar una completada desde Done Items, que no debe trasladarla, reactivarla ni perderla (06). No se diseñan negativos de nombre duplicado, ciclos o exceso de profundidad sin una regla. No se seleccionan pruebas no funcionales (facilidad de arrastre, accesibilidad, compatibilidad o tiempos de respuesta): no hay un procedimiento ni un criterio acordados, y los fallos de la herramienta no se atribuyen al producto. Queda señalado como riesgo sin cobertura.

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
| A1 (alternativa) | Arrastra el subproyecto a la raíz entre Study y Personal | Devuelve el proyecto a la raíz entre Study y Personal (reporte y captura manual) |

Traza: principal → **T11-04**; A1 → **T11-07**.

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
| R | No aplica | H (D), datos conservados (C) | R (O) | No ejercitado como operación independiente |
| H | No aplica | No ejercitado; sin fuente | H con relación y datos (C) | R (observación manual); persistencia según reporte |

| Secuencia | Caso | Fundamento |
|---|---|---|
| — →E0→ R →E2→ R | T11-01 | Creación y persistencia observadas; vista inmediata como criterio |
| R →(Edit/Save o Cancel Editing)→ R →E2→ R | T11-02, T11-03 | Cambio de nombre sin cambio de estado de ubicación |
| — →E0→ R →E1→ H →E2→ H | T11-04 | Anidación documentada y conservación como criterio |
| H →E3→ R →E2→ R | T11-07 | Retorno y ubicación reportados, posición raíz visible en captura; conservación de tarea como criterio |

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
| T11-01 Crear y seleccionar un proyecto raíz vacío | Identidad y unicidad del contenedor; R4 | UC1 principal; transición — →E0→ R →E2→ R | high | Registrado y comparado: [TL-88](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-88) |
| T11-02 Renombrar con Save | Persistencia del nombre; R5 | UC2 principal | medium | Registrado y comparado: [TL-89](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-89) |
| T11-03 Renombrar con Cancel Editing | Descarte del nombre; R6 | UC2 alternativa, descarte observado el 18/11; F5 como criterio | medium | Registrado y comparado: [TL-90](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-90) |
| T11-04 Anidar bajo Home | Relación y contenido; R2, R3 | UC3 principal; transición R →E1→ H →E2→ H | high | Registrado y comparado: [TL-91](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-91) |
| T11-05 Mover una pendiente Home ↔ Study | Pérdida, duplicación y ubicación; R1, R3 | UC4 principal; partición «pendiente» | high | Registrado y comparado: [TL-92](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-92) |
| T11-06 Intento con una completada desde Done Items | Conservar proyecto y estado; R3, R7 | UC4 alternativa; partición «completada en Done Items» | high | Registrado y comparado: [TL-93](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-93) |
| T11-07 Retorno a raíz entre Study y Personal | Ubicación y contenido del subproyecto; R8 | UC3 alternativa; transición H →E3→ R | high | Registrado y comparado: [TL-94](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-94) |

## 7. Implementación en TestLink

Se registraron **siete casos,77 pasos**, **TL-88 a TL-94**, en TL:Todo.ly → suite existente **Todo.ly tests (id3)**. Seis se incorporaron primero y07 después de confirmar el retorno a raíz. Ausencia previa comprobada para ambos conjuntos; suite86 antes,92 tras seis y93 tras el adicional. Sin suites nuevas, reimportación de anteriores ni actualización de casos ajenos.

Se abrió cada ficha: **208 textos**, Importance y Manual cotejados sin diferencias. TestLink Draft, sin ejecución formal ni revisión de integrante. Revisiones independientes10/12 APTO con observaciones atendidas; no sustituyen a otro integrante. Capturas: árbol filtrado y TL-93/TL-94 abiertos. Las fichas completas permanecen en TestLink; los enlaces reales están en la lista. Exportación XML real después del último registro, sin presentar el XML de entrada como exportación.

## 8. Cobertura pendiente y límites

- El retorno a raíz y posición entre Study/Personal quedó confirmado. No se explora reordenación independiente adicional ni se atribuye profundidad máxima.
- **Atributos al mover:** la conservación de prioridad, vencimiento u otros atributos queda pendiente por separado, porque en T11 no se observaron controles para prepararlos. No bloquea la conservación de texto, estado y ubicación.
- **Mover completadas:** se desconoce si existe otro mecanismo además del arrastre desde Done Items. La recuperación desde Recycle Bin corresponde a T08.
- **Fronteras y validaciones de nombres:** unicidad, longitud, profundidad y ciclos quedan sin regla. No se diseñan casos sobre ellas.
- **Pruebas no funcionales:** facilidad del arrastre, accesibilidad de alternativas, compatibilidad y tiempos de respuesta quedan sin cobertura y se señalan al equipo.
- **Herramienta:** los errores `noWindowsAvailable` y `cgWindowNotFound` y la pantalla gris del 18/11 no demuestran restricciones ni fallos de Todo.ly.

Datos temporales actuales en A: el proyecto raíz `Prueba T11 - proyecto renombrado 1109`. Los nombres de las fichas son datos de diseño; los datos reales del bloque manual están inventariados en exploracion.md. El temporal real termina en la raíz entre Study y Personal. La limpieza se hace al terminar los tres tickets. El proyecto temporal se retira mediante Delete únicamente como limpieza de datos propios, sin declarar ejecución de T08; sus tareas se retiran de Recycle Bin en el cierre. Las completadas de prueba se reactivan y eliminan según guía§17.

## 9. Estado

**Diseñados y registrados en TestLink; pendiente de revisión por otro integrante.** Siete casos,77 pasos. La exploración manual se distingue de ejecución formal. No se cambia el estado ni se marca la revisión del integrante en Jira.

| Criterio de aceptación | Comprobación |
|---|---|
| Operaciones y restricciones | Creación, edición, anidación y arrastre documentados; dudas explícitas. |
| Tipos de prueba justificados | Funcional y conservación, vinculados a riesgos. |
| Cobertura creación, selección, jerarquías y movimientos | Siete casos; límites y atributos adicionales pendientes. |
| Pérdida, duplicación y ubicación incorrecta | Riesgos y resultados trazados en casos01–07. |
| Escenarios válidos, negativos y alternativos | Guardar/cancelar, mover pendiente y restricción de Done Items. |
| Origen, destino, datos y resultados | Fichas nominales con datos/control y resultado por paso. |
| Registro y revisión de integrante | Siete registrados y cotejados; revisión de integrante pendiente. |

## Fichas para TestLink — siete diseños

<!-- FICHAS_GENERADAS -->

### T11-01. Add New Project con nombre nuevo crea un proyecto raíz vacío que persiste tras F5

**Importancia:** **high**. Protege la creación y localización de un contenedor sin duplicarlo ni alterar los proyectos existentes.

**Requerimiento:** PEB-75 / T11. Add New Project crea una sola entrada raíz que puede seleccionarse vacía y se conserva tras recarga.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba (cuenta A).
3. Lista inicial de **Projects** de A consignada en el registro de ejecución.
4. Ausencia de proyectos con el nombre **Prueba T11-01 - proyecto vacío**.

**Descripción:** Validar que Add New Project con un nombre nuevo crea una sola entrada raíz al final de Projects, que al seleccionarla muestra un proyecto vacío y que tras F5 conserva nombre, ubicación y contenido sin alterar los proyectos iniciales.

| Paso | Resultado esperado |
|---|---|
| 1. Hacer clic en **Add New Project**, debajo de la lista de **Projects**. | Aparecen un campo de nombre y el botón **Add** debajo de la lista de **Projects**. |
| 2. Escribir **Prueba T11-01 - proyecto vacío** en el campo de nombre. | El campo muestra **Prueba T11-01 - proyecto vacío**. |
| 3. Hacer clic una sola vez en **Add**. | Sin recargar, al terminar la operación **Projects** muestra una sola entrada nueva que comienza por **Prueba T11-01** al final de la lista raíz; el panel puede abreviar el nombre con «…» y los proyectos iniciales permanecen. La vista abandona **Loading** según el criterio de actualización visual del equipo; una entrada visible únicamente tras recarga no satisface este paso. |
| 4. Hacer clic en la entrada nueva en **Projects**. | La entrada queda resaltada y el área principal muestra el título **Prueba T11-01 - proyecto vacío**, el texto **There are no items to display** y **0 Done Items**. |
| 5. Presionar **F5**. | La página se recarga y **Projects** muestra la entrada una sola vez en la raíz, sin sangría bajo otro proyecto; los proyectos iniciales del registro permanecen. |
| 6. Hacer clic en la entrada **Prueba T11-01 - proyecto vacío** en **Projects**. | El área principal muestra el título **Prueba T11-01 - proyecto vacío**, **There are no items to display** y **0 Done Items**. |
| 7. Tomar una captura de **Projects** y del proyecto seleccionado. | La captura muestra la entrada raíz única y el proyecto vacío, sin datos personales. |

**Postcondiciones:** Proyecto raíz vacío Prueba T11-01 - proyecto vacío conservado en A para la limpieza final del lote; proyectos iniciales sin cambios. Evidencia de la consulta posterior a F5.

---

### T11-02. Edit con Save en un proyecto aplica el nombre nuevo y lo conserva tras F5

**Importancia:** **medium**. Evita perder o confundir un proyecto al cambiar su nombre.

**Requerimiento:** PEB-75 / T11. Edit y Save aplican el nombre nuevo a un proyecto y, tras recarga, existe una sola entrada con ese nombre.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba (cuenta A).
3. Lista inicial de **Projects** de A consignada en el registro de ejecución.
4. Ausencia de proyectos con nombres que comiencen por **Prueba T11-02**.

**Descripción:** Validar que Edit con el icono Save aplica el nombre nuevo a un proyecto temporal y que, tras F5, Projects muestra una sola entrada con ese nombre y ninguna con el nombre anterior.

| Paso | Resultado esperado |
|---|---|
| 1. Hacer clic en **Add New Project**, debajo de la lista de **Projects**. | Aparecen un campo de nombre y el botón **Add**. |
| 2. Escribir **Prueba T11-02 - original** en el campo de nombre. | El campo muestra **Prueba T11-02 - original**. |
| 3. Hacer clic una sola vez en **Add**. | **Projects** muestra una sola entrada nueva que comienza por **Prueba T11-02** al final de la lista raíz. |
| 4. Hacer clic en la entrada nueva en **Projects**. | El área principal muestra el título **Prueba T11-02 - original** y **There are no items to display**. |
| 5. Situar el puntero sobre la entrada del proyecto en **Projects** y hacer clic en el icono de opciones de su lado derecho. | Se despliega un menú con **Edit**, **Add item above**, **Add item below**, **Delete** y **Share**. |
| 6. Hacer clic en **Edit**. | La entrada se convierte en un campo editable con **Prueba T11-02 - original**, el icono **Save** y **Cancel Editing**. |
| 7. Sustituir el contenido del campo por **Prueba T11-02 - renombrado**. | El campo muestra **Prueba T11-02 - renombrado**. |
| 8. Hacer clic en el icono **Save**. | Se cierra el campo editable y la entrada de **Projects** muestra el nombre nuevo (el panel puede abreviarlo con «…»). |
| 9. Presionar **F5**. | La página se recarga; **Projects** muestra una sola entrada del proyecto, con el nombre nuevo, y ninguna con **Prueba T11-02 - original**. |
| 10. Hacer clic en la entrada del proyecto renombrado en **Projects**. | El área principal muestra el título **Prueba T11-02 - renombrado** y **There are no items to display**. |
| 11. Tomar una captura de **Projects** y del proyecto seleccionado. | La captura muestra el nombre nuevo como entrada única. |

**Postcondiciones:** Proyecto raíz vacío Prueba T11-02 - renombrado conservado en A para la limpieza final del lote; proyectos iniciales sin cambios.

---

### T11-03. Cancel Editing en Edit de proyecto descarta el nombre nuevo y conserva el original

**Importancia:** **medium**. Evita aplicar un nombre que la persona decidió descartar.

**Requerimiento:** PEB-75 / T11. Cancel Editing descarta el nombre editado de un proyecto; el nombre original se conserva tras recarga.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba (cuenta A).
3. Lista inicial de **Projects** de A consignada en el registro de ejecución.
4. Ausencia de proyectos con nombres que comiencen por **Prueba T11-03**.

**Descripción:** Validar que, tras sustituir el nombre de un proyecto en Edit y pulsar Cancel Editing, Projects vuelve a mostrar el nombre original y lo conserva tras F5, sin entrada con el nombre descartado.

| Paso | Resultado esperado |
|---|---|
| 1. Hacer clic en **Add New Project**, debajo de la lista de **Projects**. | Aparecen un campo de nombre y el botón **Add**. |
| 2. Escribir **Prueba T11-03 - original** en el campo de nombre. | El campo muestra **Prueba T11-03 - original**. |
| 3. Hacer clic una sola vez en **Add**. | **Projects** muestra una sola entrada nueva que comienza por **Prueba T11-03** al final de la lista raíz. |
| 4. Hacer clic en la entrada nueva en **Projects**. | El área principal muestra el título **Prueba T11-03 - original**. |
| 5. Situar el puntero sobre la entrada del proyecto en **Projects** y hacer clic en el icono de opciones de su lado derecho. | Se despliega un menú con **Edit**, **Add item above**, **Add item below**, **Delete** y **Share**. |
| 6. Hacer clic en **Edit**. | La entrada se convierte en un campo editable con **Prueba T11-03 - original**, el icono **Save** y **Cancel Editing**. |
| 7. Sustituir el contenido del campo por **Prueba T11-03 - descartado**. | El campo muestra **Prueba T11-03 - descartado**. |
| 8. Hacer clic en **Cancel Editing**. | Se cierra el campo editable y la entrada de **Projects** vuelve a mostrar **Prueba T11-03 - original**. |
| 9. Presionar **F5**. | La página se recarga; **Projects** muestra una sola entrada con **Prueba T11-03 - original** y ninguna con **Prueba T11-03 - descartado**. |
| 10. Hacer clic en la entrada **Prueba T11-03 - original** en **Projects**. | El área principal muestra el título **Prueba T11-03 - original**. |
| 11. Tomar una captura de **Projects** y del proyecto seleccionado. | La captura muestra el nombre original como entrada única. |

**Postcondiciones:** Proyecto raíz vacío Prueba T11-03 - original conservado en A para la limpieza final del lote; proyectos iniciales sin cambios.

---

### T11-04. Arrastrar un proyecto temporal sobre Home lo anida como subproyecto con su tarea

**Importancia:** **high**. Protege la relación padre/hijo entre proyectos y los datos del proyecto que cambia de ubicación.

**Requerimiento:** PEB-75 / T11. Soltar un proyecto raíz sobre Home lo convierte en subproyecto de Home; la relación, su nombre y su tarea pendiente se conservan tras recarga.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba (cuenta A).
3. Lista inicial de **Projects** de A consignada en el registro de ejecución.
4. **Home** como proyecto raíz de A, con sus tareas pendientes iniciales consignadas en el registro de ejecución.
5. Ausencia de proyectos y tareas con nombres que comiencen por **Prueba T11-04**.

**Descripción:** Validar que arrastrar por su asa un proyecto temporal raíz con una tarea pendiente y soltarlo sobre Home lo presenta como subproyecto de Home y que, tras F5, se conservan relación, nombre y tarea pendiente sin alterar las tareas iniciales de Home.

| Paso | Resultado esperado |
|---|---|
| 1. Hacer clic en **Add New Project**, debajo de la lista de **Projects**. | Aparecen un campo de nombre y el botón **Add**. |
| 2. Escribir **Prueba T11-04 - subproyecto** en el campo de nombre. | El campo muestra **Prueba T11-04 - subproyecto**. |
| 3. Hacer clic una sola vez en **Add**. | **Projects** muestra una sola entrada nueva que comienza por **Prueba T11-04** al final de la lista raíz. |
| 4. Hacer clic en la entrada nueva en **Projects**. | El área principal muestra el título **Prueba T11-04 - subproyecto** y **There are no items to display**. |
| 5. Escribir **Prueba T11-04 - dato del subproyecto** en el campo **Add new Todo, type here...**. | El campo muestra **Prueba T11-04 - dato del subproyecto**. |
| 6. Hacer clic una sola vez en **Add**, a la derecha del campo. | La tarea **Prueba T11-04 - dato del subproyecto** aparece una sola vez en el proyecto, con su checkbox sin marcar. |
| 7. Arrastrar el asa de puntos situada delante de **Prueba T11-04 - subproyecto** en **Projects** y soltarla sobre **Home**. | La entrada deja de mostrarse al final de la lista raíz y aparece sangrada debajo de **Home**, que muestra un triángulo de despliegue; ningún proyecto desaparece ni se duplica. |
| 8. Hacer clic en **Prueba T11-04 - subproyecto**, debajo de **Home**. | El área principal muestra el título **Prueba T11-04 - subproyecto** y la tarea **Prueba T11-04 - dato del subproyecto** una sola vez, con su checkbox sin marcar. |
| 9. Presionar **F5**. | La página se recarga; **Home** conserva su triángulo de despliegue en **Projects**. |
| 10. Desplegar **Home** mediante su triángulo si aparece plegado. | **Prueba T11-04 - subproyecto** aparece sangrado bajo **Home**, una sola vez en **Projects**. |
| 11. Hacer clic en **Prueba T11-04 - subproyecto**, debajo de **Home**. | Se conservan el título y la tarea **Prueba T11-04 - dato del subproyecto** una sola vez, con el mismo texto y el checkbox sin marcar. |
| 12. Hacer clic en **Home** en **Projects**. | El área principal muestra el título **Home** y conserva sus tareas pendientes iniciales del registro. |
| 13. Hacer clic en **Prueba T11-04 - subproyecto**, debajo de **Home**. | El área principal muestra su título y **Prueba T11-04 - dato del subproyecto** pendiente. |
| 14. Tomar una captura de **Projects** y del subproyecto seleccionado. | La captura muestra la relación bajo **Home** y la tarea conservada. |

**Postcondiciones:** Subproyecto temporal Prueba T11-04 - subproyecto bajo Home, con su tarea pendiente, conservado para la limpieza final del lote; tareas iniciales de Home sin cambios. No incluye eliminación del subproyecto (T08) ni retorno a la raíz (T11-07).

---

### T11-05. Arrastrar una pendiente Home–Study conserva texto, estado y ubicación tras F5

**Importancia:** **high**. Detecta pérdida, duplicación, cambio de estado o ubicación incorrecta al mover una tarea entre proyectos.

**Requerimiento:** PEB-75 / T11. Arrastrar una tarea pendiente sobre otro proyecto la traslada a ese proyecto con el mismo texto y estado, sin duplicarla ni alterar las tareas preexistentes, también tras recarga.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba (cuenta A).
3. **Home** y **Study** como proyectos raíz de A, con sus tareas pendientes iniciales consignadas en el registro de ejecución.
4. Orden **Sort By: Order** en **Home** y **Study**.
5. Ausencia de tareas con el nombre **Prueba T11-05 - mover pendiente**.

**Descripción:** Validar que una tarea pendiente arrastrada por su asa desde Home hasta Study, y después de vuelta a Home, aparece una sola vez en el proyecto de destino con el mismo texto y su checkbox sin marcar, deja de estar en el origen y conserva esa ubicación tras F5, sin alterar las tareas preexistentes.

| Paso | Resultado esperado |
|---|---|
| 1. Hacer clic en **Study** en **Projects**. | El área principal muestra el título **Study** y sus tareas pendientes iniciales del registro. |
| 2. Hacer clic en **Home** en **Projects**. | El área principal muestra el título **Home** y sus tareas pendientes iniciales del registro. |
| 3. Escribir **Prueba T11-05 - mover pendiente** en el campo **Add new Todo, type here...**. | El campo muestra **Prueba T11-05 - mover pendiente**. |
| 4. Hacer clic una sola vez en **Add**, a la derecha del campo. | **Home** muestra **Prueba T11-05 - mover pendiente** una sola vez, con su checkbox sin marcar, junto a sus tareas iniciales. |
| 5. Arrastrar el asa de puntos situada delante de **Prueba T11-05 - mover pendiente** y soltarla sobre **Study** en **Projects**, no sobre otra tarea. | La tarea deja de mostrarse en **Home** y las tareas iniciales permanecen; la tarea movida no aparece sangrada bajo otra tarea. |
| 6. Hacer clic en **Study** en **Projects**. | **Study** muestra **Prueba T11-05 - mover pendiente** una sola vez, con el mismo texto y su checkbox sin marcar, junto a sus tareas iniciales. |
| 7. Presionar **F5**. | La página se recarga sin cerrar la sesión. |
| 8. Hacer clic en **Study** en **Projects**. | **Study** conserva **Prueba T11-05 - mover pendiente** una sola vez, pendiente y con el mismo texto, y sus tareas iniciales. |
| 9. Hacer clic en **Home** en **Projects**. | **Home** no muestra **Prueba T11-05 - mover pendiente** y conserva sus tareas iniciales. |
| 10. Hacer clic en **Study** en **Projects**. | **Study** muestra **Prueba T11-05 - mover pendiente**. |
| 11. Arrastrar el asa de puntos situada delante de **Prueba T11-05 - mover pendiente** y soltarla sobre **Home** en **Projects**, no sobre otra tarea. | La tarea deja de mostrarse en **Study**; las tareas iniciales de **Study** permanecen. |
| 12. Presionar **F5**. | La página se recarga sin cerrar la sesión. |
| 13. Hacer clic en **Home** en **Projects**. | **Home** muestra **Prueba T11-05 - mover pendiente** una sola vez, con el mismo texto y su checkbox sin marcar, junto a sus tareas iniciales. |
| 14. Hacer clic en **Study** en **Projects**. | **Study** muestra únicamente sus tareas iniciales del registro, sin **Prueba T11-05 - mover pendiente**. |
| 15. Hacer clic en **Home** en **Projects**. | **Home** muestra **Prueba T11-05 - mover pendiente** una sola vez, con el mismo texto y su checkbox sin marcar. |
| 16. Tomar una captura de **Home** con la tarea devuelta. | La captura permite reconocer la tarea con su texto y estado pendiente en **Home**. |

**Postcondiciones:** Tarea pendiente Prueba T11-05 - mover pendiente en Home para la limpieza final del lote; Study y tareas iniciales de ambos proyectos sin cambios. Prioridad, vencimiento y otros atributos no se preparan ni se comprueban en este caso.

---

### T11-06. Intento de arrastrar una completada desde Done Items conserva proyecto y estado

**Importancia:** **high**. Evita que una tarea completada se pierda, cambie de proyecto parcialmente o se reactive al intentar moverla desde su sección.

**Requerimiento:** PEB-75 / T11. Una tarea de la sección de completadas de un proyecto no se traslada al intentar arrastrarla a otro proyecto; permanece completada en su proyecto de origen, también tras recarga.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba (cuenta A).
3. **Home** y **Study** como proyectos raíz de A, con sus tareas pendientes y completadas iniciales consignadas en el registro de ejecución.
4. Orden **Sort By: Order** en **Home** y **Study**.
5. Ausencia de tareas con el nombre **Prueba T11-06 - completada en Done Items**.

**Descripción:** Validar que, al intentar arrastrar desde la sección de completadas de Home una tarea completada y soltarla sobre Study, la tarea permanece una sola vez entre las completadas de Home con su checkbox marcado, no aparece en Study ni en pendientes y conserva ese estado tras F5.

| Paso | Resultado esperado |
|---|---|
| 1. Hacer clic en **Home** en **Projects**. | El área principal muestra el título **Home** y sus tareas pendientes iniciales del registro. |
| 2. Escribir **Prueba T11-06 - completada en Done Items** en el campo **Add new Todo, type here...**. | El campo muestra **Prueba T11-06 - completada en Done Items**. |
| 3. Hacer clic una sola vez en **Add**, a la derecha del campo. | **Home** muestra la tarea una sola vez entre las pendientes, con su checkbox sin marcar. |
| 4. Marcar el checkbox de **Prueba T11-06 - completada en Done Items**. | La tarea deja de mostrarse entre las pendientes de **Home**. |
| 5. Desplegar las completadas de **Home** mediante **See all** si la sección está oculta. | Se despliega la sección de completadas de **Home** con **Prueba T11-06 - completada en Done Items** una sola vez y su checkbox marcado. |
| 6. Arrastrar **Prueba T11-06 - completada en Done Items** desde la sección de completadas de **Home** y soltarla sobre **Study** en **Projects**. | La tarea no se traslada: permanece una sola vez en las completadas de **Home**, con su checkbox marcado, y no aparece entre las pendientes. No se exige un mensaje, porque no se ha identificado ninguno. |
| 7. Hacer clic en **Study** en **Projects**. | **Study** muestra únicamente sus tareas pendientes iniciales, sin **Prueba T11-06 - completada en Done Items**. |
| 8. Desplegar las completadas de **Study** mediante **See all** si la sección está oculta. | Las completadas de **Study** coinciden con las iniciales del registro, sin **Prueba T11-06 - completada en Done Items**. |
| 9. Presionar **F5**. | La página se recarga sin cerrar la sesión. |
| 10. Hacer clic en **Home** en **Projects**. | **Home** muestra sus tareas pendientes iniciales, sin **Prueba T11-06 - completada en Done Items** entre ellas. |
| 11. Desplegar las completadas de **Home** mediante **See all** si la sección está oculta. | Las completadas de **Home** muestran **Prueba T11-06 - completada en Done Items** una sola vez, con el mismo texto y su checkbox marcado. |
| 12. Tomar una captura de las completadas de **Home**. | La captura muestra la tarea completada en **Home**. |

**Postcondiciones:** Tarea Prueba T11-06 - completada en Done Items completada en Home para la limpieza final del lote; Study y tareas iniciales sin cambios. La recuperación desde Recycle Bin no forma parte de este caso (T08).

---

### T11-07. Subproyecto movido a raíz entre Study y Personal conserva ubicación y tarea

**Importancia:** **high**. Protege el proyecto y su contenido al deshacer una anidación y devolverlo a una posición raíz concreta.

**Requerimiento:** PEB-75 / T11. Retorno de un subproyecto a raíz entre Study y Personal y ubicación tras F5 respaldados por el reporte manual; conservación de la tarea como criterio del equipo.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba (cuenta A).
3. Lista inicial de **Projects** de A consignada en el registro de ejecución.
4. Subproyecto temporal **Prueba T11-07 - retorno** debajo de **Home**, con la tarea pendiente **Prueba T11-07 - dato del retorno**.
5. Tareas pendientes iniciales de **Home** consignadas en el registro de ejecución.
6. **Home**, **Study** y **Personal** como proyectos raíz de A, con **Study** inmediatamente antes de **Personal**; **Home** desplegado en **Projects**.

**Descripción:** Validar que un subproyecto temporal arrastrado a la raíz entre Study y Personal aparece una sola vez en esa posición y conserva su nombre y tarea pendiente tras F5.

| Paso | Resultado esperado |
|---|---|
| 1. Arrastrar el asa de puntos de **Prueba T11-07 - retorno** desde debajo de **Home** y soltarla entre las entradas raíz **Study** y **Personal**. | **Prueba T11-07 - retorno** aparece una sola vez en la raíz, entre **Study** y **Personal**, alineado con ellos y sin sangría bajo **Home**. |
| 2. Presionar **F5**. | La lista **Projects** conserva **Prueba T11-07 - retorno** una sola vez en la raíz, entre **Study** y **Personal**. |
| 3. Hacer clic en **Prueba T11-07 - retorno** en **Projects**. | El área principal muestra el título **Prueba T11-07 - retorno** y **Prueba T11-07 - dato del retorno** una sola vez, con su checkbox sin marcar. |
| 4. Hacer clic en **Home** en **Projects**. | El área principal muestra **Home** con sus tareas iniciales del registro; **Prueba T11-07 - retorno** permanece en la raíz del árbol y no como hijo de **Home**. |
| 5. Hacer clic en **Prueba T11-07 - retorno** en **Projects**. | El área principal muestra el título **Prueba T11-07 - retorno** y **Prueba T11-07 - dato del retorno** una sola vez, con su checkbox sin marcar. |
| 6. Tomar una captura de **Projects** y del proyecto seleccionado. | La captura identifica el proyecto raíz entre **Study** y **Personal** y su tarea pendiente conservada. |

**Postcondiciones:** Proyecto temporal Prueba T11-07 - retorno en la raíz entre Study y Personal, con su tarea pendiente, conservado para la limpieza final del lote; proyectos y tareas iniciales sin cambios.
