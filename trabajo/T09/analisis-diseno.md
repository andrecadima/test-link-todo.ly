# T09 / PEB-73 — Registro, acceso y sesión

Fecha: 18 de noviembre de 2026. Trece casos registrados en TestLink y comparados individualmente; revisión independiente 06 APTO, sin bloqueantes y con observaciones resueltas. T09-08 permanece pendiente y excluido. Sin ejecución formal ni revisión de integrante.

## 1. Análisis del área

Se analizaron Signup, Login, Remember Me, Logout y el cambio entre dos cuentas gratuitas propias de la práctica. El entorno observado fue macOS 26.6.2 y Chrome 157.0.8103.51, con el perfil aislado Todo.ly QA cuenta B. El nombre del perfil no identifica la cuenta: la identidad se verificó desde Settings / Profile.

Signup muestra Full Name, Email, Password, Timezone, términos y el botón visible Signup (nombre accesible Submit). Se abre desde Sign Up Free. El envío completamente vacío y sin términos fue rechazado; el correo ya registrado también tuvo un rechazo específico. Timezone ofrece un valor predeterminado y una lista sin opción vacía visible; se identificó La Paz UTC-04 y su diferencia con la opción mexicana UTC-07. Esto no demuestra validación de servidor ante un Timezone vacío ni reglas de fechas.

Login aceptó credenciales vigentes y rechazó los contrastes legibles de campos vacíos, correo no registrado y contraseña incorrecta. El formato mal formado produjo vistas vacías que no permiten fijar su respuesta específica: T09-08 queda pendiente. Logout, Atrás y URL directa no mostraron los marcadores de la cuenta cerrada. El aislamiento se observó con un marcador de A y otro de B en sus respectivos Home, en ambos sentidos.

Remember Me tiene dos recorridos documentados: A desmarcado → cierre y reapertura asistida → landing sin sesión; B marcado → cierre y reapertura → sesión autenticada de B confirmada en Profile, sin un segundo Login. Chrome conservó otros perfiles abiertos; no se cerró todo el proceso ni se borraron cookies. El intervalo y los fallos de herramienta están anotados en registro de exploración.

No se incluyen pruebas de penetración, API, cuentas ajenas, funciones Pro ni efectos temporales de Timezone. La creación de tareas se usa exclusivamente para preparar marcadores de sesión/aislamiento; creación y edición funcional corresponden a T06.

## 2. Riesgos que orientan el diseño

Valoración cualitativa de diseño, no frecuencia medida: P baja=1/media=2/alta=3; I bajo=1/medio=2/alto=3; nivel P×I, alto=6–9, medio=3–4 y bajo=1–2.

| Riesgo | Consecuencia | P y fundamento | I | Nivel | Casos |
|---|---|---|---|---|---|
| R1: credenciales inválidas conceden acceso o las válidas fallan | Acceso incorrecto o pérdida de disponibilidad de la cuenta | 2: varias combinaciones y correspondencia con identidad | 3 | 6, alto | T09-04/05/06/07/09/10; T09-08 pendiente |
| R2: Logout o navegación posterior exponen información | Datos accesibles después del cierre solicitado | 2: historial, URL directa y estado de sesión | 3 | 6, alto | T09-11 |
| R3: datos de A aparecen en B o viceversa | Exposición o mezcla de información entre cuentas | 2: cambios de identidad con datos persistentes | 3 | 6, alto | T09-12 |
| R4: Remember Me conserva o pierde acceso de forma incoherente | Acceso persistente no solicitado o sesión recordada ausente | 2: opción, cierre de ventanas, reapertura y cookies | 3 | 6, alto | T09-13/14 |
| R5: registro duplicado sustituye una cuenta | Alteración del identificador, credencial o datos existentes | 2: coincidencia con correo ya registrado | 3 | 6, alto | T09-02 |
| R6: Signup no señala omisiones o ofrece una zona confusa | Registro incompleto o selección equivocada | 2: campos concurrentes y opciones con nombres semejantes | 2 | 4, medio | T09-01/03 |

## 3. Reglas, restricciones y dudas

| Regla o duda | Clasificación | Fundamento |
|---|---|---|
| Signup vacío y sin términos muestra `Error. Please correct the missing fields.`, asteriscos y aviso de términos | Comportamiento observado | Mensaje global leído por AX; la captura muestra asteriscos y aviso junto a términos. Combinación conjunta, no validaciones aisladas |
| Signup duplicado muestra `Error. Account with this email address already exists!` | Comportamiento observado | Registro intentado después de que el usuario hubiera creado la candidata anterior; no demuestra que fuera una cuenta preexistente a la práctica |
| El registro duplicado no sustituye la identidad ni los datos de la cuenta existente | Criterio del equipo | Riesgo de pérdida/alteración del identificador; el contraste posterior a ese intento se ejecutará en T09-02, no se presenta como ya observado |
| Timezone predeterminado Pacific UTC-08; lista observada de 101 opciones sin entrada vacía | Comportamiento observado | Listado completo consultado en Signup |
| La Paz de Bolivia corresponde a `(UTC-04:00) Georgetown, La Paz, Manaus, San Juan` | Comportamiento observado / decisión de preparación | Selector y decisión vigente §12; se excluyen efectos sobre vencimientos |
| Login válido abre la identidad correspondiente | Comportamiento observado | A y B verificadas desde Profile con las credenciales privadas actuales |
| Login con correo vacío/contraseña informada, A sin contraseña, A con contraseña incorrecta o correo no registrado no concede acceso | Comportamiento observado | Capturas y AX; se distingue el mensaje no retenido en ambos campos vacíos |
| Mensaje genérico legible de rechazo: `Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.` | Comportamiento observado | Respuestas conservadas de los contrastes anteriores |
| Existencia de una validación sintáctica independiente de Email en Login | Duda pendiente | Correo sin arroba produjo vista vacía; no se convierte en regla del producto |
| Logout conserva la sesión cerrada ante Atrás y URL raíz observada | Comportamiento observado | Secuencia con marcador A en Home |
| A y B conservan separados sus marcadores en Home | Comportamiento observado / criterio de independencia del equipo | Contrastes en ambos sentidos; PEB-67 y exploración propia |
| Sin Remember Me, la reapertura observada volvió a landing; con Remember Me, B reapareció autenticada | Comportamiento observado | Dos recorridos y capturas; cuenta y estado explícitos, sin extrapolar caducidad |
| Máximo tres intentos fallidos por cuenta durante la exploración | Criterio del equipo | Instrucción expresa del usuario; no es una política de bloqueo de Todo.ly |
| CAPTCHA, límites de intentos del producto, caducidad de sesión y longitudes de campos | Duda pendiente | No se comprobaron ni se deducen de los ejemplos de clase |
| Registro válido completo bajo control del agente | Duda pendiente de cobertura | Las cuentas iniciales fueron registradas por el usuario; su existencia y Login sí fueron comprobados |

