# Respuesta al encargo 11 — Revisión independiente de técnicas de T10 tras el feedback del usuario

Autor: Claude (revisión de diseño). **No equivale a la revisión de un integrante del equipo ni a una ejecución formal.** No usé navegador, Jira, TestLink ni git. No leí `.secrets/`, `revision-testlink/` ni el PDF completo. El único archivo que escribí es este.

## Fuentes leídas

- `AGENTS.md` y `docs/decisiones-vigentes.md`, incluida la §16.
- `T10/feedback-tecnicas.md`, `T10/analisis-diseno.md` (§1–§9 y fichas), `T10/comentario-jira-borrador.md`, `T10/exploracion.md` y `08-T10-revision-manuales-respuesta.md`.
- `tmp/pdfs/feedback-tecnicas/secciones-revisadas.txt`, que contiene pp. 8–19, 45–56 y 58–66.
- Imágenes: las cinco capturas de `trabajo/fuentes/feedback-tecnicas-2026-11-18/` y los renders de las pp. 13 y 46.
- No encontré ningún archivo `00-contexto` en `trabajo/encargos/`. Tomé las definiciones de las secciones del PDF ya extraídas.
- El borrador de Jira reproduce las §1–§9 del análisis sin diferencias de contenido. Las observaciones valen para los dos.

## Bloqueantes

Ninguno.

## No bloqueantes

1. **La letra «A» se usa para el actor y también para la cuenta A.**
   - En la §5.1 se define A como la persona y S como Todo.ly, que es el formato del docente (p. 60).
   - Pero en UC1–UC3 «A: abre Settings / Profile» puede leerse como «la cuenta A».
   - En UC4, «A: abre Profile de B» puede leerse como si la cuenta A accediera al perfil de la cuenta B. Eso sería una violación de la separación de cuentas, justo lo contrario de lo que el caso describe.
   - **Propuesta:** escribir siempre «cuenta A» y «cuenta B» para las cuentas. Por ejemplo: «A: con sesión de la cuenta B, abre Settings / Profile» y «Previo: sesión de la cuenta A».
   - Es un cambio de redacción y no afecta a casos ni a IDs. Conviene hacerlo antes de publicar, porque el texto va a evaluación.

2. **Las etiquetas R1–R6 se repiten entre riesgos y reglas de decisión.**
   - La §2 usa R1–R6 para los riesgos y la tabla 5.2 usa R1–R6 para sus columnas.
   - En la lista resumida, la fila T10-03 dice «…; R1» (riesgo) y, en la misma fila, «regla R1» (columna de la tabla). La fila T10-04 combina el riesgo R1 con la «regla R2».
   - **Propuesta:** renombrar las columnas de la 5.2 como «Regla 1 … Regla 6», o un rótulo equivalente que no se confunda. Son encabezados de columna, no identificadores de caso, así que no chocan con AGENTS §Convenciones.

3. **Falta explicar en una frase por qué se retira la atribución de particiones.**
   - Lo escrito es correcto. No se afirma en ningún sitio que las particiones exijan rangos, y `feedback-tecnicas.md` reconoce bien que no necesitan límites numéricos (la p. 9 admite conjuntos y booleanos).
   - Pero la §5 del análisis y del borrador solo dice que «una tabla de clases/representantes no equivale a una tabla de decisión» y que «se retira la atribución». No dice qué fallaba.
   - **Propuesta:** añadir una frase parecida a esta: «Particiones divide el dominio de una entrada en clases con tratamiento equivalente y toma un representante de cada una (pp. 8–9). La tabla de decisión combina condiciones T/F y deriva acciones por regla (pp. 45–48). Casos de uso deriva casos del escenario principal y de sus extensiones (pp. 58–62). La tabla publicada mezclaba recorridos (Ok/Cancel, recuperación) con clases de entrada, por eso se reorganiza en casos de uso.»
   - Así queda contestada directamente la observación del usuario.

4. **Las extensiones se anclan al paso del actor, no al paso en que el sistema valida.**
   - En el ejemplo del docente (p. 60), la extensión 2a cuelga de «S: Validate Password».
   - En UC2, la extensión 3a cuelga del paso 3, en el que el actor introduce el correo. El rechazo lo produce S en el paso 4.
   - En UC3 pasa lo mismo: 3a y 3b cuelgan del paso 3, pero el rechazo lo produce S en el paso 5.
   - No es incorrecto: el anclaje es explícito y los casos derivados son los correctos.
   - **Opcional:** para seguir más de cerca el formato del docente, usar 4a en UC2 («Correo no registrado → S: muestra Error…») y 5a/5b en UC3. Si se cambia, hay que actualizar la lista resumida (§6).

