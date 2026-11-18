# Respuesta al encargo 10 — Revisión independiente de T11

Fecha: 18/11/2026. Agente: Claude (revisión). No usé navegador, Jira, TestLink ni git. No leí `.secrets/`, `revision-testlink/` ni los PDF. Solo escribí este archivo y no modifiqué el diseño.

Esta revisión no sustituye la revisión de otro integrante ni equivale a una ejecución formal.

## Fuentes leídas

AGENTS.md, decisiones-vigentes.md (§1–15), guía §1–19 (incluidas §11–15, §17 y §19), las plantillas `caso-testlink.md` y `comentario-jira.md`, `00-contexto.md`, `trabajo/fuentes/PEB-75.md`, `T11/exploracion.md`, `analisis-diseno.md`, `casos.json`, `casos-listos.json`, `casos-pendientes.json`, `importacion-propuesta.xml`, `comentario-jira-borrador.md` y `09-T11-diseno-respuesta.md`. Para contrastar lo que se dice observado, también revisé las evidencias de T11: las dos capturas del 17/11 y el archivo AX del 18/11.

## Bloqueantes

**Ninguno** para T11-01 a T11-06.

## No bloqueantes

Se recomienda corregirlos antes de importar o, si no da tiempo, dejarlos documentados.

1. **T11-04, paso 9.** El resultado dice «desplegado, muestra…», pero ningún paso indica desplegar Home. No se observó si Home queda plegado tras F5. Hay dos opciones:
   - añadir un paso «Hacer clic en el triángulo de despliegue de **Home**, si aparece plegado»;
   - o redactar el resultado como «Home muestra el triángulo de despliegue» y comprobar la relación en el paso 10.
2. **T11-04, precondiciones.** El paso 7 espera que «ningún proyecto desaparece ni se duplica», pero falta la precondición «Lista inicial de **Projects** de A consignada en el registro de ejecución», que sí tienen 01–03. Sin ella no hay contra qué comparar.
3. **T11-06, See all.** Los pasos 5, 8 y 11 suponen que la sección de completadas está oculta. Según la guía §13, si está desplegada se ve **Hide** y no **See all**. Se puede añadir la precondición nominal «Sección de completadas de **Home** y **Study** oculta», o escribir «si la sección está oculta», como en el ejemplo de la guía §16.
4. **Matriz de estados, celda H×E1.** «Sin cambio esperado: no ejercitado» afirma un resultado que ninguna fuente respalda. Debería decir «No ejercitado; sin fuente». En el borrador de Jira hay que hacer el mismo cambio.
5. **T11-01, paso 3: ambigüedad con Loading.** El análisis declara como criterio del equipo que la entrada se muestre sin recargar y sin quedarse en Loading. Sin embargo, el resultado esperado solo pide anotar el Loading, así que no queda claro si un Loading persistente hace fallar el paso. Conviene fijar el veredicto, por ejemplo: «Sin recargar, la vista sale de **Loading** y muestra…; un **Loading** persistente se registra como resultado no conforme, sin pulsar **Add** de nuevo».
6. **Respuesta 09, punto 2 de «Para Codex».** Afirma que el bloque manual usaba «el destino Study para la anidación». Es incorrecto: `exploracion.md` (18/11) pidió anidar bajo **Home**; Study era solo el destino de la tarea pendiente. Las fichas y el análisis están bien porque usan Home, pero esa frase no debe pasar a `exploracion.md` ni a Jira. Además, el bloque manual sigue sin respuesta y no se asume ningún resultado.
7. **Borrador de Jira.**
   - En la fila de conservación, el fundamento «Encargo expreso» no lo entenderá quien lea el ticket. Mejor: «Criterio establecido expresamente por el usuario/equipo», como dice `exploracion.md`.
   - Las secciones 7 y 9 deben actualizarse con los IDs reales al registrar.
   - Los códigos de error `noWindowsAvailable`/`cgWindowNotFound` pueden resumirse como «limitación de acceso de la herramienta».
