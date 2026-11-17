# Continuidad T09–T11

Actualización: 17 de noviembre de 2026.

## Prioridad vigente para la demo

- Respaldo inicial realizado: `git push origin master`, seis commits hasta 6ef1597 enviados correctamente el 17/11. Remoto: https://github.com/andrecadima/test-link-todo.ly.git.
- Orden de principio a fin: T10 → T09 → T11. Exploración adicional aproximada de una hora como máximo por ticket; después declarar dudas pendientes, sin ampliar indefinidamente.
- Seguir sin los cuatro PDF faltantes y sin releer completos los PDF disponibles.
- Punto de control por ticket. Mientras el usuario revisa su diseño, explorar el siguiente. Solo con OK registrar ese ticket en TestLink y comentarlo en Jira; después actualizar continuidad, commit y push. Limpieza de marcadores/proyecto al terminar los tres.
- Borrador local T10 creado: `trabajo/T10/analisis-diseno.md` y diez fichas fuente en `trabajo/T10/casos.json`. Aún NO presentado como diseño cerrado ni aprobado: cuatro candidatos de contraseña/correo siguen pendientes de reglas/contrastes; restauración de A pendiente.
- Captura manual del usuario a las 14:38 leída: Old Password vacío, New Password informado y aviso Invalid Password. Guardada en T10/evidencias; T10-03 actualizado con regla de rechazo observada, conservación de acceso aún por contrastar.
- Nuevo traspaso manual solicitado: probar Old Password incorrecto; si se rechaza, restaurar mediante Old Password correcto y New Password original; actualizar .secrets solo si se acepta. Si el intento incorrecto fuera aceptado, detenerse y registrar la credencial resultante. Pendiente respuesta; no operar la pantalla mientras el usuario introduce credenciales.
- Borrador T10 ahora tiene seis fichas con resultados principales definidos y cuatro candidatos pendientes (T10-04/05/06/07); T10-08 conserva dependencia de la restauración desde Settings. El tiempo de espera por intervención manual no es tiempo de exploración activa.
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
- No se alcanzó aún el punto de control de diseño. No escribir en Jira/TestLink hasta presentar análisis/artefactos/casos y recibir OK.

## Datos temporales que permanecen

| Cuenta | Ubicación | Dato |
|---|---|---|
| A | Home | Prueba T09-aislamiento-A-1937 |
| B vigente | Home | Prueba T09-aislamiento-B-1941 |
| A | Raíz de Projects | Prueba T11 - proyecto renombrado 1109, vacío |

Las cinco tareas tutoriales de Work y todos los proyectos predeterminados permanecen. No se probaron jerarquías de tareas. Profile de A está restaurado a Andre Cadima y zona La Paz. Hay varias pestañas abiertas del perfil Todo.ly QA cuenta B; tras Logout las pestañas antiguas pueden mostrar vistas obsoletas. Verificar identidad y estado con una consulta nueva antes de actuar.

## Herramientas y cautelas observadas

Jira MCP funciona; no se realizaron escrituras. TestLink se consultó mediante Chrome. El host de acceso DOM al navegador no está disponible. CUA nativo sufre fallos intermitentes de captura y pestañas sin contenido; abrir una pestaña GET nueva permitió recuperar la vista. No repetir mutaciones cuando Loading queda visible: primero verificar su resultado en una consulta nueva. Reenlazar cua.getApp después de cambiar de ventana/perfil y derivar índices de la última lectura. Invocar la acción expuesta `Raise` de la ventana antes de operar permitió que Settings y Login respondieran durante la verificación de recuperación; sin ella hubo clics sin efecto y `noWindowsAvailable`.
