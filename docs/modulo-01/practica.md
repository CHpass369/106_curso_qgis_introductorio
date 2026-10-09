---
title: Práctica integradora del Módulo 1
description: Diagnóstico conceptual, sin software, del paquete de datos del caso Cochabamba: sistemas de referencia, zona UTM, escala, resolución, calidad y aptitud para el análisis de acceso a servicios.
---

# Práctica integradora del Módulo 1

Antes de abrir QGIS, un profesional **lee** lo que recibió. En esta práctica recibes la descripción del paquete de datos del caso conductor y debes decidir, **solo con los conceptos del Módulo 1**, qué datos sirven, para qué escala, en qué sistema de referencia trabajar y qué problemas anticipas.

!!! abstract "En esta práctica"

    **Integrarás:** SRC y UTM (1.4–1.6), escala (1.8), resolución y precisión (1.9), modelos (1.11), dato geoespacial (1.12) y calidad (1.13).

    **Tiempo:** 2 h · **Materiales:** esta página, calculadora y cuaderno · **Producto:** informe de diagnóstico de 2 páginas (producto del Módulo 1).

---

## El encargo

> La Dirección de Planificación del municipio de **Cochabamba** quiere saber **qué zonas tienen peor acceso a los establecimientos de salud**. Te entregan un paquete de datos. Antes de empezar el análisis, debes emitir un **diagnóstico**: qué se puede hacer con estos datos, con qué precisión y con qué riesgos.

## Los datos recibidos

| Archivo | Contenido | Modelo | SRC declarado | Resolución / escala | Fuente |
|---|---|---|---|---|---|
| `limites.gpkg` | Límite municipal, 6 comunas, 327 zonas de 1 km² con población | Vectorial (polígonos) | EPSG:32719 | Comunas de OSM | OpenStreetMap; WorldPop 2020 |
| `equipamientos.csv` | 661 establecimientos de salud y educación, columnas `longitud` y `latitud` con coma decimal | Tabla | EPSG:4326 | Coordenadas con 6 decimales | OpenStreetMap |
| `vias.gpkg` | Red vial con jerarquía | Vectorial (líneas) | EPSG:32719 | Uso ≈ 1:10 000 | OpenStreetMap |
| `rios.shp` | Ríos, torrenteras, canales | Vectorial (líneas) | EPSG:4326 | — | OpenStreetMap |
| `dem_copernicus_30m.tif` | Modelo digital de **superficie** | Ráster (1 banda, Float32) | EPSG:4326 | ≈ 30 m | Copernicus |
| `sentinel2_2025-07-16.tif` | Imagen multiespectral (azul, verde, rojo, IR cercano) | Ráster (4 bandas, UInt16) | EPSG:32719 | 10 m | Copernicus Sentinel-2 |
| `poblacion_worldpop_2020.tif` | Población **estimada** por celda | Ráster (1 banda, Float32) | EPSG:4326 | ≈ 90 m | WorldPop |
| `plano_historico_1985.tif` | Plano escaneado | Ráster RGB | **Ninguno** | Escala 1:20 000 (según el rótulo) | Archivo (simulado) |

---

## Parte A · Sistemas de referencia (30 min)

1. El municipio se extiende aproximadamente entre las longitudes **−66,30°** y **−66,05°**. Calcula la zona UTM de ambos extremos. ¿Todo el municipio cae en una sola zona?
2. ¿Qué SRC de trabajo propones para el análisis? Da su nombre y su código EPSG en WGS 84 y en SIRGAS 2000.
3. ¿Qué archivos deberán **reproyectarse** al SRC de trabajo? ¿Cuál no tiene SRC y qué operación necesitará (asignar, reproyectar o georreferenciar)?
4. La ciudad está a ~17 km del meridiano 66° O. ¿Qué riesgo implica para los datos que recibas de otras instituciones?

## Parte B · Escala, resolución y precisión (30 min)

