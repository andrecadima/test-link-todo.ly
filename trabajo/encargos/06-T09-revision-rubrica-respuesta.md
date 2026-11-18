# Respuesta — Encargo 06: revisión independiente de T09 con la rúbrica nueva

Revisor: Claude (agente de revisión). Fecha: 18/11/2026.

**Alcance.** Conjunto final registrable de T09 / PEB-73: 13 casos (T09-01 a T09-07 y T09-09 a T09-14) y 171 pasos, en `casos-listos.json`, las fichas de `analisis-diseno.md` y `importacion-propuesta.xml`. T09-08 (`casos-pendientes.json`) solo se trata como cobertura pendiente.

**Lo que esta revisión no es ni hizo:**

- No es la revisión de otro integrante y no la sustituye.
- No es una ejecución de casos.
- No se usó navegador, Jira, TestLink ni git.
- No se leyó `.secrets/` ni `revision-testlink/`.
- No se releyeron PDFs.
- No se editó el diseño. El único archivo escrito es este.

**Fuentes leídas:**

- `AGENTS.md` y `docs/decisiones-vigentes.md`, incluida la §15.
- La rúbrica de `PROMPT_REVISION_TESTLINK.md`, sin ejecutar su tarea.
- `plantillas/caso-testlink.md`, la guía §7–11 y §19, y `trabajo/00-contexto.md`.
- Los artefactos de T09: `exploracion.md`, `analisis-diseno.md`, los tres JSON, `comentario-jira-borrador.md` y el XML.
- `trabajo/T10/exploracion.md`.
- Las respuestas y resoluciones 03 y 05.
- `scripts/preparar_importacion_testlink.py`, solo leído para entender cómo se genera el XML.

**Evidencias inspeccionadas directamente:**

- `2026-11-16_T09_registro-vacio.png`:
  - título y botón visibles `Signup`;
  - asteriscos en Full Name, Email y Password;
  - `(UTC-08:00) Pacific Time (US & Cana…` recortado;
  - aviso `If you don’t agree you can’t use Todo.ly`.
- `2026-11-17_T09_login-ambos-vacios-controlado.png`:
  - formulario `Login` con Email, Password, `Remember Me` y el botón `Login`;
  - sin sesión y sin mensaje visible.

---

## 1. Bloqueantes

**Ninguno.**

Comprobaciones que fundamentan este resultado:

- **Conjunto e importación.**
  - El XML tiene raíz `<testcases>`. No contiene `<testsuite>`, `internalid` ni `externalid`.
  - Tiene 13 `testcase` con nombres `T09-NN. …` y `node_order` del 1 al 13.
  - T09-08 no aparece.
  - Hay 171 `<step_number>`, la misma suma que los pasos de las fichas (10+17+10+12+6+7+7+7+7+7+41+17+23).
  - Todos los `execution_type` valen 1 (Manual).
  - `importance` vale 2 en T09-01 y T09-03 (medium) y 3 en el resto (high). Coincide con el JSON.
  - No hay `**` literales: la negrita sale como `<strong>`.
  - En `casos-listos.json` no aparece `PENDIENTE`; solo figura en `casos-pendientes.json` y `casos.json`, para T09-08.
- **Correspondencia JSON ↔ XML.**
  - El XML lo genera de forma determinista el script a partir de `casos-listos.json`. El script rechaza `PENDIENTE`, los IDs ajenos o duplicados, las descripciones que no empiezan por «Validar que» y los pasos sin resultado.
  - En `casos.json`, los casos 01–07 ocupan las mismas líneas que en `casos-listos.json`, y del 09 al 14 hay un desfase constante de 39 líneas, que es exactamente el bloque de T09-08.
  - Contrasté textualmente T09-01 y varios pasos de T09-11 a T09-14.
  - No hice una comparación automática carácter por carácter.
- **Summary (§15).**
  - El orden es: descripción «Validar que…», «Requerimiento: PEB-73 / T09…» y «Postcondiciones: …».
  - La importancia no aparece en Summary: va en el campo nativo, y su razón queda en el JSON y en la ficha.
  - Esta decisión prevalece sobre el mapeo antiguo de `00-contexto.md` (razón al inicio de Summary).
