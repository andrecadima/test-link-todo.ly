# Fase 0 — Contexto verificado

Fecha: 16 de noviembre de 2026. Estado: contexto leído; exploración de Todo.ly todavía no iniciada. Consultas Jira por MCP autenticado y TestLink por Chrome, sin editar registros.

## Fuentes y límites

Se leyeron completos AGENTS.md, decisiones-vigentes.md, guía y plantillas. Se leyeron los PDF originales locales: PlanPruebasTodo.ly (16 páginas), E Tecnicas de Black Box Testing 2025 (81 páginas) y 11P3_SIS312_BlackBoxTesting2026Nov (2 páginas). Se renderizaron las páginas con tablas/diagramas de técnicas y la página 9 del plan para contrastar la extracción.

Faltan los cuatro PDF siguientes, citados por material-clase/LEEME.md: Plantilla para Casos de Prueba y Ejemplos.pdf; Plan de Pruebas, Casos de Prueba y Fallas.pdf; Plantilla de Plan de Pruebas de Software.pdf; Plantilla para reporte de fallas.pdf. No se presume su contenido. El archivo E Tecnicas... es el original disponible de técnicas, con cinco técnicas explícitas en p. 7. La consigna exige XML de TestLink para el 18 de noviembre; tiene inconsistencias de fechas y número de sprint que no reemplazan las decisiones vigentes. El plan p. 9 contiene texto de hardware insertado en criterios de suspensión: no se reconstruye una regla omitida por inferencia.

El entorno disponible en esta sesión es macOS con Chrome; no se atribuyen observaciones a Windows ni Firefox. La configuración prevista en los casos puede ser Windows/Chrome, registrando al ejecutar las versiones reales.

## Tickets propios: alcance y criterios completos

### PEB-73 — T09 — Analizar, diseñar y registrar pruebas de registro, acceso y sesión

Enlace: https://alesalve.atlassian.net/browse/PEB-73

Estado: En curso. Responsable: RICARDO ANDRE CADIMA MERCADO. Comentarios: 0 (página final consultada).

Investigar el formulario de registro, Login, Remember Me, Logout y el comportamiento al cambiar de cuenta. Identificar validaciones y condiciones necesarias para utilizar cuentas propias de prueba.

Elegir y justificar pruebas funcionales, no funcionales o ambas. Pueden considerarse corrección del acceso, seguridad de sesión, separación entre cuentas, claridad de mensajes, accesibilidad de formularios, compatibilidad y tiempos de respuesta desde el cliente.

Definir escenarios positivos y negativos, como datos admitidos, entradas inválidas y combinaciones de credenciales. Considerar particiones, tablas de decisión, transiciones de sesión y límites confirmados. No asumir políticas de contraseñas, bloqueos o cantidades de intentos sin fundamento.

Ningún tipo de prueba es obligatorio por defecto. Justificar qué se evalúa, qué riesgo se aborda y cómo se decidirá si el resultado es satisfactorio. Señalar para revisión del equipo los riesgos relevantes que queden sin cobertura.

**Objetivo:** Analizar los riesgos del registro y manejo de sesiones y diseñar pruebas que evalúen los aspectos funcionales o no funcionales seleccionados.

**Criterios de aceptación:**

- [ ] Se documentan reglas, validaciones y dudas de registro y sesión.
- [ ] Se seleccionan y justifican los tipos de prueba.
- [ ] Se precisa la cobertura elegida para acceso, cierre, Remember Me y separación de cuentas.
- [ ] Se identifican escenarios positivos y negativos relevantes.
- [ ] Las pruebas de seguridad o rendimiento seleccionadas tienen objetivos y resultados esperados concretos.
- [ ] Los casos utilizan cuentas controladas y documentan los datos necesarios sin exponer credenciales personales.
- [ ] Los casos se registran en TestLink y otro integrante los revisa.



### PEB-74 — T10 — Analizar, diseñar y registrar pruebas de perfil y recuperación de acceso

Enlace: https://alesalve.atlassian.net/browse/PEB-74

