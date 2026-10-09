---
title: 3.7 Analizar proximidad y superposición
description: Análisis territorial mediante buffer, recorte, intersección, diferencia y disolución, controlando unidades, parámetros, geometrías y atributos resultantes en QGIS.
---

# 3.7 Analizar proximidad y superposición

Contar establecimientos por comuna (3.6) mostraba desigualdad, pero no respondía la pregunta del caso conductor: **¿quién vive lejos de un servicio de salud?** Aquí trazas un radio de 1 km alrededor de cada uno de los 173 establecimientos, lo superpones a las zonas de población y obtienes la respuesta: unas **90 000 personas —el 15 % de la población— viven en zonas a más de 1 km** de cualquier establecimiento de salud. Y casi todas están en el sur y en los bordes de la ciudad.

![Zonas habitadas según su distancia a un establecimiento de salud](../assets/images/mapas/3-7-cobertura-salud.png){ loading=lazy }

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Crear **áreas de influencia** (*buffer*) con las unidades correctas.
    - Combinar capas con **recortar, intersección, diferencia** y **disolver**.
    - Controlar qué pasa con los **atributos** en cada operación.
    - Cuantificar población cubierta y no cubierta.
    - Reconocer las limitaciones de la distancia en línea recta.

    **Tiempo:** 2 h (30 min de lectura · 90 de práctica) · **Datos:** `equipamientos` auditado, `zonas_analisis`, `comunas`, `vias.gpkg` · **Producto:** `datos/trabajo/cobertura.gpkg` y una tabla de población sin cobertura por comuna.

---

## Idea central

### Cinco operaciones, cinco preguntas

| Operación | Pregunta | Geometría resultante | Atributos |
|---|---|---|---|
| **Buffer** | ¿Qué está a menos de *d* metros? | Polígonos alrededor de cada entidad | Los de la entidad de origen |
| **Disolver** | ¿Cuál es el área total cubierta, sin superposiciones? | Unión de polígonos | Se pierden (o se agrupan por un campo) |
| **Recortar** (*clip*) | ¿Qué parte de A cae dentro de B? | Partes de A | Solo los de A |
| **Intersección** | ¿Dónde coinciden A y B? | Partes comunes | Los de A **y** B |
| **Diferencia** | ¿Qué parte de A queda **fuera** de B? | Partes de A | Solo los de A |

!!! captura "Captura pendiente · 3.7-01"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-03/3-7/3-7-01-operaciones-superposicion.png`
    - **Qué mostrar:** Diagrama de buffer, disolver, recortar, intersección y diferencia con dos capas simples.

!!! danger "Las unidades del buffer son las del SRC de la capa"

    Un buffer de **1000** sobre una capa en EPSG:4326 son **1000 grados**: cubre el planeta. Trabaja siempre con capas en un **SRC proyectado en metros** (EPSG:32719) antes de calcular distancias ([2.6](../modulo-02/06-problemas-coordenadas.md)).

### La línea recta es una simplificación

Un buffer mide distancia **euclidiana**: «a vuelo de pájaro». Una persona camina por calles, cruza un río por un puente y sube una ladera. 1 km en línea recta pueden ser 1,5 km reales o más. El buffer sirve como **primera aproximación**; el análisis de redes (fuera del alcance de este curso) mide el recorrido real.

### ¿Qué zona está «cubierta»?

Decide una regla y documéntala: una zona está cubierta si **su punto interior** (`point_on_surface`) está a menos de 1 km de un establecimiento. Otra regla posible: si más del 50 % de su superficie lo está. Cada regla da números ligeramente distintos.

---

## Hazlo conmigo

### Paso 1 · Buffer de 1 km alrededor de los establecimientos de salud

1. Filtra `equipamientos` con `"tipo" = 'salud'` (173 entidades) y comprueba que el SRC es **EPSG:32719**.
2. **Procesos ▸ Buffer** · **Distancia:** 1000 m · **Segmentos:** 16 · **Disolver resultado:** sí.
3. Guarda como `datos/trabajo/cobertura.gpkg ▸ salud_1km`.

!!! captura "Captura pendiente · 3.7-03"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-03/3-7/3-7-03-buffer.png`
    - **Qué mostrar:** El diálogo de Buffer con la distancia en metros, los segmentos y la opción Disolver resultado.

