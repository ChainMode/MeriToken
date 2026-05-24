# 04 Modos de referencia y aplicaciones de MeriToken

> Introducción: Este documento parte del posicionamiento de [01-meritoken-overview.md](./01-meritoken-overview.md), del flujo de recuperación de [02-meritoken-technical.md](./02-meritoken-technical.md) y del sentido social de [03-meritoken-social.md](./03-meritoken-social.md). Aborda por separado, para las dos clases de referenciadores —sujetos personales y sujetos `Fay`—, las tres preguntas «quién hace referencia a MeriToken», «cómo se hace la referencia» y «en qué escenarios se hace referencia a MeriToken».

## Antecedentes

Los dos roles fundacionales de MeriToken —«componente de contrato» y «conector de relaciones sociales»— solo entran en juego cuando MeriToken es referenciado de hecho. Este blueprint divide explícitamente a quienes referencian MeriToken en dos clases:

- **Sujetos personales**: personas físicas que actúan como referenciadoras y utilizan MeriToken para participar en colaboraciones, expresar evaluaciones y hacer valer sus derechos.
- **Sujetos `Fay`**: sujetos no personales dentro del sistema ifay que asumen la responsabilidad de «hacer referencia a MeriToken»; por ejemplo, organizaciones, proyectos, unidades de colaboración e instancias de servicio Fay-ificadas. En la nueva sociedad, los sujetos `Fay` asumen el rol de referenciador en paralelo con los sujetos personales, pero sus modos de referencia y sus escenarios de aplicación difieren estructuralmente de los de los sujetos personales.

La razón para discutir las dos clases de referenciadores en paralelo es evitar dos sesgos habituales en la nueva sociedad: tratar MeriToken como una mera extensión del currículo personal, o tratar MeriToken como una mera herramienta de puntuación interna en una organización. Solo al colocar las dos clases de referenciadores una junto a la otra puede presentarse una imagen completa de MeriToken como infraestructura social.

Las diferencias entre `Fay` y el `agent` tradicional las cargan los enlaces externos oficiales de [07-related-projects.md](./07-related-projects.md) y no se reformulan aquí.

## Contenido principal

### Los modos de referencia y los escenarios de aplicación de los sujetos personales

El sujeto personal es el referenciador más directo de MeriToken en la nueva sociedad. Un sujeto personal es a la vez productor de MeriToken (contribuyente, testigo, evaluador) y usuario de MeriToken (que cita entradas existentes en colaboraciones, recursos y deliberaciones).

#### Modos de referencia

La forma concreta en la que un sujeto personal hace referencia a MeriToken sigue el flujo en tres pasos «referenciar → verificar → revelar» descrito en [02-meritoken-technical.md](./02-meritoken-technical.md), y se materializa en cuatro clases de acciones concretas:

- **Referencia por tenencia**: el sujeto personal mantiene el conjunto de sus propios MeriToken en su retrato de crecimiento, su archivo de colaboraciones y su archivo de participación comunitaria, y presenta un subconjunto a contrapartes específicas cuando lo necesita. El acto de presentación solo genera un registro de referencia en el nivel mínimo de revelación y no fuerza la divulgación de los detalles.
- **Referencia por cita**: en argumentaciones, propuestas y recursos, el sujeto cita entradas MeriToken existentes —propias o ajenas— como prueba. Una cita debe acompañarse de un identificador de referencia verificable, de modo que la audiencia pueda verificar de manera independiente la existencia y la propiedad de la entrada en lugar de fiarse de la afirmación unilateral de la parte que cita.
- **Referencia relacional**: cuando colabora con otra parte, el sujeto utiliza las entradas MeriToken existentes de la contraparte como base de confianza y deposita el resultado de la colaboración presente como nuevas entradas MeriToken. Es la materialización más habitual de la semántica de «conector de relaciones sociales» en el lado del sujeto personal.
- **Referencia por retirada**: el sujeto revoca una autorización de nivel de revelación alto previamente concedida a un referenciador específico. Una retirada no borra el rastro de la acción de referencia original, pero retira al referenciador el derecho a seguir exponiendo el contenido.

Estos cuatro modos comparten el mismo sustrato técnico (cofirma multilateral, compromisos en cadena, revelación por niveles) y solo difieren en los escenarios de activación y en la elección del nivel de revelación.

#### Escenarios de aplicación

A continuación se presentan varios escenarios típicos de aplicación que muestran cómo un sujeto personal utiliza MeriToken en la colaboración cotidiana de la nueva sociedad:

- **Primer apretón de manos en una colaboración entre organizaciones**: cuando un sujeto personal se incorpora a un grupo de colaboración nuevo, puede presentar un subconjunto de MeriToken pertinentes al tema del grupo en el nivel mínimo de revelación, lo que permite al grupo realizar una revisión inicial sin exponer el retrato personal.
- **Cualificación para hablar sobre asuntos públicos**: cuando un sujeto personal interviene sobre un asunto público, cita sus propias entradas MeriToken sobre asuntos adyacentes como prueba del peso de su intervención, y la audiencia puede verificarlas de manera independiente cuando lo necesite.
- **Escenarios de educación y transmisión**: cuando un sujeto personal actúa como mentor o mentora, la relación de mentoría se deposita como las correspondientes entradas MeriToken. La acumulación a largo plazo por parte de la persona aprendiz produce un archivo de crecimiento verificable de manera independiente, no prisionero de ninguna institución educativa.
- **Escenarios de recurso y rectificación**: cuando un sujeto personal considera injusta una entrada MeriToken existente, puede iniciar una entrada de recurso para registrar el propio proceso de cuestionamiento en `GMC`. El resultado final (sea estimado o desestimado) también se deposita como una nueva entrada.
- **Cambio entre identidades**: cuando un sujeto personal se desplaza entre roles sociales (profesión, comunidad, participación pública), puede presentar de forma selectiva el subconjunto de MeriToken pertinente al rol actual y evitar la sobreexposición de retratos no relacionados.

Todos estos escenarios siguen el principio compartido de «revelación mínima por defecto, escalada impulsada por el escenario, revocación siempre presente», en consonancia con las garantías de privacidad de [02-meritoken-technical.md](./02-meritoken-technical.md).

### Los modos de referencia y los escenarios de aplicación de los sujetos Fay

Los sujetos `Fay` son los sujetos no personales dentro del sistema ifay que asumen la responsabilidad de «hacer referencia a MeriToken». Un sujeto `Fay` no sustituye a un sujeto personal; es un amplificador de la colaboración entre sujetos personales. Asume el papel de referenciar, agregar y coordinar en colaboraciones de mayor escala, con más participantes y con un ciclo de vida más largo.

#### Modos de referencia

Los modos de referencia de los sujetos `Fay` comparten el mismo flujo subyacente que los de los sujetos personales, pero difieren estructuralmente en los escenarios de uso y en los límites de autoridad:

- **Referencia por delegación**: un sujeto `Fay` ejerce la autoridad de referencia, en nombre de un grupo de sujetos personales o de sub-sujetos `Fay` dentro de su ámbito de autorización, de manera unificada. La propia relación de delegación queda registrada como una entrada MeriToken, con el ámbito de autorización, el período de validez y las condiciones de revocación enunciados explícitamente en la entrada.
- **Referencia por agregación**: un sujeto `Fay` puede agregar las entradas MeriToken de varios sujetos personales para formar una superficie compuesta de referencia hacia el exterior. La agregación no es posesión: cada entrada agregada sigue perteneciendo a su propietaria o propietario originales; el sujeto `Fay` solo conserva el derecho de uso de «hacer referencia a esas entradas en un escenario concreto».
- **Referencia por protocolo**: cuando un sujeto `Fay` colabora con otro sujeto `Fay`, la relación de referencia suele basarse en un protocolo previamente firmado. El propio protocolo también queda registrado como entradas MeriToken y constituye un libro mayor de colaboración entre sujetos `Fay`.
- **Referencia por gestión del ciclo de vida**: un sujeto `Fay` puede hacer referencia a las entradas MeriToken sobre su propio ciclo de vida (constitución, transiciones de phase, disolución), lo que permite a los sujetos externos ver su historia y sus cambios.

La autoridad de referencia de un sujeto `Fay` es técnicamente homóloga a la de un sujeto personal, pero en la capa institucional está más estrechamente restringida: el límite de la agregación, el alcance de la delegación y la visibilidad del protocolo requieren todos registros verificables relativamente claros, con el fin de evitar el desequilibrio de «un sujeto `Fay` que se apoya en su escala para imponerse a los sujetos personales».

#### Escenarios de aplicación

Los escenarios de aplicación típicos de los sujetos `Fay` en la nueva sociedad son los siguientes:

