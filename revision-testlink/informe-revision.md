# Informe de revisión de casos de TestLink — Todo.ly

Proyecto **TL:Todo.ly**, suite **Todo.ly tests**. Respaldo usado: `respaldo-20261118-1620.json` (83 casos, última versión de cada uno, con pasos).

Regla aplicada: se cambia cómo está escrito cada caso, nunca qué prueba. No se tocan IDs, importancia, tipo de ejecución, estado ni suite.

## 1. Resumen

| Ticket | Requerimiento | Casos en TestLink | OK | EDITAR | DUDA | Sin revisar | Nota |
|---|---|---|---|---|---|---|---|
| T06 | PEB-70 | 9 | 0 | 8 | 1 | 0 |  |
| T07 | PEB-71 | 6 | 0 | 6 | 0 | 0 |  |
| T08 | PEB-72 | 10 | 0 | 10 | 0 | 0 |  |
| T09 | PEB-73 | 13 | 0 | 0 | 0 | 13 | Codex los está registrando; se revisarán cuando termine. |
| T10 | PEB-74 | 6 | 0 | 6 | 0 | 0 | Propuestas preparadas, **bloqueadas**: Codex sigue registrando T10-04 a T10-06. |
| T11 | PEB-75 | 0 | 0 | 0 | 0 | 0 | Codex los está registrando; se revisarán cuando termine. |
| T12 | PEB-76 | 14 | 0 | 14 | 0 | 0 | 7 casos con **conflicto**: `admin` los editó en TestLink después del primer respaldo; no se aplican sin tu decisión. |
| T13 | PEB-77 | 13 | 0 | 12 | 1 | 0 |  |
| T14 | PEB-78 | 12 | 0 | 5 | 7 | 0 |  |
| **Total** | | **83** | **0** | **61** | **9** | **13** | |

Clasificación:

- **OK:** cumple la rúbrica; no se toca.
- **EDITAR:** se reescribe con información que ya está en el caso o en las fuentes.
- **DUDA:** también tiene propuesta de forma, pero una parte del resultado o de los datos no se puede precisar sin inventar; esa parte queda con su redacción original (sección 4).

### Criterios de redacción aplicados