- **Mensajes, todos con fuente.**
  - `Error. Account with this email address already exists!` (T09-02): `exploracion.md` l. 45 y su captura.
  - `Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.` (T09-06, 07, 09 y 10): la tabla del 17/11 y sus capturas.
  - `Error. Please correct the missing fields.` (T09-01): lectura AX, declarado como transitorio y no exigido en la captura.
  - `If you don’t agree you can’t use Todo.ly`: visible en la captura.
  - T09-05 no exige mensaje, lo que coincide con «mensaje no retenido».
- **Controles, todos con fuente.**
  - Sign Up Free, Signup, Login, Remember Me, Settings, Logout y Home: exploración y capturas.
  - Add new Todo y Add: guía §11.
  - Profile, Cancel y la distinción entre guardar y cancelar: T10 l. 9–10 y l. 35.
  - Profiles: observado en Chrome macOS. El paso dice «menú **Profiles** en macOS» y no asegura la etiqueta de Windows.
  - Atrás: nombrado como botón de Chrome, no de Todo.ly.
- **No se inventa nada en los puntos sensibles.**
  - **T09-01:** preparar cada campo vacío por separado no cambia la regla. La combinación sigue siendo conjunta y la descripción lo dice. El aviso global no se exige en la captura. La casilla se nombra «la casilla de términos», sin literal.
  - **T09-03:**
    - Pacific figura solo como «opción Pacific UTC-08», con el texto recortado de la captura.
    - El literal UTC-07 sale de decisiones §12.
    - 101 es el «inventario de referencia, sin tratarlo como límite del producto».
    - No hay BVA.
  - **T09-02:**
    - La conservación de A tras el duplicado está clasificada como **Criterio del equipo** (análisis §3 y `exploracion.md` l. 121).
    - El caso termina en Profile con A autenticada, sin Cancel ni Logout, y la postcondición lo dice.
    - La contraseña de Signup es «distinta de la vigente de A». No se la llama «válida» ni se presupone una política.
  - **T09-09:** la inexistencia del correo reservado se apoya en la recuperación de T10, a las 11:13 AM (`Error. Account with this Email address doesn't exist.`). No se infiere del error genérico de Login.
  - **Remember Me (T09-13/14):**
    - Hay una observación por estado: A desmarcado y B marcado.
    - La descripción y las postcondiciones excluyen la caducidad y el cierre completo de Chrome.
    - El intervalo se anota y no se convierte en regla.
  - **Tres intentos:** las precondiciones de T09-07 y T09-10 dicen «criterio operativo del equipo (no es una política de Todo.ly)».
- **Precondiciones.**
  - Son nominales, sin infinitivos ni formas conjugadas, y usan participios como adjetivos («consignados», «iniciada», «identificados»).
  - Las cuentas son genéricas (A, B y «registro privado»), sin correos ni contraseñas reales.
  - `Prueba-T09-no-valida-17` y la dirección `@example.com` son datos de prueba, no credenciales.
- **Alcance.**
  - No hay tareas padre ni subtareas.
  - Las tareas de T09-11 y T09-12 son marcadores de preparación, con el solapamiento con T06 declarado.
  - Timezone se limita al campo (§12).
  - No hay Pro, API ni eliminación de cuenta.

---

## 2. No bloqueantes

Leyenda:

- **[Documentar]**: basta con dejar constancia en la resolución o en el análisis.
- **[Mejora]**: opcional, no condiciona el registro.

### N1. [Documentar] Contexto del navegador en T09-13 y T09-14

- **Situación:** la observación se hizo con otros perfiles de Chrome abiertos, así que el proceso no terminó (`exploracion.md` l. 111).
- **Lo que dice el caso:**
  - El resultado del paso 13 afirma que «los demás perfiles de Chrome conservan sus ventanas y sesiones».
  - Ninguna precondición exige que exista otra ventana de otro perfil abierta.
- **Riesgo:** si quien ejecuta no tiene otro perfil abierto, cerrar las ventanas del perfil QA puede cerrar todo el proceso. Ese es el contexto distinto que el propio análisis (§5.3) pide registrar aparte.
- **Sugerencia:** añadir la precondición nominal «Otra ventana de Chrome de un perfil distinto abierta durante todo el recorrido», o anotar este matiz en la resolución.
- **Por qué no bloquea:** no cambia ninguna regla ni ningún resultado esperado del recorrido observado.

