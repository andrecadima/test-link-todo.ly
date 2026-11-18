# T10 / PEB-74 — Perfil, credenciales y recuperación de acceso

Fecha:18/11/2026. Nueve casos registrados y comparados en TestLink,79pasos. Comentario10226 actualizado y leído por MCP con casos de uso/decisión revisados y los tres IDs adicionales TL-85/86/87. T10-07 continúa pendiente y no se registra. Sin ejecución formal ni revisión de integrante.

## 1. Análisis del área

Se analizaron Settings / Profile, guardado con Ok, descarte con Cancel y recuperación: Login → Reset your Password → Send → correo Forgot Password → formulario → nuevo Login. Entorno: Chrome 157.0.8103.51/macOS 26.6.2, cuentas gratuitas propias A/B y navegador aislado; exploración, sin ejecución formal.

Profile ofrece Full Name, Email, Time zone, Old Password y New Password; **sin confirmación de contraseña**. Recuperación sí ofrece Enter a New Password, Verify New Password y Done. Se comprobaron nombre guardado/descartado, persistencia tras recarga y nombre inicial restaurado tras nueva sesión; recuperación de A y contraste de claves; recuperación inexistente rechazada.

El 18/11: a) Old incorrecto→Invalid Password; b) cambio válido desde Settings/restauración, reemplazada rechazada y original aceptada con identidad conservada; c) Email editado de B descartado por Cancel conserva original. Capturas manuales y contraste posterior en registro de exploración. No se inventa mensaje de éxito. Email válido07 y New Password vacío pendientes. Zona horaria, vencimientos, eliminación de cuenta y funciones Pro quedan fuera; sesión completa en T09.

## 2. Riesgos que orientan el diseño

Valoración cualitativa de diseño, no frecuencia medida: probabilidad P baja=1/media=2/alta=3; impacto I bajo=1/medio=2/alto=3; nivel P×I, alto=6–9, medio=3–4 y bajo=1–2. Se priorizan acceso y transporte de recuperación.

| Riesgo | Consecuencia para la persona usuaria | P y fundamento | I | Nivel | Casos |
|---|---|---|---|---|---|
| R1: cambio o recuperación deja credenciales incoherentes | Pérdida de acceso o contraseña anterior todavía utilizable | 2: secuencia con cambios persistentes y Login posterior | 3 | 6, alto | T10-03, 04, 05, 08 |
| R2: guardado del nombre no persiste o altera otro campo | Perfil incorrecto tras recarga o nueva sesión | 2: estado editado/guardado y consultas posteriores | 2 | 4, medio | T10-02 |
| R3: Cancel aplica una edición descartada | Nombre o identificador de acceso cambiado involuntariamente | 2: mismo formulario con dos salidas de edición | 3 | 6, alto | T10-01, 06 |
| R4: Email nuevo desliga datos o impide acceso | Pérdida de acceso a B o identificación incorrecta de sus datos | 2: identificador persistente con activación aún desconocida | 3 | 6, alto | T10-07, pendiente |
| R5: token de recuperación se entrega mediante HTTP | Exposición potencial de un enlace que autoriza restablecer credenciales | 3: enlace HTTP ya observado, pendiente confirmar en ejecución | 3 | 9, alto | T10-10 |
| R6: alternativa de recuperación para correo inexistente resulta confusa | La persona no distingue rechazo de solicitud aceptada | 2: resultado alternativo observable y distinto del válido | 2 | 4, medio | T10-09 |

## 3. Reglas, restricciones y dudas

| Regla / condición | Clasificación | Fundamento |
|---|---|---|
| Ok guarda Full Name; Cancel lo descarta; nombre guardado persiste tras recarga | Comportamiento observado | Profile del 17/11; tras nueva sesión se comprobó el nombre inicial restaurado, no el texto temporal. |
| El nombre temporal guardado persiste también en nueva sesión | Criterio del equipo | Persistencia solicitada; contraste previsto en 02. |
| Settings ofrece Old Password y New Password, sin confirmación | Comportamiento observado | Formulario de Profile. |
| Old Password vacío o incorrecto, con New Password informado, muestra Invalid Password | Comportamiento observado | Capturas manuales 17/11,14:38 y 18/11,15:56. |
| El rechazo conserva la credencial vigente | Observado para 03; criterio del equipo para 04 |03: Login directo;04: respaldo indirecto de b), Login posterior previsto en su ficha. |
| Old vigente y New informado: Settings cierra, reemplazada rechazada y objetivo aceptada; identidad conservada | Comportamiento observado | b),18/11 y Login/Profile posterior; A restaurada y registro privado actualizado. Sin literal de éxito. |
| Email editado y Cancel conserva correo original de B | Comportamiento observado | c),18/11,15:59 y AX; alternativo no se afirma del mismo buzón. |
| Recuperación registrada informa Info. An email has been sent with a link where you can change your password.; cambio permite nueva clave y rechaza reemplazada | Comportamiento observado | Solicitud, correo, cambio manual y Login posterior de A. |
| Recuperación no registrada muestra Error. Account with this Email address doesn't exist. | Comportamiento observado | Dirección example.com contrastada. |
| Enlace recibido sin modificar debe abrir Please Enter a New Password y usar HTTPS | Criterio del equipo | Instrucciones expresas;08 funcional y10 transporte. |
| Correo entregó HTTP; Chrome mostró Not Secure; misma ruta HTTPS cargó el formulario | Comportamiento observado | Hallazgo exploratorio para confirmar al ejecutar; sin reporte en planilla. |
| New Password vacío, Email válido, política de clave, fronteras, caducidad/uso único y sesiones paralelas | Duda pendiente | Sin regla confirmada; no se copian reglas de ejemplos ACME. |

