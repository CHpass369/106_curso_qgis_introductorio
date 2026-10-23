---
title: Descargas
description: Paquete de datos del curso (caso Cochabamba), contenido, licencias y cómo se construyó.
---

# Descargas

## Paquete de datos del curso

[:material-download: Descargar curso-qgis-cochabamba.zip (14 MB)](curso-qgis-cochabamba.zip){ .md-button .md-button--primary }

Contiene la carpeta `curso-qgis/` lista para usar: datos originales, datos de ejercicios con errores intencionales, estilos y un proyecto base con rutas relativas. Descomprímela en una ubicación **local y corta** (por ejemplo `C:\curso-qgis\`) y sigue la lección [2.1](../modulo-02/01-entorno-trabajo.md).

![Caso conductor: municipio de Cochabamba](../assets/images/mapas/caso-cochabamba.png){ loading=lazy }

### Contenido

| Carpeta | Archivo | Qué es | SRC |
|---|---|---|---|
| `datos/originales/` | `limites.gpkg` | Límite municipal, 6 comunas, 327 zonas de análisis de 1 km² con población, municipios metropolitanos | EPSG:32719 |
| | `equipamientos.csv` | 661 establecimientos de salud y educación (CSV con `;` y coma decimal) | EPSG:4326 |
| | `vias.gpkg` | Red vial con jerarquía | EPSG:32719 |
| | `rios.shp` | Ríos, torrenteras y canales | EPSG:4326 |
| | `dem_copernicus_30m.tif` | Modelo de elevación de 30 m | EPSG:4326 |
| | `sentinel2_2025-07-16.tif` | Imagen Sentinel-2, 4 bandas, 10 m | EPSG:32719 |
| | `poblacion_worldpop_2020.tif` | Población estimada, 100 m | EPSG:4326 |
| | `mercados.geojson` | Mercados y ferias (GeoJSON) | EPSG:4326 |
| | `poblacion_comunas.csv` | Población estimada por comuna (tabla sin geometría) | — |
| | `plano_historico_1985.tif` | Plano escaneado **simulado**, sin georreferenciar | — |
| `datos/ejercicios/` | `equipamientos_errores.csv` | Codificación, coordenadas intercambiadas, duplicados | EPSG:4326 |
| | `comunas_sin_prj.shp` | Shapefile sin `.prj` | desconocido |
| | `vias_principales_src_erroneo.gpkg` | SRC declarado incorrecto | erróneo |
| | `poblacion_comunas_claves.csv` | Claves con formatos distintos, huérfanos y duplicados | — |
| | `equipamientos_auditoria.gpkg` | Problemas de calidad para auditar | EPSG:32719 |
| `proyectos/` | `curso_qgis_base.qgz` | Proyecto con las capas base organizadas | EPSG:32719 |
| `estilos/` | `*.qml` | Estilos de comunas, vías, ríos, equipamientos, DEM y Sentinel-2 | — |

### Fuentes y licencias

| Fuente | Licencia | Atribución |
|---|---|---|
| OpenStreetMap (extracto Geofabrik, 08-10-2026) | ODbL 1.0 | © colaboradores de OpenStreetMap |
| Copernicus DEM GLO-30 | Licencia Copernicus DEM (uso libre con atribución) | © DLR e.V. 2010-2014 y © Airbus 2017-2018, distribuido por la ESA |
| Sentinel-2 L2A (16-07-2025, tesela 19KGA) | Datos Copernicus, uso libre | Contiene datos modificados de Copernicus Sentinel (2025) |
| WorldPop 2020, población restringida | CC BY 4.0 | WorldPop (www.worldpop.org) |
| Natural Earth (figuras) | Dominio público | Natural Earth |

!!! warning "Limitaciones que debes conocer"

    Las comunas son las de OpenStreetMap, la población es un **modelo** (WorldPop) y no un censo, y el plano de 1985 es una **simulación didáctica**. Son limitaciones reales que se discuten en las lecciones de calidad ([1.13](../modulo-01/13-calidad-informacion.md), [3.1](../modulo-03/01-preparar-datos-confiables.md)).

??? info "Cómo se construyó el paquete (reproducible)"

    Ejecuta los scripts desde la raíz del [repositorio](https://github.com/chpass369/106_curso_qgis_introductorio/tree/main/scripts). Los scripts de datos, figuras y soluciones requieren el Python de QGIS 4.x; el empaquetador usa Python estándar. En los comandos siguientes, `python-qgis` representa el lanzador de Python de tu instalación de QGIS (en Windows, `python-qgis.bat` dentro de su carpeta `bin`).

    1. Descarga las fuentes:
        - `bolivia-AAMMDD.osm.pbf` de <https://download.geofabrik.de/south-america/bolivia.html>
        - Tesela `Copernicus_DSM_COG_10_S18_00_W067_00_DEM.tif` del bucket público `copernicus-dem-30m` de AWS; guárdala en `FUENTES/` con el nombre `cop30_S18_W067.tif`, que espera el script
        - `bol_ppp_2020_constrained.tif` de <https://www.worldpop.org>
    2. Construye los datos, el proyecto base, las figuras y las soluciones. `FUENTES` es la carpeta de descargas y `SALIDA` una carpeta de trabajo:

        !!! warning "Usa una carpeta de salida dedicada"

            El constructor elimina y vuelve a crear `SALIDA/curso-qgis`. No uses una carpeta con proyectos o datos personales.

        ```bash
        python-qgis scripts/construir_paquete_datos.py FUENTES SALIDA/curso-qgis
        python-qgis scripts/generar_figuras_y_proyecto.py SALIDA/curso-qgis
        python-qgis scripts/soluciones_modulo3.py SALIDA/curso-qgis
        python-qgis scripts/generar_figuras_modulo4.py SALIDA/curso-qgis
        python scripts/empaquetar_paquete.py SALIDA/curso-qgis
        ```

    Sentinel-2 se descarga directamente desde el catálogo abierto de AWS durante la construcción. Los generadores de figuras actualizan `docs/assets/images/mapas/`; las soluciones se guardan en `SALIDA/soluciones/`, fuera del paquete para estudiantes.

    3. Copia `SALIDA/curso-qgis-cochabamba.zip` a `docs/descargas/curso-qgis-cochabamba.zip` para actualizar la descarga del sitio. Comprueba la compilación con `python -m mkdocs build --strict`.
