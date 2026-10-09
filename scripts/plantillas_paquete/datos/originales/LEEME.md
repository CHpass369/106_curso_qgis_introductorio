# Datos originales · Caso Cochabamba

Estos archivos se entregan **tal como «se recibieron»**. No los modifiques: trabaja siempre sobre copias en `datos/trabajo/`.

| Archivo | Contenido | Formato | SRC declarado | Fuente y licencia |
|---|---|---|---|---|
| `limites.gpkg` | Capas `limite_municipal`, `comunas` (6), `zonas_analisis` (hexágonos de 1 km² con población estimada) y `municipios_metropolitanos` (7) | GeoPackage | EPSG:32719 (WGS 84 / UTM 19 S) | OpenStreetMap (ODbL); población: WorldPop 2020 (CC BY 4.0) |
| `equipamientos.csv` | 661 establecimientos de salud y educación con longitud y latitud | CSV separado por `;`, coma decimal, UTF-8 | EPSG:4326 (WGS 84, grados) | OpenStreetMap (ODbL) |
| `vias.gpkg` | Red vial con campo `jerarquia` (troncal, principal, secundaria, local) | GeoPackage | EPSG:32719 | OpenStreetMap (ODbL) |
| `rios.shp` | Ríos, torrenteras y canales | Shapefile (`.shp`, `.shx`, `.dbf`, `.prj`, `.cpg`) | EPSG:4326 | OpenStreetMap (ODbL) |
| `dem_copernicus_30m.tif` | Modelo digital de superficie, ~30 m | GeoTIFF, Float32 | EPSG:4326 | Copernicus DEM GLO-30 © DLR e.V. 2010-2014 y © Airbus 2017-2018, distribuido por la ESA |
| `sentinel2_2025-07-16.tif` | Imagen Sentinel-2 L2A del 16-07-2025: bandas 2 (azul), 3 (verde), 4 (rojo) y 8 (infrarrojo cercano), 10 m, reflectancia × 10 000 | GeoTIFF, UInt16, 4 bandas | EPSG:32719 | Contiene datos modificados de Copernicus Sentinel (2025) |
| `poblacion_worldpop_2020.tif` | Población estimada por celda de ~100 m | GeoTIFF, Float32 | EPSG:4326 | WorldPop (2020), población restringida 100 m, CC BY 4.0. <https://www.worldpop.org> |
| `mercados.geojson` | Mercados y ferias | GeoJSON (RFC 7946) | EPSG:4326 | OpenStreetMap (ODbL) |
| `plano_historico_1985.tif` | Plano escaneado **sin georreferenciar** | GeoTIFF RGB sin SRC | Ninguno | **Simulado** a partir de OpenStreetMap con fines didácticos; no es un documento histórico |

## Advertencias de calidad (para discutir en clase)

- **OpenStreetMap es colaborativo**: puede haber establecimientos sin nombre (≈ 16 %), faltantes o desactualizados. Fecha de extracción: ver columna `fecha` del CSV.
- **WorldPop es un modelo**, no un censo: estima la población distribuyendo totales oficiales según imágenes satelitales. Para el municipio suma ≈ 602 000 habitantes en 2020; compáralo con las cifras del INE.
- Las **comunas** provienen de OSM y pueden no coincidir exactamente con los límites oficiales del Gobierno Autónomo Municipal.
- El **DEM** es un modelo de **superficie**: incluye edificios y vegetación.
- La ciudad está a ~17 km del límite entre las zonas **UTM 19 S y 20 S** (lección 1.6): encontrarás datos de la región en ambas zonas.

## Atribución obligatoria

Al publicar mapas hechos con estos datos incluye:

> Datos: © colaboradores de OpenStreetMap (ODbL) · Copernicus DEM GLO-30 / Sentinel-2 (ESA) · WorldPop (CC BY 4.0)