## 4. Tipos de prueba y escenarios seleccionados

| Tipo | Objetivo y pertinencia | Procedimiento | Criterio observable |
|---|---|---|---|
| Funcional | Guardado/descarte, persistencia y continuidad del acceso; R1–R4 y R6 | Contrastar Profile antes/después, recarga, Logout/Login y recuperación con buzón controlado | Valores exactos conservados o modificados según la acción; acceso con identificador/credencial vigentes |
| Seguridad observable | Transporte del enlace que autoriza recuperación; R5 | Inspeccionar esquema de enlaces del correo y conexión visible en Chrome sin interceptar tráfico ni enviar contraseña por HTTP | HTTPS en el enlace y conexión segura al formulario según criterio del equipo |

Positivos: guardar nombre, cambio válido de contraseña desde Settings (T10-05), recuperar una cuenta propia. Negativos: recuperación con correo inexistente, Old Password vacío y Old Password incorrecto, con rechazos observados. Alternativos: Cancel del nombre y Cancel del Email (T10-06). El cambio válido de Email queda pendiente de su regla de activación. No se añade compatibilidad Firefox ni accesibilidad completa sin exploración y objetivo concreto; observar un mensaje comprensible no constituye por sí solo una prueba no funcional de usabilidad.

## 5. Técnicas aplicadas y artefactos

Se aplican **casos de uso** a los recorridos secuenciales de perfil y recuperación: escenario principal, actor/sistema y extensiones con casos derivados (PDF docente pp. 58–62). Particiones agrupa entradas de tratamiento equivalente; decisión combina condiciones y acciones (pp.8–9 y45–48). Aquí una lista de clases no explica los recorridos completos, por lo que no se atribuye particiones. Las reglas desconocidas permanecen pendientes.

### 5.1 Casos de uso: actor, sistema y extensiones

**A (actor):** persona que opera la interfaz; **S (sistema):** Todo.ly. Cuenta A y cuenta B identifican las cuentas de prueba, no al actor. Según el docente, un caso de uso puede derivar varios casos de prueba; cada extensión siguiente identifica el paso del que se separa. Las cuentas, valores privados y controles se concretan en las fichas de TestLink.

**UC1 — Modificar el nombre de perfil.** Previo: sesión de la cuenta A y nombre inicial conocido.

| Escenario | Paso | Descripción |
|---|---|---|
| Principal | 1 | A: abre Settings / Profile. |
| Principal | 2 | S: muestra Full Name y los controles Ok / Cancel. |
| Principal | 3 | A: sustituye Full Name por el nombre de prueba. |
| Principal | 4 | A: pulsa Ok. |
| Principal | 5 | S: cierra Settings y conserva el nombre guardado. |
| Principal | 6 | A: consulta Profile tras recarga y nueva sesión. |
| Principal | 7 | S: muestra el nombre guardado; persistencia en nueva sesión como criterio del equipo. |
| Extensión | 4a | A: pulsa Cancel en lugar de Ok. |
| Extensión | 4a.1 | S: cierra Settings sin guardar; al reabrir Profile muestra el nombre inicial. |

**Derivación:** principal 1–7 → **T10-02**; extensión 4a → **T10-01**. La ficha02 restaura el nombre inicial al terminar.

**UC2 — Recuperar acceso mediante el buzón controlado.** Previo: sin sesión y buzón de la cuenta A controlado por quien ejecuta.

| Escenario | Paso | Descripción |
|---|---|---|
| Principal | 1 | A: abre Login → Reset your Password. |
| Principal | 2 | S: muestra el campo de correo y Send. |
| Principal | 3 | A: informa el correo registrado de A y pulsa Send. |
| Principal | 4 | S: informa el envío del enlace; llega el mensaje al buzón. |
| Principal | 5 | A: abre el enlace tal como llega en el correo. |
| Principal | 6 | S: muestra Please Enter a New Password; criterio del equipo para el enlace recibido, sin sustituir HTTP manualmente. |
| Principal | 7 | A: introduce personalmente la nueva contraseña y su confirmación, y pulsa Done. |
| Principal | 8 | S: acepta el cambio, sin exigir un mensaje literal de éxito no observado. |
| Principal | 9 | A: contrasta Login con la reemplazada y con la nueva, y consulta Profile. |
| Principal | 10 | S: rechaza la reemplazada, acepta la nueva y conserva la identidad. |
| Extensión | 4a | A: informa el correo no registrado de example.com y pulsa Send. |
| Extensión | 4a.1 | S: muestra Error. Account with this Email address doesn't exist.; no se solicita abrir ningún buzón. |

**Derivación:** principal 1–10 → **T10-08**; extensión 4a → **T10-09**. **T10-10** comprueba transversalmente el transporte en el paso 5: HTTPS como criterio del equipo, sin modificar el enlace para hacer pasar08. El hallazgo HTTP sigue por confirmar en ejecución y fuera de la planilla de fallas. La restauración posterior se realizó mediante05/b), no dentro de08.

**UC3 — Cambiar la contraseña desde Settings.** Previo: sesión de la cuenta A, credencial vigente y objetivo distintos en registro privado.

