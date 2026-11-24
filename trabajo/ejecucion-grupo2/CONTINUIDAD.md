# Estado vigente — 24/11/2026, ejecución terminada

Alcance: proyecto TC:Todo.ly grupo 2 (1387), suites TS-01 (1388) y TS-02 (1470), únicamente TC-1…TC-15. Plan 2897 / build 1: quince vinculados, descripción corregida, activo y privado. Los otros 60 casos, proyecto TL anterior y Jira no se modificaron.

Resultado final verificado por API: **10 Passed, 5 Blocked, 0 Failed, 0 Not Run**, todos Manual. Blocked por ambigüedad: TC-2, TC-10, TC-12, TC-13 y TC-14. No asumir sus criterios ni modificar las fichas. TC-15 Passed por rechazo genérico permitido expresamente.

Últimas ejecuciones: TC-1=1, TC-2=23, TC-3=3, TC-4=4, TC-5=5, TC-6=6, TC-7=7, TC-8=8, TC-9=9, TC-10=22, TC-11=11, TC-12=21, TC-13=18, TC-14=19, TC-15=20. Detalle y enlaces en INFORME-EJECUCION.md y ejecucion.json.

Se ejecutó Todo.ly manualmente en Chrome aislado (Incognito el 23/11; Guest para TC13–15 el 24/11). La API autorizada se usó solo para TestLink. Sus respuestas confirmaron globales pero omitieron pasos: se completaron TC-2/10/12/13/14/15 en interfaz y se verificaron las notas y estados de cada paso en Print. No volver a lanzar registrar_resultados.py para repetir registros ya terminados. La evidencia API anterior queda en el historial.

Adjunto1: TC-1; adjunto2: captura TC-13 en ejecución previa15. XMLRPC informó error al subir el segundo, pero la interfaz confirmó su existencia: no reenviar para evitar duplicarlo. Las demás capturas están en evidencias/. Sin bugs de producto confirmados; dudas de fichas en incidencias-fichas.md.

Cuentas nuevas QA TC004 y TC041 registradas; TC040 rechazado, sin cuenta. Credenciales y estados solo .secrets/. No se añadieron tareas, no se cambiaron contraseñas ni se eliminaron cuentas. El Login válido terminó con Logout; Todo.ly Guest queda sin sesión. No cuenta de Camila.

Siguiente paso: el grupo autor aclara los cinco casos ambiguos; después reevaluar/repetir solo los afectados. No marcar Passed por defecto. El plan/build siguen abiertos para esa continuación. Los pendientes históricos T09/T10/T11 se mantienen aparte.

Git: incluir solo trabajo/ejecucion-grupo2/ y la actualización de trabajo/CONTINUIDAD.md. Preservar sin modificar ni incorporar los cambios ajenos actuales en revision-testlink/. Secretos fuera de git; push normal, nunca force.
