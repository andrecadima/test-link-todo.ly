# Respuesta al encargo 08 — Revisión independiente de T10-04/05/06

Autor: Claude (revisión de diseño). **No equivale a la revisión de un integrante del equipo ni a una ejecución formal.** No usé navegador, Jira, TestLink ni git, y no leí `.secrets/`, `revision-testlink/` ni PDF. El único archivo que escribí es este.

## Alcance y fuentes leídas

- Fuentes leídas: `AGENTS.md`, `docs/decisiones-vigentes.md` (§7, §13–§15), la guía (§9–§11 y §19), `T10/exploracion.md`, `contraste-restauracion.txt`, `verificacion/restauracion-A-AX.txt`, `analisis-diseno.md`, `casos-listos.json`, `casos-pendientes.json`, `casos-importar-adicionales.json`, `importacion-adicionales.xml` y `07-T10-completar-manuales-respuesta.md`.
- Evidencias revisadas visualmente: `2026-11-18_T10_old-password-incorrecto-Invalid-Password.png`, `2026-11-18_T10_restauracion-reportada-area-autenticada.png` y `2026-11-18_T10_email-original-tras-Cancel.png`.
- Contraste de controles públicos con T09: **Login**, **Sign Up Free** y **Remember Me** aparecen en `T09/analisis-diseno.md` y `T09/exploracion.md`.
- Solo reviso T10-04/05/06 y la actualización del análisis. Los seis casos ya registrados quedan fuera.

## Bloqueantes

Ninguno.

## No bloqueantes

1. **T10-04: la conservación tras el rechazo no está tipificada como criterio del equipo.**
   - En la tabla del §3 del análisis, la fila de Old Password incorrecto clasifica todo como *Comportamiento observado*, incluido "el cambio no se aplica".
   - Lo único observado directamente es el aviso **Invalid Password** (captura de las 15:56).
   - La conservación de la contraseña vigente es un **criterio de seguridad del equipo**. Lo respalda de forma indirecta el contraste b), en el que la vigente se aceptó como Old Password inmediatamente después. Nadie hizo Login después de a).
   - La nota bajo la tabla 5.2 y la respuesta 07 lo explican, pero ni la fila del §3, ni la acción "conservar la vigente" de R2 en 5.2, ni la ficha lo identifican como criterio.
   - **Corrección propuesta:** dividir la fila del §3 en dos:
     - Rechazo con **Invalid Password** → Comportamiento observado.
     - La vigente sigue dando acceso tras el rechazo → Criterio del equipo, respaldado indirectamente por b) y comprobado directamente en los pasos 9–13 de T10-04 durante la ejecución.
   - Opcionalmente, añadir "(criterio del equipo)" en el requerimiento de la ficha.
   - No hace falta cambiar los pasos ni el XML: el resultado esperado está respaldado y el diseño no presenta la ejecución como una observación.
2. **T10-05, paso 12.** "El aviso es transitorio; no se repite el intento para capturarlo" es una instrucción para quien ejecuta, no un resultado. Sería más limpio llevarla a la acción ("…una sola vez, sin repetir el intento") o a las postcondiciones. No cambia lo esperado.
3. **T10-06, precondición 4.** "Indicada por la persona usuaria" depende del contexto de la exploración. Para que otras personas puedan ejecutar el caso (decisiones §7), propongo "elegida por quien ejecuta". La frase actual no afirma que la dirección sea un alias del mismo buzón, lo cual es correcto.
4. **Encabezado del análisis.** En "revisión independiente 04 APTO para los seis casos" no queda claro que "04" se refiere al encargo 04 y no al caso T10-04. Propongo "revisión independiente (encargo 04)".
5. **T10-08, ya registrado.** Sus postcondiciones siguen diciendo que la restauración está "pendiente de confirmar". No es editable en este encargo. Conviene aclarar en el comentario de PEB-74 que T10-05/b) restauró A y que se verificó.
6. **Privacidad de evidencias.** `verificacion/restauracion-A-AX.txt` y las tres capturas del 18/11 muestran direcciones reales de A y B, además de marcadores personales del navegador.
   - Ya están marcadas como evidencia privada.
   - Hay que confirmar que no se adjuntan a Jira ni a TestLink.
   - Antes de incluirlas en un commit, decidir si el repositorio puede contener esos correos.
   - En esta respuesta no transcribo ninguna dirección.

