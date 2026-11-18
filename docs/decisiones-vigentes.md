# Decisiones vigentes para T09, T10 y T11

**Fecha:** 16 de noviembre de 2026.

Estas decisiones prevalecen sobre `guia-diseno-casos-prueba-todoly.md` y sobre el plan cuando se contradicen. Lo que no se menciona aquí se rige por la guía.

## 1. Tickets y áreas

| Ticket | Clave probable | Área (plan, sección 4.4) |
|---|---|---|
| T09 | PEB-73 | Registro, inicio y cierre de sesión, Remember Me y separación de cuentas. |
| T10 | PEB-74 | Perfil, credenciales y recuperación de acceso. |
| T11 | PEB-75 | Proyectos, subproyectos y movimientos. |

Las claves se dedujeron del patrón T06 = PEB-70 y T12 = PEB-76, y deben confirmarse en Jira. Si un ticket dice otra cosa, se sigue el ticket y se informa la diferencia al usuario.

## 2. Todo se documenta dentro de T09, T10 y T11

El plan prevé tickets de implementación separados. Para estos tres tickets no se crean.

El análisis, el diseño, el registro en TestLink y la evidencia van en el mismo ticket. El comentario separa la etapa de diseño de la de implementación, como permite la guía (sección 2).

## 3. Modelos a seguir

- **T06 (PEB-70):** cómo se analiza el área y cómo se aplican y justifican las técnicas de caja negra.
- **T12 (PEB-76):** cómo quedan los casos registrados en TestLink, con la captura como evidencia en los comentarios.

T09, T10 y T11 deben reunir las dos cosas: las técnicas de T06 y la evidencia de TestLink de T12.

## 4. Técnicas de caja negra

La evaluación espera ver técnicas aplicadas como en T06: cada una con su artefacto visible (tabla de particiones, valores límite, tabla de decisión, tabla de transiciones o flujos de caso de uso) y con trazabilidad a los casos que genera.

Las áreas de T09 a T11 tienen condiciones combinadas (login) y secuencias de estados (sesión, Remember Me, proyecto raíz ↔ subproyecto). Por eso es esperable usar tablas de decisión y transiciones de estado, además de particiones, valores límite y casos de uso.

Cada técnica debe derivar casos reales a partir de reglas confirmadas. No se fuerza una técnica ni se aplican valores límite sin una frontera confirmada (guía, sección 7). Las definiciones y formatos válidos son los de las diapositivas del docente.

## 5. Jerarquías

- **Subproyectos:** sí, en T11.
- **Tareas padre/subtareas:** no. El plan las menciona, pero el equipo las retiró del alcance (guía, sección 4). No se reintroducen.

## 6. Cuentas de Todo.ly

Esta sección reemplaza, para estos tickets, la precondición de la guía (sección 10) que usa camila@gmail.com.

- Toda la exploración se hace con **dos cuentas gratuitas nuevas, A y B**. Codex las crea con los correos que indique el usuario.
- **Nunca** se usa la cuenta de Camila ni ninguna cuenta personal del equipo: ni para iniciar sesión, ni para cerrar su sesión.
- Las contraseñas solo se guardan en `.secrets/cuentas-prueba.local.md`, fuera de git. Nunca van en Jira, TestLink, commits ni capturas.
- En las cuentas de prueba se permite:
  - cambiar contraseña, email, perfil y Settings;
  - para el email, usar otro alias del mismo buzón;
  - solicitar la recuperación de contraseña.
  Cada cambio se revierte o queda anotado de inmediato en `.secrets`.
- La eliminación de la cuenta sigue fuera de alcance (plan, sección 1.4): no se diseña ni se ejecuta.
- Al terminar, las cuentas no se eliminan. Quedan limpias y documentadas.
- Todo.ly se abre en un perfil de Chrome dedicado, o en una ventana de incógnito cuando no hace falta persistencia, para no tocar las sesiones abiertas ni las de TestLink y Jira. Para probar Remember Me hace falta el perfil dedicado: cerrar una ventana de incógnito borra las cookies.

## 7. Precondiciones en los casos

Los casos deben poder ejecutarlos otras personas con sus propias cuentas. Por eso:

- La cuenta se describe de forma genérica:
  - en general: "Sesión iniciada en Todo.ly con una cuenta gratuita de prueba (cuenta A)";
  - para separación de cuentas: "Dos cuentas gratuitas de prueba sin proyectos compartidos (A y B)";
  - para recuperación: "Cuenta de prueba cuyo buzón controla quien ejecuta el caso".
- No se escriben correos ni contraseñas reales.

## 8. TestLink

La URL vigente es **http://68.211.149.112**. La guía menciona Railway y el plan menciona Azure, pero esta IP es la que se usa ahora.

## 9. No duplicar otros tickets

| Zona | Ticket que la cubre |
|---|---|
| Creación y edición de tareas, estados, papelera | T06, T07, T08 |
| Eliminación de subproyectos | T08 (casos 15 y 16) |
| Vencimientos, hora, zona horaria y fecha predeterminada | Ticket de vencimientos de Camila (T12 o T13; confirmar en Jira) |
| Filtros Inbox, Today y Next | Ticket de filtros de Camila (T12 o T13; confirmar en Jira) |
| Prioridades y ordenamiento | T14 |

Si un caso de T09 a T11 toca alguna de estas zonas, se enfoca en el riesgo propio de su ticket y menciona el solapamiento. Por ejemplo, T10 no diseña casos de zona horaria aunque esa opción esté en Settings.

## 10. Fuera de alcance

Eliminación completa de la cuenta, funciones Pro, colaboración y compras, API, creación de tareas por correo, aplicación móvil, servicios externos, y pruebas de carga, estrés, penetración o auditorías completas.

## 11. Fechas

La demostración y el cierre del sprint son el **18 de noviembre de 2026**. Se atienden primero los riesgos altos.

## 12. Aclaración del usuario sobre Timezone (16 de noviembre)

En T09, Timezone se trata únicamente como campo de Signup: obligatoriedad, valores ofrecidos y posibilidad de dejarlo vacío. No se diseñan en T09 efectos de la zona sobre fechas o vencimientos; corresponden a T12 / PEB-76.

Para las cuentas A y B el usuario solicita America/La_Paz. Signup no muestra identificadores IANA: la opción visible correspondiente a La Paz, Bolivia, es `(UTC-04:00) Georgetown, La Paz, Manaus, San Juan`. Se registrará ese texto exacto en el estado inicial. No se confundirá con `(UTC-07:00) Chihuahua, La Paz, Mazatlan`.

## 13. Priorización para la demo — 17 de noviembre

Instrucción posterior del usuario: trabajar de principio a fin por ticket, en orden T10, T09 y T11. Acotar la exploración pendiente a aproximadamente una hora por ticket y declarar las dudas restantes. Continuar sin los cuatro PDF faltantes, utilizando el formato de la guía y las definiciones ya recuperadas del original de técnicas; no releer completos los PDF.

El punto de control se realiza por ticket: presentar su diseño completo y esperar OK antes de registrarlo en TestLink y documentarlo en Jira. Mientras el usuario revisa, explorar el siguiente ticket. Después del registro y comentario autorizados, actualizar CONTINUIDAD.md, commit y push. La limpieza de los datos temporales se realiza al terminar los tres tickets.

El enlace de recuperación debe usar HTTPS: **Criterio del equipo** establecido expresamente por el usuario. Incluirlo como caso de seguridad observable y mencionar el hallazgo para confirmar durante la ejecución; no reportarlo todavía en la planilla de fallas.

Login: máximo tres intentos fallidos por cuenta en la exploración acotada. Si Remember Me o los arrastres no se pueden operar con la herramienta, pedir ejecución manual al usuario y observar el resultado; no atribuir los fallos de la herramienta a Todo.ly.

## 14. Orquestación y autorización de registro — 17 de noviembre, 19:45

Rige `PROMPT_ORQUESTACION.md`, proporcionado expresamente por el usuario. Codex conserva navegador, Jira MCP, secretos y git. Claude Code CLI propone diseños y revisiones, sin navegador, Jira, TestLink, git ni acceso a `.secrets/`; cada encargo limita los archivos que puede escribir.

T10 tiene OK del usuario, sujeto a aplicar los ajustes indicados y revisar el diseño. T09/T11 pueden registrarse y publicarse sin otro punto de control del usuario cuando la revisión independiente no tenga bloqueantes y las observaciones no bloqueantes se resuelvan o documenten. Si Claude no está instalado o autenticado, Codex realiza esa revisión con el checklist de la guía §19 y lo informa.

