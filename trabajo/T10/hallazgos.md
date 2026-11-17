# Hallazgos de exploración — T10 / PEB-74

## Enlace de recuperación entregado con HTTP

- **Estado:** observación de seguridad reproducible; pendiente de revisión del equipo y de reporte en su plantilla. No publicado en Jira ni TestLink.
- **Fecha:** 17 de noviembre de 2026.
- **Entorno:** Chrome 157.0.8103.51, macOS 26.6.2; perfil aislado `Todo.ly QA cuenta B`.
- **Precondiciones:** cuenta gratuita A con buzón controlado por quien realiza la prueba; sesión de Todo.ly cerrada en el perfil de QA; correo de recuperación disponible.
- **Fundamento del esperado:** **Criterio del equipo**, establecido expresamente por el usuario el 17/11/2026: el enlace de recuperación debe usar HTTPS. No se presenta como una regla textual del producto o de las diapositivas. El hallazgo queda para confirmar durante la ejecución del caso; no se reporta todavía en la planilla de fallas.

### Pasos para reproducir

1. Abrir Todo.ly y desplegar `Login`.
2. Seleccionar `Reset your Password`.
3. Escribir el correo de la cuenta de prueba y pulsar `Send`.
4. Abrir el mensaje `Forgot Password` recibido en el buzón controlado.
5. Revisar el esquema del enlace directo alternativo: `http://todo.ly/verifypass/[TOKEN PRIVADO]`.
6. Abrir ese enlace en el perfil de QA y observar el indicador de conexión de Chrome, sin introducir una contraseña.

### Resultado observado

El correo recibido a las 11:12 incluye el enlace directo con esquema HTTP. Al abrirlo, Chrome muestra `Not Secure`. El enlace principal visible también utiliza HTTP, aunque su destino real pasa por un servicio de seguimiento; para esta comprobación se abrió exclusivamente el enlace directo alternativo de Todo.ly.

La misma ruta y token abiertos con HTTPS muestran el formulario `Please Enter a New Password`, los campos `Enter a New Password` y `Verify New Password`, y el botón `Done`. No se envió una nueva contraseña por el agente.

### Resultado esperado — Criterio del equipo

El mensaje entrega enlaces HTTPS; la apertura del enlace de recuperación y del formulario mantiene una conexión segura. El criterio fue confirmado por el usuario; falta ejecutar formalmente el caso y registrar su resultado.

### Impacto y límites de la comprobación

El token de recuperación aparece en una URL HTTP que autoriza un cambio de credencial. Esto plantea un riesgo de exposición del token durante el transporte si la conexión no se protege. No se interceptó tráfico, no se explotó el token y no se comprobó una toma de cuenta. Tampoco se comprobó el transporte de una contraseña enviada desde HTTP, porque no se introdujo ni envió ninguna.

El contenido vacío observado en la pestaña HTTP queda como duda: el control nativo también presenta cargas vacías y errores de captura. No se debe informar que la recuperación falla basándose en esa vista.

### Evidencia y tratamiento de secretos

La observación proviene del correo autorizado, la lectura de accesibilidad y una captura temporal inspeccionada. No se incorpora una captura completa del mensaje o de la barra de direcciones al repositorio porque expone el token. El token y los enlaces reales no deben pegarse en Jira, TestLink ni la planilla de fallas. Severidad y prioridad de reporte pendientes de revisión del equipo.