## Comprobaciones específicas del encargo

| Punto | Resultado |
|---|---|
| Títulos: funcionalidad + condición + resultado, ≤90 caracteres | Cumplen: 04 ≈82, 05 ≈78 y 06 ≈67. |
| La descripción empieza con "Validar que" | Sí, en los tres, con una sola oración. |
| Precondiciones nominales, cuentas genéricas y sin secretos | Sí. El único literal es la contraseña sintética `Prueba-T10-04-incorrecta`. La regla de "menos de tres intentos" está marcada como criterio operativo del equipo (§13) y no como política de Todo.ly. |
| Una acción por paso, controles y datos en negrita, resultados observables | Sí. Login, Email, Password y Submit van en pasos separados. El XML convierte la negrita en `<strong>`. |
| Sin confirmación inexistente en Settings | Correcto: 04 afirma que no hay campo de confirmación, y la observación del 17/11 y la captura lo confirman. |
| Sin políticas, límites, mensajes de éxito ni IDs inventados | Correcto. |
| 05: el cambio b) ya restaura, sin un segundo cambio | Sí: lo indican la precondición 4 y las postcondiciones. |
| 05: negativo con exactamente un intento observado | Sí: el paso 12 dice "una sola vez", con el texto literal del AX (`contraste-restauracion.txt`). |
| 05: positivo con la original verificada | Sí: los pasos 15–20 están respaldados por `restauracion-A-AX.txt` (Full Name, Email y La Paz UTC-04). |
| 05: sin mensaje literal de éxito | Sí: el paso 7 lo excluye expresamente, y la captura de las 15:58 muestra Work sin ningún aviso. |
| 06: solo Cancel de Email, sin afirmar el mismo buzón y sin Login de B | Correcto, y la captura de las 15:59 muestra el Email original con Cancel/Ok. |
| Tabla 5.2: C1 Old informado, C2 coincide, C3 New informado; tres reglas → 03/04/05 | Correcto. Usa N.A. para C2 en R1 y deja fuera New Password vacío, que queda como duda pendiente. |
| T10-07 solo como pendiente | Sí: `casos-pendientes.json` contiene únicamente T10-07, y no aparece en el XML. |
| Coherencia entre JSON, XML y fichas | Los tres casos coinciden en título, precondiciones, pasos (18/23/10 = 51), importancia high (3) y ejecución Manual (1). La raíz es `<testcases>`, sin IDs ni externalid. El Summary sigue el orden descripción → requerimiento → postcondiciones. |

## Checklist de la guía §19 (solo T10-04/05/06 y la actualización del análisis)

- [x] Se leyó el ticket correcto y se respetó su alcance (PEB-74, Settings y Profile; T10-07 queda fuera).
- [x] El análisis explica riesgos concretos (R1 y R3), reglas y dudas (New Password vacío, cambio válido de Email).
- [x] Cada técnica tiene una aplicación real: particiones, tabla de decisión 5.2 y UC3/UC4, con trazabilidad por caso.
- [x] Los tipos de prueba se eligieron por pertinencia (funcional).
- [x] No se inventaron límites, controles, mensajes ni funciones. Queda pendiente la tipificación de NB1, que es de clasificación y no de invención.
- [x] No se reintrodujeron las jerarquías de tareas.
- [x] La ficha contiene solo los campos acordados.
- [x] Se usa importancia, no severidad.
- [x] Cada paso tiene un resultado verificable (con el matiz de NB2).
- [x] Los datos, controles y estados iniciales permiten reproducir los casos (con el matiz de NB3).
- [x] Las postcondiciones describen dónde terminan las credenciales, la sesión y la evidencia.
- [x] Se diferencian diseñado, registrado (sin ID), revisado y ejecutado.
- [x] No se afirma cobertura inexistente. Ver NB1 sobre la etiqueta de la fila del §3.

## Veredicto

**APTO** para registrar T10-04/05/06 tal como están en `importacion-adicionales.xml`. NB1 debe corregirse o documentarse en el análisis antes o junto con el registro, porque afecta a la clasificación de la regla y no al contenido del XML. NB2–NB6 son mejoras opcionales o avisos de cierre.

Esta revisión de Claude no sustituye la revisión de otro integrante, que sigue pendiente, ni constituye una ejecución formal de los casos.
