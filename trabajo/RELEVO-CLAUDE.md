# Relevo de fase 6 — 18/11/2026 (tras el encargo 14)

1. T09, T10 y T11 están terminados en TestLink y Jira: 29 casos. No reimportar ni corregir TestLink.
2. T09: TL-72 a TL-84, comentario PEB-73 10227. T10: TL-66 a TL-71 y TL-85 a TL-87, comentario PEB-74 10226. T11: TL-88 a TL-94, comentario PEB-75 10228.
3. La revisión por API del otro Claude ya terminó (aviso de Andre: 93 casos finales, respaldo 1724). TestLink es la versión final. No revertir; referencia: `revision-testlink/informe-revision.md`.
4. **Exportación TERMINADA, no repetir.** `todo-ly-tests.xml` contiene 93 casos y 29 propios, SHA-256 f17141163f48…. Extracción: T09 13, T10 9, T11 7, con IDs conservados. Procedencia: reconstrucción por API, no exportación nativa.
5. El XML completo local tiene una credencial heredada. Está ignorado por git y en git solo va la copia `.fernet` más el manifiesto. No abrirlo ni subirlo en claro. Los XML T09, T10 y T11 no contienen credenciales conocidas.
6. A está COMPLETADA: datos retirados, temporal eliminado, Trash vacía, captura final guardada. No volver a tocarla.
7. **B PENDIENTE. Siguiente paso exacto:**
   a. Esperar a que Andre seleccione Home en B. La herramienta falló tres veces; no reintentar a ciegas.
   b. Con Home abierto, borrar la tarea `Prueba T09-aislamiento-B-1941`.
   c. Abrir Recycle Bin de B y pulsar Empty Recycle Bin. La confirmación ya está recibida; no volver a pedirla.
   d. Verificar con AX «There are no items to display» y que Home no tenga datos Prueba.
   e. Tomar UNA captura final de B: `trabajo/cierre/B-estado-final.png`.
   f. Actualizar la columna B de `trabajo/estado-cuentas-final.md` y la §5 de `trabajo/INFORME-FINAL.md`, sin inventar nada.
8. No repetir: el password original de A y el email original de B ya están restaurados. Tampoco repetir Login ni cambios de credenciales.
9. Las casillas de Defaults no se pueden leer por AX: se registra la limitación y no se confirman las marcas.
10. Después de B: escanear el staging con `scripts/verificar_secretos_git.py`, hacer commit y push normal. Nunca force push. El historial antiguo sigue sin purgar.
11. Siguen pendientes, fuera de Codex: la revisión por otro integrante y la ejecución formal de los casos. No marcarlas en Jira ni cambiar estados.
12. Ahorrar cuota: no hacer auditorías extra, capturas adicionales ni comparaciones de redacción.
