---
title: 2.11 Conectar información disponible en internet
description: Conexión de información geográfica en línea mediante XYZ, WMS/WMTS y WFS; diferencias entre mapas como imagen y entidades vectoriales, cobertura, atribución, metadatos y dependencia de servicios remotos.
---

# 2.11 Conectar información disponible en internet

No todo dato tiene que estar en tu disco. Un mapa base, una imagen satelital sin nubes de toda Bolivia o el mapa de suelos del mundo están **a una URL de distancia**. Pero hay una diferencia enorme entre recibir un **dibujo** del dato y recibir **el dato mismo**, y también entre «funciona hoy» y «funcionará el día de la presentación». Esta lección te enseña a conectar servicios y a saber qué estás recibiendo.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Distinguir servicios que entregan **imágenes** (XYZ, WMS, WMTS) de los que entregan **entidades** (WFS).
    - Crear conexiones XYZ, WMS/WMTS y WFS en el Navegador.
    - Leer el **documento de capacidades** de un servicio.
    - Cumplir con la **atribución** y evaluar la **dependencia** de internet.

    **Tiempo:** 75 min (20 de lectura · 55 de práctica) · **Datos:** servicios en línea (requiere internet) · **Producto:** `proyectos/reto_2-11_servicios_web.qgz` y una ficha de cada servicio.

---

## Idea central

### ¿Imagen o dato?

| Servicio | Qué recibes | ¿Puedes consultar atributos? | ¿Puedes analizar? | Ejemplo |
|---|---|---|---|---|
| **XYZ** (teselas) | Imágenes prerrenderizadas por nivel de zoom | No | No | Mapa base OpenStreetMap |
| **WMTS** | Teselas según un estándar OGC | No | No | Sentinel-2 cloudless (EOX) |
| **WMS** | Una imagen generada para tu vista | A veces (GetFeatureInfo) | No | Suelos SoilGrids (ISRIC) |
| **WFS** | **Entidades vectoriales** con geometría y atributos | Sí | Sí | Caídas de meteoritos registradas por la NASA |

!!! captura "Captura pendiente · 2.11-01"

    - **Tipo:** Imagen (PNG) conceptual
    - **Archivo:** `assets/images/modulo-02/2-11/2-11-01-imagen-vs-entidad.png`
    - **Qué mostrar:** El mismo contenido representado como imagen WMS (píxeles) y como entidades WFS (puntos con atributos).

!!! danger "Una imagen no se analiza"

    Un WMS de límites municipales **se ve** como un mapa de límites, pero son píxeles: no puedes calcular áreas, seleccionar por atributos ni hacer intersecciones. Para analizar necesitas **WFS** o descargar los datos.

### Cada servicio tiene condiciones

| Pregunta | Por qué importa |
|---|---|
| ¿Quién lo publica? | Autoridad y confiabilidad |
| ¿Qué cobertura y fecha tiene? | Aptitud para tu área y periodo |
| ¿Qué licencia y atribución exige? | Uso legal y ético |
| ¿En qué SRC sirve? | XYZ y WMTS suelen ir en EPSG:3857 |
| ¿Qué pasa sin internet? | Tu mapa queda vacío en una presentación |

---

## Hazlo conmigo

### Paso 1 · XYZ: mapa base OpenStreetMap

1. **Navegador ▸ Mosaicos XYZ ▸ OpenStreetMap**: doble clic.
2. Haz clic derecho sobre la capa ▸ **Propiedades ▸ Información**: SRC **EPSG:3857**. QGIS lo reproyecta al vuelo a tu proyecto en 32719, por eso las letras pueden verse algo deformadas.
3. Observa la **atribución** en la esquina: © colaboradores de OpenStreetMap. Es obligatoria en cualquier mapa que publiques.

!!! captura "Captura pendiente · 2.11-02"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-11/2-11-02-xyz.gif`
    - **Qué mostrar:** Navegador → Mosaicos XYZ → OpenStreetMap → agregar al proyecto y revisar su información.

!!! warning "Política de uso de las teselas de OSM"

    Los servidores de OpenStreetMap son para uso **moderado e interactivo**. No descargues teselas masivamente ni generes atlas de cientos de páginas con ellos.

### Paso 2 · WMTS: Sentinel-2 sin nubes

1. **Navegador ▸ WMS/WMTS** ▸ clic derecho ▸ **Nueva conexión…**
2. **Nombre:** `EOX Sentinel-2 cloudless` · **URL:** `https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml`
3. Expande la conexión: QGIS lee el **documento de capacidades** y lista las capas. Agrega `s2cloudless-2025` (o el año más reciente disponible).
4. Compárala con tu `sentinel2_2025-07-16.tif`: ¿qué cubre cada una? ¿Qué fecha tiene cada una?

!!! captura "Captura pendiente · 2.11-03"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-11/2-11-03-conexion-wms.png`
    - **Qué mostrar:** El diálogo de nueva conexión WMS/WMTS con el nombre y la URL de EOX.

