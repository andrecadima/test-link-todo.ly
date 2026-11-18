<!-- BORRADOR: publicar solo después de revisión y registro verificado. -->

# T10 / PEB-74 — Perfil, credenciales y recuperación de acceso

## 1. Análisis del área

Se analizaron Settings / Profile, guardado con Ok, descarte con Cancel y recuperación: Login → Reset your Password → Send → correo Forgot Password → formulario → nuevo Login. Entorno: Chrome157.0.8103.51/macOS26.6.2, cuentas gratuitas propias A/B y navegador aislado; exploración, sin ejecución formal.

Profile ofrece Full Name, Email, Time zone, Old Password y New Password; **sin confirmación de contraseña**. Recuperación sí ofrece Enter a New Password, Verify New Password y Done. Se comprobaron nombre guardado/descartado, persistencia tras recarga y nombre inicial restaurado tras nueva sesión; recuperación de A y contraste de claves; recuperación inexistente rechazada.

El18/11: a) Old incorrecto→Invalid Password; b) cambio válido desde Settings/restauración, reemplazada rechazada y original aceptada con identidad conservada; c) Email editado de B descartado por Cancel conserva original. Capturas manuales y contraste posterior en registro de exploración. No se inventa mensaje de éxito. Email válido07 y New Password vacío pendientes. Zona horaria, vencimientos, eliminación de cuenta y funciones Pro quedan fuera; sesión completa en T09.

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

| Regla o duda | Clasificación | Fundamento |
|---|---|---|
| Ok guarda el nombre y Cancel conserva el anterior; tras recarga persiste el nombre de prueba y tras nueva sesión se conserva el nombre inicial restaurado | Comportamiento observado | `exploracion.md`, consultas de Profile del 17/11; no se atribuye a una nueva sesión el texto temporal |
| Un nombre guardado conserva su valor en nuevas sesiones | Criterio del equipo | Encargo de persistencia del usuario; T10-02 contrasta el valor de prueba en ese recorrido |
| Settings tiene Old Password y New Password, sin confirmación | Comportamiento observado | Consulta del formulario del 17/11 |
| Old Password vacío con New Password informado muestra `Invalid Password` | Comportamiento observado | Captura aportada por el usuario del 17/11 a las 14:38; la conservación posterior se contrastó por Login y Profile con la misma credencial previa |
| Old Password incorrecto con New Password informado muestra `Invalid Password` | Comportamiento observado | Contraste manual a), 18/11, 15:56: aviso con Profile detrás. |
| La contraseña vigente conserva el acceso tras el rechazo de Old Password incorrecto | Criterio del equipo | Respaldo indirecto: b) aceptó la vigente inmediatamente después. Login directo tras a) no se observó; T10-04 lo comprueba en ejecución. |
| Old Password vigente con New Password informado: Settings se cierra sin aviso de rechazo ni mensaje literal de éxito | Comportamiento observado | Contraste b) 15:58; captura manual 18/11,15:58 (Work autenticada). No se inventa un mensaje de éxito |
| Tras el cambio válido, Login rechaza la contraseña reemplazada con `Error. Wrong email or password. Please try again. Forgot your password? You can retrieve it using the form below.` y acepta la nueva, conservando la identidad de A | Comportamiento observado | Un único intento, aviso transitorio leído por AX (`contraste-restauracion.txt`); Login aceptado y Profile en `verificacion/restauracion-A-AX.txt` y `evidencias/2026-11-18_T10_Login-original-A-verificado.png` |
| Old Password debe corresponder a la vigente para aceptar un cambio | Criterio del equipo, ya contrastado | Ajuste 5 expreso del usuario; vacío, incorrecto y vigente observados (03/04/05) |
| New Password vacío en Settings | Duda pendiente | No observado; no se diseña su rechazo ni su aceptación |
| Email editado y descartado con Cancel conserva el correo original al reabrir Profile | Comportamiento observado | Contraste c) en B, 15:59; captura manual 18/11,15:59 y comparación AX con el registro privado. La dirección alternativa es distinta del original; no se afirma que sea alias del mismo buzón. No se hizo Login de B en ese recorrido |
| Cambio válido de Email y necesidad de verificación por correo | Duda pendiente | No observado; T10-07 se conserva fuera del registro |
| Para recuperación registrada se muestra `Info. An email has been sent with a link where you can change your password.` | Comportamiento observado | Solicitud de A, mensaje recibido y formulario leído |
| La recuperación completada permite Login con la nueva contraseña y rechaza la reemplazada | Comportamiento observado | Cambio manual del usuario y dos contrastes posteriores de Login |
| Un correo no registrado produce `Error. Account with this Email address doesn't exist.` | Comportamiento observado | Correo reservado example.com, captura y lectura de interfaz |
| El enlace recibido, abierto tal como llega, debe mostrar Please Enter a New Password | Criterio del equipo | Corrección expresa del usuario del 17/11, documentada en exploracion.md, Ajustes del usuario antes de registro; no se atribuye a una carga HTTP observada |
| El enlace de recuperación debe usar HTTPS | Criterio del equipo | Instrucción expresa del usuario del 17/11; caso T10-10 |
| El correo entregó HTTP y Chrome mostró Not Secure al abrir el enlace directo; la misma ruta por HTTPS cargó el formulario | Comportamiento observado | `hallazgos.md`; hallazgo para confirmar en ejecución, sin reporte en planilla |
| Plazos de recepción/caducidad, uso único, política de longitud/complejidad y cierre de otras sesiones | Duda pendiente | Sin regla confirmada; no trasladar los límites de los ejemplos docentes |
| Precondiciones describen estados; no contienen acciones ni datos reales de cuenta | Regla documentada / decisión vigente | Decisiones §7 y guía de diseño |

