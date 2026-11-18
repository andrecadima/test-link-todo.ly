# T10 / PEB-74 — Perfil, credenciales y recuperación de acceso

Fecha: 17 de noviembre de 2026. **OK del usuario recibido; revisión independiente 04 APTO para los seis casos confirmados, con observaciones resueltas/documentadas antes del registro.** No registrado en TestLink ni publicado en Jira. La exploración adicional comenzó a las 15:51 UTC; el presupuesto aproximado de una hora corresponde al trabajo activo. La espera entre el traspaso manual y la respuesta del usuario se registra separadamente. Las fichas de este archivo se generan a partir de `casos.json`, manteniendo los campos acordados. `casos-listos.json` delimita los seis casos propuestos para registro; `casos-pendientes.json` conserva cuatro candidatos que no se importarán como listos. Los códigos se conservan para trazabilidad, aunque la lista registrable no sea consecutiva.

## 1. Análisis del área

Se analizaron Settings / Profile, el guardado con Ok, el descarte con Cancel y el flujo Login → Reset your Password → Send → mensaje Forgot Password → formulario de nueva contraseña → acceso posterior. La exploración se realizó con las cuentas gratuitas A y B propias de la práctica, en Chrome 157.0.8103.51 sobre macOS 26.6.2, perfil aislado. No constituye ejecución formal de casos.

Profile ofrece Full Name, Email, Time zone, Old Password y New Password. **Settings no ofrece un campo de confirmación de contraseña.** El formulario de recuperación sí ofrece Enter a New Password y Verify New Password, con Done. Por ello no se fabrica una validación de confirmación distinta dentro de Settings.

Se observaron Cancel del nombre, guardado y persistencia tras recarga del nombre de prueba. Tras una nueva sesión se verificó la persistencia del nombre inicial restaurado mediante Ok, no la del texto temporal de prueba. La recuperación de A fue completada manualmente por el usuario; el Login posterior rechazó la contraseña reemplazada y aceptó la nueva, conservando la identidad de A. El correo no registrado produjo rechazo explícito. La captura manual de las 14:38 muestra Invalid Password con Old Password vacío y New Password informado. Posteriormente se descartó el formulario y se verificó Login con la misma contraseña vigente antes del intento, confirmando identidad A en Profile. Continúan pendientes el contraste de contraseña incorrecta, el cambio válido desde Settings y el cambio de Email.

No se incluyen zona horaria, vencimientos, eliminación de cuenta, funciones Pro, auditoría de penetración ni tiempos de respuesta sin umbral documentado. Los datos de sesión se usan para comprobar persistencia del perfil; la cobertura completa de sesión corresponde a T09.

## 2. Riesgos que orientan el diseño

Valoración cualitativa de diseño, no frecuencia medida: probabilidad P baja=1/media=2/alta=3; impacto I bajo=1/medio=2/alto=3; nivel P×I, alto=6–9, medio=3–4 y bajo=1–2. Se priorizan acceso y transporte de recuperación.

| Riesgo | Consecuencia para la persona usuaria | P y fundamento | I | Nivel | Casos |
|---|---|---|---|---|---|
| R1: cambio o recuperación deja credenciales incoherentes | Pérdida de acceso o contraseña anterior todavía utilizable | 2: secuencia con cambios persistentes y Login posterior | 3 | 6, alto | T10-03, 04, 05, 08 |
| R2: guardado del nombre no persiste o altera otro campo | Perfil incorrecto tras recarga o nueva sesión | 2: estado editado/guardado y consultas posteriores | 2 | 4, medio | T10-02 |
| R3: Cancel aplica una edición descartada | Nombre o identificador de acceso cambiado involuntariamente | 2: mismo formulario con dos salidas de edición | 3 | 6, alto | T10-01, 06 |
| R4: Email nuevo desliga datos o impide acceso | Pérdida de acceso a B o identificación incorrecta de sus datos | 2: identificador persistente con activación aún desconocida | 3 | 6, alto | T10-07 |
| R5: token de recuperación se entrega mediante HTTP | Exposición potencial de un enlace que autoriza restablecer credenciales | 3: enlace HTTP ya observado, pendiente confirmar en ejecución | 3 | 9, alto | T10-10 |
| R6: alternativa de recuperación para correo inexistente resulta confusa | La persona no distingue rechazo de solicitud aceptada | 2: resultado alternativo observable y distinto del válido | 2 | 4, medio | T10-09 |

