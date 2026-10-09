---
title: 2.4 Incorporar datos y reconocer sus diferencias
description: Incorporación e inspección de datos vectoriales y ráster en QGIS; diferencias entre GeoPackage, Shapefile, GeoJSON y GeoTIFF; geometrías, extensión, campos, bandas y metadatos.
---

# 2.4 Incorporar datos y reconocer sus diferencias

Abres `datos/originales/` y encuentras un `.gpkg`, un grupo de archivos `rios.*`, un `.geojson` y varios `.tif`. Todos son «datos geográficos», pero no guardan la información de la misma manera ni sirven para lo mismo. Antes de analizar nada, vas a pasar de **«tengo varios archivos»** a **«sé qué datos tengo y para qué sirven»**.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Distinguir **modelo** (vectorial o ráster) de **formato** (GeoPackage, Shapefile, GeoJSON, GeoTIFF).
    - Incorporar datos desde el **Navegador** y el **Administrador de fuentes de datos**.
    - Leer en una capa vectorial su geometría, número de entidades, extensión, SRC y campos.
    - Leer en un ráster sus dimensiones, tamaño de celda, bandas, tipo de dato y NoData.
    - Construir un **inventario** y decidir qué fuentes usar.

    **Tiempo:** 90 min (30 de lectura · 60 de práctica) · **Datos:** `datos/originales/` · **Producto:** `documentos/inventario_datos.csv` y `proyectos/reto_2-4_inventario.qgz`.

---

## Idea central

### Modelo y formato no son lo mismo

**Vectorial** y **ráster** son *modelos*: formas de representar el territorio ([1.11](../modulo-01/11-modelos-representacion.md)). **GeoPackage**, **Shapefile**, **GeoJSON** y **GeoTIFF** son *formatos*: formas de guardar esos modelos en archivos.

| | Vectorial | Ráster |
|---|---|---|
| Unidad | Entidad (geometría + atributos) | Celda o píxel |
| Geometría | Punto, línea o polígono | Matriz regular |
| Descripción | Campos de la tabla de atributos | Valores en una o varias bandas |
| Tamaño | Número de entidades | Columnas × filas |
| Detalle | Precisión de la geometría | Tamaño de celda |
| Pregunta típica | ¿Qué atributos tiene esta comuna? | ¿Qué elevación tiene esta celda? |

!!! captura "Captura pendiente · 2.4-02"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-02-vector-raster.png`
    - **Qué mostrar:** A la izquierda las comunas y los equipamientos de Cochabamba; a la derecha el DEM ampliado hasta distinguir sus celdas.

### Cuatro formatos que encontrarás siempre

| Formato | Archivos | Modelo | Lo que debes saber |
|---|---|---|---|
| **GeoPackage** | Un `.gpkg` | Vectorial (y ráster) | **Contenedor**: un archivo puede tener varias capas. Formato preferido del curso |
| **Shapefile** | `.shp` + `.shx` + `.dbf` (+ `.prj`, `.cpg`, `.qix`) | Vectorial | **Varios archivos** que viajan juntos; nombres de campo de hasta 10 caracteres |
| **GeoJSON** | Un `.geojson` | Vectorial | **Texto**; muy usado en la web. Según el estándar RFC 7946, en WGS 84 (grados) |
| **GeoTIFF** | Un `.tif` | Ráster | Imagen que **sabe dónde está**; una o varias bandas |

| Componente del Shapefile | Contiene |
|---|---|
| `.shp` | Geometrías |
| `.shx` | Índice de geometrías |
| `.dbf` | Tabla de atributos |
| `.prj` | Sistema de referencia |
| `.cpg` | Codificación de caracteres |

!!! danger "No copies solo el `.shp`"

    Sin `.dbf` no hay atributos; sin `.prj`, QGIS no sabe en qué SRC están las coordenadas (lo comprobarás en [2.6](06-problemas-coordenadas.md)).

!!! warning "Formato moderno no significa dato correcto"

    Un Shapefile puede ser perfectamente válido y un GeoPackage, inútil para tu trabajo. Decide por el **contenido**, la **fecha**, la **cobertura** y la **procedencia**, no por la extensión del archivo.

??? example "Así se ve un GeoJSON por dentro"

    ```json
    {
      "type": "Feature",
      "properties": { "nombre": "Mercado La Cancha" },
      "geometry": { "type": "Point", "coordinates": [-66.1557, -17.4005] }
    }
    ```

    El orden es **[longitud, latitud]**: primero X, después Y.

### Lo que revisas antes de usar una fuente

| Si es vectorial | Si es ráster |
|---|---|
| Tipo de geometría (Point, MultiPolygon…) | Columnas × filas |
| Número de entidades | Tamaño de celda y sus unidades |
| Extensión | Número de bandas y qué representa cada una |
| SRC | Tipo de dato (Byte, UInt16, Float32…) |
| Campos y sus **tipos** | Valor NoData |
| Procedencia y fecha | Extensión, SRC, procedencia y fecha |

Tres advertencias:

- **La extensión no es cobertura.** Es el rectángulo que contiene los datos; puede estar casi vacío.
- **Vacío, `0` y `NULL` no son lo mismo**, y **NoData no es cero**: un píxel con 0 puede ser una medición válida.
- **Que dos capas se superpongan bien no prueba que tengan el mismo SRC**: QGIS las reproyecta al vuelo.

---

## Hazlo conmigo

### Paso 1 · Incorporar las fuentes

1. Abre `reto_2-3_gestion.qgz` y guárdalo como `proyectos/reto_2-4_inventario.qgz`.
2. En el **Navegador**, despliega `datos/originales/limites.gpkg`: verás **cuatro capas internas**. Arrastra solo `zonas_analisis` si aún no está.
3. Abre el **Administrador de fuentes de datos** (++ctrl+l++) ▸ **Vectorial** y añade `rios.shp`.
4. Desde el Navegador, añade `mercados.geojson`, `poblacion_worldpop_2020.tif` y `sentinel2_2025-07-16.tif`.

!!! captura "Captura pendiente · 2.4-03"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-03-geopackage-capas.gif`
    - **Qué mostrar:** Expandir `limites.gpkg` desde el Navegador, observar sus cuatro capas internas y añadir solo una.

