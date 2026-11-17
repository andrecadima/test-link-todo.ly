# Registro de exploración — T09 (parcial)

- Entorno verificado en chrome://version: macOS 26.6.2 (25G83), Chrome 157.0.8103.51 (arm64).
- Fecha: 16 de noviembre de 2026. Las horas de abajo son las que muestra Todo.ly, no una conversión a hora boliviana.
- Perfiles locales aislados: `Todo.ly QA T09-T11` y `Todo.ly QA cuenta B`. No se borraron cookies globales ni se cerraron las sesiones originales de Jira/TestLink/Todo.ly.
- Estado de las cuentas: se observó una sesión abierta después de la intervención del usuario en el primer perfil. Falta confirmar que la cuenta A sea nueva para la práctica. El agente no ha creado ni confirmado la cuenta B; su contraseña generada solo está en `.secrets/cuentas-prueba.local.md`.

| N.º | Hora de la AUT | Cuenta | Acción | Resultado observado | Clasificación | Evidencia | Regla o caso que alimenta |
|---|---|---|---|---|---|---|---|
| 1 | 7:10 PM | Sin sesión | Abrir Signup | Full Name, Email, Password, Timezone, casilla de términos y Submit. Timezone tiene Pacific Time seleccionado inicialmente. | Comportamiento observado | `evidencias/2026-11-16_T09_registro-vacio.png` | Campos del registro |
| 2 | 7:10 PM | Sin sesión | Enviar formulario vacío, términos sin marcar | Texto accesible: `Error. Please correct the missing fields.`; asteriscos en nombre, email y contraseña; junto a términos: `If you don’t agree you can’t use Todo.ly`. El mensaje global desaparece antes de la captura, que sí muestra asteriscos y aviso de términos. | Comportamiento observado | Captura anterior y lectura de accesibilidad | Validación conjunta; no aísla la obligatoriedad de Timezone |
| 3 | 7:10–7:12 PM | Sin sesión | Completar datos de prueba con correo sin arroba, manteniendo términos sin aceptar | Persiste rechazo por campos/términos. El correo de la captura difiere del dato que se intentó introducir; no se toma esta prueba como validación aislada de formato de email. | Duda pendiente | `evidencias/2026-11-16_T09_registro-sin-aceptar-terminos.png` | Repetir formato inválido en condiciones controladas |
| 4 | 7:13 PM | Sesión intervenida por el usuario | Consulta de pantalla, sin alterar datos | Se ven Work con 5 tareas de ejemplo, Sub Project, Home, Study, Personal y Shopping List; Sort By: Order y Notes: Hidden. No se consultaron todos los estados ni Settings; no es un inventario inicial completo. | Comportamiento observado | Lectura de accesibilidad; sin captura dedicada | Inventario inicial por completar tras confirmar cuenta nueva |
| 5 | 7:14 PM | Sin sesión, perfil B | Desplegar Timezone | Lista de 101 opciones, desde UTC−12 hasta UTC+13. No aparece opción vacía en el listado visible completo. Se ve `(UTC-04:00) Georgetown, La Paz, Manaus, San Juan`. Hay otra La Paz en la opción mexicana UTC−07: no corresponde a Bolivia. | Comportamiento observado | Lectura completa del menú accesible | Selección válida de zona; no se manipulará el HTML para fabricar un vacío |
| 6 | 7:14 PM | Sin sesión, perfil B | Seleccionar la opción UTC−04 de La Paz | La etiqueta del selector cambia a `(UTC-04:00) Georgetown, La Paz, Manaus, San Juan`. El registro de B no se envió ni se confirmó. | Comportamiento observado | Lectura de accesibilidad | Preferencia solicitada por el usuario; persistencia aún no evaluada |

## Fronteras encontradas

No se confirmó ningún límite de longitud ni política de contraseña. No se aplica BVA todavía. La ausencia de una opción vacía en un selector no demuestra validación de servidor; solo limita la comprobación manual desde la interfaz.

## Dudas que afectan resultados esperados

| Duda | Casos afectados | Qué hace falta |
|---|---|---|
| ¿La cuenta A se creó nueva para la práctica? | Exploración autenticada y cambios de A | Respuesta del usuario a la pregunta pendiente; no utilizar una cuenta preexistente según instrucción inicial. |
| ¿El correo de B está disponible? | Registro B, separación A/B | Enviar Signup con el correo autorizado exacto y observar respuesta; si ya existe, no entrar ni recuperar. |
| Validación aislada de email y contraseña | Particiones/BVA de registro | Repetir sin campos o condiciones concurrentes que oculten el motivo de rechazo. |

