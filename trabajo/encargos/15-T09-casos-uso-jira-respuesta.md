# Respuesta al encargo 15 — T09: fundamento único por casos de uso para Jira

## Entregable

`trabajo/T09/correccion-casos-uso-jira.md`, con solo `## 5. Técnica aplicada: casos de uso` y `## 6. Lista resumida de casos`. Sustituye §5.1–§5.5 y §6 del HTML actual. No se tocaron TestLink, XML, analisis-diseno.md ni otros archivos.

Extensión estimada: unos 9 000 caracteres de Markdown. No tuve shell para medirla con exactitud y puede superar algo el rango de 8 500. Codex debe medir el HTML final. Si no entra en 32 767, recortes sin pérdida de traza: 1) eliminar la frase final de §6; 2) acortar el texto de 4 en UC1 a "inicial Pacific UTC-08; lista sin vacío con La Paz UTC-04 distinta de UTC-07", con los literales en la ficha TL-74; 3) reducir los `data-colwidth` de las tablas UC a tres columnas.

## Revisión de flujos y trazas

| UC | Principal → caso | Extensiones (paso de anclaje) → caso | Fuente de las respuestas de S |
|---|---|---|---|
| UC1 Preparar Signup y abandonar | 1–8 → T09-03 (recorrido parcial, sin registro completo) | 3a → T09-01; 7a → T09-02 | exploracion.md filas 1, 2, 5 y 6; duplicado, línea 45; conservación de identidad como criterio del equipo |
| UC2 Iniciar sesión | 1–6 → T09-04 | 3a → 05; 3b → 06; 3c → 07; 3d → 08, pendiente; 3e → 09; 3f → 10 | Tabla del 17/11; mensaje de 05 no exigido; 09 apoyado en contraste T10 |
| UC3 Logout y navegación | 1–8 → T09-11 | — | Filas de Fase 2, 7:38–7:39 PM; solo Back y URL raíz |
| UC4 Separación A/B | 1–9 → T09-12 | — | Fase 2 7:41 PM y continuación del 17/11; independencia también como criterio del equipo |
| UC5 Remember Me | 1–7 → T09-14 | 2a → T09-13 | Reaperturas observadas; sin política de expiración |

Comprobaciones:
- Los trece casos registrados y T09-08 aparecen una sola vez, con sus ID TL-72 a TL-84 y la importancia de la fuente.
- Cada extensión parte de un paso existente.
- No hay EP, reglas R de decisión ni estados S; R1–R6 aparecen solo como "Riesgo".
- T09-08 no tiene resultado esperado.
- No se añaden casos, controles ni fronteras.
- Los literales de Signup y Login coinciden con la fuente.
- Las cuentas son genéricas y no aparecen secretos.

## Alertas y observaciones

1. **Alerta de trazabilidad (no bloquea Jira):** en TestLink, el campo Requerimiento de T09-05/06/07/09/10 dice "La combinación negativa R1…R5 de la tabla de decisión" (casos-listos.json, líneas 269, 308, 351, 397 y 441). Al retirar esa tabla de Jira, esa referencia queda sin artefacto. Tampoco se puede leer esa "R" como el Riesgo R1–R6 de §2. No modifiqué TestLink ni XML. Andre debe decidir si se acepta la diferencia o se pide una corrección aparte.
2. En el HTML quedan otras menciones a las técnicas anteriores. §9, "Técnicas justificadas", dice "Particiones, decisión, estados y casos de uso". §5.5 de valores límite también desaparece al sustituir §5. Codex podría poner en §9: "Casos de uso con flujos, extensiones y trazabilidad; sin límites inventados".
3. analisis-diseno.md §5/§6 sigue con la versión anterior. Si se sincroniza, debe hacerlo Codex.
4. Hay celdas vacías en la columna Escenario, que hacen de celda combinada como en la diapositiva del ATM. Si Jira las muestra mal, se puede repetir "Principal" o "Extensiones".
