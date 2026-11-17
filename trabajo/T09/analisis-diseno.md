# T09 / PEB-73 — Registro, acceso y sesión

Fecha: 17 de noviembre de 2026. **Diseño preparado para revisión: trece casos listos y un candidato pendiente de exploración, fuera del registro propuesto.** No registrado en TestLink, no publicado en Jira y no ejecutado formalmente. Fuentes de fichas: `casos-listos.json` y `casos-pendientes.json`; `casos.json` conserva el conjunto completo. Se mantienen los códigos para trazabilidad aunque T09-08 quede reservado.

## 1. Análisis del área

Se analizaron Signup, Login, Remember Me, Logout y el cambio entre dos cuentas gratuitas propias de la práctica. El entorno observado fue macOS 26.6.2 y Chrome 157.0.8103.51, con el perfil aislado Todo.ly QA cuenta B. El nombre del perfil no identifica la cuenta: la identidad se verificó desde Settings / Profile.

Signup muestra Full Name, Email, Password, Timezone, términos y Submit. El envío completamente vacío y sin términos fue rechazado; el correo ya registrado también tuvo un rechazo específico. Timezone ofrece un valor predeterminado y una lista sin opción vacía visible; se identificó La Paz UTC-04 y su diferencia con la opción mexicana UTC-07. Esto no demuestra validación de servidor ante un Timezone vacío ni reglas de fechas.

Login aceptó credenciales vigentes y rechazó los contrastes legibles de campos vacíos, correo no registrado y contraseña incorrecta. El formato mal formado produjo vistas vacías que no permiten fijar su respuesta específica: T09-08 queda pendiente. Logout, Atrás y URL directa no mostraron los marcadores de la cuenta cerrada. El aislamiento se observó con un marcador de A y otro de B en sus respectivos Home, en ambos sentidos.

Remember Me tiene dos recorridos documentados: A desmarcado → cierre y reapertura asistida → landing sin sesión; B marcado → cierre y reapertura → sesión autenticada de B confirmada en Profile, sin un segundo Login. Chrome conservó otros perfiles abiertos; no se cerró todo el proceso ni se borraron cookies. El intervalo y los fallos de herramienta están anotados en `exploracion.md`.

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
| Signup vacío y sin términos muestra `Error. Please correct the missing fields.`, asteriscos y aviso de términos | Comportamiento observado | Captura y AX del 16/11. Es una combinación conjunta, no validaciones aisladas de cada campo |
| Signup duplicado muestra `Error. Account with this email address already exists!` | Comportamiento observado | Registro intentado después de que el usuario hubiera creado la candidata anterior; no demuestra que fuera una cuenta preexistente a la práctica |
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

## 4. Tipos de prueba y escenarios

| Tipo | Objetivo y pertinencia | Procedimiento | Criterio observable |
|---|---|---|---|
| Funcional | Validaciones visibles y acceso a identidad correcta; R1, R5, R6 | Signup negativo, selección de campo, combinaciones de Login y consulta de Profile | Rechazo/aceptación según la regla confirmada; valor seleccionado e identidad correspondientes |
| Seguridad observable de sesión | Ausencia de datos tras Logout, independencia y persistencia solicitada; R2–R4 | Marcadores, cambio A/B, historial/URL y cierre/reapertura del mismo perfil | Datos disponibles solo para la identidad y estado de sesión previstos; sin interceptar tráfico ni consultar API |

Positivos: Login válido y recuperación de sesión recordada. Negativos: formulario vacío, correo duplicado y combinaciones de Login que no autentican. Alternativos: Logout seguido de historial/URL, cambio de identidad y reapertura con/sin Remember Me. No se incorpora rendimiento sin umbral ni compatibilidad Firefox/accesibilidad completa sin procedimiento explorado y objetivo justificable.

## 5. Técnicas y artefactos

Definiciones ya recuperadas del original `E Tecnicas de Black Box Testing 2025.pdf`: particiones pp. 8–19, estados pp. 32–43, decisión pp. 45–56 y casos de uso pp. 58–66. No se releyó el PDF completo.

### 5.1 Particiones de equivalencia