## Cambios y estado

Se crearon dos perfiles locales de Chrome, sin sincronización de Google. El agente no ha modificado datos de ninguna cuenta de Todo.ly ni escrito en Jira/TestLink. La aceptación de términos para A y B fue autorizada expresamente por el usuario; no hace falta pedirla de nuevo. El acceso a Chrome produjo fallos intermitentes de captura/foco y elementos inválidos; no se atribuyen esas fallas de automatización al producto ni a las credenciales.

Fase 1 incompleta: no existe aún el inventario inicial íntegro de dos cuentas nuevas. No se registra este trabajo como ejecución formal de casos.

## Actualización posterior — fase 1 completada

Los párrafos anteriores son el registro cronológico de la preparación inicial. El usuario confirmó que ambas cuentas fueron creadas hoy y posteriormente sustituyó la candidata B por otro correo y contraseña en el archivo privado. La B vigente tiene Full Name Andre Cadima 4; la anterior candidata no forma parte de las pruebas actuales.

Se verificó Login de A con el correo exacto autorizado y se confirmó Profile: Andre Cadima. La sesión anterior del primer perfil QA tenía un correo mal escrito distinto de A; quedó intacta y excluida.

La B vigente también pudo autenticarse: el correo estaba guardado como enlace Markdown y el primer envío incluyó ese formato literal. Se corrigió la lectura y se envió solo la dirección; Login aceptado con la contraseña vigente. Este incidente de preparación no se atribuye a una falla del producto ni al rechazo de una contraseña correcta.

Se registraron las vistas iniciales de cada cuenta y sus Settings, proyectos y filtros en `../estado-cuentas-inicial.md`. Las zonas de ambas cuentas se prepararon en La Paz UTC-04 por instrucción expresa del usuario. A fue autenticada de nuevo después de cerrar B. Ambas credenciales actuales están verificadas; el bloqueo anterior queda resuelto.

La pantalla de registro mostró `Error. Account with this email address already exists!` en un intento con la antigua candidata B, después de que el usuario indicara haberla registrado. Es evidencia de un rechazo de registro duplicado en ese momento; no demuestra que la cuenta existiera antes del trabajo. Captura: `evidencias/2026-11-16_T09_email-B-ya-registrado.png`.

## Fase 2 — observaciones en curso

| Hora AUT | Cuenta | Condición y acción | Resultado observado | Clasificación | Evidencia |
|---|---|---|---|---|---|
| 7:38 PM | A | Crear `Prueba T09-aislamiento-A-1937` en Home mediante Add | Una tarea pendiente en Home. | Comportamiento observado | `evidencias/2026-11-16_T09_A-marcador-creado.png` |
| 7:39 PM | A | Logout con ese marcador existente | Landing con Login y sin el marcador. | Comportamiento observado | `evidencias/2026-11-16_T09_logout-A.png` |
| 7:39 PM | Sin sesión | Atrás después de Logout | Landing sin exposición del marcador de A. | Comportamiento observado | `evidencias/2026-11-16_T09_atras-tras-logout.png` |
| 7:39 PM | Sin sesión | Abrir directamente https://todo.ly/ después de Logout (misma URL observada durante sesión) | Landing con Login y sin el marcador. No se adivinaron endpoints internos. | Comportamiento observado | `evidencias/2026-11-16_T09_url-directa-tras-logout.png` |
| 7:39–7:40 PM | Sin sesión | Intentos con campos vacíos y A sin contraseña | Se vio rechazo genérico con los campos vacíos en la lectura de accesibilidad; hubo interrupciones de captura y página sin contenido. No se considera comprobada todavía cada combinación ni se atribuye la interrupción al producto. | Duda pendiente | Capturas login-vacios/login-A-sin-password requieren repetición antes de usarlas como evidencia de reglas. |
| 7:41 PM | B vigente | Login con credencial correcta; consultar Home y crear `Prueba T09-aislamiento-B-1941` | Home contiene solo el marcador B; no muestra el marcador de A. | Comportamiento observado | `evidencias/2026-11-16_T09_B-marcador-y-ausencia-A.png` |

Datos temporales aún por limpiar: marcador A en Home de A y marcador B en Home de B. No se han eliminado los tutoriales ni modificado prioridades, fechas, zona horaria o ajustes durante estas observaciones de fase 2. Falta el contraste inverso, Remember Me y completar las combinaciones de Login.

### Continuación del 17 de noviembre

