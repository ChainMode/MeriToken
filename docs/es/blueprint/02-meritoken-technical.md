# 02 Principios técnicos de MeriToken

> Introducción: A partir del posicionamiento establecido en [01-meritoken-overview.md](./01-meritoken-overview.md), este documento despliega las invariantes técnicas que MeriToken debe satisfacer bajo los dos roles —«componente de contrato» y «conector de relaciones sociales»—, a lo largo de cinco hilos: cifrado, almacenamiento, recuperación, garantías de privacidad y garantías de propiedad y de derecho de uso. Este documento no reformula el diseño global de `GMC`; cuando aparece comportamiento del nivel superior, se remite a los enlaces externos de [07-related-projects.md](./07-related-projects.md).

## Antecedentes

Una vez que MeriToken asume el papel de componente de contrato y de conector de relaciones sociales que se referencia repetidamente en la nueva sociedad, sus principios técnicos no pueden detenerse en «escribir una sola entrada en el libro mayor». Cada generación, transferencia y referencia de un MeriToken se examina a lo largo de dos dimensiones innegociables: primero, la verificabilidad —cualquier entrada referenciada debe poder ser verificada de manera independiente por cualquier tercero—; segundo, las garantías de privacidad —el contenido de una entrada referenciada no necesita ser plenamente revelado a partes no relacionadas durante el acto de referenciar—.

Este documento toma estas dos restricciones innegociables como punto de partida y desarrolla la discusión a lo largo de los cinco hilos de cifrado, almacenamiento, recuperación, garantías de privacidad y garantías de propiedad y de derecho de uso. Cada hilo corresponde a un conjunto de principios técnicos concretos que operan bajo las restricciones del sistema superior `GMC`, pero este documento no despliega los detalles de la capa de protocolo del propio `GMC`.

## Contenido principal

### Cifrado

A lo largo de todo el ciclo de vida de generación y transferencia, MeriToken utiliza el mismo sistema de claves asimétricas que `GMC` para emitir y contrafirmar entradas:

- **Cofirma multilateral**: una entrada MeriToken porta al menos dos clases de firmas: «contribuyente y testigo». Pueden añadirse firmas adicionales cuando intervienen evaluaciones o arbitrajes de terceros. La cofirma multilateral es el soporte técnico mínimo de la semántica de «componente de contrato»; que falte una firma significa que falta una pieza de prueba de cumplimiento.
- **Compromiso del contenido**: el contenido sustancial de una entrada (descripción de la contribución, contexto, huellas de los entregables, etc.) se registra en cadena en forma de compromiso; el contenido original en sí no necesita estar en cadena. Esto preserva la verificabilidad y, a la vez, evita exponer detalles de contenido irrelevantes a toda la red `GMC`.
- **Auditable pero ocultable**: en escenarios de auditoría, el contenido subyacente a un compromiso puede revelarse de forma selectiva, y el propio acto de revelación deja un rastro. Sin revelación, los terceros pueden seguir verificando la existencia y la propiedad de la entrada, pero no pueden leer los detalles del contenido.

El objetivo del diseño del cifrado no es convertir MeriToken en un archivo de contenido «a prueba de filtraciones». Es asegurar que, bajo la semántica de «componente de contrato», cada promesa y cada acto de cumplimiento cuente con un respaldo criptográfico independiente, y que cada acto de referencia no requiera volver a exponer el contenido original.

### Almacenamiento

La cuestión clave en la capa de almacenamiento no es «dónde almacenar» sino «con qué granularidad organizar y quién persiste»:

