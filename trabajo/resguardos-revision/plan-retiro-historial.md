# Retirada preparada del historial

Se preparó la rama local `resguardo-sin-credenciales`, reconstruyendo únicamente los commits posteriores a bd0329e y omitiendo los dos respaldos de texto que contenían una credencial heredada. El árbol final es idéntico al de master actual; no se borraron ni modificaron los originales locales y sus copias cifradas siguen disponibles.

Pendiente autorización para actualizar master remoto con `--force-with-lease`. No se ha ejecutado ese push. La corrección no garantiza eliminación de cachés/referencias antiguas del proveedor; si la credencial heredada sigue vigente, su propietario debe cambiarla. Codex no la utilizó ni accede a esa cuenta.
