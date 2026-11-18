"""Propuestas T07 (PEB-71): TL-50 a TL-55."""
from modelo import *

BASE = ["PF", "PV", "PS", "VQ", "RQ", "NB", "DA"]
REQ = "PEB-71 / T07 — Estados de tareas e indicadores."
HOME_VACIO = "Proyecto predeterminado **Home** existente, sin tareas pendientes ni completadas."
STUDY_VACIO = "Proyecto predeterminado **Study** existente, sin tareas pendientes ni completadas."
DA_CAMBIO = "Precondición «Home sin pendientes ni completadas» añadida porque el caso espera cantidades exactas (guía §10)"


def home(res="Se muestra el proyecto **Home**."):
    return ("Hacer clic en **Home**, dentro de **Projects**, en el panel izquierdo.", res)


def study(res="Se muestra el proyecto **Study**."):
    return ("Hacer clic en **Study**, dentro de **Projects**, en el panel izquierdo.", res)


def delete_menu(nombre, res):
    return (f"Pasar el mouse sobre **{nombre}**, abrir su menú de opciones y seleccionar **Delete**.", res)


CASOS = [
dict(id="TL-50", ticket="T07", clasif="EDITAR",
  name="T07-01 - Completar una tarea la pasa a Done Items sin afectar a otra pendiente",
  desc="Validar que marcar el checkbox de una tarea independiente la pasa a completadas, actualiza los indicadores de Home y Done Items y no modifica otra tarea pendiente.",
  req=REQ, pre=pre_t06(HOME_VACIO),
  steps=[
    home(),
    crear_todo("Prueba T07-01 - completar"),
    crear_todo("Prueba T07-01 - control", "Aparecen dos tareas pendientes. **Home** indica **2** pendientes y **Done Items** muestra **0**."),
    ("Marcar el checkbox situado a la izquierda de **Prueba T07-01 - completar**.", "La seleccionada sale de pendientes y la de control permanece pendiente. **Home** indica **1** pendiente y **Done Items** muestra **1**."),
    ("Hacer clic en **See all**, si las completadas están ocultas.", "**Prueba T07-01 - completar** aparece con su checkbox marcado y su texto tachado. La de control continúa en pendientes."),
    ("Presionar **F5** y abrir nuevamente **Home**.", "Los indicadores mantienen los valores **1** pendiente y **1** en **Done Items**."),
    ("Desplegar las completadas con **See all**.", "Se conserva una tarea pendiente y una completada."),
    ("Desmarcar el checkbox de **Prueba T07-01 - completar**.", "La tarea vuelve a pendientes."),
    delete_menu("Prueba T07-01 - completar", "La tarea desaparece de la lista activa."),
    delete_menu("Prueba T07-01 - control", "Las dos tareas han desaparecido de la lista activa. **Home** queda sin pendientes y **Done Items** muestra **0**."),
  ],
  post=["Las dos tareas están retiradas de **Home** y permanecen identificadas en **Recycle Bin**.", "Se conserva evidencia del cambio de estado y de los indicadores."],
  problemas=BASE + ["T", "MA"], cambios=[DA_CAMBIO],
),
dict(id="TL-51", ticket="T07", clasif="EDITAR",
  name="T07-02 - Reactivar una tarea completada la devuelve a pendientes",
  desc="Validar que desmarcar una tarea en Done Items la devuelve a pendientes con su nombre original, sin duplicarla, y que el cambio se conserva al recargar.",
  req=REQ, pre=pre_t06(HOME_VACIO),
  steps=[
    home(),
    crear_todo("Prueba T07-02 - reactivar"),
    ("Marcar el checkbox de **Prueba T07-02 - reactivar**.", "La tarea queda completada."),
    ("Presionar **F5** y abrir nuevamente **Home**.", "**Home** no indica pendientes y **Done Items** muestra **1**."),
    ("Hacer clic en **See all**.", "La tarea aparece en completadas con su checkbox marcado."),
    ("Desmarcar el checkbox de **Prueba T07-02 - reactivar**.", "La tarea vuelve a pendientes con su nombre original y desaparece de completadas. **Home** indica **1** pendiente y **Done Items** muestra **0**."),
    ("Revisar las secciones de pendientes y completadas.", "Existe una sola tarea con ese nombre; no hay una copia en cada sección."),
    ("Presionar **F5** y abrir nuevamente **Home**.", "La tarea continúa pendiente. **Home** indica **1** pendiente y **Done Items** muestra **0**."),
    delete_menu("Prueba T07-02 - reactivar", "La tarea desaparece de la lista activa y **Home** queda sin pendientes."),
  ],
  post=["La tarea está retirada de **Home** y permanece en **Recycle Bin**.", "Se conserva evidencia de la reactivación y de la ausencia de duplicados."],
  problemas=BASE + ["MA"], cambios=[DA_CAMBIO, "Título igual al ejemplo de la rúbrica (solo se añade el prefijo)"],
),
dict(id="TL-52", ticket="T07", clasif="EDITAR",
  name="T07-03 - See all, Done Items y el contador muestran las completadas; Hide las oculta",
  desc="Validar que See all, el texto Done Items y el número del contador despliegan la sección de completadas, vacía o con contenido, y que Hide la oculta sin cambiar ninguna tarea.",
  req=REQ, pre=pre_t06(HOME_VACIO),
  steps=[
    home(),
    ("Hacer clic en **See all** con **0** en **Done Items**.", "La sección se despliega sin tareas completadas. El enlace cambia a **Hide** y el contador permanece en **0**."),
    ("Hacer clic en **Hide**.", "La sección se oculta y vuelve a aparecer **See all**. No se crea ni modifica ninguna tarea."),
    crear_todo("Prueba T07-03 - pendiente"),
    crear_todo("Prueba T07-03 - completada"),
    ("Marcar únicamente el checkbox de **Prueba T07-03 - completada**.", "La tarea sale de pendientes."),
    ("Presionar **F5** y abrir nuevamente **Home**.", "Queda una pendiente y una completada. **Home** indica **1** pendiente y **Done Items** muestra **1**."),
    ("Hacer clic en **See all**.", "La completada aparece debajo de las pendientes. Ambas conservan sus estados."),
    ("Hacer clic en **Hide**.", "La completada deja de mostrarse y la pendiente sigue visible. El contador continúa en **1**."),
    ("Hacer clic en el texto **Done Items**.", "Se despliega nuevamente la misma tarea completada."),
    ("Hacer clic en **Hide**.", "La sección de completadas se oculta."),
    ("Hacer clic en el número **1** del contador de completadas.", "Se despliega la misma sección, con una sola tarea completada y sin duplicados."),
    ("Desmarcar el checkbox de **Prueba T07-03 - completada**.", "La tarea vuelve a pendientes."),
    delete_menu("Prueba T07-03 - pendiente", "La tarea desaparece de la lista activa."),
    delete_menu("Prueba T07-03 - completada", "**Home** queda sin pendientes y **Done Items** muestra **0**."),
  ],
  post=["Las dos tareas están retiradas de **Home** y permanecen en **Recycle Bin**.", "Queda evidencia de las tres vías de consulta y del comportamiento de la sección vacía."],
  problemas=BASE + ["T", "MA"], cambios=[DA_CAMBIO],
),
dict(id="TL-53", ticket="T07", clasif="EDITAR",
  name="T07-04 - Completar una tarea en Home no cambia estados ni contadores de Study",
  desc="Validar que completar una tarea en Home no modifica los estados ni las cantidades del proyecto Study, y que cada proyecto conserva sus indicadores al recargar.",
  req=REQ, pre=pre_t06(HOME_VACIO, STUDY_VACIO),
  steps=[
    home(),
    crear_todo("Prueba T07-04 - Home", "**Home** contiene una tarea pendiente y muestra **0** en **Done Items**."),
    study(),
    crear_todo("Prueba T07-04 - Study", "**Study** contiene una tarea pendiente y muestra **0** en **Done Items**.", lugar="Study"),
    home(),
    ("Marcar el checkbox de **Prueba T07-04 - Home**.", "**Home** queda sin pendientes y muestra **1** en **Done Items**. **Study** continúa indicando una pendiente en la barra lateral."),
    study("Su tarea continúa pendiente. **Done Items** muestra **0** y no aparece la tarea de Home."),
    home(),
    ("Desplegar las completadas con **See all**.", "Aparece únicamente la completada de Home. Su contador muestra **1**."),
    ("Presionar **F5** y abrir nuevamente **Home**.", "**Home** conserva una completada: no indica pendientes y **Done Items** muestra **1**."),
    study("**Study** conserva una pendiente y **Done Items** muestra **0**. Los indicadores corresponden a cada proyecto."),
    ("En **Home**, desmarcar el checkbox de **Prueba T07-04 - Home**.", "La tarea vuelve a pendientes en **Home**."),
    delete_menu("Prueba T07-04 - Home", "La tarea desaparece de **Home**."),
    study(),
    delete_menu("Prueba T07-04 - Study", "Ambos proyectos quedan sin pendientes y con **0** en **Done Items**."),
  ],
  post=["Las dos tareas están retiradas de sus proyectos y permanecen en **Recycle Bin**.", "Los demás proyectos conservan su información."],
  problemas=BASE + ["T", "MA"], cambios=["Precondiciones «Home y Study sin pendientes ni completadas» añadidas porque el caso espera cantidades exactas (guía §10)"],
),
dict(id="TL-54", ticket="T07", clasif="EDITAR",
  name="T07-09 - Estados e indicadores se conservan tras F5 y tras cerrar e iniciar sesión",
  desc="Validar que una tarea pendiente y otra completada conservan su estado, sus nombres y los indicadores de Home después de recargar y de cerrar e iniciar sesión.",
  req=REQ, pre=pre_t06(HOME_VACIO),
  steps=[
    home(),
    crear_todo("Prueba T07-09 - pendiente"),
    crear_todo("Prueba T07-09 - completada", "Aparecen dos tareas pendientes."),
    ("Marcar únicamente el checkbox de **Prueba T07-09 - completada**.", "**Home** indica **1** pendiente y **Done Items** muestra **1**."),
    ("Presionar **F5** y abrir nuevamente **Home**.", "Los indicadores mantienen **1** pendiente y **1** en **Done Items**."),
    ("Desplegar las completadas con **See all**.", "La primera continúa pendiente y la segunda completada; se conservan sus nombres."),
    ("Hacer clic en **Logout**, en la barra superior.", "Finaliza la sesión y se presenta la página de acceso."),
    ("Hacer clic en **Login**, ingresar las credenciales de la misma cuenta y confirmar el acceso.", "Se inicia sesión nuevamente en esa cuenta."),
    home("Aparece **Prueba T07-09 - pendiente** en pendientes. **Home** indica **1** pendiente y **Done Items** muestra **1**."),
    ("Desplegar las completadas con **See all**.", "Aparece **Prueba T07-09 - completada** con su checkbox marcado. No hay tareas perdidas ni duplicadas."),
    ("Desmarcar el checkbox de **Prueba T07-09 - completada**.", "La tarea vuelve a pendientes."),
    delete_menu("Prueba T07-09 - pendiente", "La tarea desaparece de la lista activa."),
    delete_menu("Prueba T07-09 - completada", "**Home** queda sin pendientes y con **0** en **Done Items**."),
  ],
  post=["La sesión queda iniciada en la misma cuenta.", "Las dos tareas están retiradas de **Home** y permanecen en **Recycle Bin**.", "Se conserva evidencia de los resultados entre sesiones."],
  problemas=BASE + ["T", "MA"], cambios=[DA_CAMBIO],
),
dict(id="TL-55", ticket="T07", clasif="EDITAR",
  name="T07-10 - Dos ciclos de completar y reactivar dejan una sola tarea pendiente",
  desc="Validar que completar y reactivar dos veces la misma tarea mantiene coherentes los indicadores en cada cambio y termina con una sola tarea pendiente con su nombre original.",
  req=REQ, pre=pre_t06(HOME_VACIO),
  steps=[
    home(),
    crear_todo("Prueba T07-10 - ciclo de estados", "Existe una tarea pendiente. **Home** indica **1** pendiente y **Done Items** muestra **0**."),
    ("Marcar el checkbox de **Prueba T07-10 - ciclo de estados**.", "La tarea queda completada. **Home** no indica pendientes y **Done Items** muestra **1**."),
    ("Desplegar las completadas con **See all**, si están ocultas.", "La tarea aparece en la sección de completadas."),
    ("Desmarcar su checkbox en completadas.", "La tarea vuelve a pendientes. **Home** indica **1** pendiente y **Done Items** muestra **0**."),
    ("Marcar nuevamente el checkbox de la misma tarea.", "La tarea vuelve a completadas. **Home** queda sin pendientes y **Done Items** muestra **1**."),
    ("Desplegar las completadas con **See all**, si están ocultas.", "Aparece una sola tarea en completadas, sin acumular una segunda completada."),
    ("Desmarcar nuevamente su checkbox.", "La tarea vuelve a pendientes. **Home** indica **1** pendiente y **Done Items** muestra **0**."),
    ("Revisar las secciones de pendientes y completadas.", "Existe una sola tarea, pendiente y con el nombre original."),
    ("Presionar **F5** y abrir nuevamente **Home**.", "Los indicadores mantienen una pendiente y cero completadas."),
    delete_menu("Prueba T07-10 - ciclo de estados", "La tarea desaparece de la lista activa y **Home** queda sin pendientes."),
  ],
  post=["La tarea está retirada de **Home** y permanece en **Recycle Bin**.", "Quedan registrados los indicadores de cada cambio y cualquier diferencia observada."],
  problemas=BASE + ["T"], cambios=[DA_CAMBIO],
),
]