### Fuentes cruzadas de controles y tratamiento de evidencias

Cancel de Settings y el nombre accesible Submit de Login fueron observados en T10 y en las consultas de identidad de A/B: fuente trabajo/T10/exploracion.md y captura de Old Password vacío. La nomenclatura visible de Signup y Sign Up Free fue verificada directamente en las capturas de exploración en las capturas registro-vacio y remember-off-reapertura-sin-sesion. Se adjuntarán como evidencia de registro únicamente el árbol y casos abiertos de TestLink con fichas genéricas; no capturas de exploración que muestren correos reales.

## 4. Tipos de prueba y escenarios

| Tipo | Objetivo y pertinencia | Procedimiento | Criterio observable |
|---|---|---|---|
| Funcional | Validaciones visibles y acceso a identidad correcta; R1, R5, R6 | Signup negativo, selección de campo, combinaciones de Login y consulta de Profile | Rechazo/aceptación según la regla confirmada; valor seleccionado e identidad correspondientes |
| Seguridad observable de sesión | Ausencia de datos tras Logout, independencia y persistencia solicitada; R2–R4 | Marcadores, cambio A/B, historial/URL y cierre/reapertura del mismo perfil | Datos disponibles solo para la identidad y estado de sesión previstos; sin interceptar tráfico ni consultar API |

Positivos: Login válido y recuperación de sesión recordada. Negativos: formulario vacío, correo duplicado y combinaciones de Login que no autentican. Alternativos: Logout seguido de historial/URL, cambio de identidad y reapertura con/sin Remember Me. No se incorpora rendimiento sin umbral ni compatibilidad Firefox/accesibilidad completa sin procedimiento explorado y objetivo justificable.

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

## 7. Implementación en TestLink

Se importaron **13 casos, 171 pasos nativos**, en proyecto TL:Todo.ly y suite existente **Todo.ly tests (id3)**, sin crear suites ni actualizar casos existentes. Filtro T09 antes: 0; total de suite antes: 70, después: 83. El importador omitía duplicados por nombre. IDs reales **TL-72 a TL-84**, disponibles en la lista resumida.

Se abrió cada caso y se compararon descripción, requerimiento, postcondiciones, precondiciones, todos los pasos/resultados, Importance y Manual: **435 textos comprobados, sin diferencias**. Estado TestLink Draft; no se presenta ejecución formal. Títulos y campos nativos corresponden a cada diseño. La evidencia adjunta muestra el árbol filtrado y TL-84 abierto; la lectura textual del árbol conserva todos los IDs aunque algunos nombres se recorten en la captura.

La revisión independiente 06 concluyó APTO; sus observaciones se resolvieron o documentaron. No sustituye la revisión de un integrante. Summary comienza por descripción y continúa con requerimiento/postcondiciones. Las fichas completas están en TestLink; las cuentas siguen genéricas. La exportación XML real y extracción por ticket se realizan en el cierre; el XML de entrada no se presenta como exportación.

## 8. Cobertura pendiente y límites

Pendientes: T09-08 y causa de sus vistas vacías; validaciones aisladas de Signup; registro válido completo observado bajo condiciones controladas; fronteras de campos; políticas de bloqueo/CAPTCHA y caducidad. No se necesita inventarlas para registrar los trece casos definidos. Las dos cuentas fueron creadas por el usuario para la práctica y su Login/estado inicial fueron verificados; no se confunde esa preparación con una ejecución formal del registro válido.

La preparación y los errores de lectura de correo Markdown, foco, captura y timeout pertenecen a la herramienta; no se reportan como defectos confirmados de Todo.ly. Las capturas con vista vacía o aviso ya desaparecido están diferenciadas en exploracion.md. Los marcadores actuales se conservan para limpieza al terminar los tres tickets, por instrucción del usuario.

## 9. Estado

**Diseñados y registrados en TestLink; pendiente de revisión por otro integrante.** Trece registrados y comparados; T09-08 excluido y dudas de §8 explícitas. Sin ejecución formal ni cambios de estado de Jira.

| Criterio de aceptación | Comprobación |
|---|---|
| Reglas y condiciones del registro/acceso | Documentadas con clasificación de fuente y dudas explícitas. |
| Tipos de prueba y riesgos | Funcional y seguridad observable, vinculados a riesgos R1–R6. |
| Escenarios positivos y negativos | Trece casos; formato mal formado y registro válido controlado pendientes explícitos. |
| Técnicas justificadas | Casos de uso con flujos principales, extensiones y trazabilidad; cobertura pendiente explícita y sin límites inventados. |
| Cuentas, sesiones y resultados | Fichas genéricas con estados y resultados observables. |
| Registro y revisión por otro integrante | Trece registrados y cotejados; revisión de integrante pendiente. |

## Fichas para TestLink — trece casos preparados

<!-- FICHAS_GENERADAS -->