| Escenario | Paso | Descripción |
|---|---|---|
| Principal | 1 | A: abre Settings / Profile. |
| Principal | 2 | S: muestra Old Password, New Password y Ok; sin confirmación adicional en Settings. |
| Principal | 3 | A: informa la vigente en Old Password y la objetivo en New Password. |
| Principal | 4 | A: pulsa Ok. |
| Principal | 5 | S: cierra Settings sin Invalid Password. |
| Principal | 6 | A: cierra sesión y contrasta Login con la reemplazada y con la objetivo. |
| Principal | 7 | S: rechaza la reemplazada y concede acceso con la objetivo, conservando Profile. |
| Extensión | 5a | A: deja Old Password vacío, con New Password informado, y pulsa Ok. |
| Extensión | 5a.1 | S: muestra Invalid Password; la vigente conserva el acceso, contrastado por Login. |
| Extensión | 5b | A: informa Old Password incorrecto, con New Password informado, y pulsa Ok. |
| Extensión | 5b.1 | S: muestra Invalid Password; conservación de acceso como criterio del equipo, respaldada indirectamente por b) y por verificar directamente en el caso04. |

**Derivación:** principal → **T10-05**;5a → **T10-03**;5b → **T10-04**. Cuando la objetivo es la original, el principal sirve de restauración sin un segundo cambio. New Password vacío queda pendiente: no se le asigna una extensión de resultado inventado.

**UC4 — Descartar la edición de Email.** Previo: sesión de la cuenta B, correo original y alternativo privados.

| Escenario | Paso | Descripción |
|---|---|---|
| Principal | 1 | A: con sesión de la cuenta B, abre Settings / Profile. |
| Principal | 2 | S: muestra Email original. |
| Principal | 3 | A: sustituye Email por el alternativo y pulsa Cancel, sin Ok. |
| Principal | 4 | S: cierra Settings sin aplicar el cambio. |
| Principal | 5 | A: vuelve a abrir Profile. |
| Principal | 6 | S: muestra exactamente el correo original. |

**Derivación:** recorrido de descarte → **T10-06**. Guardar un cambio válido de Email es otro recorrido todavía pendiente (**T10-07**); no se supone activación inmediata ni ausencia de verificación por correo.

### 5.2 Tabla de decisión de Settings — alcance confirmado y pendientes

Se conserva por el acuerdo previo del equipo. Condiciones arriba, acciones debajo y reglas por columna, como pp.46/48/53. **T/F** verdadero/falso; **N.A.** correspondencia no evaluable si Old Password está vacío; **Execute** acción esperada; **?** resultado sin confirmar, no caso listo. C2 no es una condición independiente cuando C1=F: no se crean combinaciones imposibles de correspondencia con una entrada ausente.

| Condiciones / acciones | Regla 1 | Regla 2 | Regla 3 | Regla 4 pendiente | Regla 5 pendiente | Regla 6 pendiente |
|---|---|---|---|---|---|---|
| C1: Old Password informado | F | T | T | F | T | T |
| C2: Old Password coincide con la vigente | N.A. | F | T | N.A. | F | T |
| C3: New Password informado | T | T | T | F | F | F |
| Mostrar Invalid Password | Execute | Execute | — | ? | ? | ? |
| Aceptar cambio de contraseña | — | — | Execute | ? | ? | ? |
| Caso derivado / situación | T10-03 | T10-04 | T10-05 | Sin caso | Sin caso | Sin caso |

Las tres reglas confirmadas respaldan los recorridos de UC3; **no se afirma cobertura completa de las seis combinaciones factibles**. Reglas 4–6 no se ejecutaron como intentos de cambio y no se deducen del guardado normal de Full Name. La conservación tras rechazo se comprueba en03/04; en04 es criterio del equipo con respaldo indirecto.

### 5.3 Técnicas no aplicadas

No se atribuyen particiones de equivalencia a T10 tras esta corrección. No se aplican valores límite sin frontera confirmada. La transición de sesión y Remember Me se trata en T09; raíz/subproyecto en T11. La tabla de decisión apoya solo 03/04/05, y los casos de uso derivan los recorridos descritos; no se agregan técnicas para aumentar su cantidad.

## 6. Lista resumida de casos

| Caso | Objetivo / riesgo cubierto | Fundamento de la técnica | Importancia | TestLink | Situación actual |
|---|---|---|---|---|---|
| T10-01 Cancelar nombre | Descartar una edición; R3 | Alternativa Cancel del UC1, ya contrastada | medium | [TL-66](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-66) | Registrado y comparado. |
| T10-02 Guardar nombre y persistir | Evitar pérdida del perfil; R2 | Principal UC1 con recarga y nueva sesión | high | [TL-67](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-67) | Registrado y comparado. |
| T10-03 Old Password vacío | Proteger cambio de credencial; R1 | Extensión5a de UC3 y Regla 1; Invalid Password observado | high | [TL-68](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-68) | Registrado y comparado. |
| T10-04 Old Password incorrecto | Proteger cambio de credencial; R1 | Extensión5b de UC3 y Regla 2; rechazo observado | high | [TL-85](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-85) | Registrado y comparado. |
| T10-05 Cambio válido desde Settings | Continuidad del acceso e invalidación de la reemplazada; R1 | Principal UC3 y Regla 3; acceso con objetivo e invalidación de reemplazada | high | [TL-86](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-86) | Registrado y comparado. |
| T10-06 Cancelar correo | Conservar identificador descartado; R3 | Principal de descarte UC4, pasos1–6 | high | [TL-87](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-87) | Registrado y comparado. |
| T10-07 Cambiar correo a alias y restaurar | Evitar pérdida de acceso/datos; R4 | Recorrido de guardado de Email, pendiente | high | No registrado | Pendiente de verificación/activación |
| T10-08 Recuperar acceso | Acceso con credencial nueva; R1 | Principal UC2: solicitud, enlace recibido, cambio y Login | high | [TL-69](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-69) | Registrado y comparado. |
| T10-09 Correo no registrado | Distinguir rechazo de envío aceptado; R6 | Extensión4a de UC2: correo no registrado y rechazo | medium | [TL-70](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-70) | Registrado y comparado. |
| T10-10 HTTPS del enlace | Transporte del token; R5 | Procedimiento observable sobre entrega/apertura del UC2, criterio del equipo | high | [TL-71](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-71) | Registrado y comparado. |

