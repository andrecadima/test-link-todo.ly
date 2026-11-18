## T09 cerrado registro/publicación — vigente
13 casos TL-72 a TL-84,171pasos,435 textos comparados sin diferencias; comentarioPEB-73 **10227** publicado y leído porMCP, tablas ymedia presentes. CapturavisualJirapendientever. No reimportarT09.

# Actualización vigente — 18/11/2026, 16:20

- Usuario completó T10 a/b/c. Capturas originales convertidas y leídas: a Invalid Password; b Settings cerrado, aceptación reportada sin mensaje literal; c B Email original conservado, AX completo contrastado con registro privado.
- A: un intento con reemplazada rechazado; Login con original aceptado e identidad Profile verificada. `.secrets` actual = original, actualizado sin publicar claves. Evidencia y AX en T10.
- Claude encargo07 diseña SOLO 04/05/06 y actualiza análisis T10; no editar sus archivos hasta terminar. Después revisión independiente08, importar SOLO esos tres y actualizar comentario10226 conservando nodos/media.
- T09 revisión06 APTO, no bloqueantes resueltos en06-resolucion. XML13 casos171pasos. Ausencia previa comprobada filtroT09→0; global70. Importación enviada UNA vez en suite3 con omitirduplicados. **Resultado todavía por observar: no volver a pulsar Upload sin comprobar árbol.**
- T11 Cancel Editing observado: nombre temporal descartado y original en árbol. Recarga dejó contenido omitido por herramienta; persistencia tras recarga aún por comprobar. No atribuir a producto.
- Navegador liberado por usuario; Chrome Andre TestLink import result actual, Incognito A autenticada despuésrecarga. Solo arrastres humanos pendientes T11.
- Revision-testlink con cuatro archivos contienen credencial heredada; intactos y excluidos exactamente. Copias cifradas y manifiesto en trabajo/resguardos-revision, clave solo.secrets; restauraciónbyteporbyteprobada. Archivos segurosdelotroagenteincluirmanteniéndolosintactos.

---

# Continuidad T09–T11

Actualización: **18/11/2026, demo hoy**. Orden vigente T10 → T09 → T11 → cierre. Rigen PROMPT_ORQUESTACION.md y mensajes posteriores del usuario. **No cambiar estados de Jira ni casos ajenos; revisión de integrante pendiente.**

**Prioridad resuelta por el usuario:** terminar T09, T11 y fase 6. PROMPT_REVISION_TESTLINK.md pertenece a otro agente Claude que trabaja por API; no limita nuestras publicaciones en Jira. Codex no modifica casos de otros tickets. Aplicar su rúbrica solo a fichas T09/T11 antes del registro. Incluir archivos nuevos de revision-testlink/ en commits sin modificarlos, respetando la prohibición de publicar secretos. Se solicitó nuevamente el bloque manual T10 a/b/c el 18/11 por instrucción expresa; faltan resultados. No repetirlo hasta que responda.

## Estado exacto

- **T10 registrado y publicado, cobertura parcial explícita:** seis casos, 28 pasos, TL-66 a TL-71, comparados individualmente sin diferencias. Comentario Jira **10226** en https://alesalve.atlassian.net/browse/PEB-74?focusedCommentId=10226. Tres imágenes adjuntas; seis tablas con anchos corregidos, formato revisado visualmente. Estado Jira En revisión, sin cambios por Codex. Copia real HTML y metadata en trabajo/T10/jira-publicado.* y agregado trabajo/jira-publicado.md.
- **T09:** trece casos listos, 171 pasos tras la nueva rúbrica; revisión 03 anterior APTO y nueva revisión 06 en curso, sin bloqueantes. N1–N7 corregidos/documentados. **Todavía NO importado ni publicado.** T09-08 excluido por resultado sin regla confirmada. No explorar más salvo duda del resultado principal.
- **T11:** diseño provisional de cuatro casos 01/02/04/05 y candidatos 03/06 pendientes. Falta exploración focalizada, encargo diseno Claude y revisión independiente nueva. No registrarlo como definitivo aún.
- **Cierre:** limpieza, restauración de A, exportación real, auditoría final e informe todavía pendientes. No afirmar fase 6 completada.

## Siguiente paso inmediato

