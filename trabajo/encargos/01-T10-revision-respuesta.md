# Revisión independiente de T10 / PEB-74 — respuesta de Claude

Fecha: 17/11/2026. Alcance: el conjunto registrable `trabajo/T10/casos-listos.json` (T10-01, 02, 03, 08, 09 y 10) y los artefactos que lo acompañan (`analisis-diseno.md`, `comentario-jira-borrador.md`, `importacion-propuesta.xml`, `registro-preparado.md`). Revisión de agente: **no sustituye la revisión de otro integrante**. No se ejecutaron comandos ni se accedió a `.secrets/`, al navegador, a Jira, a TestLink ni a git.

Fuentes contrastadas: `exploracion.md`, `hallazgos.md`, PEB-74 (snapshot), `00-contexto.md`, guía §5–11 y §19, decisiones §6–7, §13–14, plantillas, y las capturas `old-password-vacio-Invalid-Password.png`, `recuperacion-correo-inexistente.png`, `perfil-restaurado.png` y `nombre-guardado-persiste-recarga.png`. `casos.json` coincide literalmente con `casos-listos.json` en los seis casos listos y con `casos-pendientes.json` en los cuatro restantes.

**Ajustes 1–5 y pasos a/b/c:** no figuran en ningún archivo accesible. No se puede verificar si se aplicaron, y esta revisión no lo afirma.

---

## 1. Bloqueantes

### Contenido de `casos-listos.json`: ninguno

No hay mensajes, controles ni límites inventados. Los textos literales de los resultados esperados tienen respaldo:

- `Invalid Password`: visible en la captura del caso con Old Password vacío, como diálogo «todo.ly says» con botón OK.
- `Error. Account with this Email address doesn't exist.`: visible en la captura del correo no registrado.
- `Enter your email address to reset your password` y el botón Send: visibles en esa misma captura.
- `Info. An email has been sent…` y `Wrong email or password…`: proceden de la lectura de accesibilidad registrada en `exploracion.md`. La exploración aclara que esos avisos ya no se ven en las capturas, y los casos no se los atribuyen.
- `Please Enter a New Password`, `Enter a New Password`, `Verify New Password` y `Done`: proceden de la lectura del formulario en `exploracion.md`.
- `Not Secure`: indicador de Chrome registrado en `exploracion.md` y `hallazgos.md`.

Revisión del resto de las fichas:

- **Campos:** contienen solo los acordados (guía §8B).
- **Importancia:** se usa high/medium. No aparece severidad ni prioridad de falla.
- **Datos sensibles:** no hay contraseñas, tokens ni correos reales. La dirección `@example.com` de T10-09 es un dato reservado, no una credencial.
- **Contraseñas inválidas:** ningún caso listo contiene literalmente una contraseña de prueba inválida.
- **Alcance:** no hay tareas padre/subtareas ni zona horaria; esta solo se consulta como valor que debe conservarse.
- **Duplicación:** no se encontró duplicación real con otros tickets.
- **Criterio HTTPS:** en T10-10 aparece correctamente como Criterio del equipo, no como regla del producto.

### B1. El artefacto de importación y su documentación crean una suite por ticket, en contra de decisiones §14

Este bloqueante no afecta al contenido de los casos. Bloquea la importación **si se usa el archivo actual**.

- **`trabajo/T10/importacion-propuesta.xml`, líneas 2–4:** la raíz es `<testsuite name="T10">`, con `<node_order>` y `<details>`. Al importarse crearía la suite T10. Decisiones §14 y el encargo exigen importar en la suite existente **Todo.ly tests**, con raíz `<testcases>`, sin crear suites, sin IDs y sin actualizar casos existentes.
- **`trabajo/T10/registro-preparado.md`:** en la línea 7 dice «entrada local para crear la suite T10», y en la línea 16 describe como formato contrastado la «raíz testsuite». La línea 18 habla de un «contenedor acordado» sin nombrarlo.
- **`trabajo/T10/analisis-diseno.md` §7 (línea 104) y `comentario-jira-borrador.md` §7 (línea 106):** indican «suite T10».
- **`trabajo/00-contexto.md`, línea 133:** «suites por T09/T10/T11». Es antecedente histórico, superado por decisiones §14. No debe usarse como base del registro.

**Corrección mínima:**

1. Regenerar el XML con raíz `<testcases>` y los seis `<testcase>` sin `<testsuite>`, `<node_order>` de suite ni `<details>`. Se conservan nombre, summary, preconditions, execution_type, importance y los steps nativos. No se incluyen `internalid` ni `externalid`.
2. En el diálogo de importación, elegir como destino la suite Todo.ly tests y la opción que no actualice casos existentes.
3. Sustituir «suite T10» por «suite existente Todo.ly tests» en `registro-preparado.md`, `analisis-diseno.md` §7 y `comentario-jira-borrador.md` §7.
4. Ajustar la ruta de exportación a lo que fija decisiones §14: `testlink-xml/todo-ly-tests.xml` y, por script, `testlink-xml/T10.xml`.

