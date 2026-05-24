# 01 Panorámica de MeriToken

> Introducción: Este documento es el punto de partida de la línea principal del blueprint. Sitúa MeriToken dentro del sistema ifay y expone las dos razones por las que MeriToken se extrae de la discusión global sobre ifay como tema autónomo: como componente de contrato y como conector de relaciones sociales de la nueva sociedad. Los documentos 02 a 06 se construyen todos sobre el posicionamiento aquí establecido.

## Antecedentes

El «MeriToken» del que trata este blueprint no es un mero programa de fidelización de uso general ni una herramienta más de contabilización de contribuciones. Es una pieza de infraestructura básica dentro del entorno operativo de la «nueva sociedad» que ifay imagina. MeriToken asume al mismo tiempo roles fundacionales en dos direcciones distintas: en la capa institucional, participa en las promesas y en su cumplimiento entre individuos y organizaciones bajo la forma de un «componente de contrato»; en la capa relacional, articula contribuciones personales dispersas, registros de colaboración y evaluaciones sociales bajo la forma de un «conector de relaciones sociales».

Estas dos direcciones no son dos líneas de actividad paralelas. Son proyecciones del mismo activo sobre distintas capas de abstracción. Este blueprint eleva MeriToken a tema de la línea principal precisamente porque entre ambas proyecciones existe una tensión nada desdeñable: cuando se incrementa el rigor institucional, este no debe a su vez devorar la elasticidad de la capa relacional; cuando crece la riqueza de la capa relacional, esta no debe desestabilizar la verificabilidad de la capa contractual. Solo después de exponer con claridad la posición de MeriToken y las razones para tratarlo como tema autónomo, los documentos 02 a 06 podrán compartir un punto de partida común.

## Contenido principal

### Cómo MeriToken pertenece a GMC

MeriToken no es un protocolo de activos autónomo. Es una clase concreta de objeto contable bajo el sistema superior `GMC` (Global Merit Chain). `GMC` proporciona contabilidad encadenada global, verificabilidad entre sujetos y consistencia eventual. MeriToken se asienta sobre eso y porta la semántica concreta de «contribución — evaluación — referencia».

Esta subordinación tiene tres consecuencias directas:

- **Consistencia del sustrato de datos**: las transferencias de propiedad, los registros de referencia, las revocaciones y las actualizaciones de MeriToken siguen todos la semántica de cadena de `GMC`. No existe un libro mayor separado, lo que evita el coste de las conciliaciones entre libros.
- **Externalidad del ciclo de vida**: MeriToken no necesariamente abarca todo el ciclo de vida de un sujeto personal. Su visibilidad, su capacidad de ser referenciado y su acumulabilidad dentro de `GMC` pueden abrirse o recuperarse por etapas según las reglas del nivel superior, sin modificar la propia definición de MeriToken.
- **Externalización de la autoridad interpretativa**: el sentido concreto de MeriToken en la nueva sociedad evoluciona a medida que evoluciona el sistema superior. Este blueprint opta por dejar más temas aguas arriba —como el «marco general / la evolución de `phase`»— a la documentación oficial de ifay.ai (véase [07-related-projects.md](./07-related-projects.md)) en lugar de reformularlos en este repositorio.

La razón para exponer con tanta claridad la relación entre MeriToken y `GMC` es evitar que la lectora o el lector entienda MeriToken como una invención conceptual aislada. Es el aterrizaje del sistema superior en el nivel de «objeto contable concreto» y constituye también el punto de partida compartido para cualquier discusión técnica y social posterior.

### Las dos razones para tratar MeriToken como tema autónomo

Aunque desde el punto de vista de los datos MeriToken está subordinado a `GMC`, este repositorio opta por extraerlo de la discusión global sobre ifay como blueprint autónomo porque MeriToken asume simultáneamente dos clases de roles fundacionales en la nueva sociedad, cada una de ellas suficientemente sustancial como para merecer su propia línea de investigación. Plegar ambos roles en la discusión global de `GMC` desdibujaría sus respectivas fronteras; tratarlos por separado permite caracterizar con mayor precisión el sentido dual de MeriToken en la nueva sociedad.

#### Como componente de contrato de la nueva sociedad

La primera razón proviene de la capa institucional. En la nueva sociedad, MeriToken puede ser referenciado como un registro verificable de «qué he hecho, ante quién soy responsable y quién lo ha presenciado», y por ello asume de manera natural el papel de «componente de contrato»:

- **Un bit verificable de promesa y cumplimiento**: en la colaboración entre sujetos, el propio proceso por el que se genera un MeriToken —una contribución que es presenciada, evaluada y registrada en los libros— es una unidad mínima. Sirve como bit verificable de promesa y cumplimiento, en lugar de depender de una decisión subjetiva ulterior por parte de un tercero.
- **Sustituir el crédito de grano grueso por registros de grano fino**: el «suministro de confianza» que la sociedad tradicional vehicula a través de objetos de grano grueso —puntuaciones de crédito, reputación, relaciones personales— puede descomponerse en la nueva sociedad en una serie de entradas MeriToken de grano fino, trazables y verificables. La lógica institucional migra así desde la «reputación global» hacia los «registros específicos».
- **Frontera con `credential`**: MeriToken es un registro verificable de «lo que se ha hecho», no un credential de identidad y de propiedad de «quién soy y qué poseo». Esto último corresponde a `credential`. La frontera y la correspondencia entre ambos se desarrollan por separado en [05-meritoken-credential.md](./05-meritoken-credential.md) y no se repiten aquí.