### T09-01. Signup con campos vacíos y términos sin aceptar rechaza el envío

**Importancia:** **medium**. Detecta aceptación de un formulario sin los datos necesarios ni el consentimiento indicado.

**Requerimiento:** PEB-73 / T09. Signup informa las omisiones observadas y no concede acceso.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.

**Descripción:** Validar que Signup rechaza el envío con Full Name, Email y Password vacíos y la casilla de términos sin marcar, mostrando las señales de omisión observadas, sin aislar como reglas independientes las condiciones concurrentes.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en Chrome. | Se muestra la página pública de Todo.ly con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Sign Up Free**. | Se abre el formulario **Signup** con **Full Name**, **Email**, **Password**, **Timezone**, la casilla de términos y el botón **Signup** (nombre accesible Submit). |
| 3. Vaciar el campo **Full Name**. | **Full Name** queda vacío. |
| 4. Vaciar el campo **Email**. | **Email** queda vacío. |
| 5. Vaciar el campo **Password**. | **Password** queda vacío. |
| 6. Leer la selección inicial de **Timezone** sin cambiarla. | **Timezone** conserva su valor inicial del formulario. |
| 7. Dejar sin marcar la casilla de términos. | La casilla de términos está sin marcar. |
| 8. Hacer clic una vez en el botón **Signup**. | No se completa el registro; se muestran asteriscos junto a **Full Name**, **Email** y **Password** y el aviso **If you don’t agree you can’t use Todo.ly** junto a los términos sin marcar. Puede aparecer brevemente **Error. Please correct the missing fields.**, identificado por accesibilidad; no se exige ese aviso transitorio en la captura. |
| 9. Tomar una captura del formulario **Signup**. | La captura muestra los asteriscos y el aviso **If you don’t agree you can’t use Todo.ly**, sin datos personales. |
| 10. Abrir **https://todo.ly/** en la barra de direcciones, sin completar el registro. | Se muestra la página pública con **Login** y **Sign Up Free**; la sesión continúa cerrada y no aparece el área de proyectos de una cuenta. |

**Postcondiciones:** Sin cuenta nueva ni sesión; evidencia de la combinación vacía, sin atribuir obligatoriedad del servidor a Timezone.

---

### T09-02. Signup con el correo de una cuenta existente muestra error de duplicado

**Importancia:** **high**. Evita sustituir o confundir una cuenta al reutilizar su identificador.

**Requerimiento:** PEB-73 / T09. Signup rechaza un correo ya registrado sin sustituir la cuenta existente.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.
3. Cuenta gratuita de prueba (cuenta A) con correo y contraseña vigentes consignados en el registro privado de credenciales.
4. Contraseña de prueba para el intento de Signup, distinta de la vigente de A y consignada en el registro privado de credenciales.
5. Aceptación de los términos de Todo.ly autorizada para las cuentas de prueba.
6. Nombres de perfil de A consignados en el registro privado de referencia.

**Descripción:** Validar que Signup rechaza el correo de una cuenta de prueba ya registrada con el aviso de duplicado y que la cuenta A conserva su nombre original, usando exclusivamente una cuenta propia de prueba.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en Chrome. | Se muestra la página pública con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Sign Up Free**. | Se abre el formulario **Signup** con **Full Name**, **Email**, **Password**, **Timezone**, la casilla de términos y el botón **Signup**. |
| 3. Escribir **Prueba T09-02 - duplicado** en el campo **Full Name**. | **Full Name** muestra **Prueba T09-02 - duplicado**. |
| 4. Escribir en el campo **Email** el correo de la cuenta A, tomado del registro privado. | **Email** muestra el correo de la cuenta de prueba A existente. |
| 5. Escribir en el campo **Password** la contraseña de prueba para Signup del registro privado, distinta de la vigente de A. | **Password** contiene el valor introducido. |
| 6. Seleccionar **(UTC-04:00) Georgetown, La Paz, Manaus, San Juan** en **Timezone**. | **Timezone** muestra **(UTC-04:00) Georgetown, La Paz, Manaus, San Juan**. |
| 7. Marcar la casilla de términos del formulario **Signup**. | La casilla de términos queda marcada. |
| 8. Hacer clic una vez en el botón **Signup**. | Aparece **Error. Account with this email address already exists!**; no se inicia sesión en una cuenta nueva: no aparecen **Settings** ni **Logout**. |
| 9. Abrir **https://todo.ly/** en la barra de direcciones. | Se muestra la página pública con **Login** y **Sign Up Free**, sin sesión iniciada. |
| 10. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 11. Escribir en **Email** el correo de la cuenta A del registro privado. | **Email** muestra el correo de A. |
| 12. Escribir en **Password** la contraseña vigente de A del registro privado, la misma vigente antes del intento de Signup. | **Password** muestra el valor enmascarado. |
| 13. Hacer clic una vez en el botón **Login** del formulario (nombre accesible Submit). | Se muestra el área autenticada con **Settings** y **Logout**. |
| 14. Hacer clic en **Settings**. | Se abre **Settings**. |
| 15. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name** y **Email** de la cuenta con sesión iniciada. |
| 16. Comparar **Full Name** con el nombre de perfil de A del registro privado. | **Full Name** conserva el nombre inicial de A y no muestra **Prueba T09-02 - duplicado**, según el criterio del equipo de conservación de identidad. |
| 17. Comparar **Email** con el correo de A del registro privado. | **Email** coincide con el correo de A del registro privado. |

**Postcondiciones:** A conserva sus datos y credenciales; no se crea otra cuenta. Evidencia del rechazo sin contraseñas. Sesión iniciada en A, con **Profile** abierto.

---

### T09-03. Timezone de Signup ofrece La Paz UTC-04 y refleja la opción seleccionada

**Importancia:** **medium**. Evita confundir las opciones de La Paz y atribuir al campo reglas temporales fuera del alcance.