Estado: En curso. Responsable: RICARDO ANDRE CADIMA MERCADO. Comentarios: 0 (página final consultada).

Investigar la modificación de nombre y correo, el cambio de contraseña, las acciones de guardado y cancelación y el proceso de recuperación mediante correo. La zona horaria se analizará en el ticket de configuración temporal.

Determinar si se realizarán pruebas funcionales, no funcionales o ambas. Considerar objetivos relacionados con consistencia de datos, seguridad de cuenta, comprensión de mensajes e instrucciones, accesibilidad de formularios, compatibilidad o tiempos de respuesta.

Diseñar escenarios positivos, negativos y alternativos según las reglas disponibles. Evaluar particiones, tablas de decisión, casos de uso y límites identificados. Preparar cuentas y buzones propios, sin asumir plazos de recuperación ni restricciones tomadas de ejemplos de clase.

Ningún tipo de prueba es obligatorio por defecto. Justificar qué se evalúa, qué riesgo se aborda y cómo se decidirá si el resultado es satisfactorio. Señalar para revisión del equipo los riesgos relevantes que queden sin cobertura.

**Objetivo:** Analizar los riesgos de modificar datos de cuenta y recuperar el acceso, y diseñar las pruebas que resulten pertinentes.

**Criterios de aceptación:**

- [ ] Se documentan reglas y restricciones de los procesos analizados.
- [ ] Se seleccionan y justifican los tipos de prueba.
- [ ] Se explica cómo se abordarán los riesgos de pérdida de acceso y modificación incorrecta de datos.
- [ ] Se contemplan cambios válidos, entradas inválidas y cancelaciones cuando correspondan.
- [ ] Se justifican las técnicas y procedimientos utilizados.
- [ ] Los casos especifican cuentas, buzones, condiciones y resultados esperados.
- [ ] Los casos se registran en TestLink y otro integrante los revisa.



### PEB-75 — T11 — Analizar, diseñar y registrar pruebas de proyectos y movimientos

Enlace: https://alesalve.atlassian.net/browse/PEB-75

Estado: En curso. Responsable: RICARDO ANDRE CADIMA MERCADO. Comentarios: 0 (página final consultada).

Investigar creación y selección de proyectos, organización de subproyectos y movimiento de tareas entre proyectos. Considerar proyectos vacíos, elementos con hijos y distintos contextos de origen y destino.

Elegir y justificar pruebas funcionales, no funcionales o ambas. Entre los objetivos posibles están conservación de información y relaciones, comprensión de la ubicación resultante, facilidad del arrastre, accesibilidad de las alternativas existentes, compatibilidad y respuesta de la interfaz.

Diseñar escenarios positivos, negativos y alternativos según las operaciones permitidas. Considerar particiones, tablas de decisión y casos de uso. No imponer unicidad de nombres ni restricciones de jerarquía que todavía no estén fundamentadas.

Ningún tipo de prueba es obligatorio por defecto. Justificar qué se evalúa, qué riesgo se aborda y cómo se decidirá si el resultado es satisfactorio. Señalar para revisión del equipo los riesgos relevantes que queden sin cobertura.

**Objetivo:** Analizar los riesgos de organización por proyectos y movimiento de tareas, y diseñar pruebas sobre los aspectos de calidad seleccionados.

**Criterios de aceptación:**

- [ ] Se documentan las operaciones disponibles y sus restricciones.
- [ ] Se seleccionan y justifican los tipos de prueba.
- [ ] Se explica la cobertura elegida para creación, selección, jerarquías y movimientos.
- [ ] Se consideran los riesgos de pérdida, duplicación o ubicación incorrecta.
- [ ] Se documentan escenarios válidos, inválidos o alternativos cuando sean pertinentes.
- [ ] Los casos precisan origen, destino, datos iniciales y resultados esperados.
- [ ] Los casos se registran en TestLink y otro integrante los revisa.



## Diferencias y decisiones que gobiernan