1. Hecho: cierre de registro/publicación T10 respaldado y enviado en 89ec619, sin .secrets.
2. En Chrome Andre, volver a la pestaña TestLink. El filtro T10- está activo y muestra seis: **es contador filtrado, no total global**. Reset Filters antes de comprobar duplicados de T09. Renovar Login si expiró usando el registro privado; no pedir otra vez claves.
3. Comprobar que no existan T09. Regenerar XML desde casos-listos.json con raíz testcases, suite existente Todo.ly tests id3, duplicados mismo nombre → Do not import the test case. Importar una sola vez y verificar antes de cualquier reintento.
4. Abrir/comparar los 13, guardar IDs/enlaces/capturas, publicar PEB-73 con técnicas y artefactos, revisar formato y copiar comentario real. Actualizar continuidad, commit + push.
5. T11: explorar Cancel Editing y preparar datos propios para movimientos. Pedir los arrastres al usuario en **una sola lista por ticket**, con nombres y orden exactos. No atribuir fallas de la herramienta a restricciones del producto. Después Claude diseno y revisión nueva, registro/publicación igual a T09.

## T10: hechos y cobertura pendiente

| Caso | ID real | Interno | Pasos |
|---|---|---|---|
| T10-01 | TL-66 | 211 | 4 |
| T10-02 | TL-67 | 217 | 6 |
| T10-03 | TL-68 | 225 | 5 |
| T10-08 | TL-69 | 232 | 7 |
| T10-09 | TL-70 | 241 | 3 |
| T10-10 | TL-71 | 246 | 3 |

Enlaces reales en trabajo/T10/testlink-registro.json. Summary, Preconditions, pasos/resultados, Importance y Manual coinciden. Estado TestLink **Draft**, sin ejecución formal ni revisión de integrante. Evidencia textual por caso en verificacion/, sin form_token; resultado.json resume comparación. El árbol tenía 64 antes y 70 después de la importación del 17/11. No reimportar los seis.

Pendientes **T10-04/05/06**, pasos manuales a/b/c sin observar. **T10-07 no se registra** por instrucción expresa. A aún no se observó restaurada: la última lectura privada tenía contraseña actual distinta de anterior/original. Validar nuevamente antes del cierre por si el usuario actualizó el archivo. Nombre y zona sí estaban restaurados; B conservaba email original. No inventar mensajes ni la tabla Settings sin a/b.

T10-08 abre enlace como llega, sin sustituir HTTP por HTTPS. Si no carga el formulario en ejecución, falla ese caso. HTTPS es Criterio del equipo separado en T10-10. No reportar aún HTTP en planilla. Restauración de clave fuera de T10-08 y pendiente. No publicar capturas de exploración con correos reales; usar capturas genéricas de TestLink.

## T09: contexto ya observado

13 listos: 01–07 y 09–14. 08 mal formato pendiente; vistas vacías sin causa confirmada. Registro válido controlado, validaciones aisladas de Signup y límites pendientes. No BVA sin frontera.

Login: vacíos, inexistente e incorrecta documentados. A alcanzó tres rechazos conservadores del trabajo anterior: no añadir negativos innecesarios. Logout/Atrás/URL sin datos autenticados. Marcadores A/B separados. Remember Me: una observación desmarcado A → reapertura sin sesión; marcado B → identidad B restaurada sin nuevo Login. Otros perfiles permanecieron abiertos; no inferir caducidad ni cierre completo de Chrome. Timezone solo campo Signup, La Paz UTC-04, no vencimientos.

## T11: base anterior y alcance

En A se creó/seleccionó raíz vacía y se renombró; nombre persistente en GET. Cancel Editing visible, efecto no observado. Portada oficial describe subproyectos y movimientos: reglas documentadas, no arrastres observados. Falta raíz ↔ subproyecto, mover pendiente/completada entre Home/Study y conservación con F5. Sin límite de profundidad confirmado. No tareas padre/subtareas ni eliminación de subproyectos de T08. Máximo una hora activa; dudas de más de 15 minutos se documentan.

## Accesos y reglas de herramientas