## 4. Tipos de prueba y escenarios seleccionados

| Tipo | Objetivo y pertinencia | Procedimiento | Criterio observable |
|---|---|---|---|
| Funcional | Guardado/descarte, persistencia y continuidad del acceso; R1–R4 y R6 | Contrastar Profile antes/después, recarga, Logout/Login y recuperación con buzón controlado | Valores exactos conservados o modificados según la acción; acceso con identificador/credencial vigentes |
| Seguridad observable | Transporte del enlace que autoriza recuperación; R5 | Inspeccionar esquema de enlaces del correo y conexión visible en Chrome sin interceptar tráfico ni enviar contraseña por HTTP | HTTPS en el enlace y conexión segura al formulario según criterio del equipo |

Positivos: guardar nombre, cambio válido de contraseña desde Settings (T10-05), recuperar una cuenta propia. Negativos: recuperación con correo inexistente, Old Password vacío y Old Password incorrecto, con rechazos observados. Alternativos: Cancel del nombre y Cancel del Email (T10-06). El cambio válido de Email queda pendiente de su regla de activación. No se añade compatibilidad Firefox ni accesibilidad completa sin exploración y objetivo concreto; observar un mensaje comprensible no constituye por sí solo una prueba no funcional de usabilidad.

## 5. Técnicas aplicadas y artefactos

Definiciones del original `E Tecnicas de Black Box Testing 2025.pdf`, ya leídas en fase 0: particiones pp. 8–19, tablas de decisión pp. 45–56 y casos de uso pp. 58–66. No se releyó completo el PDF.

### 5.1 Particiones de equivalencia

Una clase agrupa datos con el mismo tratamiento esperado; se elige un representante. No se crean clases por nombres arbitrarios ni por valores de contraseña todavía sin regla.