- **Compromisos en cadena, contenido fuera de cadena**: los compromisos criptográficos y las firmas de las entradas MeriToken se persisten en la cadena de `GMC`; el contenido original (entregables de una contribución, texto de evaluación, etc.) lo conserva el sujeto fuera de cadena según su política local. Los compromisos en cadena garantizan la consistencia de las entradas a escala de red, y el contenido fuera de cadena preserva la autoridad del sujeto sobre sus propios datos.
- **Agregación por sujeto**: el almacenamiento fuera de cadena se agrega con la granularidad de los sujetos personales o de los sujetos `Fay`. Cada sujeto decide su propio soporte de almacenamiento, su política de copias de seguridad y su ventana de accesibilidad, sin depender de ningún proveedor de servicios centralizado.
- **Redundancia y recuperabilidad**: un sujeto puede optar por confiar una copia cifrada de su contenido fuera de cadena a una contraparte de confianza (lo que también se registra como una entrada MeriToken), de modo que sea posible la recuperación si la copia local se pierde. El propio acto de confianza también queda registrado en `GMC`, lo que impide cualquier vía encubierta de «recuperación a partir de la nada».

Dividir el almacenamiento en las dos capas de «compromiso en cadena / contenido fuera de cadena» equilibra los objetivos de «verificabilidad a escala de red» y «custodia controlada por el sujeto». Sin uno de los dos, MeriToken degeneraría bien en un archivo público legible por cualquiera, bien en un sistema local de puntos que no admite referencia entre sujetos.

### Recuperación

La recuperación designa el flujo concreto que cualquier sujeto (personal o `Fay`) sigue al hacer referencia a un MeriToken:

- **Por referencia y no por copia**: la parte referenciada no entrega al referenciador una copia de la entrada MeriToken. En su lugar, le proporciona un identificador de referencia verificable de manera independiente. Con ese identificador, el referenciador verifica la existencia y la propiedad de la entrada contra `GMC` y, si lo necesita, puede solicitar a la parte referenciada una revelación adicional.
- **Revelación por niveles**: el solicitante puede pedir tres niveles de revelación: «existencia + propiedad» (revelación mínima), «resumen semántico de la entrada» (revelación intermedia) y «detalles del contenido original» (revelación máxima). Cada nivel es una acción independiente; no existe el comportamiento por defecto de «haber recibido el identificador concede automáticamente acceso al contenido».
- **La recuperación deja rastro**: cada acción de recuperación (incluidas las recuperaciones de revelación cero que solo verifican la existencia) deja rastro bajo las reglas del nivel superior de `GMC`. Ese rastro sirve a la vez como prueba de auditoría y como dato de aristas en el grafo de relaciones sociales posterior, donde queda registrado «quién ha referenciado a quién».

Dividir la recuperación en los tres pasos de «referenciar → verificar → revelar» permite que MeriToken siga siendo de uso intensivo bajo la semántica de «conector de relaciones sociales»: en la mayoría de las colaboraciones bastan los dos primeros pasos para suministrar confianza; solo cuando los detalles realmente necesiten examinarse entrará en juego el tercer paso.

### Garantías de privacidad

Las garantías de privacidad no son un único rasgo, sino la semántica de privacidad extraída de cada una de las capas de cifrado, almacenamiento y recuperación:

- **Revelación mínima por defecto**: el valor por defecto de cualquier relación de referencia es el nivel mínimo de revelación; cualquier recuperación por encima del mínimo requiere el consentimiento activo de la parte referenciada, y ese consentimiento se registra a su vez como una entrada MeriToken.
- **Las relaciones no pueden reconstruirse por terceros observadores**: un tercero no puede reconstruir el grafo social completo de «quién ha referenciado a quién y qué se ha referenciado» a partir únicamente de los compromisos en cadena de `GMC`. La visibilidad de cada acto de referencia se restringe al referenciador y a la parte referenciada, y puede ampliarse opcionalmente a terceros específicos.
- **Revocación e invalidación**: bajo el acuerdo original, la parte referenciada puede revocar el permiso de revelación, tras lo cual la entrada de nivel de revelación alto deja de ser válida para el referenciador desde ese momento. Las acciones de referencia que ya hayan tenido lugar siguen siendo verificables de manera independiente, pero el contenido previamente revelado deja de poder ser referenciado de nuevo.

El objeto de la garantía de privacidad no es «que los datos no aparezcan nunca en cadena» —eso contradiría la verificabilidad—. Es «que solo los compromisos vivan en cadena, y el contenido se revele únicamente cuando esté autorizado». Esta es una consecuencia necesaria de la semántica de «componente de contrato» en la dimensión de la privacidad.