---

## 2. No bloqueantes

La marca **[Antes de registrar]** indica lo que conviene corregir o documentar antes de importar. El resto puede resolverse después o en el comentario de Jira.

### Ejecución y reproducibilidad de los casos listos

- **N1 [Antes de registrar] — T10-08, paso 4.** «Abrir el enlace de recuperación en el perfil de QA mediante HTTPS» es ambiguo. Según `exploracion.md` y `hallazgos.md`, el correo entrega enlaces **HTTP**. Al abrir el enlace directo por HTTP, la página apareció vacía (Duda pendiente, no atribuida al producto). El formulario cargó cuando se abrió la misma ruta cambiando el esquema a HTTPS. Si quien ejecuta sigue el enlace tal como llega, puede no alcanzar el resultado esperado. **Corrección:** indicar expresamente «abrir la misma ruta del enlace directo sustituyendo `http://` por `https://`, sin copiar el token a la evidencia». Así queda claro que el paso evita el hallazgo de T10-10 y no lo oculta.
- **N2 [Antes de registrar] — T10-08, precondición 4 y paso 7.** «Un dato representativo de A» no está identificado, y la exploración solo verificó la identidad en Profile (nombre, correo y zona). No se comprobó un proyecto ni una tarea. **Corrección:** concretar el dato, por ejemplo «nombres de los proyectos visibles en Projects», como estado inicial anotado. Además, clasificar la conservación de datos fuera de Profile como Criterio del equipo en `analisis-diseno.md` §3, o bien limitar el esperado del paso 7 a los valores de Profile.
- **N3 [Antes de registrar] — Precondición 2 de T10-08 y T10-09, y paso 2 de T10-10.** «Perfil dedicado de QA» es una configuración propia de esta exploración. Para que otras personas puedan ejecutarlo (decisiones §7), conviene decir «perfil de Chrome dedicado a pruebas o ventana de incógnito», y reservar el perfil dedicado para lo que necesite persistencia.
- **N4 — T10-08, postcondición.** El caso deja vigente la contraseña nueva. Está documentado, y la restauración queda para la fase 6. Conviene que el comentario de Jira lo mantenga visible como dependencia del entorno.

### Coherencia entre análisis y observación

- **N5 — `analisis-diseno.md` §1 (línea 11) y §3 (línea 32).** «El guardado persiste tras recarga y nueva sesión» como Comportamiento observado necesita un matiz. Tras recargar, se observó el valor de prueba `Prueba T10 - nombre guardado`. Tras una nueva sesión (11:43–11:44), lo observado fue el nombre **restaurado**, que también se guardó con Ok. La línea 16 de `exploracion.md` decía que faltaba ese contraste para el valor de prueba. No contradice T10-02, pero conviene redactarlo así: «persistencia tras nueva sesión observada sobre el valor restaurado mediante Ok».
- **N6 — `analisis-diseno.md` §3, línea 36.** «Criterio de seguridad propuesto para revisión; no confirmado todavía» no es una de las cuatro clasificaciones (AGENTS regla 5). Debe reclasificarse como **Duda pendiente** o, si el equipo lo aprueba, como **Criterio del equipo**. No afecta a los casos listos, porque T10-03 se basa en lo observado.
- **N7 — `comentario-jira-borrador.md`.** Antes de publicar:
  - Actualizar «Pendiente de punto de control y OK del usuario» (§7) y el encabezado (línea 5): el OK ya se dio. Sin IDs reales, se debe seguir diciendo «no registrado».
  - Completar la tabla de §7 con IDs y enlaces reales solo después del registro comprobado.
  - Redactar §8 en tercera persona sin detalles internos de la herramienta («política de CUA»). Basta «la herramienta de ejecución exige que una persona introduzca y envíe las nuevas credenciales».
  - Valorar si se sustituye el nombre real del perfil («Andre Cadima», §8) por «nombre inicial de A».

### Cobertura pendiente (no son contradicciones de los casos listos)

- **N8.** PEB-74 pide la modificación de **correo** y el cambio de contraseña, y sus criterios piden «cambios válidos, entradas inválidas y cancelaciones». El conjunto listo cubre:
  - cambio válido de nombre;
  - Cancel del nombre;
  - entrada inválida en Old Password (vacío);
  - correo no registrado en recuperación;
  - recuperación válida;
  - HTTPS del enlace.

  **No cubre** Email (Cancel ni cambio válido), Old Password incorrecto ni el cambio válido desde Settings. T10-04/05/06/07 están excluidos del registro, como corresponde. El comentario de Jira debe presentar esa falta como riesgo sin cobertura para revisión del equipo, como ya hace §8. **Debe documentarse antes de registrar**, y así consta.