Se registra **dentro de la suite existente Todo.ly tests**, sin crear suites por ticket. El XML de entrada usa raíz `<testcases>`, sin IDs asignados y sin actualizar casos existentes. Se comprueba el árbol antes de importar y cada caso después. La exportación real final es `testlink-xml/todo-ly-tests.xml`; de ella se extraen los XML por ticket mediante script.

El usuario realiza la introducción de credenciales y los arrastres. Codex agrupa los pasos manuales en una sola lista por ticket, con orden y datos vinculados al registro privado, sin publicar secretos. Dudas de más de 15 minutos se declaran pendientes. Tras tres fallos de un paso del navegador se solicita ayuda concreta. La revisión de Claude no sustituye la revisión de otro integrante.

El cierre incluye configuración y cuentas restauradas, datos temporales retirados, papelera vacía, evidencia final, comentarios publicados conservados localmente y auditoría final. No se cambian estados de Jira ni se eliminan cuentas.

## 15. Coordinación y rúbrica — 18 de noviembre

El usuario confirmó que Codex termina T09, T11 y fase 6 y sigue publicando en sus tickets Jira. PROMPT_REVISION_TESTLINK.md es para otro Claude por API; su prohibición de Jira y autorización sobre otros tickets no se trasladan a Codex. No se modifican casos ajenos. Los archivos nuevos de revision-testlink/ se incorporan a los commits sin modificarlos y sin publicar secretos.

Antes de registrar T09/T11: título con funcionalidad, condición y resultado; descripción iniciada con Validar que; precondiciones como estados/datos, sin verbos; una acción por paso con controles/datos exactos destacados y resultados observables. Se conserva objetivo, cobertura, IDs, importancia y Manual. Prevalecen las cuentas genéricas y ausencia de secretos de §7. Summary presenta primero la descripción, después requerimiento y postcondiciones; la importancia y su razón se mantienen en ficha/análisis y su campo nativo. El XML convierte la negrita de los controles a strong.

El usuario solicitó de nuevo una sola lista manual de T10 a/b/c. Cuando confirme resultados, Codex completa 04/05/06, verifica y registra solo esos tres y añade IDs/enlaces al comentario PEB-74 conservando todo su contenido. La restauración de A es necesaria también para el cierre.


## 16. Corrección de fundamento de técnicas — 18 de noviembre

El usuario observó que la tabla publicada de T10 no explicaba con claridad la técnica y aportó ejemplos docentes de decisión y casos de uso. Se contrastaron nuevamente las secciones del PDF original, sin releer otros materiales completos. No se conserva una etiqueta de técnica por apariencia de tabla. Para T10 se adopta casos de uso como fundamento principal: actor A, sistema S, escenario de éxito, extensiones ancladas al paso y casos derivados explícitos. Las condiciones inciertas siguen pendientes: casos de uso no autoriza inventar sus resultados.

La tabla de Settings solicitada anteriormente se mantiene separada, en formato docente: condiciones arriba, acciones debajo, columnas como reglas, T/F y Execute. Las combinaciones factibles con New Password vacío se muestran como pendientes; no se presentan como reglas confirmadas ni generan casos listos. No se fuerza particiones de equivalencia en T10. La instrucción no elimina técnicas justificadas de T09/T11 ni permite retocar casos ajenos.

## 17. Corrección de T09 por indicación de Andre — 18 de noviembre

En el comentario de PEB-73 se fundamentan los trece casos de T09 únicamente con casos de uso: flujos principales, extensiones ancladas, respuestas del sistema y derivación a IDs reales. Se retiran los artefactos anteriores de particiones, decisión y estados de ese comentario y se actualiza su lista resumida. La tabla de particiones anterior no justificaba adecuadamente las clases al mezclar variables y condiciones conjuntas. No se concluye que las otras técnicas sean inválidas en general. TestLink y sus XML finales se conservan; las etiquetas antiguas R1–R5 de las fichas de Login tienen una correspondencia explícita hacia UC2 para mantener la trazabilidad. T09-08 continúa pendiente, sin resultado inventado. Esta instrucción se limita a T09.