!!! captura "Captura pendiente · 2.4-06"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-06-incorporar-datos.gif`
    - **Qué mostrar:** Incorporar un GeoPackage, un Shapefile, un GeoJSON y un GeoTIFF alternando entre Navegador y Administrador de fuentes de datos.

!!! tip "Navegador y Capas no son lo mismo"

    El **Navegador** muestra lo que *existe* en tus carpetas. El panel **Capas** muestra lo que *forma parte del proyecto*.

### Paso 2 · Inspeccionar una capa vectorial

Clic derecho sobre **Ríos y torrenteras** ▸ **Propiedades ▸ Información**. Deberías leer:

| Dato | Valor esperado |
|---|---|
| Geometría | LineString |
| Entidades | 2 651 |
| SRC | EPSG:4326 · WGS 84 (grados) |
| Campos | `osm_id`, `nombre`, `tipo` (texto) |

Ahora abre la **tabla de atributos** (++f6++). ¿Cuántos ríos tienen `nombre` vacío? Ordena por esa columna haciendo clic en su encabezado.

!!! question "¿Una capa llamada `rios` que contiene polígonos está equivocada?"

    No necesariamente: podría representar la **superficie** de los cauces. El nombre no define el contenido; la geometría y los metadatos, sí.

### Paso 3 · Inspeccionar un ráster

Abre **Propiedades ▸ Información** de `sentinel2_2025-07-16`:

| Dato | Valor esperado | Qué significa |
|---|---|---|
| Dimensiones | 1 237 × 923 | 1,14 millones de celdas **por banda** |
| Tamaño de celda | 10 × 10 m | Cada píxel cubre 100 m² |
| Bandas | 4 | Azul, verde, rojo e infrarrojo cercano |
| Tipo de dato | UInt16 | Enteros de 0 a 65 535 (reflectancia × 10 000) |
| SRC | EPSG:32719 | UTM 19 S, en metros |

Compáralo con `poblacion_worldpop_2020`: **1 banda**, **Float32**, celda de **0,000833°** (≈ 90 m) y **NoData = −99999**.

!!! captura "Captura pendiente · 2.4-05"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-05-raster-informacion.png`
    - **Qué mostrar:** Propiedades ▸ Información de `sentinel2_2025-07-16.tif` destacando dimensiones, bandas, tipo de dato, tamaño de celda, extensión y SRC.

!!! danger "Más píxeles no es más información"

    Remuestrear el ráster de población a 10 m produciría diez veces más celdas, pero **ni un dato nuevo**: solo repetiría valores ([1.9](../modulo-01/09-escala-resolucion-precision.md)).

### Paso 4 · Comparar extensiones

Haz **Zoom a la capa** sobre cada fuente. Todas deberían cubrir aproximadamente el municipio, salvo la imagen Sentinel-2, que solo cubre el **área urbana central**. Anótalo: es una limitación de **cobertura** que importará en [2.10](10-explorar-raster.md).