Se confirmó la identidad A en Settings y se consultó Home: conserva `Prueba T09-aislamiento-A-1937` y no muestra `Prueba T09-aislamiento-B-1941`. La separación queda observada en ambos sentidos para esos dos marcadores. El marcador A permanece al retomar al día siguiente. Captura: `evidencias/2026-11-17_T09_A-conserva-marcador-y-no-ve-B.png`.

La sesión se encontró disponible al retomar el perfil, pero el cierre y reapertura entre días no se controlaron como experimento. Esto no sustituye las comprobaciones separadas de Remember Me marcado y sin marcar.

## Continuación acotada mientras se revisa T10

Se releyó el secreto local vigente, sin modificarlo ni publicar sus valores. A volvió a autenticar correctamente y su identidad se verificó en Settings antes de continuar. Las entradas negativas siguientes se enviaron mediante Login, sin realizar cambios de credenciales.

| Dato / combinación | Resultado y alcance | Clasificación | Evidencia |
|---|---|---|---|
| Email y Password vacíos | No se obtuvo acceso; la consulta posterior conservó Login. No se retuvo un mensaje literal fiable en ese contraste. | Comportamiento observado, mensaje pendiente | `evidencias/2026-11-17_T09_login-ambos-vacios-controlado.png` |
| Email vacío y Password informado con un valor de prueba | La captura muestra `Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.` y el formulario de Login, sin acceso. La lectura AX previa a la captura todavía no reflejaba la respuesta. | Comportamiento observado; imagen inspeccionada | `evidencias/2026-11-17_T09_login-correo-vacio-password-informado.png` |
| Correo no registrado reservado en example.com y Password de prueba | Aviso genérico Wrong email or password; Login permanece, no aparece Logout. | Comportamiento observado | `evidencias/2026-11-17_T09_login-cuenta-inexistente.png` y lectura AX |
| Correo válido de A y Password incorrecto | Aviso genérico Wrong email or password; no se concede acceso. Un intento, sin repetir por el error intermedio de captura. | Comportamiento observado | `evidencias/2026-11-17_T09_login-A-password-incorrecto.png` y lectura AX |
| Correo válido de A y Password vacío | Mismo aviso genérico; no se concede acceso. Un intento. | Comportamiento observado | `evidencias/2026-11-17_T09_login-A-password-vacio.png` y lectura AX |
| Email `PruebaT09SinArroba` y Password de prueba | La pestaña quedó sin contenido en dos contrastes; no se obtuvo mensaje de validación ni acceso verificable. Se abrió GET nuevo para recuperar la interfaz. No se concluye un defecto del producto ni un rechazo específico de formato a partir de las vistas vacías. | Duda pendiente; causa de la vista vacía no confirmada | `evidencias/2026-11-17_T09_login-formato-email-invalido.png`, `evidencias/2026-11-17_T09_login-formato-invalido-confirmado.png` |

Presupuesto conservador de A en el trabajo actual del 17/11: dos rechazos de esta continuación más el rechazo de la contraseña reemplazada comprobado anteriormente durante T10. No se realizarán más intentos negativos asociados a A. Los vacíos sin correo, el formato inválido y la cuenta inexistente no utilizan el identificador de A o B. No se observó CAPTCHA ni bloqueo en las respuestas legibles; no se afirma su inexistencia general.

Las capturas y las lecturas AX pueden corresponder a instantes distintos de una respuesta asíncrona. Se distinguen explícitamente: no se atribuye un mensaje a una imagen vacía ni se presenta una página vacía como evidencia de validación correcta.

### Remember Me — cierre controlado iniciado, reapertura pendiente

1. Se recuperó una pestaña GET con la landing y sin sesión después del intento de formato inválido.
2. Se abrió Login y se desmarcó Remember Me. Lectura AX: `checkbox Remember Me, Value: 0`. Evidencia: `evidencias/2026-11-17_T09_remember-me-desmarcado-antes-login.png`.
3. Se hizo Login válido de A con las credenciales actuales del secreto. La vista autenticada mostró Settings, Logout y los datos de A. Evidencia: `evidencias/2026-11-17_T09_remember-off-sesion-antes-cierre.png`.
4. El menú Window enumeró dos ventanas: la del correo del perfil original y Todo.ly del perfil QA. Se descartó ese menú mediante su acción accesible Cancel. Se verificó el título `Todo.ly - Google Chrome - Todo.ly QA cuenta B` y se pulsó el close button de esa ventana; no se usó Quit ni se borraron cookies.
5. La lectura posterior devolvió `timeoutReached`. Dos intentos de reenlazar Chrome y otro tras reiniciar la conexión CUA devolvieron el mismo error. El inventario indicó que Chrome seguía ejecutándose, pero no permitió comprobar la ventana ni reabrir el perfil. El host de acceso DOM también continuó no disponible.
6. Se solicitó al usuario reabrir el perfil QA y Todo.ly **sin introducir credenciales**, para observar si la sesión se conservó. Esa solicitud corresponde al procedimiento manual previsto por el usuario cuando Remember Me falla con la herramienta.