**Requerimiento:** PEB-73 / T09. Signup ofrece selección de zona y refleja la opción elegida en el formulario.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.

**Descripción:** Validar que el campo Timezone de Signup muestra su valor inicial, ofrece la opción de La Paz UTC-04 distinta de la opción mexicana UTC-07, sin una entrada vacía, y refleja la opción seleccionada, sin crear cuenta ni evaluar vencimientos.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en Chrome. | Se muestra la página pública con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Sign Up Free**. | Se abre el formulario **Signup** con el campo **Timezone**. |
| 3. Leer el valor inicial de **Timezone** sin desplegarlo. | El selector muestra la opción Pacific UTC-08; la captura de referencia deja visible **(UTC-08:00) Pacific Time (US & Cana…** con el texto recortado. |
| 4. Hacer clic en el selector **Timezone**. | Se despliega la lista de zonas horarias. |
| 5. Recorrer la lista completa de **Timezone**. | La lista no ofrece una entrada vacía. |
| 6. Anotar el número de opciones de **Timezone** en el registro de ejecución. | El inventario queda registrado; el inventario de referencia contiene 101 opciones, sin tratarlo como límite del producto. |
| 7. Localizar **(UTC-04:00) Georgetown, La Paz, Manaus, San Juan** en la lista. | Aparece la opción correspondiente a La Paz UTC-04. |
| 8. Localizar **(UTC-07:00) Chihuahua, La Paz, Mazatlan** en la lista. | La opción UTC-07 aparece como entrada distinta de La Paz UTC-04. |
| 9. Seleccionar **(UTC-04:00) Georgetown, La Paz, Manaus, San Juan**. | El selector **Timezone** muestra exactamente **(UTC-04:00) Georgetown, La Paz, Manaus, San Juan**. |
| 10. Abrir **https://todo.ly/** en la barra de direcciones, sin hacer clic en **Signup**. | Se muestra la página pública sin registro completado ni sesión iniciada. |

**Postcondiciones:** Formulario descartado sin registro. No se concluye validación de servidor para un Timezone vacío que la interfaz no permite seleccionar.

---

### T09-04. Login con credenciales vigentes de A abre la sesión de la cuenta A

**Importancia:** **high**. Protege la operación esencial de acceso a la cuenta correcta.

**Requerimiento:** PEB-73 / T09. Credenciales vigentes que corresponden a una cuenta permiten acceso a esa identidad.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.
3. Cuenta gratuita de prueba (cuenta A) con correo y contraseña vigentes consignados en el registro privado de credenciales.
4. Nombres de perfil de A consignados en el registro privado de referencia.

**Descripción:** Validar que Login con el correo y la contraseña vigentes de A concede acceso a la identidad de A, comprobada en Profile.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en Chrome. | Se muestra la página pública con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 3. Escribir en **Email** el correo de la cuenta A del registro privado. | **Email** muestra el correo de A. |
| 4. Escribir en **Password** la contraseña vigente de A del registro privado. | **Password** muestra el valor enmascarado. |
| 5. Dejar desmarcada la casilla **Remember Me**; si aparece marcada, hacer clic en ella una vez. | **Remember Me** está desmarcada. |
| 6. Hacer clic una vez en el botón **Login** del formulario (nombre accesible Submit). | Se muestra el área autenticada con **Settings** y **Logout**. |
| 7. Hacer clic en **Settings**. | Se abre **Settings**. |
| 8. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name** y **Email** de la cuenta con sesión iniciada. |
| 9. Comparar **Full Name** con el nombre de perfil de A del registro privado. | **Full Name** coincide con el nombre de A. |
| 10. Comparar **Email** con el correo de A del registro privado. | **Email** coincide con el correo de A del registro privado. |
| 11. Hacer clic en **Cancel**. | Se cierra **Settings** sin guardar cambios y vuelve a verse el área de proyectos. |
| 12. Hacer clic en **Logout**. | Se muestra la página pública con **Login** y **Sign Up Free**, con la sesión cerrada. |

**Postcondiciones:** Sesión cerrada y datos de A sin cambios; evidencia de identidad sin secretos.

---

### T09-05. Login con Email y Password vacíos no concede acceso

**Importancia:** **high**. Evita acceso sin una combinación de credenciales que corresponda a la cuenta.

**Requerimiento:** PEB-73 / T09. La combinación negativa R1 de la tabla de decisión no concede acceso.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.

**Descripción:** Validar que Login con Email y Password vacíos no concede acceso, en un único intento negativo.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en Chrome. | Se muestra la página pública con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 3. Revisar los campos sin escribir datos y sin cambiar la casilla **Remember Me**. | **Email** y **Password** están vacíos. |
| 4. Hacer clic una sola vez en el botón **Login** del formulario (nombre accesible Submit). | No se concede acceso: el formulario de acceso con **Login** sigue disponible y no aparecen **Settings**, **Logout** ni datos de proyectos. |
| 5. Tomar una captura de la pantalla resultante. | La captura muestra el formulario de acceso sin sesión iniciada. |
| 6. Abrir **https://todo.ly/** en la barra de direcciones, sin escribir credenciales. | Se muestra la página pública; la sesión sigue cerrada y no se exponen datos de A o B. |

**Postcondiciones:** Sin sesión ni cambios de cuenta. Un único intento negativo de esta ficha; evidencias sin contraseña legible.

---

### T09-06. Login con Email vacío y Password informado muestra error y no da acceso

**Importancia:** **high**. Evita acceso sin una combinación de credenciales que corresponda a la cuenta.

**Requerimiento:** PEB-73 / T09. La combinación negativa R2 de la tabla de decisión no concede acceso.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.

**Descripción:** Validar que Login con Email vacío y un Password de prueba no concede acceso y muestra el aviso genérico de credenciales incorrectas, en un único intento negativo.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en Chrome. | Se muestra la página pública con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 3. Revisar el campo **Email** sin escribir datos y sin cambiar la casilla **Remember Me**. | **Email** está vacío. |
| 4. Escribir **Prueba-T09-no-valida-17** en el campo **Password**. | **Password** muestra el valor enmascarado. |
| 5. Hacer clic una sola vez en el botón **Login** del formulario (nombre accesible Submit). | No se concede acceso y se muestra **Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.** |
| 6. Tomar una captura del aviso y del formulario. | La captura muestra el aviso y el formulario de acceso, sin contraseña legible. |
| 7. Abrir **https://todo.ly/** en la barra de direcciones, sin escribir credenciales. | Se muestra la página pública; la sesión sigue cerrada y no se exponen datos de A o B. |

**Postcondiciones:** Sin sesión ni cambios de cuenta. Un único intento negativo de esta ficha; evidencias sin contraseña legible.

---

### T09-07. Login de A con Password vacío muestra error y no concede acceso

**Importancia:** **high**. Evita acceso sin una combinación de credenciales que corresponda a la cuenta.

**Requerimiento:** PEB-73 / T09. La combinación negativa R3 de la tabla de decisión no concede acceso.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.
3. Cuenta gratuita de prueba (cuenta A) con correo y contraseña vigentes consignados en el registro privado de credenciales.
4. Cuenta A con menos de tres intentos fallidos de Login en la sesión de trabajo, según criterio operativo del equipo (no es una política de Todo.ly).
5. Contraseña vigente de A distinta de **Prueba-T09-no-valida-17**.

**Descripción:** Validar que Login con el correo de A y Password vacío no concede acceso y muestra el aviso genérico de credenciales incorrectas, en un único intento negativo.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en Chrome. | Se muestra la página pública con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 3. Escribir en **Email** el correo de la cuenta A del registro privado, sin cambiar la casilla **Remember Me**. | **Email** muestra el correo de A. |
| 4. Revisar el campo **Password** sin escribir datos. | **Password** está vacío. |
| 5. Hacer clic una sola vez en el botón **Login** del formulario (nombre accesible Submit). | No se concede acceso y se muestra **Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.** |
| 6. Tomar una captura del aviso y del formulario. | La captura muestra el aviso y el formulario de acceso, sin contraseña legible. |
| 7. Abrir **https://todo.ly/** en la barra de direcciones, sin escribir credenciales. | Se muestra la página pública; la sesión sigue cerrada y no se exponen datos de A o B. |

**Postcondiciones:** Sin sesión ni cambios de cuenta. Un único intento negativo de esta ficha; evidencias sin contraseña legible.

---

### T09-09. Login con un correo no registrado muestra error y no concede acceso

**Importancia:** **high**. Evita acceso sin una combinación de credenciales que corresponda a la cuenta.

**Requerimiento:** PEB-73 / T09. La combinación negativa R4 de la tabla de decisión no concede acceso.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.
3. Dirección reservada **prueba-t10-no-registrada-20261117@example.com** sin cuenta asociada en Todo.ly, según el contraste de recuperación de PEB-74 / T10.

**Descripción:** Validar que Login con un correo sin cuenta asociada y un Password de prueba no concede acceso y muestra el aviso genérico de credenciales incorrectas, en un único intento negativo.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en Chrome. | Se muestra la página pública con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 3. Escribir **prueba-t10-no-registrada-20261117@example.com** en el campo **Email**, sin cambiar la casilla **Remember Me**. | **Email** muestra **prueba-t10-no-registrada-20261117@example.com**. |
| 4. Escribir **Prueba-T09-no-valida-17** en el campo **Password**. | **Password** muestra el valor enmascarado. |
| 5. Hacer clic una sola vez en el botón **Login** del formulario (nombre accesible Submit). | No se concede acceso y se muestra **Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.** |
| 6. Tomar una captura del aviso y del formulario. | La captura muestra el aviso y el formulario de acceso, sin contraseña legible. |
| 7. Abrir **https://todo.ly/** en la barra de direcciones, sin escribir credenciales. | Se muestra la página pública; la sesión sigue cerrada y no se exponen datos de A o B. |

**Postcondiciones:** Sin sesión ni cambios de cuenta. Un único intento negativo de esta ficha; evidencias sin contraseña legible.

---

### T09-10. Login de A con contraseña incorrecta muestra error y no concede acceso

**Importancia:** **high**. Evita acceso sin una combinación de credenciales que corresponda a la cuenta.

**Requerimiento:** PEB-73 / T09. La combinación negativa R5 de la tabla de decisión no concede acceso.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.
3. Cuenta gratuita de prueba (cuenta A) con correo y contraseña vigentes consignados en el registro privado de credenciales.
4. Cuenta A con menos de tres intentos fallidos de Login en la sesión de trabajo, según criterio operativo del equipo (no es una política de Todo.ly).
5. Contraseña vigente de A distinta de **Prueba-T09-no-valida-17**.

**Descripción:** Validar que Login con el correo de A y una contraseña que no le corresponde no concede acceso y muestra el aviso genérico de credenciales incorrectas, en un único intento negativo.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en Chrome. | Se muestra la página pública con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 3. Escribir en **Email** el correo de la cuenta A del registro privado, sin cambiar la casilla **Remember Me**. | **Email** muestra el correo de A. |
| 4. Escribir **Prueba-T09-no-valida-17** en el campo **Password**. | **Password** muestra el valor enmascarado. |
| 5. Hacer clic una sola vez en el botón **Login** del formulario (nombre accesible Submit). | No se concede acceso y se muestra **Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.** |
| 6. Tomar una captura del aviso y del formulario. | La captura muestra el aviso y el formulario de acceso, sin contraseña legible. |
| 7. Abrir **https://todo.ly/** en la barra de direcciones, sin escribir credenciales. | Se muestra la página pública; la sesión sigue cerrada y no se exponen datos de A o B. |

**Postcondiciones:** Sin sesión ni cambios de cuenta. Un único intento negativo de esta ficha; evidencias sin contraseña legible.

---

### T09-11. Logout impide ver los datos de A con Atrás y con la URL directa

**Importancia:** **high**. Detecta exposición de datos después de Logout por historial o navegación directa.

**Requerimiento:** PEB-73 / T09. Logout deja sin acceso autenticado el historial y la URL previamente observada.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Cuenta gratuita de prueba (cuenta A) con correo y contraseña vigentes consignados en el registro privado de credenciales.
3. Sesión iniciada en Todo.ly con la cuenta A, en **https://todo.ly/**.
4. Proyecto **Home** de A sin una tarea llamada **Prueba T09-11 - sesión**.

**Descripción:** Validar que, después de Logout, ni el botón Atrás de Chrome ni la URL directa https://todo.ly/ restablecen la sesión ni muestran un marcador propio de A creado como preparación.

| Paso | Resultado esperado |
|---|---|
| 1. Hacer clic en **Home** en el panel izquierdo. | Se muestra la lista de **Home** de A, sin **Prueba T09-11 - sesión**. |
| 2. Escribir **Prueba T09-11 - sesión** en el campo **Add new Todo**. | El campo **Add new Todo** muestra **Prueba T09-11 - sesión**. |
| 3. Hacer clic en **Add**. | **Prueba T09-11 - sesión** aparece como tarea pendiente en **Home** de A. |
| 4. Hacer clic en **Logout**. | Se muestra la página pública con **Login** y **Sign Up Free**; el marcador ya no se muestra como dato autenticado. |
| 5. Hacer clic una vez en el botón **Back** (Atrás) de Chrome. | No se restablece una sesión autenticada ni se muestra **Prueba T09-11 - sesión**. |
| 6. Abrir **https://todo.ly/** en la barra de direcciones, sin hacer **Login**. | Se muestra la página pública con **Login**; no se muestra **Prueba T09-11 - sesión**. |
| 7. Tomar una captura del estado posterior a las dos navegaciones. | La captura permite reconocer la ausencia de acceso autenticado, sin secretos. |

**Postcondiciones:** Sesión cerrada. El marcador permanece en Home de A para la limpieza del lote; datos previos conservados. No se afirma protección de API ni de rutas que no se hayan observado.

---

### T09-12. Cambio de cuenta entre A y B muestra solo los datos propios de cada una

**Importancia:** **high**. Evita exposición o mezcla de información entre dos cuentas sin proyectos compartidos.

**Requerimiento:** PEB-73 / T09. Cada cuenta muestra sus propios datos de Home después de cambiar de identidad.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.
3. Dos cuentas gratuitas de prueba sin proyectos compartidos (A y B), con correos y contraseñas vigentes consignados en el registro privado de credenciales y proyecto **Home** disponible en cada una.
4. **Home** de A sin una tarea llamada **Prueba T09-12 - marcador A**; **Home** de B sin una tarea llamada **Prueba T09-12 - marcador B**.
5. Nombres de perfil de A y B consignados en el registro privado de referencia.

**Descripción:** Validar que, al alternar la sesión entre A y B, cada cuenta muestra en Home su propio marcador y no el de la otra, en ambos sentidos.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en Chrome. | Se muestra la página pública con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 3. Escribir en **Email** el correo de la cuenta A del registro privado. | **Email** muestra el correo de A. |
| 4. Escribir en **Password** la contraseña vigente de A del registro privado. | **Password** muestra el valor enmascarado. |
| 5. Hacer clic una vez en el botón **Login** del formulario (nombre accesible Submit). | Se muestra el área autenticada con **Settings** y **Logout**. |
| 6. Hacer clic en **Settings**. | Se abre **Settings**. |
| 7. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name** y **Email** de la cuenta con sesión iniciada. |
| 8. Comparar **Full Name** con el nombre de perfil de A del registro privado. | **Full Name** coincide con el nombre de A. |
| 9. Comparar **Email** con el correo de A del registro privado. | **Email** coincide con el correo de A del registro privado. |
| 10. Hacer clic en **Cancel**. | Se cierra **Settings** sin guardar cambios y vuelve a verse el área de proyectos. |
| 11. Hacer clic en **Home** en el panel izquierdo. | Se muestra la lista de **Home** de A, sin **Prueba T09-12 - marcador A** ni **Prueba T09-12 - marcador B**. |
| 12. Escribir **Prueba T09-12 - marcador A** en el campo **Add new Todo**. | El campo **Add new Todo** muestra **Prueba T09-12 - marcador A**. |
| 13. Hacer clic en **Add**. | **Prueba T09-12 - marcador A** aparece como tarea pendiente en **Home** de A. |
| 14. Hacer clic en **Logout**. | Se muestra la página pública con **Login** y **Sign Up Free**; la sesión de A queda cerrada. |
| 15. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso. |
| 16. Escribir en **Email** el correo de la cuenta B del registro privado. | **Email** muestra el correo de B. |
| 17. Escribir en **Password** la contraseña vigente de B del registro privado. | **Password** muestra el valor enmascarado. |
| 18. Hacer clic una vez en el botón **Login** del formulario (nombre accesible Submit). | Se muestra el área autenticada con **Settings** y **Logout**. |
| 19. Hacer clic en **Settings**. | Se abre **Settings**. |
| 20. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name** y **Email** de la cuenta con sesión iniciada. |
| 21. Comparar **Full Name** con el nombre de perfil de B del registro privado. | **Full Name** coincide con el nombre de B. |
| 22. Comparar **Email** con el correo de B del registro privado. | **Email** coincide con el correo de B del registro privado. |
| 23. Hacer clic en **Cancel**. | Se cierra **Settings** sin guardar cambios y vuelve a verse el área de proyectos. |
| 24. Hacer clic en **Home** en el panel izquierdo. | Se muestra la lista de **Home** de B; no aparece **Prueba T09-12 - marcador A**. |
| 25. Escribir **Prueba T09-12 - marcador B** en el campo **Add new Todo**. | El campo **Add new Todo** muestra **Prueba T09-12 - marcador B**. |
| 26. Hacer clic en **Add**. | **Prueba T09-12 - marcador B** aparece como tarea pendiente en **Home** de B. |
| 27. Hacer clic en **Logout**. | Se muestra la página pública con **Login** y **Sign Up Free**; la sesión de B queda cerrada. |
| 28. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso. |
| 29. Escribir en **Email** el correo de la cuenta A del registro privado. | **Email** muestra el correo de A. |
| 30. Escribir en **Password** la contraseña vigente de A del registro privado. | **Password** muestra el valor enmascarado. |
| 31. Hacer clic una vez en el botón **Login** del formulario (nombre accesible Submit). | Se muestra el área autenticada con **Settings** y **Logout**. |
| 32. Hacer clic en **Home** en el panel izquierdo. | **Home** de A muestra **Prueba T09-12 - marcador A** y no muestra **Prueba T09-12 - marcador B**. |
| 33. Tomar una captura de **Home** de A. | La captura muestra el marcador de A sin el de B, sin secretos. |
| 34. Hacer clic en **Logout**. | Se muestra la página pública con **Login** y **Sign Up Free**; la sesión de A queda cerrada. |
| 35. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso. |
| 36. Escribir en **Email** el correo de la cuenta B del registro privado. | **Email** muestra el correo de B. |
| 37. Escribir en **Password** la contraseña vigente de B del registro privado. | **Password** muestra el valor enmascarado. |
| 38. Hacer clic una vez en el botón **Login** del formulario (nombre accesible Submit). | Se muestra el área autenticada con **Settings** y **Logout**. |
| 39. Hacer clic en **Home** en el panel izquierdo. | **Home** de B muestra **Prueba T09-12 - marcador B** y no muestra **Prueba T09-12 - marcador A**. |
| 40. Tomar una captura de **Home** de B. | La captura muestra el marcador de B sin el de A, sin secretos. |
| 41. Hacer clic en **Logout**. | Se muestra la página pública con **Login** y **Sign Up Free**; la sesión queda cerrada y los marcadores siguen separados por cuenta. |

**Postcondiciones:** Marcadores propios en Home de sus cuentas, pendientes de la limpieza del lote; sin proyectos compartidos ni cambios a datos de otras personas.

---

### T09-13. Remember Me desmarcado: al reabrir el perfil la sesión de A queda cerrada

**Importancia:** **high**. Detecta permanencia de acceso no solicitada al reabrir el perfil de QA.

**Requerimiento:** PEB-73 / T09. El recorrido observado sin Remember Me vuelve a la página pública al reabrir.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.
3. Cuenta gratuita de prueba (cuenta A) con correo y contraseña vigentes consignados en el registro privado de credenciales.
4. Perfil dedicado de Chrome para QA, sin otras ventanas abiertas de ese perfil y disponible en el selector de perfiles de Chrome para su reapertura.
5. Configuración de Chrome sin cambios durante todo el recorrido.
6. Nombres de perfil de A consignados en el registro privado de referencia.
7. Otra ventana de Chrome de un perfil distinto abierta durante todo el recorrido.

**Descripción:** Validar que, tras Login de A con Remember Me desmarcado y el cierre de las ventanas del perfil dedicado, la reapertura de ese perfil muestra la página pública sin sesión, registrando el intervalo y sin inferir una caducidad de cookies.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en una ventana del perfil dedicado de Chrome. | Se muestra la página pública con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 3. Dejar desmarcada la casilla **Remember Me**; si aparece marcada, hacer clic en ella una vez. | **Remember Me** está desmarcada. |
| 4. Tomar una captura de la casilla **Remember Me** antes del envío. | La captura muestra **Remember Me** desmarcada. |
| 5. Escribir en **Email** el correo de la cuenta A del registro privado. | **Email** muestra el correo de A. |
| 6. Escribir en **Password** la contraseña vigente de A del registro privado. | **Password** muestra el valor enmascarado. |
| 7. Hacer clic una vez en el botón **Login** del formulario (nombre accesible Submit). | Se inicia sesión: se muestra el área autenticada con **Settings** y **Logout**. |
| 8. Hacer clic en **Settings**. | Se abre **Settings**. |
| 9. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name** y **Email** de la cuenta con sesión iniciada. |
| 10. Comparar **Full Name** con el nombre de perfil de A del registro privado. | **Full Name** coincide con el nombre de A. |
| 11. Comparar **Email** con el correo de A del registro privado. | **Email** coincide con el correo de A del registro privado. |
| 12. Anotar la hora actual como hora de cierre. | La hora de cierre queda registrada. |
| 13. Cerrar todas las ventanas del perfil dedicado con su botón de cierre, sin hacer clic en **Logout**, sin borrar cookies y sin cerrar otros perfiles. | Las ventanas del perfil dedicado quedan cerradas; los demás perfiles de Chrome conservan sus ventanas y sesiones. |
| 14. Abrir de nuevo el mismo perfil dedicado desde el selector de perfiles de Chrome (menú **Profiles** en macOS). | Se abre una ventana nueva del perfil dedicado. |
| 15. Anotar la hora actual como hora de reapertura. | Queda registrado el intervalo entre el cierre y la reapertura. |
| 16. Abrir **https://todo.ly/** en la barra de direcciones, sin escribir credenciales. | Se muestra la página pública con **Login** y **Sign Up Free**, sin **Settings** ni **Logout**, conforme al recorrido observado. |
| 17. Tomar una captura que muestre el nombre del perfil dedicado y el estado de Todo.ly. | La captura identifica el perfil reabierto y la página pública sin sesión; no se usa otro perfil como prueba. |

**Postcondiciones:** Perfil QA abierto con sesión cerrada, datos y credenciales sin cambios; intervalo y cualquier ayuda manual documentados.

---

### T09-14. Remember Me marcado: al reabrir el perfil se restaura la sesión de B

**Importancia:** **high**. Comprueba recuperación de la sesión solicitada sin confundirla con un nuevo Login.

**Requerimiento:** PEB-73 / T09. El recorrido observado con Remember Me conserva la identidad autenticada al reabrir.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.
3. Cuenta gratuita de prueba (cuenta B) con correo y contraseña vigentes consignados en el registro privado de credenciales.
4. Perfil dedicado de Chrome para QA, sin otras ventanas abiertas de ese perfil y disponible en el selector de perfiles de Chrome para su reapertura.
5. Configuración de Chrome sin cambios durante todo el recorrido.
6. Nombres de perfil de B consignados en el registro privado de referencia.
7. Otra ventana de Chrome de un perfil distinto abierta durante todo el recorrido.

**Descripción:** Validar que, tras Login de B con Remember Me marcado y el cierre de las ventanas del perfil dedicado, la reapertura de ese perfil muestra la sesión autenticada de B sin un nuevo Login, cerrando después la sesión.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en una ventana del perfil dedicado de Chrome. | Se muestra la página pública con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 3. Dejar marcada la casilla **Remember Me**; si aparece desmarcada, hacer clic en ella una vez. | **Remember Me** está marcada. |
| 4. Tomar una captura de la casilla **Remember Me** antes del envío. | La captura muestra **Remember Me** marcada. |
| 5. Escribir en **Email** el correo de la cuenta B del registro privado. | **Email** muestra el correo de B. |
| 6. Escribir en **Password** la contraseña vigente de B del registro privado. | **Password** muestra el valor enmascarado. |
| 7. Hacer clic una vez en el botón **Login** del formulario (nombre accesible Submit). | Se inicia sesión: se muestra el área autenticada con **Settings** y **Logout**. |
| 8. Hacer clic en **Settings**. | Se abre **Settings**. |
| 9. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name** y **Email** de la cuenta con sesión iniciada. |
| 10. Comparar **Full Name** con el nombre de perfil de B del registro privado. | **Full Name** coincide con el nombre de B. |
| 11. Comparar **Email** con el correo de B del registro privado. | **Email** coincide con el correo de B del registro privado. |
| 12. Anotar la hora actual como hora de cierre. | La hora de cierre queda registrada. |
| 13. Cerrar todas las ventanas del perfil dedicado con su botón de cierre, sin hacer clic en **Logout**, sin borrar cookies y sin cerrar otros perfiles. | Las ventanas del perfil dedicado quedan cerradas; los demás perfiles de Chrome conservan sus ventanas y sesiones. |
| 14. Abrir de nuevo el mismo perfil dedicado desde el selector de perfiles de Chrome (menú **Profiles** en macOS). | Se abre una ventana nueva del perfil dedicado. |
| 15. Anotar la hora actual como hora de reapertura. | Queda registrado el intervalo entre el cierre y la reapertura. |
| 16. Abrir **https://todo.ly/** en la barra de direcciones, sin escribir credenciales. | Se muestra el área autenticada con **Settings** y **Logout**, sin un nuevo envío de **Login**. |
| 17. Hacer clic en **Settings**. | Se abre **Settings**. |
| 18. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name** y **Email** de la cuenta con sesión restaurada. |
| 19. Comparar **Full Name** con el nombre de perfil de B del registro privado. | **Full Name** coincide con el nombre de B. |
| 20. Comparar **Email** con el correo de B del registro privado. | **Email** coincide con el correo de B del registro privado. |
| 21. Tomar una captura del área autenticada restaurada. | La captura muestra el perfil dedicado con la sesión autenticada, sin contraseñas. |
| 22. Hacer clic en **Cancel**. | Se cierra **Settings** sin guardar cambios y vuelve a verse el área de proyectos. |
| 23. Hacer clic en **Logout**. | Se muestra la página pública con **Login** y **Sign Up Free**; la sesión queda cerrada. |

**Postcondiciones:** Sesión de B cerrada después de conservar evidencia; datos y credenciales sin cambios. El recorrido no prueba una caducidad ni el cierre completo del proceso Chrome.

---

## Candidatos pendientes — no registrar todavía

---

### T09-08. Login con Email sin formato de correo: respuesta pendiente de confirmar

**Importancia:** **medium**. Identifica una entrada negativa cuya respuesta visible todavía no está resuelta.

**Requerimiento:** PEB-73 / T09. Tratamiento del Email mal formado, pendiente de fijar resultado visible.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sin sesión iniciada en Todo.ly en el navegador.

**Descripción:** Validar que la respuesta de Login ante un Email sin formato de correo queda identificada antes de registrar el caso, sin fijar todavía un resultado esperado, porque las vistas vacías observadas impiden atribuirle una regla de validación; candidato pendiente, no registrar como caso listo.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir **https://todo.ly/** en Chrome. | Se muestra la página pública con **Login** y **Sign Up Free**. |
| 2. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 3. Escribir **PruebaT09SinArroba** en el campo **Email**. | **Email** muestra **PruebaT09SinArroba**, sin datos de una cuenta ajena. |
| 4. Escribir **Prueba-T09-no-valida-17** en el campo **Password**. | **Password** muestra el valor enmascarado. |
| 5. Hacer clic una sola vez en el botón **Login** del formulario (nombre accesible Submit). | PENDIENTE: confirmar el tratamiento visible y el mensaje. La página vacía de la herramienta no demuestra una regla de validación del producto. |
| 6. Abrir **https://todo.ly/** en la barra de direcciones, sin escribir credenciales, y anotar el estado mostrado. | Se documenta si aparece la página pública o una sesión autenticada; no se atribuye el resultado a una regla sintáctica sin confirmarla. |

**Postcondiciones:** Candidato fuera del registro propuesto; sin cambios de credencial y con la causa de la vista vacía pendiente.
