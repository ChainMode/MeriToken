# 05 La relación entre credential y MeriToken

> Introducción: Este documento parte del posicionamiento establecido en [01-meritoken-overview.md](./01-meritoken-overview.md). Bajo la semántica de «componente de contrato», trata específicamente la frontera y la correspondencia entre MeriToken y `credential`. Ambos suelen confundirse, pero en la práctica de colaboración de la nueva sociedad, no distinguirlos debilita simultáneamente la estabilidad de la identidad y la propiedad, y la acumulabilidad de la contribución y la evaluación.

## Antecedentes

Varias preguntas en la nueva sociedad —«quién soy», «puedo hacer esto», «qué he hecho», «cómo se me ha evaluado»— deben ser portadas por objetos estructuralmente independientes entre sí, pero componibles entre sí. Si se vuelcan todas las preguntas sobre una única clase de objeto, aparecen dos sesgos típicos:

- **Sobrecarga del credential**: escribir «lo que he hecho y cómo se me ha evaluado» —es decir, contenido que debería pertenecer a MeriToken— en `credential` obliga a emitir y actualizar continuamente los credentials de identidad y propiedad. La parte emisora queda sobrecargada y el titular pierde la autoridad sobre sus propios registros de evaluación.
- **Deriva de la evaluación**: escribir «quién soy y qué poseo» en MeriToken permite que los atributos de identidad opriman el contenedor de la evaluación de la contribución. Los registros de evaluación MeriToken que deberían sostenerse mediante cofirma multilateral en la colaboración acaban diluidos por el derecho a emitir credentials.

Este blueprint divide las dos clases de objetos entre dos soportes diferentes y hace explícita la asignación: `credential` resuelve el lado de la «identidad y la propiedad»; MeriToken resuelve el lado de la «contribución y la evaluación». Ambos son independientes entre sí, y aun así se corresponden mutuamente. La tarea de este documento es dejar clara la frontera entre MeriToken y `credential`, de modo que los documentos 06–07 y los distintos despliegues lingüísticos no mezclen ambos al referenciarlos.

Los detalles de la capa de protocolo de `credential` los porta la documentación oficial del sistema ifay. Este documento ofrece únicamente la explicación mínima necesaria para «la frontera con MeriToken».

## Contenido principal

![credential management](../../zh-CN/blueprint/illustration/credential-management.png)

El esquema anterior (reutilizado provisionalmente) traza las acciones básicas de `credential` a lo largo de la cadena de emisión, verificación y revocación. La discusión de este documento se construye sobre ese conjunto de acciones y lo coloca junto a la semántica de «contribución-evaluación» de MeriToken.

### El papel de credential

`credential` resuelve la pregunta «quién es el sujeto y qué propiedad tiene sobre qué objeto», y es el soporte de credential de la identidad y la propiedad en la nueva sociedad:

- **Un bit verificable de identidad y propiedad**: `credential` lo emite un sujeto con autoridad de emisión y registra los atributos de identidad del sujeto al que se emite (pertenencia, rol, cualificación, etc.) o su propiedad sobre un objeto concreto (control sobre un recurso, un bit de protocolo, un rol de protocolo). Responde a «en qué estado de propiedad se encuentra este sujeto respecto a un objeto concreto en un momento concreto».
- **Emitido, verificado y revocado en la capa credential-and-token**: el ciclo de vida de `credential` está restringido por las reglas de protocolo de la capa credential-and-token. El acto de emisión define su ámbito de validez. El acto de verificación permite a cualquier tercero confirmar de manera independiente la existencia y la propiedad del credential. El acto de revocación permite a la parte emisora recuperar a tiempo un credential cuando cambia la propiedad, lo que impide que el credential siga siendo citado tras desligarse de la propiedad real.
- **Centrado en la cualificación de entrada de «lo que se puede hacer»**: en la colaboración entre sujetos, `credential` se examina típicamente como una cualificación de entrada. Que un sujeto posea el `credential` correspondiente significa que, en la capa institucional, tiene la cualificación de entrar en una superficie concreta de colaboración, citar un bit concreto de protocolo o invocar una interfaz concreta de recursos. `credential` no evalúa directamente cómo se ha desempeñado el sujeto en el pasado.
- **La estabilidad va por delante**: la estabilidad semántica de `credential` es su propiedad fundamental. Una pertenencia de larga duración o un derecho de control de larga duración sobre un recurso no fluctúan con frecuencia con el desempeño de colaboración a corto plazo del titular. La parte fluctuante debe ser portada por MeriToken y no reflejarse en `credential`.