| Variable / condición | Clase y tratamiento esperado | Representante | Casos |
|---|---|---|---|
| Conjunto de Signup | Campos vacíos y términos sin aceptar: rechazo conjunto | Full Name/Email/Password vacíos y casilla desmarcada | T09-01 |
| Correo de Signup | Correo ya registrado: rechazo de duplicado | Correo de la cuenta de prueba A | T09-02 |
| Opciones de Timezone | Valores del conjunto ofrecido: selección reflejada | Opción La Paz UTC-04 | T09-03; no se fabrica una opción vacía |
| Presencia de datos en Login | Email/Password ausentes: no autentica | Ambos vacíos, Email vacío o Password vacío | T09-05/06/07; reglas R1–R3 |
| Identificador conocido no registrado | No identifica una cuenta: no autentica | Correo reservado contrastado por recuperación | T09-09; R4 |
| Correspondencia de Password con la cuenta | No coincide: rechazo / coincide: acceso a esa identidad | Valor de prueba distinto / clave vigente privada | T09-10 / T09-04; R5/R6 |

No se usa el texto sin arroba para afirmar existencia o inexistencia de una cuenta, ni para atribuir un validador sintáctico no confirmado. T09-08 conserva ese contraste como candidato pendiente, fuera de la tabla de reglas confirmadas.

### 5.2 Tabla de decisión de Login

Formato docente: condiciones arriba, acciones abajo y columnas como reglas. `T` verdadero, `F` falso, `X` irrelevante para resolver la regla; `Execute` indica acción esperada. La tabla se reduce por ausencia de un dato necesario: no se necesitan las condiciones de correspondencia cuando faltan campos; una contraseña no tiene correspondencia sin cuenta identificada. X no significa una combinación imposible.

| Condiciones / acciones | R1 | R2 | R3 | R4 | R5 | R6 |
|---|---|---|---|---|---|---|
| Email informado | F | F | T | T | T | T |
| Password informado | F | T | F | T | T | T |
| Email identifica una cuenta existente | X | X | X | F | T | T |
| Password corresponde a esa cuenta | X | X | X | X | F | T |
| **Conceder acceso a la identidad** | — | — | — | — | — | Execute |
| **Mantener sesión cerrada** | Execute | Execute | Execute | Execute | Execute | — |
| **Caso derivado** | T09-05 | T09-06 | T09-07 | T09-09 | T09-10 | T09-04 |

El presupuesto de intentos es una restricción de la exploración; no se deriva de esta tabla un número de intentos que bloquee al producto. Los casos con datos de A se distribuyen respetando el presupuesto.

### 5.3 Transición de estados

Estados: **S0** sesión cerrada/perfil abierto; **S1** autenticada con Remember Me desmarcado; **S2** autenticada con Remember Me marcado; **C1** ventanas del perfil cerradas tras S1; **C2** ventanas cerradas tras S2. El navegador puede mantener otros perfiles y su proceso abiertos. Los estados C1/C2 conservan el antecedente que distingue la reapertura.

Matriz docente: filas estado actual, columnas evento, celdas estado siguiente. `—` evento no ejercitado en ese estado; no representa por sí solo una restricción del producto. Reaperturas: S1/C1 observadas con A; S2/C2 con B.

| Estado actual | Login válido sin recordar | Login válido recordando | Login inválido | Logout | Cerrar ventanas QA | Reabrir QA y consultar URL | Atrás / URL tras Logout |
|---|---|---|---|---|---|---|---|
| S0 | S1 | S2 | S0 | — | — | — | S0 |
| S1 | — | — | — | S0 | C1 | — | — |
| S2 | — | — | — | S0 | C2 | — | — |
| C1 | — | — | — | — | — | S0, observado | — |
| C2 | — | — | — | — | — | S2, observado | — |

| Secuencia generada | Caso | Riesgo |
|---|---|---|
| S0 → Login válido → S1 → Logout → S0 | T09-04 | Identidad y acceso correcto |
| S0 → Login inválido → S0 | T09-05/06/07/09/10 | Acceso indebido |
| Sesión autenticada → Logout → S0 → Atrás → S0 → URL directa → S0 | T09-11 | Datos visibles después del cierre |
| S0 → Login A sin recordar → S1 → cierre → C1 → reapertura → S0 | T09-13 | Persistencia no solicitada |
| S0 → Login B recordando → S2 → cierre → C2 → reapertura → S2 → Logout → S0 | T09-14 | Recuperación de sesión solicitada e identidad |

