# Respuesta — Revisión independiente de T09 / PEB-73 (después de correcciones)

Revisor: Claude (agente). Fecha: 17/11/2026.

**Alcance:**

- `trabajo/T09/casos-listos.json` (13 casos: T09-01 a T09-07 y T09-09 a T09-14).
- Su importación `trabajo/T09/importacion-propuesta.xml`.
- Los artefactos de soporte `analisis-diseno.md`, `comentario-jira-borrador.md` y `exploracion.md`.

T09-08 (`casos-pendientes.json`) está excluido del registro. Solo se menciona como cobertura pendiente.

**Lo que esta revisión no es ni hizo:**

- No sustituye la revisión de otro integrante.
- No se registró nada en TestLink, no se publicó nada en Jira y no se ejecutó ningún caso.
- No se leyó `.secrets/` ni se buscó en esa carpeta.
- No se ejecutaron comandos.

**Fuentes leídas:**

- `AGENTS.md`, `docs/decisiones-vigentes.md`, `PROMPT_ORQUESTACION.md` y la guía, §7–11 y §19.
- `trabajo/fuentes/PEB-73.md`.
- Las respuestas y la resolución del encargo 02.
- Los artefactos actuales de T09.
- `trabajo/T10/exploracion.md` como fuente cruzada autorizada.

**Capturas inspeccionadas directamente:**

- `2026-11-16_T09_registro-vacio.png`: título `Signup`, botón visible `Signup`, asteriscos, aviso `If you don’t agree you can’t use Todo.ly`, Timezone `(UTC-08:00) Pacific Time (US & Cana…` recortado.
- `2026-11-17_T09_remember-off-reapertura-sin-sesion.png`: `Login` y `Sign Up Free`, sin sesión.
- `2026-11-17_T09_login-cuenta-inexistente.png`: Email `prueba-t10-no-registrada-20…`, aviso `Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.` y botón visible `Login`.
- `trabajo/T10/evidencias/2026-11-17_T10_old-password-vacio-Invalid-Password.png`: Settings / Profile con los botones `Ok` y `Cancel`.

## Verificación de las correcciones del encargo 02

| Hallazgo previo | Estado en los artefactos actuales |
|---|---|
| B1 `Submit` en lugar de `Signup` | **Resuelto.** T09-01 paso 1 dice «botón Signup (nombre accesible Submit)», y las acciones de T09-01 y T09-02 dicen «pulsar Signup». Coincide en JSON, fichas y XML. Confirmado en `registro-vacio`. |
| N1 suite por ticket / raíz `<testsuite>` | **Resuelto.** El XML tiene raíz `<testcases>`, sin `<testsuite>`, sin `internalid` ni `externalid`. `analisis-diseno.md` §7 y el borrador §7 dicen «suite existente Todo.ly tests… sin crear suites ni actualizar existentes». La exportación final es `todo-ly-tests.xml` y el T09.xml se extrae por script. |
| N2 OK antiguo | **Resuelto.** §7 y §9 dicen «registro autorizado tras revisión sin bloqueantes», sin declarar registro ni revisión. |
| N3 fuente de la inexistencia del correo de T09-09 | **Resuelto.** `trabajo/T10/exploracion.md` l. 31, a las 11:13 AM, registra la recuperación con `prueba-t10-no-registrada-20261117@example.com` y el mensaje `Error. Account with this Email address doesn't exist.`. La captura de Login de T09 muestra la misma dirección. El diseño ya no deduce la inexistencia del mensaje genérico de Login. |
| N4 integridad de A tras un duplicado | **Resuelto.** `analisis-diseno.md` §3 la etiqueta como «Criterio del equipo», no como observación. El paso 2 está acotado a «no se inicia sesión en una cuenta nueva». |
| N5 aviso de Signup | **Resuelto.** §3 atribuye el mensaje global a la lectura AX y los asteriscos y el aviso de términos a la captura. El paso 2 advierte que el aviso es transitorio. |
| N6 correos en capturas | **Documentado** en `analisis-diseno.md` §3, «Fuentes cruzadas…»: no se publicarán capturas de exploración con correos reales. Véase también N5 más abajo. |
| N7 `Cancel` de Settings y `Submit` de Login | **Resuelto.** `trabajo/T10/exploracion.md` l. 9 registra los botones `Ok` y `Cancel` en Settings / Profile, y la captura de Old Password vacío los muestra. `exploracion.md` de T09, l. 119, registra la fuente cruzada. |
| N8 `Sign Up Free` | **Resuelto.** Ya aparece en T09-01, T09-02, T09-03 y T09-13. |
| N9 Timezone y cierre de T09-03 | **Resuelto en el paso 4**: «página pública sin registro completado ni sesión iniciada». La etiqueta completa del paso 1 sigue con una observación menor (N3 más abajo). |
| N10 presupuesto de intentos | **Resuelto.** T09-07 y T09-10 dicen «Según criterio del equipo… (no es una política de Todo.ly)». |
| N11 regreso final de B | Se mantiene como resultado esperado basado en el criterio de independencia. Es aceptable. |