- Repo master, remoto https://github.com/andrecadima/test-link-todo.ly.git. Último cierre respaldado y enviado: 89ec619 (T10 registrado y publicado). Fase 0: 6a6b0a3; fase 1: 50f74c9.
- Secretos solo .secrets/cuentas-prueba.local.md, ignorado, permiso 600. Cuentas A/B y sección TestLink. El usuario pidió recordar acceso TestLink: ya guardado privadamente, no pedirlo ni copiarlo a Claude, memorias, comentarios o git. La memoria añadida contiene solo el puntero al archivo, ningún valor.
- CUA exige que el usuario introduzca/envíe nuevas credenciales. Es una limitación de la herramienta, no falta de autorización. **Login con credenciales existentes sí está autorizado**. No cambiar claves por otra vía para eludir la limitación.
- Jira MCP funciona; escribir solo comentarios/adjuntos en PEB-73/74/75. Mantener estados. Comentarios 73/75 pendientes; 74 publicado.
- TestLink http://68.211.149.112, proyecto TL:Todo.ly id1, suite existente Todo.ly tests id3. Nunca crear suites ni actualizar casos existentes al importar. Entrada testcases, sin IDs. Exportación real final todo-ly-tests.xml; extraer T09/T10/T11 por script.
- Claude Code 2.1.327 autenticado, opus. Encargos aislados solo Read/Write/Edit/Glob/Grep, MCP vacío, navegador y comandos desactivados; .claude/settings.json niega .secrets. No --continue. Respuestas 01/02/03/04 disponibles. 03 T09 APTO; 04 T10 APTO seis casos. No sustituye revisión de integrante.

## CUA: continuidad práctica

El host DOM del navegador no estaba disponible: se usa app nativa Chrome. Perfil Andre para TestLink/Jira; Todo.ly solo perfil dedicado QA, sin usar sesiones personales. El usuario dejó las ventanas en un solo escritorio. Después de compacción, rewriteDocumentation.

**Las coordenadas App.click usan píxeles completos de la captura**, no puntos lógicos: captura 2400×1636. El clic [199,362] enfocó navbar; [398,724] enfocó el campo Title y expuso el iframe de navegación. No dividir las coordenadas Retina por dos. Basarse siempre en captura fresca.

AX a veces omite iframes que sí aparecen en captura; enfocarlos mediante clic por coordenadas puede exponerlos. No concluir error del sitio por un árbol vacío. El menú Profiles → Andre volvió a mostrar el contenido, pero no siempre fue suficiente. App.getScreenshot puede reflejar una imagen anterior: inspeccionar cada evidencia antes de publicarla. No repetir POST/Upload a ciegas. AX fresco tras acciones y completo tras captura antes de reutilizar índices.

Navegar por barra usando click + setValue + Return resultó más fiable que super+l/typeText. Diálogo de archivos: Choose File → super+shift+g → setValue ruta absoluta → Return → Open; después verificar nombre antes de Upload. La selección funcionó sin ayuda. Direct link del caso: imagen Show / Hide direct link, leer URL real.

Ruta del importador contrastada con código oficial: /lib/testcases/tcImport.php?containerID=3&useRecursion=0. Es un formulario UI de sesión autenticada, no un cambio por API. Comprobar destino Todo.ly tests y omitir duplicados. Una sesión vieja puede redirigir a login.php?note=expired; credenciales TestLink disponibles en privado.

## Jira: publicación y formato

Se consultó getContentFormatGuide para addOrEditJiraIssueComment. HTML con tablas, celdas data-colwidth y data-layout wide para lectura con desplazamiento horizontal. El script preparar_comentario_jira.py convierte el formato acotado local; validar longitud menor a 32767.

Adjuntos: discover uploadAttachmentToJiraIssue, fase1 devuelve uploadCommand; ejecutar receta sin registrar tokens; tomar media data.id + collection. Para embeber en HTML, no ejecutar fase2. Los comandos curl pueden agregar progreso después del JSON: parsear el primer objeto balanceado. No reintentar si ya se conserva el ID. Tres medios T10 reales están en comentario10226; metadata en archivos locales. Actualizar copia publicada desde Jira antes de auditoría.

Editar comentario existente exige lectura HTML previa y conservar todos los nodos. Solo se ajustaron anchos de tablas y se añadió captura del árbol filtrado; imágenes anteriores conservadas. La lectura posterior comprobó seis tablas, 219 celdas dimensionadas, tres imágenes y seis enlaces; captura visual posterior muestra tablas legibles con scroll.

## Datos reales para limpieza final

| Cuenta | Ubicación | Dato temporal real |
|---|---|---|
| A | Home | Prueba T09-aislamiento-A-1937 |
| B | Home | Prueba T09-aislamiento-B-1941 |
| A | Raíz | Prueba T11 - proyecto renombrado 1109, vacío |

No confundir nombres de fichas con datos reales. Conservar Work (cinco tutoriales), Sub Project predeterminado, Home, Study, Personal y Shopping List. Baseline Settings: La Paz UTC-04, inicio Work, domingo, Small, vencimiento None, Project Tag marcado, contextMenuRightClick desmarcado, AutoEditNotesOnClick marcado; cotejar estado-cuentas-inicial.md. Limpieza al final, vaciar papeleras con confirmación de herramienta cuando corresponda, no borrar cuentas.

