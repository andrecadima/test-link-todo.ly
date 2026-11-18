# Continuidad T09–T11

Actualización: 17 de noviembre de 2026. **No se crearon casos en TestLink ni comentarios en Jira.**

## Instrucción vigente

Rige `PROMPT_ORQUESTACION.md` y las correcciones posteriores del usuario, por encima de notas antiguas. Orden T10 → T09 → T11 → cierre. T10 tiene OK del usuario. T09/T11 no requieren nuevo punto de control si la revisión independiente no tiene bloqueantes y los demás hallazgos se corrigen o documentan. No cambiar estados de Jira ni casos de otros tickets. Revisar es distinto de ejecutar y de la revisión de otro integrante.

Registrar dentro de la suite existente **Todo.ly tests**, sin nuevas suites ni actualizar casos existentes. XML de entrada con raíz `<testcases>`, nombres T0X-NN, sin IDs. Comprobar duplicados antes de importar y abrir cada caso después. Exportar realmente `testlink-xml/todo-ly-tests.xml` al final y extraer T09/T10/T11 con el script; los XML propuestos no son exportaciones.

El usuario autoriza credenciales de las cuentas de prueba de `.secrets/cuentas-prueba.local.md`, pero CUA requiere que el usuario introduzca y envíe las credenciales nuevas. No hay falta de autorización: es una limitación de la herramienta. Inicio de sesión normal y verificaciones sí pueden hacerse. No publicar secretos ni enviar el archivo a Claude.

## Respaldo y herramientas

- Branch master, remoto https://github.com/andrecadima/test-link-todo.ly.git. Respaldo inicial y preparación enviados; último commit anterior a estas correcciones: 0716dd1.
- Fase 0: 6a6b0a3; fase 1: 50f74c9. Ambas cuentas fueron creadas por el usuario y sus accesos se comprobaron. Estado inicial y capturas en el repositorio.
- Claude Code 2.1.327 instalado y autenticado, prueba OK. `.claude/settings.json` tiene los deny solicitados; Edit(path) cubre escrituras aunque la CLI advierta que Write(path) es redundante/no reconocido como regla de archivos.
- Encargos aislados con Read/Write/Edit/Glob/Grep, MCP vacío, navegador desactivado y sin comandos ni git. Cada encargo autoriza solo su archivo de respuesta. Nunca --continue entre encargos.
- Jira MCP autenticado, refresco de T09/T10/T11: En revisión (ya estaban así; no lo cambió Codex), responsable Andre, sin adjuntos ni comentarios. No marcar revisión ni modificar estado.
- TestLink: http://68.211.149.112, proyecto Todo.ly id1, suite Todo.ly tests id3; inventario inicial 48 casos. Recontar y comprobar nombres antes de importar.
- `scripts/preparar_importacion_testlink.py` ya genera `<testcases>` y pasos nativos. `scripts/extraer_xml_por_ticket.py` preserva casos/IDs de la exportación real; validado con fixture sintético en tmp, no con el servidor. `scripts/sincronizar_fichas.py` alinea JSON, fichas y borrador.

## T10 / PEB-74

Seis listos: 01/02/03/08/09/10 (28 pasos). Cuatro candidatos pendientes: 04/05/06/07. El 07 **no se registra**. Las acciones manuales a/b/c completan 04/05/06; no afirmar resultados aún.

Observado: Cancel/guardado de nombre y F5, restauración de nombre y persistencia en nueva sesión; recuperación recibida y cambio manual; contraseña reemplazada rechazada y actual aceptada; correo inexistente; Old Password vacío → Invalid Password y Login posterior con contraseña vigente. No se confirmó política de contraseñas ni cambio válido de email.

La revisión `01-T10-revision-respuesta.md` no encontró bloqueantes de contenido en los seis casos listos; objetó la raíz antigua del XML. Corregida a testcases. Resoluciones en `01-T10-resolucion.md`. Tras a/b/c, actualizar diseño, tabla de decisión y lanzar revisión nueva antes de registrar.

T10-08 paso 4 abre el enlace **tal como llega**, sin reemplazar HTTP por HTTPS. Si no muestra Please Enter a New Password durante la ejecución, es falla de ese caso. T10-10 exige HTTPS como Criterio del equipo; hallazgo a confirmar, todavía sin planilla de fallas. T10-08 compara únicamente identidad de Profile, no datos no relevados.

