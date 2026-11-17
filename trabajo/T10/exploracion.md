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

La regla de la herramienta de control del navegador exige que el usuario tome el control antes de introducir una nueva contraseña u otra credencial de autenticación. La exploración de cambios efectivos de contraseña y correo queda pendiente de ese paso; no se han modificado esas credenciales por el agente. Inicialmente se delegó la lectura del correo al usuario; posteriormente este autorizó expresamente consultar el mensaje de recuperación que dejó abierto en Chrome. La consulta se limitó a ese mensaje.

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

## Recuperación: recepción y formulario, 17 de noviembre

Actualización que sustituye el pendiente de recepción de la sección anterior:

| Cuenta | Acción | Resultado observado | Clasificación | Evidencia |
|---|---|---|---|---|
| A | Revisar la captura proporcionada y el mensaje de recuperación que el usuario dejó abierto y autorizó consultar | Asunto `Forgot Password`, remitente visible `Todo.ly noreply@todo.ly`, recibido el 17/11/2026 a las 11:12; saludo `Dear Andre Cadima,`. Incluye instrucciones para cambiar la contraseña y dos enlaces de recuperación. El remitente visible no constituye verificación de autenticidad técnica del correo. | Comportamiento observado | Mensaje abierto en Gmail; no se conserva captura ni token en Git. |
| A | Abrir el enlace directo alternativo del correo en el perfil `Todo.ly QA cuenta B`, sin sesión iniciada | El enlace usa HTTP. La barra de Chrome muestra `Not Secure`; el área de contenido apareció vacía. No se introdujeron credenciales. | Comportamiento observado; carga vacía no atribuida al producto | Lectura de accesibilidad y captura temporal inspeccionada, sin guardar en el repositorio porque contiene el token. |
| A | Abrir la misma ruta y token con HTTPS, en una pestaña nueva del mismo perfil | Carga `Please Enter a New Password`, con los campos enmascarados `Enter a New Password` y `Verify New Password`, y el botón `Done`. | Comportamiento observado | Lectura de accesibilidad del formulario. |

Se solicitó al usuario completar personalmente la nueva contraseña, su confirmación y el envío, y actualizar únicamente el secreto local conservando la contraseña anterior para restaurarla. La política de CUA indica: `Changing a password or other authentication credential: Ask the user to take over before any new credential is entered, and have them complete the entry, confirmation, and submission steps themselves.` El agente no ha introducido ni enviado una nueva contraseña. El cambio efectivo y sus verificaciones de Login siguen pendientes de confirmación y consulta posterior.

No se han confirmado límites de contraseña, caducidad, uso único del token ni invalidación de sesiones. Las cargas vacías también aparecieron durante fallos del control nativo; no se registran como un defecto confirmado de Todo.ly. El enlace HTTP se documenta con pasos de reproducción y alcance limitado en [hallazgos.md](hallazgos.md).

## Recuperación: cambio manual y verificación posterior

El usuario confirmó que completó ambos campos y pulsó `Done`, y que actualizó la contraseña actual en `.secrets/cuentas-prueba.local.md`. El archivo ya contenía la contraseña actual indicada; se conservó también la anterior en el mismo archivo ignorado, para su restauración posterior. No se copian valores a este registro.

| Hora AUT | Cuenta | Acción | Resultado observado | Clasificación | Evidencia |
|---|---|---|---|---|---|
| 11:40–11:42 AM | A | Consultar la pestaña después del cambio manual y abrir Settings | Sesión iniciada; Profile muestra el nombre original, el correo de A y La Paz UTC-04. No se presenció el aviso exacto inmediatamente posterior a Done. | Comportamiento observado; envío completado según el usuario | `evidencias/2026-11-17_T10_A-sesion-despues-recuperacion.png` |
| 11:43 AM | A | Cerrar sesión y probar una vez Login con el correo de A y la contraseña anterior | `Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.` No se inicia sesión y el campo Password vuelve a quedar vacío. | Comportamiento observado | Lectura de accesibilidad con el mensaje exacto; `evidencias/2026-11-17_T10_password-anterior-rechazada.png` muestra el formulario sin el aviso, que ya había desaparecido al capturar. La imagen fue inspeccionada y no contiene contraseña visible. |
| 11:43–11:44 AM | A | Login con el mismo correo y la contraseña actual; abrir Settings | Se inicia sesión y Profile confirma el correo de A, Andre Cadima y La Paz UTC-04. El nombre guardado inicialmente se conserva también tras una nueva sesión. | Comportamiento observado | Lectura de accesibilidad del área autenticada y de Profile. |

La recuperación permite el acceso con la nueva contraseña y rechaza la anterior en el contraste realizado. No demuestra por sí sola caducidad del token, uso único ni cierre de otras sesiones. **Cambio pendiente de revertir:** la contraseña actual de A continúa siendo la elegida por el usuario durante esta recuperación; la anterior está conservada en el secreto local. Su restauración requerirá nuevamente entrada y envío manuales del usuario.