No se transforma el intervalo observado en una regla de tiempo. Si cambia la configuración del navegador o se cierra todo su proceso, es otro contexto que deberá registrarse al ejecutar.

### 5.4 Flujos de casos de uso

**UC1 — Enviar Signup.** A abre el formulario; S ofrece campos y condiciones; A envía datos; S acepta o informa rechazo. Alternativas observadas: vacío/términos no aceptados (**T09-01**), correo duplicado (**T09-02**). Selección del campo Timezone antes del envío: **T09-03**. El flujo exitoso completo no se acredita como explorado por el agente y queda como cobertura pendiente.

**UC2 — Consultar datos al cambiar de cuenta.** A inicia sesión, S muestra su identidad y Home; A incorpora un marcador propio, sale e inicia B; S muestra B sin el dato de A; B incorpora su marcador y sale; A vuelve y S conserva solo su dato; B vuelve y S conserva solo el suyo. **T09-12** deriva el recorrido completo de ida/vuelta. Las tareas son datos de preparación, no una repetición del objetivo funcional de T06.

### 5.5 Valores límite

No aplicados. No se confirmó una frontera de longitud o de intentos del producto. El catálogo discreto de Timezone se aborda como conjunto de valores ofrecidos, no como una frontera numérica de fechas. No se trasladan límites de ATM, ACME u otros ejemplos del docente.

## 6. Lista resumida de casos

| Caso | Objetivo / riesgo | Fundamento de la técnica | Importancia | Estado |
|---|---|---|---|---|
| T09-01 Signup vacío | Omisiones y términos; R6 | Clase conjunta inválida y alternativa UC1 | medium | Preparado |
| T09-02 Signup duplicado | Conservar cuenta existente; R5 | Partición correo registrado y alternativa UC1 | high | Preparado |
| T09-03 Timezone de Signup | Selección correcta; R6 | Valor del conjunto ofrecido; campo del UC1 | medium | Preparado |
| T09-04 Login válido | Acceso a A; R1 | Regla R6 y secuencia S0→S1→S0 | high | Preparado |
| T09-05 Login vacío | Denegar sin credenciales; R1 | Regla R1, ausencia de ambos campos | high | Preparado |
| T09-06 Email vacío | Denegar sin identificador; R1 | Regla R2 | high | Preparado |
| T09-07 Password vacío | Denegar sin contraseña; R1 | Regla R3 | high | Preparado |
| T09-08 Email mal formado | Respuesta no resuelta; R1/R6 | Candidato de entrada negativa; regla por confirmar | medium | Pendiente; excluido |
| T09-09 Cuenta inexistente | Denegar sin cuenta; R1 | Regla R4 y partición no registrada confirmada | high | Preparado |
| T09-10 Contraseña incorrecta | Denegar correspondencia falsa; R1 | Regla R5 y partición no corresponde | high | Preparado |
| T09-11 Logout, Atrás y URL | Cerrar acceso a datos; R2 | Secuencia de estados e historial | high | Preparado |
| T09-12 Aislamiento A/B | Evitar mezcla/exposición; R3 | Flujo UC2 completo con dos marcadores | high | Preparado |
| T09-13 Remember Me desmarcado | Sesión cerrada al reabrir; R4 | S1→C1→S0 | high | Preparado |
| T09-14 Remember Me marcado | Recuperar identidad al reabrir; R4 | S2→C2→S2 y cierre posterior | high | Preparado |

## 7. Implementación propuesta en TestLink

Pendiente de punto de control y OK. Proyecto TL:Todo.ly, suite T09 sin alterar otros tickets; nombres T09-NN, Importance individual, Manual, Summary con requerimiento/descripción/postcondiciones, Preconditions separado y pasos nativos con resultado por paso. No hay IDs ni enlaces nuevos confirmados. Los trece casos registrables están separados del candidato T09-08.

La evidencia real incluirá árbol de suite y un caso abierto; la exportación final se guardará en `testlink-xml/T09.xml` después de verificar el registro. Un XML local preparado para importar no se presenta como esa exportación.

## 8. Cobertura pendiente y límites

