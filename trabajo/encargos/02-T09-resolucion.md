# Resolución de revisión T09 — Codex

Respuesta de origen: `02-T09-revision-respuesta.md`. Los cambios se aplicaron después de terminar la revisión. No hubo registro externo.

| Hallazgo | Resolución |
|---|---|
| B1: Submit no es el texto visible de Signup | Corregido a Signup, conservando la anotación de nombre accesible cuando aporta contexto. Codex inspeccionó directamente registro-vacio y remember-off-reapertura-sin-sesion: Signup y Sign Up Free visibles. JSON, fichas y XML regenerados. |
| N1: suite nueva y raíz antigua | Generador produce testcases; destino Todo.ly tests, sin suites ni IDs. Documentación y borrador corregidos. Exportación real completa y extracción por script documentadas. |
| N2: OK antiguo | Actualizado: registro autorizado tras revisión sin bloqueantes; no se declara registro ni revisión de integrante. |
| N3: fuente de inexistencia del correo | Citada trabajo/T10/exploracion.md, Recuperación: solicitud y contraste, 11:13 AM. Se permite expresamente leer esa fuente en la nueva revisión. No se deriva inexistencia del mensaje genérico de Login. |
| N4: integridad tras duplicado | Identificada como Criterio del equipo, no observación realizada con A. Resultado de envío acotado a rechazo y ausencia de nueva sesión; el Login posterior comprueba identidad como parte del caso. |
| N5: aviso de Signup | Se distingue aviso transitorio leído por AX de asteriscos/aviso de términos capturados. Se dice «se muestra», sin afirmar cuándo se genera el aviso fijo de términos. |
| N6: correos en capturas de exploración | No se publicarán esas capturas como evidencia de registro. Se usarán árbol/casos de TestLink con fichas genéricas. Los valores de credenciales no se consultan ni reproducen en revisión. |
| N7: controles Cancel/Login | Fuente cruzada y nomenclatura añadidas a exploracion.md y análisis. El caso usa Login visible; Cancel fue observado en consultas de identidad y T10. |
| N8: Sign Up Free | Aplicado en apertura de Signup y lectura de la página pública de Remember Me. |
| N9: Timezone y cierre | El texto completo de Pacific procede del listado AX ya documentado, no del recorte de captura. Cierre acotado a página pública sin registro ni sesión. Sin efectos temporales. |
| N10: presupuesto | Identificado expresamente como criterio del equipo, no política del producto. |
| N11: retorno final B | Conservado como resultado esperado del criterio de independencia, no afirmado como ejecución ya realizada. |

T09-08 sigue fuera del registro; registro válido controlado y fronteras no confirmadas siguen como cobertura pendiente. No se requiere ampliar exploración para resolver esos pendientes antes de registrar el conjunto definido, conforme a la autorización del usuario.