8. **T11-05, paso 5: «no se crea una subtarea».** Tiene fuente: la tarea de tutorial `You can drag and drop task on each other to create sub tasks, like this` aparece en la captura del 17/11. Funciona como resguardo del destino y no como escenario de jerarquías de tareas, así que no infringe decisiones §5. Aun así:
   - conviene citar esa fuente en la fila de reglas;
   - o expresar el resultado de forma más observable: «la tarea no aparece sangrada bajo otra tarea».
9. **Longitud de títulos.** T11-03 y T11-05 tienen unos 86 caracteres sin prefijo y unos 94 con «T11-0N. ». Entran en el «aproximadamente ≤90», pero se podrían acortar; por ejemplo: «Cancel Editing en Edit de proyecto descarta el nombre nuevo y conserva el original».
10. **Limpieza del lote.** Falta indicar cómo se retirará el subproyecto de T11-04 si T11-07 sigue pendiente. Conviene documentar que se usará Delete como limpieza y no como ejecución de los casos 15–16 de T08. Sus tareas pasarán a Recycle Bin, que debe quedar vacía al cierre (decisiones §14). La completada de T11-06 se reactiva y se elimina según la guía §17.
11. **Pasos 5 de T11-02 y T11-03 (situar el puntero y hacer clic en opciones).** Se aceptan como una sola interacción, porque el icono solo aparece al pasar el puntero, como indica el tutorial `Hover your mouse over a project or item and click the icon…`. No requiere cambio.

## Contraste de lo que pedía el encargo

| Punto | Resultado |
|---|---|
| Seis listos (01–06), 07 pendiente y fuera del XML | Correcto. `casos-listos.json` tiene 01–06; `casos-pendientes.json` tiene 07; el XML contiene solo seis `<testcase>`. `casos.json` tiene las siete fichas con la misma estructura. |
| 03: Cancel observado el 18/11; F5 posterior en blanco | Correcto. El descarte se clasifica como observado y la persistencia tras F5 como criterio del equipo. La pantalla gris se atribuye a la herramienta y no se presenta como fallo del producto. El archivo AX solo muestra la pestaña, lo que coincide con «falta de contenido». |
| 04: anidación documentada y triángulo observado en Work | Correcto. La portada respalda la anidación como regla documentada. La captura del 17/11 muestra Work → Sub Project, con el hijo sangrado y el triángulo a la izquierda del padre. Ningún arrastre se presenta como observado. |
| 05: mover pendiente según tutorial y portada | Correcto. El tutorial `Move items to different project using drag and drop. (Drag the small handler in front of the task)` se ve en la captura. |
| 06: reporte previo del usuario (guía §13) | Correcto. Se clasifica como regla documentada por reporte del equipo, se aclara que no es un fallo de la herramienta y no se afirma que no exista otro mecanismo. Recycle Bin queda excluida (T08). No se exige ningún mensaje. |
| 07: retorno a la raíz y reordenación pendientes | Correcto. Los pasos de ubicación están marcados PENDIENTE y se aclara que no se presupone el procedimiento. Study y Personal son contiguos en la raíz observada. |
| Ningún dato acreditado como creado o arrastrado sin fuente | Correcto en el análisis, el borrador y las fichas: «nombres de diseño todavía no creados», «ningún arrastre se presenta como observado». La única desviación es la frase sobre Study de la respuesta 09 (no bloqueante 6). |
| Bloque manual pendiente | Correcto: no se asume confirmación y la anidación pedida es bajo Home. |

## Rúbrica