5. ¿A qué escala máxima es razonable usar el DEM de 30 m? (Pista: una celda ≈ 0,5 mm en el mapa.)
6. ¿Y la imagen de 10 m? ¿Se podría digitalizar sobre ella el borde de una acera?
7. Las coordenadas de los establecimientos tienen **6 decimales** en grados. ¿Qué precisión numérica representan? ¿Es una buena estimación de su exactitud?
8. Calcula el **error gráfico** de un mapa de salida a 1:100 000 y a 1:10 000. ¿Qué capas tendrían sentido en cada uno?

## Parte C · Calidad y aptitud (40 min)

9. Para cada fuente, completa:

    | Fuente | Elemento de calidad más preocupante (ISO 19157) | Por qué | ¿Cómo lo evaluarías? |
    |---|---|---|---|
    | OSM (establecimientos) | | | |
    | WorldPop | | | |
    | DEM Copernicus | | | |
    | Comunas (OSM) | | | |

10. El indicador «habitantes por establecimiento» combina WorldPop y OSM. Si WorldPop sobrestima un 10 % y OSM omite un 15 % de los establecimientos, ¿en cuánto se sobrestima el indicador?
11. ¿Para qué **sí** sirven estos datos y para qué **no**? Escribe dos usos adecuados y dos inadecuados.

## Parte D · Informe (20 min)

Redacta el **informe de diagnóstico** (2 páginas) con: SRC de trabajo y justificación, tabla de datos con su tratamiento, escala de trabajo y de salida, principales riesgos de calidad y una recomendación sobre cómo comunicar la incertidumbre en los resultados.

---

## ¿Lo hiciste bien?

??? success "Respuestas de referencia"

    1. −66,30° → zona 19; −66,05° → (113,95 / 6) = 18,99 → zona **19**. Todo el municipio cae en la zona 19 (muy cerca del borde).
    2. **WGS 84 / UTM 19 S (EPSG:32719)**; en SIRGAS 2000: **EPSG:31979**.
    3. Reproyectar: `equipamientos.csv` (tras importarlo en 4326), `rios.shp`, el DEM y la población. El plano histórico **no tiene SRC**: necesita **georreferenciación** (puntos de control), no una simple asignación.
    4. Que lleguen datos de la región en **UTM 20 S** y, si se declaran mal, aparezcan desplazados ~640 km ([1.6](06-sistema-utm.md), [2.6](../modulo-02/06-problemas-coordenadas.md)).
    5. 30 m / 0,5 mm ≈ **1:60 000** como escala máxima razonable; para mayor detalle el DEM se ve «pixelado» y su exactitud no alcanza.
    6. ≈ 1:20 000. **No**: una acera mide 2–3 m, menos que una celda de 10 m.
    7. 6 decimales ≈ **0,1 m**. No: es **precisión numérica**; la exactitud de OSM suele ser de varios metros.
    8. 1:100 000 → **20 m**: comunas, vías principales, zonas, ríos principales. 1:10 000 → **2 m**: toda la red vial, establecimientos con nombre, imagen de 10 m como fondo.
    9. Respuestas posibles: OSM → **completitud** (omisiones) y exactitud temática (clasificación de establecimientos); WorldPop → **exactitud temática/cuantitativa** (es un modelo); DEM → **exactitud** vertical y que es de **superficie** (incluye edificios); Comunas → **exactitud posicional** de los límites frente a los oficiales.
    10. Numerador ×1,10; denominador ×0,85 → 1,10 / 0,85 ≈ **1,29**: se sobrestima ≈ **29 %**.
    11. Sí: patrones generales de acceso, priorizar zonas para verificar en terreno. No: decidir la ubicación exacta de un edificio, calcular camas por habitante (no hay capacidad confiable).

---

## Referencias

- Longley, P. A., Goodchild, M. F., Maguire, D. J., & Rhind, D. W. (2015). *Geographic Information Science and Systems* (4.ª ed.). Wiley.
- International Organization for Standardization. (2013). *ISO 19157:2013 Geographic information — Data quality*. ISO.
- Descripción del paquete de datos: [Descargas](../descargas/index.md).
