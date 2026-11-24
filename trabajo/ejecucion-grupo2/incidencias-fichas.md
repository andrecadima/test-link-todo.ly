# Ambigüedades de las fichas importadas — grupo 2

Andre indicó documentar las ambigüedades sin asumir resultados. Se registran como **Blocked / AMBIGUO**, conservando las acciones y observaciones reales. No se modifican las especificaciones recibidas ni se afirman defectos de Todo.ly sin criterio suficiente.

| Caso | Observación real | Definición pendiente | Ejecución final |
|---|---|---|---|
| TC-2 / TC-002 | Email vacío rechazado: asterisco Email y Error. Please correct the missing fields.; sin sesión. | La precondición sobre inexistencia de cuenta asociada al nombre no identifica un medio o criterio verificable. No se supone unicidad del nombre. | 23 |
| TC-10 / TC-033 | Se ejecutaron los datos literales de Steps; acceso aceptado y posterior Logout. | Summary y Steps contienen pares distintos. El grupo debe unificarlos; no se elige una pareja como definición correcta. | 22 |
| TC-12 / TC-043 | Email vacío rechazado con Wrong email or password; sin señal específica del campo. | Precisar si el mensaje genérico satisface la validación Email y qué señal exige. | 21 |
| TC-13 / TC-044 | Password vacío rechazado con Wrong email or password; sin señal específica del campo. | Precisar si el mensaje genérico satisface la validación Password y qué señal exige. | 18 |
| TC-14 / TC-045 | Ambos vacíos rechazados con Wrong email or password; sin señal específica de los campos. | Precisar las validaciones observables de los campos obligatorios. | 19 |

TC-15 especifica credenciales no válidas **o** cuenta inexistente: el rechazo genérico observado cumple ese esperado. No acredita por sí solo la inexistencia de la cuenta; se usó el correo reservado que la ficha proporciona como no registrado.

Las notas por paso de los cinco casos ambiguos y de TC-15 se comprobaron en Print tras completar su registro nativo. Las primeras ejecuciones TC-2 y TC-10 con Passed se conservan en el historial, sustituidas por el último veredicto Blocked.
