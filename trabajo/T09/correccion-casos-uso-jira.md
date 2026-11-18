## 5. Técnica aplicada: casos de uso

Técnica única: casos de uso (PDF docente pp. 58–62). **A** es el actor (quien opera la interfaz) y **S** el sistema (Todo.ly); se numera el escenario principal y cada extensión parte de un paso existente; un caso de uso puede derivar varios casos. Cuenta A y cuenta B son cuentas de prueba, no el actor. Cada respuesta de S procede de exploracion.md o de un criterio del equipo identificado. No hay límites confirmados ni registro válido observado bajo control: este último queda pendiente.

**UC1 — Preparar Signup y abandonar el envío.** Objetivo: A prepara el formulario y lo abandona sin registrar; antes puede enviarlo vacío o con un correo ya registrado. Precondiciones: sin sesión en Chrome; para 7a, cuenta A con credenciales en el registro privado, contraseña de prueba distinta de la vigente y términos autorizados.

| Escenario | Paso | Descripción |
|---|---|---|
| Principal | 1 | A: abre https://todo.ly/ y pulsa Sign Up Free. |
| | 2 | S: muestra Signup con Full Name, Email, Password, Timezone, términos y botón Signup. |
| | 3 | A: despliega Timezone. |
| | 4 | S: inicial Pacific UTC-08; lista sin entrada vacía con `(UTC-04:00) Georgetown, La Paz, Manaus, San Juan`, distinta de `(UTC-07:00) Chihuahua, La Paz, Mazatlan`. |
| | 5 | A: selecciona La Paz UTC-04. |
| | 6 | S: el selector muestra exactamente esa opción. |
| | 7 | A: abre https://todo.ly/ sin pulsar Signup. |
| | 8 | S: página pública, sin registro ni sesión. |
| Extensiones | 3a | A: conserva Timezone, deja Full Name, Email y Password vacíos y términos sin marcar; pulsa Signup. |
| | 3a.1 | S: no registra; asteriscos en los tres campos y `If you don’t agree you can’t use Todo.ly`; `Error. Please correct the missing fields.` transitorio (AX). Respuesta conjunta, sin obligatoriedad independiente. Sigue en 7. |
| | 7a | A: en lugar de abandonar, informa Full Name de prueba, Email de la cuenta A y la contraseña de prueba, marca términos y pulsa Signup. |
| | 7a.1 | S: `Error. Account with this email address already exists!`; no abre sesión nueva. |
| | 7a.2 | A: inicia sesión con las credenciales vigentes de A y abre Settings / Profile. |
| | 7a.3 | S: conserva Full Name y Email de A (criterio del equipo). |

Postcondición: sin cuenta nueva; en 7a, sesión de A con Profile abierto. **Derivación:** principal 1–8 → **T09-03**, recorrido parcial que no cubre el registro completo; 3a → **T09-01**; 7a → **T09-02**.

**UC2 — Iniciar sesión.** Objetivo: A accede con la identidad propia. Precondiciones: sin sesión; cuenta A con credenciales y nombres en el registro privado. Las extensiones 3a–3f sustituyen el paso 3 y continúan con el envío 4; cada rechazo confirmado sustituye la respuesta 5 y finaliza sin sesión. La extensión 3d permanece sin resultado definido.

| Escenario | Paso | Descripción |
|---|---|---|
| Principal | 1 | A: abre https://todo.ly/ y pulsa Login. |
| | 2 | S: despliega Email, Password, Remember Me y Login. |
| | 3 | A: informa correo y contraseña vigentes de A, con Remember Me desmarcada. |
| | 4 | A: pulsa Login una vez. |
| | 5 | S: área autenticada con Settings y Logout; Profile muestra Full Name y Email de A. |
| | 6 | A: pulsa Cancel y Logout; S: página pública sin sesión. |
| Extensiones | 3a | A: deja Email y Password vacíos. |
| | 3a.1 | S (tras 4): no concede acceso; Login sigue disponible. Sin mensaje literal exigido: no se retuvo. |
| | 3b | A: Email vacío y Password de prueba. |
| | 3b.1 | S: sin acceso; aviso genérico `Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.` |
| | 3c | A: Email de A y Password vacío. |
| | 3c.1 | S: sin acceso; aviso genérico. |
| | 3d | A: Email sin arroba y Password de prueba. |
| | 3d.1 | S: pendiente; las vistas vacías no fijan resultado ni validador. |
| | 3e | A: correo reservado de example.com sin cuenta (contraste T10) y Password de prueba. |
| | 3e.1 | S: sin acceso; aviso genérico. |
| | 3f | A: Email de A y Password de prueba que no le corresponde. |
| | 3f.1 | S: sin acceso; aviso genérico. |

Postcondición del principal y los rechazos confirmados: sesión cerrada y A sin cambios; un intento negativo por caso. No se atribuye postcondición a 3d, pendiente. **Derivación:** principal → **T09-04**; 3a → **T09-05**; 3b → **T09-06**; 3c → **T09-07**; 3e → **T09-09**; 3f → **T09-10**; 3d → **T09-08** pendiente, sin resultado esperado ni registro.

**UC3 — Cerrar sesión y navegar después.** Objetivo: A cierra sesión sin que la navegación posterior recupere datos. Precondiciones: sesión de A en https://todo.ly/; Home de A sin `Prueba T09-11 - sesión`.

| Escenario | Paso | Descripción |
|---|---|---|
| Principal | 1 | A: añade `Prueba T09-11 - sesión` en Home. |
| | 2 | S: muestra el marcador en Home de A. |
| | 3 | A: pulsa Logout. |
| | 4 | S: página pública con Login y Sign Up Free, sin el marcador. |
| | 5 | A: pulsa Back de Chrome. |
| | 6 | S: no restablece sesión ni muestra el marcador. |
| | 7 | A: abre https://todo.ly/ sin Login. |
| | 8 | S: página pública con Login, sin el marcador. |