Pendientes: T09-08 y causa de sus vistas vacías; validaciones aisladas de Signup; registro válido completo observado bajo condiciones controladas; fronteras de campos; políticas de bloqueo/CAPTCHA y caducidad. No se necesita inventarlas para registrar los trece casos definidos. Las dos cuentas fueron creadas por el usuario para la práctica y su Login/estado inicial fueron verificados; no se confunde esa preparación con una ejecución formal del registro válido.

La preparación y los errores de lectura de correo Markdown, foco, captura y timeout pertenecen a la herramienta; no se reportan como defectos confirmados de Todo.ly. Las capturas con vista vacía o aviso ya desaparecido están diferenciadas en exploracion.md. Los marcadores actuales se conservan para limpieza al terminar los tres tickets, por instrucción del usuario.

## 9. Estado

**Trece casos diseñados y preparados para revisión; un candidato pendiente y excluido del registro.** Sin registro nuevo, comentario publicado ni ejecución formal. Después del OK y de verificar TestLink se actualizará a “Diseñados y registrados en TestLink; pendiente de revisión por otro integrante”, manteniendo la cobertura pendiente explícita. No se cambia el estado de Jira ni se marca la revisión de otra persona.

## Fichas para TestLink — trece casos preparados

<!-- FICHAS_GENERADAS -->

### T09-01. Rechazar Signup con campos vacíos y términos sin aceptar

**Importancia:** **medium**. Detecta aceptación de un formulario sin los datos necesarios ni el consentimiento indicado.

**Requerimiento:** PEB-73 / T09. Signup informa las omisiones observadas y no concede acceso.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.

**Descripción:** Comprobar la combinación vacía observada; no aislar como reglas independientes todas sus condiciones concurrentes.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir https://todo.ly/ y desplegar Signup. | Se muestran Full Name, Email, Password, Timezone, casilla de términos y Submit. |
| 2. Dejar Full Name, Email y Password vacíos, conservar Timezone predeterminado y dejar los términos sin marcar; pulsar Submit. | Se rechaza el envío con Error. Please correct the missing fields.; aparecen asteriscos en nombre, correo y contraseña, y el aviso If you don’t agree you can’t use Todo.ly. |
| 3. Conservar evidencia de las señales visibles y volver a https://todo.ly/ sin completar el registro. | La sesión continúa cerrada; no aparece el área de proyectos de una cuenta. |

**Postcondiciones:** Sin cuenta nueva ni sesión; evidencia de la combinación vacía, sin atribuir obligatoriedad del servidor a Timezone.

---

### T09-02. Rechazar el registro con el correo de una cuenta de prueba existente

**Importancia:** **high**. Evita sustituir o confundir una cuenta al reutilizar su identificador.

**Requerimiento:** PEB-73 / T09. Signup rechaza un correo ya registrado sin sustituir la cuenta existente.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.
3. Cuenta gratuita de prueba A y credenciales vigentes conocidas por quien ejecuta, conservadas únicamente en un registro privado.
4. Datos de registro válidos conocidos para la cuenta de prueba y aceptación de los términos por quien ejecuta.

**Descripción:** Comprobar el rechazo de un duplicado usando exclusivamente una cuenta propia de prueba.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Signup e introducir Prueba T09-02 - duplicado en Full Name, el correo de A en Email y una contraseña de prueba privada válida en Password; seleccionar La Paz UTC-04. | Los campos contienen los datos previstos y el correo corresponde a la cuenta de prueba existente. |
| 2. Quien ejecuta marca los términos que acepta y pulsa Submit. | Aparece Error. Account with this email address already exists!; no se registra una segunda cuenta con ese correo. |
| 3. Volver a Login e iniciar sesión con las credenciales de A vigentes antes del intento; abrir Settings / Profile. | Se accede a A y se conservan su identidad y nombre originales, sin aplicar el nombre del registro duplicado. |

**Postcondiciones:** A conserva sus datos y credenciales; no se crea otra cuenta. Evidencia del rechazo sin contraseñas.

---

### T09-03. Consultar y seleccionar Timezone como campo de Signup

**Importancia:** **medium**. Evita confundir las opciones de La Paz y atribuir al campo reglas temporales fuera del alcance.

**Requerimiento:** PEB-73 / T09. Signup ofrece selección de zona y refleja la opción elegida en el formulario.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.