**Clasificación:** Duda pendiente. Se confirmó la casilla desmarcada y Login previo; el cierre intentado y sus errores no prueban qué estado tendría la sesión después de reabrir. Falta observar la reapertura y el contraste separado con Remember Me marcado. No se atribuye esta falla de control a un defecto de Todo.ly. La ventana del correo no fue objetivo de ninguna acción de cierre; su permanencia posterior aún no pudo verificarse por el timeout.

### Reapertura observada — Remember Me desmarcado

El usuario indicó que había reabierto el perfil sin Login. La primera ventana recibida por CUA correspondía a **Andre**, con un formulario de Login rellenado: no se pulsó Submit ni se usó esa ventana como evidencia del experimento. Su árbol conservaba las pestañas de TestLink, Jira y correo. Se seleccionó explícitamente **Todo.ly QA cuenta B** desde Profiles; ese perfil mostró una ventana con New Tab. Se abrió https://todo.ly/ sin introducir credenciales. Tras una carga inicialmente vacía, la lectura posterior mostró la landing pública con `javascript:ShowLogin();` y `javascript:ShowSignup();`, sin Settings ni Logout. Solo entonces se inició el siguiente contraste.

- **Resultado observado:** en el perfil correcto, después del cierre previo con Remember Me desmarcado, **no reapareció una sesión autenticada**.
- **Evidencia:** `evidencias/2026-11-17_T09_remember-off-reapertura-sin-sesion.png`; lectura AX confirma perfil y landing.
- **Límite:** la reapertura fue asistida por el usuario tras fallos de CUA y hubo un intervalo entre cierre y consulta. No se infiere una duración de sesión ni que todo el proceso de cierre/reapertura fuese automatizado sin interrupciones.
- **Siguiente contraste:** Remember Me marcado con B. Se verificó la casilla `Value: 1` antes del envío; las credenciales proporcionadas nuevamente por el usuario coinciden con el archivo privado. No se modifica el secreto ni se publica la contraseña. Login y reapertura marcados aún pendientes de resultado final.

### Reapertura observada — Remember Me marcado

La consulta GET posterior al envío de Login mostró el área autenticada; Settings confirmó Full Name Andre Cadima 4 y el correo de B. Se guardó `evidencias/2026-11-17_T09_remember-on-B-identidad-antes-cierre.png`. La casilla estaba marcada antes del Login, como muestra `evidencias/2026-11-17_T09_remember-me-marcado-antes-login.png`.

Se cerró exclusivamente la ventana cuyo título identificaba el perfil QA. La lectura inmediata volvió a dar timeoutReached. Esta vez se recuperó el control consultando Finder y reenlazando Chrome: reapareció la ventana original Andre con sus pestañas de Jira, TestLink y correo, sin operar su formulario de Todo.ly. Desde Profiles se seleccionó Todo.ly QA cuenta B; abrió New Tab, confirmando que la ventana anterior de QA ya estaba cerrada. Se abrió https://todo.ly/ sin introducir ninguna credencial nueva ni ejecutar Login.

La página mostró **Settings y Logout**, y al abrir Profile se confirmó de nuevo **Andre Cadima 4 y el correo de B**. Resultado: **la sesión autenticada de B reapareció al reabrir el perfil con Remember Me marcado**. Evidencia del área autenticada después de reabrir: `evidencias/2026-11-17_T09_remember-on-reapertura-autenticada.png`; identidad corroborada mediante AX de Profile.

Los resultados corresponden a dos recorridos independientes: A sin marcar y B marcado, en el mismo perfil local. No se deduce una caducidad ni un cierre completo del proceso Chrome; sus otros perfiles permanecieron abiertos. No se borraron cookies ni se alteraron contraseñas o correo. Se deja B autenticada con Settings abierto tras la comprobación.

Se cierra la exploración adicional para el diseño de T09. Permanecen pendientes el mensaje específico y la causa de la vista vacía con correo mal formado, las validaciones aisladas de cada campo de Signup, una exploración controlada del registro válido (los registros iniciales fueron completados por el usuario) y cualquier frontera de longitud. No se aplica análisis de valores límite sin esa frontera.