- T11 conserva la frase «elementos con hijos». Se informó al usuario antes de seguir: solo se cubrirán proyectos/subproyectos; las tareas padre/subtareas están excluidas por el super prompt y decisiones §5. No se modifica Jira para resolver esta diferencia.
- No se crean tickets de implementación separados (decisiones §2), aunque el plan lo describe.
- El usuario pidió combinar análisis y evidencia en los tres tickets y conservar el punto de control previo a escrituras externas.
- Ningún checklist de revisión ni estado de Jira se modificará por iniciativa del agente. La revisión corresponde a otro integrante.

## Modelos de Jira efectivamente encontrados

### T06 / PEB-70

Comentario 10223: https://alesalve.atlassian.net/browse/PEB-70?focusedCommentId=10223

Contiene «Análisis», una tabla Parte del área / Qué se analiza / Riesgo que orienta el diseño, una lista de 12 casos y un párrafo de técnicas: principalmente casos de uso, complementados por particiones y procedimientos manuales de seguridad/accesibilidad. No contiene tablas de particiones, valores límite, decisión o estados desarrolladas. El encargo actual exige esos artefactos cuando estén justificados; se agregan por instrucción del usuario, sin afirmar que ya estaban en T06.

La lista histórica incluye código al editar y teclado; la guía los retiró. El árbol real tiene nueve casos T06 (TL-41 a TL-49): Add, Enter, edición directa, menú Edit, clic fuera, Escape, atributos entre sesiones, vacío/espacios e incorporar archivos. No se asume que las 12 propuestas del comentario sean 12 registros reales.

### T12 / PEB-76

Comentario 10220: https://alesalve.atlassian.net/browse/PEB-76?focusedCommentId=10220

Estructura: contexto; correcciones al conjunto; entregable XML; cobertura con identificadores y capturas por caso; exploración funcional; hallazgos; estado. Describe 14 casos (nombres TL-001 a TL-014) de vencimientos y configuración temporal, dentro del conjunto de 39 con T13/T14. El texto final aún dice listos para importar/ejecutar, aunque en TestLink ya se ven los registros; se distingue el registro actual de la ejecución formal, que no se verificó.

Hay 14 imágenes en el listado de adjuntos de PEB-76. Las imágenes se identificaron por el comentario y metadatos; no se verificó individualmente el contenido de cada adjunto. La evidencia nueva incluirá IDs reales, enlaces directos, árbol de suite y un caso abierto, con datos propios y sin secretos.

## Organización real de TestLink

- Sitio: http://68.211.149.112/ ; TestLink 1.9.20 [DEV]. Sesión visible: admin.
- Proyecto: TL:Todo.ly (id 1), descripción Todo.ly tests proyect.
- Una suite: Todo.ly tests (id 3), total 48 casos. No existen aún suites por ticket en el árbol observado.
- T12–T14: 39 casos con prefijos en el nombre TL-001...TL-039; el identificador real del primero es TL-40, no TL-001. No confundir nombre importado con ID real.
- T06: IDs reales TL-41...TL-49, títulos sin prefijo T06.
- Se abrieron TL-41 (id interno 161) y TL-40 (id interno 83). Ambos tienen Requirement dentro de Summary y Preconditions separado. Ambos muestran Create step: no hay pasos nativos registrados. En T06 hay una tabla de pasos dentro de Summary; en T12 listas de pasos y resultados separados dentro de Summary. T06 contiene postcondiciones al final de Summary; el caso T12 incluye limpieza en la lista de pasos, sin campo separado de postcondiciones.
- TL-41: Draft, Importance High, Execution type Manual. TL-40: Ready for review, High, Manual; duración 10.00 min. No se alteraron los selectores ni Save.
- Para el trabajo nuevo: suites por T09/T10/T11 dentro de la organización existente, sin mover otros casos, títulos T0X-NN, ID automático real de TestLink y pasos nativos Step actions / Expected results. Esta adaptación obedece al super prompt.
- Enlaces verificables por IDs observados: http://68.211.149.112/lib/testcases/archiveData.php?edit=testcase&id=161 y http://68.211.149.112/lib/testcases/archiveData.php?edit=testcase&id=83 . Requieren sesión; enlaces finales se comprobarán después del registro.