## Cierre pendiente

Limpiar y documentar estado final con capturas; restauración A/email B y registro privado. Exportar suite real y extraer XML preservando IDs. Copiar comentarios reales (74 ya copiado), auditoría final independiente Claude, checklist §19 y por criterios, INFORME-FINAL, commit + push. El usuario pide al terminar un checklist claro de avanzado y faltante. No declarar fase 6 completa si queda restauración/limpieza sin comprobar.

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

## Punto seguro — prioridad por aclarar antes de T09

Después de cerrar T10 y enviar 89ec619 se encontraron dos archivos nuevos del usuario, no incluidos en ese commit: `PROMPT_REVISION_TESTLINK.md` y `docs/ejemplo-caso-de-prueba.pdf`. El prompt propone una tarea nueva prioritaria: revisión de todos los casos, excepción de alcance a AGENTS, ninguna escritura en Jira y punto de control antes de aplicar propuestas. **No se ha tratado el archivo no invocado como autorización automática para editar casos ajenos.** Se preguntó al usuario si prioriza terminar T09–T11 o revisar primero todos los casos. Falta respuesta; no repetir la pregunta ni nuevas solicitudes de claves. Mientras se aclara, solo lecturas y respaldos de trabajo propio; no se importó T09 ni se modificaron otros casos.

El nuevo ejemplo se leyó visualmente completo: una sola página, Successful Product Purchase. La extracción de texto está vacía porque es una imagen; render en tmp/pdfs/ejemplo-docente/pagina-1.png. Se observan descripción iniciada con Validar que, precondición como dato/estado, acciones separadas con controles concretos, respuesta por paso y postcondiciones. No atribuirle nuevas reglas de Todo.ly. No se releyeron los PDF previos. Se aplicó la habilidad PDF para esta lectura.

El archivo .secrets/testlink-api.local.md mencionado por el prompt **no existe**. Si el usuario activa la revisión global, usar navegador según su fallback, sin pedir otra vez el acceso de TestLink ya guardado. Antes de toda modificación: respaldo completo, propuestas y OK del punto de control. Cualquier respaldo/propuesta con credenciales preexistentes debe quedar privado o redactado para evitar subir secretos a git. El archivo de ejemplo del docente y el nuevo prompt permanecen intactos y sin incluir en nuestros commits hasta aclarar la tarea.

La visualización de PEB-74 ya se comprobó en Chrome: tablas legibles con desplazamiento horizontal después del ajuste de 219 celdas. TestLink sigue en la primera pestaña, filtro T10- (seis casos); Jira PEB-74 está en la segunda pestaña. La copia real publicada contiene seis tablas, tres imágenes y los seis enlaces. Este punto seguro no es cierre de T09/T11 ni fase 6.

## Coordinación actual — 18/11

El otro Claude es el único autor de revision-testlink/ y revisa por API casos existentes de otros tickets. Codex registra T09/T11 y publica en Jira. No editar archivos de revision-testlink; incluir sus archivos nuevos en commits solo tras comprobar que no contienen secretos. No interpretar sus instrucciones de no Jira como reglas para Codex.

Rúbrica T09/T11: título funcionalidad+condición+resultado (aprox. 90 caracteres), descripción iniciada con Validar que, precondiciones únicamente estados/datos sin infinitivos ni formas conjugadas, una acción por paso con controles/datos exactos en negrita y resultados observables. Se conservan IDs, objetivo, importancia, alcance y dudas. Cuenta/correo/contraseña siguen genéricos mediante registro privado, por decisiones §7.

El bloque manual T10 fue solicitado en una sola lista: a incorrecta Prueba-T10-04-incorrecta + New original, detener si acepta; b vigente → original y actualizar secreto tras aceptación; c B cambia Email al alias indicado y Cancel, nunca Ok, reabrir y capturar. Mientras el usuario introduce credenciales no operar el navegador; avanzar con archivos. Tras confirmación: verificar Login A original y Email B original, completar/revisar 04/05/06, importar SOLO esos tres sin repetir los seis existentes y añadir IDs/enlaces al comentario 10226 preservando su HTML/media.

**Navegador cedido por instrucción expresa del usuario:** no usar ninguna pestaña, ventana ni CUA hasta que avise que terminó T10. Trabajo local permitido. T09 diseño05 integrado, 171 pasos; revisión06 Claude en curso. El respaldo/propuestas y dos scripts de revision-testlink contienen una credencial preexistente: intactos y excluidos de Git, pendiente resguardo cifrado para respaldarlos sin exponer valores.