**Descripción:** Comprobar opciones, valor inicial y ausencia de una opción vacía en la interfaz; sin crear cuenta ni evaluar vencimientos.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Signup y consultar el valor inicial de Timezone. | El selector muestra (UTC-08:00) Pacific Time (US & Canada), según la referencia observada. |
| 2. Desplegar el selector y revisar sus opciones, registrando el inventario visible. | La lista incluye (UTC-04:00) Georgetown, La Paz, Manaus, San Juan y la opción mexicana UTC-07 distinta; no ofrece una entrada vacía en el listado observado. El inventario de referencia contiene 101 opciones. |
| 3. Seleccionar (UTC-04:00) Georgetown, La Paz, Manaus, San Juan. | El selector refleja exactamente la opción UTC-04 elegida. |
| 4. Volver a https://todo.ly/ sin enviar Signup. | No se crea cuenta ni se modifica la configuración de A o B. |

**Postcondiciones:** Formulario descartado sin registro. No se concluye validación de servidor para un Timezone vacío que la interfaz no permite seleccionar.

---

### T09-04. Iniciar sesión con credenciales que corresponden a A

**Importancia:** **high**. Protege la operación esencial de acceso a la cuenta correcta.

**Requerimiento:** PEB-73 / T09. Credenciales vigentes que corresponden a una cuenta permiten acceso a esa identidad.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.
3. Cuenta gratuita de prueba A y credenciales vigentes conocidas por quien ejecuta, conservadas únicamente en un registro privado.

**Descripción:** Recorrer la regla positiva de la tabla de decisión y comprobar identidad en Profile.

| Paso | Resultado esperado |
|---|---|
| 1. Desplegar Login e introducir el correo de A y su contraseña vigente del registro privado; desmarcar Remember Me para este recorrido. | Los datos corresponden a A y la casilla está desmarcada. |
| 2. Pulsar Login, cuyo nombre accesible es Submit. | Se muestra el área autenticada con Settings y Logout. |
| 3. Abrir Settings / Profile y comparar identidad con el registro privado. | El nombre y el correo corresponden a A; no se abre otra cuenta. |
| 4. Cerrar Settings con Cancel y pulsar Logout. | Se vuelve a la página pública, con la sesión cerrada. |

**Postcondiciones:** Sesión cerrada y datos de A sin cambios; evidencia de identidad sin secretos.

---

### T09-05. Rechazar Login con ambos campos vacíos

**Importancia:** **high**. Evita acceso sin una combinación de credenciales que corresponda a la cuenta.

**Requerimiento:** PEB-73 / T09. La combinación negativa R1 de la tabla de decisión no concede acceso.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.

**Descripción:** Comprobar una regla negativa aislada sin ampliar el presupuesto de intentos.

| Paso | Resultado esperado |
|---|---|
| 1. Desplegar Login; dejar o introducir Email vacío y Password vacío; conservar Remember Me sin cambios. | Los campos contienen la combinación prevista, con datos de prueba y sin exponer credenciales en evidencia. |
| 2. Pulsar Login / Submit una sola vez. | No se concede acceso. La lectura posterior conserva Login y no muestra datos de proyectos autenticados. |
| 3. Conservar evidencia y abrir https://todo.ly/ en una consulta nueva sin introducir otras credenciales. | Aparece la página pública; la sesión sigue cerrada y no se exponen datos de A o B. |

**Postcondiciones:** Sin sesión ni cambios de cuenta. Un único intento negativo de esta ficha; evidencias sin contraseña legible.

---

### T09-06. Rechazar Login con Email vacío y Password informado

**Importancia:** **high**. Evita acceso sin una combinación de credenciales que corresponda a la cuenta.

**Requerimiento:** PEB-73 / T09. La combinación negativa R2 de la tabla de decisión no concede acceso.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.

**Descripción:** Comprobar una regla negativa aislada sin ampliar el presupuesto de intentos.

| Paso | Resultado esperado |
|---|---|
| 1. Desplegar Login; dejar o introducir Email vacío y Prueba-T09-no-valida-17 en Password; conservar Remember Me sin cambios. | Los campos contienen la combinación prevista, con datos de prueba y sin exponer credenciales en evidencia. |
| 2. Pulsar Login / Submit una sola vez. | No se concede acceso y se muestra Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below. |
| 3. Conservar evidencia y abrir https://todo.ly/ en una consulta nueva sin introducir otras credenciales. | Aparece la página pública; la sesión sigue cerrada y no se exponen datos de A o B. |