## 3. Reglas, restricciones y dudas

| Regla o duda | Clasificación | Fundamento |
|---|---|---|
| Ok guarda el nombre y Cancel conserva el anterior; tras recarga persiste el nombre de prueba y tras nueva sesión se conserva el nombre inicial restaurado | Comportamiento observado | `exploracion.md`, consultas de Profile del 17/11; no se atribuye a una nueva sesión el texto temporal |
| Un nombre guardado conserva su valor en nuevas sesiones | Criterio del equipo | Encargo de persistencia del usuario; T10-02 contrasta el valor de prueba en ese recorrido |
| Settings tiene Old Password y New Password, sin confirmación | Comportamiento observado | Consulta del formulario del 17/11 |
| Old Password vacío con New Password informado muestra `Invalid Password` | Comportamiento observado | Captura aportada por el usuario del 17/11 a las 14:38; la conservación posterior se contrastó por Login y Profile con la misma credencial previa |
| Old Password incorrecto y cambio válido desde Settings | Duda pendiente | Segundo contraste manual y restauración solicitados; no confundir el rechazo de vacío con el de incorrecto |
| Old Password debe corresponder a la vigente para aceptar un cambio | Criterio del equipo | Ajuste 5 expreso del usuario. Vacío ya observado; mensaje de incorrecto y aceptación válida se completan con a/b |
| Cancel específico de Email y cambio válido a alias sin verificar por correo | Duda pendiente | No atribuir a Email el contraste realizado únicamente con Full Name |
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

Positivos: guardar nombre, cambio válido de credencial cuando quede confirmado, recuperar una cuenta propia. Negativos: recuperación con correo inexistente y Old Password vacío, con rechazos observados; Old Password incorrecto sigue sujeto a confirmación. Alternativos: Cancel y vuelta al estado inicial. El cambio de Email queda pendiente de su regla de activación. No se añade compatibilidad Firefox ni accesibilidad completa sin exploración y objetivo concreto; observar un mensaje comprensible no constituye por sí solo una prueba no funcional de usabilidad.

## 5. Técnicas aplicadas y artefactos

Definiciones del original `E Tecnicas de Black Box Testing 2025.pdf`, ya leídas en fase 0: particiones pp. 8–19 y casos de uso pp. 58–66. No se releyó completo el PDF.

### 5.1 Particiones de equivalencia

Una clase agrupa datos con el mismo tratamiento esperado; se elige un representante. No se crean clases por nombres arbitrarios ni por valores de contraseña todavía sin regla.

| Variable | Clase / tratamiento | Válida o inválida para la operación | Representante genérico | Caso y estado |
|---|---|---|---|---|
| Correo solicitado en recuperación | Correo de una cuenta registrada: solicitud aceptada y mensaje al buzón | Válida | Correo de A, conocido por quien ejecuta | T10-08, regla observada |
| Correo solicitado en recuperación | Correo sin cuenta: rechazo explícito | Inválida para recuperar una cuenta | `prueba-t10-no-registrada-20261117@example.com` | T10-09, regla observada |
| Credencial en Login posterior a recuperación | Contraseña vigente: acceso a A | Válida | Nueva contraseña privada de A | T10-08, contraste del flujo de recuperación |
| Credencial en Login posterior a recuperación | Contraseña reemplazada: rechazo | Inválida | Contraseña privada anterior de A | T10-08, contraste del flujo de recuperación |
| Old Password al cambiar desde Settings | Vacío con New Password informado: aviso Invalid Password | Inválida, rechazo observado | Campo vacío y alternativa privada no vacía | T10-03, rechazo y conservación de acceso observados |
| Old Password al cambiar desde Settings | No coincide / coincide con la actual | Resultado pendiente de contraste | Un valor distinto; valor vigente privado | T10-04/05, **particiones candidatas** |

