# Revisión independiente definitiva — T10 / PEB-74 (encargo 04)

Fecha: 17/11/2026. Revisor: Claude, agente de revisión. **No sustituye la revisión de otro integrante, no es una ejecución de casos y no acredita ningún registro en TestLink ni publicación en Jira.** No se usaron navegador, Jira, TestLink ni git, y no se accedió a `.secrets/`.

**Alcance:** solo los seis casos confirmados T10-01, 02, 03, 08, 09 y 10, tal como están en `casos-listos.json`, en las fichas de `analisis-diseno.md` y en `importacion-propuesta.xml`. Los candidatos T10-04/05/06/07 no se evalúan como registrables y no deben importarse.

**Fuentes leídas:** AGENTS.md, decisiones-vigentes (§6–7, §9–10, §13–14), PROMPT_ORQUESTACION.md, guía §7–11 y §19, plantilla de caso, `00-contexto.md` (solo lo relativo a T10 y a la suite), `analisis-diseno.md`, `exploracion.md`, `hallazgos.md`, `casos-listos.json`, `casos-pendientes.json`, `casos.json`, `importacion-propuesta.xml`, `comentario-jira-borrador.md`, `01-T10-revision-respuesta.md` y `01-T10-resolucion.md`.

**Capturas inspeccionadas:** `login-A-area-autenticada.png`, `old-password-vacio-Invalid-Password.png` y `recuperacion-correo-inexistente.png`.

**Corrección del usuario, que prevalece sobre la revisión 01:** en T10-08, el paso 4 abre el enlace tal como llega, sin cambiar HTTP por HTTPS. Por eso no se reitera la antigua sugerencia N1.

---

## 1. Bloqueantes

**No hay bloqueantes para registrar los seis casos con el XML actual.** Se comprobó cada criterio del encargo:

| Criterio | Resultado | Fundamento |
|---|---|---|
| Resultados, controles o límites inventados | Ninguno | Cada literal tiene respaldo (ver la tabla de respaldo, debajo). No se fija ningún límite de longitud ni política de contraseña, ni plazo de recepción, caducidad o uso único. Los pasos 3 y 5 de T10-08 renuncian expresamente a exigir un plazo y un aviso que no se observaron. |
| Expectativas que no son comportamiento observado | Clasificadas | La persistencia del valor de prueba tras una nueva sesión (T10-02, paso 5) figura como **Criterio del equipo** en `analisis-diseno.md` §3. HTTPS (T10-10) figura como **Criterio del equipo** en el Requerimiento de la propia ficha. Que el enlace tal como llega cargue el formulario (T10-08, paso 4) se apoya en la corrección expresa del usuario documentada en `exploracion.md` ("Ajustes del usuario antes de registro"); ver N2. |
| Contradicción con lo observado | Ninguna | T10-03: Invalid Password y la conservación de la credencial se observaron (captura y Login posterior). T10-08: el rechazo de la contraseña reemplazada y el acceso con la nueva se observaron. T10-09: rechazo visible en la captura. En T10-08, el paso 4 tal como llega puede fallar en la ejecución (la carga HTTP apareció vacía en la exploración, sin atribuirse al producto). Eso no es una contradicción: el propio esperado dice que, en ese caso, falla T10-08. |
| Tabla de decisión Old Password | No se afirma | Ningún archivo revisado declara aplicada una tabla de decisión para Old Password ni conoce el comportamiento con un valor incorrecto o válido. §5.1 marca "No coincide / coincide" como **particiones candidatas** pendientes, y UC3 deja T10-04/05 pendientes. Correcto. |
| Trazabilidad técnica → caso | Completa | UC1 → T10-02 (principal) y T10-01 (alternativa). UC2 → T10-08 (principal) y T10-09 (alternativa). Particiones de correo → T10-08 (registrado) y T10-09 (sin cuenta). Particiones de credencial tras la recuperación → T10-08. Old Password vacío → T10-03. T10-10 se justifica como seguridad observable derivada de UC2 y del Criterio del equipo. Riesgos: R1 → 03/08, R2 → 02, R3 → 01, R5 → 10 y R6 → 09. La no aplicación de valores límite y de tablas está justificada (§5.3). |
| Ficha | Correcta | Solo título, importancia con razón, requerimiento, precondiciones, descripción, pasos/resultados y postcondiciones. No aparecen severidad, técnica ni tipo. Importancia high/medium, mapeada a 3/2 en el XML. `execution_type` 1 (Manual). |
| Precondiciones | Genéricas | "Sesión iniciada en Todo.ly con una cuenta gratuita de prueba A", "Sin sesión iniciada en Todo.ly en el navegador" y "cuyo buzón controla quien ejecuta", conforme a decisiones §7. No aparecen el perfil dedicado de QA, correos reales ni contraseñas. |
| Secretos | Ninguno en casos ni XML | No hay contraseñas, tokens ni correos reales. La dirección `prueba-t10-no-registrada-20261117@example.com` es un dato reservado. El borrador de Jira ya no contiene el nombre real ni la referencia a la herramienta (N7 de la revisión 01, resuelto). |
| Duplicación con otros tickets | Ninguna real | El paso 6 de T10-08 usa el mismo aviso de rechazo que T09 (tabla de decisión de Login), pero el riesgo es otro: que la credencial reemplazada por la recuperación siga siendo válida. El Logout/Login de T10-02 sirve para persistir el perfil, no para probar la sesión (lo declara §1). No se diseña zona horaria (solo se comprueba que no cambia) ni jerarquías de tareas. |
| XML | Conforme a decisiones §14 | Raíz `<testcases>`, seis `<testcase>`, sin `<testsuite>`, sin `internalid`/`externalid` y sin `<details>` de suite. Contenido literal coincidente con `casos-listos.json`. Summary con Importancia/Requerimiento/Descripción/Postcondiciones, según el mapeo de la plantilla. `casos.json` coincide con listos más pendientes. El bloqueante B1 de la revisión 01 está resuelto. |