!!! tip "Disolver o no disolver"

    Sin disolver obtienes 173 círculos superpuestos (útil para saber **cuántos** establecimientos cubren cada lugar). Disuelto obtienes **un** polígono con el área total cubierta (útil para calcular superficies sin contar dos veces).

### Paso 2 · Recortar al municipio

Los círculos se salen del municipio. **Procesos ▸ Cortar** (*clip*) · **Entrada:** `salud_1km` · **Superposición:** `limite_municipal`. Calcula su superficie (`$area / 1e6`) y compárala con la del municipio: el área cubierta es **≈ 38,6 %** del municipio (gran parte del resto es cordillera y zonas no urbanizadas).

### Paso 3 · Zonas cubiertas y no cubiertas

1. En `zonas_analisis` (exportada a `cobertura.gpkg ▸ zonas`), crea el campo `cubierta` (booleano):

    ```sql
    intersects(point_on_surface($geometry), aggregate('salud_1km', 'collect', $geometry))
    ```

    La expresión toma un punto interior de cada zona y comprueba si cae dentro del área de 1 km (`salud_1km` debe llamarse así en el panel Capas).

2. Selecciona las zonas habitadas no cubiertas: `"pob_2020" > 0 AND NOT "cubierta"` → **83** zonas.
3. **Resumen estadístico** de `pob_2020` sobre la selección: **suma ≈ 90 073** habitantes (**15 %** de 602 197).

