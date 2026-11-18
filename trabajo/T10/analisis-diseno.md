# T10 / PEB-74 — Perfil, credenciales y recuperación de acceso

Fecha: 17 de noviembre de 2026; actualizado el 18 de noviembre de 2026 con los contrastes manuales a/b/c. **OK del usuario recibido; revisión independiente (encargo 04) APTO para los seis casos confirmados, con observaciones resueltas/documentadas antes del registro.** Seis casos registrados y comparados en TestLink; comentario Jira 10226 publicado y comprobado el 18/11/2026. **Nueve casos diseñados:** seis registrados (T10-01/02/03/08/09/10) y tres listos para registro (T10-04/05/06), sin ID de TestLink hasta su registro y verificación. La exploración adicional comenzó a las 15:51 UTC; el presupuesto aproximado de una hora corresponde al trabajo activo. La espera entre el traspaso manual y la respuesta del usuario se registra separadamente. Las fichas de este archivo se generan a partir de `casos.json`, manteniendo los campos acordados. `casos-listos.json` contiene los nueve casos diseñados (los seis registrados sin modificar y los tres nuevos); `casos-pendientes.json` conserva únicamente T10-07, que no se importará. Los códigos se conservan para trazabilidad, aunque la lista registrable no sea consecutiva.

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

## Fichas para TestLink — seis casos registrados y tres listos para registro

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
