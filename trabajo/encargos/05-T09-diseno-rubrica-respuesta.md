# Respuesta — Encargo 05: diseño editorial de T09 conforme a la rúbrica nueva

Autor: Claude (agente de diseño). Fecha: 18/11/2026.

**Alcance.** Se reescribió la redacción de `trabajo/T09/casos-listos.json` y `trabajo/T09/casos-pendientes.json`. No se tocaron otros archivos: casos.json, fichas, lista resumida, borrador y XML los sincroniza Codex.

**Lo que no se hizo:**

- No se leyó ni se escribió `revision-testlink/`.
- No se usó navegador, Jira, TestLink ni git.
- No se leyó `.secrets/`.
- No se releyeron PDFs.

No se afirma registro, publicación, ejecución ni revisión de un integrante. La revisión independiente queda para una llamada nueva.

**Fuentes leídas:**

- `AGENTS.md`, `docs/decisiones-vigentes.md` (incluida la §15) y la rúbrica de `PROMPT_REVISION_TESTLINK.md`.
- `plantillas/caso-testlink.md` y la guía, §7–11 y §19.
- `trabajo/00-contexto.md`.
- De T09: `analisis-diseno.md`, `exploracion.md` y los dos JSON.
- Respuestas y resoluciones de las revisiones 02 y 03.
- `trabajo/T10/exploracion.md`.

## 1. Cambios aplicados

### Títulos

Cada título sigue la forma funcionalidad + condición + resultado. Con el prefijo `T09-NN - ` ninguno pasa de 82 caracteres. Ejemplos:

- `Signup con campos vacíos y términos sin aceptar rechaza el envío`
- `Login de A con contraseña incorrecta muestra error y no concede acceso`
- `Remember Me marcado: al reabrir el perfil se restaura la sesión de B`

El campo `titulo` sigue sin el prefijo, como antes. T09-08 ahora dice «respuesta pendiente de confirmar» en lugar de «Investigar…», y no anticipa ningún resultado.

### Descripción

Cada caso tiene una sola oración que empieza con «Validar que…». Se conservan las acotaciones que ya existían:

- sin aislar condiciones concurrentes (T09-01);
- sin evaluar vencimientos (T09-03);
- un único intento negativo (T09-05 a T09-10);
- sin inferir caducidad (T09-13).

### Precondiciones

Ahora son nominales y no llevan verbos conjugados.

