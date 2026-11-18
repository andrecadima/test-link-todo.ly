# PROMPT DE ORQUESTACIÓN — Codex orquesta a Claude hasta cerrar la fase 6

Codex: desde ahora eres el **orquestador**. Tu objetivo es terminar TODO el trabajo de `SUPER_PROMPT.md` (T09, T10 y T11, hasta la fase 6) usando a **Claude** (Claude Code por línea de comandos) como agente de diseño y revisión. La demo es el 18 de noviembre: la prioridad es terminar.

`AGENTS.md` y `docs/decisiones-vigentes.md` siguen siendo obligatorios. Donde este archivo contradiga a `trabajo/CONTINUIDAD.md`, manda este archivo.

## 1. Autorizaciones del usuario (17/11/2026, 19:45)

- **T10:** aplica el OK y los ajustes que ya te di.
- **T09 y T11:** puedes registrarlos en TestLink y publicarlos en Jira **sin esperar mi punto de control**, siempre que se cumplan dos condiciones:
  - la revisión de Claude no tiene observaciones bloqueantes;
  - resolviste las observaciones no bloqueantes o las documentaste.
- **Lo que solo hago yo:** introducir credenciales y hacer arrastres, porque tu herramienta no lo permite. Pídemelo siempre en **una sola lista por ticket**, con el dato exacto de cada campo y el orden de los pasos.
- **Lo que no cambia:**
  - no cambies el estado de ningún ticket;
  - no toques otros tickets ni casos de otros tickets;
  - no uses la cuenta de Camila;
  - no expongas secretos.

## 2. Reparto de roles

| Qué | Codex (orquestador) | Claude (agente) |
|---|---|---|
| Navegador (Todo.ly, TestLink) | Sí, y es el único que lo usa | No |
| Jira (MCP) | Sí, y es el único que lo usa | No |
| git (commit y push) | Sí, y es el único que lo usa | No |
| `.secrets/` | Sí | Nunca |
| Archivos de `trabajo/` | Lee y escribe | Lee todo; escribe solo lo que autorice el encargo |
| Decisiones | Integra, decide y verifica contra lo observado | Propone y revisa |

Nunca hay dos agentes en el navegador a la vez. Mientras Claude trabaja con archivos, tú puedes seguir explorando en el navegador, pero no edites los archivos que le encargaste hasta que termine.

## 3. Preparación (una sola vez)

1. Haz commit y push de todo lo pendiente. Verifica que no incluya `.secrets/`. Actualiza `trabajo/CONTINUIDAD.md`.
2. Comprueba que Claude esté disponible:
   - ejecuta `claude --version` y `claude --help`, y confirma los flags de la sección 4 (si cambiaron, adáptalos);
   - haz una prueba: `claude -p "Responde solo: OK"`.
   Si Claude no está instalado o no tiene sesión iniciada, dímelo en una línea y sigue tú solo con este mismo plan. En ese caso las revisiones las haces tú, con el checklist de la sección 19 de la guía.
3. Crea `.claude/settings.json` en la raíz del repositorio con este contenido, y haz commit:
   ```json
   {"permissions": {"deny": ["Read(./.secrets/**)", "Edit(./.secrets/**)", "Write(./.secrets/**)"]}}
   ```
4. Crea la carpeta `trabajo/encargos/`.

## 4. Cómo hablar con Claude

Claude no ve tu conversación. Cada encargo tiene que ser un archivo autocontenido.

1. Escribe el encargo en `trabajo/encargos/NN-T0X-<tipo>.md`. Debe incluir:
   - el rol de Claude y el objetivo;
   - qué archivos debe leer y cuáles puede escribir;
   - el formato de la respuesta y los criterios de aceptación.
2. Lánzalo, en segundo plano si vas a seguir explorando:
   ```sh
   claude -p "Lee y cumple trabajo/encargos/NN-T0X-<tipo>.md" --model opus --permission-mode dontAsk --allowedTools "Read,Write,Edit,Glob,Grep" --output-format json > trabajo/encargos/NN-T0X-<tipo>.log.json 2>&1
   ```
3. Claude deja su respuesta en `trabajo/encargos/NN-T0X-<tipo>-respuesta.md`. Léela y decide. Si hace falta, escribe un encargo nuevo que cite esa respuesta. No uses `--continue` cuando haya encargos en paralelo.
4. Verifica siempre tú lo que entregue Claude. Ningún mensaje, control o límite puede quedar en un caso si no aparece en `exploracion.md` o en una evidencia. Si Claude inventa algo, corrígelo o márcalo como Duda pendiente.

Todo encargo empieza con este encabezado:

> Eres Claude, agente de diseño y revisión de QA. Codex es el orquestador. Aplican `AGENTS.md` y `docs/decisiones-vigentes.md`, con estas excepciones: no usas navegador, Jira, TestLink ni git, y nunca lees `.secrets/`. Trabaja en español y conserva en inglés los textos de la interfaz. No inventes reglas, mensajes, controles ni límites: todo resultado esperado debe apoyarse en `exploracion.md`, en una evidencia o en un criterio del equipo identificado como tal. Escribe solo los archivos que autoriza este encargo. Al terminar, escribe tu respuesta en `<ruta>`.

