# Respuesta al encargo 09 — Diseño final acotado de T11

Fecha: 18/11/2026. Agente: Claude (diseño). No usé navegador, Jira, TestLink ni git, y no leí `.secrets/` ni `revision-testlink/`.

## Archivos escritos

Solo los autorizados:

- `trabajo/T11/casos.json`: fuente de las siete fichas (T11-01 a T11-07).
- `trabajo/T11/casos-listos.json`: T11-01 a T11-06, contenido idéntico al de `casos.json`.
- `trabajo/T11/casos-pendientes.json`: T11-07.
- `trabajo/T11/analisis-diseno.md`: nueve secciones con la estructura de T10 y las fichas después de `<!-- FICHAS_GENERADAS -->`, escritas a mano a partir del JSON. Codex debe sincronizarlas.
- `trabajo/T11/comentario-jira-borrador.md`: nueve secciones sin fichas; la sección 7 dice «por registrar», sin IDs.

## Decisiones

| Caso | Situación | Fundamento del resultado principal |
|---|---|---|
| 01 Crear, seleccionar y F5 | Listo | Observado el 17/11. La vista inmediata sin Loading es criterio del equipo; el paso 3 pide anotar un Loading persistente sin repetir Add. |
| 02 Renombrar con Save y F5 | Listo | Observado el 17/11 (menú de opciones, Save y persistencia en una nueva carga). |
| 03 Cancel Editing | **Pasa a listo** | Descarte observado el 18/11. La persistencia tras F5 es criterio del equipo, declarado así en el análisis. |
| 04 Raíz → subproyecto | Listo | Home como padre y un proyecto temporal con su propia tarea marcadora. Anidación documentada por la portada. La representación sangrada con triángulo se observó en Work → Sub Project. Relación y contenido tras F5 son criterio del equipo. |
| 05 Pendiente Home ↔ Study | Listo | Portada y tutorial de la interfaz (asa delante de la tarea) más criterio de conservación. Se comparan origen y destino con las tareas preexistentes consignadas. No se preparan prioridad ni vencimiento. |
| 06 Completada desde Done Items | **Reformulado y listo** | Reporte previo del usuario (guía §13), clasificado como regla documentada y no como fallo de la herramienta. Se espera que permanezca completada en Home y fuera de Study, también tras F5. No se exige mensaje. No se afirma que no exista otro mecanismo. Recycle Bin queda fuera (T08). |
| 07 Retorno a la raíz y reordenación | **Nuevo, pendiente** | Procedimiento sin confirmar; los pasos de ubicación están marcados PENDIENTE. No se importa. |

- Rúbrica aplicada: títulos de unos 90 caracteres como máximo; descripción en una sola oración que empieza con «Validar que»; precondiciones nominales («Ausencia de…», «Home y Study como…», «Orden Sort By: Order…»); una acción por paso; controles y datos en **negrita**; cuentas genéricas y ningún secreto.
- No se impusieron límites de profundidad, ciclos, unicidad ni longitud, y no se aplicaron valores límite. No hay tareas padre/subtareas ni Delete de subproyectos.
- Técnicas: casos de uso Actor/Sistema con trazas; matriz docente de transición (—/R/H × E0–E3, con el retorno a R pendiente); partición pendiente frente a completada en Done Items, solo porque las fuentes indican tratamientos diferentes (trazas a 05/06). No se forzó tabla de decisión.

## Para Codex

1. **Ejecución manual pendiente.** No presenté ningún arrastre como observado. Cuando llegue el reporte del usuario:
   - Si contradice 04, 05 o 06, esos casos deben volver a pendiente o corregirse antes de registrar.
   - Si confirma el retorno a la raíz, hay que completar los pasos PENDIENTE de 07.
   - Si el arrastre desde Done Items sí traslada la tarea, 06 se convierte en un hallazgo frente al reporte del equipo y hay que avisar al usuario.
2. **Ajustes de datos.** El bloque manual usaba otros nombres (`… 1811`) y el destino Study para la anidación; las fichas usan Home como padre, como pide el encargo. Si el reporte trae datos reales, regístralos en `exploracion.md` y no en las fichas.
3. **XML desactualizado.** `trabajo/T11/importacion-propuesta.xml` corresponde al diseño anterior y no estaba autorizado. Hay que regenerarlo desde `casos-listos.json`, convirtiendo la negrita a strong.
4. **Precondición de 07.** Supone un subproyecto ya anidado bajo Home. Cuando se cierre el caso, conviene confirmar si esa preparación se describe como estado o si se añade a los pasos.
5. **Limpieza final del lote.** Proyectos y tareas `Prueba T11-0N…`, además de `Prueba T11 - proyecto renombrado 1109`. La completada de 06 se reactiva y elimina según la guía §17.
6. **Revisión.** Sigue pendiente la revisión independiente con la checklist de la guía §19 y la de otro integrante. Este diseño no cuenta como revisión.
