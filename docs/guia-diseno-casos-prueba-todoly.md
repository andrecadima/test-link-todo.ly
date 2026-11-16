# Guía para analizar tickets y diseñar casos de prueba de Todo.ly

**Última actualización:** 16 de noviembre de 2026.  
**Propósito:** permitir que otro agente continúe el trabajo con el mismo criterio, formato y alcance acordados con el equipo.  
**Aplicación:** https://todo.ly/  
**Idioma de trabajo:** español; conservar los nombres de controles y mensajes de la interfaz en inglés.

## 1. Cómo utilizar esta guía

1. Leer el ticket completo, sus criterios de aceptación y sus comentarios actuales.
2. Consultar el PlanPruebasTodo.ly y los materiales de clase cuando la tarea necesite sus reglas o formatos.
3. Identificar qué funciones, reglas y riesgos corresponden al ticket.
4. Resolver las dudas que impidan escribir resultados esperados verificables.
5. Redactar el análisis del área y justificar los tipos de prueba y técnicas elegidos.
6. Presentar una lista resumida de casos con el fundamento de la técnica aplicada a cada uno.
7. Desarrollar los casos detallados con el formato de esta guía.
8. Registrar y revisar en TestLink únicamente cuando esa actividad forme parte del trabajo solicitado. Conservar los enlaces reales como evidencia.

Esta guía resume acuerdos de la conversación. No sustituye el contenido vigente de Jira, TestLink, el plan ni las diapositivas. No es una especificación oficial del producto ni acredita que todos los casos propuestos estén ejecutados.

Si el usuario pide únicamente redacción o corrección, entregar el contenido solicitado sin modificar por iniciativa propia Jira, TestLink o Google Docs. Si pide registrar o actualizar, realizar la acción dentro de ese alcance y comprobar su resultado.

## 2. Contexto del proyecto

- Equipo: Alejandra Salinas, Andre Cadima y Camila Carvajal.
- Práctica académica de pruebas de caja negra, manuales, sobre la aplicación web pública.
- Cuenta gratuita. No hay acceso al código, al servidor ni a un entorno propio de Todo.ly.
- Jira organiza el trabajo; TestLink compartido, desplegado en Railway, administra los casos. Las fallas se documentarán con la plantilla del equipo en una planilla.
- El trabajo se basa en riesgo, relevancia para el usuario y cobertura útil; no en completar cantidades artificiales de casos.
- El docente sugirió plantillas y técnicas de clase. No se estableció una norma obligatoria ni un mínimo general de casos.
- La exploración inicial recorrió sistemáticamente las funciones y módulos. Puede describirse como exploración guiada por funcionalidades; no presentarla como una sesión exclusivamente freestyle.
- El mapa de funciones es un único entregable visual. No generar otro diagrama por defecto.

La organización final acordada contempla un único sprint de planificación y desarrollo del 4 al 18 de noviembre de 2026, con entrega intermedia del plan el 11 de noviembre. El 18 corresponde al demo. La relación de la fecha del 23 con entregas posteriores deberá confirmarse antes de planificar trabajo adicional. No inventar un Sprint 3.

### Organización mediante tickets

Se distribuyeron áreas de análisis en nueve tickets, tres por integrante. Los resultados de análisis y diseño sirven para desglosar después los tickets de implementación y registro en TestLink. El equipo revisa los resultados entre integrantes.

Algunos tickets existentes todavía combinan en su título analizar, diseñar y registrar. Se debe leer el alcance real y distinguir las etapas en el comentario, sin cambiar unilateralmente los tickets existentes.

El formato acordado para nuevas tareas de Jira es:

- Título.
- Objetivo.
- Descripción.
- Prioridad de la tarea: alta, media o baja.
- Story points de la secuencia Fibonacci; el equipo solicitó 5 para las tareas amplias de análisis y diseño discutidas.
- Criterios de aceptación mediante checklist.

No añadir un campo de dependencia ni asignar un responsable por defecto. La prioridad de una tarea de Jira es distinta de la importancia de un caso y de la prioridad de una falla.

## 3. Referencias y alcance de tickets conocidos

