# Respuesta al encargo 13 — fase 6 mínima

## Archivos escritos (solo los autorizados)

1. `scripts/exportar_testlink_api.py` — **no ejecutado, no compilado** (no se usó Bash). No hubo red, API ni escrituras remotas.
2. `trabajo/INFORME-FINAL-borrador.md` — unas 50 líneas, con las secciones pendientes marcadas.
3. Este archivo.

No se leyeron `.secrets/`, respaldos, logs JSON de otros encargos ni otros archivos de `revision-testlink/` aparte de `informe-revision.md`. No se tocaron XML, diseños, casos ni archivos de otros agentes.

## Script de exportación

- **Barrera:** sin `--revision-finalizada` termina con código 3 antes de leer la clave o importar `xmlrpc.client`. Si `testlink-xml/todo-ly-tests.xml` (o los T0X.xml al usar `--extraer`) ya existe, también lo rechaza salvo que se pase `--sobrescribir`.
- **Clave:** se lee solo de `TESTLINK_API_KEY`. No se imprime y se enmascara en los mensajes de error. Nota: los scripts de `revision-testlink/` usan `TESTLINK_DEVKEY`; si se reutiliza esa variable, hay que exportarla con el nombre `TESTLINK_API_KEY`.
- **Solo lectura:** una lista cerrada de métodos (`checkDevKey`, `getProjects`, `getTestSuiteByID`, `getTestSuitesForTestSuite`, `getTestCasesForTestSuite` con deep/full y `getTestCase` sin versión). Cualquier otro método se rechaza. No usa ningún `exportTestSuite`.
- **Validaciones:**
  - errores de TestLink en formato `code/message`;
  - que la suite 3 pertenezca al proyecto 1;
  - el prefijo del proyecto;
  - la jerarquía de subsuites y que cada caso cuelgue de una suite recorrida;
  - que cada `getTestCase` devuelva exactamente una versión del caso pedido;
  - la presencia de los campos obligatorios;
  - una versión del listado mayor que la de `getTestCase`, que se reporta;
  - una prueba de ida y vuelta del XML antes de escribirlo, con escritura atómica.
- **XML:** `testsuite` → `testcase internalid/name` con `node_order`, `externalid`, `version`, `summary`, `preconditions`, `execution_type`, `importance` (más `status`/`active`/`is_open` si la API los entrega) y `steps/step` con `expectedresults`. Lleva un comentario de procedencia y se acompaña de `todo-ly-tests.procedencia.json`, con hash, métodos e IDs pero sin textos. No exporta keywords, campos personalizados ni adjuntos (está documentado).
- **Contraste:** compara contra los tres `testlink-registro.json` solo los IDs internos y externos y el prefijo del caso; no compara la redacción. Espera 29 casos. Ante diferencias, las lista, termina con código 2 y no ejecuta la extracción. Nunca corrige nada.
- `--extraer` reutiliza `extract()` de `scripts/extraer_xml_por_ticket.py`. Su regex acepta tanto `T09-01.` como `T09-01 - `.

### Supuestos no verificados contra el servidor

- Que `getTestCase` sin `version` devuelva la última versión.
- El nombre de los campos (`testcase_id`, `tc_external_id`, `steps`, `expected_results`, `parent_id`, `node_order`).
- La forma variable de la respuesta de `getTestSuitesForTestSuite`.

Si alguno falla, el script aborta sin escribir.

Riesgo a tener en cuenta: la URL es `http://`, así que la clave viaja sin cifrar. Es la URL indicada; no se cambió.

## Pendiente

1. Que Andre avise de que la revisión por API terminó. Después, que Codex ejecute `TESTLINK_API_KEY=… python3 scripts/exportar_testlink_api.py --revision-finalizada --extraer` y revise cualquier diferencia que se reporte.
2. Recomendado antes: `python3 -m py_compile scripts/exportar_testlink_api.py` (no se pudo hacer aquí).
3. Terminar la limpieza de A/B y escribir `trabajo/estado-cuentas-final.md`. Hoy no existe.
4. Completar las secciones PENDIENTE del borrador (motivos de T09-08/T10-07, estado de las cuentas, datos de la exportación, revisión del otro integrante) y renombrarlo a `trabajo/INFORME-FINAL.md`.
5. Commit y push normales, sin force, con `scripts/verificar_secretos_git.py`. El historial antiguo sigue sin purgar.