| Criterio | Resultado |
|---|---|
| Títulos con funcionalidad, condición y resultado, de unos 90 caracteres como máximo | Cumplen. 03 y 05 quedan en el margen con el prefijo (no bloqueante 9). |
| Descripción en una sola oración que empieza por «Validar que» | Cumple en los seis. |
| Precondiciones nominales, sin verbos | Cumplen («Acceso…», «Sesión iniciada…», «Lista… consignada», «Ausencia de…», «Orden Sort By: Order…»). |
| Una acción por paso | Cumple. El caso de pasar el puntero y hacer clic se acepta (no bloqueante 11). |
| Datos y controles en negrita | Cumple. En el XML, la negrita se convirtió a `<strong>`. |
| Resultados observables | Cumplen, con dos reservas: el Loading de 01 y el «desplegado» de 04 (no bloqueantes 1 y 5). |
| La ficha contiene exactamente los campos acordados | Cumple: título, importancia con razón, requerimiento, precondiciones, descripción, pasos y postcondiciones. No incluye técnica, riesgo ni severidad. |
| XML | Raíz `<testcases>`, sin `<testsuite>`, sin `internalid`/`externalid`. `execution_type` 1 (Manual) en el caso y en cada paso. Importance: high=3 (01, 04, 05, 06) y medium=2 (02, 03). Número de pasos igual al de `casos-listos.json`: 7, 11, 11, 12, 15 y 12. Summary con descripción, requerimiento y postcondiciones, en ese orden (decisiones §15). Está sincronizado; la nota de la respuesta 09 sobre un «XML desactualizado» ya no aplica. |
| Casos de uso con flujos Actor/Sistema y trazas | Cumple: UC1–UC4, con alternativas trazadas a 03, 06 y 07. |
| Matriz de estados en formato docente (filas = estado actual, columnas = evento) | Cumple. Solo debe corregirse la celda H×E1 (no bloqueante 4). |
| Partición pendiente/completada justificada por tratamientos distintos según las fuentes | Cumple: la tarea pendiente se fundamenta en la portada, el tutorial y el criterio del equipo; la completada en Done Items, en la guía §13. Recycle Bin queda fuera de alcance. |
| Sin valores límite sin frontera ni tabla de decisión forzada | Cumple, y se justifica en §5.4. |
| Sin tareas padre/subtareas ni eliminación de subproyectos | Cumple. Las menciones son exclusiones o resguardos (no bloqueante 8). |
| Datos preexistentes conservados | Cumple: se consignan las tareas y proyectos iniciales y se contrastan en origen y destino. Falta la lista de Projects en 04 (no bloqueante 2). |
| Limpieza del lote declarada con honestidad | Cumple: las postcondiciones indican qué queda pendiente de la limpieza final. Falta precisar el método para el subproyecto (no bloqueante 10). |

## Checklist de la guía §19

- [x] Se leyó el ticket correcto (PEB-75) y se respetó su alcance.
- [x] El análisis explica riesgos concretos (R1–R8, con P×I justificado), reglas y dudas.
- [x] Cada técnica tiene una aplicación real y una traza a los casos.
- [x] Los tipos de prueba se eligieron por pertinencia; la parte no funcional se declara sin cobertura y con su motivo.
- [x] No se inventaron límites, controles, mensajes ni funciones. Única reserva: la celda H×E1 de la matriz, que no se usa en ningún caso.
- [x] No se reintrodujeron las jerarquías de tareas.
- [x] La ficha de cada caso contiene solo los campos acordados.
- [x] Se usa importancia, no severidad.
- [x] Cada paso tiene un resultado verificable, con las reservas 1 y 5.
- [x] Los datos, controles y estados iniciales permiten reproducir el caso, con las reservas 2 y 3.
- [x] La limpieza y las postcondiciones indican dónde terminan los datos (falta el método de 04).
- [x] Se diferencian los estados diseñado, listo, pendiente, no registrado y no ejecutado.
- [x] No se afirma cobertura ni evidencia que no exista.

## Veredicto

**APTO para T11-01, T11-02, T11-03, T11-04, T11-05 y T11-06.** No hay bloqueantes. Antes de importar, conviene aplicar los no bloqueantes 1–5, que afectan a fichas o al análisis; el resto puede documentarse.

T11-07 no se evaluó para registro: sigue pendiente, como corresponde.

Si el reporte manual del usuario contradice 04, 05 o 06, este veredicto deja de valer para ese caso y hay que revisarlo antes de registrarlo.
