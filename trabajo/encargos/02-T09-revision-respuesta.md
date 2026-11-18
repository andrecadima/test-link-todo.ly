# Respuesta — Revisión independiente de T09 / PEB-73

Revisor: Claude (agente). Fecha: 17/11/2026. Alcance: `trabajo/T09/casos-listos.json` (13 casos) y sus artefactos de soporte (`analisis-diseno.md`, `comentario-jira-borrador.md`, `importacion-propuesta.xml`). T09-08 (`casos-pendientes.json`) está excluido del registro y solo se comenta como cobertura pendiente.

Esta revisión **no** sustituye la revisión de otro integrante. No se registró nada en TestLink, no se publicó nada en Jira y no se ejecutó ningún caso. No se leyó `.secrets/`. Los ajustes 1–5 y la lista a/b/c de T10 no aparecen en las fuentes accesibles, así que no se evalúan ni se dan por aplicados.

Evidencias inspeccionadas: `registro-vacio`, `registro-sin-aceptar-terminos`, `email-B-ya-registrado`, `login-correo-vacio-password-informado`, `login-A-password-vacio`, `login-cuenta-inexistente`, `login-A-password-incorrecto`, `atras-tras-logout`, `A-conserva-marcador-y-no-ve-B`, `remember-off-reapertura-sin-sesion` y `remember-on-reapertura-autenticada`.

---

## 1. Bloqueantes

### B1. El botón de Signup se llama `Signup` en la interfaz, no `Submit`

- **Dónde:**
  - `casos-listos.json` → T09-01, paso 1 (resultado esperado) y paso 2 (acción).
  - T09-02, paso 2 (acción).
  - Las mismas filas en `analisis-diseno.md` (fichas T09-01 y T09-02) y en `importacion-propuesta.xml`.
  - `analisis-diseno.md` y `comentario-jira-borrador.md`, §1 («Signup muestra … términos y Submit»).
- **Evidencia de la contradicción:**
  - En `2026-11-16_T09_registro-vacio.png`, `2026-11-16_T09_registro-sin-aceptar-terminos.png` y `2026-11-16_T09_email-B-ya-registrado.png`, el botón del formulario Signup muestra el texto **`Signup`**.
  - `Submit` sale de la lectura accesible de `exploracion.md` (fila 1). No es el texto visible.
  - El resultado esperado de T09-01 paso 1 («Se muestran … Submit») no se puede verificar: quien ejecute el caso no verá ningún control con ese texto. Esto incumple la guía §11 («conservar los textos reales») y el §19 («no se inventaron … controles»).
- **Corrección mínima:**
  - Sustituir `Submit` por `Signup` en esos pasos y párrafos.
  - Si se quiere conservar el dato accesible: «botón Signup (nombre accesible Submit, según lectura AX)».
  - Hay que regenerar el XML desde el JSON corregido.
  - Login no tiene este problema: el botón visible es `Login` y T09-04 lo nombra bien.

No hay otros bloqueantes. En concreto:

- **Mensajes:** no se encontraron mensajes inventados. `Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.` aparece legible en las cuatro capturas de T09-06, T09-07, T09-09 y T09-10. `Error. Account with this email address already exists!` aparece legible en `email-B-ya-registrado`.
- **Límites:** no hay límites ni BVA inventados.
- **Jerarquías y otros tickets:** no hay tareas padre/subtareas ni duplicación real de otros tickets.
- **Secretos:** no hay secretos en las fichas.

---

## 2. No bloqueantes

Leyenda: **[Corregir antes de registrar]** = debe corregirse; documentarlo no basta. **[Documentar antes de registrar]** = puede quedar así si se documenta. **[Mejora]** = opcional.

### N1. [Corregir antes de registrar] El destino en TestLink sigue siendo una suite por ticket

