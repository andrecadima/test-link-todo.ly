# Ejecución del grupo 2 — 23/11/2026

## Alcance vigente

Andre pidió ejecutar en Chrome y registrar los resultados reales en TestLink. Su captura posterior limita el alcance a TS-01 Registro de usuario (9 casos) y TS-02 Inicio de sesión (6 casos). No corregir sus especificaciones, no tocar los otros 60 casos ni el proyecto TL:Todo.ly anterior, ni publicar en Jira sin otro pedido.

Proyecto: TC:Todo.ly grupo 2, id 1387. Suites: 1388 y 1470. Casos nativos TC-1 a TC-15; no confundirlos con los códigos TC-001, TC-033, etc. de sus títulos. Mapeo en ejecucion.json.

## Preparación verificada

El proyecto no tenía planes. Codex creó el plan activo privado «Ejecución grupo 2 - 2026-11-23», id2897, y el build activo/abierto «Todo.ly web - 2026-11-23», id1. Es una etiqueta de sesión, no una versión comprobada de la AUT. La descripción inicial decía75 antes de que Andre acotara: falta corregirla a15 y las dos suites.

Vinculación CONFIRMADA: exactamente15 filas con Added on date, TC-1…TC-15 de las dos suites; los otros60 quedaron sin vincular. No se ejecutó ningún caso ni se guardó Passed/Failed/Blocked todavía. Todos figuran localmente not_run.

## Bloqueo actual y siguiente paso

Al volver a Desktop, TestLink quedó en blanco, sin documento AX. Cambiar de pestaña y navegar por la barra no recuperó la vista. Se pidió a Andre recargar manualmente TestLink y abrir Desktop → Execute Tests del plan2897. Esperar su aviso antes de usar Chrome, para no interferir con el handoff.

La conexión del navegador de Codex in Chrome informó «browser access host unavailable». El acceso CUA nativo a Chrome sí funcionó para crear plan/build y vincular casos. La ventana está en el perfil RICARDO ANDRE (ucb.edu.bo), TestLink autenticado como admin. Codex abrió una pestaña New Tab vacía; no cerró sesiones ajenas.

Después del aviso:
1. Confirmar vista Execute Tests y campos de resultado/notas por paso y por caso; no pulsar las X rojas de Test Specification: eliminan pasos. Manual indica tipo, no resultado.
2. Corregir descripción del plan a15 casos, solo suites TS-01 y TS-02.
3. Leer las quince fichas y sus precondiciones/datos; abrir Todo.ly en QA o incógnito, aislado de sesiones existentes. No usar cuentas personales ni Camila. Confirmar las cuentas de prueba requeridas, sin exponer claves.
4. Antes de aceptar términos para registros nuevos, solicitar confirmación en ese momento. Cambios de contraseña, captcha o correo requieren intervención según la política CUA.
5. Ejecutar cada acción y contrastar el resultado esperado con el obtenido, sin reutilizar observaciones del18/11 como ejecución actual. Guardar resultados solo después de observarlos. Separar defecto del producto, discrepancia de ficha y bloqueo de entorno/precondición.
6. Conservar evidencia sin secretos y registrar las incidencias en TestLink, con pasos de reproducción, esperado/obtenido y entorno. Resumir totales al terminar.

Secretos solo en .secrets/. No copiar credenciales originales del XML a documentos públicos. El repositorio ya tenía cambios ajenos en revision-testlink/ del23/11: preservarlos sin editar ni incluirlos en este checkpoint. No force push. La limpieza B del trabajo anterior sigue documentada allí, pero no es el alcance prioritario de esta nueva etapa.