- **Sujetos de colaboración de proyectos públicos**: los proyectos públicos transregionales y entre organizaciones colaboran hacia el exterior como sujetos `Fay`, agregando las contribuciones de muchos sujetos personales en una superficie unificada de referencia hacia el exterior que muestra el perfil global de MeriToken del proyecto.
- **Libros mayores de colaboración a escala sectorial**: varios sujetos `Fay` de un sector establecen un libro mayor compartido mediante referencia por protocolo, reconocen mutuamente sus entradas MeriToken y evitan la conciliación reiterada entre organizaciones.
- **Unidades de ejecución en la gobernanza comunitaria**: los sujetos `Fay` que actúan como unidades de ejecución dentro de una comunidad implementan las decisiones tomadas mediante deliberación y depositan las acciones de decisión como entradas MeriToken trazables. Quienes integran la comunidad pueden citar esas entradas en cualquier momento para cuestionar o elogiar a la unidad de ejecución.
- **Continuidad transgeneracional de los proyectos**: los proyectos de larga duración existen en forma de sujetos `Fay`, de modo que el archivo de colaboración se preserva incluso después de la marcha de los miembros fundadores. Las personas que se incorporan acceden a la historia del proyecto mediante referencia por tenencia y evitan las rupturas de conocimiento de un «reinicio del proyecto».
- **Asumir la responsabilidad y dar testimonio del cumplimiento**: un sujeto `Fay` en la nueva sociedad es a la vez un amplificador de la colaboración y portador de responsabilidad. Cuando un sujeto `Fay` hace una promesa al exterior, la propia promesa queda registrada como una entrada MeriToken, y el cumplimiento o el incumplimiento se anclan en la entrada correspondiente.

Los escenarios de aplicación de los sujetos `Fay` no sustituyen a los de los sujetos personales. Son, más bien, «dos escalas de la misma infraestructura»: los sujetos personales atienden la colaboración local, cara a cara y puntual, mientras que los sujetos `Fay` atienden la colaboración transregional, entre organizaciones y a largo plazo. Las dos clases de referenciadores se referencian entre sí y se rinden cuentas mutuamente a través de las entradas MeriToken, lo que constituye la ecología de colaboración de la nueva sociedad.

> ⏳ **Ilustración pendiente** (slot: `meritoken-usage-comparison`)
> Descripción: Un diagrama comparativo que presenta a las dos clases de referenciadores —sujetos personales y sujetos `Fay`—, junto con sus modos de referencia (tenencia / cita / relacional / retirada frente a delegación / agregación / protocolo / ciclo de vida) y los escenarios de aplicación típicos, con anotaciones que muestran que las dos clases de referenciadores se referencian entre sí y se rinden cuentas mutuamente a través de las entradas MeriToken.
> Archivo previsto: `illustration/meritoken-usage-comparison.png`

## Relación con otros temas

| Tema | Relación con este documento |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Aporta las definiciones de los dos roles fundacionales sobre los que aterrizan la referencia y las aplicaciones de este documento. |
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Aporta el flujo de recuperación y la semántica de privacidad / propiedad que sostienen cada modo de referencia presentado aquí. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Aporta el trasfondo de sentido social para los escenarios de aplicación que aquí aparecen (relaciones sociales, lógica política, estructura económica, mapeo del crecimiento personal). |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | En la capa de la semántica de «identidad y propiedad», contrasta con la semántica de «contribución y evaluación» que se trata aquí, evitando que ambas se mezclen. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Extiende los escenarios de aplicación de aquí en colaboraciones de alta densidad entre sujetos y en escenarios rodantes. |
| [07-related-projects.md](./07-related-projects.md) | Aporta los enlaces externos oficiales para los temas aguas arriba como `Fay`, `agent`, ifay, `GMC` y el marco general. |

## Notas de términos

`Reserved_Term`s que aparecen en este documento:

- **Fay**: Sujeto no personal que hace referencia a MeriToken; véase [glossary.md](./glossary.md).
- **agent**: Entidad agent en los marcos LLM tradicionales; véase [glossary.md](./glossary.md).
- **ifay**: Nombre del sistema del proyecto; véase [glossary.md](./glossary.md).
- **GMC**: Global Merit Chain, el sistema superior al que pertenece MeriToken; véase [glossary.md](./glossary.md).
- **credential**: credential (credencial de identidad y de propiedad) para un sujeto personal o un sujeto `Fay`; véase [glossary.md](./glossary.md).

La forma principal en chino de MeriToken se utiliza como denominación convencional de MeriToken únicamente en el cuerpo del texto de los blueprints `zh-CN` y `zh-TW`. Véase la sección `Localized_Term` de [glossary.md](./glossary.md) para conocer las reglas de localización de MeriToken en cada lengua.
