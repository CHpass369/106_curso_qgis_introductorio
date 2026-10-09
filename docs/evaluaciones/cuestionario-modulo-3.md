---
title: Cuestionario · Módulo 3
description: Diez preguntas de autoevaluación sobre calidad, edición, formularios, indicadores, uniones, relaciones espaciales, proximidad, ráster y reproducibilidad, con repaso de módulos anteriores.
---

# Cuestionario · Módulo 3

Responde **antes** de abrir cada respuesta. Objetivo: 8 de 10. Las preguntas 9 y 10 son de **repaso**.

??? question "1. Dos puntos tienen el mismo código pero están a 3 km. ¿Los eliminas como duplicados?"

    No. Son **entidades distintas** con un código mal asignado: se corrige el código y se registra en la bitácora. → [3.1](../modulo-03/01-preparar-datos-confiables.md)

??? question "2. ¿Qué diferencia hay entre una geometría válida y una topología correcta?"

    La validez se evalúa en **cada** geometría; la topología, en la **relación** entre geometrías (huecos, solapamientos). → [3.2](../modulo-03/02-digitalizar-editar-precision.md)

??? question "3. ¿Por qué `\"pob\" / nullif(\"n_salud\", 0)` es mejor que `coalesce(\"pob\" / \"n_salud\", 0)`?"

    Porque devuelve `NULL` (no calculable) en lugar de **0**, que se leería como «excelente cobertura». → [3.4](../modulo-03/04-construir-indicadores-expresiones.md)

??? question "4. Unes una tabla en la que `C05` aparece dos veces. ¿Qué pasa?"

    QGIS toma la **primera** coincidencia y descarta la otra **sin aviso**. Comprueba la unicidad antes de unir. → [3.5](../modulo-03/05-integrar-tablas.md)

??? question "5. Un punto cae exactamente sobre el límite de dos comunas. ¿En cuántas lo cuenta *interseca*?"

    En **ambas**. *Está dentro* no lo cuenta en ninguna. → [3.6](../modulo-03/06-relaciones-espaciales.md)

??? question "6. Un buffer de 1000 sobre una capa en EPSG:4326 cubre medio continente. ¿Por qué?"

    Porque las unidades son **grados**: 1000° no son 1 km. Reproyecta a un SRC en metros. → [3.7](../modulo-03/07-proximidad-superposicion.md)

??? question "7. ¿Qué método de remuestreo usarías para reproyectar un ráster de población (conteos)?"

    **Suma** (al agrandar celdas) o trabajar con densidades: vecino más cercano a celdas más pequeñas multiplica el total. → [3.8](../modulo-03/08-preparar-combinar-raster.md)

??? question "8. ¿Por qué un RMSE de 0 con *thin plate spline* no garantiza una buena georreferenciación?"

    Porque el modelo pasa exactamente por los puntos de control; el error real se mide con puntos **independientes**. → [3.10](../modulo-03/10-georreferenciar-mapas-historicos.md)

??? question "9. Repaso · ¿Qué significa que un 15 % de la población «no tiene cobertura»? Menciona dos supuestos."

    Que vive en zonas cuyo punto interior está a más de 1 km en **línea recta** de un establecimiento de salud registrado en **OSM**, con población **modelada** (WorldPop). Otros supuestos: tipo de establecimiento incluido, regla de cobertura. → [3.7](../modulo-03/07-proximidad-superposicion.md)

??? question "10. Repaso · ¿Por qué la pendiente calculada sobre un DEM en grados es errónea?"

    Porque mezcla distancias horizontales en **grados** con alturas en **metros**. → [3.9](../modulo-03/09-relieve-estadisticas-zonales.md) · [2.6](../modulo-02/06-problemas-coordenadas.md)
