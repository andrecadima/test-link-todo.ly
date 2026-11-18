# Continuidad T09–T11

Actualización: 17 de noviembre de 2026. Estado actual: diseños de T10 y T09 presentados para OK; T11 provisional y acceso visual bloqueado. **Todavía no se crearon casos en TestLink ni comentarios en Jira.**

## Prioridad y autorización vigentes

- Demo: 18 de noviembre. Trabajar T10 → T09 → T11, con aproximadamente una hora máxima de exploración adicional por ticket y dudas explícitas para lo no resuelto.
- Seguir sin los cuatro PDF faltantes; no releer los originales completos. Contexto y definiciones están en `trabajo/00-contexto.md`.
- Punto de control por ticket antes de escribir en Jira/TestLink. Mientras el usuario revisa, avanzar con el siguiente. No interpretar un mensaje genérico de continuar como aprobación de un diseño no revisado.
- **Solicitud de aprobación conjunta ya enviada**: T10 (seis casos con cuatro candidatos pendientes) y T09 (trece casos con T09-08 pendiente). Opciones: aprobar ambos, solo T10 o pedir ajustes. Pendiente respuesta; no volver a pedir lo mismo sin necesidad.
- Con OK: registrar, abrir y comparar cada caso, anotar IDs/enlaces reales, capturar suite/caso, exportar XML real, publicar comentario del ticket, verificar formato y commit + push. No cambiar estados de Jira ni marcar revisión de otro integrante.
- Limpieza de datos de A/B al terminar los tres tickets. No borrar cuentas, proyectos predeterminados ni tutoriales.

## Terminado y respaldado

- Fase 0: fuentes, alcance, criterios, técnicas y mapeo de TestLink; commit 6a6b0a3.
- Fase 1: Login A/B e inventario de ambas con capturas; commit 50f74c9. El usuario creó las cuentas para la práctica. B vigente tiene Full Name Andre Cadima 4.
- Credenciales actuales en `.secrets/cuentas-prueba.local.md`, ignorado por Git; ambas fueron verificadas mediante Login. No publicar valores. A conserva además su contraseña anterior para restaurar.
- Respaldo inicial al remoto realizado; commits posteriores también enviados. Remoto: https://github.com/andrecadima/test-link-todo.ly.git. Último diseño enviado antes de esta actualización: 36f7320 (T09).

## T10 / PEB-74 — presentado para revisión

- `trabajo/T10/analisis-diseno.md`: análisis, riesgos, particiones, flujos y fichas completas.
- **Seis casos listos:** T10-01/02/03/08/09/10, fuente `casos-listos.json`.
- **Cuatro candidatos fuera del registro:** T10-04/05/06/07, fuente `casos-pendientes.json`.
- Observados: Cancel/guardado del nombre y persistencia, restauración del nombre; recuperación A, correo recibido y formulario; contraseña reemplazada rechazada y nueva aceptada; correo inexistente rechazado; Old Password vacío → Invalid Password y conservación de la credencial previa comprobada por Login.
- Pendientes: Old Password incorrecto, cambio válido/restauración desde Settings, Cancel específico de Email y cambio válido de Email/posible verificación. No se afirma que el producto exija verificar correo.
- La herramienta CUA exige entrada y envío manuales de nuevas credenciales. El usuario pidió delegar esos cambios: se explicó la limitación y se cerraron como pendientes, **sin reiterar solicitudes de cambio manual**. No es falta de autorización del usuario.
- La contraseña actual de A, posterior a recuperación, sigue vigente; la original no se restauró. El nombre y zona de referencia sí están restaurados.
- HTTPS del enlace de recuperación es Criterio del equipo expreso. T10-10 lo comprueba como seguridad observable; HTTP previo es hallazgo para confirmar en ejecución. No reportar todavía en planilla de fallas.
- `comentario-jira-borrador.md` contiene análisis/lista sin fichas. `importacion-propuesta.xml` contiene seis casos/28 pasos, sin IDs asignados. No es exportación real ni registro comprobado.

## T09 / PEB-73 — presentado para revisión