## 7. Implementación en TestLink

Se registraron **seis casos, 28 pasos**, en **TL:Todo.ly → Todo.ly tests (id3)**: TL-66 a TL-71. Suite:64 antes,70 después; sin T10 previo, duplicados omitidos por nombre, sin suites nuevas ni actualización de existentes. Cada título, Summary, Preconditions, paso/resultado, Importance y Manual fue cotejado: **sin diferencias**. Estado TestLink **Draft**.

Se añadieron únicamente T10-04/05/06: **TL-85, TL-86 y TL-87**,51 pasos;128 textos y campos nativos cotejados sin diferencias. Total T10: **nueve casos,79 pasos**. Revisiones08 y11 APTO, observaciones resueltas; no sustituyen la revisión de otro integrante. T10-07 fuera del registro.

La exploración fue macOS/Chrome; guía §10 prevé ejecución Windows/Chrome con versiones reales anotadas. T10-10 requiere enlace no utilizado: antes de T10-08 o con solicitud propia. Evidencias externas: árbol y ficha genérica TestLink; no capturas de Profile con correos reales. Exportación real y extracción por ticket pendientes del cierre.

Comentario [PEB-74 / 10226](https://alesalve.atlassian.net/browse/PEB-74?focusedCommentId=10226): cuatro capturas (tres anteriores conservadas y nueva vista de nueve casos con TL-87 abierto), tablas legibles con desplazamiento horizontal. Estado Jira conservado.

## 8. Cobertura pendiente y límites

T10-07 (Email válido) no se registra. New Password vacío, políticas de clave, fronteras, caducidad/uso único y sesiones paralelas siguen pendientes. A quedó restaurada por 05/b), con Login verificado; B conserva Email original. Los cuatro PDF faltantes no se usan como fuentes.

Nombre vacío produjo Loading y después conservó el nombre inicial, sin validador legible: no se deduce obligatoriedad. HTTP queda como hallazgo a confirmar durante ejecución, sin planilla de fallas. La revisión por integrante y ejecución formal permanecen pendientes.

## 9. Estado

**Diseñados y registrados en TestLink; pendiente de revisión por otro integrante.** Nueve casos,79 pasos. T10-07 excluido; cobertura completa y ejecución formal pendientes. Sin reporte de HTTP en planilla.

Comprobación de criterios de aceptación, sin modificar el checklist ni el estado del ticket:

| Criterio | Situación |
|---|---|
| Reglas y restricciones documentadas | Documentadas, con dudas explícitas. |
| Tipos de prueba seleccionados y justificados | Funcional y seguridad observable, vinculados a riesgos. |
| Riesgos de pérdida de acceso y modificación incorrecta | R1–R6 trazados; Settings03/04/05 y Cancel06 cubiertos; Email válido07 pendiente. |
| Cambios válidos, inválidos y cancelaciones | Nombre, recuperación, contraseña y Cancel cubiertos; Email válido pendiente. |
| Técnicas y procedimientos justificados | Casos de uso con extensiones/trazas; decisión Settings con pendientes explícitos; sin límites inventados. |
| Cuentas, buzones, condiciones y resultados en los casos | Fichas genéricas; única contraseña literal: dato sintético inválido de04. |
| Registro en TestLink y revisión de otro integrante | Nueve registrados y comparados; revisión de integrante pendiente. |

## Fichas para TestLink — nueve casos registrados

<!-- FICHAS_GENERADAS -->

### T10-01. Cancelar la modificación del nombre conserva el perfil

**Importancia:** **medium**. Evita que se guarden cambios que la persona decidió descartar.

**Requerimiento:** PEB-74 / T10. Cancelar la edición del nombre conserva el valor anterior.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión del navegador identificados al ejecutar.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba A.
3. Nombre inicial de A conocido por quien ejecuta; datos de acceso conservados en un registro privado.

**Descripción:** Comprobar que Cancel descarta un nombre editado y que el valor original permanece al volver a consultar Profile.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Settings y consultar Profile. Anotar el Full Name inicial en la evidencia de la ejecución. | Profile muestra el nombre inicial de A y ofrece Ok y Cancel. |
| 2. Sustituir Full Name por Prueba T10-01 - nombre descartado y pulsar Cancel. | Se cierra Settings sin aplicar el nombre editado. |
| 3. Volver a abrir Settings / Profile. | Full Name coincide exactamente con el nombre inicial; el texto descartado no aparece como nombre guardado. |
| 4. Conservar evidencia sin contraseñas y cerrar Settings con Cancel. | La cuenta conserva el nombre inicial y no quedan cambios de perfil pendientes. |

**Postcondiciones:** Nombre inicial conservado; correo y Settings sin cambios. Evidencia de la consulta posterior sin secretos.

