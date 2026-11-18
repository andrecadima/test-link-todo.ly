# PROMPT — Revisión y reescritura de los casos de prueba de Todo.ly en TestLink

## Rol y objetivo

Eres Claude y actúas como analista QA senior. Trabajas solo a través de la API de TestLink y de los archivos del repositorio. En paralelo, Codex usa el navegador, Jira y git, y está registrando los casos de T09 y T11. Tu tarea es revisar **todos** los casos de prueba del proyecto **TL:Todo.ly** en TestLink (http://68.211.149.112) y reescribir los que sean ambiguos. Al terminar, cualquier desarrollador debe poder leer el título de un caso, entender qué se prueba y replicarlo paso a paso sin tener que preguntar nada.

Es una práctica evaluada de Gestión de Calidad (UCB, SIS-312). Los casos los escribieron varios integrantes del equipo. **Cambias cómo está escrito cada caso, nunca qué prueba.**

**Autorización del usuario (excepción a la regla 1 de `AGENTS.md`):** en esta tarea puedes editar casos de todos los tickets, no solo los de T09, T10 y T11. El resto de `AGENTS.md` sigue vigente.

## Fuentes

1. `docs/ejemplo-caso-de-prueba.pdf`: el modelo del docente ("Successful Product Purchase", SauceDemo). Es la referencia de estilo. Léelo primero.
2. `docs/guia-diseno-casos-prueba-todoly.md`: textos reales de la interfaz de Todo.ly (secciones 11 a 15) y reglas de cada ticket.
3. `trabajo/00-contexto.md` y `trabajo/T09|T10|T11/exploracion.md`: mensajes y controles observados en la exploración.

## Rúbrica: qué hace bueno a un caso

### Título
- Dice qué funcionalidad se prueba, en qué condición y qué resultado se espera. Ejemplo: `T07-02 - Reactivar una tarea completada la devuelve a pendientes`.
- Conserva el prefijo de ticket y el número que ya tenga el caso.
- No sirven:
  - títulos genéricos ("Prueba de login", "Caso 3");
  - el nombre del módulo solo;
  - verbos vacíos ("Probar…", "Verificar que funciona…").
- Máximo unos 90 caracteres.

### Descripción (Summary)
- Una sola oración que empieza con **"Validar que…"**, como en el ejemplo del docente.
- El requerimiento `PEB-XX / TXX`. Si el caso ya lo tiene, se conserva.
- Al final, las **postcondiciones**, bajo el encabezado "Postcondiciones:", porque TestLink no tiene un campo propio para ellas. Si el equipo ya usa otra convención consistente, respétala.

### Precondiciones: sin verbos
- Describen solo estados y datos. No llevan verbos de acción: ni infinitivos (Tener, Ingresar, Abrir, Crear, Iniciar) ni formas conjugadas (el usuario tiene, se debe). Sí se permiten participios usados como adjetivos: "sesión iniciada", "proyecto creado".
- ❌ "Tener credenciales user:admin, password:12345 para acceder a la página web todo.ly".
- ✅ "Cuenta de Todo.ly registrada: usuario admin / contraseña 12345." · "Sesión iniciada en Todo.ly." · "Proyecto **Home** sin tareas pendientes ni completadas."
- Una precondición por línea, numerada y con los datos concretos: cuenta, proyecto, nombres de las tareas.
- Si una precondición es en realidad una acción (crear una tarea, marcarla como completada), pásala a los pasos.

### Pasos (Steps nativos de TestLink)
- Una acción por paso, en imperativo y con el control exacto en negrita: "Hacer clic en **Add**", "Escribir **Prueba T07-02 - tarea** en el campo **Add new Todo**".
- El paso incluye los datos exactos: textos y nombres.
- Cada paso tiene su resultado esperado observable, con el texto literal de la interfaz cuando existe. Por ejemplo: "Aparece el mensaje **Info. Item has been moved to project: Home**".
- No sirven: "funciona correctamente", "se comporta como se espera", "verificar que todo esté bien".
- Si un caso tiene los pasos escritos dentro del Summary y los Steps nativos vacíos, pásalos a Steps nativos (un paso por fila, con su resultado esperado). En el Summary deja solo la descripción, el requerimiento y las postcondiciones.

### Postcondiciones
- Describen el estado final del sistema y de los datos: dónde quedan las tareas y qué muestra la pantalla.

## Límites obligatorios

- No cambies el objetivo, la cobertura, la importancia, el tipo de ejecución ni el ID de ningún caso. No borres casos, no crees casos nuevos y no muevas casos entre suites.
- **No inventes** textos de interfaz, mensajes, controles ni límites. Si un texto no aparece en el caso original ni en las fuentes, deja la redacción original de esa parte y anótala como duda en el informe.
- **Credenciales:** si un caso ya trae credenciales, consérvalas, reformuladas sin verbos. No agregues contraseñas que el caso no tenga.
- **T09, T10 y T11:** inclúyelos en el análisis, pero no los edites hasta que el usuario confirme que Codex terminó de registrarlos.
- No escribas en Jira.
- **No ejecutes git:** los commits los hace Codex. Deja todo tu trabajo dentro de `revision-testlink/`.
- No leas `.secrets/`.

## Cómo acceder a TestLink: API XML-RPC

- Endpoint: `http://68.211.149.112/lib/api/xmlrpc/v1/xmlrpc.php`
- La clave de la API está en la variable de entorno `TESTLINK_DEVKEY`. Tus scripts la leen de ahí. Nunca la imprimas ni la guardes en archivos.
- Antes de nada, comprueba que la API funcione:
  - `tl.sayHello` y `tl.about`;
  - `system.listMethods`, para confirmar que existen `tl.updateTestCase` y `tl.getTestCase`;
  - `tl.checkDevKey`.
- Escribe los scripts en Python, con `xmlrpc.client`, dentro de `revision-testlink/scripts/`.
- Si la API no está habilitada, la clave no funciona o falta `tl.updateTestCase`, detente y avísame. No tienes navegador.

## Fases

### Fase 1 — Respaldo e inventario (solo lectura)

1. Descarga todos los casos del proyecto TL:Todo.ly a `revision-testlink/respaldo-AAAAMMDD-HHMM.json`: todas las suites, la última versión de cada caso, con sus pasos. Ese respaldo es lo que permite revertir.
2. Escribe `revision-testlink/scripts/revertir.py`, que restaure cualquier caso desde el respaldo. Pruébalo en modo simulación, sin escribir nada.
3. Evalúa cada caso contra la rúbrica y clasifícalo como OK, EDITAR o DUDA, con los problemas concretos que tenga.

### Fase 2 — Propuestas

1. Para cada caso EDITAR, escribe la versión nueva completa en `revision-testlink/propuestas.json`: ID externo, versión, nombre, summary, preconditions y steps.
2. Genera `revision-testlink/informe-revision.md` con:
   - un resumen: total de casos y cuántos son OK, EDITAR y DUDA, por ticket;
   - una tabla: ID | Ticket | Título antes | Título después | Problemas | Cambios;
   - tres ejemplos completos de antes y después: uno con precondiciones con verbos, uno con un título ambiguo y uno con los pasos dentro del Summary;
   - las dudas: lo que no pudiste aclarar sin inventar.
3. **Punto de control:** muéstrame el resumen y los tres ejemplos, y espera mi OK.

### Fase 3 — Aplicar

1. **Piloto:** aplica la propuesta a un solo caso. Vuelve a leerlo por la API y compáralo campo por campo con la propuesta: nombre, summary, preconditions y cada paso con su resultado esperado.
   - Si coincide, sigue sin esperar mi respuesta.
   - Si no coincide, corrige el script y repite el piloto.
2. Aplica el resto de los casos en lote. Registra cada uno en `revision-testlink/aplicado.log` con su ID y el resultado (OK o error), sin datos sensibles.
3. Si un caso no se puede editar (por ejemplo, porque su versión ya tiene ejecuciones), no lo fuerces: anótalo en el informe.
4. Vuelve a leer todos los casos editados y confirma que coinciden con las propuestas.

### Fase 4 — Cierre

- Actualiza `informe-revision.md` con el resultado final (casos aplicados, fallidos y pendientes) y con las instrucciones para revertir usando el respaldo.
- Resúmeme en cinco líneas qué cambió.
