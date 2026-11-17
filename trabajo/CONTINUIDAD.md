# Continuidad T09–T11

Actualización: 17 de noviembre de 2026.

## Prioridad vigente para la demo

- Respaldo inicial realizado: `git push origin master`, seis commits hasta 6ef1597 enviados correctamente el 17/11. Remoto: https://github.com/andrecadima/test-link-todo.ly.git.
- Orden de principio a fin: T10 → T09 → T11. Exploración adicional aproximada de una hora como máximo por ticket; después declarar dudas pendientes, sin ampliar indefinidamente.
- Seguir sin los cuatro PDF faltantes y sin releer completos los PDF disponibles.
- Punto de control por ticket. Mientras el usuario revisa su diseño, explorar el siguiente. Solo con OK registrar ese ticket en TestLink y comentarlo en Jira; después actualizar continuidad, commit y push. Limpieza de marcadores/proyecto al terminar los tres.
- Diseño T10 cerrado para punto de control: seis casos listos T10-01/02/03/08/09/10 en `trabajo/T10/casos-listos.json`; cuatro candidatos T10-04/05/06/07 en `casos-pendientes.json`, excluidos del registro propuesto. Fichas y artefactos en `analisis-diseno.md`.
- Captura manual de las 14:38: Invalid Password con Old Password vacío. Después se descartó el formulario y se verificó Login con la misma credencial previa; identidad A confirmada en Settings. T10-03 tiene rechazo y conservación observados.
- El usuario pidió delegar también los cambios de credenciales. Se explicó la limitación de CUA y se cerró la exploración adicional sin reiterar solicitudes manuales. No se modificó contraseña ni Email. Restauración de A y reglas de cambio/cancelación de Email pendientes, sin atribuir necesidad de verificación al producto.
- Mantener el punto de control solicitado: presentar seis casos registrables y cuatro pendientes, esperar OK antes de TestLink/Jira. Mientras se revisa, explorar T09. La delegación general no se interpreta como aprobación de un diseño aún no presentado.
- Settings no presenta confirmación de contraseña. Nombre vacío enviado una vez: Loading; nueva consulta conserva el nombre original, sin mensaje fiable. No convertirlo en una regla ni continuar buscando fronteras sin evidencia.
- HTTPS del enlace es ahora Criterio del equipo expreso; T10-10 diseñado para confirmarlo durante ejecución. No reportar aún en la planilla de fallas.

## Terminado

- Fase 0: contexto y originales locales leídos; commit 6a6b0a3.
- Fase 1: Login A y B vigente comprobados, estado inicial y capturas; commit 50f74c9. Secretos ignorados por Git. B vigente es Andre Cadima 4; usar exclusivamente los datos actuales de .secrets, sin copiar correos o contraseñas desde registros anteriores.
- T09: Logout, Atrás y URL directa tras cierre; separación de dos marcadores en ambos sentidos.
- T10: Cancel del nombre, guardado del nombre y persistencia tras recarga; nombre inicial restaurado y comprobado. Solicitud de recuperación de A confirmada por interfaz y rechazo de correo inexistente observado.
- T11: crear y seleccionar proyecto raíz temporal vacío; renombrarlo y conservar el nombre en una nueva consulta.

## En curso / pendiente

- La fase 2 NO está terminada. Faltan combinaciones de Login y Remember Me controlado; comprobaciones restantes de perfil/credenciales; proyectos/subproyectos y movimientos.
- Recuperación de A completada manualmente por el usuario. Se verificó rechazo de la contraseña anterior en un intento y Login exitoso con la actual; identidad, nombre y zona inicial confirmados en Profile. Contraseña anterior conservada en el secreto local; la actual sigue vigente y está pendiente restaurarla manualmente con el usuario. No almacenar ni publicar el token.
- `trabajo/T10/hallazgos.md` contiene pasos para reproducir la entrega del enlace HTTP y el indicador Not Secure observado. Es una observación de seguridad para revisión, sin explotación ni reporte externo. La carga vacía no se atribuye al producto.
- La herramienta CUA exige control del usuario antes de introducir nuevas contraseñas u otras credenciales. El usuario ya autorizó crear cuentas y aceptar los términos; no volver a pedir esas autorizaciones. Para cambios de contraseña/correo corresponde un traspaso de control, no permiso repetido.
- Drag de proyecto devolvió noWindowsAvailable; la consulta siguiente mantuvo el proyecto temporal en raíz. No atribuir una restricción a Todo.ly por esa falla de herramienta.
- Faltan cuatro PDF de clase, enumerados en 00-contexto.md. No suponer su contenido.
- T10 preparado para su punto de control por ticket; pendiente OK del usuario. No escribir en Jira/TestLink sin ese OK. T09 y T11 aún sin diseño cerrado.

## Datos temporales que permanecen

| Cuenta | Ubicación | Dato |
|---|---|---|
| A | Home | Prueba T09-aislamiento-A-1937 |
| B vigente | Home | Prueba T09-aislamiento-B-1941 |
| A | Raíz de Projects | Prueba T11 - proyecto renombrado 1109, vacío |

Las cinco tareas tutoriales de Work y todos los proyectos predeterminados permanecen. No se probaron jerarquías de tareas. Profile de A está restaurado a Andre Cadima y zona La Paz. Hay varias pestañas abiertas del perfil Todo.ly QA cuenta B; tras Logout las pestañas antiguas pueden mostrar vistas obsoletas. Verificar identidad y estado con una consulta nueva antes de actuar.

## Herramientas y cautelas observadas

Jira MCP funciona; no se realizaron escrituras. TestLink se consultó mediante Chrome. El host de acceso DOM al navegador no está disponible. CUA nativo sufre fallos intermitentes de captura y pestañas sin contenido; abrir una pestaña GET nueva permitió recuperar la vista. No repetir mutaciones cuando Loading queda visible: primero verificar su resultado en una consulta nueva. Reenlazar cua.getApp después de cambiar de ventana/perfil y derivar índices de la última lectura. Invocar la acción expuesta `Raise` de la ventana antes de operar permitió que Settings y Login respondieran durante la verificación de recuperación; sin ella hubo clics sin efecto y `noWindowsAvailable`.
