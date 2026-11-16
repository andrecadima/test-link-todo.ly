# Estado inicial de las cuentas de prueba

Fecha: 16 de noviembre de 2026. Estado del documento: A y B verificadas por Login con las credenciales vigentes de .secrets. Inventario completo de ambas. No es ejecución formal de casos.

## Entorno y procedencia

macOS 26.6.2 (25G83), Chrome 157.0.8103.51 arm64, verificado en `chrome://version`. No se atribuye esta exploración a Windows ni a Firefox. El usuario confirmó que A y B fueron creadas hoy para esta práctica. El agente no acredita el envío inicial de esos registros: lo realizó el usuario.

Las comprobaciones de Login se realizaron en el perfil local aislado `Todo.ly QA cuenta B`. El nombre del perfil no identifica por sí mismo qué cuenta tiene sesión: se verificó la identidad mediante el correo exacto en Settings.

El otro perfil, `Todo.ly QA T09-T11`, conserva una sesión cuyo correo contiene un error de escritura y no coincide con A. Solo se consultó su identidad en Settings; no se editó ni cerró esa sesión. Queda excluido de las pruebas.

## Cuenta A — verificada

- Full Name: Andre Cadima.
- Login: aceptado con el correo exacto autorizado y la contraseña local guardada; identidad confirmada en Profile.
- Fecha y hora mostrada por la AUT: 16 de noviembre de 2026, 7:26–7:27 PM. No se usa el reloj de la AUT como evidencia de hora boliviana.
- Zona al registrarse, según captura del usuario: `(UTC-08:00) Pacific Time (US & Canada)`.
- Preparación autorizada: se guardó `(UTC-04:00) Georgetown, La Paz, Manaus, San Juan` y se reabrió Settings para confirmar. Este es el valor base acordado para la limpieza final. La interfaz no usa la etiqueta IANA America/La_Paz.

### Proyectos en orden

| Orden | Proyecto | Es subproyecto de | Pendientes | Done Items |
|---|---|---|---|---|
| 1 | Work | Raíz | 5 de ejemplo, incluyendo una tarea hija de ejemplo | 0 |
| 1.1 | Sub Project | Work | 0 | 0 |
| 2 | Home | Raíz | 0 | 0 |
| 3 | Study | Raíz | 0 | 0 |
| 4 | Personal | Raíz | 0 | 0 |
| 5 | Shopping List | Raíz | 0 | 0 |

Las cinco tareas de ejemplo de Work se conservan tal como estaban; no se ejecutan pruebas sobre la jerarquía de tareas. Textos iniciales:

1. Add new tasks using the field below
2. Move items to different project using drag and drop. (Drag the small handler in front of the task)
3. Hover your mouse over a project or item and click the icon on the right side of the item for more options
4. Try to drag and reorder items
5. Hija de la anterior: You can drag and drop task on each other to create sub tasks, like this

### Recycle Bin y filtros

Recycle Bin vacía: `There are no items to display`. Inbox, Today y Next también sin tareas pendientes; cada filtro muestra 0 Done Items. Se consultaron individualmente todos los proyectos y filtros; las capturas registran las vistas.

### Sort By y Settings

Sort By: Order. Notes: Hidden. Los campos de cambio de contraseña se encuentran vacíos.

| Campo | Valor inicial para restaurar |
|---|---|
| Full Name | Andre Cadima |
| Email | Correo original de cuenta A; referencia privada en .secrets |
| Time zone | (UTC-04:00) Georgetown, La Paz, Manaus, San Juan, tras preparación autorizada |
| Start Page | Work |
| First Day of Week | Sunday |
| Text Size | Small |
| Automatically set empty due date to | None |
| Show Project Tag in Filters | Marcado |
| Show context Menu when right clicking on item | Sin marcar |
| Automatically Edit Notes on Click | Marcado |

### Capturas de A

- `T09/evidencias/2026-11-16_A_inicio-Work.png`
- `T09/evidencias/2026-11-16_A_Profile-LaPaz.png`
- `T09/evidencias/2026-11-16_A_Default-Settings.png`
- `T09/evidencias/2026-11-16_A_inicial-Home.png`
- `T09/evidencias/2026-11-16_A_inicial-Study.png`
- `T09/evidencias/2026-11-16_A_inicial-Personal.png`
- `T09/evidencias/2026-11-16_A_inicial-Shopping-List.png`
- `T09/evidencias/2026-11-16_A_inicial-Sub-Project.png`
- `T09/evidencias/2026-11-16_A_inicial-Recycle-Bin.png`
- `T09/evidencias/2026-11-16_A_inicial-Inbox.png`
- `T09/evidencias/2026-11-16_A_inicial-Today.png`
- `T09/evidencias/2026-11-16_A_inicial-Next.png`