### Garantías de propiedad y de derecho de uso

La propiedad y los derechos de uso son dos asuntos que deben tratarse por separado:

- **La propiedad se define por la relación de firma**: la propiedad de una entrada MeriToken se define conjuntamente por las firmas más tempranas del «contribuyente y el testigo» sobre esa entrada y queda anclada de forma inmutable en `GMC`. La propiedad no se diluye por sucesivas referencias y no se desplaza hacia sujetos no firmantes mediante acuerdos de transferencia.
- **Los derechos de uso los concede la parte referenciada**: a diferencia de la propiedad, el «derecho de uso» describe «quién, en qué escenarios, puede hacer referencia a este MeriToken e incorporarlo a su cadena argumentativa». Los derechos de uso los concede la parte referenciada por escenario, formando una matriz de autorización de «escenario × usuario» independiente de los cambios en la propiedad.
- **Prioridad en caso de conflicto**: cuando la propiedad y los derechos de uso entran en conflicto (por ejemplo, el titular del derecho de uso desea revelar el contenido original mientras que la persona propietaria se niega), el derecho de revocación de la persona propietaria tiene prioridad. Esta prioridad es la consecuencia directa, bajo la semántica de «componente de contrato», de que «la promesa precede a la cita».

Dividir la propiedad y los derechos de uso en dos capas evita la ambigüedad de «haber referenciado tu MeriToken significa que ahora me pertenece». La propiedad es un bit institucional; el derecho de uso es un bit relacional. La distinción entre ambos se invoca de manera reiterada en las colaboraciones de la nueva sociedad.

> ⏳ **Ilustración pendiente** (slot: `meritoken-technical-flow`)
> Descripción: Un diagrama de flujo que muestra el ciclo cerrado de cifrado / almacenamiento / recuperación de MeriToken: cofirma multilateral del contribuyente y del testigo → compromiso en cadena en `GMC` → contenido fuera de cadena conservado localmente por el sujeto → recuperación por el referenciador mediante un identificador → revelación por niveles → reescritura del rastro de recuperación en `GMC`.
> Archivo previsto: `illustration/meritoken-technical-flow.png`

## Relación con otros temas

| Tema | Relación con este documento |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Aporta las definiciones de los dos roles que este documento tecnifica. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Extiende la «recuperación / garantía de privacidad / derecho de uso» de este documento al sentido en las capas de las relaciones sociales, la lógica política y la estructura económica. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Concretiza el flujo de «recuperación» de este documento en escenarios de aplicación para las dos clases de referenciadores: los sujetos personales y los sujetos `Fay`. |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Sitúa la «propiedad y los derechos de uso» de este documento junto al credential de identidad y de propiedad que porta `credential`, y establece la correspondencia. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Reutiliza los flujos de recuperación y revelación definidos en este documento bajo el uso de alta densidad y los escenarios rodantes. |
| [07-related-projects.md](./07-related-projects.md) | Aporta los enlaces externos oficiales para los temas aguas arriba como la capa de protocolo global de `GMC` y el entorno operativo del sistema ifay. |

## Notas de términos

`Reserved_Term`s que aparecen en este documento:

- **GMC**: Global Merit Chain, el sistema superior al que pertenece MeriToken; véase [glossary.md](./glossary.md).
- **Fay**: Sujeto no personal que hace referencia a MeriToken; véase [glossary.md](./glossary.md).
- **credential**: credential (credencial de identidad y de propiedad) para un sujeto personal o un sujeto `Fay`; véase [glossary.md](./glossary.md).
- **ifay**: Nombre del sistema del proyecto; véase [glossary.md](./glossary.md).

La forma principal en chino de MeriToken se utiliza como denominación convencional de MeriToken únicamente en el cuerpo del texto de los blueprints `zh-CN` y `zh-TW`. Véase la sección `Localized_Term` de [glossary.md](./glossary.md) para conocer las reglas de localización de MeriToken en cada lengua.