### 5.2 Flujos de casos de uso

**UC1 — Editar nombre.** Actor: persona con sesión A. Flujo principal: A abre Profile; S muestra valores; A edita Full Name y pulsa Ok; S conserva el nombre; A recarga y abre nueva sesión; S muestra el valor guardado. Alternativa: A pulsa Cancel y S conserva el anterior. Recorridos derivados: **T10-02 principal; T10-01 alternativa**. El flujo incluye restauración del dato al terminar.

**UC2 — Recuperar acceso.** Actor: persona que controla el buzón de A. Principal: A abre Reset your Password e informa su correo; S confirma envío; A consulta el buzón y abre el enlace tal como llega; S ofrece formulario; A introduce personalmente y confirma nueva contraseña; S permite acceso con ella; A contrasta credencial reemplazada y datos de A. Alternativa: correo sin cuenta → S rechaza la solicitud y mantiene el formulario. Derivación: **T10-08 principal y T10-09 alternativa**. La comprobación de HTTPS se separa como objetivo de seguridad observable **T10-10**, derivado del punto de entrega/apertura del enlace y del criterio expreso del equipo.

**UC3 — Cambiar contraseña desde Settings, pendiente.** Principal candidato: A acredita contraseña vigente y propone otra; S acepta; A verifica acceso y restaura el estado inicial. Alternativa observada: Old Password vacío → aviso Invalid Password, **T10-03**. Alternativa incorrecto y principal válido pendientes de contraste: **T10-04/05**, aún no listos para registro definitivo.

**UC4 — Editar Email de B, pendiente.** Flujo propuesto: B edita a alias de su propio buzón, guarda y verifica persistencia/acceso; alternativa Cancel conserva el original; cierre restaura el correo. **T10-06/07**. La necesidad de verificar el correo y el momento de activación siguen pendientes; no se impone una secuencia de activación no observada.

### 5.3 Técnicas no aplicadas

No se aplican valores límite: no hay una frontera real confirmada de longitud ni una granularidad establecida. No se fuerza tabla de decisión ni transición formal de estados sobre guardar/cancelar; los recorridos simples de edición se representan como casos de uso, conforme a la guía §7.4. La sesión y Remember Me se modelan en T09; raíz/subproyecto corresponde a T11.

## 6. Lista resumida de casos

| Caso | Objetivo / riesgo cubierto | Fundamento de la técnica | Importancia | Situación actual |
|---|---|---|---|---|
| T10-01 Cancelar nombre | Descartar una edición; R3 | Alternativa Cancel del UC1, ya contrastada | medium | Preparado |
| T10-02 Guardar nombre y persistir | Evitar pérdida del perfil; R2 | Principal UC1 con recarga y nueva sesión | high | Preparado |
| T10-03 Old Password vacío | Proteger cambio de credencial; R1 | Partición inválida vacío y alternativa UC3; aviso Invalid Password observado | high | Preparado; rechazo y conservación de acceso observados |
| T10-04 Old Password incorrecto | Proteger cambio de credencial; R1 | Partición candidata no corresponde y alternativa UC3 | high | Pendiente de regla/resultado |
| T10-05 Cambio válido desde Settings | Continuidad del acceso; R1 | Principal UC3, contraste antes/después y reversión | high | Pendiente de exploración |
| T10-06 Cancelar correo | Conservar identificador descartado; R3 | Alternativa UC4 | high | Pendiente de contraste específico |
| T10-07 Cambiar correo a alias y restaurar | Evitar pérdida de acceso/datos; R4 | Principal UC4 | high | Pendiente de verificación/activación |
| T10-08 Recuperar acceso | Acceso con credencial nueva; R1 | Particiones de correo/credencial y UC2 principal | high | Preparado; nueva credencial queda vigente y registrada privadamente |
| T10-09 Correo no registrado | Distinguir rechazo de envío aceptado; R6 | Partición sin cuenta y alternativa UC2 | medium | Preparado |
| T10-10 HTTPS del enlace | Transporte del token; R5 | Procedimiento observable sobre entrega/apertura del UC2, criterio del equipo | high | Preparado; hallazgo a confirmar en ejecución |

