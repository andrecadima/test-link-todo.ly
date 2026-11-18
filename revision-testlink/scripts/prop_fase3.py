"""Fase final (18/11, 17:24): T09, T10 y T11 registrados por Codex. Se evalúa la versión ACTUAL.

- T09 (TL-72..84), T10-04..06 (TL-85..87) y T11 (TL-88..94): cumplen la rúbrica; solo el prefijo del título
  («TXX-NN.») no sigue el formato acordado «TXX-NN - ». Se cambia únicamente el nombre.
- T10-01..03 y T10-08..10 (TL-66..71): se conservan Preconditions, «Importancia», requerimiento y
  «Postcondiciones» tal como están; se reemplaza la descripción por «Validar que…», se ponen en negrita
  controles y datos, se separan en pasos propios las acciones que el caso prueba y se completa el título.
  TL-66: la autora quitó el rótulo del requerimiento; se aplica la misma decisión que en T12/T13
  («Requerimiento: PEB-74 / T10. <texto de la autora>»).
"""
import html as _html
import json
import re

import modelo
import prop_t10

SOLO_TITULO = [f"TL-{i}" for i in list(range(72, 85)) + list(range(85, 88)) + list(range(88, 95))]

PUBLICA = "Se muestra la página pública con **Login** y **Sign Up Free**, con la sesión cerrada."
AUTENTICADA = "Se muestra el área autenticada con **Settings** y **Logout**."

PASOS = {
"TL-66": None,  # los de prop_t10 ya separan la acción probada
"TL-67": [
    ("Abrir **Settings** / **Profile** y anotar el **Full Name** inicial.", "El perfil corresponde a A y muestra su nombre inicial."),
    ("Escribir **Prueba T10-02 - nombre guardado** en **Full Name**.", "**Full Name** contiene **Prueba T10-02 - nombre guardado**."),
    ("Hacer clic en **Ok**.", "El guardado termina y **Settings** se cierra sin aviso de rechazo."),
    ("Recargar la página y abrir **Settings** / **Profile**.", "**Full Name** muestra exactamente **Prueba T10-02 - nombre guardado**; correo y zona horaria conservan sus valores iniciales."),
    ("Cerrar **Settings** con **Cancel** y hacer clic en **Logout**.", PUBLICA),
    ("Iniciar sesión nuevamente con las credenciales vigentes de A.", "**Login** permite acceder a la misma cuenta A."),
    ("Abrir **Settings** / **Profile**.", "Se conserva **Prueba T10-02 - nombre guardado** después de la nueva sesión."),
    ("Restituir el nombre inicial, hacer clic en **Ok**, recargar y volver a consultar **Profile**.", "**Full Name** vuelve al valor inicial; no quedan cambios de nombre de esta prueba."),
],
"TL-68": [
    ("Abrir **Settings** / **Profile** sin modificar nombre, correo ni configuración temporal.", "Se muestran **Old Password** y **New Password**; no hay campo de confirmación en **Settings**."),
    ("Dejar **Old Password** vacío e introducir personalmente una contraseña alternativa en **New Password**.", "**Old Password** está vacío y **New Password** contiene la contraseña alternativa."),
    ("Hacer clic en **Ok** una sola vez.", "Aparece un aviso con el texto exacto **Invalid Password**; el intento no debe sustituir la credencial vigente."),
    ("Cerrar el aviso con **OK** y descartar los campos editados con **Cancel** en **Settings**.", "Se cierra el aviso y luego **Settings**; la entrada alternativa queda descartada."),
    ("Hacer clic en **Logout**.", PUBLICA),
    ("Iniciar sesión con el correo y la contraseña vigentes antes del intento.", "**Login** permite acceder a A con la credencial inicial; no se necesita la contraseña alternativa rechazada."),
    ("Consultar **Profile** y conservar evidencia sin secretos.", "Se mantienen la identidad y los valores iniciales de A; la evidencia del aviso no revela contraseñas."),
],
"TL-69": [
    ("Abrir Todo.ly, desplegar **Login** y seleccionar **Reset your Password**.", "Se presenta **Enter your email address to reset your password** y el control **Send**."),
    ("Introducir el correo de A en el campo de recuperación.", "El campo contiene el correo de A."),
    ("Hacer clic en **Send** una vez.", "Aparece **Info. An email has been sent with a link where you can change your password.**"),
    ("Consultar personalmente el buzón controlado y abrir el mensaje **Forgot Password** correspondiente a esa solicitud; no copiar el token a la evidencia.", "Llega un mensaje dirigido a A con instrucciones y enlace de recuperación. No se exige un plazo de recepción no documentado."),
    ("Abrir el enlace de recuperación tal como llega en el correo, sin cambiar su esquema ni copiar el token a la evidencia.", "Se muestra **Please Enter a New Password** con **Enter a New Password**, **Verify New Password** y **Done**. Si el enlace recibido no carga el formulario, se registra una falla de este caso; HTTPS se evalúa separadamente en T10-10."),
    ("Introducir personalmente la misma nueva contraseña en **Enter a New Password** y **Verify New Password**.", "Ambos campos contienen la nueva contraseña."),
    ("Hacer clic en **Done** y actualizar el registro privado.", "Se acepta el envío y A queda accesible; el acceso con la nueva contraseña se confirma en el paso 11. No se exige un aviso literal posterior a **Done** porque no se observó su texto."),
    ("Cerrar sesión con **Logout**.", PUBLICA),
    ("Realizar un intento de **Login** con el correo de A y la contraseña reemplazada.", "No se concede acceso; se muestra **Wrong email or password** dentro del aviso de rechazo observado."),
    ("Iniciar sesión con el correo de A y la nueva contraseña.", "Acceso a A: " + AUTENTICADA),
    ("Abrir **Settings** / **Profile**.", "**Full Name** y **Email** conservan el nombre inicial y el correo de A registrados privadamente antes de la recuperación."),
],
"TL-70": [
    ("Abrir Todo.ly, desplegar **Login** y seleccionar **Reset your Password**.", "Se presenta el campo de correo para recuperación y el control **Send**."),
    ("Introducir **prueba-t10-no-registrada-20261117@example.com** en el campo de recuperación.", "El campo contiene **prueba-t10-no-registrada-20261117@example.com**."),
    ("Hacer clic en **Send** una vez.", "Aparece **Error. Account with this Email address doesn't exist.**; el formulario de recuperación permanece disponible."),
    ("Conservar evidencia del aviso sin credenciales y cerrar el panel de **Login**.", "No se inicia una sesión ni se modifica ninguna cuenta A o B."),
],
"TL-71": [
    ("Abrir personalmente el mensaje **Forgot Password** de la solicitud de A e inspeccionar el esquema de cada enlace de recuperación y su destino visible, sin publicar el token.", "Los enlaces de recuperación utilizan HTTPS según el criterio del equipo. Un enlace HTTP constituye una discrepancia a registrar en la ejecución."),
    ("Abrir en el navegador el enlace directo recibido, sin introducir contraseñas.", "Se abre la página de recuperación."),
    ("Consultar la indicación de conexión de Chrome junto a la dirección.", "El recorrido de recuperación utiliza una conexión segura; Chrome no presenta **Not Secure** para la página de recuperación."),
    ("Registrar el esquema y el indicador observados en evidencia que oculte el token y cerrar esa pestaña.", "La evidencia permite evaluar el criterio sin divulgar el token; no se ha enviado una nueva contraseña ni cambiado la cuenta."),
],
}


