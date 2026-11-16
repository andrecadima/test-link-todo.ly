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