---

### T10-02. Guardar el nombre y conservarlo tras recarga y nueva sesión

**Importancia:** **high**. Detecta pérdida o aplicación incorrecta de datos de perfil entre consultas y sesiones.

**Requerimiento:** PEB-74 / T10. El nombre guardado persiste tras recarga y nuevo Login.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión del navegador identificados al ejecutar.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba A.
3. Nombre inicial y credenciales vigentes de A disponibles en un registro privado.

**Descripción:** Comprobar el guardado y la persistencia del nombre; al terminar se restaura el valor inicial.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Settings / Profile y anotar el Full Name inicial. | El perfil corresponde a A y muestra su nombre inicial. |
| 2. Introducir Prueba T10-02 - nombre guardado en Full Name y pulsar Ok. | El guardado termina y Settings se cierra sin aviso de rechazo. |
| 3. Recargar la página y abrir Settings / Profile. | Full Name muestra exactamente Prueba T10-02 - nombre guardado; correo y zona horaria conservan sus valores iniciales. |
| 4. Cerrar Settings con Cancel, pulsar Logout e iniciar sesión nuevamente con las credenciales vigentes de A. | Login permite acceder a la misma cuenta A. |
| 5. Abrir Settings / Profile. | Se conserva Prueba T10-02 - nombre guardado después de la nueva sesión. |
| 6. Restituir el nombre inicial, pulsar Ok, recargar y volver a consultar Profile. | Full Name vuelve al valor inicial; no quedan cambios de nombre de esta prueba. |

**Postcondiciones:** Nombre inicial restaurado y comprobado; correo y configuración temporal sin modificaciones. Sesión A disponible y evidencia de persistencia conservada.

---

### T10-03. Intentar cambiar la contraseña sin indicar la contraseña actual

**Importancia:** **high**. Protege frente a sustitución de credenciales desde una sesión sin acreditar la contraseña actual.

**Requerimiento:** PEB-74 / T10. Un intento de cambio con Old Password vacío se rechaza con Invalid Password y conserva la credencial vigente.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión del navegador identificados al ejecutar.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba A.
3. Contraseña vigente y contraseña alternativa de prueba conocidas únicamente por quien ejecuta; registro privado disponible.

**Descripción:** Comprobar el rechazo observado para Old Password vacío con New Password informado y verificar después que la credencial vigente se conserva.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Settings / Profile sin modificar nombre, correo ni configuración temporal. | Se muestran Old Password y New Password; no hay campo de confirmación en Settings. |
| 2. Dejar Old Password vacío, introducir personalmente una contraseña alternativa en New Password y pulsar Ok una sola vez. | Aparece un aviso con el texto exacto Invalid Password; el intento no debe sustituir la credencial vigente. |
| 3. Cerrar el aviso con OK y descartar los campos editados con Cancel en Settings. | Se cierra el aviso y luego Settings; la entrada alternativa queda descartada. |
| 4. Pulsar Logout e iniciar sesión con el correo y la contraseña vigentes antes del intento. | Login permite acceder a A con la credencial inicial; no se necesita la contraseña alternativa rechazada. |
| 5. Consultar Profile y conservar evidencia sin secretos. | Se mantienen la identidad y los valores iniciales de A; la evidencia del aviso no revela contraseñas. |

**Postcondiciones:** Contraseña vigente antes del intento conservada y acceso comprobado; nombre, correo y configuración sin cambios. Evidencia del rechazo sin secretos.

---

### T10-04. Settings con Old Password incorrecto muestra Invalid Password y conserva la clave

**Importancia:** **high**. Detecta sustitución de credenciales sin acreditar la contraseña vigente de la cuenta.

**Requerimiento:** PEB-74 / T10. Old Password incorrecto muestra Invalid Password; criterio del equipo: la contraseña vigente conserva el acceso tras el rechazo.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba (cuenta A).
3. Correo y contraseña vigente de A consignados en el registro privado de credenciales.
4. Contraseña vigente de A distinta de **Prueba-T10-04-incorrecta**.
5. Contraseña objetivo de prueba para A, distinta de la vigente, consignada en el registro privado de credenciales.
6. Nombre de perfil y correo de A consignados en el registro privado de referencia.

**Descripción:** Validar que Settings rechaza con el aviso Invalid Password un cambio de contraseña cuyo Old Password no coincide con la vigente y que A sigue accediendo con su contraseña vigente.

