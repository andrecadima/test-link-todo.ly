<!-- BORRADOR: publicar solo después de revisión y registro verificado. -->

# T10 / PEB-74 — Perfil, credenciales y recuperación de acceso

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