**Postcondiciones:** Sin sesión ni cambios de cuenta. Un único intento negativo de esta ficha; evidencias sin contraseña legible.

---

### T09-07. Rechazar Login de A con Password vacío

**Importancia:** **high**. Evita acceso sin una combinación de credenciales que corresponda a la cuenta.

**Requerimiento:** PEB-73 / T09. La combinación negativa R3 de la tabla de decisión no concede acceso.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.
3. Cuenta gratuita de prueba A y credenciales vigentes conocidas por quien ejecuta, conservadas únicamente en un registro privado.
4. Menos de tres intentos fallidos asociados a A en la exploración del lote; la clave vigente es distinta de Prueba-T09-no-valida-17.

**Descripción:** Comprobar una regla negativa aislada sin ampliar el presupuesto de intentos.

| Paso | Resultado esperado |
|---|---|
| 1. Desplegar Login; dejar o introducir el correo vigente de A y Password vacío; conservar Remember Me sin cambios. | Los campos contienen la combinación prevista, con datos de prueba y sin exponer credenciales en evidencia. |
| 2. Pulsar Login / Submit una sola vez. | No se concede acceso y se muestra Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below. |
| 3. Conservar evidencia y abrir https://todo.ly/ en una consulta nueva sin introducir otras credenciales. | Aparece la página pública; la sesión sigue cerrada y no se exponen datos de A o B. |

**Postcondiciones:** Sin sesión ni cambios de cuenta. Un único intento negativo de esta ficha; evidencias sin contraseña legible.

---

### T09-09. Rechazar Login con un correo no registrado

**Importancia:** **high**. Evita acceso sin una combinación de credenciales que corresponda a la cuenta.

**Requerimiento:** PEB-73 / T09. La combinación negativa R4 de la tabla de decisión no concede acceso.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.
3. El correo reservado prueba-t10-no-registrada-20261117@example.com no pertenece a una cuenta; esta condición fue contrastada mediante recuperación en la exploración.

**Descripción:** Comprobar una regla negativa aislada sin ampliar el presupuesto de intentos.

| Paso | Resultado esperado |
|---|---|
| 1. Desplegar Login; dejar o introducir prueba-t10-no-registrada-20261117@example.com y Prueba-T09-no-valida-17 en Password; conservar Remember Me sin cambios. | Los campos contienen la combinación prevista, con datos de prueba y sin exponer credenciales en evidencia. |
| 2. Pulsar Login / Submit una sola vez. | No se concede acceso y se muestra Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below. |
| 3. Conservar evidencia y abrir https://todo.ly/ en una consulta nueva sin introducir otras credenciales. | Aparece la página pública; la sesión sigue cerrada y no se exponen datos de A o B. |

**Postcondiciones:** Sin sesión ni cambios de cuenta. Un único intento negativo de esta ficha; evidencias sin contraseña legible.

---

### T09-10. Rechazar Login de A con contraseña incorrecta

**Importancia:** **high**. Evita acceso sin una combinación de credenciales que corresponda a la cuenta.

**Requerimiento:** PEB-73 / T09. La combinación negativa R5 de la tabla de decisión no concede acceso.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.
3. Cuenta gratuita de prueba A y credenciales vigentes conocidas por quien ejecuta, conservadas únicamente en un registro privado.
4. Menos de tres intentos fallidos asociados a A en la exploración del lote; la clave vigente es distinta de Prueba-T09-no-valida-17.

**Descripción:** Comprobar una regla negativa aislada sin ampliar el presupuesto de intentos.

| Paso | Resultado esperado |
|---|---|
| 1. Desplegar Login; dejar o introducir el correo vigente de A y Prueba-T09-no-valida-17 en Password; conservar Remember Me sin cambios. | Los campos contienen la combinación prevista, con datos de prueba y sin exponer credenciales en evidencia. |
| 2. Pulsar Login / Submit una sola vez. | No se concede acceso y se muestra Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below. |
| 3. Conservar evidencia y abrir https://todo.ly/ en una consulta nueva sin introducir otras credenciales. | Aparece la página pública; la sesión sigue cerrada y no se exponen datos de A o B. |