### N2. [Mejora] T09-01, paso 8: criterio de aprobación ante el aviso transitorio

- **Problema:** «Aparece el aviso transitorio…» puede leerse como obligatorio para quien ejecuta sin lectura de accesibilidad.
- **Sugerencia:** «Puede aparecer brevemente…; el criterio verificable son los asteriscos y el aviso de términos».
- **Situación actual:** el texto ya aclara que no se exige en la captura, así que solo es un matiz de claridad.

### N3. [Mejora] Resultados redundantes en las comparaciones de identidad

- **Dónde:** el resultado del último paso de comparación en T09-02 (paso 17), T09-04 (paso 10) y T09-12 (pasos 9 y 22).
- **Problema:** esos resultados vuelven a mencionar Full Name o «el nombre y el correo», ya comprobados en el paso anterior. Por ejemplo, en T09-02 el paso 17 compara Email, pero su resultado vuelve a hablar de Full Name.
- **Sugerencia:** limitar cada resultado al campo de su acción. En T09-02, la mención de «no **Prueba T09-02 - duplicado**» puede ir en el resultado del paso 16.

### N4. [Mejora] T09-11, paso 5: nombre del botón del navegador

**Atrás** corresponde a Chrome en español; en inglés es Back. Se puede escribir «**Atrás** (Back)» para quien ejecute en otro idioma. No es un control de Todo.ly, así que no se inventa ninguno.

### N5. [Documentar] Texto desactualizado sobre el orden de Summary

- **Dónde:** `analisis-diseno.md` §7 y `comentario-jira-borrador.md` §7.
- **Problema:** dicen «Summary con requerimiento/descripción/postcondiciones», pero el XML aplica, correctamente, descripción → requerimiento → postcondiciones (§15).
- **Sugerencia:** ajustar el orden en ambos textos antes de publicar, para que el comentario coincida con lo registrado.
- **Relacionado:** el mapeo de `00-contexto.md` («razón breve al inicio de Summary») queda superado por la §15. Conviene una nota si se cita.

### N6. [Mejora] Borrador de Jira con referencias operativas

- **Problema:** el borrador conserva:
  - «verificada directamente por Codex» (§3);
  - rutas como `trabajo/T10/exploracion.md` (§3 y §5.1);
  - `exploracion.md` (§1).
- **Sugerencia:** antes de publicar, usar tercera persona y nombres de evidencia sin rutas. Ya se señaló en la revisión 03 (N7).
- **Alcance:** no afecta a los casos registrables.

### N7. [Mejora] Redundancia en las precondiciones de T09-02, T09-04, T09-13 y T09-14

- **Problema:** «Cuenta… con correo… consignados en el registro privado» y «Nombres de perfil y correos de A consignados en el registro privado de referencia» repiten el correo.
- **Sugerencia:** limitar la segunda precondición a «Nombre de perfil de A consignado…».
- **Por qué es solo una mejora:** la redundancia no afecta la ejecución.

### N8. [Mejora, solo informativa] Literal de la casilla de términos

- La captura `registro-vacio.png` muestra junto a la casilla el texto `I have read and agree to the Terms of Service.`
- Ese literal **no está transcrito** en `exploracion.md`. Por eso el diseño hace bien en usar «la casilla de términos» y no debe cambiarse por ahora.
- Si Codex quiere usar el literal, primero debe anotarlo en la exploración como transcripción de esa captura. No es necesario para registrar.

### Cobertura pendiente (no es un defecto del conjunto registrable)

- **T09-08, Email mal formado:** las vistas vacías tienen una causa sin confirmar. Está bien excluido. No debe registrarse con un resultado condicional ni con el marcador `PENDIENTE`.
- **Signup:** faltan las validaciones aisladas por campo y un registro válido completo bajo control del equipo.
- **Fronteras y políticas:** no hay longitudes ni política de contraseñas confirmadas, y no se observaron bloqueo, CAPTCHA ni un límite de intentos del producto.
- **Remember Me:** falta la caducidad de la sesión recordada, el cierre completo del proceso Chrome y la repetición de cada estado con la misma cuenta.