- `importacion-propuesta.xml`, línea 2, tiene raíz `<testsuite name="T09">` con `<details>`. Importarlo así crearía una suite T09, en contra de la decisión vigente §14: suite existente `Todo.ly tests`, raíz `<testcases>`, sin crear suites y sin actualizar casos existentes.
- `analisis-diseno.md` §7 y `comentario-jira-borrador.md` §7 dicen «suite T09» y «Pendiente de punto de control y OK».
- `analisis-diseno.md` §7 y `comentario-jira-borrador.md` §7 citan `testlink-xml/T09.xml` como exportación final. Según la decisión §14, ese archivo se extrae por script de `testlink-xml/todo-ly-tests.xml`.
- **No se avala.** Hay que regenerar el XML con raíz `<testcases>` (sin `<testsuite>`, sin IDs y sin `node_order` de suite) y redactar §7 de nuevo: «suite existente Todo.ly tests; sin suite por ticket».

### N2. [Documentar antes de registrar] El estado del diseño está desactualizado

- `analisis-diseno.md` y el borrador, §9: «Después del OK…».
- Según la decisión §14 y `PROMPT_ORQUESTACION.md` §1, T09 ya no necesita otro OK del usuario si la revisión no tiene bloqueantes.
- Hay que actualizar la redacción sin afirmar registro ni revisión de integrante hasta que existan.

### N3. [Documentar antes de registrar] T09-09: la frase «contrastada mediante recuperación» no tiene apoyo en T09

- **Dónde:**
  - Precondición 3 de T09-09: «esta condición fue contrastada mediante recuperación en la exploración».
  - `analisis-diseno.md` §5.1: «Correo reservado contrastado por recuperación».
- **Problema:**
  - `exploracion.md` de T09 solo registra un Login rechazado con un correo de `example.com` (`login-cuenta-inexistente.png`). No registra ningún contraste mediante recuperación.
  - El prefijo `prueba-t10-…` sugiere que viene de T10, que está fuera de las lecturas autorizadas, así que no puedo verificarlo.
- **Corrección:** citar la fuente exacta (archivo/fila de T10) o reducir la precondición a lo observable: «correo del dominio reservado example.com, no utilizado por ninguna cuenta de prueba».
- No se debe presentar el rechazo de Login como prueba de que la cuenta no existe: la respuesta genérica no distingue entre ambos casos.

### N4. [Documentar antes de registrar] T09-02, paso 3: un resultado que no fue observado

- «Se accede a A y se conservan su identidad y nombre originales, sin aplicar el nombre del registro duplicado.»
- La exploración solo observó el mensaje de duplicado, y con la antigua candidata B, no con A. Nunca se comprobó la cuenta existente después del intento.
- Es un resultado esperado válido como **Criterio del equipo** (no sustituir una cuenta existente), pero `analisis-diseno.md` §3 no lo identifica así.
- **Corrección:** añadir en §3 la fila «Signup duplicado no altera la cuenta existente — Criterio del equipo; no observado». Pasa lo mismo con «no se registra una segunda cuenta con ese correo» (paso 2): no es directamente observable en la interfaz, así que conviene acotarlo a «no se inicia sesión en una cuenta nueva».

### N5. [Documentar antes de registrar] T09-01: atribución del mensaje y del aviso

- `Error. Please correct the missing fields.` solo se observó por lectura AX. `exploracion.md` fila 2 indica que desaparece antes de la captura. En `analisis-diseno.md` §3 la fila dice «Captura y AX»: conviene precisar que **el mensaje viene solo de AX** y que la captura muestra los asteriscos.
- El paso 2 debería advertir que el mensaje es transitorio («puede desaparecer en segundos»), para que no se dé por fallido el caso si no se captura a tiempo.
- `If you don’t agree you can’t use Todo.ly` se ve con la casilla desmarcada en ambas capturas, pero no en la de la casilla marcada. Ninguna evidencia demuestra si aparece por el envío o si está fijo mientras la casilla esté sin marcar. Mejor redactarlo como «se muestra el aviso…», sin presentarlo como efecto del Submit.

### N6. [Documentar antes de registrar] La captura de duplicado y las de Login con A muestran correos reales