| Paso | Resultado esperado |
|---|---|
| 1. Hacer clic en **Settings**. | Se abre **Settings**. |
| 2. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name**, **Email**, **Time zone**, **Old Password**, **New Password** y los botones **Ok** y **Cancel**; no hay campo de confirmación de contraseña. |
| 3. Escribir **Prueba-T10-04-incorrecta** en el campo **Old Password**. | **Old Password** muestra el valor enmascarado. |
| 4. Escribir en **New Password** la contraseña objetivo de A del registro privado. | **New Password** muestra el valor enmascarado. |
| 5. Hacer clic una sola vez en **Ok**. | Aparece un aviso con el texto exacto **Invalid Password** y el botón **OK**; **Profile** sigue visible detrás del aviso. |
| 6. Tomar una captura del aviso y de **Profile**. | La captura muestra **Invalid Password** con las contraseñas enmascaradas; se conserva como evidencia privada, sin publicar el correo de A. |
| 7. Hacer clic en **OK** del aviso. | Se cierra el aviso y **Profile** sigue abierto. |
| 8. Hacer clic en **Cancel**. | Se cierra **Settings** sin guardar cambios y vuelve a verse el área de proyectos. |
| 9. Hacer clic en **Logout**. | Se muestra la página pública con **Login** y **Sign Up Free**, con la sesión cerrada. |
| 10. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 11. Escribir en **Email** el correo de la cuenta A del registro privado. | **Email** muestra el correo de A. |
| 12. Escribir en **Password** la contraseña vigente de A del registro privado, la misma vigente antes del intento. | **Password** muestra el valor enmascarado. |
| 13. Hacer clic una vez en el botón **Login** del formulario (nombre accesible Submit). | Se muestra el área autenticada con **Settings** y **Logout**; la contraseña vigente sigue dando acceso. |
| 14. Hacer clic en **Settings**. | Se abre **Settings**. |
| 15. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name** y **Email** de la cuenta con sesión iniciada. |
| 16. Comparar **Full Name** con el nombre de perfil de A del registro privado. | **Full Name** coincide con el nombre de A. |
| 17. Comparar **Email** con el correo de A del registro privado. | **Email** coincide con el correo de A del registro privado. |
| 18. Hacer clic en **Cancel**. | Se cierra **Settings** sin guardar cambios y vuelve a verse el área de proyectos. |

**Postcondiciones:** Contraseña vigente de A conservada y acceso comprobado; la contraseña objetivo no se aplicó. Sesión A iniciada, sin cambios de nombre, correo ni zona horaria. Evidencia del rechazo sin contraseñas legibles ni correos publicados.

---

### T10-05. Settings con Old Password vigente cambia la clave y permite Login con la nueva

**Importancia:** **high**. Protege la continuidad del acceso y la invalidación de la credencial reemplazada tras un cambio voluntario.

**Requerimiento:** PEB-74 / T10. Un cambio con Old Password vigente y New Password informado se acepta: Login rechaza la contraseña reemplazada y concede acceso a A con la nueva.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba (cuenta A).
3. Correo y contraseña vigente de A consignados en el registro privado de credenciales.
4. Contraseña objetivo de A distinta de la vigente, consignada en el registro privado; contraseña original como objetivo para el recorrido de restauración.
5. Nombre de perfil, correo y zona horaria de A consignados en el registro privado de referencia.
6. Cuenta A con menos de tres intentos fallidos de Login en la sesión de trabajo, según criterio operativo del equipo (no es una política de Todo.ly).

**Descripción:** Validar que un cambio de contraseña en Settings con Old Password vigente cierra Settings sin aviso de rechazo, que Login rechaza después la contraseña reemplazada y que concede acceso a la identidad de A con la contraseña objetivo.

| Paso | Resultado esperado |
|---|---|
| 1. Hacer clic en **Settings**. | Se abre **Settings**. |
| 2. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name**, **Email**, **Time zone**, **Old Password**, **New Password** y los botones **Ok** y **Cancel**. |
| 3. Comparar **Full Name** con el nombre de perfil de A del registro privado. | **Full Name** coincide con el nombre de A. |
| 4. Comparar **Email** con el correo de A del registro privado. | **Email** coincide con el correo de A del registro privado. |
| 5. Escribir en **Old Password** la contraseña vigente de A del registro privado. | **Old Password** muestra el valor enmascarado. |
| 6. Escribir en **New Password** la contraseña objetivo de A del registro privado. | **New Password** muestra el valor enmascarado. |
| 7. Hacer clic una sola vez en **Ok**. | Se cierra **Settings** sin el aviso **Invalid Password** y vuelve a verse el área de proyectos con **Settings** y **Logout**. No se exige un mensaje de éxito, porque no se observó ninguno. |
| 8. Hacer clic en **Logout**. | Se muestra la página pública con **Login** y **Sign Up Free**, con la sesión cerrada. |
| 9. Hacer clic en **Login** en la página pública. | Se despliega el formulario de acceso con **Email**, **Password**, la casilla **Remember Me** y el botón **Login**. |
| 10. Escribir en **Email** el correo de la cuenta A del registro privado. | **Email** muestra el correo de A. |
| 11. Escribir en **Password** la contraseña reemplazada de A, vigente antes del paso 7, tomada del registro privado. | **Password** muestra el valor enmascarado. |
| 12. Hacer clic una sola vez en el botón **Login** del formulario (nombre accesible Submit). | No se concede acceso y se muestra **Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.** |
| 13. Escribir en **Email** el correo de la cuenta A del registro privado, sustituyendo cualquier contenido del campo. | **Email** muestra el correo de A. |
| 14. Escribir en **Password** la contraseña objetivo de A del registro privado. | **Password** muestra el valor enmascarado. |
| 15. Hacer clic una vez en el botón **Login** del formulario (nombre accesible Submit). | Se muestra el área autenticada con **Settings** y **Logout**. |
| 16. Hacer clic en **Settings**. | Se abre **Settings**. |
| 17. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name**, **Email** y **Time zone** de la cuenta con sesión iniciada. |
| 18. Comparar **Full Name** con el nombre de perfil de A del registro privado. | **Full Name** coincide con el nombre de A. |
| 19. Comparar **Email** con el correo de A del registro privado. | **Email** coincide con el correo de A del registro privado. |
| 20. Comparar **Time zone** con la zona horaria de A del registro privado. | **Time zone** conserva la zona horaria de A del registro privado. |
| 21. Tomar una captura de **Profile**. | La captura muestra la identidad de A con los campos de contraseña sin valores legibles; se conserva como evidencia privada, sin publicar el correo de A. |
| 22. Hacer clic en **Cancel**. | Se cierra **Settings** sin guardar cambios y vuelve a verse el área de proyectos. |
| 23. Anotar en el registro privado la contraseña objetivo como vigente de A. | El registro privado identifica la contraseña objetivo como vigente y la reemplazada como anterior. |

