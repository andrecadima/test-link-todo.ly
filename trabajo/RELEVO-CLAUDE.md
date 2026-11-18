# Relevo de fase 6 — 18/11/2026
1. T09/T10/T11 terminados: 29 casos; no reimportar ni corregir TestLink.
2. T09:13 casos TL-72–TL-84; Jira PEB-73 comentario10227.
3. T10:9 casos TL-66–TL-71 y TL-85–TL-87; PEB-74 comentario10226.
4. T11:7 casos TL-88–TL-94; PEB-75 comentario10228.
5. Otro Claude revisa TestLink por API; su versión será final. Esperar aviso explícito de Andre antes de exportar.
6. Codex está limpiando Todo.ly. Si no continúa, Andre realiza los pasos7–11 manualmente, solo en A/B.
7. A: Home ya vacío; dos marcadores T09/T07 enviados a papelera. Study ya vacío; dos tareas temporales T11 enviadas a papelera.
8. A COMPLETADA: proyecto vacío eliminado y papelera vaciada; captura cierre/A-estado-final.png y AX cierre/A-final-AX.txt.
9. B PENDIENTE: seleccionar Home (herramienta no lo logró tras3intentos; se pidió ayuda), borrar Prueba T09-aislamiento-B-1941 y vaciar Recycle Bin.
10. Vaciar Recycle Bin en A y B. Andre confirmó expresamente estas tres acciones en el chat18/11. Nunca usar Camila ni borrar cuentas.
11. Comparar Profile/Default Settings con trabajo/estado-cuentas-inicial.md: nombresA Andre Cadima/B Andre Cadima4, emailoriginal privado, LaPazUTC04, Work/Sunday/Small/None, casillas sí/no/sí; Order/Hidden y cinco tutorialesWork conservados.
12. Contraseña originalA ya restaurada/verificada; B emailoriginal conservado. No repetir Login ni cambios de credenciales.
13. estado-cuentas-final.md registra Acompleta/Bpendiente. Captura finalA guardada; faltaB. Defaults desplegables coinciden; AX no expone marcas de casillas.
14. Claude puede preparar solo con archivos el script API de exportación/extracción y borrador de informe. No navegador/Jira/git/.secrets ni lectura de respaldos con credenciales.
15. El script recibe API key por variable privada de entorno; jamás incrustarla/imprimirla. Codex/Andre la suministra fuera de git al ejecutar.
16. NO EJECUTAR exportación hasta aviso de Andre. Luego exportar suiteid3, proyectoid1, últimas versiones, a testlink-xml/todo-ly-tests.xml.
17. Preferir XML-RPC TestLink de solo lectura; si no existe exportaciónnativa, reconstruir XML fiel desde getTestSuitesForTestSuite/getTestCasesForTestSuite/getTestCase, conservando IDs/pasos/metadatos, y declarar procedenciaAPI.
18. Extraer con scripts/extraer_xml_por_ticket.py los T09.xml/T10.xml/T11.xml y manifiesto. No usar XML de importación como exportaciónreal.
19. No comparar ni revertir redacción final a diseños locales; diferencias esperadas, referencia revision-testlink/informe-revision.md.
20. Informe breve trabajo/INFORME-FINAL.md: IDs/enlaces por ticket, tres comentariosJira, pendientesT09-08/T10-07 y demás dudas documentadas, estado real de cuentas/XML/revisión integrante.
21. Jira: https://alesalve.atlassian.net/browse/PEB-73?focusedCommentId=10227 ; PEB-74?focusedCommentId=10226 ; PEB-75?focusedCommentId=10228.
22. Sin modificaciones de estados Jira ni casos ajenos. Sin consulta visual10227. Sin capturas extra fuera de las dos finales solicitadas.
23. Commit+push NORMAL, nunca force push (denegado). Escanear staging con scripts/verificar_secretos_git.py; .secrets siempre ignorado.
24. revision-testlink/respaldo-*.json ignorados. Incluir archivos nuevos seguros sin editarlos; historialantiguo conserva cuatro archivos con credencial heredada; árbolactualprotegido. No afirmar historialpurgado.
25. Siguiente paso: terminar limpieza autorizada y finalestado; esperar aviso revisión final; ejecutar exportación+extracción; completar informe; commit/push.