**Tabla de respaldo de literales:**

| Literal en los casos | Respaldo |
|---|---|
| `Invalid Password` (diálogo con botón OK) | Visible en `old-password-vacio-Invalid-Password.png`. |
| Ausencia de campo de confirmación en Settings | Misma captura: solo Old Password y New Password. |
| `Enter your email address to reset your password`, `Send`, `Error. Account with this Email address doesn't exist.` | Visibles en `recuperacion-correo-inexistente.png`. |
| `Info. An email has been sent…`, `Wrong email or password`, `Please Enter a New Password`, `Enter a New Password`, `Verify New Password`, `Done`, `Not Secure` | Lectura AX registrada en `exploracion.md` y `hallazgos.md`. No se atribuyen a ninguna captura, y ninguna captura las contiene. |
| `login-A-area-autenticada.png` | Muestra solo el área autenticada (proyectos, Settings y Logout visibles). **No muestra Profile ni identidad.** Ningún caso le atribuye texto, y `exploracion.md` lo advierte. Correcto. |

---

## 2. No bloqueantes

Las marcas indican cuándo conviene atenderlos:

- **[Antes de importar]:** recomendable y barato. Si no se corrige, basta con documentarlo.
- **[Antes de publicar]:** afecta al comentario de Jira.
- Sin marca: puede atenderse después.

- **N1 [Antes de importar] — T10-08, postcondición.** Dice: "La restauración de la contraseña original se realiza mediante el cambio válido de Settings y se verifica por Login". Ese cambio válido no se ha observado (T10-04/05 pendientes, a/b sin resultado). No es un resultado esperado de un paso, pero da por conocido un flujo pendiente. Redacción propuesta: "La restauración de la contraseña original queda fuera de este caso y se anota en el registro privado; el procedimiento válido de restauración está pendiente de confirmar". Si se modifica, hay que cambiar a la vez `casos-listos.json`, `casos.json`, la ficha y el XML.
- **N2 [Antes de publicar] — clasificación del esperado del paso 4 de T10-08.** `analisis-diseno.md` §3 no tiene una fila que clasifique "el enlace recibido, abierto tal como llega, muestra el formulario". La exploración solo vio el formulario por HTTPS, y la vista HTTP quedó vacía sin atribuirse al producto. Conviene añadir esa fila como **Criterio del equipo (instrucción expresa del usuario del 17/11)**, con referencia a `exploracion.md` ("Ajustes del usuario antes de registro"). Así el comentario de Jira deja claro que no es un comportamiento observado.
- **N3 — T10-08, paso 5.** El esperado "El cambio permite acceder a A" se verifica en realidad en el paso 7. Lo observado tras Done fue una sesión iniciada en A (11:40–11:42). Podría precisarse: "Se acepta el envío y A queda accesible; el acceso con la nueva contraseña se confirma en el paso 7". No cambia el resultado principal.
- **N4 — T10-10, precondiciones.** No indican el estado de sesión. `hallazgos.md` reprodujo el caso con la sesión cerrada. Añadir "Sin sesión iniciada en Todo.ly en el navegador" haría el caso más reproducible y coherente con T10-08/09.
- **N5 — Independencia de T10-08 y T10-10.** Ambos usan una solicitud de recuperación de A. Si se ejecutan seguidos, T10-10 requiere un enlace no usado (su precondición 3 ya lo dice) y debe ejecutarse antes de que T10-08 consuma el token, o con una solicitud propia. Puede indicarse al planificar la ejecución, sin cambiar las fichas.
- **N6 — Entorno.** La plantilla dice "Windows con Chrome"; las fichas dicen "equipo con Chrome; sistema operativo y versión identificados al ejecutar". Es aceptable y más reproducible, pero conviene que el comentario de Jira explique que la exploración se hizo en macOS y que el equipo ejecuta en Windows (guía §10, Entorno).
- **N7 [Antes de publicar] — `comentario-jira-borrador.md`:**
  - retirar el comentario HTML "BORRADOR";
  - sustituir el encabezado de la columna "Situación previa al punto de control" (§6) por un estado actual con IDs y enlaces reales tras el registro comprobado;
  - en §9, cambiar "El bloque manual a/b/c completa la cobertura" por "completaría", porque a/b/c no tienen resultado;
  - en §3, unificar las filas de las líneas 36 y 38, que repiten "cambio válido desde Settings" como Duda pendiente.