def _parrafos(summary_html):
    return [m.group(0) for m in re.finditer(r"<p>.*?</p>", summary_html, re.S)]


def casos(respaldo):
    live = {c["full_tc_external_id"]: c for c in json.load(open(respaldo, encoding="utf-8"))["casos"]}
    base = {c["id"]: c for c in prop_t10.CASOS}
    out = []
    for k in SOLO_TITULO:
        c = live[k]
        m = re.match(r"^(T(?:09|10|11)-\d\d)\. (.*)$", c["name"])
        assert m, (k, c["name"])
        out.append({"id": k, "ticket": m.group(1)[:3], "clasif": "EDITAR", "solo_nombre": True,
                    "name": f"{m.group(1)} - {m.group(2)}",
                    "raw": {"summary": c["summary"], "preconditions": c["preconditions"],
                            "steps": sorted(c["steps"], key=lambda s: int(s["step_number"]))},
                    "problemas": ["TF"], "cambios": [], "dudas": []})
    for k in ["TL-66", "TL-67", "TL-68", "TL-69", "TL-70", "TL-71"]:
        b, c = base[k], live[k]
        ps = _parrafos(c["summary"])
        nuevos = []
        for par in ps:
            txt = _html.unescape(re.sub(r"<[^>]+>", "", par))
            if txt.startswith("Descripción:"):
                nuevos.append(f"<p><strong>Descripción:</strong> {modelo.md(b['desc'])}</p>")
            elif k == "TL-66" and txt.startswith("Cancelar la edición del nombre"):
                nuevos.append("<p>Requerimiento: PEB-74 / T10. " + modelo.md(txt) + "</p>")
            else:
                nuevos.append(par)
        assert any("Validar que" in x for x in nuevos), k
        steps = PASOS[k] or b["steps"]
        cambios = ["Se conservan Preconditions, «Importancia», requerimiento y «Postcondiciones» tal como están"]
        if k == "TL-66":
            cambios.append("La autora quitó el rótulo del requerimiento: se antepone «Requerimiento: PEB-74 / T10.» a su texto (misma decisión que en T12/T13)")
        out.append({"id": k, "ticket": "T10", "clasif": "EDITAR", "solo_nombre": False, "name": b["name"],
                    "raw": {"summary": "".join(nuevos), "preconditions": c["preconditions"],
                            "steps": [{"step_number": i, "actions": modelo.p(a), "expected_results": modelo.p(e), "execution_type": 1}
                                      for i, (a, e) in enumerate(steps, 1)]},
                    "problemas": [x for x in b["problemas"]] + (["RQ"] if k == "TL-66" else []) + ["TF"],
                    "cambios": cambios, "dudas": []})
    return out
