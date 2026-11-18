# Informe final T09–T11 — 18/11/2026

> **Estado: fase 6 incompleta.** La cuenta B sigue pendiente de limpieza (ver §5). La revisión por otro integrante y la ejecución formal de los casos también están pendientes. Este informe no declara el trabajo cerrado.

## 1. Casos en TestLink (TL:Todo.ly, suite Todo.ly tests id 3) y comentarios en Jira

Hay 29 casos propios, todos Manual y en Draft. Enlace de cada caso: `http://68.211.149.112/linkto.php?tprojectPrefix=TL&item=testcase&id=TL-NN`. El mapa completo, con URL, ID interno, pasos e importancia, está en [T09](T09/testlink-registro.json) · [T10](T10/testlink-registro.json) · [T11](T11/testlink-registro.json).

| Ticket | Casos | Caso → ID TestLink | Comentario Jira |
|---|---|---|---|
| T09 / PEB-73 | 13 | 01→TL-72 · 02→73 · 03→74 · 04→75 · 05→76 · 06→77 · 07→78 · 09→79 · 10→80 · 11→81 · 12→82 · 13→83 · 14→84 | [10227](https://alesalve.atlassian.net/browse/PEB-73?focusedCommentId=10227) |
| T10 / PEB-74 | 9 | 01→TL-66 · 02→67 · 03→68 · 04→85 · 05→86 · 06→87 · 08→69 · 09→70 · 10→71 | [10226](https://alesalve.atlassian.net/browse/PEB-74?focusedCommentId=10226) |
| T11 / PEB-75 | 7 | 01→TL-88 · 02→89 · 03→90 · 04→91 · 05→92 · 06→93 · 07→94 | [10228](https://alesalve.atlassian.net/browse/PEB-75?focusedCommentId=10228) |

Corrección posterior T09: el comentario10227 fundamenta sus trece casos únicamente en casos de uso UC1–UC5, con flujos, extensiones y trazabilidad. TestLink y los XML exportados se conservan.

Cada comentario tiene su copia local en `trabajo/T0X/jira-publicado.html`. No se cambiaron estados de Jira ni se marcaron revisiones.

## 2. Pendientes de diseño (no registrados)

- **T09-08** (Login con un Email sin formato de correo): la herramienta mostró vistas vacías que no permiten atribuir a Todo.ly una regla de validación. Por eso el resultado visible y el mensaje siguen sin confirmar. Fuente: `trabajo/T09/casos-pendientes.json`.
- **T10-07** (cambio válido de Email de B a un alias y restauración): no se sabe si el cambio exige verificación por correo ni en qué momento el nuevo identificador queda vigente. Los resultados principales serían condicionales, así que, por instrucción del usuario (ajuste 4), queda como cobertura pendiente y no se registra. Fuente: `trabajo/T10/casos-pendientes.json`.
- Otras dudas documentadas en los análisis y comentarios. Por ejemplo, en T10 no hay resultado confirmado para las combinaciones de Settings con New Password vacío. Ninguna de estas dudas se convierte en regla.

## 3. Revisión y ejecución

- La redacción final de TestLink es la que dejó la revisión por API del otro Claude, que Andre avisó como terminada (93 casos finales, respaldo 1724). No se compara con los diseños locales ni se revierte. Las diferencias de redacción son esperadas y están documentadas en `revision-testlink/informe-revision.md`; en T09 y T11 solo cambió el prefijo del título. La revisión no modificó IDs, importancia, tipo de ejecución, estado ni suite.
- **Pendiente:** revisión por otro integrante del grupo. La revisión de Claude no la sustituye.
- **Pendiente:** ejecución formal de los 29 casos. Explorar no equivale a ejecutar.
- No se afirma que el checklist de cierre (guía §19 y decisiones §14) esté cumplido: faltan la cuenta B y la captura final de B.

## 4. Exportación XML (terminada)

- Script de exportación ejecutado en **solo lectura** con resultado correcto. Fecha: 2026-11-18T21:39:30Z. Métodos usados: `checkDevKey`, `getProjects`, `getTestSuiteByID`, `getTestSuitesForTestSuite`, `getTestCasesForTestSuite` y `getTestCase`.
- `testlink-xml/todo-ly-tests.xml`: 93 casos en la suite 3, de ellos 29 propios (esperados 29, sin diferencias). SHA-256 `f17141163f48…`. Manifiesto: `testlink-xml/todo-ly-tests.procedencia.json`.
- Extracción exacta, con IDs internos y externos conservados y sin comparar la redacción: `T09.xml` (13), `T10.xml` (9) y `T11.xml` (7). Manifiesto: `testlink-xml/origen-exportacion.json`.
- **Procedencia:** el XML se reconstruyó fielmente desde la API XML-RPC. No es una exportación nativa hecha desde la interfaz. No incluye adjuntos, campos personalizados, keywords ni requisitos nativos. Los XML de importación no se presentan como exportación.
- La API key ya existía y se leyó en My Settings sin regenerarla. Es privada y no se imprimió.

## 5. Estado de las cuentas de prueba (detalle en `trabajo/estado-cuentas-final.md`)

- **A, completada:** retiradas las cuatro tareas «Prueba» de Home y Study, eliminado el proyecto temporal vacío y vaciada la Recycle Bin (confirmado por AX y en la única captura, `cierre/A-estado-final.png`). Profile y los desplegables de Default Settings coinciden con el baseline. La contraseña original ya se había restaurado en T10; no se repitió.
- **B, PENDIENTE:** el marcador `Prueba T09-aislamiento-B-1941` sigue en Home y la Recycle Bin está sin vaciar. La herramienta de Codex falló tres veces al seleccionar Home, y se pidió a Andre que lo seleccionara, sin respuesta todavía. No existe captura final de B. Profile y los desplegables de Defaults coinciden con el baseline. El email original ya estaba conservado.
- En ambas cuentas, AX no expone el estado de las casillas de Defaults, así que no se confirma si están marcadas.
- Andre ya confirmó las acciones irreversibles de A y B. No se borraron cuentas ni se usó la cuenta de Camila.

## 6. Privacidad y repositorio

- El XML completo local incluye una credencial heredada de casos ajenos. Se conserva intacto y git lo ignora. En git solo va una copia cifrada con Fernet, idéntica byte a byte al descifrarla (`trabajo/resguardos-revision/todo-ly-tests.xml.fernet`), más el manifiesto. La clave está solo en `.secrets/`. Los XML T09, T10 y T11 no contienen credenciales conocidas.
- El historial antiguo de git conserva cuatro archivos raw con la credencial heredada. El usuario **no autorizó** el force push y **el historial no se ha purgado**. El árbol actual está protegido por un hook y por `scripts/verificar_secretos_git.py`.
- Entrega mediante commit `Cierre T09–T11: exportación final e informe` y push normal, sin force. La limpieza B sigue pendiente y está registrada en CONTINUIDAD.md.