5. **La regla 4 de la tabla (Old y New vacíos) se parece al guardado normal de T10-02.**
   - La §16 de las decisiones fija que las tres combinaciones con New Password vacío quedan pendientes, y la tabla lo cumple.
   - Pero un lector puede notar que T10-02, en su paso 2, espera «sin aviso de rechazo» al guardar el nombre, con los campos de contraseña vacíos en la práctica.
   - La frase «no se deducen del guardado normal de Full Name» ya responde a eso.
   - **Opcional:** añadir que la acción «Aceptar cambio de contraseña» no se ha observado en ningún intento con New Password vacío. Así se entiende por qué se mantiene «?» aunque haya un guardado de nombre observado.

6. **Restos del término «clase» en un caso ya registrado.** T10-09 (TL-70) dice «la clase correo no registrado» en su descripción. No se puede editar en este encargo, y el término es genérico. Lo menciono solo por si el docente lo interpreta como un resto de las particiones. No requiere acción.

7. **Formato de los valores no aplicables.** El docente marca con **X** las condiciones no aplicables y las reglas por validar con el PO (pp. 53 y 55). La tabla usa «N.A.» y «?», con su leyenda. Es válido. Opcionalmente, se puede mencionar que equivale a la X del docente.

## Comprobaciones específicas

| Punto | Resultado |
|---|---|
| Exactitud técnica de las particiones | Correcta. No se afirma que las particiones exijan rangos. La retirada se presenta como una decisión sobre el fundamento, no como un error de la técnica (ver NB3). |
| Tabla de decisión con formato del docente | Correcta. Condiciones arriba, acciones abajo, reglas en columnas, T/F y Execute (pp. 46 y 48). |
| Condiciones C1/C2/C3 y número de reglas | Correcto. Si C1 = F, C2 no se puede evaluar. Quedan 2 reglas con C1 = F y 4 con C1 = T: 6 combinaciones factibles, no las 8 independientes. Las reglas 1–3 corresponden a T10-03/04/05, que están observadas. Las reglas 4–6 tienen «?» y no generan caso. No se presenta la tabla como cobertura completa. |
| UC1 (nombre) | El principal 1–7 deriva T10-02, y la extensión 4a (Cancel) deriva T10-01. La persistencia en nueva sesión figura como criterio del equipo, como dice la exploración. Correcto. |
| UC2 (recuperación) | El principal 1–10 deriva T10-08 y la extensión 3a deriva T10-09, con los literales observados. En el paso 6 el enlace se abre tal como llega, sin cambiar HTTP por HTTPS, y que cargue el formulario figura como criterio del equipo (en la exploración, el HTTP cargó vacío sin atribuirlo al producto). Correcto. |
| T10-10 | Se trata como control transversal del paso 5, con HTTPS como criterio del equipo. No se modifica el enlace para que T10-08 pase y no se reporta en la planilla de fallas. Correcto. |
| UC3 (Settings) | El principal deriva T10-05 (cambio y restauración verificados en b). La extensión 3a deriva T10-03, con la conservación de la clave observada por Login. La extensión 3b deriva T10-04: el rechazo está observado y la conservación es criterio del equipo, con respaldo indirecto de b). Coincide con la §3 (NB1 del encargo 08 resuelto). |
| UC4 (Email) | El principal es el descarte y deriva T10-06. El guardado de Email (T10-07) queda como recorrido pendiente y no se presenta como extensión con resultado. Correcto (ver NB1 sobre «A … de B»). |
| Reglas ACME trasladadas | Ninguna. No aparecen los 4 intentos, las 24 horas ni la retención de tarjeta. El «menos de tres intentos» de T10-05 está marcado como criterio operativo del equipo. |
| Flujos o mensajes inventados | Ninguno. No hay mensaje de éxito tras Ok o Done. Los literales Invalid Password, Info…, Error. Account… y Wrong email or password están en la exploración. |
| Trazabilidad de los nueve casos | Los seis originales (01, 02, 03, 08, 09 y 10) y los tres adicionales (04, 05 y 06) están en la §5 y en la lista resumida. T10-07 figura solo como pendiente. Casos e IDs sin cambios. |
| Estados honestos | Seis registrados (TL-66 a TL-71) y tres listos sin ID. La revisión del integrante y la ejecución formal siguen pendientes. Correcto. |

## Veredicto

**APTO** para publicar la corrección de técnicas de T10.

Recomiendo aplicar antes NB1 (A/B) y NB2 (R1–R6), porque son cambios de redacción, cuestan poco y evitan lecturas erróneas en un texto evaluado. NB3 es muy recomendable. NB4–NB7 son opcionales.

Esta revisión no sustituye la revisión de otro integrante, que sigue pendiente, ni la ejecución formal de los casos.
