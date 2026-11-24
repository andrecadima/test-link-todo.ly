# Ejecución del grupo 2 — informe final

Pruebas manuales realizadas en Chrome/macOS el 23 y 24 de noviembre de 2026. Alcance: **TS-01 Registro de usuario (9)** y **TS-02 Inicio de sesión (6)** del proyecto **TC:Todo.ly grupo 2 (1387)**. Plan **Ejecución grupo 2 - 2026-11-23 (2897)**, build **Todo.ly web - 2026-11-23 (1)**. El nombre del build es una etiqueta de sesión; no acredita una versión de la aplicación.

**15 casos con resultado: 10 Passed, 5 Blocked por ambigüedad, 0 Failed y 0 Not Run.** Se documentaron los 85 pasos; no se modificaron las fichas originales.

| Caso TestLink | Código del grupo | Resultado | Evidencia de ejecución |
|---|---|---|---|
| TC-1 | TC-001 | Passed | [Ejecución 1](http://68.211.149.112/lib/execute/execPrint.php?id=1) |
| TC-2 | TC-002 | Blocked | [Ejecución 23](http://68.211.149.112/lib/execute/execPrint.php?id=23) |
| TC-3 | TC-003 | Passed | [Ejecución 3](http://68.211.149.112/lib/execute/execPrint.php?id=3) |
| TC-4 | TC-004 | Passed | [Ejecución 4](http://68.211.149.112/lib/execute/execPrint.php?id=4) |
| TC-5 | TC-037 | Passed | [Ejecución 5](http://68.211.149.112/lib/execute/execPrint.php?id=5) |
| TC-6 | TC-039 | Passed | [Ejecución 6](http://68.211.149.112/lib/execute/execPrint.php?id=6) |
| TC-7 | TC-040 | Passed | [Ejecución 7](http://68.211.149.112/lib/execute/execPrint.php?id=7) |
| TC-8 | TC-041 | Passed | [Ejecución 8](http://68.211.149.112/lib/execute/execPrint.php?id=8) |
| TC-9 | TC-042 | Passed | [Ejecución 9](http://68.211.149.112/lib/execute/execPrint.php?id=9) |
| TC-10 | TC-033 | Blocked | [Ejecución 22](http://68.211.149.112/lib/execute/execPrint.php?id=22) |
| TC-11 | TC-034 | Passed | [Ejecución 11](http://68.211.149.112/lib/execute/execPrint.php?id=11) |
| TC-12 | TC-043 | Blocked | [Ejecución 21](http://68.211.149.112/lib/execute/execPrint.php?id=21) |
| TC-13 | TC-044 | Blocked | [Ejecución 18](http://68.211.149.112/lib/execute/execPrint.php?id=18) |
| TC-14 | TC-045 | Blocked | [Ejecución 19](http://68.211.149.112/lib/execute/execPrint.php?id=19) |
| TC-15 | TC-046 | Passed | [Ejecución 20](http://68.211.149.112/lib/execute/execPrint.php?id=20) |

## Ambigüedades pendientes de aclaración del grupo autor

| Caso | Motivo y aclaración necesaria |
|---|---|
| TC-2 / TC-002 | La precondición exige inexistencia de una cuenta asociada al nombre, sin definir cómo comprobarla. El rechazo de Email vacío sí se observó. Aclarar la precondición. |
| TC-10 / TC-033 | Summary y Steps contienen parejas de credenciales distintas. Los datos literales de Steps permitieron entrar, pero no se elige una fuente como correcta. Unificar los datos autorizados. |
| TC-12 / TC-043 | Email vacío: rechazo genérico. Definir si ese mensaje satisface la validación del campo Email requerida por la ficha. |
| TC-13 / TC-044 | Password vacío: rechazo genérico. Definir si ese mensaje satisface la validación del campo Password requerida por la ficha. |
| TC-14 / TC-045 | Ambos campos vacíos: rechazo genérico. Definir las señales observables de las validaciones de campos obligatorios. |

Los cinco casos permanecen **Blocked**, identificados como **AMBIGUO** en sus notas globales. No se atribuye una falla del producto a una definición incompleta. TC-15 admite expresamente el rechazo por credenciales inválidas o cuenta inexistente; el mensaje genérico observado satisface ese esperado, sin demostrar cuál dato falló.

## Registro y evidencia

- Resultados y observaciones por paso guardados en TestLink. TC-1…11 se registraron inicialmente por interfaz. La API permitió guardar los resultados globales posteriores, pero la instancia omitió las notas de pasos enviadas; se completaron **TC-2, TC-10, TC-12, TC-13, TC-14 y TC-15 por interfaz**, comprobando sus notas y estados en Print. Las ejecuciones anteriores se conservaron como historial, no como nuevas pruebas manuales.
- La última lectura API confirmó los quince resultados, modo Manual y exactamente quince casos vinculados al plan. Véase [verificacion-final.json](verificacion-final.json). La descripción del plan se corrigió de 75 a 15 casos.
- [TC-1](evidencias/2026-11-23_TC1.png) tiene además un adjunto en TestLink. [TC-4](evidencias/2026-11-23_TC4.png), [TC-13](evidencias/2026-11-24_TC13.png), [TC-14](evidencias/2026-11-24_TC14.png) y [TC-15](evidencias/2026-11-24_TC15.png) se conservan localmente. La captura de TC-13 también está en el adjunto2 de la ejecución previa15; la última ejecución18 contiene las notas completas.
- El intento inicial de TC-13 del 23/11 no tuvo lectura estable. Su veredicto se basa en la prueba completa observada el 24/11, sin reutilizar el mensaje de otro caso.

## Estado y límites

No se confirmaron bugs de Todo.ly contra un criterio inequívoco. Los problemas de Chrome y de persistencia de la API de TestLink se distinguieron de defectos de la aplicación. No se usó Todo.ly por API.

Se crearon únicamente las dos cuentas QA de los registros positivos TC-004 y TC-041, con datos del ejercicio y sin tareas de prueba añadidas. TC-040 fue rechazado y no creó cuenta. Las credenciales y estados están en el archivo privado ignorado; no se cambiaron contraseñas ni se eliminaron cuentas. El acceso de TC-10 terminó con Logout; la sesión Guest final de Todo.ly permanece sin autenticar. No se usó la cuenta de Camila.

**Pendiente:** aclaración de las cinco fichas por el grupo autor y reevaluación/repetición de esos casos con un criterio definido. Los otros 60 casos y el proyecto anterior no se modificaron; Jira no se utilizó en esta ejecución.
