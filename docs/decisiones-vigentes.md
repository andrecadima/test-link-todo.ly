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