| Antes | Después |
|---|---|
| «…conocidas por quien ejecuta…» | «Cuenta gratuita de prueba (cuenta A) con correo y contraseña vigentes consignados en el registro privado de credenciales.» |
| «A acumula menos de tres intentos…» | «Cuenta A con menos de tres intentos fallidos de Login en la sesión de trabajo, según criterio operativo del equipo (no es una política de Todo.ly).» |
| «la clave vigente es distinta de…» | «Contraseña vigente de A distinta de **Prueba-T09-no-valida-17**.» |
| «No existen los marcadores…» | «**Home** de A sin una tarea llamada **Prueba T09-12 - marcador A**; **Home** de B sin…» |
| «posibilidad de reabrir ese mismo perfil» / «configuración de Chrome estable» | «Perfil dedicado de Chrome para QA, sin otras ventanas abiertas de ese perfil y disponible en el selector de perfiles de Chrome para su reapertura.» y «Configuración de Chrome sin cambios durante todo el recorrido.» |
| T09-09: «La dirección… no pertenece a una cuenta» | «Dirección reservada **…@example.com** sin cuenta asociada en Todo.ly, según el contraste de recuperación de PEB-74 / T10 (respuesta Error. Account with this Email address doesn't exist.).» |
| T09-02: «Datos de registro válidos… y aceptación de los términos por quien ejecuta» | Contraseña de prueba para Signup en el registro privado, distinta de la vigente de A, y «Aceptación de los términos de Todo.ly autorizada para las cuentas de prueba». |
| T09-11: «Sesión iniciada como A» | «Sesión iniciada en Todo.ly con la cuenta A, en **https://todo.ly/**». Es la redacción genérica de la decisión §7, con la URL que la exploración observó durante la sesión. |

Además:

- Se mantiene exacta la precondición «Sin sesión iniciada en Todo.ly en el navegador.».
- No hay correos ni claves reales. Los datos de prueba se conservan exactos: `Prueba-T09-no-valida-17`, el correo de example.com, `PruebaT09SinArroba` y los nombres de los marcadores.

### Pasos

Hay una acción por paso, en infinitivo, con los controles y los datos exactos en `**negrita**` para que el XML los convierta en `strong`. Se separaron en pasos propios:

- la apertura de `https://todo.ly/`;
- el clic en **Login** o **Sign Up Free**;
- cada campo (**Email**, **Password**, **Full Name**, **Timezone** y la casilla de términos);
- el estado de **Remember Me**;
- el envío;
- **Settings**, **Profile**, la comparación de identidad, **Cancel** y **Logout**;
- **Home**, **Add new Todo** y **Add**;
- las capturas;
- las anotaciones de hora de cierre y de reapertura;
- la reapertura del perfil.

T09-12 ya no usa atajos como «Iniciar sesión como A»: cada Login está desarrollado campo a campo y no se remite a otro caso.

### Resultados por paso

Cada resultado corresponde a la acción de su paso:

- un campo introducido refleja el dato;
- los clics de envío llevan el mensaje o estado conocido.

Matices conservados:

- **T09-01:** el aviso `Error. Please correct the missing fields.` figura como transitorio e identificado por lectura de accesibilidad, «no se exige en la captura». El paso de captura solo exige los asteriscos y `If you don’t agree you can’t use Todo.ly`.
- **T09-05:** no exige mensaje. El paso de captura solo exige el formulario sin sesión.
- **T09-03:** el valor inicial se mantiene como opción Pacific UTC-08 con el texto recortado `(UTC-08:00) Pacific Time (US & Cana…`. No se completa el literal.
- **Mensajes que no cambian:** el genérico de Login se exige en T09-06, 07, 09 y 10, y el de duplicado en T09-02. Ambos se ven en capturas, según las revisiones 02 y 03.
- **T09-08:** sigue con el resultado `PENDIENTE` sin un esperado inventado. Solo se separaron sus acciones.

## 2. Número de casos y pasos

| Conjunto | Casos | Pasos antes | Pasos ahora |
|---|---|---|---|
| `casos-listos.json` | 13 (T09-01 a T09-07, T09-09 a T09-14) | 52 | 158 |
| `casos-pendientes.json` | 1 (T09-08) | 3 | 6 |

Pasos por caso en los listos:

| Caso | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 09 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pasos | 6 | 16 | 8 | 11 | 6 | 7 | 7 | 7 | 7 | 7 | 39 | 16 | 21 |

No se borraron ni se agregaron casos.

## 3. Dudas que limitan la rúbrica (para Codex o para la revisión)

1. **Profile dentro de Settings.** Las fuentes dicen «Settings / Profile» y «abrir Profile», pero no aclaran si Profile se muestra por defecto o requiere un clic aparte. Se usó «Seleccionar **Profile** en **Settings**» como paso propio. Si Profile aparece directamente, ese paso es redundante pero sigue siendo ejecutable.
2. **Etiqueta de la casilla de términos.** No está transcrita en las fuentes, así que se escribe «la casilla de términos», sin negrita ni texto inventado.
3. **Enmascarado de Password.**
   - En Login, «muestra el valor enmascarado» tiene respaldo en T10 (Password enmascarado en el formulario de Login preparado).
   - En el Password de Signup no consta, así que T09-02 dice «contiene el valor introducido».
4. **Estado inicial de la casilla de términos (T09-01, paso 3).** El resultado «sin marcar» se basa en el envío explorado. No se añadió una acción condicional de desmarcar.
5. **Título del formulario de Login.** No está registrado, así que se describe como «formulario de acceso», enumerando sus controles observados: **Email**, **Password**, **Remember Me** y el botón **Login**.
6. **Opción mexicana UTC-07 (T09-03).** Se escribió el literal `(UTC-07:00) Chihuahua, La Paz, Mazatlan`, tomado de la decisión §12. Antes decía «opción mexicana UTC-07». No se agrega ninguna regla nueva.
7. **Reapertura del perfil (T09-13 y T09-14).** El menú **Profiles** solo se observó en macOS. El paso dice «selector de perfiles de Chrome (menú **Profiles** en macOS)». En Windows, quien ejecute usará el selector equivalente. No se inventó un control para Windows.
8. **Botón Atrás (T09-11).** Es un control de Chrome, no de Todo.ly. Se nombra **Atrás**. Con Chrome en inglés se llama Back.
9. **Cierre de T09-02.**
   - El caso original termina en Profile con la sesión de A abierta.
   - No se añadieron **Cancel** ni **Logout**, porque serían acciones de restauración nuevas y no una separación de pasos.
   - Si Codex o el usuario quieren añadirlos, ambos controles tienen respaldo (T09-04). La postcondición tendría que mencionar entonces la sesión cerrada.
10. **Longitud de T09-12.** Tiene 39 pasos porque cada Login se desarrolla completo. Es fiel a la rúbrica («no uses ejecutar otro caso como atajo»), aunque extenso.
11. **Capturas de Profile (T09-14, paso 19).** Pueden mostrar el correo de la cuenta de prueba de quien ejecute. Rige la política ya documentada: no publicar capturas con correos reales y usar como evidencia el árbol y los casos de TestLink.
12. **T09-08, paso 6.** Conserva «abrir… y anotar el estado» en un solo paso, porque la anotación es el registro del resultado pendiente y no una acción independiente.

Ninguna de estas dudas obliga a pasar un caso listo a pendiente.

## 4. Checklist de no alteración

| Comprobación | Estado |
|---|---|
| Exactamente 13 IDs listos (T09-01 a T09-07, T09-09 a T09-14) y T09-08 solo en pendientes | Cumple |
| Estructura JSON intacta: mismos campos y pasos como pares [acción, resultado] | Cumple |
| `importancia` y `razon` sin cambios | Cumple |
| `requerimiento` sin cambios | Cumple |
| `postcondiciones` sin cambios | Cumple |
| Cobertura: las mismas reglas R1–R6, secuencias S0–C2, UC1/UC2 y particiones; ningún caso nuevo ni borrado | Cumple |
| Todos los resultados originales conservados, ahora repartidos por pasos | Cumple |
| Restauraciones o cierres originales conservados: Cancel/Logout en T09-04 y T09-14; Logout final en T09-12; vuelta a la página pública en T09-01, 03, 05–10; marcadores para la limpieza del lote en T09-11/12 | Cumple |
| Sin mensajes, controles, límites ni plazos nuevos; sin BVA | Cumple. Literales nuevos con fuente: el UTC-07 de la decisión §12 y el enmascarado de Login de T10. |
| Criterios del equipo marcados como tales: presupuesto de tres intentos, independencia tras un duplicado, separación A/B | Cumple. Las precondiciones de intentos dicen «criterio operativo del equipo (no es una política de Todo.ly)». |
| Correo inexistente sustentado por T10, no por el mensaje genérico de Login | Cumple |
| Timezone limitado al formulario | Cumple |
| Remember Me: un estado por cuenta (A desmarcado, B marcado), sin inferir caducidad | Cumple |
| Sin correos ni contraseñas reales; las credenciales se citan como referencias al registro privado | Cumple |
| T09-08 pendiente, sin esperado inventado | Cumple |

Estado: **rediseño editorial preparado para revisión independiente.** No está registrado en TestLink, no está publicado en Jira y no se ha ejecutado.