!!! info "Atribución y licencia"

    *Sentinel-2 cloudless – https://s2maps.eu by EOX IT Services GmbH (contiene datos modificados de Copernicus Sentinel)*. La versión 2016 es CC BY 4.0; los años posteriores son **CC BY-NC-SA 4.0**: no se pueden usar con fines comerciales.

### Paso 3 · WMS: suelos de Bolivia

1. Nueva conexión WMS · **Nombre:** `ISRIC SoilGrids WRB` · **URL:** `https://maps.isric.org/mapserv?map=/map/wrb.map`
2. Agrega la capa `wrb` (grupos de suelos de referencia, *World Reference Base*).
3. Con **Identificar**, haz clic en el valle de Cochabamba: el WMS responde con información de esa celda (*GetFeatureInfo*), pero **no** te entrega polígonos.

!!! captura "Captura pendiente · 2.11-04"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-11/2-11-04-capabilities-wms.png`
    - **Qué mostrar:** El catálogo de capas devuelto por el WMS de SoilGrids en el Navegador.

### Paso 4 · WFS: entidades por internet

1. **Navegador ▸ WFS / OGC API - Features** ▸ **Nueva conexión…**
2. **URL:** `https://gs-stable.geo-solutions.it/geoserver/wfs` (servidor de demostración).
3. Agrega la capa `mapstore:Meteorite_Landings_from_NASA_Open_Data_Portal`: más de 45 000 caídas de meteoritos documentadas en el mundo (datos abiertos de la NASA).
4. Abre su **tabla de atributos**: tiene `name`, `mass_g` (masa en gramos), `year` y `fall` (si se vio caer o se encontró). ¡Son entidades, no una imagen!
5. Selecciona con el rectángulo los puntos dentro de Bolivia y ordena por `mass_g`. ¿Cuál es el más pesado?
6. Ahora **puedes guardarlos**: **Exportar ▸ Guardar objetos seleccionados como…** ▸ `datos/trabajo/meteoritos_bolivia.gpkg`.

!!! note "Servidores de demostración"

    `gs-stable.geo-solutions.it` es un servidor de pruebas de GeoServer: es útil para practicar, pero puede cambiar sin aviso. Para trabajo real, usa servicios institucionales.