**Postcondiciones:** Contraseña objetivo vigente en A, comprobada por Login, y registro privado actualizado; cuando la objetivo es la original, A queda restaurada sin un segundo cambio de contraseña. Un único intento fallido de Login con la contraseña reemplazada. Nombre, correo y zona horaria sin cambios; sesión A iniciada. Evidencias sin contraseñas legibles ni correos publicados.

---

### T10-06. Profile con Email editado y Cancel conserva el correo original de B

**Importancia:** **high**. Evita pérdida de acceso por aplicar un identificador de cuenta que la persona decidió descartar.

**Requerimiento:** PEB-74 / T10. Cancel descarta una edición de Email en Profile y el correo original de B permanece al reabrir Profile.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión identificados en el registro de ejecución.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba (cuenta B).
3. Correo original de B consignado en el registro privado de referencia.
4. Dirección de correo alternativa elegida por quien ejecuta, distinta del correo original de B, consignada en el registro privado de referencia.
5. Profile de B sin cambios pendientes.

**Descripción:** Validar que, tras sustituir Email por una dirección alternativa y pulsar Cancel sin Ok, Profile de B vuelve a mostrar exactamente el correo original.

| Paso | Resultado esperado |
|---|---|
| 1. Hacer clic en **Settings**. | Se abre **Settings**. |
| 2. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name**, **Email**, **Time zone** y los botones **Ok** y **Cancel**. |
| 3. Comparar **Email** con el correo original de B del registro privado. | **Email** coincide con el correo original de B. |
| 4. Sustituir el contenido de **Email** por la dirección alternativa del registro privado. | **Email** muestra la dirección alternativa. |
| 5. Hacer clic una vez en **Cancel**, sin hacer clic en **Ok**. | Se cierra **Settings** sin guardar cambios y vuelve a verse el área de proyectos. |
| 6. Hacer clic en **Settings**. | Se abre **Settings**. |
| 7. Seleccionar **Profile** en **Settings**. | **Profile** muestra **Full Name** y **Email** de la cuenta con sesión iniciada. |
| 8. Comparar **Email** con el correo original de B del registro privado. | **Email** coincide exactamente con el correo original de B y no muestra la dirección alternativa. |
| 9. Tomar una captura de **Profile**. | La captura muestra **Email** con el correo original de B; se conserva como evidencia privada, sin publicar direcciones reales. |
| 10. Hacer clic en **Cancel**. | Se cierra **Settings** sin guardar cambios y vuelve a verse el área de proyectos. |

**Postcondiciones:** B conserva su correo original y su sesión iniciada; no se envió ningún cambio de Email. Este caso no incluye Login: su objetivo es el descarte de la edición. El cambio válido de Email sigue pendiente en T10-07.

---

### T10-08. Recuperar el acceso de una cuenta registrada mediante su buzón

**Importancia:** **high**. Cubre pérdida de acceso, aplicación de la nueva credencial y conservación de identidad y datos.

**Requerimiento:** PEB-74 / T10. La recuperación de una cuenta registrada permite establecer una nueva contraseña y volver a acceder.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión del navegador identificados al ejecutar.
2. Sin sesión iniciada en Todo.ly en el navegador.
3. Cuenta gratuita de prueba A cuyo buzón controla quien ejecuta; contraseña inicial conocida y otra contraseña de prueba disponibles en registro privado.
4. Nombre inicial y correo de A conocidos por quien ejecuta, con sus valores conservados de forma privada para comprobar identidad.

**Descripción:** Recorrer solicitud, correo, formulario y Login posterior. Las condiciones de seguridad del transporte se evalúan separadamente en T10-10.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Todo.ly, desplegar Login y seleccionar Reset your Password. | Se presenta Enter your email address to reset your password y el control Send. |
| 2. Introducir el correo de A y pulsar Send una vez. | Aparece Info. An email has been sent with a link where you can change your password. |
| 3. Consultar personalmente el buzón controlado y abrir el mensaje Forgot Password correspondiente a esa solicitud; no copiar el token a la evidencia. | Llega un mensaje dirigido a A con instrucciones y enlace de recuperación. No se exige un plazo de recepción no documentado. |
| 4. Abrir el enlace de recuperación tal como llega en el correo, sin cambiar su esquema ni copiar el token a la evidencia. | Se muestra Please Enter a New Password con Enter a New Password, Verify New Password y Done. Si el enlace recibido no carga el formulario, se registra una falla de este caso; HTTPS se evalúa separadamente en T10-10. |
| 5. Introducir personalmente la misma nueva contraseña en ambos campos y pulsar Done; actualizar el registro privado. | Se acepta el envío y A queda accesible; el acceso con la nueva contraseña se confirma en el paso 7. No se exige un aviso literal posterior a Done porque no se observó su texto. |
| 6. Cerrar sesión y realizar un intento de Login con la contraseña reemplazada. | No se concede acceso; se muestra Wrong email or password dentro del aviso de rechazo observado. |
| 7. Iniciar sesión con la nueva contraseña y abrir Settings / Profile. | Acceso a A; Full Name y Email conservan el nombre inicial y el correo de A registrados privadamente antes de la recuperación. |