**Postcondiciones:** Sin sesión ni cambios de cuenta. Un único intento negativo de esta ficha; evidencias sin contraseña legible.

---

### T09-11. Cerrar sesión y proteger datos ante Atrás y URL directa

**Importancia:** **high**. Detecta exposición de datos después de Logout por historial o navegación directa.

**Requerimiento:** PEB-73 / T09. Logout deja sin acceso autenticado el historial y la URL previamente observada.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Cuenta gratuita de prueba A y credenciales vigentes conocidas por quien ejecuta, conservadas únicamente en un registro privado.
3. Sesión iniciada como A; proyecto Home disponible y sin una tarea llamada Prueba T09-11 - sesión.

**Descripción:** Comprobar una secuencia de estados con un marcador propio reconocible; la creación de la tarea es preparación para la observación de sesión.

| Paso | Resultado esperado |
|---|---|
| 1. Seleccionar Home y crear mediante Add una tarea Prueba T09-11 - sesión. | Home de A muestra el marcador pendiente para distinguir sus datos. |
| 2. Pulsar Logout. | Aparece la página pública y el marcador ya no se muestra como dato autenticado. |
| 3. Usar Atrás del navegador una vez. | No se restablece una sesión autenticada ni se expone el marcador de A. |
| 4. Introducir directamente https://todo.ly/, URL observada durante la sesión, sin Login. | Se muestra la página pública con acceso a Login; no se expone el marcador. |
| 5. Conservar evidencia del estado posterior a las dos navegaciones. | La evidencia permite reconocer la ausencia de acceso autenticado sin contener secretos. |

**Postcondiciones:** Sesión cerrada. El marcador permanece en Home de A para la limpieza del lote; datos previos conservados. No se afirma protección de API ni de rutas que no se hayan observado.

---

### T09-12. Separar los datos propios de A y B al cambiar de cuenta

**Importancia:** **high**. Evita exposición o mezcla de información entre dos cuentas sin proyectos compartidos.

**Requerimiento:** PEB-73 / T09. Cada cuenta muestra sus propios datos de Home después de cambiar de identidad.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.
3. Dos cuentas gratuitas de prueba A y B sin proyectos compartidos; credenciales privadas vigentes y proyectos Home disponibles.
4. No existen los marcadores Prueba T09-12 - marcador A y Prueba T09-12 - marcador B en sus respectivos Home.

**Descripción:** Comprobar aislamiento en ambos sentidos mediante datos distintos y consultas de identidad.

| Paso | Resultado esperado |
|---|---|
| 1. Iniciar sesión como A y verificar su identidad en Settings; cerrar Settings con Cancel. | El perfil corresponde a A. |
| 2. Abrir Home y crear Prueba T09-12 - marcador A; pulsar Logout. | El marcador pertenece a Home de A y la sesión queda cerrada. |
| 3. Iniciar sesión como B, verificar identidad en Settings y consultar Home. | Se abre B; no aparece el marcador de A. |
| 4. Crear Prueba T09-12 - marcador B en Home de B y pulsar Logout. | B conserva su marcador y la sesión queda cerrada. |
| 5. Iniciar sesión como A y consultar Home. | A muestra su marcador y no el de B. |
| 6. Pulsar Logout, iniciar sesión como B y consultar Home. | B muestra su marcador y no el de A. |
| 7. Conservar evidencia de ambos sentidos y pulsar Logout. | La sesión queda cerrada y los marcadores siguen separados por cuenta. |

**Postcondiciones:** Marcadores propios en Home de sus cuentas, pendientes de la limpieza del lote; sin proyectos compartidos ni cambios a datos de otras personas.

---

### T09-13. Reabrir el perfil tras Login con Remember Me desmarcado

**Importancia:** **high**. Detecta permanencia de acceso no solicitada al reabrir el perfil de QA.

**Requerimiento:** PEB-73 / T09. El recorrido observado sin Remember Me vuelve a la página pública al reabrir.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.
3. Cuenta gratuita de prueba A y credenciales vigentes conocidas por quien ejecuta, conservadas únicamente en un registro privado.
4. Perfil dedicado sin otras ventanas propias; configuración de Chrome estable durante el recorrido y posibilidad de reabrir ese mismo perfil.

