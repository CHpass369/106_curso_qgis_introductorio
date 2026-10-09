---
title: 3.8 Preparar y combinar datos ráster
description: Preparación y combinación de datos ráster mediante control de extensión, resolución, alineación, NoData, reproyección, remuestreo y álgebra ráster en QGIS.
---

# 3.8 Preparar y combinar datos ráster

Reproyectas el ráster de población de WorldPop a UTM con 30 m de celda para combinarlo con el DEM, y el total del municipio pasa de **1,1 millones** a **10,4 millones de habitantes**. Nadie se mudó a Cochabamba: el método de **remuestreo** copió el valor de cada celda grande en las nueve celdas pequeñas que la reemplazan. Combinar ráster es potente, pero cada paso de preparación (SRC, celda, alineación, NoData) puede cambiar el resultado sin avisar.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Revisar **SRC, extensión, tamaño de celda, alineación y NoData** antes de combinar.
    - **Reproyectar** y **remuestrear** eligiendo el método según el tipo de dato.
    - **Recortar** ráster por extensión o por máscara.
    - Usar la **calculadora ráster** para índices (NDVI) y máscaras lógicas.
    - Verificar que la preparación no alteró el significado de los datos.

    **Tiempo:** 2 h (30 min de lectura · 90 de práctica) · **Datos:** `dem_copernicus_30m.tif`, `poblacion_worldpop_2020.tif`, `sentinel2_2025-07-16.tif`, `limite_municipal` · **Producto:** `datos/trabajo/raster/` con DEM en UTM, NDVI y una máscara de aptitud.

---

## Idea central

### Para combinar, las grillas deben coincidir

Dos ráster solo se pueden operar celda a celda si comparten:

| Requisito | Si no se cumple… |
|---|---|
| **SRC** | Las celdas no representan el mismo lugar |
| **Tamaño de celda** | No hay correspondencia uno a uno |
| **Alineación** (origen de la grilla) | Celdas desplazadas medio píxel |
| **Extensión** | El resultado se limita a la zona común |
| **NoData** declarado | Valores de relleno contaminan los cálculos |

### El método de remuestreo depende del dato

| Tipo de dato | Ejemplo | Método adecuado | Por qué |
|---|---|---|---|
| **Categórico** | Uso del suelo (1 = urbano, 2 = cultivo…) | **Vecino más cercano** | No inventa categorías intermedias |
| **Continuo** | Elevación, temperatura | **Bilineal** o **cúbico** | Suaviza sin saltos artificiales |
| **Conteo** | Personas por celda | **Suma** (al agrandar celdas) o redistribuir proporcionalmente | Conserva el total |
| **Índice o tasa** | NDVI, densidad | **Media** o bilineal | Promedia sin sumar |

!!! danger "Reproyectar un conteo puede multiplicar la población"

    | Ráster de población reproyectado a UTM | Población total |
    |---|---|
    | Original (≈ 90 m, grados) | **1 145 726** |
    | 100 m, vecino más cercano | 939 700 |
    | 100 m, **suma** | **1 145 726** |
    | 30 m, vecino más cercano | **10 409 601** |

    (Totales del área recortada, que incluye parte de los municipios vecinos.) Para conteos, **nunca** reduzcas la celda copiando valores; si necesitas otra resolución, agrégala con **suma** o trabaja con **densidad** (personas/km²).

### Álgebra ráster

La **calculadora ráster** opera celda a celda con expresiones:

```text
NDVI:            ("s2@4" - "s2@3") / ("s2@4" + "s2@3")
Máscara lógica:  ("pendiente@1" < 15) * ("ndvi@1" < 0.3)
```

Una expresión lógica devuelve **1** (verdadero) o **0** (falso); multiplicar dos máscaras equivale a un **Y** lógico.

---

## Hazlo conmigo

### Paso 1 · Ficha de compatibilidad

Antes de nada, compara los tres ráster ([2.10](../modulo-02/10-explorar-raster.md)):