- **N9.** También quedan sin confirmar la política de contraseña, las fronteras de campos, la caducidad y el uso único del token, la invalidación de otras sesiones y la obligatoriedad de Full Name (intento único con Loading). No procede proponer valores límite: no hay ninguna frontera confirmada.

### Evidencias

- **N10 [Antes de adjuntar en Jira].** Las capturas `old-password-vacio-Invalid-Password.png`, `perfil-restaurado.png` y `nombre-guardado-persiste-recarga.png` muestran **el correo real de la cuenta A** en el campo Email. No son contraseñas, pero decisiones §7 excluye correos reales de los casos. Si alguna captura se adjunta a Jira o TestLink, conviene recortar o tapar ese campo. Ninguna de las cuatro capturas revisadas muestra contraseñas legibles: New Password aparece enmascarado.
- **N11.** `cancel-conserva-nombre.png` y `password-anterior-rechazada.png` no muestran el aviso ni el valor que se les asocia, como reconoce `exploracion.md`. No deben citarse en Jira como prueba visual de esos textos.

---

## 3. Veredicto

**APTO** para el conjunto `casos-listos.json` (T10-01, 02, 03, 08, 09 y 10). Su contenido no tiene bloqueantes.

Condición de registro: **no importar `importacion-propuesta.xml` en su estado actual** (B1). Primero hay que regenerarlo con raíz `<testcases>` hacia la suite existente Todo.ly tests, sin crear suites ni actualizar casos. Se recomienda aplicar N1–N3 antes de generar ese XML y documentar N8 en el comentario.

El veredicto no se refiere a los candidatos pendientes T10-04/05/06/07 ni equivale a la revisión de otro integrante. Tampoco acredita registro ni ejecución.

---

## Checklist de la guía §19

| # | Ítem | Estado | Fundamento |
|---|---|---|---|
| 1 | Ticket correcto y alcance respetado | Cumple | PEB-74: perfil, credenciales y recuperación. La zona horaria, la eliminación de cuenta y Pro quedan excluidas (decisiones §9–10). |
| 2 | El análisis explica riesgos, reglas y dudas | Cumple | Hay matriz R1–R6 con P×I justificada y tabla de reglas clasificadas. Ver N5 y N6 para los matices. |
| 3 | Cada técnica tiene aplicación real y justificación por caso | Cumple | Las particiones (correo registrado/no registrado, credencial vigente/reemplazada, Old Password vacío) se trazan a T10-03/08/09. UC1 se traza a T10-01/02 y UC2 a T10-08/09. T10-10 se justifica como seguridad observable con criterio del equipo. La decisión de no usar límites ni tabla de decisión está justificada. |
| 4 | Tipos de prueba elegidos por pertinencia | Cumple | Funcional y seguridad observable, con objetivo, procedimiento y criterio. No se añaden compatibilidad, accesibilidad ni rendimiento sin base. |
| 5 | No se inventaron límites, controles, mensajes ni funciones | Cumple | Todos los literales están respaldados (ver §1). La conservación de datos fuera de Profile (T10-08) debe clasificarse como criterio (N2). |
| 6 | No se reintrodujeron jerarquías de tareas | Cumple | No hay tareas padre/subtareas. |
| 7 | La ficha contiene solo los campos acordados | Cumple | Título, importancia y razón, requerimiento, precondiciones, descripción, pasos/resultados y postcondiciones. |
| 8 | Se usa importancia, no severidad ni prioridad | Cumple | high/medium, con su mapeo a 3/2 en el XML. |
| 9 | Cada paso tiene un resultado verificable | Cumple | Todos los pasos tienen un esperado observable. En T10-08 el paso 7 debe concretar el dato (N2). |
| 10 | Datos, controles y estados iniciales permiten reproducir el caso | Pendiente | Falta precisar T10-08 paso 4 (cambio de http a https, N1), el «dato representativo» (N2) y el «perfil dedicado de QA» (N3). |
| 11 | Limpieza y postcondiciones indican dónde terminan los datos | Cumple | Los nombres se restauran. T10-08 declara que la credencial nueva queda vigente y que su restauración está pendiente en el entorno (N4). |
| 12 | Se diferencian diseñado, registrado, revisado, ejecutado y fallido | Cumple | El diseño declara «no registrado, no publicado, no ejecutado». **Registro, revisión de integrante y ejecución: no realizados.** El hallazgo HTTP no se reporta en la planilla. |
| 13 | No se afirma cobertura o evidencia inexistente | Pendiente | Falta matizar la persistencia «tras nueva sesión» (N5) y no citar capturas sin el aviso (N11). La cobertura de Email y del cambio desde Settings se declara correctamente como pendiente. |
