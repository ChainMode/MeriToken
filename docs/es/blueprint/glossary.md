# Glosario (es)

Este glosario es el diccionario de referencia único para la documentación multilingüe del blueprint de iFay. Las entradas listadas en la tabla `Reserved_Term` conservan su forma inglesa original en todas las versiones lingüísticas y no se traducen. Las entradas de la tabla `Localized_Term` cambian su forma principal según la lengua de destino. Las entradas que no son ni `Reserved_Term` ni `Localized_Term` se localizan según los usos propios de cada lengua.

## Reserved_Term (forma inglesa original conservada en todas las lenguas)

| Original en inglés | Definición | Política de traducción | Enlace de referencia (Upstream_Project_Doc_Link) |
|----------|----------|----------|-----------------------------------|
| iFay / ifay | Nombre del ecosistema del proyecto iFay; en el contexto de avatares, `iFay` (Individual Fay) designa un avatar digital personal anclado 1:N a un único `Human Prime` | Reservado: se conserva la forma inglesa original en todas las lenguas | https://ifay.ai |
| agent | Entidad agent (en los marcos LLM tradicionales, una entidad de programa que ejecuta tareas de forma autónoma) | Reservado: se conserva la forma inglesa original en todas las lenguas | https://ifay.ai |
| phase | Etapa (un número de etapa evolutiva en el blueprint) | Reservado: se conserva la forma inglesa original en todas las lenguas, con el número escrito a continuación (por ejemplo, `phase 1`) | — |
| credential | Credential (credencial de identidad y propiedad para un `Human Prime` o un sujeto `Fay`) | Reservado: se conserva la forma inglesa original en todas las lenguas | ./05-meritoken-credential.md |
| GMChain | Global Merit Chain, el sistema superior no monetario de medición de contribución social y gobernanza al que pertenece MeriToken | Reservado: se conserva la abreviatura canónica `GMChain` en todas las lenguas | ./01-meritoken-overview.md |
| Fay | Término general para los avatares digitales autónomos dentro del sistema iFay (`Fay = iFay + coFay`), donde `iFay` es el avatar personal anclado a un único `Human Prime` y `coFay` es el avatar colaborativo no personal de rol público atribuido en una sola capa a una persona física responsable o a una organización | Reservado: se conserva la forma inglesa original en todas las lenguas | ./04-meritoken-usage.md |
| Human Prime | Persona física representada y responsable última dentro del sistema iFay | Reservado: se conserva `Human Prime` | https://ifay.ai |
| Host | Dispositivo físico terminal, aplicación cliente o entorno de ejecución donde opera o ejerce control autorizado un `Fay` (nunca se refiere a una persona física) | Reservado: se conserva `Host` | https://ifay.ai |

## Localized_Term (la forma principal cambia según la lengua de destino)

| Original en inglés | 中文主用名 | Regla de tratamiento |
|----------|------------|----------|
| MeriToken | 美誉值 | El cuerpo del texto de `zh-CN` y `zh-TW` utiliza «美誉值» (`zh-TW`: «美譽值») como forma principal y permite anotar entre paréntesis la forma inglesa original `MeriToken` en su primera aparición en esa versión lingüística. El cuerpo del texto de `en`, `de`, `es`, `fr`, `ja`, `ko` y `ru` utiliza la forma inglesa original `MeriToken` y no debe sustituirse por una traducción localizada. |

## Nota sobre MeriToken_Chinese_Name

«美誉值» es el nombre principal en chino de MeriToken y solo se utiliza como denominación convencional de este concepto en el cuerpo del texto de los blueprints `zh-CN` y `zh-TW`. MeriToken es una medida estrictamente no monetaria de contribución social: no es canjeable por dinero, especulativa ni transferible. La cadena «美誉值» no aparece en ninguna otra versión lingüística (incluida `en`).

## Entradas no reservadas

| Término de origen | Forma sugerida en español | Notas |
|------|----------|------|
| 蓝图 | blueprint | Se traduce según el uso convencional de cada lengua. |
| 校对 | revisión | — |
| 凭证管理 | gestión de credential | Cuando «credential» se conserva en su forma original, la frase completa se traduce como «gestión de credential». |
