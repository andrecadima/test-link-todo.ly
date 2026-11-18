Eres Claude, agente de diseño y revisión de QA. Codex es el orquestador. Aplican `AGENTS.md` y `docs/decisiones-vigentes.md`, con estas excepciones: no usas navegador, Jira, TestLink ni git, y nunca lees `.secrets/`. Trabaja en español y conserva en inglés los textos de la interfaz. No inventes reglas, mensajes, controles ni límites: todo resultado esperado debe apoyarse en `exploracion.md`, en una evidencia o en un criterio del equipo identificado como tal. Escribe solo los archivos que autoriza este encargo. Al terminar, escribe tu respuesta en `trabajo/encargos/03-T09-revision-respuesta.md`.

# Revisión independiente de T09 / PEB-73

## Objetivo y permisos
Revisar el conjunto registrable de T09 para la demo del 18/11/2026. No editar el diseño ni los casos. Único archivo autorizado para escritura: `trabajo/encargos/03-T09-revision-respuesta.md`. No ejecutar comandos, no usar agentes adicionales, no leer configuración personal ni archivos fuera del repositorio. Nunca acceder a .secrets, ni siquiera mediante búsqueda. Para buscar, limitar explícitamente rutas a docs/, plantillas/ y los archivos de trabajo listados.

## Lecturas
- AGENTS.md; docs/decisiones-vigentes.md; PROMPT_ORQUESTACION.md (prevalece sobre instrucciones antiguas de continuidad).
- docs/guia-diseno-casos-prueba-todoly.md, en especial §7–10 y §19.
- trabajo/00-contexto.md para definiciones docentes ya recuperadas; NO releer PDF completos.
- plantillas/caso-testlink.md; plantillas/comentario-jira.md.
- trabajo/fuentes/PEB-73.md y trabajo/fuentes/PEB-70.md, PEB-76.md.
- trabajo/T09/exploracion.md; analisis-diseno.md; casos.json; casos-listos.json; casos-pendientes.json; comentario-jira-borrador.md.
- Evidencias de trabajo/T09/evidencias/ que sustenten afirmaciones concretas. Priorizar capturas que la exploración identifica como legibles; no atribuir avisos a capturas en las que desaparecieron. Nunca buscar fuera de esa carpeta.
- Para solapamientos, trabajo/00-contexto.md y snapshots PEB-71/72/77/78; solo si el caso lo requiere.

## Situación que debes respetar
Los diseños son propuestas, no ejecución formal. No hay casos nuevos registrados ni comentarios publicados. Los casos-pendientes están expresamente EXCLUIDOS del registro: no tratarlos como listos ni exigir registrarlos con resultados condicionales. Su cobertura insuficiente se informa, sin confundirla con una contradicción en un caso listo.
El usuario acaba de autorizar el registro tras revisión sin bloqueantes. El destino nuevo es la suite existente Todo.ly tests; XML de entrada con raíz <testcases>, SIN crear suites ni actualizar casos existentes. Los diseños/archivos antiguos aún pueden decir suite por ticket: identifícalo para corregirlo, no lo avales.
T10 tiene OK y el usuario ya proporcionó sus ajustes y bloque a/b/c; esta revisión se limita a T09. Su recuperación y controles pueden leerse como fuentes cruzadas en trabajo/T10/exploracion.md, sin acceder a secretos.
Ningún estado o mensaje puede presentarse como observado solo porque es un resultado esperado. Separar Regla documentada, Comportamiento observado, Criterio del equipo y Duda pendiente. Criterio HTTPS fue expresamente indicado por el usuario.
Precondiciones: estados, cuentas genéricas y configuración; sin acciones ni correos/contraseñas reales. Cualquier dato literal de contraseña de prueba inválida se evalúa distinguiéndolo de una credencial real; no intentar leer .secrets para compararlo.

## Revisión y formato
Escribe tres partes con este orden:
1. **Bloqueantes**: cada hallazgo con caso/archivo/sección exactos, evidencia de contradicción o falta, y corrección mínima propuesta. Incluye invenciones de mensajes/controles/límites, trazabilidad técnica falsa, ficha incorrecta, secretos, tareas padre/subtareas o duplicación real de otros tickets. Si no hay, indicar Ninguno.
2. **No bloqueantes**: mejoras, cobertura pendiente y limitaciones. Marcar qué debe documentarse antes de registrar. No expandir exploración ni proponer BVA sin frontera confirmada.
3. **Veredicto: APTO o NO APTO**, para el conjunto casos-listos.json (no para candidatos pendientes ni una revisión humana de integrante).
Incluye dentro de la respuesta una tabla del checklist §19 (13 ítems) con Cumple / Pendiente / No cumple y fundamento breve. No marcar registro, revisión de integrante o ejecución como realizados.

## Criterios de aceptación
- Todas las fichas listas comparadas con evidencia/reglas, pasos y resultados verificables, sin acciones en precondiciones.
- Técnicas realmente aplicadas, artefactos y casos trazables.
- Hallazgos concretos y corregibles, sin adornos ni reglas nuevas.
- No escribir nada distinto del archivo de respuesta; no modificar estado externo.


## Revisión nueva después de correcciones
Lee primero trabajo/encargos/02-T09-revision-respuesta.md y 02-T09-resolucion.md. Verifica las correcciones en los artefactos ACTUALES; no repitas como vigentes defectos de XML/controles que ya no estén. Puedes leer trabajo/T10/exploracion.md y la captura de Old Password vacío como fuentes cruzadas explícitas para la inexistencia del correo y Cancel de Settings. No editar ningún diseño ni respuesta anterior.

Evalúa el conjunto registrable completo y su importación: si hay cualquier bloqueante vigente en casos o artefacto de importación, el veredicto es NO APTO. No emitir APTO condicionado a que luego se quite un bloqueante; debe estar ya resuelto. Pendientes excluidos no son registros ficticios.

Archivo único autorizado para escribir: trabajo/encargos/03-T09-revision-respuesta.md.
