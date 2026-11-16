# AGENTS.md — Instrucciones permanentes para Codex

## Qué es este repositorio

Es el espacio de trabajo para analizar, diseñar, registrar en TestLink y documentar en Jira los tickets **T09, T10 y T11** de la práctica de pruebas de caja negra sobre Todo.ly (Gestión de Calidad, UCB SIS-312, Grupo 5).

Es una práctica evaluada y crítica. Importan más la calidad, la trazabilidad y la honestidad de la documentación que la cantidad de casos.

## Orden de precedencia de las fuentes

Cuando dos fuentes se contradicen, manda la que aparece primero:

1. Lo que el usuario diga en el chat.
2. `docs/decisiones-vigentes.md`.
3. `docs/guia-diseno-casos-prueba-todoly.md`.
4. `docs/PlanPruebasTodo.ly.pdf`.
5. `docs/material-clase/`: definiciones de técnicas y plantillas del docente.
6. Tickets de referencia en Jira: T06 (PEB-70) y T12 (PEB-76).

## Herramientas

| Herramienta | Uso |
|---|---|
| Jira (alesalve.atlassian.net, proyecto PEB) | Leer tickets de referencia; escribir solo en T09, T10 y T11. |
| TestLink (http://68.211.149.112, sesión ya iniciada en Chrome) | Registrar los casos de T09, T10 y T11. |
| Todo.ly (https://todo.ly) | Explorar solo con las cuentas de prueba A y B creadas para este trabajo. |

## Reglas de oro

1. **Alcance.** Trabajas solo en T09, T10 y T11. Los demás tickets de Jira y los casos de otros tickets en TestLink son de solo lectura.
2. **Cuentas.** Nunca uses la cuenta de Camila ni ninguna cuenta personal del equipo. No inicies sesión con ellas y no cierres su sesión si está abierta.
3. **Aislamiento del navegador.** Abre Todo.ly en un perfil de Chrome dedicado o en una ventana de incógnito. No borres cookies ni datos globales de Chrome, porque perderías las sesiones de TestLink y Jira.
4. **Secretos.** Las contraseñas van solo en `.secrets/cuentas-prueba.local.md`, que git ignora. Nunca las pongas en commits, Jira, TestLink ni capturas.
5. **Nada inventado.** No inventes reglas, límites, mensajes, controles ni funciones. Clasifica cada regla como Regla documentada, Comportamiento observado, Criterio del equipo o Duda pendiente.
6. **Estados honestos.** Explorar no es ejecutar un caso. No digas que algo está registrado, revisado o ejecutado sin evidencia real.
7. **Jira.** No cierres tickets, no cambies su estado y no marques revisiones. La revisión la hace otro integrante.
8. **Jerarquías.** Se trabajan subproyectos. Las tareas padre/subtareas quedan fuera.
9. **Irreversibles.** Pregunta antes de cualquier acción irreversible que no afecte solo a las cuentas de prueba.

## Idioma y estilo

- Escribe en español.
- Conserva en inglés, tal como aparecen, los nombres de controles y mensajes de Todo.ly y TestLink.
- En Jira, redacta en tercera persona, claro y verificable.

## Convenciones

- Datos creados en Todo.ly: `Prueba T09-03 - descripción breve`. Usa nombres únicos.
- Casos: numeración por ticket (T09-01, T09-02…), salvo que TestLink asigne su propio ID. No crees identificadores nuevos del tipo BP o CQ.
- Archivos de trabajo: `trabajo/T0X/exploracion.md` y `trabajo/T0X/analisis-diseno.md`.
- Evidencias: `trabajo/T0X/evidencias/AAAA-MM-DD_T0X_descripcion.png`.
- Exportaciones XML: `testlink-xml/T0X.xml`.

## Estructura del repositorio

```
AGENTS.md                     reglas permanentes (este archivo)
SUPER_PROMPT.md               la tarea, por fases
docs/decisiones-vigentes.md   decisiones que prevalecen sobre la guía
docs/guia-diseno-casos-prueba-todoly.md
docs/PlanPruebasTodo.ly.pdf
docs/material-clase/          PDFs del docente
plantillas/                   formatos de trabajo
trabajo/                      lo que produces tú
testlink-xml/                 exportaciones de TestLink
.secrets/                     credenciales locales (no se suben)
```

## Git

- Haz un commit al terminar cada fase o cada ticket, con mensajes como `T09: análisis y diseño`.
- Antes de cada commit, verifica que `.secrets/` no esté incluido.
- Haz push si el repositorio tiene un remoto configurado.

## Cuando tengas dudas

- Si una duda cambia el resultado esperado principal de un caso, deja ese caso como pendiente, continúa con los demás e infórmala.
- Si una duda bloquea un ticket completo, pregunta al usuario.
- Si necesitas un captcha, un correo de verificación o de recuperación, o una decisión de alcance, pídeselo al usuario. No entres a su correo.