- **N8 — XML, apóstrofo de T10-09.** En el XML, `doesn't` está codificado como `&amp;#x27;` dentro de un HTML escapado; debería mostrarse como `doesn't`. Al abrir el caso importado, comprobar que TestLink no muestra `&#x27;` literal.
- **N9 — Evidencias.** `old-password-vacio-Invalid-Password.png` (y otras de Profile) muestran el correo real de A y el nombre real. Por la resolución 01 (N10/N11), no se publican en Jira; mantenerlo. `login-A-area-autenticada.png` no prueba la identidad de A y no debe citarse como tal.

### Cobertura pendiente — no bloquea el registro de los seis casos

Es cobertura que falta en PEB-74, no un defecto de los seis casos. Debe quedar explícita en Jira, y ya consta en §8 y §9 del diseño y del borrador:

- **T10-04** (Old Password incorrecto), **T10-05** (cambio válido desde Settings y restauración) y **T10-06** (Cancel de Email): dependen de los pasos manuales a/b/c, **todavía sin observar**. No pueden completarse con resultados supuestos.
- **T10-07** (cambio válido de Email): no se registra, por instrucción expresa.
- **Particiones Old Password "no coincide / coincide":** son candidatas. No hay tabla de decisión aplicada ni comportamiento conocido.
- **Dudas pendientes:** política y límites de contraseña, fronteras de campos, caducidad y uso único del token, cierre de otras sesiones, obligatoriedad de Full Name y verificación de correo al cambiar Email.
- **Estado del entorno:** la contraseña de A sigue siendo la fijada en la recuperación. Su restauración queda pendiente para el cierre (fase 6).

El ticket T10 **no** debe declararse terminado ni con cobertura completa. Los criterios de PEB-74 sobre el correo y el cambio de contraseña desde Settings siguen sin casos registrables.

---

## 3. Checklist de la guía §19 (seis casos y XML actuales)

| # | Ítem | Estado | Fundamento |
|---|---|---|---|
| 1 | Ticket correcto y alcance respetado | Cumple | PEB-74. Se excluyen zona horaria, eliminación de cuenta y Pro. |
| 2 | Análisis con riesgos, reglas y dudas | Cumple | R1–R6 con P×I. Reglas clasificadas en cuatro categorías. Ver N2 y N7 para matices. |
| 3 | Técnicas con aplicación real y justificación por caso | Cumple | UC1, UC2 y particiones trazadas a los seis casos. T10-10 con criterio del equipo. No se aplican límites ni tablas sin base. |
| 4 | Tipos de prueba por pertinencia | Cumple | Funcional y seguridad observable, con objetivo y criterio. |
| 5 | No se inventan límites, controles, mensajes ni funciones | Cumple | Todos los literales están respaldados. N1 (postcondición) y N2 (clasificación) son matices de redacción, no resultados inventados. |
| 6 | Sin jerarquías de tareas | Cumple | — |
| 7 | Ficha solo con los campos acordados | Cumple | — |
| 8 | Importancia, no severidad ni prioridad | Cumple | high = 3, medium = 2. |
| 9 | Cada paso con resultado verificable | Cumple | N3 sugiere precisar el paso 5 de T10-08. |
| 10 | Datos, controles y estados iniciales reproducibles | Cumple | Precondiciones genéricas. N4 y N5 mejorarían T10-10. |
| 11 | Limpieza y postcondiciones | Cumple con observación | Los nombres se restauran. T10-08 declara la credencial vigente; ver N1 sobre el procedimiento de restauración. |
| 12 | Se diferencian diseñado, registrado, revisado, ejecutado y fallido | Cumple | El diseño indica "No registrado, no publicado y no ejecutado formalmente". El hallazgo HTTP no se reporta en la planilla. La revisión de integrante sigue pendiente. |
| 13 | No se afirma cobertura ni evidencia inexistente | Cumple | Las capturas no se usan para avisos leídos por AX. La cobertura pendiente es explícita. Ver N7 sobre la palabra "completa" en §9. |

---

## 4. Veredicto

**APTO** para registrar los seis casos T10-01, 02, 03, 08, 09 y 10 mediante el `importacion-propuesta.xml` actual, en la suite existente **Todo.ly tests**, sin crear suites ni actualizar casos existentes. No hay bloqueantes. Se recomienda resolver N1 antes de importar; si no se resuelve, hay que documentarlo. N2 y N7 deben resolverse antes de publicar en Jira.

Se distinguen dos cosas:

- **Bloqueo para registrar estos seis casos:** ninguno.
- **Cobertura pendiente de T10:** T10-04/05/06 dependen de a/b/c, que no se han observado; T10-07 no se registra. No se importan, y su falta debe declararse en el comentario como riesgo sin cobertura. T10 no queda finalizado.

Este veredicto no acredita registro, publicación ni ejecución, y no sustituye la revisión de otro integrante. En Jira, el estado sigue siendo "pendiente de revisión por otro integrante". La decisión y la integración corresponden a Codex.
