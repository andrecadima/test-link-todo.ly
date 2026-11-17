# Continuidad T09–T11

Actualización: 17 de noviembre de 2026.

## Terminado

- Fase 0: contexto y originales locales leídos; commit 6a6b0a3.
- Fase 1: Login A y B vigente comprobados, estado inicial y capturas; commit 50f74c9. Secretos ignorados por Git. B vigente es Andre Cadima 4; usar exclusivamente los datos actuales de .secrets, sin copiar correos o contraseñas desde registros anteriores.
- T09: Logout, Atrás y URL directa tras cierre; separación de dos marcadores en ambos sentidos.
- T10: Cancel del nombre, guardado del nombre y persistencia tras recarga; nombre inicial restaurado y comprobado. Solicitud de recuperación de A confirmada por interfaz y rechazo de correo inexistente observado.
- T11: crear y seleccionar proyecto raíz temporal vacío; renombrarlo y conservar el nombre en una nueva consulta.

## En curso / pendiente

- La fase 2 NO está terminada. Faltan combinaciones de Login y Remember Me controlado; comprobaciones restantes de perfil/credenciales; proyectos/subproyectos y movimientos.
- Se pidió al usuario confirmar recepción y contenido del correo de recuperación de A. No acceder al buzón. No almacenar ni publicar un enlace de recuperación con token en los documentos.
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

Jira MCP funciona; no se realizaron escrituras. TestLink se consultó mediante Chrome. El host de acceso DOM al navegador no está disponible. CUA nativo sufre fallos intermitentes de captura y pestañas sin contenido; abrir una pestaña GET nueva permitió recuperar la vista. No repetir mutaciones cuando Loading queda visible: primero verificar su resultado en una consulta nueva. Reenlazar cua.getApp después de cambiar de ventana/perfil y derivar índices de la última lectura.
