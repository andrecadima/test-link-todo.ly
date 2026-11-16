# Plantilla de caso de prueba (ficha para TestLink)

La ficha lleva exactamente los campos acordados (guía, secciones 8B y 9). El tipo de prueba, la técnica, el riesgo y la severidad **no** van aquí: se explican en el comentario de Jira.

---

### T0X-NN. Título que nombra la acción y su objetivo

**Importancia:** **high**, **medium** o **low**, con una razón breve.

**Requerimiento:** PEB-XX / T0X. Comportamiento concreto que se comprobará.

**Precondiciones:**
1. Acceso a internet. Windows con Chrome; la versión se anota al ejecutar.
2. Sesión iniciada en Todo.ly con una cuenta gratuita de prueba (cuenta A). No se escriben correos ni contraseñas reales.
3. Estado inicial específico del caso: proyectos, tareas, Settings y nombres que no deben existir.

**Descripción:** una o dos frases sobre qué se comprobará.

| Paso | Resultado esperado |
|---|---|
| 1. Acción concreta, con el proyecto, el control y el dato exactos. | Efecto observable de esa acción. |
| 2. Acción siguiente. | Resultado comprobable. |
| 3. F5 o nuevo inicio de sesión, cuando el riesgo sea la persistencia. | Lo que debe conservarse: contenido, estado, cantidad o ubicación. |
| 4. Limpieza de los datos creados, después de conservar la evidencia. | Situación concreta después de la limpieza. |

**Postcondiciones:** dónde terminan los datos de prueba (proyecto, completadas, papelera o retirados) y qué evidencia queda.

---

## Interpretación de la importancia

- **high:** protege una operación esencial, o evita la pérdida de acceso o la pérdida, alteración o exposición de información.
- **medium:** variante relevante, coherencia de lo que se muestra o condición especial.
- **low:** comprobación secundaria con impacto limitado.

## Mapeo a los campos de TestLink

Codex completa esta tabla en la fase 0, a partir de cómo están registrados los casos de T06 y T12.

| Campo del diseño | Campo de TestLink (confirmar con T12) |
|---|---|
| Título | Nombre del test case |
| Importancia | Importance |
| Requerimiento | Summary: etiqueta Requerimiento, referencia PEB-XX / T0X y comportamiento. Confirmado en TL-41 y TL-40; sin vínculo formal observado. |
| Descripción | Summary |
| Precondiciones | Preconditions |
| Paso / Resultado esperado | Steps: Step actions / Expected results |
| Postcondiciones | Al final de Summary, como TL-41; la limpieza además se desarrolla en los pasos. |
| — | Execution type: Manual |