| | DEM | Población | Sentinel-2 |
|---|---|---|---|
| SRC | EPSG:4326 | EPSG:4326 | EPSG:32719 |
| Celda | ≈ 30 m (en grados) | ≈ 90 m (en grados) | 10 m |
| Tipo | Continuo | **Conteo** | Reflectancia (continuo) |
| NoData | — | −99999 | — |

Conclusión: **ninguno** se puede combinar directamente con otro.

### Paso 2 · Reproyectar el DEM a UTM con celda de 30 m

1. **Ráster ▸ Proyecciones ▸ Combar (reproyectar)** (*Warp*).
2. **SRC de destino:** EPSG:32719 · **Método de remuestreo:** *Bilineal* · **Resolución de salida:** 30 · marca **Usar píxeles alineados al objetivo** (`-tap`).
3. Salida: `datos/trabajo/raster/dem_utm_30m.tif`.
4. Verifica: celda exactamente 30 × 30 m; elevaciones entre ~2 530 y ~4 560 m (como el original).

!!! captura "Captura pendiente · 3.8-04"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-03/3-8/3-8-04-warp.png`
    - **Qué mostrar:** El diálogo Combar (reproyectar) con SRC de destino, remuestreo bilineal, resolución 30 m y píxeles alineados.

### Paso 3 · Reproyectar la población conservando el total

1. **Combar (reproyectar)** `poblacion_worldpop_2020.tif` · EPSG:32719 · **Resolución:** 100 · **Remuestreo:** *Suma* · **NoData de destino:** −99999.
2. Verifica el total con **Procesos ▸ Estadísticas de capa ráster** (*suma*): debe ser **1 145 726**, igual que el original.
3. Repite a 30 m con *vecino más cercano* y comprueba cómo se multiplica el total. **Borra ese archivo**: es un error didáctico.

!!! captura "Captura pendiente · 3.8-06"

    - **Tipo:** PNG comparativo
    - **Archivo:** `assets/images/modulo-03/3-8/3-8-06-remuestreo-conteo.png`
    - **Qué mostrar:** Estadísticas del ráster de población original, reproyectado con suma y reproyectado con vecino más cercano a 30 m.

### Paso 4 · Recortar por el municipio

**Ráster ▸ Extracción ▸ Cortar ráster por capa de máscara** · **Máscara:** `limite_municipal` · marca **Ajustar la extensión a la máscara** y **Mantener la resolución de la entrada**. Aplica al DEM en UTM → `dem_municipio.tif`.

### Paso 5 · NDVI con la calculadora ráster

1. **Ráster ▸ Calculadora ráster**.
2. Expresión (bandas 4 = infrarrojo cercano, 3 = rojo):

    ```text
    ("sentinel2_2025-07-16@4" - "sentinel2_2025-07-16@3") / ("sentinel2_2025-07-16@4" + "sentinel2_2025-07-16@3")
    ```

3. Salida: `ndvi_2025-07-16.tif` (**Float32**).
4. Simbolízalo con *pseudocolor*, rampa *RdYlGn*, de −0,2 a 0,8. Mediana del área: **≈ 0,20**; un **28 %** de las celdas supera 0,3.

!!! captura "Captura pendiente · 3.8-08"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-8/3-8-08-calculadora-ndvi.gif`
    - **Qué mostrar:** Escribir la expresión del NDVI en la calculadora ráster y simbolizar el resultado con pseudocolor.

!!! warning "Enteros y división"

    Las bandas de Sentinel-2 son **UInt16**. En algunas herramientas, dividir dos enteros devuelve un entero (0 o 1). Asegúrate de que la salida sea **Float32**.

### Paso 6 · Alinear para combinar

Para combinar el DEM (30 m) con el NDVI (10 m), deben compartir grilla. **Ráster ▸ Alinear ráster**: elige el DEM como **referencia**, agrega el NDVI con remuestreo **promedio** y genera `ndvi_30m_alineado.tif`. Ahora sí: ambos tienen el mismo SRC, celda, origen y extensión.