**Postcondiciones:** Cuenta A accesible con la nueva contraseña, que queda vigente y reflejada en el registro privado; identidad y valores de Profile conservados. Sin token ni contraseñas publicados. La restauración de la contraseña original queda fuera de este caso y se anota en el registro privado; el procedimiento válido de restauración está pendiente de confirmar.

---

### T10-09. Solicitar recuperación con un correo no registrado

**Importancia:** **medium**. Comprueba la alternativa de una solicitud que no identifica una cuenta recuperable.

**Requerimiento:** PEB-74 / T10. La recuperación informa el rechazo de un correo que no pertenece a una cuenta.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión del navegador identificados al ejecutar.
2. Sin sesión iniciada en Todo.ly en el navegador.
3. Dirección reservada para ejemplos sin cuenta en Todo.ly: prueba-t10-no-registrada-20261117@example.com.

**Descripción:** Comprobar el tratamiento observado para la clase correo no registrado, sin consultar ni crear buzones externos.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Todo.ly, desplegar Login y seleccionar Reset your Password. | Se presenta el campo de correo para recuperación y el control Send. |
| 2. Introducir prueba-t10-no-registrada-20261117@example.com y pulsar Send una vez. | Aparece Error. Account with this Email address doesn't exist.; el formulario de recuperación permanece disponible. |
| 3. Conservar evidencia del aviso sin credenciales y cerrar el panel de Login. | No se inicia una sesión ni se modifica ninguna cuenta A o B. |

**Postcondiciones:** Sin sesión ni cambios de cuenta. Evidencia del rechazo conservada. El comportamiento de revelar existencia de cuenta se documenta, sin convertirlo en una auditoría de seguridad.

---

### T10-10. Comprobar HTTPS en el enlace de recuperación recibido

**Importancia:** **high**. Detecta exposición observable del token de recuperación mediante una URL HTTP.

**Requerimiento:** PEB-74 / T10. Criterio del equipo: el enlace de recuperación debe usar HTTPS.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión del navegador identificados al ejecutar.
2. Sin sesión iniciada en Todo.ly en el navegador.
3. Cuenta gratuita de prueba A cuyo buzón controla quien ejecuta.
4. Mensaje de recuperación de A disponible con enlace aún no utilizado; sin otras credenciales visibles en pantalla.

**Descripción:** Examinar el esquema de los enlaces y la indicación de conexión al abrir el enlace directo, sin introducir una nueva contraseña ni interceptar tráfico.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir personalmente el mensaje Forgot Password de la solicitud de A e inspeccionar el esquema de cada enlace de recuperación y su destino visible, sin publicar el token. | Los enlaces de recuperación utilizan HTTPS según el criterio del equipo. Un enlace HTTP constituye una discrepancia a registrar en la ejecución. |
| 2. Abrir el enlace directo recibido en el navegador sin introducir contraseñas; consultar la indicación de conexión de Chrome. | El recorrido de recuperación utiliza una conexión segura; Chrome no presenta Not Secure para la página de recuperación. |
| 3. Registrar esquema e indicador observados en evidencia que oculte el token y cerrar esa pestaña. | La evidencia permite evaluar el criterio sin divulgar el token; no se ha enviado una nueva contraseña ni cambiado la cuenta. |

**Postcondiciones:** Credenciales y datos sin cambios. Resultado del caso pendiente de ejecución formal; hallazgo previo HTTP indicado para confirmar, sin reporte en la planilla de fallas.

---

## Candidatos pendientes — no registrar todavía

---

### T10-07. Cambiar el correo de B a un alias y restaurar el original

**Importancia:** **high**. Protege el acceso y los datos al modificar el identificador de la cuenta.

**Requerimiento:** PEB-74 / T10. Guardar un cambio válido de Email conserva los datos y permite acceso con el identificador vigente.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión del navegador identificados al ejecutar.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba B.
3. Correo original, contraseña vigente y alias nuevo del mismo buzón controlado disponibles para quien ejecuta; el alias no pertenece a otra cuenta.
4. Duda pendiente: requisito de verificación de correo y secuencia de activación del nuevo identificador. Si la interfaz lo exige, buzón controlado y verificación a cargo de quien ejecuta.

**Descripción:** Propuesta pendiente hasta confirmar si el cambio exige verificar por correo. Durante la exploración acotada no se completará esa verificación si se exige.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Settings / Profile y anotar privadamente el correo inicial y un dato representativo de B. | El perfil y los datos corresponden a B. |
| 2. Introducir personalmente el alias en Email y pulsar Ok sin modificar otros campos. | PENDIENTE: confirmar aceptación directa o solicitud de verificación. No fijar activación inmediata mientras esa regla sea desconocida. |
| 3. Una vez confirmada la regla, seguir únicamente su flujo válido y volver a consultar Profile tras recarga. | PENDIENTE: definir el punto exacto en que el alias pasa a ser el identificador vigente; los datos de B se conservan. |
| 4. Comprobar Login con el identificador vigente conforme al flujo confirmado. | Acceso a la misma B con sus datos; resultado sobre el identificador anterior pendiente de la regla observada. |
| 5. Restaurar personalmente el correo original por el flujo válido, actualizar el registro privado y comprobar Login. | B queda accesible con su correo original y conserva la contraseña y los datos iniciales. |

**Postcondiciones:** Correo original de B restaurado y registro privado coherente. Caso pendiente: no registrar como listo con resultados principales condicionales.