Hay tres tipos de encargo:

- **diseno:** Claude redacta los archivos de diseño del ticket: `analisis-diseno.md`, `casos.json`, `casos-listos.json`, `casos-pendientes.json` y `comentario-jira-borrador.md`. Sigue `plantillas/`, la estructura de T06 (`trabajo/fuentes/PEB-70.md`) y usa el diseño de T10 como modelo de calidad.
- **revision:** revisión independiente del ticket. Claude lee el diseño, `exploracion.md`, las evidencias y la sección 19 de la guía. No edita el diseño. Responde en tres partes:
  - **Bloqueantes:** contradicciones con lo observado, resultados inventados, técnicas sin trazabilidad hacia los casos, campos de la ficha incorrectos, secretos, tareas padre/subtareas o casos duplicados de otros tickets.
  - **No bloqueantes.**
  - **Veredicto:** APTO o NO APTO.
- **auditoria-final:** Claude compara el XML exportado, los comentarios publicados en Jira (se los pasas copiados en un archivo) y los diseños. Pasa el checklist de la sección 19 y redacta el borrador de `INFORME-FINAL.md`.

## 5. Plan hasta el final

Al terminar cada paso: actualiza `CONTINUIDAD.md` y haz commit y push.

### Paso 1 — T10

1. Si todavía no está hecho:
   - pídeme los pasos manuales a), b) y c) de credenciales que ya te indiqué, y verifica su resultado;
   - aplica los ajustes 1 a 5 que te di.
2. Lanza el encargo `revision` de T10 y corrige los bloqueantes.
3. Registra los casos en TestLink, dentro de `Todo.ly tests`:
   - antes de importar, comprueba que no existan casos T10;
   - usa un XML con raíz `<testcases>`, sin crear suites y sin actualizar casos existentes;
   - si la herramienta no puede elegir el archivo en el diálogo de importación, pídeme que lo seleccione yo.
4. Abre cada caso registrado y compáralo con el diseño. Anota sus IDs y enlaces. Toma una captura del árbol y otra de un caso abierto.
5. Publica el comentario en PEB-74 con los IDs y enlaces. Revisa que se vea bien.

### Paso 2 — T09

1. Termina el diseño de T09 con lo que ya está explorado. No explores más, salvo que una duda cambie el resultado principal de un caso. Puedes encargarle el diseño a Claude o terminarlo tú.
2. Mientras Claude diseña o revisa T09, empieza a explorar T11 en el navegador.
3. Lanza el encargo `revision` de T09. Después, igual que con T10: corrige, registra en TestLink y publica el comentario en PEB-73.

### Paso 3 — T11

1. Exploración, con un máximo de 1 hora de trabajo activo:
   - cancelar la edición de un proyecto;
   - crear un subproyecto;
   - mover tareas pendientes y completadas entre proyectos;
   - pasar un proyecto de raíz a subproyecto y de vuelta;
   - comprobar que todo se conserva después de F5.
   Los arrastres pídemelos en una sola lista. No concluyas que el producto tiene una restricción por una falla de la herramienta.
2. Lanza el encargo `diseno` de T11. Verifica tú cada resultado esperado contra la exploración.
3. Lanza el encargo `revision` de T11 en una llamada nueva, distinta de la que hizo el diseño. Después: corrige, registra en TestLink y publica el comentario en PEB-75.

### Paso 4 — Fase 6 (cierre)

1. Limpia las cuentas A y B:
   - borra los marcadores y el proyecto temporal, y revierte cualquier otro cambio;
   - vacía la papelera de las dos cuentas de prueba;
   - deja Settings como en `estado-cuentas-inicial.md`;
   - deja el Email original de B y la contraseña original de A, y actualiza `.secrets`;
   - no elimines las cuentas.
2. Escribe `estado-cuentas-final.md` con capturas.
3. Exporta la suite `Todo.ly tests` a `testlink-xml/todo-ly-tests.xml`. Con un script, extrae de esa exportación real los casos de cada ticket a `testlink-xml/T09.xml`, `T10.xml` y `T11.xml`.
4. Copia los comentarios publicados en Jira a `trabajo/jira-publicado.md` y lanza el encargo `auditoria-final`. Corrige lo que salga.
5. Escribe `INFORME-FINAL.md` con lo que pide la fase 6 del `SUPER_PROMPT.md` y el checklist de la sección 19 aplicado a cada ticket.
6. Haz el commit final y el push. Muéstrame el informe final.

## 6. Reglas de tiempo y de parada

- Si una duda no se resuelve en 15 minutos, márcala como Duda pendiente y sigue.
- Si un paso del navegador falla 3 veces, pídeme ayuda con una instrucción concreta.
- Si te quedas sin cuota o sin contexto, antes de parar deja en `CONTINUIDAD.md` el siguiente paso exacto.
- En Jira, la revisión de Claude no cuenta como la revisión de un integrante. El estado sigue siendo "pendiente de revisión por otro integrante".