- `trabajo/T09/analisis-diseno.md`: análisis, particiones, tabla de decisión de seis reglas, matriz/secuencias de estados, flujos y fichas.
- **Trece casos listos:** T09-01/02/03/04/05/06/07/09/10/11/12/13/14. XML propuesto: trece casos/52 pasos, sin IDs asignados.
- **T09-08 pendiente:** correo sin formato provocó vistas vacías; no se fijó mensaje o validador sintáctico. Registro válido controlado, validaciones aisladas de Signup y fronteras siguen como cobertura pendiente.
- Login rechazó cuenta inexistente, Email vacío con contraseña, A con Password vacío y A con contraseña incorrecta. A alcanzó el máximo conservador de tres rechazos del trabajo actual (incluye uno anterior de T10): no hacer más negativos con A.
- Logout, Atrás y URL directa no mostraron datos autenticados. Marcadores de A/B separados en ambos sentidos.
- **Remember Me observado en ambos recorridos:** A desmarcado → cierre/reapertura asistida → landing sin sesión; B marcado → cierre/reapertura → área autenticada e identidad B confirmada en Profile, sin nuevo Login. Mismo perfil local; otros perfiles Chrome quedaron abiertos. Intervalos e interrupciones documentados, sin deducir caducidad.
- Timezone se limita al campo Signup. La opción base de ambas cuentas es La Paz UTC-04; no confundir con la opción mexicana UTC-07 ni probar vencimientos.

## T11 / PEB-75 — provisional, exploración visual bloqueada

- Observación anterior en A: crear/seleccionar raíz temporal vacía, Options / Edit, Save y nombre persistente en GET nuevo. Cancel Editing visible; efecto no contrastado. Un arrastre anterior falló en la herramienta, sin cambio observado del árbol.
- `trabajo/T11/analisis-diseno.md` prepara cuatro fichas de resultado definido: T11-01/02/04/05. T11-03 (Cancel Editing) y T11-06 (completada) quedan pendientes y fuera del registro propuesto.
- La portada oficial https://todo.ly/ fue consultada como documentación pública: describe subproyectos por arrastre y tareas entre proyectos. Esa documentación y el criterio del usuario de conservación fundamentan T11-04/05; **no se afirma que se hayan ejecutado ni observado los arrastres en las cuentas**.
- Sin unicidad, longitud o profundidad máxima confirmadas. Regreso a raíz, reordenación, movimiento de completadas y atributos no visibles/preparados siguen pendientes. No se incluyen tareas padre/subtareas ni eliminación de subproyectos de T08.
- Al intentar retomar a las 23:47 UTC, Chrome y Finder devolvieron `cgWindowNotFound`, también tras reset de CUA. Reintento posterior confirmó el mismo error. No hubo mutaciones adicionales de T11.
- **Solicitud de recuperación visual ya enviada:** dejar Mac desbloqueado y Chrome QA visible, sin credenciales ni cambios de datos. Pendiente respuesta. No atribuir el fallo al producto ni pedir otra vez cambios de contraseñas.

## Último estado visual y datos reales pendientes de limpieza

Último estado comprobado: perfil **Todo.ly QA cuenta B**, B autenticada y Settings / Profile abierto tras Remember Me. El estado actual no es visible por cgWindowNotFound: consultar identidad nuevamente antes de cualquier acción.

| Cuenta | Ubicación | Dato temporal real |
|---|---|---|
| A | Home | Prueba T09-aislamiento-A-1937 |
| B | Home | Prueba T09-aislamiento-B-1941 |
| A | Raíz | Prueba T11 - proyecto renombrado 1109, vacío |

Los datos con códigos de las fichas son **datos de diseño todavía no creados**. Work conserva sus cinco tareas tutoriales y todos los proyectos predeterminados. La sesión con correo mal escrito del perfil Todo.ly QA T09-T11 queda excluida e intacta. El perfil Andre conserva Jira/TestLink/correo y un formulario de Todo.ly rellenado: no usarlo para Login o pruebas.

## Herramientas y preparación para registro

- Jira MCP autenticado funciona; TestLink se consultó por Chrome, sin escrituras. Host DOM de navegador no disponible.
- CUA: usar lecturas frescas y la acción expuesta Raise antes de operar. Después de captura, obtener AX completo antes de reutilizar índices. Reenlazar tras cambiar ventana/perfil. No repetir mutaciones en Loading: consultar resultado con GET nuevo.
- Timeout tras cerrar ventana QA: consultar `cua.getApp('Finder')` y reenlazar Chrome permitió recuperar la ventana original; después Profiles → QA. Esto resolvió el cierre de Remember Me marcado. **No resolvió el cgWindowNotFound posterior.**
- El menú Window se descartó mediante su acción accesible Cancel; Escape no produjo un cierre fiable. No usar Quit ni borrar cookies globales.
- `scripts/preparar_importacion_testlink.py` genera XML local con pasos nativos desde casos-listos.json, contrastado con código oficial 1.9.20. No conecta con el servidor ni asigna IDs. Importar solo tras OK y comprobar antes el árbol para evitar duplicados. La exportación real final se obtiene del servidor después de verificar todos los casos.
- Mantener siempre distinto: diseño, documento público, comportamiento observado, registro real, revisión y ejecución. Las capturas de avisos transitorios pueden no contener el mensaje leído por AX; los registros señalan esa diferencia.