## 7. Implementación en TestLink

**OK del usuario recibido; revisión independiente 04 APTO para seis casos, sin bloqueantes.** Destino: proyecto TL:Todo.ly, suite existente Todo.ly tests, nombres T10-NN, Importance individual y ejecución Manual; Summary con requerimiento/descripción/postcondiciones, Preconditions separado y pasos nativos. XML de entrada con raíz testcases, sin IDs, nuevas suites ni actualización de existentes. No hay registro comprobado todavía.

La exploración se realizó en macOS; la ejecución prevista por la guía §10 es Windows con Chrome, cuya versión y sistema deben identificarse al ejecutar. T10-10 necesita un enlace no utilizado: se ejecuta antes de consumirlo con T10-08 o mediante una solicitud propia, sin reutilizar un token consumido.

El comentario final de Jira contendrá la lista resumida con IDs y enlaces reales y las capturas de registro; las fichas completas estarán en TestLink. La exportación real será testlink-xml/todo-ly-tests.xml y el XML T10 se extraerá de ella mediante script. Los candidatos con resultado principal pendiente no se presentarán como casos listos ni se registrarán sin resolverlos.

## 8. Cobertura pendiente y límites

Pendientes: Old Password incorrecto, cambio válido desde Settings, restauración de A, Email de B, política de contraseña, fronteras de campos, token de uso único/caducidad y sesiones paralelas. Se solicitaron al usuario los pasos manuales a/b/c en un único bloque para completar T10-04/05/06. T10-07 se conserva exclusivamente como cobertura pendiente y no se registra, por instrucción expresa. No se afirma que el producto exija verificación de correo: esa regla no se alcanzó a consultar mediante un cambio válido. Los cuatro PDF faltantes se excluyen expresamente como fuentes por instrucción del usuario.

El nombre vacío se envió una vez con credenciales de cambio vacías: la vista quedó en Loading y una nueva consulta conservó el nombre inicial de A. No hubo una validación visible fiable; no se establece obligatoriedad ni se genera un caso de rechazo basándose solo en ese intento. No se repite la exploración para buscar límites arbitrarios.

No se reporta el hallazgo HTTP en la planilla de fallas: el comentario lo dejará para confirmar durante la ejecución. La revisión por otro integrante permanece pendiente y no se marcará por el agente.

## 9. Estado

Diseño con OK del usuario y revisión independiente APTO del conjunto confirmado: **seis casos listos (T10-01/02/03/08/09/10) y cuatro candidatos pendientes (T10-04/05/06/07), excluidos del registro propuesto**. El bloque manual a/b/c completaría la cobertura de T10-04/05/06; su resultado aún está pendiente. **No registrado, no publicado y no ejecutado formalmente.** Se actualizará a “Diseñados y registrados en TestLink; pendiente de revisión por otro integrante” únicamente después del registro comprobado. La revisión de Claude no sustituye la revisión de otro integrante.

## Fichas para TestLink — seis casos preparados

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

### T10-04. Intentar cambiar la contraseña con la contraseña actual incorrecta

**Importancia:** **high**. Detecta sustitución de credenciales sin validar correctamente la contraseña anterior.

**Requerimiento:** PEB-74 / T10. Validar la correspondencia de Old Password con la cuenta; resultado principal pendiente de confirmar.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión del navegador identificados al ejecutar.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba A.
3. Credencial vigente, una entrada distinta de ella y una contraseña alternativa disponibles únicamente para quien ejecuta.

