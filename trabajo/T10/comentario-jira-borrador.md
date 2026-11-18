<!-- BORRADOR: publicar solo después de revisión y registro verificado. -->

# T10 / PEB-74 — Perfil, credenciales y recuperación de acceso

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
