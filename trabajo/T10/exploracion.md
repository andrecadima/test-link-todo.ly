# Registro de exploración — T10

- Fecha: 17 de noviembre de 2026.
- Entorno: perfil dedicado Todo.ly QA cuenta B, macOS/Chrome según inventario inicial; sesión A confirmada por correo exacto en Settings.
- Estado: exploración parcial, no ejecución formal ni registro de casos.

| Hora AUT | Cuenta | Acción | Resultado observado | Clasificación | Evidencia |
|---|---|---|---|---|---|
| 11:07 AM | A | Abrir Settings / Profile | Campos Full Name, Email, Time zone, Old Password, New Password; botones Ok y Cancel. | Comportamiento observado | Lectura de interfaz |
| 11:07 AM | A | Cambiar Full Name a `Prueba T10 - nombre cancelado`, pulsar Cancel y reabrir Settings | Full Name conserva Andre Cadima. | Comportamiento observado | `evidencias/2026-11-17_T10_cancel-conserva-nombre.png` |
| 11:07–11:08 AM | A | Cambiar Full Name a `Prueba T10 - nombre guardado`, pulsar Ok, recargar y reabrir Profile | Se conserva el nombre guardado. Email y zona La Paz no cambian en la consulta. | Comportamiento observado | `evidencias/2026-11-17_T10_nombre-guardado-persiste-recarga.png` |
| 11:08 AM | A | Restaurar Andre Cadima y pulsar Ok | El guardado termina y se cierra Settings; pendiente de una lectura posterior específica para certificar la restauración. | Comportamiento observado | Lectura de interfaz |

## Reglas y dudas

Guardar y cancelar se distinguen por el valor leído al reabrir Profile. La persistencia observada tras recargar no demuestra persistencia tras una nueva sesión: falta ese contraste. No se confirmó ninguna frontera de longitud del nombre ni política de contraseña.

La regla de la herramienta de control del navegador exige que el usuario tome el control antes de introducir una nueva contraseña u otra credencial de autenticación. La exploración de cambios efectivos de contraseña y correo queda pendiente de ese paso; no se han modificado esas credenciales. La recuperación con buzón controlado también requiere la intervención del usuario para leer el correo; no se accede al buzón.

No se operó la zona horaria ni la fecha predeterminada durante T10. No se abrió la eliminación de cuenta.

## Restauración confirmada

A las 11:11 AM se reabrió Profile y se confirmó Full Name Andre Cadima y la zona inicial La Paz UTC-04. Evidencia: `evidencias/2026-11-17_T10_perfil-restaurado.png`. El cambio temporal de nombre quedó revertido; no se cambió correo ni contraseña.

## Recuperación: solicitud y contraste

| Hora AUT | Cuenta o dato | Acción | Resultado observado | Clasificación | Evidencia |
|---|---|---|---|---|---|
| 11:12 AM | A | Cerrar sesión, abrir Login, Reset your Password, ingresar el correo de A y pulsar Send (nombre accesible Submit) | `Info. An email has been sent with a link where you can change your password.` Se solicitó al usuario revisar su buzón. No se abrió el correo ni el enlace. | Comportamiento observado; recepción pendiente | `evidencias/2026-11-17_T10_recuperacion-A-confirmacion-envio.png` |
| 11:13 AM | `prueba-t10-no-registrada-20261117@example.com` | Solicitar recuperación con ese correo reservado para ejemplos | `Error. Account with this Email address doesn't exist.` El formulario permanece visible. | Comportamiento observado | `evidencias/2026-11-17_T10_recuperacion-correo-inexistente.png` |

La confirmación de envío no prueba recepción, validez, caducidad ni uso único del enlace. No se aplicará el plazo de 24 horas del ejemplo docente como regla de Todo.ly. Pendiente: recepción del correo de A por el usuario y las comprobaciones de cambios de credenciales que requieren su control directo del navegador. Las contraseñas actuales no se modificaron por el agente.

Nota de evidencia visual: la captura posterior al envío de A muestra la landing, porque el aviso Info ya había desaparecido. Su texto exacto proviene de la lectura de accesibilidad inmediatamente posterior al envío. La captura de Cancel muestra Home tras descartar; el valor Andre Cadima se leyó al reabrir Profile. La captura `perfil-restaurado` sí muestra Profile con el valor original. No atribuir a una captura un texto que no esté visible en ella.