**Descripción:** Propuesta pendiente: comprobar el tratamiento de una contraseña anterior incorrecta. No registrar como caso listo hasta confirmar la regla o aprobar expresamente el criterio de seguridad.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Settings / Profile sin alterar nombre, correo ni configuración temporal. | Se muestran los controles Old Password y New Password vacíos. |
| 2. Introducir personalmente una contraseña incorrecta en Old Password y la alternativa en New Password; pulsar Ok una sola vez. | PENDIENTE: confirmar rechazo y señal visible. El criterio de seguridad propuesto exige que la contraseña incorrecta no autorice el cambio. |
| 3. Registrar la respuesta y comprobar qué credencial permite Login, sin superar el presupuesto de intentos de la exploración. | Se identifica el estado real de la credencial sin atribuir fallos de la herramienta al producto. |
| 4. Restaurar personalmente la credencial inicial si fuera necesario y actualizar el registro privado. | La cuenta queda accesible con su contraseña inicial y el registro privado coincide. |

**Postcondiciones:** Cuenta accesible y credencial inicial conservada o restaurada; regla y resultado principal pendientes antes del registro definitivo.

---

### T10-05. Cambiar la contraseña desde Settings y recuperar el estado inicial

**Importancia:** **high**. Protege la continuidad del acceso después de un cambio voluntario de credencial.

**Requerimiento:** PEB-74 / T10. Un cambio válido desde Settings permite Login con la nueva contraseña y deja sin efecto la anterior.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión del navegador identificados al ejecutar.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba A.
3. Contraseña inicial vigente y otra contraseña de prueba disponibles únicamente para quien ejecuta; posibilidad de recuperación por buzón controlado si ocurre un fallo.

**Descripción:** Comprobar cambio válido, acceso posterior y reversión. La observación del flujo Settings todavía debe completarse antes de declarar listo el caso.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Settings / Profile. | El perfil corresponde a A y presenta Old Password y New Password. |
| 2. Introducir personalmente la contraseña vigente en Old Password y la alternativa en New Password; pulsar Ok. | El cambio válido es aceptado sin alterar nombre, correo ni configuración temporal. Resultado del flujo Settings pendiente de confirmar en la exploración. |
| 3. Cerrar sesión y probar una vez Login con la contraseña inicial. | Login no concede acceso con la contraseña reemplazada. |
| 4. Iniciar sesión con la contraseña alternativa. | Login concede acceso a A y se conserva su información. |
| 5. Volver a Settings y restaurar personalmente la contraseña inicial mediante Old Password y New Password; actualizar el registro privado. | La restauración es aceptada y el registro privado refleja la contraseña inicial vigente. |
| 6. Cerrar sesión, iniciar sesión con la contraseña inicial y consultar Profile. | A vuelve a ser accesible con la contraseña inicial; nombre y correo conservan los valores previos. |

**Postcondiciones:** Contraseña inicial restaurada y Login comprobado; nombre, correo y Settings sin cambios; registro privado actualizado y sin secretos en evidencias.

---

### T10-06. Cancelar una edición de correo conserva el identificador de acceso

**Importancia:** **high**. Evita pérdida de acceso por una modificación de correo descartada.

**Requerimiento:** PEB-74 / T10. Cancel descarta el correo editado en Profile.

**Precondiciones:**
1. Acceso a internet y equipo con Chrome; sistema operativo y versión del navegador identificados al ejecutar.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba B.
3. Correo original de B y alias alternativo del mismo buzón controlado disponibles para quien ejecuta; credenciales en registro privado.

**Descripción:** Comprobar la cancelación de la edición de Email. El descarte de nombre fue observado; el efecto específico sobre Email sigue pendiente de contraste.

| Paso | Resultado esperado |
|---|---|
| 1. Abrir Settings / Profile y verificar que corresponde a B; anotar privadamente el correo original. | Email muestra el identificador original de B. |
| 2. Sustituir personalmente Email por el alias de prueba del mismo buzón y pulsar Cancel. | Settings se cierra y la edición se descarta; este resultado específico requiere contraste exploratorio. |
| 3. Volver a abrir Profile. | Email conserva exactamente el correo original de B. |
| 4. Cerrar Settings, pulsar Logout e iniciar sesión con el correo original y su contraseña vigente. | Login permite acceder a B con el identificador original; no se necesita una verificación para una edición descartada. |

**Postcondiciones:** B conserva su correo original y su acceso; no se ha enviado un cambio válido de correo ni utilizado un buzón ajeno.

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