---

## 1. Bloqueantes

**Ninguno.**

Comprobaciones concretas:

- **Mensajes.** Los dos mensajes literales tienen respaldo:
  - `Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.` se exige en T09-06, T09-07, T09-09 y T09-10. Se ve legible en las capturas de Login de T09, por ejemplo `login-cuenta-inexistente`, y también en T10 l. 58.
  - `Error. Account with this email address already exists!` se exige en T09-02. Respaldo: `exploracion.md` l. 45 y `email-B-ya-registrado`.
  - `Error. Please correct the missing fields.` se exige en T09-01. Viene de la lectura AX y está declarado como tal y como transitorio.
  - T09-05 no exige mensaje, lo que coincide con «mensaje no retenido» en `exploracion.md` l. 72.
- **Controles.** Todos los que usan los casos aparecen en la exploración, en capturas o en la fuente cruzada de T10:
  - `Sign Up Free`, `Signup`, `Login`, `Remember Me`, `Settings`, `Logout` y `Add`;
  - `Profile` y `Cancel`.
- **Límites.** No hay BVA ni fronteras inventadas. El valor 101 de Timezone es un inventario observado, no un límite.
- **Trazabilidad técnica.**
  - La tabla de decisión R1–R6 corresponde a T09-05, 06, 07, 09, 10 y 04.
  - Las transiciones S0–C2 corresponden a T09-04, 11, 13 y 14.
  - UC1 corresponde a T09-01, 02 y 03; UC2, a T09-12.
  - Las particiones de §5.1 están asignadas a sus casos.
  - Ninguna técnica figura sin un caso derivado, y BVA está justificado como no aplicado.
- **Ficha.** Tiene título, importancia con razón, requerimiento, precondiciones, descripción, pasos con su resultado y postcondiciones. No incluye severidad ni técnica. En el XML, `importance` vale 2 para medium y 3 para high, `execution_type` vale 1 (manual) y los pasos son nativos.
- **Precondiciones.** Describen estados, cuentas genéricas A/B y configuración, sin acciones. No contienen correos ni contraseñas reales. `Prueba-T09-no-valida-17` es un dato de prueba declarado como no válido y la precondición exige que sea distinto de la clave vigente, así que no es una credencial. No se comparó con `.secrets/`.
- **Alcance.**
  - No hay tareas padre ni subtareas.
  - Las tareas de T09-11 y T09-12 son marcadores de preparación y declaran el solapamiento con T06.
  - Timezone se limita al campo, según la decisión §12.
  - No hay Pro, API ni eliminación de cuenta.
- **Importación.** El XML coincide caso por caso con `casos-listos.json`: 13 casos, T09-08 ausente, los mismos textos y `node_order` del 1 al 13. No crea suites ni trae IDs.

---

## 2. No bloqueantes

Leyenda:

- **[Documentar antes de registrar]**: puede registrarse así si queda anotado en la resolución o el análisis.
- **[Mejora]**: opcional.

### N1. [Mejora] «Pulsar Login / Submit una sola vez»

