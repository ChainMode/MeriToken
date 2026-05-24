# 00 Guía de lectura

> Este documento es el punto de entrada del blueprint. Explica el eje de redacción del blueprint de este repositorio, esboza el perfil de la lectora o lector y las rutas de lectura recomendadas, y la o lo encamina hacia los documentos de la línea principal (01–06).

![Banner de título de ifay](../../zh-CN/blueprint/illustration/ifay-title-banner.png)

## Antecedentes

El blueprint de este repositorio se organiza en torno a un análisis en profundidad de **MeriToken**. En la nueva sociedad, MeriToken asume dos roles fundacionales —«componente de contrato» y «conector de relaciones sociales»—, por lo que constituye el eje de contenido de cada documento de este blueprint.

Temas como el sistema ifay, GMC, Fay, agent y phase se sitúan como trasfondo de apoyo del que un análisis de MeriToken no puede prescindir. Solo se introducen cuando el desarrollo del análisis de MeriToken los hace estrictamente necesarios, y a continuación se redirige a la lectora o al lector mediante enlaces externos hacia las páginas oficiales correspondientes en ifay.ai. Este repositorio no desarrolla en extensión esos temas aguas arriba o periféricos.

Las lectoras y lectores a quienes se dirige este blueprint son:

- Investigadoras, investigadores, autoras, autores y colaboradores que deseen comprender de manera sistemática los principios técnicos, el sentido social y los escenarios de aplicación de MeriToken;
- Profesionales con cierta familiaridad previa con los conceptos básicos del sistema ifay que ahora deseen examinar con más detalle el papel concreto de MeriToken en la nueva sociedad, en particular cómo MeriToken interactúa con las instituciones que lo rodean;
- Traductoras, traductores y mantenedores que necesiten redactar o traducir este blueprint sobre MeriToken para versiones lingüísticas adicionales.

## Contenido principal

### Eje del blueprint: MeriToken

El cuerpo principal del blueprint (01–06) despliega el análisis en profundidad de MeriToken en el siguiente orden:

- **Panorámica (01)**: cómo MeriToken pertenece a GMC; las dos razones por las que se trata como tema autónomo: como componente de contrato de la nueva sociedad y como conector de relaciones sociales de la nueva sociedad.
- **Principios técnicos (02)**: cifrado, almacenamiento, recuperación, garantías de privacidad y garantías de propiedad y de derecho de uso.
- **Sentido social (03)**: relaciones sociales, lógica política, estructura económica, mapeo del crecimiento personal y el sentido de MeriToken como vehículo del mapeo entre «contribución personal y peso del discurso social».
- **Modos de referencia y aplicaciones (04)**: los modos de referencia y los escenarios de aplicación típicos de las dos clases de referenciadores: los sujetos personales y los sujetos Fay.
- **Relación con credential (05)**: las definiciones de rol, la frontera y la correspondencia entre credential y MeriToken.
- **Temas avanzados (06)**: casos de extensión como el uso de alta densidad entre múltiples sujetos y los escenarios rodantes.

### Rutas de lectura recomendadas

El orden de lectura recomendado es secuencial por número: `01 → 02 → 03 → 04 → 05 → 06`. Si el tiempo es limitado o el objetivo es más específico, las siguientes rutas alternativas pueden resultar útiles:

- **Para lectoras y lectores centrados en la implementación técnica**: `01 → 02 → 05 → 06` — establecer primero el posicionamiento básico de MeriToken y profundizar después en el ciclo cerrado cifrado/almacenamiento/recuperación y en la frontera con credential.
- **Para lectoras y lectores centrados en el sentido social e institucional**: `01 → 03 → 04 → 06` — comprender primero la posición global de MeriToken y desplegar después el sentido social, los modos de referencia y las aplicaciones.
- **Para quienes necesiten explicar MeriToken a otras personas**: `01 → 04 → 03` — dejar claro primero «qué es y quién lo utiliza» y completar después «por qué se diseña de este modo».

`07-related-projects.md` es el documento de interfaz entre este blueprint y los temas aguas arriba. Es una referencia complementaria que se consulta según necesidad y no forma parte de la ruta de lectura principal.

### Relación con los temas aguas arriba y los temas periféricos

Los temas aguas arriba y periféricos como ifay, GMC, Fay, agent y phase se concentran en [07-related-projects.md](./07-related-projects.md) en forma de «notas de posicionamiento mínimas necesarias más una lista de enlaces externos», que encaminan a la lectora o al lector hacia las páginas oficiales correspondientes en ifay.ai. El propio blueprint no desarrolla esos temas en extensión, con el fin de preservar la densidad de redacción del eje MeriToken.

Si no ha tenido contacto previo con estos conceptos aguas arriba, recomendamos visitar primero los enlaces externos de [07-related-projects.md](./07-related-projects.md) para construir un trasfondo rápido y volver después a la línea principal en 01.

## Relación con otros temas

| N.º | Tema | Relación con esta guía |
|------|------|---------------|
| 01 | Panorámica de MeriToken | Punto de partida de la línea principal y documento que sigue a esta guía |
| 02 | Principios técnicos de MeriToken | Segundo documento de la línea principal |
| 03 | Sentido social de MeriToken | Tercer documento de la línea principal |
| 04 | Modos de referencia y aplicaciones de MeriToken | Cuarto documento de la línea principal |
| 05 | Relación entre credential y MeriToken | Quinto documento de la línea principal |
| 06 | Temas avanzados de MeriToken | Sexto documento de la línea principal |
| 07 | Relación con el sistema ifay | Interfaz y lista de enlaces externos para los temas aguas arriba y periféricos |

## Notas de términos

`Reserved_Term`s que aparecen en este documento:

- **ifay**: Nombre del sistema del proyecto; véase [glossary.md](./glossary.md).
- **GMC**: Global Merit Chain, el sistema superior al que pertenece MeriToken; véase [glossary.md](./glossary.md).
- **Fay**: Sujeto no personal que hace referencia a MeriToken; véase [glossary.md](./glossary.md).
- **agent**: Entidad agent en los marcos LLM tradicionales; véase [glossary.md](./glossary.md).
- **phase**: Número de etapa evolutiva en el blueprint; véase [glossary.md](./glossary.md).
- **credential**: credential (credencial de identidad y de propiedad) para un sujeto personal o un sujeto Fay; véase [glossary.md](./glossary.md).

La forma principal en chino de MeriToken se utiliza como denominación convencional de MeriToken únicamente en el cuerpo del texto de los blueprints `zh-CN` y `zh-TW`. Véase la sección `Localized_Term` de [glossary.md](./glossary.md) para conocer las reglas de localización de MeriToken en cada lengua.
