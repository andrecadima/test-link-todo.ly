# T10 — Preparación local para registro

Estado: **OK recibido; pendiente completar los pasos manuales, corregir observaciones y revisión final**. No se ha importado ni registrado ningún caso nuevo.

- `casos-listos.json`: seis casos del punto de control, T10-01/02/03/08/09/10.
- `casos-pendientes.json`: T10-04/05/06/07, fuera de la importación.
- `importacion-propuesta.xml`: entrada local con raíz testcases para importar los casos dentro de la suite existente Todo.ly tests, sin crear suites. No contiene IDs internos ni externos, ni credenciales.
- `testlink-xml/T10.xml`: todavía no existe; se extraerá por script de la **exportación real testlink-xml/todo-ly-tests.xml**, después de comprobar IDs, campos y pasos en TestLink.

Generación reproducible:

```sh
python3 scripts/preparar_importacion_testlink.py trabajo/T10/casos-listos.json trabajo/T10/importacion-propuesta.xml --ticket T10
```

Formato contrastado con el [importador oficial de TestLink 1.9.20](https://github.com/TestLinkOpenSourceTRMS/testlink-code/blob/testlink_1_9_20_fixed/lib/testcases/tcImport.php): raíz testcases, nombre de caso, summary, preconditions y steps/step con número, actions, expectedresults y execution_type. Las [constantes oficiales](https://github.com/TestLinkOpenSourceTRMS/testlink-code/blob/testlink_1_9_20_fixed/cfg/const.inc.php) asignan Importance high=3, medium=2, low=1; [la clase oficial de casos](https://github.com/TestLinkOpenSourceTRMS/testlink-code/blob/testlink_1_9_20_fixed/lib/functions/testcase.class.php) identifica Manual=1. No se atribuye al servidor compartido una importación validada por consultar estas fuentes públicas.

Después de revisión final sin bloqueantes: consultar el árbol real para evitar casos duplicados; importar únicamente este conjunto bajo Todo.ly tests, sin actualizar existentes; revisar individualmente los seis casos; anotar IDs y enlaces reales; conservar capturas del árbol y un caso abierto; exportar realmente Todo.ly tests y extraer los tickets por script. Nunca actualizar casos de otros tickets por coincidencia de nombre o ID. El comentario de Jira se publica después de esa verificación y conserva las dudas de cobertura.

## Precomprobación autenticada actual — 17/11, 21:40 aprox.

La sesión antigua expiró; se accedió de nuevo y se confirmó admin y proyecto TL:Todo.ly en Chrome. El árbol completo de Test Specification mostró **Todo.ly tests (64)**: los 48 iniciales más casos de estados/papelera de otros tickets. No aparecen nombres T09-NN, T10-NN ni T11-NN. No se editó ningún caso ajeno. Destino de importación: suite id3. La revisión independiente 04 dio APTO para los seis casos confirmados de T10; pendientes 04/05/06 y excluido 07.

## Envío realizado — verificación pendiente

Se seleccionó Import Test Cases para Todo.ly tests (id3), XML, duplicado por mismo nombre y Do not import the test case. Se eligió el XML de seis casos mediante el diálogo de archivo y se pulsó Upload file **una sola vez**. La navegación posterior fue tcImport.php, sin parámetros de GET; no se logró leer el resultado. Se abrió Test Specification mediante un GET nuevo para consultar existencia, pero el control quedó sin contenido. No hay todavía IDs confirmados y no se declara registro ni fallo de importación. **No reenviar sin comprobar primero si existen los seis nombres.**
