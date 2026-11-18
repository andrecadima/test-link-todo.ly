# Resguardo de la revisión paralela

Seis archivos ajenos contienen una credencial preexistente y permanecen intactos e ignorados. El manifiesto conserva sus copias cifradas con Fernet (autenticación e integridad); la clave local `.secrets/resguardo-revision-git.key` no se sube. Se detectaron también dos respaldos posteriores con la misma credencial heredada; se conservan cifrados y quedan fuera del árbol rastreado. Los demás archivos seguros se incluyen sin modificaciones.

Con `cryptography` disponible (en esta máquina instalado en el directorio ignorado `tmp/python-crypto`), restauración en un directorio privado nuevo:

```sh
python3 scripts/resguardar_revision.py --restore tmp/revision-restaurada-nueva
```

El script no sobrescribe archivos. Se comprobó una restauración byte por byte contra los originales. Para recuperar el respaldo en otra máquina hace falta la clave privada, que debe transferir el usuario de forma segura.