### Mapeo de campos

| Campo del diseño | Campo TestLink y decisión |
|---|---|
| Título | Nombre del test case; ID automático separado del prefijo T0X-NN |
| Importancia | Importance High/Medium/Low; razón breve al inicio de Summary |
| Requerimiento | Summary, etiqueta Requerimiento: PEB-XX / T0X + comportamiento; así está en ambos ejemplos, sin vínculo formal de requisito observado |
| Descripción | Summary, etiqueta Descripción |
| Precondiciones | Preconditions; estado previo y configuración, cuentas genéricas A/B; sin datos reales |
| Paso / Resultado esperado | Steps nativos: Step actions / Expected results; cada fila Manual (adaptación explícita a lo solicitado) |
| Postcondiciones | Al final de Summary, etiqueta Postcondiciones; limpieza además en los pasos |
| — | Execution type Manual; revisión por otro integrante pendiente |

## Técnicas: definición y formato del docente

Fuente original: docs/material-clase/E Tecnicas de Black Box Testing 2025.pdf. Numeración física del PDF.

| Técnica | Definición y formato leído | Aplicación que se investigará |
|---|---|---|
| Particiones de equivalencia, pp. 8–19 | Dividir entradas en clases con comportamiento esperado similar y escoger un representante por grupo. Para rango, una válida y dos inválidas; para elemento de conjunto, válida/no válida. La regla determina la equivalencia, no el nombre del dato. | Campos de registro/perfil; no inventar clases sin tratamiento confirmado. |
| Valores límite de 2 valores, pp. 20 y 23–24 | La diapositiva enumera justo debajo del mínimo, mínimo, un nominal entre mínimo y máximo, máximo y justo encima del máximo. Con límites m/M y paso δ: m−δ, m, nominal, M, M+δ. «2 valores» se refiere al enfoque de fronteras; la lista total tiene cinco puntos. | Solo si se confirma frontera real y granularidad. |
| Valores límite de 3 valores, pp. 21 y 25–30 | Justo debajo, en y encima del mínimo; justo debajo, en y encima del máximo. m−δ, m, m+δ, M−δ, M, M+δ. El docente recomienda este enfoque para mayor riesgo. | No se copiarán las longitudes de contraseñas de ACME como límites de Todo.ly. |
| Transición de estados, pp. 32–43 | Sistema con estados finitos y eventos que provocan cambios; una misma entrada puede producir salidas diferentes según la historia. Tabla: filas estado actual, columnas evento, celdas estado siguiente (pp. 36, 40, 43); casos como secuencias de estados/eventos. | Sesión y Remember Me; raíz ↔ subproyecto. Añadir una tabla trazable de secuencias y casos sin reemplazar la matriz docente. |
| Tabla de decisión, pp. 45–56 | Condiciones arriba a la izquierda, acciones debajo; columnas de reglas a la derecha, con combinaciones T/F y acciones Execute. Cada columna genera un caso; reducción solo explicando condiciones irrelevantes. p. 53 usa X para indiferencia; p. 55 usa X para combinaciones imposibles: se declarará la leyenda de cada tabla. | Login: combinación de existencia/validez de cuenta y contraseña que corresponde a esa cuenta. No presentar una contraseña como válida fuera de su relación con una cuenta. |
| Casos de uso, pp. 58–66 | Interacción actor A / sistema S, escenario principal exitoso y extensiones/alternativas. No equivale automáticamente a un TC: relaciones 1:1, 1:N o N:1; derivar recorridos concretos. | Recuperación y movimientos, incluyendo persistencia y alternativas reales. |

Las pp. 69–73 distinguen positivos (entradas esperadas válidas) y negativos (condiciones inválidas controladas, sin bloqueo). Son enfoques de escenario; no reemplazan la técnica de derivación. Los tres intentos de ATM, cuatro intentos del ejemplo de acceso y 24 horas de recuperación son reglas de ejemplos del docente, no reglas de Todo.ly.