Anclar el papel de `credential` a «el credential de la identidad y la propiedad» mantiene simples y auditables las vías de emisión y revocación, sin que las perturben los registros de evaluación frecuentes.

### El papel de MeriToken

MeriToken resuelve la pregunta «qué ha hecho el sujeto y cómo se le ha evaluado», y es el soporte de los registros de contribución y evaluación en la nueva sociedad:

- **Un bit acumulable de contribución y evaluación**: MeriToken se genera mediante cofirma multilateral entre quienes colaboran (véanse las secciones «Cifrado» y «Recuperación» de [02-meritoken-technical.md](./02-meritoken-technical.md)) y registra, en una colaboración concreta, «quién contribuyó qué, quién atestiguó qué y cómo evaluó cada cual a cada cual». Responde a «en qué colaboraciones pasadas concretas ha actuado este sujeto, y cómo».
- **Subordinado al sistema superior `GMC`**: a diferencia de la cadena de emisión y revocación de `credential`, la cadena de generación-referencia-revocación de MeriToken se contabiliza de manera unificada bajo el sistema superior `GMC`, con la semántica de cadena que garantiza la consistencia y la inmutabilidad a escala de red (véase la sección «Cómo MeriToken pertenece a GMC» de [01-meritoken-overview.md](./01-meritoken-overview.md)).
- **Centrado en el rastro del proceso de «qué se hizo y cómo se hizo»**: MeriToken no actúa como verificación de una cualificación de entrada; se genera de forma continua a lo largo de la colaboración. Hacia el exterior puede citarse, agregarse y compararse, pero cada entrada corresponde a un hecho concreto de colaboración y no puede crearse ni eliminarse a voluntad.
- **Acumulable, revocable, con revelación por niveles**: los MeriToken se acumulan mediante colaboraciones a largo plazo en un retrato de crecimiento multidimensional. Cuando cambia el acuerdo original, la parte referenciada puede revocar el correspondiente permiso de revelación. Cada referencia deja rastro bajo `GMC` (véase la sección «Garantías de privacidad» de [02-meritoken-technical.md](./02-meritoken-technical.md)).

Anclar el papel de MeriToken a «el registro de la contribución y la evaluación» permite que la evaluación de grano fino del proceso de colaboración se acumule en el tiempo y permanezca bajo control independiente, sin verse anexada por la autoridad de emisión de credential.

### La frontera y la correspondencia

`credential` y MeriToken asumen cada uno un papel insustituible en la colaboración de la nueva sociedad. La tabla siguiente los presenta en paralelo a lo largo de cinco ejes semánticos:

| Eje semántico | `credential` | MeriToken |
|--------|--------------|---------------------|
| Foco semántico | Credential de identidad y propiedad; responde a «quién es el sujeto y qué posee sobre qué objeto» | Registro de contribución y evaluación; responde a «en qué colaboraciones el sujeto ha hecho qué y cómo se le ha evaluado» |
| Ciclo de vida | Emitido, verificado y revocado en la capa credential-and-token; pone el énfasis en las transiciones de estado de la cualificación de entrada | Contabilizado bajo el sistema superior `GMC`; la cadena de generación-referencia-revocación deja rastro bajo la semántica de cadena |
| Forma de tenencia | Un objeto de estado anclado bilateralmente entre la parte emisora y el titular; pone el énfasis en la estabilidad | Un objeto de proceso cofirmado multilateralmente por quienes colaboran; pone el énfasis en la acumulabilidad |
| Modo de referencia | Examinado en la entrada de la colaboración para verificar «si se posee la cualificación» | Citado, agregado y comparado durante o después de la colaboración para presentar «cómo se han hecho las cosas en el pasado» |
| Semántica entre sujetos | El mismo sujeto posee diferentes `credential`s en diferentes superficies de colaboración, que no son necesariamente comparables entre sí | Los MeriToken acumulados por el mismo sujeto en distintos temas pueden citarse de forma cruzada, pero el peso de evaluación no migra automáticamente |

La frontera se sostiene en cuatro niveles que se refuerzan mutuamente, garantizando que las dos clases de objetos no se mezclen:

- **No sustituibles**: `credential` no puede usarse para registrar «lo que he hecho y cómo se me ha evaluado»; de lo contrario aparece la sobrecarga del credential y una carga desequilibrada para la parte emisora. MeriToken no puede usarse para registrar «quién soy y qué poseo»; de lo contrario aparece la deriva de la evaluación y la dilución de la propiedad. Cada uno carga con tareas institucionales distintas.
- **Mutuamente presupuestos y extendidos**: en muchas colaboraciones, `credential` aporta la cualificación de entrada y MeriToken deposita el rastro del proceso una vez que el sujeto está dentro. Por ejemplo, en una deliberación entre organizaciones, `credential` decide si una persona participante tiene la cualificación para hablar, mientras que MeriToken registra la contribución y la evaluación de cada intervención, lo que se acumula en el tiempo para influir en el peso del discurso en temas posteriores (véase la sección «Lógica política» de [03-meritoken-social.md](./03-meritoken-social.md)).
- **Citados juntos, portados por separado**: en la referencia por delegación y por agregación de los sujetos `Fay` (véase la sección «Los modos de referencia y los escenarios de aplicación de los sujetos Fay» de [04-meritoken-usage.md](./04-meritoken-usage.md)), suele presentarse hacia el exterior, al mismo tiempo, un conjunto de `credential`s y un conjunto de entradas MeriToken. El primero prueba que el sujeto `Fay` posee autoridad de representación; el conjunto de MeriToken presenta su historia de colaboración. Ambos se citan en paralelo, no se fusionan.
- **Vías de revocación independientes**: la revocación de `credential` la activa la parte emisora cuando cambia la propiedad; la revocación de MeriToken la activa la parte referenciada como retirada del permiso de revelación. Estas dos vías de revocación no deben compensarse entre sí: la parte emisora no puede usar la recuperación de `credential` para borrar una entrada MeriToken ya atestiguada; la parte referenciada no puede trabajar en sentido inverso a partir de la retirada de la revelación de un MeriToken para forzar a la parte emisora a recuperar el `credential`. La independencia de las vías de revocación sigue el principio definido en la sección «La frontera y la correspondencia» de este documento.

> ⏳ **Ilustración pendiente** (slot: `meritoken-credential-boundary`)
> Descripción: Un diagrama comparativo que presenta la frontera y la correspondencia entre `credential` y MeriToken a lo largo de los dos ejes semánticos «identidad y propiedad» y «contribución y evaluación». Durante la fase de transición puede reutilizarse provisionalmente `credential-management.png`.
> Archivo previsto: `illustration/meritoken-credential-boundary.png`

## Relación con otros temas

| Tema | Relación con este documento |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Aporta las definiciones de los dos roles fundacionales sobre los que aterriza este documento, así como la subordinación de MeriToken a `GMC`. |
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Aporta la semántica técnica de MeriToken en la capa de propiedad y derecho de uso, sobre la cual este documento coloca en correspondencia la cadena de emisión y revocación de `credential`. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Reutiliza, en «lógica política» y «estructura económica», la frontera trazada aquí, lo que impide que los temas de identidad y propiedad opriman el espacio de la contribución y la evaluación. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | En la referencia por delegación y por agregación de los sujetos `Fay`, reutiliza el principio de «citados juntos, portados por separado» enunciado aquí. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Pone en práctica de forma concreta la división de fronteras enunciada aquí en la colaboración de alta densidad entre sujetos y en los escenarios rodantes. |
| [07-related-projects.md](./07-related-projects.md) | Aporta los enlaces externos oficiales para `credential`, `GMC`, ifay, `Fay` y otros temas aguas arriba. |

## Notas de términos

`Reserved_Term`s que aparecen en este documento:

- **credential**: credential (credencial de identidad y de propiedad) para un sujeto personal o un sujeto `Fay`; véase [glossary.md](./glossary.md).
- **GMC**: Global Merit Chain, el sistema superior al que pertenece MeriToken; véase [glossary.md](./glossary.md).
- **Fay**: Sujeto no personal que hace referencia a MeriToken; véase [glossary.md](./glossary.md).
- **ifay**: Nombre del sistema del proyecto; véase [glossary.md](./glossary.md).

La forma principal en chino de MeriToken se utiliza como denominación convencional de MeriToken únicamente en el cuerpo del texto de los blueprints `zh-CN` y `zh-TW`. Véase la sección `Localized_Term` de [glossary.md](./glossary.md) para conocer las reglas de localización de MeriToken en cada lengua.