- **Título:** formato único `TXX-NN - funcionalidad + condición + resultado`, ≤ 90 caracteres aprox. T06 se numera según el orden actual en TestLink (T06-01 = TL-41 … T06-09 = TL-49). T07 y T08 usan el número que ya tenían los datos del caso (p. ej. *Prueba T07-01 - completar*). En T12, T13 y T14 `TL-0NN:` pasa a `T12-NN -`, `T13-NN -` o `T14-NN -` conservando el número (TL-015 → T13-15, TL-028 → T14-28). Si el texto del título ya cumplía, solo cambia el prefijo. Ver la tabla de correspondencia (sección 3).
- **Summary:** `Descripción: Validar que…` (una oración) · `Requerimiento: PEB-XX / TXX` (se conserva el texto existente; en T06–T08, donde faltaba, se usa el nombre del área de la guía §3) · `Postcondiciones:` en lista numerada. En T10 se conserva además la línea `Importancia:` que usa el equipo.
- **Preconditions:** estados, una por línea, sin verbos de acción. Las credenciales que ya estaban se conservan; no se agregan contraseñas.
- **Steps nativos:** infinitivo, controles y datos en negrita, un resultado observable por paso, con el texto literal cuando existe. Varias acciones en un paso solo en preparación o limpieza con un único resultado (crear una tarea escribiendo + **Enter**/**Add**, crear varias tareas iguales, asignar una fecha que no es el objeto del caso, eliminar datos de prueba). Lo que el caso prueba va siempre en un paso propio con su resultado; una recarga con **F5** seguida de la consulta de una sola vista cuenta como un paso.
- **Mensajes de Sort By:** donde el caso selecciona un criterio, se usa el texto literal de la guía §15. Es el único texto de interfaz que se incorpora desde las fuentes.

## 2. Tabla de casos

Códigos de problema: **T** Título genérico o sin el resultado esperado; **PF** Título sin prefijo de ticket; **PV** Precondiciones con verbos de acción; **PS** Pasos escritos dentro del Summary; Steps nativos vacíos; **RS** Resultados esperados en una lista aparte, sin correspondencia paso a paso; **VQ** Descripción que no empieza con «Validar que…»; **RQ** Falta el requerimiento PEB-XX / TXX; **PC** Postcondiciones ausentes o incompletas; **NB** Controles y datos sin negrita; **MA** Varias acciones en un mismo paso; **DA** Datos o estado inicial no especificados; **RV** Resultado esperado vago o condicional.

| ID | Ticket | Clasif. | Título antes | Título después | Problemas | Cambios |
|---|---|---|---|---|---|---|
| TL-2 | T12 | EDITAR | TL-002: Escribir el vencimiento con la palabra today | T12-02 - Escribir today asigna Today 10:00 AM y ubica la tarea en Today | PV, PS, RS, VQ, PC, NB, T | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Se añaden las consultas de Inbox y Next que el resultado original ya exigía («no aparece en Inbox ni en Next») |
| TL-3 | T12 | EDITAR | TL-003: Escribir el vencimiento con la palabra tomorrow | T12-03 - Escribir tomorrow asigna Tomorrow 10:00 AM y ubica la tarea en Next | PV, PS, RS, VQ, PC, NB, T | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Se añade la consulta de Inbox que el resultado original ya exigía |
| TL-4 | T12 | EDITAR | TL-004: Escribir el vencimiento con el nombre de un día de la semana | T12-04 - Escribir Friday como vencimiento asigna el próximo viernes a las 10:00 AM | PV, PS, RS, VQ, PC, NB, T | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; El calendario real pasa de los pasos a las precondiciones como recurso disponible |
| TL-5 | T12 | EDITAR | TL-005: Cambiar un vencimiento ya guardado | T12-05 - Cambiar el vencimiento de tomorrow a today mueve la tarea de Next a Today | PV, PS, RS, VQ, PC, NB, T, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos |
| TL-6 | T12 | EDITAR | TL-006: Quitar el vencimiento de una tarea | T12-06 - Borrar el vencimiento deja la tarea sin fecha y la devuelve a Inbox | PV, PS, RS, VQ, PC, NB, T, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos |
| TL-7 | T12 | EDITAR | TL-007: Aceptar una fecha pasada y marcarla como vencida | T12-07 - Una fecha pasada (yesterday) se acepta y la tarea se marca como 1 day overdue | PV, PS, RS, VQ, PC, NB, T | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado |
| TL-8 | T12 | EDITAR | TL-008: Revisar los límites entre hoy y mañana | T12-08 - Una tarea de hoy 23:59 queda en Today y una de mañana 00:00 queda en Next | PV, PS, RS, VQ, PC, NB, T, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos |
| TL-9 | T12 | EDITAR | TL-009: Postergar una tarea 1 día y 1 semana | T12-09 - Postpone 1 week y 1 day adelantan la fecha y conservan la hora 10:00 AM | PV, PS, RS, VQ, PC, NB, T, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos |
| TL-10 | T12 | EDITAR | TL-010: Escribir una fecha sin indicar la hora | T12-10 - Una fecha sin hora se guarda sin error con la hora por defecto 10:00 AM | PV, PS, RS, VQ, PC, NB, T, RV | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Parte vaga conservada con su redacción original (ver dudas) |
| TL-11 | T12 | EDITAR | TL-011: Rechazar una fecha inválida | T12-11 - Una fecha inválida muestra un aviso y no cambia el vencimiento de la tarea | PV, PS, RS, VQ, PC, NB, T, MA, RV | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Parte vaga conservada con su redacción original (ver dudas) |
| TL-12 | T12 | EDITAR | TL-012: Aplicar un vencimiento por defecto a las tareas nuevas | T12-12 - New Task Due Date en Tomorrow asigna esa fecha a las tareas nuevas; None no | PV, PS, RS, VQ, PC, NB, T, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos |
| TL-13 | T12 | EDITAR | TL-013: Mostrar el año cuando el vencimiento es de otro año | T12-13 - Un vencimiento de otro año muestra el año en la etiqueta de la tarea | PV, PS, RS, VQ, PC, NB, T | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado |
| TL-14 | T12 | EDITAR | TL-014: Comprobar la coherencia entre la zona horaria y la hora mostrada | T12-14 - Cambiar Time Zone en Profile ajusta la hora mostrada del vencimiento | PV, PS, RS, VQ, PC, NB, T, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos |
| TL-15 | T13 | EDITAR | TL-015: Una tarea nueva sin fecha aparece en Inbox | T13-15 - Una tarea nueva sin fecha aparece en Inbox | PV, PS, RS, VQ, PC, NB, DA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Estado inicial concreto en precondiciones; Se añade a las precondiciones el proyecto Work, que el caso consulta |
| TL-16 | T13 | EDITAR | TL-016: Una tarea dentro de un proyecto no aparece en Inbox | T13-16 - Una tarea sin fecha creada en el proyecto Work no aparece en Inbox | PV, PS, RS, VQ, PC, NB, T | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado |
| TL-17 | T13 | EDITAR | TL-017: Al asignar la fecha de hoy la tarea pasa de Inbox a Today | T13-17 - Al asignar la fecha de hoy la tarea pasa de Inbox a Today | PV, PS, RS, VQ, PC, NB | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita |
| TL-18 | T13 | EDITAR | TL-018: Al asignar la fecha de mañana la tarea pasa a Next | T13-18 - Al asignar la fecha de mañana la tarea pasa a Next | PV, PS, RS, VQ, PC, NB | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita |
| TL-19 | T13 | EDITAR | TL-019: Al asignar una fecha pasada la tarea aparece en Today como vencida | T13-19 - Al asignar una fecha pasada la tarea aparece en Today como vencida | PV, PS, RS, VQ, PC, NB | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita |
| TL-20 | T13 | EDITAR | TL-020: Al quitar la fecha la tarea vuelve a Inbox | T13-20 - Al quitar la fecha la tarea vuelve a Inbox | PV, PS, RS, VQ, PC, NB, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Acciones separadas en pasos |
| TL-21 | T13 | EDITAR | TL-021: Al mover una tarea de Inbox a un proyecto deja de ser parte de Inbox | T13-21 - Arrastrar una tarea de Inbox al proyecto Work la saca de Inbox sin duplicarla | PV, PS, RS, VQ, PC, NB, T | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado |
| TL-22 | T13 | EDITAR | TL-022: Completar una tarea la saca del filtro y la envía a Done Items | T13-22 - Completar una tarea la saca del filtro y la envía a Done Items | PV, PS, RS, VQ, PC, NB | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita |
| TL-23 | T13 | EDITAR | TL-023: Los contadores de Inbox, Today y Next se actualizan correctamente | T13-23 - Crear y fechar una tarea cambia en 1 los contadores de Inbox, Today y Next | PV, PS, RS, VQ, PC, NB, T | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Se añade abrir Today antes de cambiar la fecha: con fecha de hoy la tarea ya no está en Inbox (T13-17); «Sin número = 0» tomado de la guía §11 (la interfaz puede ocultar la insignia) |
| TL-24 | T13 | EDITAR | TL-024: Mover una tarea entre Today y Next cambiando solo la fecha | T13-24 - Cambiar solo la fecha mueve la tarea entre Today y Next y conserva su prioridad | PV, PS, RS, VQ, PC, NB, T, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Se abre Today antes de asignar la prioridad: tras guardar today la tarea sale de Inbox (T13-17) |
| TL-25 | T13 | DUDA | TL-025: Comprobar que la etiqueta y el filtro de una tarea cuentan la misma historia | T13-25 - Una tarea con fecha de mañana sin hora muestra una etiqueta coherente con Next | PV, PS, RS, VQ, PC, NB, T, RV | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Parte vaga conservada con su redacción original (ver dudas) |
| TL-26 | T13 | EDITAR | TL-026: Comprobar que el orden dentro de Today y Next coincide con el criterio visible | T13-26 - El orden de las tareas en Today y Next coincide con el criterio de Sort By | PV, PS, RS, VQ, PC, NB, T, MA, RV | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Parte vaga conservada con su redacción original (ver dudas); Mensaje literal de Sort by Due Date tomado de la guía §15 |
| TL-27 | T13 | EDITAR | TL-027: Una tarea completada deja de contar en los filtros inteligentes | T13-27 - Completar tareas las saca de Inbox, Today y Next y baja en 1 cada contador | PV, PS, RS, VQ, PC, NB, T, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos |
| TL-28 | T14 | EDITAR | TL-028: Asignar la prioridad 1 a una tarea | T14-28 - Asignar la prioridad 1 muestra la tarea en rojo y negrita y se conserva tras F5 | PV, PS, RS, VQ, PC, NB, T | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado |
| TL-29 | T14 | EDITAR | TL-029: Las cuatro prioridades se distinguen entre sí | T14-29 - Las prioridades 1 a 4 se distinguen por color y negrita y se conservan tras F5 | PV, PS, RS, VQ, PC, NB, T, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos |
| TL-30 | T14 | DUDA | TL-030: Ordenar por Order y reordenar las tareas arrastrando | T14-30 - Con Sort By Order, arrastrar una tarea al primer lugar la reordena y se conserva | PV, PS, RS, VQ, PC, NB, T, DA, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Estado inicial concreto en precondiciones; Acciones separadas en pasos; Mensaje literal de Sort by Order tomado de la guía §15 |
| TL-31 | T14 | DUDA | TL-031: Ordenar las tareas por Priority | T14-31 - Sort By Priority ordena las tareas de la prioridad 1 a la prioridad 4 | PV, PS, RS, VQ, PC, NB, T, DA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Estado inicial concreto en precondiciones; Mensaje literal de Sort by Priority tomado de la guía §15 |
| TL-32 | T14 | EDITAR | TL-032: Las tareas con la misma prioridad mantienen un orden estable | T14-32 - Las tareas con la misma prioridad mantienen un orden estable | PV, PS, RS, VQ, PC, NB, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Acciones separadas en pasos; Mensajes literales de Sort by Order y Sort by Priority tomados de la guía §15 |
| TL-33 | T14 | DUDA | TL-033: Ordenar las tareas por Due Date | T14-33 - Sort By Due Date ordena las tareas de la fecha más cercana a la más lejana | PV, PS, RS, VQ, PC, NB, T, DA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Estado inicial concreto en precondiciones; Mensaje literal de Sort by Due Date tomado de la guía §15 |
| TL-34 | T14 | DUDA | TL-034: Ubicación de las tareas sin vencimiento al ordenar por Due Date | T14-34 - Con Sort By Due Date, las tareas sin vencimiento quedan en una posición estable | PV, PS, RS, VQ, PC, NB, T, RV | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Parte vaga conservada con su redacción original (ver dudas); Mensaje literal de Sort by Due Date tomado de la guía §15 |
| TL-35 | T14 | DUDA | TL-035: Cambiar entre criterios de orden y reconocer el criterio activo | T14-35 - Sort By muestra el criterio elegido (Order, Priority o Due Date) tras F5 | PV, PS, RS, VQ, PC, NB, T, DA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Estado inicial concreto en precondiciones; Mensajes literales de Sort By tomados de la guía §15 |
| TL-36 | T14 | DUDA | TL-036: En Priority y Due Date no se puede reordenar arrastrando | T14-36 - En Priority y Due Date no se puede reordenar arrastrando | PV, PS, RS, VQ, PC, NB, DA, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Estado inicial concreto en precondiciones; Acciones separadas en pasos; Mensajes literales de Sort By tomados de la guía §15 |
| TL-37 | T14 | EDITAR | TL-037: Reconocer la prioridad sin depender únicamente del color | T14-37 - Reconocer la prioridad sin depender únicamente del color | PV, PS, RS, VQ, PC, NB, RV | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Parte vaga conservada con su redacción original (ver dudas) |
| TL-38 | T14 | DUDA | TL-038: Cambiar la prioridad mientras la lista está ordenada por Priority | T14-38 - Con Sort By Priority, subir una tarea a prioridad 1 la reubica sin recargar | PV, PS, RS, VQ, PC, NB, T, DA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Estado inicial concreto en precondiciones; Mensaje literal de Sort by Priority tomado de la guía §15 |
| TL-39 | T14 | EDITAR | TL-039: La prioridad no cambia el filtro donde aparece la tarea | T14-39 - La prioridad no cambia el filtro donde aparece la tarea | PV, PS, RS, VQ, PC, NB, MA | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Acciones separadas en pasos; Se indica en qué filtro está la tarea antes de cada cambio de fecha, porque sale de Inbox al tener fecha (T13-17) |
| TL-40 | T12 | EDITAR | TL-001: Asignar un vencimiento con fecha y hora | T12-01 - Asignar fecha y hora de vencimiento las muestra en la tarea y la ubica en Next | PV, PS, RS, VQ, PC, NB, T | Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Cada paso con su resultado esperado; Descripción en una oración «Validar que…»; Postcondiciones explícitas al final del Summary; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Postcondición «la cuenta queda como estaba» precisada: la tarea eliminada queda en Recycle Bin (guía §14.1 y §17) |
| TL-41 | T06 | EDITAR | Crear una tarea mediante Add | T06-01 - Crear una tarea con Add la agrega una sola vez a Home y se conserva tras F5 | PF, PV, PS, VQ, NB, T | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado |
| TL-42 | T06 | EDITAR | Crear una tarea mediante Enter | T06-02 - Crear una tarea con Enter la agrega una sola vez a Home y se conserva tras F5 | PF, PV, PS, VQ, NB, T, RQ | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Requerimiento PEB-XX / TXX añadido |
| TL-43 | T06 | EDITAR | Editar directamente una tarea y guardar | T06-03 - Editar una tarea con clic sobre su nombre y Enter guarda el nombre nuevo tras F5 | PF, PV, PS, VQ, NB, T, RQ, MA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Requerimiento PEB-XX / TXX añadido; Acciones separadas en pasos |
| TL-44 | T06 | EDITAR | Editar una tarea desde su menú de opciones | T06-04 - Editar con Edit del menú de opciones cambia solo la tarea elegida | PF, PV, PS, VQ, NB, T, RQ, MA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Requerimiento PEB-XX / TXX añadido; Acciones separadas en pasos |
| TL-45 | T06 | EDITAR | Guardar una edición al hacer clic fuera | T06-05 - Hacer clic fuera del editor guarda la edición de una tarea y se conserva tras F5 | PF, PV, PS, VQ, NB, T, RQ, MA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Requerimiento PEB-XX / TXX añadido; Acciones separadas en pasos |
| TL-46 | T06 | EDITAR | Cancelar una modificación mediante Escape | T06-06 - Presionar Escape durante la edición descarta el cambio y conserva el texto original | PF, PV, PS, VQ, NB, T, RQ, MA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Requerimiento PEB-XX / TXX añadido; Acciones separadas en pasos |
| TL-47 | T06 | EDITAR | Conservar atributos y contenido entre sesiones | T06-07 - Editar el nombre conserva prioridad, vencimiento y estado tras F5 y nueva sesión | PF, PV, PS, VQ, NB, T, RQ, MA, DA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Requerimiento PEB-XX / TXX añadido; Acciones separadas en pasos; Estado inicial concreto en precondiciones |
| TL-48 | T06 | DUDA | Intentar crear una tarea vacía o con espacios | T06-08 - Pulsar Add con el campo vacío o con cinco espacios no crea ninguna tarea | PF, PV, PS, VQ, NB, T, RQ, RV | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Requerimiento PEB-XX / TXX añadido; Parte vaga conservada con su redacción original (ver dudas); «La tarea se crea correctamente» reemplazado por un resultado observable |
| TL-49 | T06 | EDITAR | Intentar incorporar archivos al campo de creación de tareas | T06-09 - Arrastrar un archivo al campo de creación no adjunta archivos ni crea tareas | PF, PV, PS, VQ, NB, T, RQ, MA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Requerimiento PEB-XX / TXX añadido; Acciones separadas en pasos; La repetición por formato, antes implícita («después de evaluar todos los archivos»), queda como paso explícito |
| TL-50 | T07 | EDITAR | Completar una tarea independiente | T07-01 - Completar una tarea la pasa a Done Items sin afectar a otra pendiente | PF, PV, PS, VQ, RQ, NB, DA, T, MA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Estado inicial concreto en precondiciones; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Precondición «Home sin pendientes ni completadas» añadida porque el caso espera cantidades exactas (guía §10) |
| TL-51 | T07 | EDITAR | Reactivar una tarea completada | T07-02 - Reactivar una tarea completada la devuelve a pendientes | PF, PV, PS, VQ, RQ, NB, DA, MA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Estado inicial concreto en precondiciones; Acciones separadas en pasos; Precondición «Home sin pendientes ni completadas» añadida porque el caso espera cantidades exactas (guía §10); Título igual al ejemplo de la rúbrica (solo se añade el prefijo) |
| TL-52 | T07 | EDITAR | Consultar y ocultar tareas completadas | T07-03 - See all, Done Items y el contador muestran las completadas; Hide las oculta | PF, PV, PS, VQ, RQ, NB, DA, T, MA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Estado inicial concreto en precondiciones; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Precondición «Home sin pendientes ni completadas» añadida porque el caso espera cantidades exactas (guía §10) |
| TL-53 | T07 | EDITAR | Mantener independientes los estados e indicadores de cada proyecto | T07-04 - Completar una tarea en Home no cambia estados ni contadores de Study | PF, PV, PS, VQ, RQ, NB, DA, T, MA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Estado inicial concreto en precondiciones; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Precondiciones «Home y Study sin pendientes ni completadas» añadidas porque el caso espera cantidades exactas (guía §10) |
| TL-54 | T07 | EDITAR | Conservar estados e indicadores después de recargar y volver a iniciar sesión | T07-09 - Estados e indicadores se conservan tras F5 y tras cerrar e iniciar sesión | PF, PV, PS, VQ, RQ, NB, DA, T, MA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Estado inicial concreto en precondiciones; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Precondición «Home sin pendientes ni completadas» añadida porque el caso espera cantidades exactas (guía §10) |
| TL-55 | T07 | EDITAR | Mantener la coherencia al repetir completar y reactivar | T07-10 - Dos ciclos de completar y reactivar dejan una sola tarea pendiente | PF, PV, PS, VQ, RQ, NB, DA, T | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Estado inicial concreto en precondiciones; Título con funcionalidad, condición y resultado; Precondición «Home sin pendientes ni completadas» añadida porque el caso espera cantidades exactas (guía §10) |
| TL-56 | T08 | EDITAR | Eliminar una pendiente sin afectar a otras tareas | T08-01 - Eliminar una pendiente la envía a Recycle Bin sin afectar a otras tareas | PF, PV, PS, VQ, RQ, NB, T, MA, DA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Estado inicial concreto en precondiciones; Precondiciones «Home y Study sin pendientes ni completadas» añadidas porque el caso espera cantidades exactas (guía §10) |
| TL-57 | T08 | EDITAR | Eliminar una tarea completada | T08-02 - Eliminar una tarea completada la retira de Done Items y la envía a Recycle Bin | PF, PV, PS, VQ, RQ, NB, T, MA, DA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Estado inicial concreto en precondiciones; Precondición de proyecto sin pendientes ni completadas añadida porque el caso espera cantidades exactas (guía §10) |
| TL-58 | T08 | EDITAR | Eliminar todas las completadas únicamente del proyecto seleccionado | T08-03 - Delete all elimina solo las completadas del proyecto seleccionado | PF, PV, PS, VQ, RQ, NB, T, MA, DA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Estado inicial concreto en precondiciones; Precondiciones «Home y Study sin pendientes ni completadas» añadidas porque el caso espera cantidades exactas (guía §10) |
| TL-59 | T08 | EDITAR | Intentar Delete all cuando no existen completadas | T08-04 - Delete all sin tareas completadas no elimina ninguna tarea pendiente | PF, PV, PS, VQ, RQ, NB, T, MA, DA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Estado inicial concreto en precondiciones; Precondición de proyecto sin pendientes ni completadas añadida porque el caso espera cantidades exactas (guía §10) |
| TL-60 | T08 | EDITAR | Recuperar una pendiente en su proyecto original | T08-05 - Arrastrar una pendiente de Recycle Bin a Home la recupera como pendiente | PF, PV, PS, VQ, RQ, NB, T, MA, DA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Estado inicial concreto en precondiciones; Precondición de proyecto sin pendientes ni completadas añadida porque el caso espera cantidades exactas (guía §10) |
| TL-61 | T08 | EDITAR | Recuperar una completada en otro proyecto conservando su estado | T08-06 - Recuperar en Study una completada eliminada de Home conserva su estado | PF, PV, PS, VQ, RQ, NB, T, MA, DA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Estado inicial concreto en precondiciones; Precondición «Study sin pendientes ni completadas» añadida porque el caso espera cantidades exactas en Study (guía §10) |
| TL-62 | T08 | EDITAR | Conservar la eliminación después de recargar y volver a iniciar sesión | T08-07 - Una tarea eliminada sigue fuera de Home tras F5 y tras iniciar sesión otra vez | PF, PV, PS, VQ, RQ, NB, T, MA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos |
| TL-63 | T08 | EDITAR | Cancelar la eliminación de un subproyecto con tareas | T08-08 - Cancelar la eliminación de un subproyecto conserva el subproyecto y sus tareas | PF, PV, PS, VQ, RQ, NB, T, MA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos |
| TL-64 | T08 | EDITAR | Confirmar la eliminación de un subproyecto y recuperar una tarea | T08-09 - Eliminar un subproyecto envía sus tareas a Recycle Bin y una se puede recuperar | PF, PV, PS, VQ, RQ, NB, T, MA, DA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Estado inicial concreto en precondiciones; Precondición «Proyecto Work existente» añadida: el caso coloca el subproyecto dentro de Work |
| TL-65 | T08 | EDITAR | Vaciar la papelera sin afectar a tareas de los proyectos | T08-10 - Empty Recycle Bin vacía la papelera sin afectar a las tareas de Home | PF, PV, PS, VQ, RQ, NB, T, MA, DA | Prefijo de ticket añadido; Precondiciones reescritas como estados, una por línea; Pasos migrados a Steps nativos; Descripción en una oración «Validar que…»; Requerimiento PEB-XX / TXX añadido; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos; Estado inicial concreto en precondiciones; Precondición de proyecto sin pendientes ni completadas añadida porque el caso espera cantidades exactas (guía §10); Precondición «Recycle Bin solo con contenido desechable» tomada de la guía §14.6 |
| TL-66 | T10 | EDITAR (bloqueado) | T10-01. Cancelar la modificación del nombre conserva el perfil | T10-01 - Cancelar la modificación del nombre conserva el perfil | VQ, NB, MA | Descripción en una oración «Validar que…»; Controles y datos en negrita; Acciones separadas en pasos |
| TL-67 | T10 | EDITAR (bloqueado) | T10-02. Guardar el nombre y conservarlo tras recarga y nueva sesión | T10-02 - Guardar un nombre nuevo con Ok lo conserva tras recarga y nueva sesión | VQ, NB, T, MA | Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos |
| TL-68 | T10 | EDITAR (bloqueado) | T10-03. Intentar cambiar la contraseña sin indicar la contraseña actual | T10-03 - Old Password vacío al cambiar la contraseña muestra Invalid Password y no la cambia | VQ, NB, T, MA | Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Acciones separadas en pasos |
| TL-69 | T10 | EDITAR (bloqueado) | T10-08. Recuperar el acceso de una cuenta registrada mediante su buzón | T10-08 - Recuperar el acceso por correo permite entrar con la nueva contraseña | VQ, NB, T | Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado; Descripción técnica previa («Recorrer solicitud, correo, formulario y Login posterior. Las condiciones de seguridad…») resumida en la oración «Validar que…» |
| TL-70 | T10 | EDITAR (bloqueado) | T10-09. Solicitar recuperación con un correo no registrado | T10-09 - Pedir Reset your Password con un correo no registrado muestra un error | VQ, NB, T | Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado |
| TL-71 | T10 | EDITAR (bloqueado) | T10-10. Comprobar HTTPS en el enlace de recuperación recibido | T10-10 - El enlace de recuperación recibido por correo usa HTTPS | VQ, NB, T | Descripción en una oración «Validar que…»; Controles y datos en negrita; Título con funcionalidad, condición y resultado |

## 3. Correspondencia de títulos

| ID TestLink | Título anterior | Título nuevo |
|---|---|---|
| TL-2 | TL-002: Escribir el vencimiento con la palabra today | T12-02 - Escribir today asigna Today 10:00 AM y ubica la tarea en Today |
| TL-3 | TL-003: Escribir el vencimiento con la palabra tomorrow | T12-03 - Escribir tomorrow asigna Tomorrow 10:00 AM y ubica la tarea en Next |
| TL-4 | TL-004: Escribir el vencimiento con el nombre de un día de la semana | T12-04 - Escribir Friday como vencimiento asigna el próximo viernes a las 10:00 AM |
| TL-5 | TL-005: Cambiar un vencimiento ya guardado | T12-05 - Cambiar el vencimiento de tomorrow a today mueve la tarea de Next a Today |
| TL-6 | TL-006: Quitar el vencimiento de una tarea | T12-06 - Borrar el vencimiento deja la tarea sin fecha y la devuelve a Inbox |
| TL-7 | TL-007: Aceptar una fecha pasada y marcarla como vencida | T12-07 - Una fecha pasada (yesterday) se acepta y la tarea se marca como 1 day overdue |
| TL-8 | TL-008: Revisar los límites entre hoy y mañana | T12-08 - Una tarea de hoy 23:59 queda en Today y una de mañana 00:00 queda en Next |
| TL-9 | TL-009: Postergar una tarea 1 día y 1 semana | T12-09 - Postpone 1 week y 1 day adelantan la fecha y conservan la hora 10:00 AM |
| TL-10 | TL-010: Escribir una fecha sin indicar la hora | T12-10 - Una fecha sin hora se guarda sin error con la hora por defecto 10:00 AM |
| TL-11 | TL-011: Rechazar una fecha inválida | T12-11 - Una fecha inválida muestra un aviso y no cambia el vencimiento de la tarea |
| TL-12 | TL-012: Aplicar un vencimiento por defecto a las tareas nuevas | T12-12 - New Task Due Date en Tomorrow asigna esa fecha a las tareas nuevas; None no |
| TL-13 | TL-013: Mostrar el año cuando el vencimiento es de otro año | T12-13 - Un vencimiento de otro año muestra el año en la etiqueta de la tarea |
| TL-14 | TL-014: Comprobar la coherencia entre la zona horaria y la hora mostrada | T12-14 - Cambiar Time Zone en Profile ajusta la hora mostrada del vencimiento |
| TL-15 | TL-015: Una tarea nueva sin fecha aparece en Inbox | T13-15 - Una tarea nueva sin fecha aparece en Inbox |
| TL-16 | TL-016: Una tarea dentro de un proyecto no aparece en Inbox | T13-16 - Una tarea sin fecha creada en el proyecto Work no aparece en Inbox |
| TL-17 | TL-017: Al asignar la fecha de hoy la tarea pasa de Inbox a Today | T13-17 - Al asignar la fecha de hoy la tarea pasa de Inbox a Today |
| TL-18 | TL-018: Al asignar la fecha de mañana la tarea pasa a Next | T13-18 - Al asignar la fecha de mañana la tarea pasa a Next |
| TL-19 | TL-019: Al asignar una fecha pasada la tarea aparece en Today como vencida | T13-19 - Al asignar una fecha pasada la tarea aparece en Today como vencida |
| TL-20 | TL-020: Al quitar la fecha la tarea vuelve a Inbox | T13-20 - Al quitar la fecha la tarea vuelve a Inbox |
| TL-21 | TL-021: Al mover una tarea de Inbox a un proyecto deja de ser parte de Inbox | T13-21 - Arrastrar una tarea de Inbox al proyecto Work la saca de Inbox sin duplicarla |
| TL-22 | TL-022: Completar una tarea la saca del filtro y la envía a Done Items | T13-22 - Completar una tarea la saca del filtro y la envía a Done Items |
| TL-23 | TL-023: Los contadores de Inbox, Today y Next se actualizan correctamente | T13-23 - Crear y fechar una tarea cambia en 1 los contadores de Inbox, Today y Next |
| TL-24 | TL-024: Mover una tarea entre Today y Next cambiando solo la fecha | T13-24 - Cambiar solo la fecha mueve la tarea entre Today y Next y conserva su prioridad |
| TL-25 | TL-025: Comprobar que la etiqueta y el filtro de una tarea cuentan la misma historia | T13-25 - Una tarea con fecha de mañana sin hora muestra una etiqueta coherente con Next |
| TL-26 | TL-026: Comprobar que el orden dentro de Today y Next coincide con el criterio visible | T13-26 - El orden de las tareas en Today y Next coincide con el criterio de Sort By |
| TL-27 | TL-027: Una tarea completada deja de contar en los filtros inteligentes | T13-27 - Completar tareas las saca de Inbox, Today y Next y baja en 1 cada contador |
| TL-28 | TL-028: Asignar la prioridad 1 a una tarea | T14-28 - Asignar la prioridad 1 muestra la tarea en rojo y negrita y se conserva tras F5 |
| TL-29 | TL-029: Las cuatro prioridades se distinguen entre sí | T14-29 - Las prioridades 1 a 4 se distinguen por color y negrita y se conservan tras F5 |
| TL-30 | TL-030: Ordenar por Order y reordenar las tareas arrastrando | T14-30 - Con Sort By Order, arrastrar una tarea al primer lugar la reordena y se conserva |
| TL-31 | TL-031: Ordenar las tareas por Priority | T14-31 - Sort By Priority ordena las tareas de la prioridad 1 a la prioridad 4 |
| TL-32 | TL-032: Las tareas con la misma prioridad mantienen un orden estable | T14-32 - Las tareas con la misma prioridad mantienen un orden estable |
| TL-33 | TL-033: Ordenar las tareas por Due Date | T14-33 - Sort By Due Date ordena las tareas de la fecha más cercana a la más lejana |
| TL-34 | TL-034: Ubicación de las tareas sin vencimiento al ordenar por Due Date | T14-34 - Con Sort By Due Date, las tareas sin vencimiento quedan en una posición estable |
| TL-35 | TL-035: Cambiar entre criterios de orden y reconocer el criterio activo | T14-35 - Sort By muestra el criterio elegido (Order, Priority o Due Date) tras F5 |
| TL-36 | TL-036: En Priority y Due Date no se puede reordenar arrastrando | T14-36 - En Priority y Due Date no se puede reordenar arrastrando |
| TL-37 | TL-037: Reconocer la prioridad sin depender únicamente del color | T14-37 - Reconocer la prioridad sin depender únicamente del color |
| TL-38 | TL-038: Cambiar la prioridad mientras la lista está ordenada por Priority | T14-38 - Con Sort By Priority, subir una tarea a prioridad 1 la reubica sin recargar |
| TL-39 | TL-039: La prioridad no cambia el filtro donde aparece la tarea | T14-39 - La prioridad no cambia el filtro donde aparece la tarea |
| TL-40 | TL-001: Asignar un vencimiento con fecha y hora | T12-01 - Asignar fecha y hora de vencimiento las muestra en la tarea y la ubica en Next |
| TL-41 | Crear una tarea mediante Add | T06-01 - Crear una tarea con Add la agrega una sola vez a Home y se conserva tras F5 |
| TL-42 | Crear una tarea mediante Enter | T06-02 - Crear una tarea con Enter la agrega una sola vez a Home y se conserva tras F5 |
| TL-43 | Editar directamente una tarea y guardar | T06-03 - Editar una tarea con clic sobre su nombre y Enter guarda el nombre nuevo tras F5 |
| TL-44 | Editar una tarea desde su menú de opciones | T06-04 - Editar con Edit del menú de opciones cambia solo la tarea elegida |
| TL-45 | Guardar una edición al hacer clic fuera | T06-05 - Hacer clic fuera del editor guarda la edición de una tarea y se conserva tras F5 |
| TL-46 | Cancelar una modificación mediante Escape | T06-06 - Presionar Escape durante la edición descarta el cambio y conserva el texto original |
| TL-47 | Conservar atributos y contenido entre sesiones | T06-07 - Editar el nombre conserva prioridad, vencimiento y estado tras F5 y nueva sesión |
| TL-48 | Intentar crear una tarea vacía o con espacios | T06-08 - Pulsar Add con el campo vacío o con cinco espacios no crea ninguna tarea |
| TL-49 | Intentar incorporar archivos al campo de creación de tareas | T06-09 - Arrastrar un archivo al campo de creación no adjunta archivos ni crea tareas |
| TL-50 | Completar una tarea independiente | T07-01 - Completar una tarea la pasa a Done Items sin afectar a otra pendiente |
| TL-51 | Reactivar una tarea completada | T07-02 - Reactivar una tarea completada la devuelve a pendientes |
| TL-52 | Consultar y ocultar tareas completadas | T07-03 - See all, Done Items y el contador muestran las completadas; Hide las oculta |
| TL-53 | Mantener independientes los estados e indicadores de cada proyecto | T07-04 - Completar una tarea en Home no cambia estados ni contadores de Study |
| TL-54 | Conservar estados e indicadores después de recargar y volver a iniciar sesión | T07-09 - Estados e indicadores se conservan tras F5 y tras cerrar e iniciar sesión |
| TL-55 | Mantener la coherencia al repetir completar y reactivar | T07-10 - Dos ciclos de completar y reactivar dejan una sola tarea pendiente |
| TL-56 | Eliminar una pendiente sin afectar a otras tareas | T08-01 - Eliminar una pendiente la envía a Recycle Bin sin afectar a otras tareas |
| TL-57 | Eliminar una tarea completada | T08-02 - Eliminar una tarea completada la retira de Done Items y la envía a Recycle Bin |
| TL-58 | Eliminar todas las completadas únicamente del proyecto seleccionado | T08-03 - Delete all elimina solo las completadas del proyecto seleccionado |
| TL-59 | Intentar Delete all cuando no existen completadas | T08-04 - Delete all sin tareas completadas no elimina ninguna tarea pendiente |
| TL-60 | Recuperar una pendiente en su proyecto original | T08-05 - Arrastrar una pendiente de Recycle Bin a Home la recupera como pendiente |
| TL-61 | Recuperar una completada en otro proyecto conservando su estado | T08-06 - Recuperar en Study una completada eliminada de Home conserva su estado |
| TL-62 | Conservar la eliminación después de recargar y volver a iniciar sesión | T08-07 - Una tarea eliminada sigue fuera de Home tras F5 y tras iniciar sesión otra vez |
| TL-63 | Cancelar la eliminación de un subproyecto con tareas | T08-08 - Cancelar la eliminación de un subproyecto conserva el subproyecto y sus tareas |
| TL-64 | Confirmar la eliminación de un subproyecto y recuperar una tarea | T08-09 - Eliminar un subproyecto envía sus tareas a Recycle Bin y una se puede recuperar |
| TL-65 | Vaciar la papelera sin afectar a tareas de los proyectos | T08-10 - Empty Recycle Bin vacía la papelera sin afectar a las tareas de Home |
| TL-66 | T10-01. Cancelar la modificación del nombre conserva el perfil | T10-01 - Cancelar la modificación del nombre conserva el perfil |
| TL-67 | T10-02. Guardar el nombre y conservarlo tras recarga y nueva sesión | T10-02 - Guardar un nombre nuevo con Ok lo conserva tras recarga y nueva sesión |
| TL-68 | T10-03. Intentar cambiar la contraseña sin indicar la contraseña actual | T10-03 - Old Password vacío al cambiar la contraseña muestra Invalid Password y no la cambia |
| TL-69 | T10-08. Recuperar el acceso de una cuenta registrada mediante su buzón | T10-08 - Recuperar el acceso por correo permite entrar con la nueva contraseña |
| TL-70 | T10-09. Solicitar recuperación con un correo no registrado | T10-09 - Pedir Reset your Password con un correo no registrado muestra un error |
| TL-71 | T10-10. Comprobar HTTPS en el enlace de recuperación recibido | T10-10 - El enlace de recuperación recibido por correo usa HTTPS |

## 3b. Ejemplos completos de antes y después

Las contraseñas se muestran enmascaradas en este informe; en TestLink se conservan tal como estaban.

### 3b.1. Precondiciones con verbos: TL-41

#### Antes

**Título:** Crear una tarea mediante Add

**Summary:**

```
**Requerimiento:** PEB-70 / T06. La creación debe conservar el contenido enviado en el proyecto seleccionado.

**Descripción:** Comprobar la creación y persistencia de una tarea utilizando el botón Add.

**Pasos:**

| Paso | Resultado esperado
| 1. En el panel izquierdo, dentro de Projects, haz clic en **Home**. | El título del área principal muestra Home.
| 2. Haz clic en **Add new Todo, type here…** y escribe **Prueba T06 - creación con Add**. | El campo contiene el texto introducido.
| 3. Haz clic una vez en **Add**, situado a la derecha. | Aparece una sola tarea con ese nombre.
| 4. Presiona **F5** y consulta nuevamente Home. | La tarea conserva su nombre y continúa en el proyecto.
| 5. Pasa el mouse sobre la tarea, abre su menú de opciones de la derecha y selecciona **Delete**. | La tarea desaparece de la lista activa.
**Postcondiciones:** La tarea de prueba está retirada de la lista activa. Las tareas preexistentes conservan su información.
```

**Preconditions:**

```
1.
Tener acceso a internet.

2.
Iniciar sesión con las credenciales correo: **camila@gmail.com** — contraseña: [oculta] en el sitio: https://todo.ly/).

3.
Existe el proyecto **Home**.

4.
Se dispone de un medio para tomar notas. Si un paso falla, se conservará la evidencia antes de limpiar los datos.
```

**Steps nativos:** ninguno

#### Después

**Título:** T06-01 - Crear una tarea con Add la agrega una sola vez a Home y se conserva tras F5

**Summary:**

- **Descripción:** Validar que una tarea creada con el botón Add en el proyecto Home se guarda una sola vez con el texto introducido y se conserva después de recargar la página.
- **Requerimiento:** PEB-70 / T06. La creación debe conservar el contenido enviado en el proyecto seleccionado.
- **Postcondiciones:**
  1. La tarea de prueba está retirada de la lista activa.
  2. Las tareas preexistentes conservan su información.

**Preconditions:**

1. Acceso a internet disponible.
2. Cuenta de Todo.ly registrada: correo **camila@gmail.com** / contraseña [oculta] (sitio https://todo.ly/).
3. Sesión iniciada en Todo.ly con esa cuenta.
4. Proyecto predeterminado **Home** existente.
5. Ninguna tarea existente con los nombres que usa este caso.
6. Medio para tomar notas y capturar evidencias disponible; ante un paso fallido, evidencia conservada antes de limpiar los datos.

**Steps nativos:**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Hacer clic en **Home**, dentro de **Projects**, en el panel izquierdo. | El título del área principal muestra **Home**. |
| 2 | Escribir **Prueba T06 - creación con Add** en el campo **Add new Todo, type here…**. | El campo contiene **Prueba T06 - creación con Add**. |
| 3 | Hacer clic una vez en **Add**, a la derecha del campo. | Aparece una sola tarea con el nombre **Prueba T06 - creación con Add**. |
| 4 | Presionar **F5** y consultar nuevamente **Home**. | La tarea conserva su nombre y continúa en **Home**. |
| 5 | Pasar el mouse sobre **Prueba T06 - creación con Add**, abrir su menú de opciones de la derecha y seleccionar **Delete**. | La tarea desaparece de la lista activa. |

### 3b.2. Título ambiguo: TL-50

#### Antes

**Título:** Completar una tarea independiente

**Summary:**

```
**Descripción:** Comprobar la finalización de una tarea independiente y la conservación de otra tarea pendiente.

| Paso | Resultado esperado
| 1. Abre **Home** y crea mediante **Add new Todo, type here…** y **Add** las tareas **Prueba T07-01 - completar** y **Prueba T07-01 - control**. | Aparecen dos tareas pendientes. Home indica **2** pendientes y **Done Items** muestra **0**.
| 2. Marca el checkbox situado a la izquierda de **Prueba T07-01 - completar**. | La seleccionada sale de pendientes. La de control permanece pendiente. Home indica **1** pendiente y **Done Items** muestra **1**.
| 3. Despliega las completadas mediante **See all**, si están ocultas. | La seleccionada aparece con su checkbox marcado y su texto tachado. La de control continúa en pendientes.
| 4. Presiona **F5**, abre nuevamente Home y despliega las completadas. | Se conserva una tarea pendiente y una completada. Los indicadores mantienen los valores **1** y **1**.
| 5. Desmarca la tarea completada. Después, elimina ambas mediante sus respectivos menús de opciones y **Delete**. | Las dos tareas desaparecen de la lista activa. Home queda sin pendientes y **Done Items** muestra **0**.
**Postcondiciones:** Las dos tareas están retiradas de Home y permanecen identificadas en Recycle Bin. Se conserva evidencia del cambio de estado y de los indicadores.
```

**Preconditions:**

```
1. Tener acceso a Internet.
2. Tener una sesión iniciada en Todo.ly con la cuenta camila@gmail.com, utilizando la contraseña de pruebas indicada.
3. Existe el proyecto predeterminado Home.
4. Se dispone de un medio para tomar notas y capturar evidencias. Si un paso falla, se conservará la evidencia antes de limpiar los datos.
```

**Steps nativos:** ninguno

#### Después

**Título:** T07-01 - Completar una tarea la pasa a Done Items sin afectar a otra pendiente

**Summary:**

- **Descripción:** Validar que marcar el checkbox de una tarea independiente la pasa a completadas, actualiza los indicadores de Home y Done Items y no modifica otra tarea pendiente.
- **Requerimiento:** PEB-71 / T07 — Estados de tareas e indicadores.
- **Postcondiciones:**
  1. Las dos tareas están retiradas de **Home** y permanecen identificadas en **Recycle Bin**.
  2. Se conserva evidencia del cambio de estado y de los indicadores.

**Preconditions:**

1. Acceso a internet disponible.
2. Cuenta de Todo.ly registrada: correo **camila@gmail.com**, con la contraseña de pruebas indicada por el equipo.
3. Sesión iniciada en Todo.ly con esa cuenta.
4. Proyecto predeterminado **Home** existente, sin tareas pendientes ni completadas.
5. Ninguna tarea existente con los nombres que usa este caso.
6. Medio para tomar notas y capturar evidencias disponible; ante un paso fallido, evidencia conservada antes de limpiar los datos.

**Steps nativos:**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Hacer clic en **Home**, dentro de **Projects**, en el panel izquierdo. | Se muestra el proyecto **Home**. |
| 2 | Escribir **Prueba T07-01 - completar** en el campo **Add new Todo, type here…** y hacer clic en **Add**. | La tarea **Prueba T07-01 - completar** aparece pendiente en **Home**. |
| 3 | Escribir **Prueba T07-01 - control** en el campo **Add new Todo, type here…** y hacer clic en **Add**. | Aparecen dos tareas pendientes. **Home** indica **2** pendientes y **Done Items** muestra **0**. |
| 4 | Marcar el checkbox situado a la izquierda de **Prueba T07-01 - completar**. | La seleccionada sale de pendientes y la de control permanece pendiente. **Home** indica **1** pendiente y **Done Items** muestra **1**. |
| 5 | Hacer clic en **See all**, si las completadas están ocultas. | **Prueba T07-01 - completar** aparece con su checkbox marcado y su texto tachado. La de control continúa en pendientes. |
| 6 | Presionar **F5** y abrir nuevamente **Home**. | Los indicadores mantienen los valores **1** pendiente y **1** en **Done Items**. |
| 7 | Desplegar las completadas con **See all**. | Se conserva una tarea pendiente y una completada. |
| 8 | Desmarcar el checkbox de **Prueba T07-01 - completar**. | La tarea vuelve a pendientes. |
| 9 | Pasar el mouse sobre **Prueba T07-01 - completar**, abrir su menú de opciones y seleccionar **Delete**. | La tarea desaparece de la lista activa. |
| 10 | Pasar el mouse sobre **Prueba T07-01 - control**, abrir su menú de opciones y seleccionar **Delete**. | Las dos tareas han desaparecido de la lista activa. **Home** queda sin pendientes y **Done Items** muestra **0**. |

### 3b.3. Pasos dentro del Summary: TL-15

#### Antes

**Título:** TL-015: Una tarea nueva sin fecha aparece en Inbox

**Summary:**

```
**Requerimiento:** PEB-77 / T13 — Inbox, Today y Next. Inbox debe recibir las tareas que todavía no tienen fecha ni proyecto.

**Pasos:**

1. En el panel de la izquierda, haz clic en _Inbox_.
2. En la parte inferior de la lista, haz clic en el campo _Add new task_.
3. Escribe el nombre exacto: **Prueba T13 - sin fecha**
4. Presiona **Enter**. La tarea aparece en la lista sin ninguna fecha a la derecha.
5. Abre _Today_ y busca la tarea.
6. Abre _Next_ y busca la tarea.
7. Abre el proyecto _Work_ y busca la tarea.
8. Vuelve a _Inbox_ y recarga con **F5**.
9. Al terminar, elimina la tarea con el menú de la derecha, opción _Delete_.

**Resultados esperados:**

1. La tarea **Prueba T13 - sin fecha** aparece en _Inbox_ inmediatamente después de presionar Enter.
2. La tarea no muestra ninguna fecha de vencimiento.
3. La tarea no aparece en _Today_, ni en _Next_, ni dentro de ningún proyecto.
4. Después de recargar, la tarea sigue en _Inbox_.
5. Al final la tarea de prueba queda eliminada.
```

**Preconditions:**

```
**Iniciar sesión:** correo: **camila@gmail.com** — contraseña: [oculta] (sitio: https://todo.ly/).

La cuenta no tiene tareas con los nombres que se crean en este caso, para que no se confundan entre sí.
```

**Steps nativos:** ninguno

#### Después

**Título:** T13-15 - Una tarea nueva sin fecha aparece en Inbox

**Summary:**

- **Descripción:** Validar que una tarea creada en Inbox sin fecha ni proyecto aparece solo en Inbox, no en Today, Next ni Work, y sigue allí después de recargar.
- **Requerimiento:** PEB-77 / T13 — Inbox, Today y Next. Inbox debe recibir las tareas que todavía no tienen fecha ni proyecto.
- **Postcondiciones:**
  1. La tarea **Prueba T13 - sin fecha** está eliminada mediante **Delete** y ya no aparece en Inbox, Today, Next ni en los proyectos (queda en **Recycle Bin**).
  2. Las demás tareas de la cuenta conservan su información.

**Preconditions:**

1. Cuenta de Todo.ly registrada: correo **camila@gmail.com** / contraseña [oculta] (sitio https://todo.ly/).
2. Sesión iniciada en Todo.ly con esa cuenta.
3. Proyecto **Work** existente en el panel izquierdo.
4. Ninguna tarea existente con los nombres que se crean en este caso, para que no se confundan entre sí.

**Steps nativos:**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Hacer clic en **Inbox** en el panel izquierdo. | Se muestra la lista **Inbox**. |
| 2 | Escribir **Prueba T13 - sin fecha** en el campo **Add new task** y presionar **Enter**. | La tarea **Prueba T13 - sin fecha** aparece en **Inbox** inmediatamente después de presionar **Enter**, sin ninguna fecha de vencimiento a la derecha. |
| 3 | Hacer clic en **Today** en el panel izquierdo. | La tarea no aparece en **Today**. |
| 4 | Hacer clic en **Next** en el panel izquierdo. | La tarea no aparece en **Next**. |
| 5 | Hacer clic en el proyecto **Work**, dentro de **Projects**, en el panel izquierdo. | La tarea no aparece dentro del proyecto **Work**. |
| 6 | Hacer clic en **Inbox** en el panel izquierdo. | La tarea sigue en **Inbox**. |
| 7 | Presionar **F5** para recargar la página. | Después de recargar, la tarea sigue en **Inbox**. |
| 8 | Pasar el mouse sobre **Prueba T13 - sin fecha**, abrir el menú de opciones de la derecha y seleccionar **Delete**. | La tarea **Prueba T13 - sin fecha** desaparece de **Inbox**. |

## 4. Pendientes para la autora del caso (casos DUDA)

Estos casos se aplican con la parte dudosa en su redacción original. Queda pendiente que quien redactó cada caso la precise:

- **TL-25** (T13-25): El resultado principal es condicional («si la etiqueta dice Tomorrow…») y el paso «si el campo lo permite, borra la hora» no fija el dato. Se conserva la redacción original; conviene que quien redactó el caso defina la etiqueta esperada.
- **TL-30** (T14-30): El caso parte de tareas ya existentes en Work sin nombrarlas, y el paso final elimina «las tareas de prueba» sin decir cuáles. Se conserva la redacción original; conviene fijar nombres concretos (por ejemplo, crear las tareas dentro del caso).
- **TL-31** (T14-31): El caso parte de tareas ya existentes en Work sin nombrarlas, y el paso final elimina «las tareas de prueba» sin decir cuáles. Se conserva la redacción original; conviene fijar nombres concretos (por ejemplo, crear las tareas dentro del caso).
- **TL-33** (T14-33): No se nombran las tareas a crear ni se prepara una tarea vencida, aunque un resultado la menciona. El caso parte de tareas ya existentes en Work sin nombrarlas, y el paso final elimina «las tareas de prueba» sin decir cuáles. Se conserva la redacción original; conviene fijar nombres concretos (por ejemplo, crear las tareas dentro del caso).
- **TL-34** (T14-34): El resultado principal es vago («lugar predecible, normalmente al final»). Se conserva tal cual; falta definir la posición esperada. Para observar si las tareas sin fecha se intercalan, Work debería tener tareas con fecha; el caso no las prepara.
- **TL-35** (T14-35): El caso no crea tareas, pero su último paso elimina «las tareas de prueba». Se conserva; falta definir con qué tareas se ejecuta.
- **TL-36** (T14-36): El caso parte de tareas ya existentes en Work sin nombrarlas, y el paso final elimina «las tareas de prueba» sin decir cuáles. Se conserva la redacción original; conviene fijar nombres concretos (por ejemplo, crear las tareas dentro del caso).
- **TL-38** (T14-38): El caso parte de tareas ya existentes en Work sin nombrarlas, y el paso final elimina «las tareas de prueba» sin decir cuáles. Se conserva la redacción original; conviene fijar nombres concretos (por ejemplo, crear las tareas dentro del caso).
- **TL-48** (T06-08): Los resultados esperados del caso están rotulados como «propuestos». La guía (§12) exige identificar si el rechazo de vacíos/espacios es regla o criterio del equipo; se conservan sin cambios hasta que el equipo lo confirme.

## 4b. Otras dudas y observaciones

- **TL-10** (T12): El original no indicaba resultado para la recarga con F5; se propone «la tarea sigue en Next con la misma fecha y hora» (mismo criterio que T12-02 a T12-07). Confirmar con quien redactó el caso.
- **TL-10** (T12): El resultado condicional «si no permite guardar sin hora, se anota como observación» se conserva tal cual.
- **TL-11** (T12): No hay texto literal del aviso de fecha inválida en el caso ni en las fuentes; se conserva «aparece un aviso indicando que la fecha no es válida».
- **TL-11** (T12): No se indica con qué control se cierra el panel sin guardar; se conserva «cerrar el panel si quedó abierto».
- **TL-12** (T12): El caso no registra el valor inicial de New Task Due Date ni lo restaura si era distinto de None.
- **TL-12** (T12): Control para guardar Settings: el caso dice «Save si la ventana lo muestra»; en T10 Settings muestra Ok y Cancel. Se conserva la redacción original.
- **TL-14** (T12): No se indica el control para guardar en Settings («Guarda y cierra»); se conserva la redacción original.
- **TL-26** (T13): El caso no restaura el criterio de Sort By al terminar; se deja indicado en las postcondiciones.
- **TL-37** (T14): El resultado del paso 5 es una instrucción condicional ante fallo («se registra como riesgo…»); se conserva tal cual.
- **TL-46** (T06): La guía (§12) indica que Escape se observó con dudas en algunas condiciones; el resultado esperado se conserva sin cambios.
- **TL-47** (T06): El paso de Set Due Date no fija la fecha a asignar («un vencimiento»); se conserva así y se pide anotarla. Si se quiere un dato fijo, lo debe definir el equipo.
- **TL-49** (T06): La guía (§12) indica que el rechazo de adjuntos es criterio del equipo, no regla oficial; el resultado «puede ignorar la entrada o informar que no está admitida» se conserva tal cual.
- **TL-65** (T08): No se conoce el texto de la confirmación de Empty Recycle Bin; se conserva «completar la confirmación si aparece».
- **Ediciones concurrentes:** después del primer respaldo (15:32), el usuario `admin` de TestLink modificó TL-66 (2026-11-18 20:11:39), TL-40 (2026-11-18 20:10:29), TL-2 (2026-11-18 20:11:00), TL-3 (2026-11-18 20:15:25), TL-4 (2026-11-18 20:15:49), TL-5 (2026-11-18 20:16:14), TL-6 (2026-11-18 20:19:19), TL-7 (2026-11-18 20:19:54) (hora del servidor). En T12 quitó «Requerimiento: PEB-76 / T12 —» del Summary y cambió «Iniciar sesión:» por «Credenciales Válidas:». Aplicar la propuesta sobrescribiría esos cambios; quedan sin aplicar hasta que decidas.
- **Renumeración T12–T14:** los títulos pasan de `TL-0NN:` a `T12-NN -`/`T13-NN -`/`T14-NN -`. El comentario de PEB-76 cita los nombres antiguos (TL-001…TL-039); la tabla de la sección 3 sirve de correspondencia.
- **T12–T13 (general):** el campo de creación figura como **Add new task**, mientras que T06–T08 y la guía §11 usan **Add new Todo, type here…**. Puede ser que el texto cambie entre Inbox y un proyecto; se conserva el de cada caso.
- **T06–T08 (general):** las precondiciones citan la cuenta de Camila con «la contraseña de pruebas indicada» (sin contraseña) y TL-41 la trae explícita. Se conservan como están; decisiones-vigentes §6–7 piden cuentas genéricas solo para T09–T11.
- **T09, T10 (T10-04 a T10-06) y T11:** Codex sigue registrándolos; no se revisan ni se editan hasta que termine. En el respaldo hay 13 casos sin revisar: TL-72, TL-73, TL-74, TL-75, TL-76, TL-77, TL-78, TL-79, TL-80, TL-81, TL-82, TL-83, TL-84.

## 5. Aplicación

Pendiente: se aplica después del OK del usuario (Fase 3).

## 6. Cómo revertir

El respaldo `respaldo-20261118-1620.json` contiene nombre, summary, preconditions y pasos de los 83 casos antes de cualquier cambio.

```bash
cd revision-testlink/scripts
# Simulación (no escribe): muestra qué casos difieren del respaldo
python3 revertir.py --respaldo ../respaldo-20261118-1620.json --todos
# Restaurar casos concretos
python3 revertir.py --respaldo ../respaldo-20261118-1620.json --ids TL-41,TL-42 --aplicar
# Restaurar todo
python3 revertir.py --respaldo ../respaldo-20261118-1620.json --todos --aplicar
```

La clave de la API se lee de `TESTLINK_DEVKEY`. Con `--aplicar`, el script vuelve a leer cada caso y confirma que coincide con el respaldo.