---

## Inténtalo tú

!!! example "Reto 3.8 · Máscara de terreno urbanizable"

    Construye `mascara_apta.tif` (1 = apto, 0 = no apto) donde se cumplan **a la vez**:

    - pendiente **menor de 15 %** (calcúlala con **Ráster ▸ Análisis ▸ Pendiente** sobre el DEM en UTM, en porcentaje; lo verás a fondo en [3.9](09-relieve-estadisticas-zonales.md));
    - NDVI **menor de 0,3** (sin vegetación densa);
    - elevación **menor de 2 800 m**.

    Documenta cada paso de preparación (SRC, celda, alineación, remuestreo) en una tabla y responde: ¿qué porcentaje del municipio es apto? ¿Dónde se concentra?

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Compatibilidad | La ficha identifica las incompatibilidades de los tres ráster |
| DEM | En EPSG:32719, celda 30 m alineada, valores conservados |
| Población | Reproyectada con **suma**: total 1 145 726 sin cambios |
| NDVI | Float32, rango entre −1 y 1, mediana ≈ 0,2 |
| Máscara | Solo 0 y 1, misma grilla que el DEM, proceso documentado |

### Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| La población total cambia | Remuestreo inadecuado para conteos | Usa *suma* o trabaja con densidades |
| NDVI con solo 0 y 1 | División entera | Salida Float32 |
| La calculadora no deja combinar | Grillas distintas | **Alinear ráster** antes |
| Bordes con valores raros | NoData no declarado | Declara NoData en origen y destino |
| Categorías con decimales tras reproyectar | Bilineal sobre datos categóricos | Vecino más cercano |

---

## Comprueba lo aprendido

??? question "1. ¿Qué método de remuestreo usarías para un mapa de uso del suelo? ¿Y para un DEM?"

    Uso del suelo: **vecino más cercano** (categorías). DEM: **bilineal** o cúbico (continuo).

??? question "2. ¿Por qué el total de población se multiplicó por casi 10 al pasar a 30 m con vecino más cercano?"

    Porque cada celda de ~90 m se dividió en ~9 celdas de 30 m y **cada una copió el valor completo**: la misma población se contó nueve veces.

??? question "3. ¿Qué significa que dos ráster estén alineados?"

    Que comparten **SRC, tamaño de celda y origen** de la grilla: cada celda de uno coincide exactamente con una del otro.

??? question "4. ¿Qué devuelve `(\"pendiente@1\" < 15) * (\"ndvi@1\" < 0.3)`?"

    1 donde se cumplen **ambas** condiciones y 0 en el resto.

??? question "5. Repaso de 1.9 · ¿Mejora la información del DEM si lo remuestreas de 30 a 5 m?"

    No. Aumentas el número de celdas, no el detalle real: es **falsa resolución**.

---

## Tu proyecto

Guarda la máscara de terreno apto: en [3.12](12-laboratorio-decision-territorial.md) la combinarás con las zonas sin cobertura para proponer ubicaciones para un nuevo centro de salud.

---

## Referencias

- Tomlin, C. D. (1990). *Geographic Information Systems and Cartographic Modeling*. Prentice Hall.
- Tucker, C. J. (1979). Red and photographic infrared linear combinations for monitoring vegetation. *Remote Sensing of Environment, 8*(2), 127–150. <https://doi.org/10.1016/0034-4257(79)90013-0>
- Tatem, A. J. (2017). WorldPop, open data for spatial demography. *Scientific Data, 4*, 170004. <https://doi.org/10.1038/sdata.2017.4>
- GDAL. (s. f.). *gdalwarp: métodos de remuestreo*. <https://gdal.org/en/stable/programs/gdalwarp.html>
- QGIS Project. (s. f.). *Manual de usuario: Calculadora ráster*. <https://docs.qgis.org/latest/es/docs/user_manual/working_with_raster/raster_analysis.html#raster-calculator>
