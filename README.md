# Todo.ly QA — T09, T10 y T11

Espacio de trabajo para que Codex analice, diseñe, registre en TestLink y documente en Jira los tickets T09, T10 y T11 de la práctica de caja negra sobre Todo.ly (Gestión de Calidad, UCB SIS-312, Grupo 5).

## Cómo ponerlo en marcha

1. Crea un repositorio **privado** en GitHub (contiene los nombres del equipo y material del curso) y sube el contenido de esta carpeta.
2. Copia los PDFs de clase a `docs/material-clase/`. La lista está en `docs/material-clase/LEEME.md`.
3. Clona el repositorio en la PC donde corre Codex: la misma en la que Chrome tiene abiertos TestLink y Jira.
4. Abre `SUPER_PROMPT.md` y completa los dos correos de las cuentas de prueba. Si los dejas vacíos, Codex te los pedirá.
5. Abre Codex en la carpeta del repositorio y pega el contenido de `SUPER_PROMPT.md`.

Codex lee `AGENTS.md` automáticamente cuando trabaja en este repositorio. Ahí están las reglas permanentes.

## Contenido

| Ruta | Qué contiene |
|---|---|
| `AGENTS.md` | Reglas permanentes para Codex. |
| `SUPER_PROMPT.md` | La tarea completa, dividida en fases. |
| `docs/decisiones-vigentes.md` | Decisiones que prevalecen sobre la guía: áreas, cuentas de prueba, subproyectos sí y subtareas no, todo dentro de T09–T11. |
| `docs/guia-diseno-casos-prueba-todoly.md` | Guía del equipo, sin cambios. |
| `docs/PlanPruebasTodo.ly.pdf` | Plan maestro de pruebas. |
| `docs/material-clase/` | PDFs del docente (los copias tú). |
| `plantillas/` | Formatos del comentario de Jira, de la ficha de TestLink, del registro de exploración y del estado de cuenta. |
| `trabajo/T09`, `trabajo/T10`, `trabajo/T11` | Exploración, análisis, diseño y evidencias que genera Codex. |
| `testlink-xml/` | Exportaciones XML de TestLink. |
| `.secrets/` | Contraseñas de las cuentas de prueba. Codex lo crea y no se sube a GitHub. |

## Cuándo te va a necesitar Codex

- Para darle los correos de las cuentas de prueba, si no los completaste.
- Para resolver un captcha o revisar un correo de verificación o de recuperación.
- Para aprobar el diseño en el punto de control, antes de que escriba en TestLink y Jira.
- Para pegar las capturas en Jira, si su acceso no permite adjuntar imágenes.