## Precondiciones acordadas

Decisiones §7 prevalece sobre la cuenta concreta de la guía y ejemplos de TestLink. Cada ficha será autocontenida: conexión, navegador/configuración real al ejecutar, sesión o ausencia de sesión según caso, cuenta gratuita de prueba A o dos cuentas A/B sin proyectos compartidos. Recuperación: buzón controlado por quien ejecuta. Se describe el estado inicial; la preparación activa de tareas/proyectos se desarrolla en pasos. No se incluyen correos ni contraseñas reales. Un caso de Login no exige sesión ya iniciada.

## Antecedentes y solapamientos

Se consultaron completos descripción, objetivo, criterios y comentarios de PEB-65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 77 y 78 por MCP. Todas las consultas de comentarios terminaron con isLast=true (máximo 3 comentarios por ticket, sin otra página). Copias locales de lectura en trabajo/fuentes/, con credenciales ajenas omitidas. No equivalen a nuevas validaciones de Todo.ly.

| Área / casos de referencia | Solapamiento y tratamiento |
|---|---|
| T01 PEB-65 | Entorno, persistencia y XML de TestLink; habilitación marcada lista, sin comentarios. No recrear infraestructura. |
| T02 PEB-66, comentarios 10215–10217 | Feature tour, registro, Work inicial, proyecto Uni, apertura de recuperación y Logout. Controles identificados no equivalen a efectos comprobados. Hay datos inconsistentes de versión en el relato: registrar el entorno propio. No usar Uni ni la cuenta ajena. |
| T03 PEB-67, comentario 10218 | Base: descripción oficial/interfaz/exploración. Persistencia e independencia son criterios del equipo. Límites de campos y reglas de cuenta siguen por investigar. |
| T05 PEB-69, comentario 10219 | Riesgos altos de acceso/recuperación, credenciales, separación y movimientos; medios de creación/selección. El comentario prioriza áreas pero no contiene matriz de probabilidad/impacto calculada: justificar valoraciones propias, no atribuirle cifras. |
| T06 PEB-70; TL-41...49 | Crear/editar tareas y conservar atributos entre sesiones. En T11 crear tareas solo como preparación; verificar integridad por el movimiento, no duplicar edición. En T09 consultar tras cambiar cuenta por aislamiento. |
| T07 PEB-71 | Completar/reactivar, contadores y consulta de completadas. No tiene comentarios y no aparece un conjunto T07 en el árbol. La guía conserva casos 1,2,3,4,9,10; esto es diseño de referencia, no registro confirmado. T11 solo investiga posibilidad de mover completadas y conservación del estado. |
| T08 PEB-72 | Papelera y eliminación; sin comentarios, sin conjunto identificado en árbol. Guía: casos 15–16 cubren cancelar/confirmar eliminación de subproyecto. No duplicarlos. Limpieza de datos propios no equivale a ejecución de T08. |
| T12 PEB-76; 14 casos | Vencimientos, zona horaria y fecha predeterminada. T10 los excluye aunque estén en Settings. T11 puede preparar un atributo representativo y comprobar que mover no lo altera; no validar reglas temporales. |
| T13 PEB-77; nombres TL-015...027 | Pertenencia a filtros, fechas/estado, contadores y movimiento Inbox→proyecto. T11 se concentra en proyectos origen/destino; no repite clasificación de filtros. |
| T14 PEB-78; nombres TL-028...039 | Prioridad, Sort By, empates, reordenar tareas y arrastre limitado en Priority/Due Date. T11 trata movimiento entre proyectos y reordenación de proyectos; no duplicar orden de tareas. |

## Estado y siguiente paso

Contexto preparado con cuatro PDF faltantes documentados y diferencias notificadas. No se inició sesión ni se modificó Todo.ly durante esta fase. No se escribieron registros en Jira/TestLink. La siguiente fase requiere aislar un perfil nuevo de Chrome, explorar registro y crear cuentas solo con los correos autorizados que estén libres. El punto de control posterior al diseño sigue obligatorio.