A todavía conserva la contraseña posterior a recuperación; **no se restauró la original**. El registro privado tiene actual, anterior/original y una copia de la reemplazada para evitar perder trazabilidad. No se modificó ninguna contraseña desde Settings en este bloque. Nombre y zona sí están restaurados. Después de a/b, distinguir C3 informada en las filas de la tabla: no inferir que guardar Profile con ambos campos vacíos sea inválido.

## T09 / PEB-73

**13 listos**, 01–07 y 09–14, 52 pasos. 08 email mal formado pendiente y excluido. Técnicas: particiones, tabla de decisión de seis reglas, transiciones de sesión y flujos. Sin fronteras confirmadas, no hay valores límite. Registro válido controlado y validaciones aisladas de Signup siguen pendientes.

`02-T09-revision-respuesta.md`: NO APTO por llamar Submit al botón visible Signup. Corregido y resuelto en `02-T09-resolucion.md`.

`03-T09-revision-respuesta.md`: **APTO, sin bloqueantes**. Las N1–N7 se corrigieron o documentaron en `03-T09-resolucion.md`. JSON/fichas/XML sincronizados. No publicar las capturas de exploración con correos reales, incluida la fuente cruzada T10; publicar solo árbol y casos genéricos TestLink. Su revisión no sustituye la de otro integrante.

Login: cuenta inexistente, Email vacío, Password vacío e incorrecto observados. A alcanzó el máximo conservador de tres rechazos del trabajo; no añadir negativos. Logout/Atrás/URL observados sin acceso autenticado. Marcadores propios A/B separados en ambos sentidos.

Remember Me: desmarcado con A → reapertura sin sesión; marcado con B → reapertura autenticada e identidad B confirmada, sin nuevo Login. Cada recorrido una vez, cuentas distintas, otros perfiles Chrome abiertos. No concluir duración ni cierre completo de Chrome. Timezone solo campo Signup; ambas cuentas base La Paz UTC-04, no efectos en vencimientos.

## T11 / PEB-75

Diseño **provisional**: 01/02/04/05 listos por reglas documentadas y criterio de integridad (22 pasos); 03 Cancel Editing y 06 movimiento de completada pendientes. No afirmar que los arrastres se observaron.

Observado en A: crear/seleccionar proyecto raíz temporal vacío, Options / Edit, Save, nombre persistente tras GET. Cancel Editing visible, efecto pendiente. Arrastre falló en herramienta sin cambio confirmado; no es restricción del producto. Portada oficial documenta subproyectos y movimientos.

Falta exploración focalizada de Cancel, subproyecto, tareas pendientes/completadas entre Home/Study, raíz ↔ subproyecto, conservación después de F5. Preparar una sola lista de arrastres para el usuario. Máximo una hora activa; duda de 15 min queda pendiente. Después encargo **diseno** a Claude (archivos autorizados), verificación por Codex y revisión independiente en llamada nueva. Sin tareas padre/subtareas ni eliminación de subproyectos de T08.

## Navegador: bloqueo actual y siguiente paso exacto

Última identidad comprobada en QA: **B**, Andre Cadima 4. El perfil dedicado es **Todo.ly QA cuenta B**. En esta continuación Chrome presenta Todo.ly vacío, sin árbol HTML; la captura muestra contenido vacío. El intento de activación devolvió `noWindowsAvailable`; reenlazar y recargar por AX no recuperó el contenido. No se completó todavía Logout B / Login A.

El usuario recuperó el perfil e indicó que B estaba autenticada. Se verificó realmente Settings / Profile: identidad B (Andre Cadima 4), email original de B y zona La Paz UTC-04. Se cerró Profile con Cancel y se pulsó Logout. El título pasó a Todo.ly Simple Todo List, pero el contenido quedó vacío: **no se confirmó visualmente la página pública ni se inició sesión en A**. Un GET nuevo y reenlazar Chrome no recuperaron el HTML; la captura siguió vacía y el clic de activación devolvió noWindowsAvailable. No es un fallo confirmado de Todo.ly. No hubo cambios de contraseña, correo ni registro privado en este bloque.

Siguiente paso: el usuario recupera la ventana de QA, abre Login e inicia sesión en A con Cuenta A → Contraseña actual del registro privado; deja Settings / Profile abierto. Desde ahí se retoma la lista a/b/c ya recibida, sin volver a pedir datos ni publicar claves. CUA requiere intervención del usuario antes de introducir y enviar nuevas credenciales. Codex verifica resultado y Login posterior. No operar simultáneamente mientras el usuario completa los cambios.