- **Dónde:** paso 2 de T09-05, T09-06, T09-07, T09-09 y T09-10, en el JSON, las fichas y el XML.
- **Problema:** el botón visible es `Login`, como se ve en `login-cuenta-inexistente.png`. `Submit` es solo su nombre accesible (`exploracion.md` l. 119). La barra puede hacer pensar que hay dos controles.
- **Por qué no bloquea:** la acción se puede ejecutar porque el texto visible aparece primero, y ningún resultado esperado exige ver «Submit». Es distinto del antiguo B1.
- **Sugerencia:** usar la misma forma que T09-01: «Pulsar Login (nombre accesible Submit) una sola vez».

### N2. [Mejora] Ruta interna del repositorio en una precondición de TestLink

- **Dónde:** T09-09, precondición 3: «fuente del contraste: trabajo/T10/exploracion.md, sección…».
- **Problema:** quien ejecute desde TestLink no tiene acceso a esa ruta.
- **Sugerencia:** «… no pertenece a una cuenta (contrastado en la exploración de PEB-74 / T10: la recuperación respondió `Error. Account with this Email address doesn't exist.`)». La ruta exacta puede quedarse en `analisis-diseno.md` §5.1.

### N3. [Documentar antes de registrar] T09-03 paso 1: etiqueta completa de Pacific

