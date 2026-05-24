# 06 Temas avanzados de MeriToken

> Introducción: Este documento es el slot de extensión del conjunto de temas sobre MeriToken. A partir de todos los acuerdos previos en [01-meritoken-overview.md](./01-meritoken-overview.md) hasta [05-meritoken-credential.md](./05-meritoken-credential.md), desarrolla como temas avanzados autónomos dos escenarios de uso de alta densidad de MeriToken en la nueva sociedad: «uso de alta densidad entre múltiples sujetos» y «escenarios rodantes». Cada tema no reformula los conceptos ya cubiertos en la línea principal; vuelve a colocar los mecanismos de la línea principal en un escenario concreto de presión para mirarlos de nuevo.

## Antecedentes

La línea principal, los documentos 01 a 05, ha clarificado la posición de MeriToken, sus principios técnicos, su sentido social, sus modos de referencia y sus aplicaciones, y su frontera con `credential`. Sin embargo, una vez que la nueva sociedad aterriza de hecho, emergen dos clases de escenarios de «alta carga» que la discusión de la línea principal no puede cubrir directamente:

- **Uso de alta densidad entre múltiples sujetos**: cuando varios sujetos `Fay` y varios sujetos personales hacen referencia a MeriToken de forma continuada sobre el mismo tema, una referencia individual parece sencilla, pero el agregado plantea tres problemas: sobrecarga, revelación y agregación.
- **Escenarios rodantes**: cuando el ciclo de vida de una colaboración es lo suficientemente largo, MeriToken deja de ser el rastro de un entregable puntual y debe atravesar ciclos de acumulación, revisión, retirada y archivado a lo largo de varias rondas. Esto exige que el mecanismo de MeriToken siga siendo autoconsistente en una escala temporal larga, y no solo parecer razonable en un único acto de referencia.

Este documento desarrolla los dos temas. Cada tema esboza primero la fuente de la presión, repasa después los mecanismos de la línea principal (recuperación, revelación, rastro, propiedad y derechos de uso, frontera con `credential`, etc.) bajo esa presión, y señala preguntas abiertas que merecen mayor argumentación o trabajo de ingeniería. Este documento no introduce conceptos nuevos en la capa de protocolo; todo es una derivación continua de los mecanismos ya definidos en la línea principal, aplicados en escenarios nuevos.

## Contenido principal

### Tema A: Uso de alta densidad entre múltiples sujetos

**Fuente de la presión**: en la colaboración real de la nueva sociedad, «un sujeto `Fay` hace referencia a un MeriToken» es un escenario mínimo demasiado idealizado. Lo más habitual es que sobre el mismo tema aparezcan simultáneamente tres clases de referenciadores:

- **Múltiples sujetos `Fay`**: por ejemplo, colaboradoras y colaboradores de distintos sectores y regiones que hacen referencia, cada cual en nombre de quienes integran su agrupación, a los MeriToken pertinentes;
- **Múltiples sujetos personales**: por ejemplo, las personas clave participantes sobre el tema citan, cada una, las entradas MeriToken de sus propias colaboraciones pertinentes pasadas;
- **Referencia anidada**: los sujetos `Fay` anteriores hacen referencia, a su vez, a entradas MeriToken de algunos sujetos personales como base de su autoridad de representación.

Esta referencia de alta densidad ocurre dentro del mismo tema, en la misma ventana temporal y sobre la misma superficie de revelación, y empuja varias propiedades del mecanismo de MeriToken hasta sus límites de presión a la vez.

**Mecanismos repasados**:

- **El límite de la agregación de referencias**: la referencia por agregación de un único sujeto `Fay` ya es una superficie compuesta de referencia (véase la sección «Los modos de referencia y los escenarios de aplicación de los sujetos Fay» de [04-meritoken-usage.md](./04-meritoken-usage.md)). Cuando las superficies compuestas de referencia de varios sujetos `Fay` se apilan sobre el mismo tema, la persona revisora externa no necesita que «cada MeriToken se despliegue» sino «confirmar que esas superficies agregadas no se contradicen entre sí sin desplegar los detalles». Esto significa que la referencia por agregación debe admitir «conciliabilidad en el nivel de la agregación», no solo verificabilidad en el nivel de las entradas individuales.
- **Coordinación de la revelación por niveles**: en el uso de alta densidad, cada parte referenciada (un sujeto personal o un sujeto `Fay` de nivel inferior) puede tener un permiso distinto de nivel de revelación. La parte agregadora no puede mezclar revelaciones de nivel alto y nivel bajo en una única presentación externa; de lo contrario, equivaldría a forzar la escalada de una revelación de nivel bajo. El tema A exige el principio de «el nivel mínimo de revelación como red de seguridad»: el nivel de revelación de una superficie agregada no es superior al nivel de permiso más bajo entre cualquiera de las entradas referenciadas que contiene, y solo se escala como conjunto cuando todas las partes referenciadas consienten activamente.
- **Eco de la vía de revocación**: cuando un sujeto personal subyacente revoca su permiso de revelación, la cuota correspondiente a esa entrada debe quedar invalidada de inmediato en cada superficie agregada de sujeto `Fay` que dependía de ella. No debe darse la situación de que «aguas arriba se ha revocado pero aguas abajo la agregación sigue exponiendo mediante cachés». Esto extiende la semántica de «revocación e invalidación» de la sección «Garantías de privacidad» de [02-meritoken-technical.md](./02-meritoken-technical.md) al escenario anidado.
- **Legibilidad del rastro de recuperación**: en el escenario de alta densidad, registrar cada referencia bajo `GMC` hace que el volumen del rastro de un único tema crezca con rapidez. El rastro en la capa del mecanismo sigue siendo necesario, pero, para la presentación humana, debe plegarse a lo largo de los tres ejes de «tema — sujeto — tiempo» con el fin de evitar que el proceso de auditoría se ahogue en entradas de rastro en bruto.

**Preguntas abiertas**:

- Qué conjunto de mecanismos de compromiso porta exactamente la conciliabilidad en el nivel de la agregación debe diseñarse junto con las reglas del nivel superior de `GMC`;
- El flujo de negociación entre «el nivel mínimo de revelación como red de seguridad» y el deseo de una participante o un participante individuales de escalar el conjunto debería, a su vez, registrarse como entradas MeriToken;
- Las reglas de presentación para el plegado del rastro no son una cuestión de la capa de protocolo, pero deben acordarse al unísono entre el conjunto de herramientas que da soporte al blueprint.

> ⏳ **Ilustración pendiente** (slot: `meritoken-deep-cases-density`)
> Descripción: Un diagrama conceptual que presenta la agregación de referencias / revelación por niveles / vías de revocación de MeriToken en escenarios de colaboración de alta densidad entre sujetos.
> Archivo previsto: `illustration/meritoken-deep-cases-density.png`

### Tema B: Escenarios rodantes

**Fuente de la presión**: en proyectos de ciclo de vida largo, MeriToken no se queda en la unidad mínima de «una contribución — una evaluación — un rastro». Reaparecerá a lo largo de una escala temporal larga mediante ciclos de acumulación, revisión, retirada y archivado. Los escenarios típicos incluyen proyectos públicos transgeneracionales, colaboraciones de código abierto que evolucionan a largo plazo y la gobernanza comunitaria que se enfrenta a múltiples cohortes de participantes. La presión que aportan tales proyectos ya no es la complejidad de un único acto de referencia, sino la autoconsistencia del mecanismo en una escala temporal larga.

**Mecanismos repasados**:

- **Acumulación**: cada etapa del proyecto deposita nuevas entradas MeriToken que se registran bajo `GMC` y no se pierden cuando cambian las etapas. Pero la «imagen global» que el proyecto presenta hacia el exterior debe evitar apilar todas las entradas indiscriminadamente; es necesario estratificar por etapa, por rol y por tema. Esto es coherente con «de la capacidad puntual al retrato multidimensional» de la sección «Mapeo del crecimiento personal» de [03-meritoken-social.md](./03-meritoken-social.md), pero del lado del proyecto debe ser un sujeto `Fay` el que asuma la responsabilidad de la agregación estratificada.
- **Revisión**: cuando una entrada MeriToken existente recibe, en la capa de los hechos, un nuevo testimonio, una nueva evaluación o una nueva comparación, la respuesta apropiada es añadir una entrada de revisión en lugar de sobrescribir la original. La entrada de revisión es a su vez una entrada MeriToken, que contiene el motivo de la revisión y la cofirma multilateral. A lo largo de la línea temporal, una persona lectora puede ver tanto la entrada original como las revisiones posteriores, lo que evita la situación en la que «una única entrada se reescribe repetidamente y la historia queda aplanada».
- **Retirada**: en un ciclo de vida largo, la retirada se refiere no solo a la retirada de los permisos de revelación sino también a la retirada del efecto de la entrada original (por ejemplo, la parte emisora se marcha, o la condición previa de la colaboración cambia). La retirada del efecto no borra el rastro; marca el estado de la entrada como «retirada» de modo que las personas que la referencien posteriormente puedan distinguir «las referencias hechas antes de la retirada» de «las referencias hechas después de la retirada». El acto de retirada sigue la vía de revocación independiente definida en la sección «La frontera y la correspondencia» de [05-meritoken-credential.md](./05-meritoken-credential.md), sin compensar la vía de recuperación de `credential`.
- **Archivado**: cuando termina una etapa de un proyecto o el proyecto en su conjunto concluye, las entradas MeriToken pertinentes deben pasar a un estado archivado en lugar de ser destruidas. En el estado archivado, las entradas siguen pudiendo ser verificadas y citadas de manera independiente, pero el nivel de revelación por defecto desciende al mínimo, lo que evita la situación en la que, años después de la finalización de un proyecto de larga duración, las entradas sigan exponiendo a quienes participaron en un nivel de revelación alto. La transición de archivado se registra a su vez bajo `GMC`, lo que evita cualquier opacidad de «pasado un determinado momento, la visibilidad de una entrada cambia silenciosamente».

**Autoconsistencia del mecanismo**: acumulación / revisión / retirada / archivado forman un ciclo completo, y cada acción deja rastro como una nueva entrada. Esto garantiza que la dimensión del «tiempo» en sí misma quede integrada en el mecanismo de MeriToken, en lugar de ser controlada unilateralmente desde fuera por la parte titular del proyecto. Cualquier cambio de estado a lo largo de la dimensión temporal debe ser verificable de manera independiente, sin depender de la interpretación de la parte titular del proyecto.

**Preguntas abiertas**:

- Si el ámbito de cofirma multilateral de una entrada de revisión debe coincidir exactamente con el de la entrada original es algo que debe afinarse por escenario;
- Si el nivel de revelación por defecto de la transición de archivado puede ajustarse colectivamente entre la parte titular del proyecto y quienes participaron, y el flujo de negociación que ello requiere;
- Si el peso de la referencia entre etapas decae con el tiempo es una elección estratégica por proyecto y debe ser apoyada por el conjunto de herramientas en lugar de ser impuesta por la capa de protocolo.

## Relación con otros temas

| Tema | Relación con este documento |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Aporta las definiciones de los dos roles fundacionales. El tema A y el tema B se construyen ambos sobre «componente de contrato / conector de relaciones sociales». |
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Aporta la semántica técnica concreta de recuperación, revelación, retirada y propiedad/derecho de uso, que los temas tratados aquí reutilizan bajo alta densidad y sobre escalas temporales largas. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Aporta la base de sentido social del «mapeo del peso del discurso». El tema A la reutiliza en la colaboración entre sujetos; el tema B la reutiliza en los escenarios rodantes. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Aporta los modos de referencia y los escenarios de aplicación para las dos clases de referenciadores: sujetos personales y sujetos `Fay`. El tema A es su extensión bajo el apilamiento de alta densidad. |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Aporta la frontera y la correspondencia con `credential`. El tema B reutiliza el principio de «vías de revocación independientes» en la vía de retirada. |
| [07-related-projects.md](./07-related-projects.md) | Aporta los enlaces externos oficiales para los temas aguas arriba como ifay, `GMC`, `Fay`, `agent`, `phase` y el marco general. |

## Notas de términos

`Reserved_Term`s que aparecen en este documento:

- **GMC**: Global Merit Chain, el sistema superior al que pertenece MeriToken; véase [glossary.md](./glossary.md).
- **Fay**: Sujeto no personal que hace referencia a MeriToken; véase [glossary.md](./glossary.md).
- **credential**: credential (credencial de identidad y de propiedad) para un sujeto personal o un sujeto `Fay`; véase [glossary.md](./glossary.md).
- **ifay**: Nombre del sistema del proyecto; véase [glossary.md](./glossary.md).

La forma principal en chino de MeriToken se utiliza como denominación convencional de MeriToken únicamente en el cuerpo del texto de los blueprints `zh-CN` y `zh-TW`. Véase la sección `Localized_Term` de [glossary.md](./glossary.md) para conocer las reglas de localización de MeriToken en cada lengua.