!!! captura "Captura pendiente · 2.4-07"

    - **Tipo:** Imagen (PNG) comparativa
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-07-extension.png`
    - **Qué mostrar:** La extensión del municipio frente a la extensión, más pequeña, de la imagen Sentinel-2.

### Paso 5 · Leer los metadatos disponibles

Abre `datos/originales/LEEME.md`. Compara lo que declara con lo que acabas de observar. Cuando un dato no esté documentado, **no lo inventes**: escribe *No disponible* o *Por verificar*. La ausencia de documentación también es información.

---

## Inténtalo tú

!!! example "Reto 2.4 · Inventario del paquete de datos"

    Crea `documentos/inventario_datos.csv` (puedes hacerlo en una hoja de cálculo) con **todas** las fuentes de `datos/originales/`, incluida **cada capa interna** de `limites.gpkg`:

    | id | fuente | capa | modelo | formato | geometría o bandas | entidades o dimensiones | SRC | fecha | procedencia | estado | justificación |
    |---|---|---|---|---|---|---|---|---|---|---|---|

    Para **estado** usa solo: **Utilizable**, **Revisar / preparar** o **No utilizar por ahora**. La justificación es una frase, por ejemplo:

    > *Revisar / preparar:* el ráster de población está en grados y con otra resolución que las zonas de análisis; habrá que reproyectarlo antes de combinarlos.

    Luego responde: ¿qué fuentes están en grados y cuáles en metros? ¿Qué dos problemas de SRC prevés para el análisis de cobertura?

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Completitud | Están todas las fuentes y las cuatro capas de `limites.gpkg` (12 filas) |
| Vector | Geometría, entidades y SRC coinciden con lo que muestra QGIS |
| Ráster | Dimensiones, bandas, tipo de dato, celda y NoData están registrados |
| SRC | Detectaste que `rios.shp`, `mercados.geojson`, `equipamientos.csv`, el DEM y la población están en EPSG:4326 |
| Decisión | Cada fuente tiene estado y una justificación concreta |
| Conservación | `datos/originales/` sigue intacto |

### Errores frecuentes

| Síntoma | Causa probable | Qué revisar |
|---|---|---|
| Solo recibí `datos.shp` | Faltan componentes | Pide `.dbf`, `.shx`, `.prj` y `.cpg` |
| Un GeoPackage «abre» varias capas | Es un contenedor | Elige la capa interna que necesitas |
| Una capa aparece lejísimos | Coordenadas o SRC inesperados | Extensión y SRC ([2.6](06-problemas-coordenadas.md)) |
| No puedo sumar unos números | El campo es de texto | Tipo de campo ([2.7](07-leer-datos.md)) |
| Caracteres raros (`Ã±`) | Codificación | Archivo `.cpg` o codificación de la fuente ([2.5](05-tablas-coordenadas.md)) |
| El ráster tiene huecos | Celdas NoData | Propiedades ▸ Transparencia |

---

## Comprueba lo aprendido

??? question "1. Copias `predios.shp` y nada más. ¿Tienes la fuente completa?"

    No. Faltan al menos `.shx` y `.dbf`; probablemente también `.prj` y `.cpg`.

??? question "2. `limites.gpkg` aparece una vez en la carpeta, pero QGIS muestra cuatro capas. ¿Es un error?"

    No. GeoPackage es un **contenedor** de varias capas.

??? question "3. Dos capas coinciden perfectamente en el mapa. ¿Tienen el mismo SRC?"

    No necesariamente: QGIS reproyecta al vuelo. Consulta el SRC de cada fuente.

??? question "4. ¿La extensión de una capa garantiza que hay datos en todo ese rectángulo?"

    No. Es el rectángulo mínimo que la contiene; la cobertura puede ser parcial.

??? question "5. Un campo contiene `10`, `20` y `30`, pero es de tipo texto. ¿Por qué importa?"

    Porque no podrás hacer operaciones numéricas (sumar, promediar, clasificar) sin convertirlo.

??? question "6. ¿Qué significa NoData en un ráster?"

    Que en esa celda **no hay valor válido**. No es cero: un cero puede ser una medición real.

??? question "7. Recibes dos capas correctas, de 2014 y de 2026. ¿Cuál usas?"

    Depende del **período** que necesita el trabajo, la cobertura, la procedencia y el método. La fecha más reciente no siempre es la adecuada.

??? question "8. Repaso de 1.11 · ¿Qué modelo elegirías para la elevación y cuál para los equipamientos? ¿Por qué?"

    **Ráster** para la elevación (fenómeno continuo); **vectorial** de puntos para los equipamientos (objetos discretos con posición).

---

## Tu proyecto

Tu inventario es el primer documento de **calidad** del caso conductor. Agrega dos columnas: «¿sirve para medir acceso a servicios?» y «¿qué preparación necesita?». En [3.1](../modulo-03/01-preparar-datos-confiables.md) convertirás esas notas en un plan de preparación de datos.

---

## Referencias

- Longley, P. A., Goodchild, M. F., Maguire, D. J., & Rhind, D. W. (2015). *Geographic Information Science and Systems* (4.ª ed., cap. 7). Wiley.
- Butler, H., Daly, M., Doyle, A., Gillies, S., Hagen, S., & Schaub, T. (2016). *The GeoJSON Format* (RFC 7946). IETF. <https://doi.org/10.17487/RFC7946>
- Open Geospatial Consortium. (s. f.). *OGC GeoPackage Encoding Standard*. <https://www.geopackage.org>
- ESRI. (1998). *ESRI Shapefile Technical Description*. <https://www.esri.com/content/dam/esrisites/sitecore-archive/Files/Pdfs/library/whitepapers/pdfs/shapefile.pdf>
- QGIS Project. (s. f.). *Manual de usuario: Abrir datos*. <https://docs.qgis.org/latest/es/docs/user_manual/managing_data_source/opening_data.html>
- QGIS Project. (s. f.). *Manual de usuario: Propiedades de capas ráster*. <https://docs.qgis.org/latest/es/docs/user_manual/working_with_raster/raster_properties.html>