## Cierre acotado para la demo — continuación del 17 de noviembre

El usuario priorizó terminar por ticket (T10, T09, T11), acotando la exploración restante a aproximadamente una hora por ticket. Inicio de esta continuación: 15:51 UTC. Se hizo push de los seis commits existentes al remoto antes de explorar.

Profile de A volvió a mostrar únicamente Old Password y New Password en Change Password: **no existe un control de confirmación en Settings** en la vista consultada. La validación de confirmación distinta no se atribuye a ese formulario; el control Verify New Password pertenece a recuperación.

Se envió una vez Full Name vacío, conservando correo y configuración, y con los campos de cambio de contraseña vacíos. La vista original quedó en Loading. Una nueva consulta GET y apertura de Profile mostró Andre Cadima, correo de A y La Paz UTC-04. No se obtuvo un mensaje de validación fiable; no se confirma una regla de obligatoriedad del nombre ni se diseña su rechazo como regla del producto. Captura de la vista en proceso: `evidencias/2026-11-17_T10_nombre-vacio-en-proceso.png`.

Se dejó Settings de A abierto para intervención manual solicitada al usuario: Old Password vacío y New Password igual a la contraseña anterior privada, pulsar Ok y comunicar el mensaje. Se pidió realizar solamente ese intento para comprobar el estado antes del siguiente. **Sin respuesta ni resultado confirmado todavía.** Luego corresponden el contraste con Old Password incorrecto y la restauración por el flujo válido. No se introdujo ninguna nueva credencial por el agente.

La instrucción expresa del usuario establece HTTPS como **Criterio del equipo** para el enlace de recuperación. T10-10 lo incorpora como seguridad observable; el comentario de Jira lo mencionará como hallazgo a confirmar durante la ejecución. No se reporta en la planilla de fallas.

### Respuesta manual: Old Password vacío

El usuario proporcionó `Screenshot 2026-11-17 at 2.38.43 PM.heic` como respuesta al traspaso de control. La captura fue abierta y leída: muestra Settings / Profile de A, Old Password vacío, New Password con contenido enmascarado y un aviso de Todo.ly con el texto exacto **`Invalid Password`**, botón `OK`. Nombre y zona La Paz siguen visibles. No se conoce ni se transcribe la contraseña a partir de la imagen.

- **Clasificación:** Comportamiento observado: el intento con Old Password vacío produce el aviso Invalid Password. No demuestra por sí solo la conservación de la contraseña, que se contrastará mediante Login.
- **Evidencia:** `evidencias/2026-11-17_T10_old-password-vacio-Invalid-Password.png`, conversión PNG de la captura proporcionada, sin token ni contraseña legible.
- **Diseño:** T10-03 deja de tener pendiente el mensaje de rechazo. Su ejecución incluye verificar el acceso con la credencial anterior al intento.
- **Siguiente traspaso solicitado:** probar Old Password incorrecto y, si se rechaza, efectuar el cambio válido para restaurar la contraseña original, actualizando el secreto únicamente al confirmar aceptación. Si el intento incorrecto fuese aceptado, detenerse y registrar esa credencial como vigente. Aún no hay resultado confirmado de esas dos acciones.

La hora entre la solicitud manual y esta respuesta no se contabiliza como exploración activa del producto. Se mantiene el límite aproximado de una hora de trabajo activo y se dejarán las dudas no resueltas expresamente pendientes.

### Contraste de conservación y cierre de exploración adicional

El usuario solicitó que el agente continuara sin delegarle más cambios. Se retomó la pantalla y se descartó con Cancel el formulario que conservaba New Password enmascarado. Se cerró la sesión de A, se abrió una nueva consulta GET y se realizó Login con la contraseña actual de `.secrets`. Su valor coincidía privadamente con el usado en el último Login exitoso anterior al intento vacío. Login fue aceptado y Settings confirmó identidad A, nombre original y La Paz UTC-04. **Queda observada la conservación de la credencial tras Old Password vacío.** No se modificó ninguna contraseña ni correo.

Se cierra la exploración adicional de T10 para priorizar la demo. Quedan pendientes T10-04 (Old Password incorrecto), T10-05 (cambio válido y restauración desde Settings), T10-06 (Cancel de Email) y T10-07 (cambio válido de Email y posible verificación). La causa inmediata es la exigencia de entrada/envío manual de nuevas credenciales de la herramienta, no una restricción observada de Todo.ly. No se repite la solicitud al usuario.

El diseño propone seis casos listos y conserva cuatro candidatos pendientes fuera del conjunto registrable. No se interpreta la delegación general como aprobación de un diseño todavía no presentado. Se mantiene el punto de control por ticket antes de Jira/TestLink.