!!! captura "Captura pendiente · 2.11-05"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-11/2-11-05-conexion-wfs.png`
    - **Qué mostrar:** El diálogo de conexión WFS con la URL, la versión del servicio y la opción de recuperar el número máximo de entidades.

!!! tip "La fuente oficial en Bolivia: GeoBolivia"

    La Infraestructura de Datos Espaciales del Estado, **GeoBolivia** (<https://geo.gob.bo>), publica servicios WMS y WFS de instituciones públicas (límites, catastro, temáticos). Busca en su catálogo la **URL de capacidades** de cada servicio y conéctala igual que en los pasos 3 y 4. Los servidores públicos a veces cambian de dirección o están fuera de línea: anota siempre la URL y la fecha en que la usaste.

    <!-- TODO-MANUAL[verificar]: confirmar URL vigente de los servicios WMS/WFS de GeoBolivia (no respondió el 08-10-2026) y agregarla como paso 5 con una capa de límites oficiales. -->

### Paso 5 · Probar sin internet

Desconecta la red (o activa el modo avión) y recarga el proyecto. ¿Qué capas desaparecen? ¿Cuáles siguen? Así sabrás qué depende de terceros el día de tu presentación.

!!! captura "Captura pendiente · 2.11-06"

    - **Tipo:** Imagen (PNG) comparativa
    - **Archivo:** `assets/images/modulo-02/2-11/2-11-06-dependencia-internet.png`
    - **Qué mostrar:** El mismo proyecto con conexión y sin conexión.

---

## Inténtalo tú

!!! example "Reto 2.11 · Ficha de servicios"

    Agrega a `reto_2-11_servicios_web.qgz` al menos **un servicio de cada tipo** (XYZ, WMS o WMTS, WFS) útil para el caso conductor, y completa para cada uno:

    | Campo | Servicio 1 | Servicio 2 | Servicio 3 |
    |---|---|---|---|
    | Tipo (XYZ, WMS, WMTS, WFS) | | | |
    | Publicador | | | |
    | URL de capacidades | | | |
    | Capa usada | | | |
    | Cobertura y fecha | | | |
    | SRC en que sirve | | | |
    | Licencia y atribución | | | |
    | ¿Imagen o entidades? | | | |
    | ¿Sirve para analizar? | | | |
    | ¿Qué pasa sin internet? | | | |

    Responde: ¿qué servicio usarías como **fondo** de tu atlas del Módulo 4 y cuál **no** usarías? ¿Por qué?

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Conexiones | Hay al menos un servicio de imagen y uno de entidades funcionando |
| Diferencia | Explicas por qué el WFS se puede exportar y analizar y el WMS no |
| Atribución | Cada servicio tiene su atribución y licencia anotadas |
| Dependencia | Identificaste qué capas desaparecen sin internet |
| Juicio | La elección del fondo considera licencia, fecha y disponibilidad |

### Errores frecuentes

| Síntoma | Causa probable | Solución |
|---|---|---|
| La conexión no lista capas | URL sin la ruta de capacidades, o servidor caído | Prueba la URL en el navegador web |
| Las letras del mapa base se ven estiradas | Reproyección de teselas en 3857 | Es normal; para salidas finales, considera el SRC del proyecto |
| El WFS carga solo parte de las entidades | Límite de entidades por solicitud | Ajusta **Número máximo de objetos** en la conexión |
| El WMS se ve en blanco | Fuera de escala o de cobertura | Revisa los rangos de escala en las capacidades |
| El mapa queda vacío en la presentación | Sin internet | Usa datos locales para lo imprescindible |

---

## Comprueba lo aprendido

??? question "1. ¿Por qué no puedes calcular el área de un municipio a partir de un WMS?"

    Porque un WMS entrega **una imagen**: no hay geometrías, solo píxeles coloreados.

??? question "2. ¿Qué es el documento de capacidades?"

    Un XML que describe el servicio: capas, SRC disponibles, formatos, escalas y metadatos. QGIS lo lee al expandir la conexión.

??? question "3. ¿Por qué un mapa base XYZ suele estar en EPSG:3857?"

    Porque las teselas web se generan en Pseudo-Mercator, el estándar de los mapas web.

??? question "4. ¿Qué debes incluir siempre al publicar un mapa con OpenStreetMap?"

    La atribución «© colaboradores de OpenStreetMap».

??? question "5. Repaso de 2.3 · ¿Copiar la carpeta del proyecto incluye las capas WMS?"

    No: se guarda la **conexión**, no los datos. Sin internet o si el servidor cambia, la capa no se verá.

---

## Tu proyecto

Busca en GeoBolivia u otra fuente oficial una capa que **mejore** tu caso conductor (por ejemplo, límites oficiales de distritos o establecimientos del Ministerio de Salud). Compárala con los datos de OpenStreetMap: ¿coinciden? ¿Cuál usarías y por qué? Este contraste es una evaluación de **exactitud temática y completitud** ([1.13](../modulo-01/13-calidad-informacion.md)).

---

## Referencias

- de la Beaujardiere, J. (Ed.). (2006). *OpenGIS Web Map Server Implementation Specification* (OGC 06-042). Open Geospatial Consortium. <https://www.ogc.org/standards/wms>
- Vretanos, P. A. (Ed.). (2014). *OGC Web Feature Service 2.0 Interface Standard* (OGC 09-025r2). Open Geospatial Consortium. <https://www.ogc.org/standards/wfs>
- NASA. (s. f.). *Meteorite Landings* [Conjunto de datos]. NASA Open Data Portal. <https://data.nasa.gov/>
- Masó, J., Pomakis, K., & Julià, N. (2010). *OpenGIS Web Map Tile Service Implementation Standard* (OGC 07-057r7). <https://www.ogc.org/standards/wmts>
- Poggio, L., et al. (2021). SoilGrids 2.0: producing soil information for the globe with quantified spatial uncertainty. *SOIL, 7*, 217–240. <https://doi.org/10.5194/soil-7-217-2021>
- OpenStreetMap Foundation. (s. f.). *Tile Usage Policy*. <https://operations.osmfoundation.org/policies/tiles/>
- QGIS Project. (s. f.). *Manual de usuario: Trabajar con datos OGC*. <https://docs.qgis.org/latest/es/docs/user_manual/working_with_ogc/ogc_client_support.html>
