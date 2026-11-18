<!-- BORRADOR: publicar solo después de revisión y registro verificado. -->

# T09 / PEB-73 — Registro, acceso y sesión

## 1. Análisis del área

Se analizaron Signup, Login, Remember Me, Logout y el cambio entre dos cuentas gratuitas propias de la práctica. El entorno observado fue macOS 26.6.2 y Chrome 157.0.8103.51, con el perfil aislado Todo.ly QA cuenta B. El nombre del perfil no identifica la cuenta: la identidad se verificó desde Settings / Profile.

Signup muestra Full Name, Email, Password, Timezone, términos y el botón visible Signup (nombre accesible Submit). Se abre desde Sign Up Free. El envío completamente vacío y sin términos fue rechazado; el correo ya registrado también tuvo un rechazo específico. Timezone ofrece un valor predeterminado y una lista sin opción vacía visible; se identificó La Paz UTC-04 y su diferencia con la opción mexicana UTC-07. Esto no demuestra validación de servidor ante un Timezone vacío ni reglas de fechas.

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

Cancel de Settings y el nombre accesible Submit de Login fueron observados en T10 y en las consultas de identidad de A/B: fuente trabajo/T10/exploracion.md y captura de Old Password vacío. La nomenclatura visible de Signup y Sign Up Free fue verificada directamente por Codex en las capturas registro-vacio y remember-off-reapertura-sin-sesion. Se adjuntarán como evidencia de registro únicamente el árbol y casos abiertos de TestLink con fichas genéricas; no capturas de exploración que muestren correos reales.

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
| Identificador conocido no registrado | No identifica una cuenta: no autentica | Correo reservado contrastado en trabajo/T10/exploracion.md, sección Recuperación: solicitud y contraste, 11:13 AM | T09-09; R4 |
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

Registro autorizado tras revisión sin bloqueantes y tratamiento de observaciones. Proyecto TL:Todo.ly, suite existente Todo.ly tests; XML de entrada testcases, sin crear suites ni actualizar existentes; nombres T09-NN, Importance individual, Manual, Summary con requerimiento/descripción/postcondiciones, Preconditions separado y pasos nativos con resultado por paso. No hay IDs ni enlaces nuevos confirmados. Los trece casos registrables están separados del candidato T09-08.

La evidencia real incluirá árbol de suite y un caso abierto; se exportará realmente Todo.ly tests a `testlink-xml/todo-ly-tests.xml` después de verificar el registro; de ella se extraerá `testlink-xml/T09.xml` mediante script. Un XML local preparado para importar no se presenta como esa exportación.

## 8. Cobertura pendiente y límites

Pendientes: T09-08 y causa de sus vistas vacías; validaciones aisladas de Signup; registro válido completo observado bajo condiciones controladas; fronteras de campos; políticas de bloqueo/CAPTCHA y caducidad. No se necesita inventarlas para registrar los trece casos definidos. Las dos cuentas fueron creadas por el usuario para la práctica y su Login/estado inicial fueron verificados; no se confunde esa preparación con una ejecución formal del registro válido.

La preparación y los errores de lectura de correo Markdown, foco, captura y timeout pertenecen a la herramienta; no se reportan como defectos confirmados de Todo.ly. Las capturas con vista vacía o aviso ya desaparecido están diferenciadas en exploracion.md. Los marcadores actuales se conservan para limpieza al terminar los tres tickets, por instrucción del usuario.

## 9. Estado

**Trece casos diseñados y preparados para revisión; un candidato pendiente y excluido del registro.** Sin registro nuevo, comentario publicado ni ejecución formal. Después de la revisión sin bloqueantes y de verificar TestLink se actualizará a “Diseñados y registrados en TestLink; pendiente de revisión por otro integrante”, manteniendo la cobertura pendiente explícita. No se cambia el estado de Jira ni se marca la revisión de otra persona.