- `2026-11-16_T09_email-B-ya-registrado.png` muestra legible un correo personal, además de pestañas, marcadores y extensiones del perfil personal.
- `login-A-password-vacio.png` y `login-A-password-incorrecto.png` muestran legible el correo de A.
- `registro-sin-aceptar-terminos.png` muestra parte de un identificador personal.
- No hay contraseñas, pero la decisión §7 y la regla 4 de AGENTS piden no exponer correos reales.
- **Corrección:** no adjuntar estas capturas a Jira ni a TestLink sin taparlas. Para Jira bastan el árbol de la suite y un caso abierto (modelo T12).

### N7. [Documentar antes de registrar] Controles no documentados en la exploración de T09

- «Cerrar Settings con Cancel» (T09-04 paso 4; T09-12 paso 1; T09-14 paso 6).
- «Pulsar Login, cuyo nombre accesible es Submit» (T09-04 paso 2).
- `exploracion.md` de T09 no registra `Cancel` en Settings: el único Cancel citado es del menú Window de Chrome. Tampoco registra el nombre accesible del botón Login.
- Probablemente se observaron en T10, pero no lo puedo verificar con las fuentes autorizadas.
- **Corrección:** citar la fuente o redactar de forma neutral («cerrar Settings sin guardar cambios», «pulsar Login»).

### N8. [Mejora] Textos visibles de la página pública

- T09-13 paso 4 y T09-01 paso 1 hablan de «Login/Signup» o «desplegar Signup».
- Las capturas `remember-off-reapertura-sin-sesion` y `atras-tras-logout` muestran **`Login`** y **`Sign Up Free`**. El título del formulario emergente sí es `Signup`.
- Sugerencia: «pulsar Sign Up Free; se abre el formulario Signup».

### N9. [Mejora] T09-03