| Variable | Clase / tratamiento | Válida o inválida para la operación | Representante genérico | Caso y estado |
|---|---|---|---|---|
| Correo solicitado en recuperación | Correo de una cuenta registrada: solicitud aceptada y mensaje al buzón | Válida | Correo de A, conocido por quien ejecuta | T10-08, regla observada |
| Correo solicitado en recuperación | Correo sin cuenta: rechazo explícito | Inválida para recuperar una cuenta | `prueba-t10-no-registrada-20261117@example.com` | T10-09, regla observada |
| Credencial en Login posterior a recuperación | Contraseña vigente: acceso a A | Válida | Nueva contraseña privada de A | T10-08, contraste del flujo de recuperación |
| Credencial en Login posterior a recuperación | Contraseña reemplazada: rechazo | Inválida | Contraseña privada anterior de A | T10-08, contraste del flujo de recuperación |
| Old Password al cambiar desde Settings | Vacío con New Password informado: aviso Invalid Password | Inválida, rechazo observado | Campo vacío y alternativa privada no vacía | T10-03, rechazo y conservación de acceso observados |
| Old Password al cambiar desde Settings | No coincide con la vigente: aviso Invalid Password | Inválida, rechazo observado | `Prueba-T10-04-incorrecta` | T10-04 |
| Old Password al cambiar desde Settings | Coincide con la vigente: cambio aceptado | Válida, aceptación observada | Contraseña vigente privada | T10-05 |
| New Password al cambiar desde Settings | Informado | Válida para las tres reglas observadas | Contraseña alternativa u objetivo privada | T10-03/04/05 |
| New Password al cambiar desde Settings | Vacío | **Duda pendiente**, sin caso | — | Sin caso |
| Credencial en Login posterior al cambio desde Settings | Contraseña reemplazada: rechazo / contraseña objetivo: acceso a A | Inválida / válida | Anterior y objetivo privadas | T10-05 |
| Email en Profile antes de Cancel | Dirección alternativa distinta del original, descartada | Edición descartada: se conserva el original | Dirección alternativa indicada por la persona usuaria | T10-06 |

### 5.2 Tabla de decisión de Change Password en Settings

Formato docente: condiciones arriba, acciones abajo y columnas como reglas. **N.A.** indica que la condición no se evalúa porque no hay valor que comparar. Las tres reglas son combinaciones observadas el 17/11 y el 18/11; la combinación con New Password vacío no se incluye porque no se observó (duda pendiente) y no se completa la tabla con resultados inventados.

| Condiciones / acciones | R1 | R2 | R3 |
|---|---|---|---|
| C1: Old Password informado | No | Sí | Sí |
| C2: Old Password coincide con la vigente | N.A. | No | Sí |
| C3: New Password informado | Sí | Sí | Sí |
| **Mostrar Invalid Password y conservar la vigente** | X | X | — |
| **Aceptar el cambio: Settings se cierra; Login rechaza la reemplazada y acepta la nueva** | — | — | X |
| **Caso derivado** | T10-03 | T10-04 | T10-05 |

La conservación de la vigente en R1 se contrastó por Login (17/11); en R2 es criterio de seguridad del equipo respaldado de forma indirecta, porque el Old Password vigente fue aceptado inmediatamente después en R3. T10-04 incorpora el Login con la vigente para comprobarlo directamente en ejecución.

### 5.3 Flujos de casos de uso

**UC1 — Editar nombre.** Actor: persona con sesión A. Flujo principal: A abre Profile; S muestra valores; A edita Full Name y pulsa Ok; S conserva el nombre; A recarga y abre nueva sesión; S muestra el valor guardado. Alternativa: A pulsa Cancel y S conserva el anterior. Recorridos derivados: **T10-02 principal; T10-01 alternativa**. El flujo incluye restauración del dato al terminar.

**UC2 — Recuperar acceso.** Actor: persona que controla el buzón de A. Principal: A abre Reset your Password e informa su correo; S confirma envío; A consulta el buzón y abre el enlace tal como llega; S ofrece formulario; A introduce personalmente y confirma nueva contraseña; S permite acceso con ella; A contrasta credencial reemplazada y datos de A. Alternativa: correo sin cuenta → S rechaza la solicitud y mantiene el formulario. Derivación: **T10-08 principal y T10-09 alternativa**. La comprobación de HTTPS se separa como objetivo de seguridad observable **T10-10**, derivado del punto de entrega/apertura del enlace y del criterio expreso del equipo.