**Descripción:** Repetir el recorrido observado con A, registrando intervalo y cierre de ventanas; no inferir una caducidad de cookies.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Login y desmarcar Remember Me; conservar evidencia de la casilla desmarcada antes del envío. | Remember Me está desmarcado. |
| 2. Introducir las credenciales vigentes de A, pulsar Login y confirmar identidad en Profile. | Se inicia sesión en A; Settings y Logout están disponibles. |
| 3. Cerrar todas las ventanas de ese perfil dedicado sin pulsar Logout, sin borrar cookies y sin cerrar otros perfiles. Anotar el intervalo hasta la reapertura. | Las ventanas del perfil QA quedan cerradas; el resto del navegador conserva sus sesiones. |
| 4. Reabrir el mismo perfil y consultar https://todo.ly/ sin introducir credenciales. | Aparece la página pública con Login/Signup, sin una sesión autenticada, conforme al recorrido observado. |
| 5. Conservar evidencia con nombre del perfil y estado de Todo.ly. | La evidencia identifica la reapertura correcta; no se usa otro perfil como prueba. |

**Postcondiciones:** Perfil QA abierto con sesión cerrada, datos y credenciales sin cambios; intervalo y cualquier ayuda manual documentados.

---

### T09-14. Reabrir el perfil tras Login con Remember Me marcado

**Importancia:** **high**. Comprueba recuperación de la sesión solicitada sin confundirla con un nuevo Login.

**Requerimiento:** PEB-73 / T09. El recorrido observado con Remember Me conserva la identidad autenticada al reabrir.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.
3. Cuenta gratuita de prueba B con credenciales privadas vigentes; perfil dedicado sin otras ventanas propias y configuración de Chrome estable.

**Descripción:** Repetir el recorrido observado con B, comprobando la identidad restaurada y cerrando después la sesión.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Login y marcar Remember Me; conservar evidencia de la casilla antes del envío. | Remember Me está marcado. |
| 2. Introducir las credenciales vigentes de B, pulsar Login y consultar Profile. | Se inicia sesión y se confirma la identidad de B. |
| 3. Cerrar todas las ventanas de ese perfil sin Logout, sin borrar cookies y sin cerrar otros perfiles; registrar el intervalo. | Las ventanas QA quedan cerradas conservando la configuración del recorrido. |
| 4. Reabrir el mismo perfil y consultar https://todo.ly/ sin introducir credenciales. | Aparece el área autenticada con Settings y Logout, sin un nuevo envío de Login. |
| 5. Abrir Profile y contrastar identidad con el registro privado. | La sesión restaurada corresponde a B, no a A ni a otra cuenta. |
| 6. Conservar evidencia, cerrar Profile con Cancel y pulsar Logout. | Se vuelve a la página pública y la sesión queda cerrada. |

**Postcondiciones:** Sesión de B cerrada después de conservar evidencia; datos y credenciales sin cambios. El recorrido no prueba una caducidad ni el cierre completo del proceso Chrome.

---

## Candidato pendiente — no registrar todavía

---

### T09-08. Investigar Login con Email sin formato de correo

**Importancia:** **medium**. Identifica una entrada negativa cuya respuesta visible todavía no está resuelta.

**Requerimiento:** PEB-73 / T09. Tratamiento del Email mal formado, pendiente de fijar resultado visible.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión de Todo.ly cerrada en un perfil dedicado de QA, sin sesiones de otras personas en ese perfil.

**Descripción:** Candidato pendiente: las vistas vacías impiden fijar una respuesta de validación. No registrar como caso listo.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Login e introducir PruebaT09SinArroba en Email y Prueba-T09-no-valida-17 en Password. | Los campos contienen los representantes de prueba, sin datos de una cuenta ajena. |
| 2. Pulsar Login / Submit una sola vez. | PENDIENTE: confirmar el tratamiento visible y el mensaje. La página vacía de la herramienta no demuestra una regla de validación del producto. |
| 3. Abrir una consulta GET nueva sin introducir credenciales y registrar el estado. | Se documenta si aparece la página pública o una sesión autenticada; no se atribuye el resultado a una regla sintáctica sin confirmarla. |

**Postcondiciones:** Candidato fuera del registro propuesto; sin cambios de credencial y con la causa de la vista vacía pendiente.
