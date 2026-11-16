# Plantilla del comentario de Jira (T09, T10, T11)

Sigue la estructura real del comentario de T06 (PEB-70). Si T06 difiere de esta plantilla, manda T06. Después de publicar, revisa que las tablas se vean bien en Jira.

Las fichas completas de los casos viven en TestLink. En Jira va la lista resumida con los IDs y enlaces de TestLink.

---

## T0X — Análisis, diseño e implementación: <área>

### 1. Análisis del área
Operaciones, controles, estados y contexto observados. Indicar con qué cuentas y en qué entorno se exploró.

### 2. Riesgos que orientan el diseño
| Riesgo | Consecuencia para el usuario | Probabilidad | Impacto | Nivel |
|---|---|---|---|---|
| | | | | |

### 3. Reglas, restricciones y dudas
| Regla o duda | Clasificación | Fundamento o evidencia |
|---|---|---|
| | Regla documentada / Comportamiento observado / Criterio del equipo / Duda pendiente | |

### 4. Tipos de prueba y escenarios seleccionados
| Tipo de prueba | Por qué aplica | Procedimiento | Criterio observable |
|---|---|---|---|
| Funcional | | | |

Escenarios positivos, negativos y alternativos elegidos, y qué cobertura distinta aporta cada uno.

### 5. Técnicas de caja negra aplicadas
Incluir solo las que las reglas justifican. Cada artefacto debe señalar los casos que genera.

#### 5.1 Particiones de equivalencia
| Variable o condición | Clase | Válida / Inválida | Representante | Caso |
|---|---|---|---|---|

#### 5.2 Valores límite (solo sobre fronteras confirmadas)
| Frontera | Fuente de la frontera | Valores (2 o 3 valores, según el docente) | Caso |
|---|---|---|---|

#### 5.3 Tabla de decisión
| Condiciones | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| C1: … | V | V | F | F |
| C2: … | V | F | V | F |
| **Acciones** | | | | |
| A1: … | X | | | |
| A2: … | | X | X | X |
| **Caso** | T0X-01 | T0X-02 | … | … |

Indicar si se redujo la tabla y con qué criterio.

#### 5.4 Transición de estados
Estados: … · Eventos: …

| Estado actual | Evento | Estado siguiente | ¿Válida? | Caso |
|---|---|---|---|---|

#### 5.5 Casos de uso
- Flujo básico: …
- Flujos alternos: …
- Casos derivados: …

### 6. Lista resumida de casos
| Caso | Objetivo o riesgo cubierto | Fundamento de la técnica aplicada | Importancia |
|---|---|---|---|

### 7. Implementación en TestLink
| Caso | ID en TestLink | Enlace |
|---|---|---|

Evidencia: capturas adjuntas del árbol de la suite y de un caso abierto. Exportación XML: `testlink-xml/T0X.xml`.

### 8. Cobertura pendiente y dudas abiertas
Qué queda sin cubrir, por qué y qué consecuencia tiene.

### 9. Estado
Diseñados y registrados en TestLink; pendiente de revisión por otro integrante.