Todo esto ya está declarado en `analisis-diseno.md` §8 y en el borrador, §8.

---

## 3. Checklist de la guía §19 y rúbrica

### Guía §19

| # | Ítem | Estado | Fundamento |
|---|---|---|---|
| 1 | Ticket correcto y alcance respetado | Cumple | PEB-73: Signup, Login, Remember Me, Logout y cambio de cuenta. Timezone solo como campo. |
| 2 | El análisis explica riesgos, reglas y dudas | Cumple | R1–R6 con P×I. §3 clasifica observado, criterio del equipo y duda. |
| 3 | Técnica aplicada y justificada por caso | Cumple | Particiones, tabla de decisión R1–R6 → 05/06/07/09/10/04, matriz S0–C2 → 04/11/13/14, UC1/UC2 → 01/02/03/12. BVA no aplicado y justificado. |
| 4 | Tipos de prueba elegidos por pertinencia | Cumple | Funcional y seguridad observable de sesión. Rendimiento y compatibilidad excluidos con motivo. |
| 5 | No se inventan límites, controles, mensajes ni funciones | Cumple | Ver §1. Matices en N4 y N8. |
| 6 | Sin jerarquías de tareas retiradas | Cumple | — |
| 7 | La ficha solo tiene los campos acordados | Cumple | Siete campos. Sin severidad ni técnica. |
| 8 | Importancia, no severidad | Cumple | Campo nativo 2/3; razón en la ficha. |
| 9 | Cada paso tiene un resultado verificable | Cumple | 171 de 171 con resultado. Matiz en N2. |
| 10 | Datos, controles y estado inicial reproducibles | Cumple con observación | Precondiciones genéricas y nombres únicos. Contexto del navegador en N1. |
| 11 | Limpieza y postcondiciones dicen dónde terminan los datos | Cumple | Marcadores de 11 y 12 en Home para la limpieza del lote; estado final de cada sesión declarado (T09-02 en Profile). |
| 12 | Se distingue diseñado / registrado / revisado / ejecutado / fallido | Cumple | Estado: «preparados para revisión», sin registro, publicación ni ejecución. |
| 13 | No se afirma cobertura o evidencia inexistente | Cumple | Las fuentes cruzadas están declaradas y el criterio del equipo está separado de lo observado. |

### Rúbrica de `PROMPT_REVISION_TESTLINK.md` y §15

| Criterio | Estado |
|---|---|
| Título: funcionalidad + condición + resultado, prefijo T09-NN, ≤ 90 caracteres | Cumple. El nombre más largo ronda los 81 caracteres. |
| Descripción: una oración que empieza por «Validar que…» | Cumple en los 13 casos. |
| Summary: descripción → requerimiento → postcondiciones | Cumple en el XML. N5 trata el texto desactualizado. |
| Precondiciones nominales, sin verbos, una por línea y con datos concretos | Cumple. N7 es solo una mejora de redundancia. |
| Una acción por paso, en imperativo, con controles y datos en negrita | Cumple. Las acciones condicionales de Remember Me son una sola acción. |
| Resultado observable con el literal cuando existe | Cumple. |
| `strong` en el XML, sin asteriscos literales | Cumple. |
| Importance en su campo nativo, Manual, sin IDs ni suites | Cumple. |
| Sin `PENDIENTE` en los listos; T09-08 fuera | Cumple. |
| Sin secretos ni correos reales; cuentas genéricas (§7) | Cumple. |
| Sin duplicar otros tickets ni tareas padre/subtareas | Cumple. |

---

## 4. Veredicto

**APTO para registrar los 13 casos** (T09-01 a T09-07 y T09-09 a T09-14, 171 pasos) tal como están en `casos-listos.json` e `importacion-propuesta.xml`.

- No hay bloqueantes.
- N1 y N5 deberían al menos documentarse (o ajustarse) antes de registrar y publicar. El resto son mejoras opcionales.
- T09-08 sigue como cobertura pendiente, fuera del registro. Su exclusión no es un defecto del conjunto.
- Este veredicto no equivale a la revisión de otro integrante ni a una ejecución. Después del registro, el estado debe seguir siendo «pendiente de revisión por otro integrante».