Postcondición: sesión cerrada; marcador pendiente de limpieza. No se extrapola a otras URL internas ni a caducidad. **Derivación:** principal 1–8 → **T09-11**.

**UC4 — Alternar entre cuentas A y B.** Objetivo: cada cuenta muestra solo sus datos. Precondiciones: sin sesión; dos cuentas gratuitas de prueba sin proyectos compartidos (A y B), credenciales y nombres en el registro privado; Home de cada una sin marcadores T09-12.

| Escenario | Paso | Descripción |
|---|---|---|
| Principal | 1 | A: inicia sesión con A, confirma Profile y añade `Prueba T09-12 - marcador A` en Home. |
| | 2 | S: Home de A muestra su marcador. |
| | 3 | A: Logout; inicia sesión con B, confirma Profile y abre Home. |
| | 4 | S: Home de B sin el marcador A. |
| | 5 | A: añade `Prueba T09-12 - marcador B`; Logout; inicia sesión con A y abre Home. |
| | 6 | S: muestra el marcador A, no el B. |
| | 7 | A: Logout; inicia sesión con B y abre Home. |
| | 8 | S: muestra el marcador B, no el A. |
| | 9 | A: Logout; S: página pública. |

Postcondición: cada marcador en su cuenta, pendiente de limpieza. **Derivación:** principal 1–9 → **T09-12**, ida y vuelta A→B→A→B.

**UC5 — Reabrir el perfil con o sin Remember Me.** Objetivo: A comprueba si la sesión se recuerda al reabrir. Precondiciones: perfil dedicado de Chrome para QA, no incógnito, sin sesión de Todo.ly ni otras ventanas propias; otra ventana de un perfil distinto abierta; configuración de Chrome sin cambios; cuentas A y B en el registro privado.

| Escenario | Paso | Descripción |
|---|---|---|
| Principal | 1 | A: abre https://todo.ly/ en el perfil dedicado y pulsa Login. |
| | 2 | A: deja Remember Me marcada, informa credenciales vigentes de B y pulsa Login. |
| | 3 | S: área autenticada; Profile confirma la identidad de B. |
| | 4 | A: anota la hora y cierra todas las ventanas del perfil, sin Logout, sin borrar cookies ni cerrar otros perfiles. |
| | 5 | A: reabre el mismo perfil desde Profiles, anota la hora y abre https://todo.ly/ sin credenciales. |
| | 6 | S: Settings y Logout sin nuevo Login; Profile muestra la identidad de B. |
| | 7 | A: Cancel y Logout; S: página pública. |
| Extensiones | 2a | A: deja Remember Me desmarcada e inicia sesión con A; sigue 3–5 con A. |
| | 2a.1 | S (en 6): página pública con Login y Sign Up Free, sin Settings ni Logout. |

Postcondición: sesión de B cerrada; en 2a, perfil abierto sin sesión. Se registra el intervalo sin deducir política de expiración. **Derivación:** principal → **T09-14**; 2a → **T09-13**.

## 6. Lista resumida de casos

| Caso | Objetivo / riesgo | Fundamento | Importancia | TestLink |
|---|---|---|---|---|
| T09-01 Signup vacío | Omisiones y términos; Riesgo R6 | UC1 ext. 3a | medium | [TL-72](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-72) |
| T09-02 Signup duplicado | Conservar cuenta; Riesgo R5 | UC1 ext. 7a | high | [TL-73](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-73) |
| T09-03 Timezone | Selección correcta; Riesgo R6 | UC1 principal, parcial | medium | [TL-74](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-74) |
| T09-04 Login válido | Acceso a A; Riesgo R1 | UC2 principal | high | [TL-75](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-75) |
| T09-05 Login vacío | Sin credenciales; Riesgo R1 | UC2 ext. 3a | high | [TL-76](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-76) |
| T09-06 Email vacío | Sin identificador; Riesgo R1 | UC2 ext. 3b | high | [TL-77](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-77) |
| T09-07 Password vacío | Sin contraseña; Riesgo R1 | UC2 ext. 3c | high | [TL-78](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-78) |
| T09-08 Email mal formado | Respuesta no resuelta; Riesgos R1/R6 | UC2 ext. 3d, sin resultado | medium | Pendiente; excluido |
| T09-09 Cuenta inexistente | Sin cuenta; Riesgo R1 | UC2 ext. 3e | high | [TL-79](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-79) |
| T09-10 Contraseña incorrecta | Correspondencia falsa; Riesgo R1 | UC2 ext. 3f | high | [TL-80](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-80) |
| T09-11 Logout, Back y URL | Datos tras cierre; Riesgo R2 | UC3 principal | high | [TL-81](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-81) |
| T09-12 Aislamiento A/B | Evitar mezcla; Riesgo R3 | UC4 principal | high | [TL-82](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-82) |
| T09-13 Remember Me desmarcado | Sesión cerrada al reabrir; Riesgo R4 | UC5 ext. 2a | high | [TL-83](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-83) |
| T09-14 Remember Me marcado | Recuperar identidad; Riesgo R4 | UC5 principal | high | [TL-84](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-84) |

Los trece casos registrados y comparados no cambian; solo se reformula su fundamento.

Referencias anteriores en TestLink: las etiquetas de Login R1→UC2/3a (T09-05), R2→UC2/3b (06), R3→UC2/3c (07), R4→UC2/3e (09) y R5→UC2/3f (10) se conservan solo como correspondencia de lectura de las fichas existentes. Son distintas de los riesgos R1–R6; el fundamento vigente en este comentario son los casos de uso.
