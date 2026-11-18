# Respuesta al encargo 07 — T10, tres contrastes manuales

Autor: Claude (diseño). **No es una revisión independiente**; queda pendiente la llamada de revisión y la del integrante del equipo. No se usaron navegador, Jira, TestLink, git ni `.secrets/`; no se ejecutaron comandos. No se leyeron PDF ni `revision-testlink/`.

## 1. Archivos modificados

| Archivo | Cambio |
|---|---|
| `trabajo/T10/casos-listos.json` | Se insertaron T10-04, T10-05 y T10-06 (orden numérico, después de T10-03). Los seis objetos registrados (01/02/03/08/09/10) **no se modificaron** en ningún carácter: la inserción se hizo con un único reemplazo situado entre el cierre de T10-03 y la apertura de T10-08. |
| `trabajo/T10/casos-pendientes.json` | Queda solo T10-07, con el contenido anterior idéntico. |
| `trabajo/T10/analisis-diseno.md` | Solo la parte anterior a `<!-- FICHAS_GENERADAS -->`: encabezado de estado, §1, R4 en §2, §3 reglas, §4 escenarios, §5 (particiones, nueva tabla de decisión 5.2, UC3/UC4 en 5.3, técnicas no aplicadas 5.4), §6 lista, §7, §8, §9 y título de la sección de fichas. Se conservan los seis IDs/enlaces TL-66…TL-71, las evidencias y el comentario 10226. |

**Nota para Codex:** la parte posterior a `FICHAS_GENERADAS` sigue teniendo las fichas antiguas de 04/05/06 bajo "Candidatos pendientes". Hay que regenerarla desde el JSON y, si corresponde, actualizar `casos.json`, que este encargo no me autorizaba a tocar.

## 2. Casos nuevos

| Caso | Título | Pasos | Importancia |
|---|---|---|---|
| T10-04 | Cambio de contraseña en Settings con Old Password incorrecto muestra Invalid Password y conserva la vigente | 18 | high |
| T10-05 | Cambio de contraseña en Settings con Old Password vigente rechaza la clave reemplazada y da acceso con la nueva | 23 | high |
| T10-06 | Edición de Email en Profile descartada con Cancel conserva el correo original de B | 10 | high |

Los tres siguen la rúbrica: descripción de una sola oración que empieza con "Validar que…", precondiciones nominales, una acción por paso, controles y datos en **negrita** y resultados observables. Usan cuentas genéricas y registro privado. El único valor escrito es la contraseña incorrecta sintética `Prueba-T10-04-incorrecta`, que no es una credencial real. En T10-05, Login, Email, Password y el botón Login (Submit) van en pasos separados. No contiene un segundo cambio de contraseña: el propio cambio b) sirve de restauración, y así se indica en las precondiciones y postcondiciones.

## 3. Fuente de cada resultado esperado

| Resultado | Fuente |
|---|---|
| Profile muestra Full Name, Email, Time zone, Old Password, New Password, Ok y Cancel, sin confirmación de contraseña | `exploracion.md` 11:07 y 15:51; `verificacion/restauracion-A-AX.txt` |
| 04 paso 5: aviso con el texto exacto **Invalid Password** y botón **OK**, con Profile visible detrás | `exploracion.md` 18/11 a); captura `evidencias/2026-11-18_T10_old-password-incorrecto-Invalid-Password.png`, revisada visualmente |
| 04 paso 7: OK cierra el aviso y Profile sigue abierto | `exploracion.md`, Contraste de conservación (formulario aún abierto tras el aviso de T10-03); mismo patrón que la ficha registrada T10-03 |
| 04 paso 13: la vigente sigue dando acceso | **Observación indirecta**: en b), el Old Password vigente fue aceptado inmediatamente después de a). No hubo un Login directo después de a). Ver duda 1 |
| Cancel/Logout/Login muestran área pública/autenticada con Settings y Logout | Patrón observado en T09 (rúbrica) y en el AX de restauración |
| 05 paso 7: Settings se cierra sin aviso; no se exige mensaje de éxito | `exploracion.md` b); captura `2026-11-18_T10_restauracion-reportada-area-autenticada.png`, revisada (área Work, sin mensaje) |
| 05 paso 12: error literal `Error. Wrong email or password…`, transitorio y en un solo intento | `contraste-restauracion.txt`; `exploracion.md` b) |
| 05 pasos 15–20: acceso con la objetivo; Full Name, Email y Time zone conservados | `verificacion/restauracion-A-AX.txt`; `evidencias/2026-11-18_T10_Login-original-A-verificado.png` |
| 05 paso 22: registro privado actualizado | `exploracion.md` b) ("actual = original") |
| 06 paso 5: Cancel cierra Settings sin guardar | `exploracion.md` c); mismo comportamiento de Cancel que en T10-01 |
| 06 paso 8: Email coincide exactamente con el original | `exploracion.md` c): captura 15:59 `2026-11-18_T10_email-original-tras-Cancel.png` y comparación AX con el registro privado |
| Precondición "menos de tres intentos fallidos" | Criterio operativo del equipo (decisiones §13), identificado como tal |

## 4. Decisiones y dudas

1. **Login con la vigente en T10-04.** Lo incluí para comprobar directamente que la clave no se sustituye (riesgo R1), como en T10-03. En la exploración solo se observó de forma indirecta. Así figura en §3 y en la nota de la tabla 5.2. Si la revisión prefiere limitar 04 a lo observado directamente, se pueden quitar los pasos 9–18 (Logout, Login y Profile) y ajustar el requerimiento y las postcondiciones.
2. **Campo Email tras el Login fallido (05 paso 13).** No consta si conserva el correo, así que el paso lo vuelve a escribir "sustituyendo cualquier contenido". No supone ningún comportamiento.
3. **New Password vacío:** duda pendiente, fuera de la tabla. No se diseñó ningún caso.
4. **T10-06:** no afirma que la dirección alternativa sea alias del mismo buzón, ni incluye Login de B. Las capturas con direcciones reales se tratan como evidencia privada.
5. **"todo.ly says"** aparece en la captura como cabecera del diálogo de Chrome. No se exige en el resultado; solo se exigen **Invalid Password** y **OK**.
6. **T10-08 (registrado)** sigue diciendo en sus postcondiciones que la restauración está "pendiente de confirmar". No lo modifiqué porque el encargo pide no alterar los seis. Ahora §8 del análisis indica que la restauración se realizó en b).

## 5. Conteos

- Diseñados: **9** (T10-01/02/03/04/05/06/08/09/10).
- Registrados en TestLink: **6** (TL-66…TL-71, 28 pasos). Por registrar: **3** (T10-04/05/06, 51 pasos), sin ID hasta su registro y verificación.
- Pendientes, no registrables: **1** (T10-07).
- `casos-listos.json`: 9 objetos; `casos-pendientes.json`: 1 objeto.
- Tabla de decisión: 3 reglas (R1→T10-03, R2→T10-04, R3→T10-05). Casos de uso: UC3 principal 05 / alternativas 04 y 03; UC4 alternativa Cancel 06 / principal 07 pendiente.