- **Paso 1:** las capturas muestran el valor inicial cortado, «(UTC-08:00) Pacific Time (US & Cana…». La etiqueta completa es plausible, pero conviene anotar que se verifica al ejecutar.
- **Paso 4:** «no se modifica la configuración de A o B» no lo comprueba ninguna acción del caso. Basta con «no se crea cuenta ni se inicia sesión».

### N10. [Mejora] Redacción del presupuesto de intentos en las precondiciones (T09-07 y T09-10)

- «Menos de tres intentos fallidos asociados a A en la exploración del lote» depende del contexto de este equipo.
- Sugerencia: «Según criterio del equipo, la cuenta A acumula menos de tres intentos fallidos en la sesión de trabajo (no es una política de Todo.ly)».
- El valor literal `Prueba-T09-no-valida-17` es un dato de prueba inventado y declarado como no válido, no una credencial. La precondición exige que sea distinto de la clave vigente. Es aceptable; no se comparó con `.secrets/`.

### N11. [Mejora] T09-12, paso 6

- El regreso final de B y la conservación de su propio marcador en un segundo Login no se observaron como tales. Sí se observaron los dos sentidos de no-exposición (`B-marcador-y-ausencia-A` y `A-conserva-marcador-y-no-ve-B`).
- El resultado se apoya en el criterio de independencia (PEB-67), ya etiquetado en §3 como «Comportamiento observado / criterio». Basta con mantenerlo así.

### Cobertura pendiente (informar, no exigir en este registro)

- **T09-08 (email mal formado):** vista vacía sin causa confirmada. Está bien excluido.
- **Validaciones aisladas de cada campo de Signup**, incluido el formato de email: no se exploraron.
- **Registro válido completo controlado:** las cuentas las creó el usuario.
- **Pendientes con su riesgo para revisión del equipo:**
  - fronteras de longitud;
  - política de contraseñas;
  - bloqueo, CAPTCHA o límite de intentos del producto;
  - caducidad de la sesión recordada;
  - cierre completo del proceso de Chrome.

  Todo esto está bien declarado en §8. No se propone BVA porque no hay ninguna frontera confirmada.
- **Remember Me:** cada estado se observó una sola vez y con cuentas distintas (A desmarcado, B marcado). La matriz lo declara correctamente.
- **Criterio HTTPS:** pertenece a la recuperación (T10). Ningún caso de T09 lo usa ni lo necesita.

---

## 3. Checklist de la guía §19

| # | Ítem | Estado | Fundamento |
|---|---|---|---|
| 1 | Ticket correcto y alcance respetado | Cumple | PEB-73: registro, Login, Remember Me, Logout y cambio de cuenta. Timezone limitado al campo (decisión §12). Sin Pro, API ni eliminación de cuenta. |
| 2 | El análisis explica riesgos, reglas y dudas | Cumple | §2 tiene riesgos P×I con casos; §3 clasifica las reglas. Falta etiquetar el criterio de T09-02 (N4). |
| 3 | Cada técnica tiene aplicación real y justificación por caso | Cumple | Particiones, tabla de decisión R1–R6, transiciones S0–C2 y UC1/UC2 trazados a casos. BVA no aplicado y justificado. |
| 4 | Tipos de prueba elegidos por pertinencia | Cumple | Funcional y seguridad observable de sesión. Rendimiento y compatibilidad excluidos con motivo. |
| 5 | No se inventaron límites, controles, mensajes ni funciones | No cumple | B1 (`Submit` frente al `Signup` visible). Revisar N7 (Cancel en Settings, sin fuente en T09). Mensajes y límites correctos. |
| 6 | Sin jerarquías de tareas retiradas | Cumple | No aparecen tareas padre/subtareas. Sub Project solo aparece en capturas del estado inicial. |
| 7 | La ficha solo tiene los campos acordados | Cumple | Título, importancia + razón, requerimiento, precondiciones, descripción, pasos y postcondiciones. Sin severidad ni técnica. |
| 8 | Importancia, no severidad | Cumple | high/medium con razón. |
| 9 | Cada paso tiene un resultado verificable | Pendiente | Falla T09-01 paso 1 (B1). Débiles: T09-03 paso 4 y T09-02 pasos 2–3 (N4, N9). |
| 10 | Datos, controles y estados iniciales reproducibles | Pendiente | Precondiciones genéricas y sin acciones. Faltan la fuente de T09-09 (N3) y el nombre real del botón (B1). |
| 11 | Limpieza y postcondiciones dicen dónde terminan los datos | Cumple | Los marcadores de T09-11 y T09-12 quedan en Home para la limpieza del lote, de forma explícita. |
| 12 | Se distingue diseñado / registrado / revisado / ejecutado / fallido | Cumple | Todo figura como «diseñado, no registrado, no ejecutado». Registro, revisión de integrante y ejecución **no realizados**. |
| 13 | No se afirma cobertura o evidencia inexistente | Pendiente | Correcto en general. Por precisar: N3 (recuperación no documentada en T09), N5 (mensaje atribuido a la captura) y N1 (exportación T09.xml frente a extracción por script). |

---

## 4. Veredicto

**NO APTO** para `casos-listos.json` en su estado actual, solo por **B1**: el control `Submit` no existe con ese texto en la interfaz y deja inverificable el resultado de T09-01 paso 1. Afecta también a la acción de T09-01 paso 2 y T09-02 paso 2.

Pasa a APTO con la corrección mínima de B1 en `casos-listos.json`, en las fichas de `analisis-diseno.md`/borrador y en el XML regenerado. No hace falta explorar de nuevo ni cambiar el diseño de técnicas.

Antes de importar hay que hacer además:

- **N1 (corregir):** XML con raíz `<testcases>` en la suite existente `Todo.ly tests`, sin crear suites.
- **N2–N7 (documentar o corregir):**
  - N2: estado §9;
  - N3: fuente de T09-09;
  - N4: criterio en T09-02;
  - N5: origen AX del mensaje de T09-01;
  - N6: no publicar capturas con correos reales;
  - N7: fuente de Cancel.

Esta revisión no equivale a la revisión de otro integrante. El estado tras registrar sigue siendo «pendiente de revisión por otro integrante».
