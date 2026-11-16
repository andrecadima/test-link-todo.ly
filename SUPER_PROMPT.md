# SUPER PROMPT — Codex · T09, T10 y T11 de Todo.ly

## Datos para completar antes de pegar

Si los dejas vacíos, Codex te los pedirá al empezar.

- Correo para la cuenta de prueba A:
- Correo para la cuenta de prueba B:

Sugerencia: usa dos alias de tu Gmail, por ejemplo `tucorreo+todoly-a@gmail.com` y `tucorreo+todoly-b@gmail.com`. Los correos de verificación y de recuperación llegarán a tu bandeja normal.

---

Hola Codex. Este trabajo es crítico para mi evaluación de Gestión de Calidad. Antes de hacer nada, lee completos `AGENTS.md` y `docs/decisiones-vigentes.md`. Sus reglas son obligatorias durante todo el trabajo.

## Objetivo

En los tickets T09, T10 y T11 del proyecto PEB de Jira, y solo en ellos:

1. Analiza el área de riesgo de Todo.ly (https://todo.ly) que cubre cada ticket.
2. Diseña los casos de prueba con las técnicas de caja negra vistas en clase, justificadas por el riesgo y por reglas confirmadas.
3. Registra los casos en TestLink (http://68.211.149.112; la sesión ya está iniciada en Chrome).
4. Documenta todo en cada ticket de Jira: las técnicas con la calidad de T06 (PEB-70) y la evidencia de TestLink como en T12 (PEB-76).

Toda la exploración de Todo.ly se hace con dos cuentas de prueba nuevas que vas a crear tú: A y B. No uses la cuenta de Camila ni ninguna cuenta del equipo.

## Fase 0 — Contexto (todavía sin tocar Todo.ly)

1. Lee `docs/guia-diseno-casos-prueba-todoly.md`, `docs/PlanPruebasTodo.ly.pdf` y todo `docs/material-clase/`. Si falta algún PDF de clase, avísame y no supongas su contenido.
2. En Jira, lee completos (descripción, criterios de aceptación y comentarios) estos tickets:
   - T09, T10 y T11. Confirma sus claves (probablemente PEB-73, PEB-74 y PEB-75) y su alcance real.
   - T06 (PEB-70): cómo se estructura el comentario y cómo se aplican y justifican las técnicas.
   - T12 (PEB-76): cómo se dejó la evidencia del registro en TestLink.
   - PEB-65, PEB-66, PEB-67 y PEB-69.
   - El resto de los tickets de diseño (T07, T08, T13 y T14), para no duplicar casos.
3. En TestLink, abre los casos de T06 y T12 y anota cómo están organizados: proyecto, suites, nomenclatura, uso de Summary, Preconditions, Steps/Expected results e Importance, y dónde van el requerimiento y las postcondiciones.
4. Escribe `trabajo/00-contexto.md` con:
   - las claves, el alcance real y los criterios de aceptación de T09, T10 y T11;
   - la estructura de T06 y de T12 que vas a replicar;
   - el mapeo de campos de TestLink (completa la tabla de `plantillas/caso-testlink.md`);
   - la definición exacta de cada técnica según las diapositivas del docente: valores límite de 2 y 3 valores, formato de la tabla de decisión, transición de estados, etc.;
   - los casos de otros tickets que se solapan con T09, T10 y T11.
5. Si el alcance real de un ticket no coincide con `docs/decisiones-vigentes.md`, avísame antes de seguir.
6. Commit: `Fase 0: contexto`.

## Fase 1 — Cuentas de prueba

1. Abre Todo.ly en un perfil de Chrome dedicado. No uses ni cierres ninguna sesión de Todo.ly que ya esté abierta, y no borres cookies globales.
2. Antes de registrarte, explora el formulario de registro, que es parte de T09: campos, validaciones, mensajes con datos vacíos o mal formados, y qué pasa con un email ya registrado. Anótalo en `trabajo/T09/exploracion.md` usando `plantillas/registro-exploracion.md`.
3. Crea la cuenta A y la cuenta B con los correos indicados y contraseñas fuertes que generes tú.
   - Guárdalas en `.secrets/cuentas-prueba.local.md`. Ese archivo está ignorado por git.
   - Actualiza el archivo cada vez que cambies una credencial.
4. Si aparece un captcha o hay que abrir un correo de verificación, pídeme ayuda. No entres a mi correo.
5. Apenas crees cada cuenta, registra su estado por defecto en `trabajo/estado-cuentas-inicial.md` con `plantillas/estado-cuenta.md`: proyectos predeterminados, Settings, papelera y Sort By. Es la referencia para dejar las cuentas limpias al final.
6. Commit: `Fase 1: cuentas de prueba y estado inicial`. Verifica que no incluya `.secrets/`.

## Fase 2 — Exploración focalizada por ticket

Explora lo necesario para confirmar las reglas de las que dependen los resultados esperados.

- Registra cada observación en `trabajo/T0X/exploracion.md`, con las condiciones, la cuenta usada y una captura en `trabajo/T0X/evidencias/`.
- Lo observado no prueba que el comportamiento sea correcto. Clasifica cada regla como Regla documentada, Comportamiento observado, Criterio del equipo o Duda pendiente.
- Busca fronteras reales antes de aplicar valores límite.

### T09 — Registro, sesión y separación de cuentas
- Login con combinaciones de email y contraseña: válidos, inválidos, vacíos y cuenta inexistente.
- Cierre de sesión.
- Acceso a páginas internas después del logout, con el botón atrás del navegador y con la URL directa.
- Remember Me marcado y sin marcar: cierra todas las ventanas del perfil dedicado y vuelve a abrirlo.
- Separación de datos: lo creado en A no debe verse en B, y viceversa.
- Si los intentos fallidos provocan un bloqueo o un captcha, documéntalo y sigue con la otra cuenta.

### T10 — Perfil, credenciales y recuperación
- Campos de Settings y perfil: guardar, cancelar y persistencia con F5 y con una nueva sesión.
- Validaciones del cambio de contraseña y del cambio de email.
- Cambio válido de contraseña en la cuenta A y vuelta a la contraseña anterior.
- Si cambias el email, usa otro alias del mismo buzón y después vuelve al original.
- Recuperación de contraseña:
  - con la cuenta A (pídeme que revise el correo y te diga qué llegó);
  - con un correo no registrado del dominio `example.com`.
- No toques la zona horaria ni la fecha predeterminada: son del ticket de vencimientos.
- No pruebes la eliminación de la cuenta: está fuera de alcance.

### T11 — Proyectos, subproyectos y movimientos
- Crear, renombrar y seleccionar proyectos.
- Crear subproyectos.
- Mover proyectos, si la interfaz lo permite: reordenar, convertir en subproyecto y volver a la raíz.
- Mover tareas pendientes y completadas entre proyectos.
- Conservación del contenido, los atributos y las relaciones después de mover y después de F5.
- Independencia entre proyectos: Home como proyecto principal y Study como contraste.
- Profundidad máxima de anidación, solo si la encuentras de verdad.
- No incluyas tareas padre/subtareas.
- No dupliques la eliminación de subproyectos, que ya está en T08.

Revierte cada cambio de configuración en cuanto termines de observarlo. Haz un commit al cerrar cada ticket: `T0X: exploración`.

## Fase 3 — Análisis y diseño

Para cada ticket, escribe `trabajo/T0X/analisis-diseno.md`. Usa la estructura de `plantillas/comentario-jira.md`, ajustada a la estructura real de T06, y escribe los casos con `plantillas/caso-testlink.md`. El documento debe incluir:

- **Riesgos** concretos, con probabilidad e impacto. Prioriza los altos.
- **Tipos de prueba** elegidos por pertinencia, cada uno con objetivo, procedimiento y criterio observable:
  - funcional;
  - y solo si se justifica: seguridad observable de sesión o entradas, usabilidad, accesibilidad de controles o compatibilidad con Firefox.
- **Escenarios** positivos, negativos y alternativos, cuando aporten cobertura distinta.
- **Técnicas** aplicadas de verdad, cada una con su artefacto (tabla de particiones, valores límite, tabla de decisión, tabla de transiciones o flujos de caso de uso) y con la trazabilidad a los casos que genera. Úsalas solo si las reglas las justifican. Candidatos naturales:
  - tabla de decisión para el login;
  - transición de estados para la sesión y Remember Me;
  - particiones y valores límite para los campos de registro y de perfil, si hay fronteras confirmadas;
  - casos de uso para la recuperación y para los movimientos;
  - transición de estados para proyecto raíz ↔ subproyecto.
- **Lista resumida:** | Caso | Objetivo o riesgo cubierto | Fundamento de la técnica aplicada |
- **Fichas** con exactamente los campos acordados. Precondiciones genéricas, según la sección 7 de las decisiones vigentes, sin correos ni contraseñas reales.

Si una duda impide fijar el resultado esperado principal de un caso, déjalo como pendiente y sigue con los demás.

Haz un commit por ticket: `T0X: análisis y diseño`.

## PUNTO DE CONTROL

Antes de escribir nada en TestLink o en Jira, muéstrame por cada ticket:
- el resumen del análisis;
- las técnicas aplicadas, con sus artefactos;
- la lista resumida de casos.

Espera mi OK. Aplica mis correcciones y haz commit de nuevo.

## Fase 4 — Registro en TestLink

1. Registra los casos con la organización real que anotaste en la fase 0: suite por ticket, misma nomenclatura, Importance, ejecución Manual y cada paso con su resultado esperado.
2. No edites, borres ni renumeres casos de otros tickets.
3. Abre cada caso registrado y compáralo con el diseño. Corrige las diferencias.
4. Guarda capturas en `trabajo/T0X/evidencias/`: el árbol de la suite del ticket y al menos un caso abierto.
5. Exporta a XML la suite de cada ticket y guárdala en `testlink-xml/T0X.xml`. El plan pide la exportación XML para la demo del 18 de noviembre.
6. Anota en `trabajo/T0X/analisis-diseno.md` los IDs y enlaces reales de cada caso.

Haz un commit por ticket: `T0X: registro en TestLink`.

## Fase 5 — Documentación en Jira

En T09, T10 y T11, publica un comentario con el contenido final de `trabajo/T0X/analisis-diseno.md`. Las fichas completas de los casos quedan en TestLink; en Jira va la lista resumida con los IDs y enlaces. El comentario tiene estas secciones:

1. Análisis del área.
2. Riesgos.
3. Reglas, restricciones y dudas, con su fundamento.
4. Tipos de prueba y escenarios, con su justificación.
5. Técnicas aplicadas, con sus artefactos.
6. Lista resumida de casos, con el fundamento de la técnica de cada uno.
7. Implementación: IDs y enlaces de TestLink, y las capturas como evidencia (como en T12).
8. Cobertura pendiente y dudas abiertas.
9. Estado: "Diseñados y registrados en TestLink; pendiente de revisión por otro integrante".

Además:
- Si no puedes adjuntar imágenes, dime las rutas de las capturas para que las pegue yo. Deja igual los IDs y los enlaces en el comentario.
- Revisa cómo se ve el comentario publicado y corrige tablas o formato rotos.
- Comprueba el checklist de criterios de aceptación de cada ticket.
- No cambies el estado de los tickets.

## Fase 6 — Cierre

1. Deja las cuentas A y B limpias:
   - solo los proyectos predeterminados;
   - ningún dato `Prueba ...`;
   - la papelera vacía;
   - los Settings iguales a `trabajo/estado-cuentas-inicial.md`;
   - el email original.
   No elimines las cuentas.
2. Registra el estado final en `trabajo/estado-cuentas-final.md`, con capturas.
3. Pasa el checklist de la sección 19 de la guía por cada ticket.
4. Escribe `trabajo/INFORME-FINAL.md` y muéstramelo. Debe incluir:
   - por ticket: la clave, el número de casos, los IDs y enlaces de TestLink, las técnicas usadas y el enlace al comentario de Jira;
   - las dudas pendientes y los casos que quedaron sin una regla confirmada;
   - el estado final de las cuentas de prueba;
   - lo que no pudiste hacer y por qué;
   - el resultado del checklist.
5. Commit final y push, si hay un remoto configurado: `Cierre T09–T11`.