**UC3 — Cambiar contraseña desde Settings.** Actor: persona con sesión A. Principal: A abre Profile, informa la contraseña vigente en Old Password y la objetivo en New Password y pulsa Ok; S cierra Settings sin aviso de rechazo; A cierra sesión e intenta una vez Login con la reemplazada; S lo rechaza; A inicia sesión con la objetivo; S concede acceso y Profile conserva la identidad; A actualiza su registro privado. Cuando la objetivo es la original, este mismo recorrido restaura A, sin un segundo cambio. Alternativas: Old Password incorrecto → Invalid Password y la vigente sigue dando acceso; Old Password vacío → Invalid Password. Derivación: **T10-05 principal; T10-04 y T10-03 alternativas**, coincidentes con las reglas R3, R2 y R1 de la tabla 5.2.

**UC4 — Editar Email de B.** Actor: persona con sesión B. Alternativa observada: B sustituye Email por una dirección alternativa y pulsa Cancel; S cierra Settings y, al reabrir Profile, muestra el correo original → **T10-06**. Principal: B guarda un Email nuevo y S lo aplica con la activación que corresponda → **T10-07, pendiente**: la necesidad de verificar el correo y el momento de activación no se observaron; no se impone una secuencia no observada.

### 5.4 Técnicas no aplicadas

No se aplican valores límite: no hay una frontera real confirmada de longitud ni una granularidad establecida. La tabla de decisión se reserva para Change Password, donde tres condiciones combinadas producen resultados distintos; no se fuerza sobre guardar/cancelar del nombre o del Email, que se representan como casos de uso, conforme a la guía §7.4. No se aplica transición formal de estados. La sesión y Remember Me se modelan en T09; raíz/subproyecto corresponde a T11.

## 6. Lista resumida de casos

| Caso | Objetivo / riesgo cubierto | Fundamento de la técnica | Importancia | TestLink | Situación actual |
|---|---|---|---|---|---|
| T10-01 Cancelar nombre | Descartar una edición; R3 | Alternativa Cancel del UC1, ya contrastada | medium | [TL-66](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-66) | Registrado y comparado. |
| T10-02 Guardar nombre y persistir | Evitar pérdida del perfil; R2 | Principal UC1 con recarga y nueva sesión | high | [TL-67](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-67) | Registrado y comparado. |
| T10-03 Old Password vacío | Proteger cambio de credencial; R1 | Partición inválida vacío y alternativa UC3; aviso Invalid Password observado | high | [TL-68](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-68) | Registrado y comparado. |
| T10-04 Old Password incorrecto | Proteger cambio de credencial; R1 | Regla R2 de la tabla 5.2, partición no coincide y alternativa UC3 | high | Sin ID | Listo; sin ID todavía |
| T10-05 Cambio válido desde Settings | Continuidad del acceso e invalidación de la reemplazada; R1 | Regla R3 de la tabla 5.2, partición coincide y principal UC3; sirve como restauración | high | Sin ID | Listo; sin ID todavía |
| T10-06 Cancelar correo | Conservar identificador descartado; R3 | Alternativa Cancel del UC4 | high | Sin ID | Listo; sin ID todavía |
| T10-07 Cambiar correo a alias y restaurar | Evitar pérdida de acceso/datos; R4 | Principal UC4 | high | No registrado | Pendiente de verificación/activación |
| T10-08 Recuperar acceso | Acceso con credencial nueva; R1 | Particiones de correo/credencial y UC2 principal | high | [TL-69](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-69) | Registrado y comparado. |
| T10-09 Correo no registrado | Distinguir rechazo de envío aceptado; R6 | Partición sin cuenta y alternativa UC2 | medium | [TL-70](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-70) | Registrado y comparado. |
| T10-10 HTTPS del enlace | Transporte del token; R5 | Procedimiento observable sobre entrega/apertura del UC2, criterio del equipo | high | [TL-71](http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-71) | Registrado y comparado. |

## 7. Implementación en TestLink