| Ticket | Referencia | Área |
|---|---|---|
| T06 | [PEB-70](https://alesalve.atlassian.net/browse/PEB-70) | Creación y edición de tareas. |
| T07 | [PEB-71](https://alesalve.atlassian.net/browse/PEB-71) | Estados de tareas e indicadores. |
| T08 | [PEB-72](https://alesalve.atlassian.net/browse/PEB-72) | Eliminación y papelera. |
| T14 | Consultar Jira; no inventar su clave. | Prioridades y ordenamiento. |

El análisis de riesgos se citó en la conversación como [PEB-69](https://alesalve.atlassian.net/browse/PEB-69). Consultar su contenido antes de atribuirle clasificaciones o reglas específicas.

Los nombres T06, T07 y T08 identifican tareas de trabajo, no requisitos formales completos del producto. En el campo Requerimiento se utiliza la referencia acordada al ticket y, además, se expresa el comportamiento que el caso comprobará.

No crear identificadores adicionales del tipo BP o CQ. El usuario rechazó esa nomenclatura.

## 4. Producto y prioridades de calidad

Todo.ly permite gestionar tareas y organizarlas mediante proyectos, prioridad, vencimiento y estado de finalización.

Las funciones centrales para este trabajo son:

- Crear y editar contenido.
- Guardar y conservar cambios.
- Completar y reactivar tareas.
- Mantener indicadores coherentes.
- Asignar tareas al proyecto correspondiente.
- Eliminar y recuperar información.
- Gestionar prioridades, vencimientos y ordenamiento en los tickets que los cubran.

Los riesgos de mayor interés son la pérdida de información, alteración de contenido o estado, duplicación, afectación de elementos ajenos y resultados que solo existan temporalmente en la interfaz.

Home, Study, Personal y Shopping List presentan controles similares. No repetir automáticamente la misma prueba en los cuatro proyectos. Seleccionar representantes y añadir contrastes entre proyectos cuando el riesgo sea precisamente la independencia o el destino de los datos.

Inbox, Today y Next son filtros. Que compartan controles con los proyectos no demuestra que seleccionen tareas con las mismas reglas. Antes de diseñar casos sobre ellos, confirmar sus condiciones de inclusión y exclusión.

### Decisión vigente sobre jerarquías de tareas

Para los documentos y casos actuales, el usuario pidió trabajar con tareas independientes y retirar los escenarios de tareas padre/subtareas.

- Retirar T07-05, T07-06, T07-07 y T07-08 del diseño anterior.
- T07 conserva los casos originalmente numerados 1, 2, 3, 4, 9 y 10.
- Reemplazar el antiguo T08-03 sobre eliminación de una subtarea por recuperación de una tarea completada.
- El antiguo T08-14 sobre anidar en la papelera se reemplaza por intentar reordenar dentro de la papelera.
- Conservar los casos sobre proyectos y subproyectos: son funciones distintas y sí forman parte de la exploración reportada.

Existe una contradicción histórica: la exploración inicial del agente, capturas y documentación pública mostraron jerarquías; posteriormente el usuario indicó que no lograba reproducirlas y pidió retirarlas. La decisión de alcance anterior gobierna el diseño actual. No convertirla en una afirmación universal de inexistencia ni reintroducir los casos retirados como cobertura acordada. Si una tarea futura exige resolver esa contradicción, contrastar las evidencias y documentar el resultado.

## 5. Base de pruebas y resultados esperados

Los resultados esperados deben poder justificarse mediante:

1. Documentación del producto.
2. Mensajes y restricciones comunicados por la interfaz.
3. Observaciones exploratorias concretas, indicando sus condiciones.
4. Criterios de calidad propuestos por el equipo.

Una observación describe lo que ocurrió; no demuestra por sí sola que sea correcto. Si falta una regla, no inventar el resultado esperado.

Puede indicarse en lenguaje sencillo:

- Regla documentada.
- Comportamiento observado.
- Criterio propuesto por el equipo.
- Duda pendiente.

No se necesita crear un registro con códigos nuevos para usar estas distinciones.

Ejemplo: que un campo acepte un texto vacío no demuestra que deba aceptarlo. Tampoco se puede exigir su rechazo como regla oficial sin fundamento. Primero se contrasta la validación o se identifica expresamente el criterio del equipo.

Una duda que determina el resultado principal impide cerrar ese caso como listo para ejecución. Se puede avanzar con los demás casos independientes y dejar identificada la cobertura pendiente.

## 6. Diferenciar tipo, enfoque y técnica

| Concepto | Qué significa | Ejemplos |
|---|---|---|
| Tipo de prueba | Qué aspecto de calidad se evalúa. | Funcional, compatibilidad, usabilidad, accesibilidad, seguridad o rendimiento percibido. |
| Enfoque del escenario | Qué recorrido o condición se utiliza. | Positivo, negativo o alternativo. |
| Técnica de diseño | Cómo se derivan los casos a partir de reglas y riesgos. | Particiones de equivalencia, valores límite, casos de uso o tablas justificadas por las reglas. |

No escribir seleccionar pruebas funcionales como una obligación. Evaluar si corresponden funcionales, no funcionales o ambas y justificar la decisión.

Tampoco incluir todos los tipos para aparentar amplitud. Cada selección necesita objetivo, riesgo, procedimiento y criterio de evaluación.

Consideraciones acordadas:

- La compatibilidad debe relacionarse con configuraciones reales disponibles. No añadir Safari, iOS o Android solo porque sean ejemplos habituales.
- La accesibilidad y la seguridad pueden ser pertinentes, pero no son obligatorias en cada ticket.
- No declarar cumplimiento de un estándar completo por una comprobación manual limitada.
- Una medición de rendimiento desde el cliente necesita datos, condiciones y un criterio acordado; no inventar tiempos máximos.
- Un resultado negativo no significa una prueba fallida. El caso pasa si la aplicación maneja correctamente la condición no admitida.
- Reactivar, ocultar una sección o cambiar de proyecto suelen ser recorridos alternativos válidos, no entradas negativas.
- No fabricar escenarios inválidos cuando el control solo admite acciones válidas. Las condiciones sin elementos elegibles también pueden aportar cobertura.

## 7. Elección y fundamento de técnicas

### 7.1. Casos de uso

Utilizarlos para operaciones y recorridos observables:

- Crear y guardar.
- Editar o cancelar.
- Completar y reactivar.
- Eliminar, localizar en la papelera y recuperar.
- Consultar después de recargar o volver a iniciar sesión.

Explicar qué recorrido origina cada caso y qué riesgo comprueba. Decir únicamente técnica: casos de uso no aporta suficiente fundamento.

### 7.2. Particiones de equivalencia

Definir grupos que compartan una regla o tratamiento esperado y seleccionar representantes.

Ejemplos aplicables:

- Tarea pendiente frente a completada antes de eliminarla.
- Proyecto con completadas frente a proyecto sin completadas.
- Contenido textual frente a intento de incorporar un archivo como objeto al campo.

No declarar particiones diferentes solo porque los datos tengan nombres o extensiones diferentes. JPG, MP4 y PDF pueden ser muestras de una misma clase de entrada no admitida si la regla y el tratamiento son iguales.

### 7.3. Valores límite

Las clases incluyeron variantes de dos y tres valores. Respetar el material docente al aplicarlas.

Para un máximo confirmado L, un ejemplo de tres puntos es L−1, L y L+1; una selección de dos puntos puede comprobar L y el valor vecino de la partición inválida, L+1.

Primero debe existir una frontera justificable. La exploración puede buscarla, pero no se debe presentar una longitud arbitraria como límite del producto.

### 7.4. Tablas y análisis de estados

- El usuario rechazó forzar tablas de decisión para recorridos simples de edición, guardado y cancelación.
- Utilizarlas únicamente si las combinaciones de condiciones y resultados justifican el esfuerzo.
- El equipo mencionó tablas de verdad entre los contenidos de clase. No tratarlas automáticamente como sinónimo de tablas de decisión; consultar las diapositivas.
- El análisis pendiente → completada → pendiente puede apoyar el diseño. No afirmar que una técnica formal de transiciones fue exigida en clase sin comprobarlo.

## 8. Dos entregables de texto por ticket

### A. Comentario de análisis y resultado para Jira

Redactarlo de forma comprensible y, preferentemente, en tercera persona:

1. Análisis del área: operaciones, controles, estados y contexto.
2. Riesgos que orientan el diseño.
3. Reglas, restricciones y dudas relevantes, con su fundamento.
4. Tipos de prueba y escenarios seleccionados, con justificación.
5. Técnicas elegidas y cómo se aplicaron.
6. Lista resumida de casos, explicando para cada uno el fundamento de la técnica.
7. Cobertura pendiente y evidencia real de registro/revisión, cuando exista.

Formato recomendado para la lista:

| Caso | Objetivo o riesgo cubierto | Fundamento de la técnica aplicada |
|---|---|---|
| Número y título | Qué consecuencia se busca detectar. | Qué regla, partición o recorrido generó el caso y por qué aporta cobertura. |

La técnica y su fundamento van aquí, fuera de la ficha detallada de cada TC.

No escribir se registraron y revisaron los casos si solo se redactaron en el chat. En ese estado, indicar que están propuestos o preparados para registro.

### B. Casos detallados para TestLink

Cada caso debe contener exactamente los campos acordados:

- Título.
- Importancia, con una razón breve.
- Requerimiento.
- Precondiciones.
- Descripción sencilla.
- Tabla de pasos y resultado esperado por cada paso.
- Postcondiciones.

No añadir por defecto campos de severidad, prioridad de falla, riesgo potencial, tipo de prueba o técnica dentro de esta ficha. Los riesgos, tipos y técnicas se explican en el análisis y la lista resumida.

## 9. Plantilla de caso de prueba

### N. Título que identifica una acción y su objetivo

**Importancia:** **high**, **medium** o **low**, seguida de una justificación breve.

**Requerimiento:** PEB-XX / TXX. Comportamiento concreto que se comprobará.

**Precondiciones:** Se cumplen las precondiciones comunes. Añadir aquí los datos, estados o configuraciones específicos del caso.

**Descripción:** Una o dos frases sencillas sobre qué se comprobará.

| Paso | Resultado esperado |
|---|---|
| 1. Acción concreta, con proyecto, control y dato identificados. | Efecto observable correspondiente a esa acción. |
| 2. Acción siguiente. | Resultado comprobable de esa acción. |
| 3. Consulta o recarga, cuando aporte cobertura. | Contenido, estado, cantidad o ubicación que debe conservarse. |
| 4. Limpieza de los datos creados, después de conservar evidencia. | Situación concreta después de la limpieza. |

**Postcondiciones:** Estado final de los elementos de prueba, de los datos preexistentes y de la evidencia. Indicar si los datos permanecen en la papelera.

### Interpretación de importancia

- **high:** protege una operación esencial o evita pérdida, alteración, eliminación incorrecta o recuperación defectuosa de información.
- **medium:** comprueba una variante relevante, coherencia de visualización o condición especial cuyo efecto debe controlarse.
- **low:** comprobación secundaria con impacto limitado.

La importancia pertenece al diseño del caso. La severidad y la prioridad de una falla se determinarán al reportar un defecto real; no se asignan anticipadamente como campos del TC en este proyecto.

## 10. Precondiciones y datos de prueba

Base utilizada en los casos recientes:

1. Acceso a internet.
2. Sesión iniciada en Todo.ly con **camila@gmail.com**, usando las credenciales de prueba autorizadas por el equipo.
3. Existencia del proyecto predeterminado requerido; normalmente **Home**.
4. Preparación del estado inicial necesario y ausencia de nombres que puedan confundirse con los del caso.
5. Medio para notas y capturas; si un paso falla, conservar evidencia antes de limpiar.
6. Navegador y versión efectiva registrados.

Esta guía no contiene contraseñas. Las credenciales se obtienen del contexto autorizado del equipo.

### Reglas de preparación

- Utilizar Home como proyecto principal y Study para contrastar destinos o independencia.
- No depender del proyecto Uni creado durante una exploración anterior.
- En casos que esperan cantidades exactas desde cero, especificar Home sin pendientes ni completadas. No borrar información ajena para cumplir esa condición.
- Si no se puede partir de cero, registrar cantidades iniciales y adaptar de forma explícita los resultados; no mezclar cantidades absolutas y relativas.
- Para subproyectos, crear proyectos temporales identificados como datos de prueba. No eliminar proyectos predeterminados para demostrar una operación.
- Usar nombres exactos y únicos, por ejemplo Prueba T08-03 - recuperar completada.
- Los casos son independientes. No exigir que otro caso haya terminado correctamente para preparar el siguiente, salvo que se documente una dependencia real.

### Entorno

El equipo utiliza Windows. Los casos recientes se redactaron para Chrome; la versión debe comprobarse al ejecutar. Camila reportó Windows 11 y Firefox 159.0.1 como otra configuración disponible.

No inventar una versión de Chrome ni convertir una versión mencionada por un agente en una versión verificada. Las observaciones realizadas en el navegador integrado del chat no equivalen a ejecuciones en Chrome o Firefox.

## 11. Cómo redactar pasos y resultados

- Conservar los textos reales: Home, Projects, Add new Todo, type here…, Add, Done Items, See all, Hide, Delete, Recycle Bin.
- Identificar la ubicación del control cuando ayude: panel izquierdo, extremo derecho de la tarea, esquina superior derecha.
- Especificar el dato que se escribe y el número de veces que se pulsa un control cuando sea relevante.
- Evitar pasos como probar edición, verificar que funciona o guardar de alguna forma.
- Cada fila debe tener un resultado observable. No usar funciona correctamente como único resultado.
- Una fila puede agrupar preparación sencilla, pero no acumular varios objetivos independientes difíciles de diagnosticar.
- Después de una acción asíncrona, comprobar que termine antes de decidir el resultado.
- No exigir un texto de alerta, botón o confirmación que no se haya identificado.
- Incluir F5 o un nuevo inicio de sesión cuando el riesgo sea persistencia; no repetirlos indiscriminadamente en todos los casos.
- Una ausencia de datos puede verse sin insignia numérica junto al proyecto. No exigir un cero visible si la interfaz simplemente oculta la insignia.

## 12. Reglas vigentes de T06 — Creación y edición

- El proyecto de referencia es Home.
- La creación puede utilizar Add o Enter.
- Se identificaron edición directa y acceso mediante Edit.
- Enter confirma la edición. Escape fue observado con dudas en algunas condiciones; no generalizar que siempre funciona con cualquier entrada.
- Los resultados esperados de entradas vacías o solo espacios necesitan una regla o un criterio del equipo claramente identificado.
- El usuario retiró del conjunto de T06 los antiguos casos 10, sobre código durante la edición, y 12, sobre operación mediante teclado.
- Conservó el antiguo caso 11, de texto extenso. Con los originales 1–9 y 11 se obtiene el conjunto de diez discutido. No eliminar automáticamente el antiguo caso 9, sobre entrada de código durante creación, por confundirlo con el 10 retirado.
- Se redactó además un caso sobre intentar incorporar archivos al campo. Su inclusión final o el caso al que sustituirá no quedó fijado; no aumentar automáticamente el conjunto acordado.

### Texto extenso

El usuario reportó haber introducido aproximadamente 820 000 caracteres con espacios en tareas y títulos de proyectos sin advertencia visible. El texto extendía mucho la página.

Esto significa aceptación observada para ese dato, no ausencia demostrada de cualquier límite. Tampoco demuestra por sí solo conservación íntegra después de recargar.

El caso debe:

- Preparar una referencia de longitud conocida.
- Comprobar aceptación y conservación del contenido.
- Recuperar y comparar el texto, no juzgar truncamiento solo por su presentación.
- Comprobar que otras tareas y el formulario sigan utilizables.
- Registrar las dificultades de navegación sin inventar un umbral formal de usabilidad.

### Archivos frente a texto

La prueba de archivos se refiere al campo textual de creación. Escribir informe.pdf, pegar una ruta o escribir una URL sigue siendo introducir texto.

Para probar un archivo se debe intentar incorporar el objeto real, por ejemplo mediante arrastre. Si el navegador abre el archivo, eso no demuestra que Todo.ly lo haya adjuntado.

El rechazo de adjuntos en ese campo se planteó como criterio del equipo, no como regla oficial verificada para todos los formatos. No extrapolarlo a Notes Pro, enlaces u otras funciones del producto.

Una entrada de código de prueba sin ejecución observable tampoco demuestra protección completa frente a todas las variantes de una vulnerabilidad.

## 13. Reglas vigentes de T07 — Estados e indicadores

- Marcar una tarea independiente la retira de pendientes y permite consultarla en completadas.
- Desmarcarla desde completadas la reactiva.
- See all, el número y Done Items permiten desplegar la sección de completadas; Hide la oculta.
- Las pendientes permanecen visibles por encima de las completadas desplegadas.
- Mostrar u ocultar la sección no cambia estados ni elimina información.
- Done Items corresponde al proyecto seleccionado; se contrastó Work con Home.
- El número junto al proyecto representa pendientes en los contextos independientes cubiertos.
- La información debe conservarse al recargar y al iniciar una nueva sesión.
- El usuario confirmó que las tareas de Done Items no se pueden arrastrar desde esa sección del proyecto.

No confundir esa última restricción con la recuperación desde Recycle Bin.

### Casos que permanecen en el diseño actual

| Numeración original | Caso |
|---|---|
| 1 | Completar una tarea independiente. |
| 2 | Reactivar una tarea completada. |
| 3 | Consultar y ocultar completadas. |
| 4 | Mantener estados e indicadores independientes entre proyectos. |
| 9 | Conservar estados después de recargar e iniciar sesión. |
| 10 | Mantener coherencia en ciclos sucesivos de completar y reactivar. |

No reemplazar los cuatro casos retirados por pruebas redundantes solo para volver a diez.

### Hallazgo histórico de contadores

En la exploración del agente se observaron desfases de Done Items que se corregían con F5. Los ejemplos documentados estuvieron asociados a los experimentos de jerarquías posteriormente retirados del alcance.

No afirmar que esa falla está reproducida en todos los casos actuales de tareas independientes. Mantener la comprobación del contador inmediato y contrastarlo con la recarga cuando corresponda.

Si un contador resulta incorrecto y F5 lo corrige, la comprobación inmediata permanece fallida: la recarga no convierte retroactivamente el paso en satisfactorio.

## 14. Reglas vigentes de T08 — Eliminación y papelera

### 14.1. Eliminación individual y masiva

- Delete retira la tarea seleccionada del proyecto y permite localizarla en Recycle Bin, según la exploración reportada.
- Delete all, junto a Done Items, afecta a las completadas del proyecto seleccionado.
- Las pendientes y los datos de otros proyectos deben conservarse.
- El estado vacío de completadas debe tratarse sin eliminar pendientes.
- La sección oculta de completadas no debe reducir el alcance de Delete all.
- No confundir Delete all del proyecto con Empty Recycle Bin.

### 14.2. Recuperación

- La recuperación se realiza arrastrando desde Recycle Bin hacia un proyecto de Projects.
- Una tarea pendiente recuperada aparece en pendientes.
- Una tarea completada recuperada aparece en Done Items y conserva su estado completado.
- Puede recuperarse en el proyecto original o en otro proyecto.
- La tarea recuperada debe dejar de aparecer en la papelera y existir una sola vez en el destino.
- El mensaje naranja reportado es: **Info. Item has been moved to project: Home**, o Study u otro destino elegido.
- El color naranja de un mensaje Info no convierte un traslado exitoso en error.

No proponer un botón Restore ni un menú de recuperación: no corresponden a la interfaz reportada.

### 14.3. Controles de una tarea en Recycle Bin

- No tiene menú de opciones.
- Su checkbox está deshabilitado y no permite cambiar su estado.
- El checkbox deshabilitado no impide recuperarla mediante arrastre.
- La restricción observada para arrastrar completadas en Done Items no se aplica por inferencia a las completadas de Recycle Bin.

### 14.4. Reordenar dentro de la papelera

No se permite reorganizar sus elementos. La advertencia reportada contiene:

> You can't rearrange items in a Filter list. You can only move them to projects.

Preparar Sort By: Order antes de este escenario para no mezclar la restricción de la papelera con una restricción de ordenamiento.

El intento inválido no debe perder ni duplicar tareas y debe permitir una recuperación válida posterior.

### 14.5. Eliminación de subproyectos

- La confirmación reportada es **Do you really want to delete the selected project?**
- Cancelar conserva el subproyecto y sus tareas.
- Aceptar retira el subproyecto y sus tareas aparecen en Recycle Bin sin un contenedor que represente al proyecto.
- El proyecto eliminado no se observó como elemento recuperable en la papelera.
- No afirmar borrado físico en base de datos ni irreversibilidad absoluta solo por la existencia de una confirmación.
- Utilizar un subproyecto temporal con tareas desechables; conservar Work y los proyectos originales.

### 14.6. Vaciado

La documentación pública describe Empty Recycle Bin como eliminación definitiva del contenido de la papelera. La comprobación manual se limita a su efecto observable, no prueba el borrado físico de registros.

Diseñar y ejecutar el caso con una papelera cuyo contenido sea exclusivamente desechable y esté identificado. No vaciar una papelera compartida para limpiar rutinariamente otros casos.

### Lista actual de casos de T08

| Caso | Objetivo |
|---|---|
| 1 | Eliminar una pendiente sin afectar a otra tarea. |
| 2 | Eliminar individualmente una completada. |
| 3 | Recuperar una completada conservando su estado; reemplaza el antiguo caso de subtarea. |
| 4 | Eliminar una tarea sin afectar a otro proyecto. |
| 5 | Eliminar todas las completadas de un conjunto mixto. |
| 6 | Intentar Delete all sin completadas. |
| 7 | Limitar Delete all al proyecto seleccionado. |
| 8 | Eliminar completadas mientras su sección está oculta. |
| 9 | Conservar la eliminación después de recargar y volver a iniciar sesión. |
| 10 | Vaciar Recycle Bin sin afectar a tareas de los proyectos. |
| 11 | Recuperar una pendiente en su proyecto original. |
| 12 | Recuperar una pendiente en otro proyecto. |
| 13 | Intentar cambiar el estado mediante el checkbox deshabilitado de la papelera. |
| 14 | Intentar reordenar dentro de Recycle Bin; reemplaza el escenario de anidación. |
| 15 | Cancelar la eliminación de un subproyecto con tareas. |
| 16 | Confirmar la eliminación de un subproyecto y recuperar una de sus tareas pendientes. |

Esta lista es el diseño propuesto en la conversación, no una certificación de registro, ejecución o revisión. Consultar TestLink y Jira antes de anunciar su estado.

## 15. Ordenamiento y mensajes reportados

| Selección | Mensaje reportado | Regla comunicada |
|---|---|---|
| Order | Info. Sorted by Order. You can rearrange items by dragging them. | Permite reorganizar mediante arrastre. |
| Priority | Info. Sorted by Priority. You cannot rearrange items, you can only move them to different project | Impide reorganizar y permite trasladar a proyectos. |
| Due Date | Info. Sorted by Due Date. You cannot rearrange items, you can only move them to different project | Impide reorganizar y permite trasladar a proyectos. |

Los textos anteriores proceden del reporte del usuario. Al ejecutar un caso que compare mensajes literales, conservar evidencia de su redacción y puntuación efectivas.

No confundir:

- Reordenar: cambiar posición en la misma lista.
- Trasladar: cambiar de proyecto.
- Recuperar: trasladar desde Recycle Bin a un proyecto.
- Completar/reactivar: cambiar el estado.

## 16. Ejemplo completo del formato acordado

### 3. Recuperar una tarea completada conservando su estado

**Importancia:** **high**, porque recuperar una tarea no debe modificar el estado de finalización que tenía antes de eliminarla.

**Requerimiento:** PEB-72 / T08. Una tarea completada recuperada desde Recycle Bin debe aparecer en Done Items del proyecto de destino, conservando su contenido.

**Precondiciones:** Se cumplen las precondiciones comunes. Home no contiene tareas pendientes ni completadas y no existen los nombres utilizados.

**Descripción:** Comprobar la recuperación de una tarea completada y la conservación de su estado.

| Paso | Resultado esperado |
|---|---|
| 1. Abre Home y crea mediante Add las tareas Prueba T08-03 - recuperar completada y Prueba T08-03 - control pendiente. | Aparecen dos tareas pendientes. |
| 2. Marca el checkbox de Prueba T08-03 - recuperar completada y despliega las completadas mediante See all, si están ocultas. | La seleccionada aparece en completadas; la de control permanece pendiente y Done Items muestra 1. |
| 3. Abre el menú de opciones de la completada y selecciona Delete. | La tarea desaparece de completadas y Done Items muestra 0. La de control permanece pendiente. |
| 4. Abre Recycle Bin y localiza la eliminada. | Aparece una sola tarea con el nombre previsto. |
| 5. Arrástrala mediante su asa de puntos sobre Home, en Projects. | Aparece Info. Item has been moved to project: Home y la tarea sale de la papelera. |
| 6. Abre Home y despliega Done Items. | La recuperada aparece completada, con su checkbox marcado y su nombre original. La de control sigue pendiente y Done Items muestra 1. |
| 7. Presiona F5 y consulta Home y Recycle Bin. | La recuperada continúa completada en Home, aparece una sola vez y no permanece en la papelera. La de control conserva su información. |
| 8. Conserva la evidencia, desmarca la completada y elimina ambas tareas mediante sus menús y Delete. | Home queda sin las tareas creadas por el caso. |

**Postcondiciones:** Las dos tareas están retiradas de Home e identificadas en Recycle Bin después de la limpieza. Queda evidencia de que la recuperación conservó el estado completado.

El fundamento de la técnica para este ejemplo debe aparecer en el comentario del ticket: se seleccionó un representante de la partición de completadas y se recorrió eliminación → recuperación → consulta para comprobar que recuperar no equivale a reactivar.

## 17. Limpieza, evidencias y reporte

- Preparar únicamente datos desechables y registrar qué se creó o modificó.
- Conservar evidencia antes de limpiar un caso fallido.
- Indicar el destino final de cada dato: proyecto, completadas, papelera o retirado definitivamente.
- Delete deja información en Recycle Bin. No escribir cuenta restaurada al estado inicial si la papelera conserva datos nuevos.
- Para retirar una completada mediante la limpieza acordada, se puede reactivarla y eliminarla desde pendientes después de documentar el resultado.
- Si se pide explorar y dejar la cuenta como estaba, registrar primero el estado inicial y comprobar la restauración al terminar.
- No inferir cancelaciones disponibles en todas las operaciones porque exista una confirmación al eliminar proyectos.
- Una falla lleva el resultado esperado y observado, pasos, datos, entorno y evidencia según la plantilla del equipo. Severidad y prioridad se evalúan en ese reporte.
- No atribuir una causa interna, pérdida física de base de datos o cobertura completa de seguridad a partir de observaciones de interfaz.
- La automatización de redacción o de interacción no convierte esta práctica en una suite de pruebas automatizadas: el alcance acordado es manual.

## 18. Registro y revisión entre integrantes

Al registrar:

1. Utilizar la organización real del proyecto de TestLink.
2. Incorporar las precondiciones comunes a cada caso o garantizar que sean accesibles sin depender de este chat.
3. Mantener la tabla de paso y resultado esperado por paso.
4. Utilizar la importancia acordada: high, medium o low.
5. Conservar la referencia PEB-XX / TXX y el comportamiento comprobado.
6. Añadir al ticket los identificadores o enlaces reales de los casos.
7. Solicitar o registrar la revisión del otro integrante según el proceso del equipo.
8. Documentar los cambios derivados de la revisión.

No renumerar identificadores reales de TestLink ni reasignarlos a casos distintos para ocultar retiradas. Si la numeración solo existe en un borrador, puede actualizarse con una correspondencia explícita.

## 19. Revisión antes de entregar

- [ ] Se leyó el ticket correcto y se respetó su alcance.
- [ ] El análisis explica riesgos concretos, reglas y dudas.
- [ ] Cada técnica tiene una aplicación real y una justificación por caso.
- [ ] Los tipos de prueba se eligieron por pertinencia.
- [ ] No se inventaron límites, controles, mensajes ni funciones.
- [ ] No se reintrodujeron los escenarios de jerarquías de tareas retirados.
- [ ] La ficha de cada TC contiene únicamente los campos acordados.
- [ ] Se utiliza importancia, no severidad o prioridad de falla.
- [ ] Cada paso tiene un resultado verificable.
- [ ] Los datos, controles y estados iniciales permiten reproducir el caso.
- [ ] La limpieza y las postcondiciones describen dónde terminan los datos.
- [ ] Se diferencian diseñado, registrado, revisado, ejecutado y fallido.
- [ ] No se afirma cobertura o evidencia que todavía no existe.

## 20. Evidencia histórica disponible en este workspace

Los siguientes archivos sirven como antecedentes; no sustituyen la decisión de alcance vigente ni acreditan ejecuciones en Chrome:

- [Observaciones de T07](C:/Users/usser/Documents/ChatGPT/Calidad/output/t07-observaciones.json).
- [Contador antes de F5](C:/Users/usser/Documents/ChatGPT/Calidad/output/t07-contador-antes-f5.png).
- [Contador después de F5](C:/Users/usser/Documents/ChatGPT/Calidad/output/t07-contador-despues-f5.png).
- [Captura histórica del grupo de tareas](C:/Users/usser/Documents/ChatGPT/Calidad/output/t07-grupo-completado.png).
- [Cuenta restaurada tras T07](C:/Users/usser/Documents/ChatGPT/Calidad/output/t07-cuenta-restaurada.png).
- [Consulta de T08 sin modificación de tareas](C:/Users/usser/Documents/ChatGPT/Calidad/output/t08-consulta-sin-cambios.png).

El archivo exploratory-testing-freestyle.md de la raíz trata sobre Toolshop, otra aplicación. No utilizar sus reglas, hallazgos ni datos como base de Todo.ly.

### Material de clase disponible

Las siguientes rutas se comprobaron como existentes. Su inclusión no significa que esta guía sustituya la lectura de sus contenidos:

- [Consigna de la práctica](<C:/Users/usser/Desktop/Uni/GesCALIDADSistemas/11P3_SIS312_BlackBoxTesting2026Nov.pdf>).
- [Plantilla de plan de pruebas](<C:/Users/usser/Desktop/Uni/GesCALIDADSistemas/Plantilla de Plan de Pruebas de Software.pdf>).
- [Plantilla de casos y ejemplos](<C:/Users/usser/Desktop/Uni/GesCALIDADSistemas/Plantilla para Casos de Prueba y Ejemplos.pdf>).
- [Plantilla de reporte de fallas](<C:/Users/usser/Desktop/Uni/GesCALIDADSistemas/Plantilla para reporte de fallas.pdf>).
- [Diapositivas de plan, casos y fallas](<C:/Users/usser/Desktop/Uni/GesCALIDADSistemas/Plan de Pruebas, Casos de Prueba y Fallas.pdf>).
- [Diapositivas de técnicas de caja negra](<C:/Users/usser/Desktop/Uni/GesCALIDADSistemas/Tecnicas de Black Box Testing.pdf>).

El documento PlanPruebasTodo.ly se consulta mediante el conector de Google Drive por su nombre; esta guía no dispone de un enlace verificado al documento.

Las fuentes públicas complementarias son la [descripción oficial del producto](https://todo.ly/) y el [blog oficial](https://todo.ly/blog/). Contrastar su vigencia antes de convertir una publicación histórica en una regla de la versión actual.

## 21. Instrucción breve para el siguiente agente

> Lee esta guía y el ticket solicitado antes de redactar. Entrega primero un comentario de análisis con riesgos, reglas, elección de tipos de prueba y una lista resumida que explique el fundamento de la técnica de cada caso. Después desarrolla los TC con título, importancia justificada, requerimiento, precondiciones, descripción breve, tabla de pasos/resultados y postcondiciones. Mantén fuera de la ficha detallada la explicación de técnicas, tipos y riesgos. Usa datos desechables, controles reales y proyectos predeterminados cuando corresponda. Distingue lo observado de lo esperado y resuelve las dudas que cambien el resultado principal. Aplica las últimas correcciones de T06, T07 y T08; no reintroduzcas tareas padre/subtareas en el alcance actual. No declares casos registrados, revisados o ejecutados sin evidencia real y no modifiques herramientas externas si la solicitud solo pide redacción.