- **Dónde:** T09-03, paso 1. Resultado esperado: `(UTC-08:00) Pacific Time (US & Canada)`.
- **Problema:**
  - La captura `registro-vacio` muestra la etiqueta recortada, «(UTC-08:00) Pacific Time (US & Cana…».
  - `exploracion.md` fila 1 dice «Pacific Time seleccionado inicialmente» y la fila 5 describe el listado AX sin transcribir esa opción.
  - La resolución 02 atribuye el texto completo al «listado AX ya documentado», pero ese literal no figura en `exploracion.md`.
- **Corrección mínima, una de dos:**
  - añadir a `exploracion.md` el literal de la lectura AX;
  - o redactar el resultado como «muestra la opción Pacific UTC-08 (`(UTC-08:00) Pacific Time (US & Cana…` visible)».
- El calificativo «según la referencia observada» evita que sea un bloqueante.

### N4. [Mejora] T09-13 paso 2: el resultado no recoge la verificación de identidad

- **Problema:** la acción incluye «confirmar identidad en Profile», pero el resultado solo dice «Se inicia sesión en A; Settings y Logout están disponibles».
- **Sugerencia:** añadir «Profile muestra el nombre y el correo de A». T09-14 paso 2 lo hace con B.

### N5. [Documentar antes de registrar] Capturas con correos reales, ampliado a la fuente cruzada de T10

- La captura `2026-11-17_T10_old-password-vacio-Invalid-Password.png`, ahora citada como fuente de `Cancel`, muestra legible un correo personal en Profile.
- Se suma a las capturas de T09 ya señaladas en la revisión 02 (N6).
- La decisión documentada de publicar solo el árbol y los casos abiertos de TestLink cubre este caso. Basta con que la resolución mencione también la captura de T10.

### N6. [Mejora] T09-02 paso 1: «contraseña de prueba privada válida»

- **Problema:** la política de contraseñas es una Duda pendiente (§3), así que «válida» no se puede comprobar de antemano.
- **Sugerencia:** «una contraseña de prueba privada distinta de la vigente de A». Si aparece un mensaje distinto del de duplicado, se registra como resultado real de la ejecución.

### N7. [Mejora] Redacción menor

- En T09-05, «dejar o introducir Email vacío y Password vacío» puede quedarse en «dejar Email y Password vacíos».
- En T09-05 paso 1, el resultado «con datos de prueba» no aplica cuando ambos campos están vacíos.
- El borrador de Jira, §1 y §3, menciona «Codex» y rutas del repositorio. Para un comentario en tercera persona dirigido al equipo conviene decir «se verificó en las capturas de exploración» y citar los nombres de evidencia sin rutas. Es opcional.

### Cobertura pendiente (se informa, no se exige en este registro)

- **T09-08, email mal formado:** las vistas vacías no tienen causa confirmada. Está bien excluido y no debe registrarse con un resultado condicional.
- **Signup:** faltan las validaciones aisladas de cada campo y un registro válido completo bajo control del equipo.
- **Fronteras de longitud y política de contraseñas:** sin confirmar. No se propone BVA.
- **Bloqueo, CAPTCHA o límite de intentos del producto:** no se observaron ni se afirma que no existan.
- **Caducidad de la sesión recordada y cierre completo del proceso Chrome.**
- **Remember Me:** cada estado se observó una vez y con cuentas distintas (A desmarcado, B marcado). Está declarado.
- **Criterio HTTPS:** es un criterio del equipo indicado por el usuario y corresponde a la recuperación (T10). Ningún caso de T09 lo necesita.

Todo esto ya figura en `analisis-diseno.md` §8 y en el borrador.

---

## Checklist de la guía §19

| # | Ítem | Estado | Fundamento |
|---|---|---|---|
| 1 | Ticket correcto y alcance respetado | Cumple | PEB-73: registro, Login, Remember Me, Logout y cambio de cuenta. Timezone limitado al campo. Sin Pro, API ni eliminación de cuenta. Los marcadores de tarea declaran el solapamiento con T06. |
| 2 | El análisis explica riesgos, reglas y dudas | Cumple | Riesgos R1–R6 con P×I y casos. §3 clasifica Comportamiento observado, Criterio del equipo y Duda pendiente, incluido el criterio de T09-02. |
| 3 | Cada técnica tiene aplicación real y justificación por caso | Cumple | Particiones (§5.1), tabla de decisión R1–R6, matriz S0–C2 con secuencias y UC1/UC2, todas trazadas a casos. BVA no aplicado y justificado. |
| 4 | Tipos de prueba elegidos por pertinencia | Cumple | Funcional y seguridad observable de sesión, con criterio observable. Rendimiento y compatibilidad excluidos con motivo. |
| 5 | No se inventaron límites, controles, mensajes ni funciones | Cumple | Mensajes y controles con fuente: capturas, AX o T10. Observaciones menores en N1 («Login / Submit») y N3 (literal de Pacific). |
| 6 | Sin jerarquías de tareas retiradas | Cumple | No aparecen tareas padre ni subtareas. |
| 7 | La ficha solo tiene los campos acordados | Cumple | Siete campos. Sin severidad ni técnica. En el XML, Summary agrupa importancia, requerimiento, descripción y postcondiciones, y Preconditions va aparte. |
| 8 | Importancia, no severidad | Cumple | high o medium con razón. En el XML, 3 y 2. |
| 9 | Cada paso tiene un resultado verificable | Cumple | Todos los pasos tienen un resultado observable. Mejora en T09-13 paso 2 (N4). |
| 10 | Datos, controles y estados iniciales reproducibles | Cumple | Precondiciones genéricas y sin acciones, con marcadores de nombre único. Fuente de T09-09 citada. Matices en N2, N3 y N6. |
| 11 | Limpieza y postcondiciones dicen dónde terminan los datos | Cumple | Los marcadores de T09-11 y T09-12 quedan en Home para la limpieza del lote. Las sesiones quedan cerradas. |
| 12 | Se distingue diseñado / registrado / revisado / ejecutado / fallido | Cumple | Estado: «diseñados, no registrados, no ejecutados». Registro, revisión de integrante y ejecución **no realizados**. |
| 13 | No se afirma cobertura o evidencia inexistente | Cumple | Las fuentes cruzadas están declaradas y el criterio del equipo está separado de lo observado. La exportación real y la extracción por script figuran como futuras. N3 debe documentarse. |

---

## 3. Veredicto

**APTO** para el conjunto `casos-listos.json` (13 casos) y su importación `importacion-propuesta.xml`, tal como están ahora.

- No queda ningún bloqueante vigente.
- El XML cumple la decisión §14: raíz `<testcases>`, destino en la suite existente `Todo.ly tests`, sin crear suites, sin IDs y sin actualizar casos existentes.
- El veredicto no depende de corregir nada más.
- Los no bloqueantes N1–N7 pueden resolverse antes de importar o quedar documentados, como pide `PROMPT_ORQUESTACION.md` §1. Los que piden al menos dejar constancia son N3 y N5.

El veredicto no cubre T09-08 ni otros candidatos pendientes, y no equivale a la revisión de otro integrante. Después del registro, el estado debe seguir siendo «pendiente de revisión por otro integrante».