Se registraron **seis casos, 28 pasos**, en **TL:Todo.ly → Todo.ly tests (id3)**: TL-66 a TL-71. Suite:64 antes,70 después; sin T10 previo, duplicados omitidos por nombre, sin suites nuevas ni actualización de existentes. Cada título, Summary, Preconditions, paso/resultado, Importance y Manual fue cotejado: **sin diferencias**. Estado TestLink **Draft**.

T10-04/05/06: **listos para registro**,51pasos; revisión independiente08 APTO, observaciones atendidas. Se incorporarán únicamente estos tres y sus IDs se añadirán tras verificarlos. T10-07 queda fuera. La revisión independiente no sustituye la de otro integrante.

La exploración fue macOS/Chrome; guía§10 prevé ejecución Windows/Chrome con versiones reales anotadas. T10-10 requiere enlace no utilizado: antes de T10-08 o con solicitud propia. Evidencias externas: árbol y ficha genérica TestLink; no capturas de Profile con correos reales. Exportación real y extracción por ticket pendientes del cierre.

Comentario [PEB-74 / 10226](https://alesalve.atlassian.net/browse/PEB-74?focusedCommentId=10226): tres capturas conservadas (árbol global, TL-66 abierto y filtro de seis casos), tablas legibles con desplazamiento horizontal. Estado Jira conservado.

## 8. Cobertura pendiente y límites

Pendientes: cambio válido de Email de B, New Password vacío en Settings, política de contraseña, fronteras de campos, token de uso único/caducidad y sesiones paralelas. Los pasos manuales a/b/c se realizaron el 18/11 y completaron T10-04/05/06; la restauración de la contraseña original de A quedó hecha y verificada mediante el cambio b), y el registro privado se actualizó. T10-07 se conserva exclusivamente como cobertura pendiente y no se registra, por instrucción expresa. No se afirma que el producto exija verificación de correo: esa regla no se alcanzó a consultar mediante un cambio válido. Los cuatro PDF faltantes se excluyen expresamente como fuentes por instrucción del usuario.

El nombre vacío se envió una vez con credenciales de cambio vacías: la vista quedó en Loading y una nueva consulta conservó el nombre inicial de A. No hubo una validación visible fiable; no se establece obligatoriedad ni se genera un caso de rechazo basándose solo en ese intento. No se repite la exploración para buscar límites arbitrarios.

No se reporta el hallazgo HTTP en la planilla de fallas: el comentario lo dejará para confirmar durante la ejecución. La revisión por otro integrante permanece pendiente y no se marcará por el agente.

## 9. Estado

**Nueve casos diseñados: seis registrados en TestLink (T10-01/02/03/08/09/10) y tres por registrar (T10-04/05/06) hasta su registro y verificación; pendiente de revisión por otro integrante.** T10-07 está excluido del registro; **la cobertura completa de T10 no está terminada**. No se ejecutaron formalmente los casos ni se reportó el hallazgo HTTP en la planilla de fallas.

Comprobación de criterios de aceptación, sin modificar el checklist ni el estado del ticket:

| Criterio | Situación |
|---|---|
| Reglas y restricciones documentadas | Documentadas, con dudas explícitas. |
| Tipos de prueba seleccionados y justificados | Funcional y seguridad observable, vinculados a riesgos. |
| Riesgos de pérdida de acceso y modificación incorrecta | R1–R6 trazados; Settings03/04/05 y Cancel06 cubiertos; Email válido07 pendiente. |
| Cambios válidos, inválidos y cancelaciones | Nombre, recuperación, contraseña y Cancel cubiertos; Email válido pendiente. |
| Técnicas y procedimientos justificados | Particiones, decisión y flujos con artefactos/trazas; sin límites inventados. |
| Cuentas, buzones, condiciones y resultados en los casos | Fichas genéricas; única contraseña literal: dato sintético inválido de04. |
| Registro en TestLink y revisión de otro integrante | Seis registrados, tres por registrar; revisión de integrante pendiente. |