Al terminar el inventario se cerró únicamente la sesión A utilizada para verificar Login, en el perfil aislado, para probar la cuenta B.

## Cuenta B vigente — verificada

El usuario cambió el correo y la contraseña de B. La candidata anterior queda fuera del trabajo. El correo vigente se conserva en .secrets y se confirmó exactamente en Profile después de Login. El error inicial de formato se debió a que el correo en el archivo local estaba escrito como enlace Markdown: se normalizó a una dirección simple y Login fue aceptado. No fue un rechazo de la contraseña vigente.

- Full Name real: Andre Cadima 4.
- Login: aceptado con el correo y la contraseña actuales del archivo privado.
- Hora mostrada por la AUT: 7:34–7:35 PM del 16 de noviembre de 2026.
- Zona inicial de la cuenta: Pacific Time UTC-08. Se preparó la opción La Paz UTC-04 autorizada, se guardó y se reabrió Profile para confirmarla. Se utilizará ese valor como referencia de restauración.

### Proyectos en orden (consultados individualmente)

| Orden | Proyecto | Es subproyecto de | Pendientes | Done Items |
|---|---|---|---|---|
| 1 | Work | Raíz | 5 de ejemplo, incluida una hija de ejemplo | 0 |
| 1.1 | Sub Project | Work | 0 | 0 |
| 2 | Home | Raíz | 0 | 0 |
| 3 | Study | Raíz | 0 | 0 |
| 4 | Personal | Raíz | 0 | 0 |
| 5 | Shopping List | Raíz | 0 | 0 |

Work muestra los mismos cinco textos tutoriales descritos en A. Se conservarán sin operar sobre sus relaciones. Recycle Bin vacía; Inbox, Today y Next vacíos, con 0 Done Items. Sort By: Order y Notes: Hidden.

### Settings de B (consultados, sin inferirlos de A)

| Campo | Valor inicial para restaurar |
|---|---|
| Full Name | Andre Cadima 4 |
| Email | Correo original de B vigente, guardado en .secrets |
| Time zone | (UTC-04:00) Georgetown, La Paz, Manaus, San Juan, tras preparación autorizada |
| Start Page | Work |
| First Day of Week | Sunday |
| Text Size | Small |
| Automatically set empty due date to | None |
| Show Project Tag in Filters | Marcado |
| Show context Menu when right clicking on item | Sin marcar |
| Automatically Edit Notes on Click | Marcado |

### Capturas de B vigente

- `T09/evidencias/2026-11-16_B_Default-Settings.png`
- `T09/evidencias/2026-11-16_B_Profile-LaPaz.png`
- `T09/evidencias/2026-11-16_B_inicial-Home.png`
- `T09/evidencias/2026-11-16_B_inicial-Inbox.png`
- `T09/evidencias/2026-11-16_B_inicial-Next.png`
- `T09/evidencias/2026-11-16_B_inicial-Personal.png`
- `T09/evidencias/2026-11-16_B_inicial-Recycle-Bin.png`
- `T09/evidencias/2026-11-16_B_inicial-Shopping-List.png`
- `T09/evidencias/2026-11-16_B_inicial-Study.png`
- `T09/evidencias/2026-11-16_B_inicial-Sub-Project.png`
- `T09/evidencias/2026-11-16_B_inicial-Today.png`
- `T09/evidencias/2026-11-16_B_inicio-Work.png`

## Verificación final de la preparación

A se volvió a autenticar correctamente tras cerrar B y conserva su nombre, correo y zona La Paz. Evidencia adicional: `T09/evidencias/2026-11-16_A_Profile-LaPaz-verificado.png`. Ambas contraseñas vigentes fueron comprobadas mediante Login; no falta ninguna. No se conservan contraseñas en este documento ni en capturas.

Se completó la referencia de ambas cuentas. Próxima actividad: fase 2, exploración focalizada T09/T10/T11. Jira y TestLink continúan sin escrituras hasta el punto de control del diseño.
