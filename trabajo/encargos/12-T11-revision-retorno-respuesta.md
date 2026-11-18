# Respuesta 12 — Revisión específica de T11-07 y de los resultados manuales

Revisé AGENTS.md, decisiones-vigentes.md, la última sección de exploracion.md, analisis-diseno.md, casos-importar-adicionales.json, importacion-adicionales.xml y las capturas manual-1 a manual-5. No revisé de nuevo los casos 01–06 (TL-88 a TL-93).

Lo que muestran las capturas coincide con la lectura de Codex. Captura 1: aviso `Info. Item has been moved to project: Study`. Captura 2: la pendiente aparece en Study. Captura 3: la completada aparece en `1 Done Items`. Captura 4: el temporal está bajo Work → Sub Project. Captura 5: el temporal está en la raíz, entre Study y Personal, alineado con ellos, y encima aparece el menú de importación de TestLink. El JSON y el XML de T11-07 tienen el mismo texto. El XML no lleva IDs, usa importance 3 y execution_type 1, y marca los controles con strong. Tiene seis pasos, cada uno con una sola acción. No añade padre/subtareas ni el uso de Delete de T08.

## Bloqueantes

**Para importar T11-07:** ninguno.

**Para publicar T11:** una contradicción en el análisis.

1. **R8 en `analisis-diseno.md` §2.** El fundamento de P dice «procedimiento no confirmado», pero §1, §3, §5.2 y §8 dan por confirmado el retorno a la raíz, por reporte del usuario y captura 5. Además, «o reordenar la raíz» sugiere que se cubre una reordenación independiente, que no se ejecutó (§5.2 y §8). Propuesta:
   - Riesgo: «R8: devolver un subproyecto a una posición raíz concreta lo pierde o lo coloca en otra posición».
   - P: «2: cambio de ubicación con posición de destino concreta; retorno confirmado por reporte y captura».
   - Para mantener la coherencia, aplicar el mismo criterio en §4 («Alternativos: … retorno a la raíz entre Study y Personal (07)») y en §6 («T11-07 Retorno a la raíz entre Study y Personal»).

## No bloqueantes

Pueden corregirse antes de importar o anotarse:

1. **Precondición de posición (07).** El destino «entre Study y Personal» solo se puede ejecutar si las dos entradas raíz son contiguas y el subproyecto se ve bajo Home. Propongo añadir: «**Home**, **Study** y **Personal** como proyectos raíz de A, con **Study** inmediatamente antes de **Personal**; **Home** desplegado en **Projects**». En las capturas 1–5 ese orden aparece en A.
2. **Origen de cada afirmación en el requerimiento y el summary (07).** Hoy dicen «ubicación y datos se conservan tras F5 según el criterio del equipo». La ubicación tras F5 viene del reporte del usuario; solo la conservación de la tarea es criterio del equipo. Propuesta: «…; la ubicación tras F5 se basa en el reporte manual y la conservación de la tarea es criterio del equipo». En el paso 3, conviene sacar del resultado esperado la frase «conservación como criterio del equipo», porque es una nota sobre el origen y no algo que se observa en pantalla.
3. **Resultado del paso 5 (07).** Le falta la negrita en los datos y no es tan concreto como el paso 3. Propuesta: «El área principal muestra el título **Prueba T11-07 - retorno** y **Prueba T11-07 - dato del retorno** una sola vez, con su checkbox sin marcar».
4. **Razón de importancia (solo ficha, no va al XML).** «al deshacer una anidación y reordenar la raíz» debería decir «…y devolverlo a una posición raíz concreta». Es el mismo motivo del bloqueante 1.
5. **Inventario de limpieza (`exploracion.md`).** En las capturas 4 y 5, la pendiente de Study tiene el texto `Prueba T11 - mover completada 1811` y ya no se ve `Prueba T11 - mover pendiente 1811`, que sí aparecía en las capturas 2 y 3. Hay que listar las dos tareas por su texto e indicar que la ubicación de `mover pendiente 1811` está por confirmar en la limpieza. No hay que atribuirlo al producto.
6. **`analisis-diseno.md` §8.** Dice «El subproyecto temporal se retira mediante Delete», pero ese temporal ya es un proyecto raíz. Debería decir «El proyecto temporal…».
7. **Captura 5 como evidencia en Jira.** Lleva encima el menú de TestLink/Chrome. No expone secretos, pero conviene recortarla o aclararlo en el pie de la imagen.
8. **`node_order` 1 en el XML.** No afecta al contenido. Comprobar tras importar que TL asigna el ID siguiente sin reordenar ni actualizar los casos existentes.

No encontré contradicciones sobre pendientes ni sobre el registro:
- **Pendiente:** el traslado Home → Study y su persistencia figuran como reporte más captura.
- **Completada:** la restricción se limita a Done Items, sin generalizarla a otros mecanismos.
- **Anidación bajo Home:** su persistencia se atribuye al reporte, no a la captura 4.
- **Registro:** los seis casos suman 71 pasos (7+11+11+14+16+12) y T11-07 no tiene ningún ID inventado.

## Veredicto

- **Importar solo T11-07: APTO.** Recomiendo aplicar antes los no bloqueantes 1–3.
- **Publicar T11: NO APTO** hasta corregir R8 (bloqueante 1 y su coherencia en §4 y §6). Con ese cambio de texto pasa a APTO sin otra revisión. Esta revisión no sustituye a la de otro integrante.
