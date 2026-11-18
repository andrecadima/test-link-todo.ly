# Informe final T09–T11 — BORRADOR (18/11/2026)

> Borrador preparado sin navegador, Jira, TestLink ni git. Las secciones marcadas **PENDIENTE** se completan con evidencia real antes de renombrarlo a `trabajo/INFORME-FINAL.md`. No se afirma ningún cierre no realizado.

## 1. Casos registrados en TestLink (proyecto TL:Todo.ly, suite Todo.ly tests, id 3)

Enlace de cada caso: `http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=<ID>`. Fuente: `trabajo/T0X/testlink-registro.json`. Total propio: **29** (13 + 9 + 7), todos Manual y en Draft.

| Ticket | Casos | Mapa caso → ID TestLink |
|---|---|---|
| T09 / PEB-73 | 13 | 01→TL-72 · 02→TL-73 · 03→TL-74 · 04→TL-75 · 05→TL-76 · 06→TL-77 · 07→TL-78 · 09→TL-79 · 10→TL-80 · 11→TL-81 · 12→TL-82 · 13→TL-83 · 14→TL-84 |
| T10 / PEB-74 | 9 | 01→TL-66 · 02→TL-67 · 03→TL-68 · 04→TL-85 · 05→TL-86 · 06→TL-87 · 08→TL-69 · 09→TL-70 · 10→TL-71 |
| T11 / PEB-75 | 7 | 01→TL-88 · 02→TL-89 · 03→TL-90 · 04→TL-91 · 05→TL-92 · 06→TL-93 · 07→TL-94 |

La numeración por ticket no es correlativa (T09-08 y T10-07 no tienen caso registrado; ver §3).

## 2. Comentarios publicados en Jira

| Ticket | Comentario | Copia local |
|---|---|---|
| PEB-73 / T09 | https://alesalve.atlassian.net/browse/PEB-73?focusedCommentId=10227 | `trabajo/T09/jira-publicado.html` |
| PEB-74 / T10 | https://alesalve.atlassian.net/browse/PEB-74?focusedCommentId=10226 | `trabajo/T10/jira-publicado.html` |
| PEB-75 / T11 | https://alesalve.atlassian.net/browse/PEB-75?focusedCommentId=10228 | `trabajo/T11/jira-publicado.html` |

No se cambiaron estados de Jira ni se marcaron revisiones.

## 3. Pendientes y dudas declaradas

- **T09-08** y **T10-07**: sin caso registrado; quedan como pendientes documentados en el análisis de cada ticket. PENDIENTE: citar aquí el motivo exacto desde `trabajo/T09/` y `trabajo/T10/`.
- Demás dudas: las documentadas en cada análisis/diseño y en los comentarios de Jira (p. ej., combinaciones de Settings con New Password vacío en T10, sin resultado confirmado). No se convierten en reglas.

## 4. Revisión de redacción en TestLink (otro Claude, por API)

La versión final de los casos en TestLink es la revisada por API; **no** se compara ni revierte contra los diseños locales. Las diferencias de redacción respecto de los diseños son esperadas (p. ej., prefijo `TXX-NN - ` en títulos, «Validar que…», pasos con controles en negrita) y están documentadas en `revision-testlink/informe-revision.md`. IDs, importancia, tipo de ejecución y suite no cambian por esa revisión.

## 5. Cobertura y revisión de otro integrante

- Cobertura por ticket: según las tablas de técnicas publicadas en cada comentario de Jira (T10 con casos de uso como fundamento principal, decisiones-vigentes §16).
- La revisión de Claude no sustituye la revisión de otro integrante del grupo. **PENDIENTE**: la realiza otro integrante; no se marca en Jira.

## 6. Estado final de las cuentas de prueba A y B

**PENDIENTE**: `trabajo/estado-cuentas-final.md` aún no existe. Completar con la limpieza real (relevo, pasos 7–13): datos «Prueba» retirados, Recycle Bin vacía en A y B, Profile/Settings comparados con `trabajo/estado-cuentas-inicial.md` y una captura final por cuenta. No se borraron cuentas ni se usó la cuenta de Camila.

## 7. Exportación XML

**PENDIENTE — no ejecutada.** Se espera el aviso explícito de Andre de que la revisión por API terminó. Preparado `scripts/exportar_testlink_api.py` (XML-RPC, solo lectura, exige `--revision-finalizada`, clave en `TESTLINK_API_KEY`). El script no se ha ejecutado ni probado contra la API.

- Salida prevista: `testlink-xml/todo-ly-tests.xml` + `todo-ly-tests.procedencia.json`; luego `T09.xml`, `T10.xml`, `T11.xml` y `origen-exportacion.json` con `scripts/extraer_xml_por_ticket.py`.
- Procedencia: XML **reconstruido desde la API** con la estructura de la exportación nativa; no es una exportación hecha desde la interfaz. Los XML de importación no se presentan como exportación.
- PENDIENTE: anotar total de casos, 29 propios verificados (o diferencias reportadas) y SHA-256.

## 8. Repositorio e incidencia del historial

- Commit y push normales; **nunca** force push. Staging revisado con `scripts/verificar_secretos_git.py`; `.secrets/` y `revision-testlink/respaldo-*.json` ignorados.
- Incidencia: el historial antiguo conserva cuatro archivos con una credencial heredada. El árbol actual está protegido; **el historial no se ha purgado**.