El perfil Chrome **Andre** conserva Jira/TestLink/correo y llegó a mostrar A autenticada; no usar su sesión Todo.ly para la exploración. El perfil Todo.ly QA T09-T11 con correo mal escrito está excluido e intacto. No cerrar otros perfiles, no borrar cookies globales.

CUA: después de compacción, rewriteDocumentation. AX fresco tras acciones; tras captura, AX completo antes de reutilizar índices. Reenlazar al cambiar perfil. Si un POST queda vacío, comprobar con GET nuevo y no reenviar formularios. Finder → Chrome resolvió una vez un timeout tras cerrar QA, pero no los errores posteriores de ventana.

## Datos reales para limpieza final

| Cuenta | Ubicación | Dato temporal real |
|---|---|---|
| A | Home | Prueba T09-aislamiento-A-1937 |
| B | Home | Prueba T09-aislamiento-B-1941 |
| A | Raíz | Prueba T11 - proyecto renombrado 1109, vacío |

No se crearon otros datos de T11 en esta preparación. Los nombres de las fichas son diseño, no inventario real. Conservar los proyectos predeterminados y cinco tutoriales de Work. Limpieza al final de los tres tickets, no eliminar cuentas. Comprobar configuración contra `estado-cuentas-inicial.md`, restauración de contraseña A/email B y vaciado de ambas papeleras con confirmación de la herramienta cuando corresponda.

## Fase 6 pendiente

Registrar y comparar cada caso; obtener IDs/enlaces/capturas; publicar comentarios solo en PEB-74/73/75 y comprobar formato. No cambiar estados. Guardar comentarios reales en `trabajo/jira-publicado.md`. Exportar suite real y extraer XML. Estado final de cuentas con evidencia, auditoría final independiente Claude y checklist §19, informe final, commit + push.

## Listas exactas del usuario — T10 (recibidas, no volver a pedir)

### AJUSTES 1 a 5 (aplicar antes de registrar T10)

1. Suite: no crear suites. XML con raíz <testcases>, importado dentro de Todo.ly tests, con nombres T10-NN.
2. T10-08, paso 4: «Abrir el enlace de recuperación tal como llega en el correo» → se muestra Please Enter a New Password. No cambiar el enlace a HTTPS a mano; lo evalúa T10-10. Si en ejecución el enlace HTTP no carga el formulario, es una falla de T10-08.
3. Precondiciones: en T10-08 y T10-09, y cualquier caso de T09/T11 que lo diga, sustituir «Sesión de Todo.ly cerrada en el perfil dedicado de QA» por «Sin sesión iniciada en Todo.ly en el navegador».
4. Pendientes: completar T10-04/05/06 con a/b/c. T10-07 (cambio válido de email) queda como cobertura pendiente del comentario y no se registra.
5. Tabla de decisión de Settings tras confirmar a/b: C1 Old Password informado; C2 Old Password coincide con la vigente; C3 New Password informado. C1 No → Invalid Password (T10-03); C1 Sí/C2 No → rechazo con mensaje observado (T10-04); C1/C2/C3 Sí → cambio aceptado (T10-05). New Password vacío queda Duda pendiente si no se observa.

### PASOS MANUALES a), b), c) — a cargo del usuario

- a) Cuenta A, Settings, T10-04: Old Password con un valor incorrecto inventado; New Password = contraseña original de A; Ok; captura del mensaje.
- b) Cuenta A, Settings, T10-05: Old Password = vigente de A; New Password = original de A; Ok; captura. Cambio válido y restauración de A; usuario actualiza .secrets.
- c) Cuenta B, Settings, T10-06: Email = andrecadimaschool+todoly-cambio@gmail.com; Cancel, nunca Ok; captura.
- Después Codex verifica Login de A con la original (reemplazada solo un intento si se contrasta) y correo original de B conservado.

**Bloque único ya solicitado al usuario:** incluye Logout B/Login A, a con dato sintético Prueba-T10-04-incorrecta y referencias Cuenta A → Contraseña anterior/original y Contraseña actual; después b, Logout A/Login B y c; dejar Profile de B abierto. Pendiente respuesta, no repetir la solicitud. Si a se acepta inesperadamente, detener y registrar el hecho sin asumir que se rechazó. No operar el navegador mientras el usuario introduce/envía los cambios.
