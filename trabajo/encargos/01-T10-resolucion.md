# Resolución de la revisión 01 — T10

Alcance de revisión: seis casos listos; T10-04/05/06/07 no incluidos. No se registró ni ejecutó ningún caso.

- Bloqueante XML: corregido. Raíz testcases, destino suite existente Todo.ly tests, sin suites nuevas ni IDs ni actualizaciones de casos existentes.
- N1: no se adopta la sugerencia de reemplazar manualmente HTTP por HTTPS en T10-08. La instrucción expresa posterior del usuario exige abrir el enlace tal como llega; si falla el formulario en ejecución, falla T10-08. HTTPS se evalúa por separado en T10-10.
- N2: T10-08 compara exclusivamente nombre y email de Profile, conocidos en el registro privado.
- N3: precondición genérica Sin sesión iniciada en Todo.ly en el navegador.
- N4: postcondición y continuidad mantienen la credencial resultante de recuperación y restauración posterior pendiente.
- N5: se distingue nombre temporal tras F5 de nombre original restaurado visto al abrir nueva sesión.
- N6: clasificación corregida a Criterio del equipo. No se afirma mensaje de Old Password incorrecto hasta observarlo.
- N7: destino y autorización actualizados; retirar metadata operativa antes de publicar. Jira solo contendrá registro real con sus IDs después de verificarlo.
- N8/N9: 04/05/06 requieren observación manual; 07 queda excluido. Política, límites y verificación de email siguen Duda pendiente.
- N10/N11: capturas de exploración con datos de cuenta no se publicarán en Jira; se publicarán árbol y caso genérico de TestLink. No atribuir a una captura un aviso transitorio que solo se leyó mediante AX.

Después de completar a/b/c y actualizar los casos, se necesita una revisión nueva del conjunto definitivo. El veredicto del encargo 01 no cubre casos que todavía no se completaron.