!!! captura "Captura pendiente · 3.7-06"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-7/3-7-06-zonas-no-cubiertas.gif`
    - **Qué mostrar:** Seleccionar las zonas habitadas no cubiertas y leer la suma de población en el Resumen estadístico.

### Paso 4 · Intersección: ¿qué comunas tienen la población descubierta?

**Procesos ▸ Intersección** entre las zonas no cubiertas y `Comunas` (para heredar el nombre), y luego **Estadísticas por categorías** (campo `nombre`, suma de `pob_2020`). Completa:

| Comuna | Población sin cobertura | % de su población |
|---|---|---|
| Itocta | 49 714 | 41,3 % |
| Alejo Calatayud | 20 102 | 17,7 % |
| Tunari | 12 881 | 14,0 % |
| Valle Hermoso | 7 376 | 11,8 % |
| Adela Zamudio, Molle | 0 | 0 % |

Más de la mitad de la población sin cobertura vive en **Itocta**, la comuna del sur.

### Paso 5 · Diferencia: dónde no llega el servicio

**Procesos ▸ Diferencia** · **Entrada:** `limite_municipal` · **Superposición:** `salud_1km`. El resultado es el territorio **fuera** de 1 km de cualquier establecimiento. Superponlo a la imagen Sentinel-2: ¿es territorio urbanizado o cerro?

??? info "Para saber más · buffers múltiples"

    **Procesos ▸ Buffer de anillos múltiples** crea anillos a 500, 1000 y 2000 m en una sola operación: útil para clasificar la población por **bandas de distancia** en lugar de «dentro / fuera».

---

## Inténtalo tú

!!! example "Reto 3.7 · Sensibilidad del resultado"

    El 15 % depende de **dos decisiones**: la distancia (1 km) y qué cuenta como establecimiento de salud. Recalcula la población sin cobertura en cuatro escenarios:

    | Escenario | Establecimientos | Distancia | Población sin cobertura | % |
    |---|---|---|---|---|
    | A (base) | Todos los de salud (173) | 1 000 m | ≈ 90 073 | 15,0 |
    | B | Solo hospitales y clínicas | 1 000 m | | |
    | C | Todos | 500 m | | |
    | D | Solo hospitales | 2 000 m | | |

    Escribe un párrafo: ¿qué escenario usarías para un informe al municipio y por qué? ¿Cómo comunicarías que el resultado **depende de supuestos**?

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Unidades | Todos los buffers se calcularon en EPSG:32719 |
| Resultado base | 83 zonas habitadas sin cobertura; ≈ 90 000 habitantes (15 %) |
| Operaciones | Usaste recortar, intersección y diferencia según la pregunta |
| Atributos | Explicas qué atributos conserva cada operación |
| Sensibilidad | Escenarios: B ≈ 109 000 (18 %); C ≈ 324 000 (54 %); D ≈ 179 000 (30 %) |
| Limitación | Mencionas que la distancia euclidiana subestima el recorrido real |

### Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| El buffer cubre medio mundo | Capa en grados | Reproyecta a 32719 |
| La suma de población es mayor que el total | Zonas contadas varias veces por buffers sin disolver | Disuelve o usa una regla por zona |
| La intersección no tiene los atributos esperados | Elegiste recortar o diferencia | Usa intersección |
| Geometrías no válidas tras la operación | Polígonos de entrada inválidos | **Corregir geometrías** antes |
| Muy lento | Muchos segmentos o sin índice espacial | Reduce segmentos; crea índice espacial |

---

## Comprueba lo aprendido

??? question "1. ¿Qué diferencia hay entre recortar e intersección?"

    Ambas devuelven la parte común, pero **recortar** conserva solo los atributos de la capa de entrada; **intersección**, los de ambas.

??? question "2. ¿Por qué disolver el buffer antes de calcular el área cubierta?"

    Porque los círculos superpuestos sumarían varias veces la misma superficie.

??? question "3. ¿Qué limitación tiene un buffer para medir accesibilidad?"

    Mide línea recta, no el recorrido real por calles, puentes y pendientes.

??? question "4. ¿Por qué el resultado «15 % sin cobertura» debe ir acompañado de sus supuestos?"

    Porque cambia con la distancia elegida, la definición de establecimiento, la regla de cobertura y la calidad de los datos.

??? question "5. Repaso de 1.13 · ¿Cómo se propaga aquí el error de los datos de entrada?"

    Un establecimiento omitido en OSM deja «descubierta» una zona que no lo está; una población sobreestimada infla el número de personas sin cobertura.

---

## Tu proyecto

Este es el **resultado central** del caso conductor. Prepara una tabla final con la población sin cobertura por comuna en el escenario que elijas, y guarda la capa de zonas no cubiertas: es la entrada del laboratorio de decisión ([3.12](12-laboratorio-decision-territorial.md)).

---

## Referencias

- Higgs, G. (2004). A literature review of the use of GIS-based measures of access to health care services. *Health Services and Outcomes Research Methodology, 5*(2), 119–139. <https://doi.org/10.1007/s10742-005-4304-7>
- Guagliardo, M. F. (2004). Spatial accessibility of primary care: Concepts, methods and challenges. *International Journal of Health Geographics, 3*, 3. <https://doi.org/10.1186/1476-072X-3-3>
- de Smith, M. J., Goodchild, M. F., & Longley, P. A. (2018). *Geospatial Analysis* (6.ª ed., cap. 4: Building blocks of spatial analysis). <https://www.spatialanalysisonline.com>
- QGIS Project. (s. f.). *Algoritmos de Procesos: Superposición de vectores*. <https://docs.qgis.org/latest/es/docs/user_manual/processing_algs/qgis/vectoroverlay.html>
- QGIS Project. (s. f.). *Algoritmos de Procesos: Geometría de vectores (Buffer, Disolver)*. <https://docs.qgis.org/latest/es/docs/user_manual/processing_algs/qgis/vectorgeometry.html>