La implicación clave de ver MeriToken como un componente de contrato es la siguiente: las reglas institucionales dejan de depender de una máquina centralizada de puntuación crediticia. Las tres cosas —«formación del contrato, cumplimiento, incumplimiento trazable»— se anclan cada una en registros MeriToken concretos. Un contrato deja de ser una promesa textual; pasa a ser un objeto estructurado, referenciable y auditable.

#### Como conector de relaciones sociales de la nueva sociedad

La segunda razón proviene de la capa relacional. La misma entrada MeriToken, además de asumir el rol de componente de contrato, es también un nodo de relaciones sociales que conecta entre sí a sujetos dispersos:

- **Aristas mínimas del grafo de relaciones**: cada registro MeriToken contiene la relación multilateral «contribuyente — evaluador — destinatario del servicio». Estas relaciones ternarias constituyen de manera natural el grafo de relaciones de la nueva sociedad. El grafo en su conjunto no necesita ser mantenido por ningún nodo central; se ensambla a partir de las relaciones locales incrustadas en cada entrada MeriToken.
- **Conexión entre tipos de sujeto**: el conector es indiferente a la forma del sujeto. Sujetos personales entre sí, sujetos personales con sujetos `Fay` y sujetos `Fay` entre sí pueden formar todos cadenas de colaboración estables a través de las relaciones de referencia de MeriToken. Los detalles sobre cómo los sujetos `Fay` hacen referencia a MeriToken se elaboran en [04-meritoken-usage.md](./04-meritoken-usage.md).
- **Una vía de migración del desconocido al conocido**: MeriToken no es solo un registro de «relaciones que ya se han formado»; es también un punto de entrada para «relaciones que aún no se han formado». Quienes se desconocen pueden establecer un nivel inicial de confianza haciendo referencia mutuamente a las entradas MeriToken existentes de la otra parte y depositar después el resultado de la colaboración presente en nuevas entradas MeriToken generadas. Las relaciones sociales en la nueva sociedad obtienen así una vía estructurada que va del desconocido al conocido.

La implicación clave de ver MeriToken como un conector de relaciones sociales es la siguiente: las relaciones sociales dejan de depender de las recomendaciones algorítmicas y de las valoraciones de caja negra de las plataformas. Vuelven a un mecanismo de generación localizado, enraizado en «colaboración concreta, testimonio concreto y referencia concreta».

> ⏳ **Ilustración pendiente** (slot: `meritoken-overview-contract`)
> Descripción: Un diagrama conceptual que presenta simultáneamente a MeriToken asumiendo los dos roles fundacionales de «componente de contrato» y «conector de relaciones sociales» en la nueva sociedad, e indica que está subordinado al sistema superior `GMC`.
> Archivo previsto: `illustration/meritoken-overview-contract.png`

## Relación con otros temas

Este documento es el punto de partida de la línea principal 01–06. Su conexión con los temas posteriores se resume a continuación:

| Tema posterior | Conexión con este documento |
|----------|-------------|
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Aterriza los dos roles, «componente de contrato» y «conector de relaciones sociales», sobre los principios técnicos de cifrado, almacenamiento, recuperación, privacidad, propiedad y derechos de uso. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Continúa desplegando los dos roles en cuatro hilos de sentido social: relaciones sociales, lógica política, estructura económica y mapeo del crecimiento personal. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Concretiza los dos roles en los modos de referencia y los escenarios de aplicación de las dos clases de referenciadores: los «sujetos personales» y los «sujetos `Fay`». |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Define, bajo la semántica de «componente de contrato», la frontera y la correspondencia entre MeriToken y `credential`. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Desarrolla estudios avanzados de los dos roles en escenarios de alta densidad como la colaboración entre múltiples sujetos y los escenarios rodantes. |
| [07-related-projects.md](./07-related-projects.md) | Aporta las notas de posicionamiento mínimas y los enlaces externos a la documentación oficial para los temas aguas arriba y periféricos como `GMC`, ifay, `Fay`, `agent`, `phase` y el marco general. |

Si aún no ha leído [00-readers-guide.md](./00-readers-guide.md), recomendamos volver primero allí para establecer la visión de conjunto y regresar después aquí para continuar con la línea principal.

## Notas de términos

`Reserved_Term`s que aparecen en este documento:

- **GMC**: Global Merit Chain, el sistema superior al que pertenece MeriToken; véase [glossary.md](./glossary.md).
- **Fay**: Sujeto no personal que hace referencia a MeriToken; véase [glossary.md](./glossary.md).
- **credential**: credential (credencial de identidad y de propiedad) para un sujeto personal o un sujeto `Fay`; véase [glossary.md](./glossary.md).
- **ifay**: Nombre del sistema del proyecto; véase [glossary.md](./glossary.md).
- **agent**: Entidad agent en los marcos LLM tradicionales; véase [glossary.md](./glossary.md).
- **phase**: Número de etapa evolutiva en el blueprint; véase [glossary.md](./glossary.md).

La forma principal en chino de MeriToken se utiliza como denominación convencional de MeriToken únicamente en el cuerpo del texto de los blueprints `zh-CN` y `zh-TW`. Véase la sección `Localized_Term` de [glossary.md](./glossary.md) para conocer las reglas de localización de MeriToken en cada lengua.
