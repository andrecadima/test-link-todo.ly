# T10 — Preparación local para registro

Estado: **pendiente de OK y de recuperar el control de Chrome**. No se ha importado ni registrado ningún caso nuevo.

- `casos-listos.json`: seis casos del punto de control, T10-01/02/03/08/09/10.
- `casos-pendientes.json`: T10-04/05/06/07, fuera de la importación.
- `importacion-propuesta.xml`: entrada local para crear la suite T10 con los seis casos y sus pasos nativos. No contiene IDs internos ni externos, ni credenciales.
- `testlink-xml/T10.xml`: todavía no existe; deberá ser la **exportación real de la suite registrada**, después de comprobar IDs, campos y pasos en TestLink.

Generación reproducible:

```sh
python3 scripts/preparar_importacion_testlink.py trabajo/T10/casos-listos.json trabajo/T10/importacion-propuesta.xml --ticket T10
```

Formato contrastado con el [importador oficial de TestLink 1.9.20](https://github.com/TestLinkOpenSourceTRMS/testlink-code/blob/testlink_1_9_20_fixed/lib/testcases/tcImport.php): raíz testsuite, nombre de suite/caso, summary, preconditions y steps/step con número, actions, expectedresults y execution_type. Las [constantes oficiales](https://github.com/TestLinkOpenSourceTRMS/testlink-code/blob/testlink_1_9_20_fixed/cfg/const.inc.php) asignan Importance high=3, medium=2, low=1; [la clase oficial de casos](https://github.com/TestLinkOpenSourceTRMS/testlink-code/blob/testlink_1_9_20_fixed/lib/functions/testcase.class.php) identifica Manual=1. No se atribuye al servidor compartido una importación validada por consultar estas fuentes públicas.

Después del OK: consultar el árbol real para evitar duplicar una suite o casos ya creados; importar únicamente este conjunto bajo el contenedor acordado; revisar individualmente los seis casos; anotar IDs y enlaces reales; conservar capturas del árbol y un caso abierto; exportar la suite real. Nunca actualizar casos de otros tickets por coincidencia de nombre o ID. El comentario de Jira se publica después de esa verificación y conserva las dudas de cobertura.
