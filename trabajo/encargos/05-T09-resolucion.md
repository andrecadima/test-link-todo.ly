# Integración de diseño 05 — T09

Codex comprobó que se conservaron los 13 IDs, importancia, razón y requerimiento. Las descripciones comienzan con Validar que y los nombres completos no superan 90 caracteres.

Ajustes de integración sin cambiar cobertura: T09-01 prepara cada campo vacío por separado y conserva Timezone; T09-03 separa recorrer/anotar y localizar cada zona; las comparaciones Full Name/Email se separan por campo y sus referencias privadas quedan como estados nominales; T09-09 evita un mensaje conjugado como precondición (el contraste sigue trazado a T10). T09-02 explicita el estado final real de la sesión A en Profile, sin añadir Logout ni otra operación.

Resultado: 13 casos listos, **171 pasos**; T09-08 sigue excluido. Canonical JSON, fichas, borrador y XML se sincronizaron. Summary empieza con descripción Validar que, después requerimiento y postcondiciones; Importance se conserva en su campo nativo. Controles/datos en negrita se convierten en strong. El XML no contiene IDs ni suites.

No se usó el navegador; el usuario realiza T10 y pidió no usarlo hasta avisar. No hay registro ni publicación T09 todavía. Es necesaria una revisión independiente nueva del conjunto definitivo.
