---
title: 2.7 Leer los datos antes de utilizarlos
description: Lectura y control básico de calidad de atributos en QGIS; tabla de atributos, identificación, estadísticas, valores nulos, identificadores y detección de registros incompletos o sospechosos.
---

# 2.7 Leer los datos antes de utilizarlos

Quieres saber cuántas camas de salud hay por comuna y sumas el campo `Capacidad`. QGIS no te deja: el campo es **texto**, porque entre los números hay `S/D`. Cuando lo arreglas, descubres que 161 establecimientos tienen capacidad **0**: ¿son establecimientos sin camas o es otra forma de decir «no sé»? Antes de analizar, hay que **leer** la tabla como lo haría un auditor.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Recorrer la tabla de atributos y conectar filas con entidades del mapa.
    - Usar **Resumen estadístico** para detectar mínimos, máximos y valores raros.
    - Distinguir `NULL`, cero, texto vacío y códigos como `S/D`.
    - Revisar identificadores, categorías y coherencia entre campos.
    - Construir una **matriz de control** sin corregir todavía nada.

    **Tiempo:** 90 min (25 de lectura · 65 de práctica) · **Datos:** la capa de `equipamientos_errores.csv` (de [2.5](05-tablas-coordenadas.md)) y `limites.gpkg ▸ zonas_analisis` · **Producto:** `documentos/control_calidad_equipamientos.csv`.

---

## Idea central

### Cuatro dimensiones de calidad de los atributos

| Dimensión | Pregunta | Ejemplo en el caso |
|---|---|---|
| **Completitud** | ¿Están los valores obligatorios? | 104 establecimientos sin `nombre` |
| **Validez** | ¿Respetan su dominio, rango y formato? | `Capacidad` = `S/D` en un campo numérico |
| **Consistencia** | ¿Se escribe igual lo que es igual? | `salud`, `SALUD`, `Salud ` |
| **Unicidad** | ¿Lo que debe ser único lo es? | Filas duplicadas, códigos repetidos |

Son las mismas dimensiones de la norma ISO 19157 que viste en [1.13](../modulo-01/13-calidad-informacion.md), aplicadas a la tabla.

### Cuatro formas de «no hay dato»

| Valor | Qué significa | Cómo se comporta |
|---|---|---|
| `NULL` | Ausencia de valor | Se excluye de sumas y promedios |
| `0` | Un número: cero | **Entra** en sumas y promedios |
| `""` (texto vacío) | Un texto sin caracteres | No es `NULL`: no aparece con `IS NULL` |
| `S/D`, `N/A`, `-`, `-9999` | Un **código** que alguien eligió | Rompe los tipos numéricos y debe documentarse |

!!! danger "Cero no es «no sé»"

    Si 161 establecimientos tienen capacidad 0 porque nadie la midió, el promedio de camas por establecimiento quedará **muy por debajo** de la realidad. Antes de calcular, averigua qué significa cada 0.

### Sospechoso no es incorrecto

Un valor **sospechoso** (una zona con 7 841 habitantes por km²) merece revisión; un valor **incorrecto** es el que se confirmó erróneo con evidencia. Los extremos existen: el centro de Cochabamba es denso. **Detecta, documenta y verifica antes de corregir.**

---

## Hazlo conmigo

### Paso 1 · Recorrer la tabla

1. Abre la tabla de atributos de la capa importada de `equipamientos_errores.csv` (++f6++).
2. Haz clic en el encabezado **Nombre del establecimiento** para ordenarla: los vacíos aparecen juntos al principio.
3. Selecciona una fila y usa **Acercar el mapa a las filas seleccionadas** (++ctrl+j++). Repite al revés: con **Identificar** (++ctrl+shift+i++), haz clic en un punto y localiza su fila.

!!! captura "Captura pendiente · 2.7-02"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-7/2-7-02-tabla-atributos.png`
    - **Qué mostrar:** La tabla de atributos de equipamientos con encabezados, filas seleccionadas, botón de zoom a la selección y conteo de entidades visibles.

!!! tip "Mostrar solo lo que te interesa"

    En la esquina inferior izquierda de la tabla, cambia **Mostrar todos los objetos** por **Mostrar objetos seleccionados** o **Mostrar objetos visibles en el mapa**.

### Paso 2 · Escribir un diccionario mínimo

Un nombre de campo no explica su contenido. Antes de calcular, anota:

| Campo | Tipo en QGIS | Qué representa | Unidad | ¿Obligatorio? | Valores válidos |
|---|---|---|---|---|---|
| `Código` | Texto | Identificador del establecimiento | — | Sí | `EQ-` + 4 dígitos, único |
| `Tipo` | Texto | Sector | — | Sí | `salud`, `educacion` |
| `Capacidad` | **Texto** (¿por qué?) | Camas o plazas | camas / alumnos | No | Entero > 0 |

### Paso 3 · Estadísticas para conocer los datos

1. Abre **Ver ▸ Paneles ▸ Resumen estadístico**.
2. Elige la capa **Zonas de análisis** y el campo `pob_2020`.
3. Anota: recuento (327), mínimo (0), máximo (7 841), mediana (≈ 497) y número de ceros.

!!! captura "Captura pendiente · 2.7-04"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-7/2-7-04-resumen-estadistico.png`
    - **Qué mostrar:** Panel **Resumen estadístico** analizando `pob_2020` de las zonas de análisis.

??? question "125 zonas tienen población 0. ¿Es un error?"

    No necesariamente. Muchas zonas están en la cordillera del Tunari o en el sur no urbanizado. WorldPop asigna 0 donde no detecta edificaciones. Compruébalo: selecciónalas con la expresión `"pob_2020" = 0` y mira dónde están.

Ahora elige la capa de equipamientos y el campo `Capacidad`. El panel solo ofrece **recuento, únicos, vacíos…**: no calcula media porque el campo es **texto**.

### Paso 4 · Revisar valores únicos

En **Resumen estadístico**, con el campo `Tipo`, mira **Valores únicos**: aparecen **6** en lugar de 2. Para verlos todos: **Propiedades ▸ Simbología ▸ Categorizado ▸ Clasificar**, o en la tabla, **Ordenar** por ese campo.

!!! captura "Captura pendiente · 2.7-05"

    - **Tipo:** Imagen (PNG) comparativa
    - **Archivo:** `assets/images/modulo-02/2-7/2-7-05-categorias-inconsistentes.png`
    - **Qué mostrar:** El campo `Tipo` con las grafías `salud`, `SALUD`, `Salud `, `educacion`, `EDUCACION`, `Educacion ` en una simbología categorizada.

!!! warning "Un espacio al final también es otra categoría"

    `Salud` y `Salud ` (con espacio) son textos distintos para cualquier programa. Se ven iguales en pantalla; por eso hay que contarlos.

### Paso 5 · Seleccionar para investigar

Abre **Seleccionar por expresión** (++ctrl+f3++) y prueba, una por una, contando cuántas entidades selecciona cada una:

```sql
"Nombre del establecimiento" IS NULL OR trim("Nombre del establecimiento") = ''
"Capacidad" IN ('S/D', '0', '') OR "Capacidad" IS NULL
lower(trim("Tipo")) NOT IN ('salud', 'educacion')
```

La selección **no modifica** los datos: es tu lupa. Las expresiones las estudiarás a fondo en [2.8](08-seleccionar-filtrar.md).

---

## Inténtalo tú

!!! example "Reto 2.7 · Matriz de control de calidad"

    Crea `documentos/control_calidad_equipamientos.csv` con una fila por problema detectado:

    | control | dimensión | campo | expresión o método | registros afectados | ejemplo | gravedad | acción propuesta |
    |---|---|---|---|---|---|---|---|
    | Nombre faltante | Completitud | Nombre del establecimiento | `IS NULL OR trim(...) = ''` | 104 | EQ-0001 | Media | Completar desde OSM o terreno |

    Incluye al menos: nombres faltantes, capacidad con códigos, capacidad 0, grafías de `Tipo`, filas duplicadas y coordenadas faltantes. **No corrijas nada**: la corrección es parte de [3.1](../modulo-03/01-preparar-datos-confiables.md).

    **Pregunta final:** ¿podrías calcular hoy «capacidad total de salud por comuna»? Justifica en tres líneas.

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Completitud | Encontraste los 104 nombres faltantes y los 3 registros sin coordenadas |
| Validez | Distinguiste `S/D` (164), `0` (161) y vacío (171) en `Capacidad` |
| Consistencia | Contaste las 6 grafías de `Tipo` |
| Unicidad | Encontraste las 4 filas duplicadas |
| Método | Cada fila de la matriz tiene expresión, conteo y ejemplo verificable |
| Juicio | Concluyes que la capacidad **no** es confiable para calcular hoy |

### Errores frecuentes

| Síntoma | Causa probable | Qué revisar |
|---|---|---|
| No puedo sumar un campo «numérico» | Es texto | Tipo del campo y códigos especiales |
| `IS NULL` no encuentra los vacíos | Son textos vacíos, no `NULL` | Añadir `OR "campo" = ''` |
| La media parece muy baja | Ceros que significan «sin dato» | Distribución y significado del 0 |
| Aparecen más categorías de las esperadas | Mayúsculas, tildes o espacios | `lower(trim("campo"))` |
| Un máximo enorme | Valor extremo real o error de unidades | Verificar el registro concreto |

---

## Comprueba lo aprendido

??? question "1. ¿Por qué `NULL` no es lo mismo que `0`?"

    `NULL` es ausencia de valor y se excluye de los cálculos; `0` es un número y entra en sumas y promedios.

??? question "2. ¿Por qué un nombre no suele ser un buen identificador?"

    Porque puede repetirse, cambiar o escribirse de varias formas. Un identificador debe ser **único, estable** y con formato fijo.

??? question "3. El máximo de un campo es mucho mayor que el resto. ¿Lo eliminas?"

    No. Primero verifica: puede ser un valor extremo real. Solo se corrige lo que se **confirma** como erróneo.

??? question "4. ¿Por qué no conviene mezclar detección y corrección?"

    Porque perderías la evidencia de qué estaba mal y por qué lo cambiaste. Primero se documenta; luego se corrige sobre una copia.

??? question "5. Un establecimiento está `CERRADO` pero tiene capacidad 300. ¿Qué dimensión falla?"

    La **coherencia lógica** entre campos. Hay que decidir si el estado o la capacidad está desactualizado.

??? question "6. Repaso de 1.13 · ¿Qué es la aptitud para el uso?"

    Que un dato es de buena calidad **para un propósito concreto**: la misma capa puede servir para un mapa de ubicación y no para calcular camas por habitante.

---

## Tu proyecto

Repite el control con la capa **limpia** `datos/trabajo/equipamientos.gpkg` (de [2.5](05-tablas-coordenadas.md)). ¿Qué problemas persisten aunque las coordenadas estén bien? Anótalos en tu `LEEME.txt` como **limitaciones conocidas** del caso conductor: tendrás que mencionarlas en el informe final.

---

## Referencias

- International Organization for Standardization. (2013). *ISO 19157:2013 Geographic information — Data quality*. ISO.
- Wickham, H. (2014). Tidy data. *Journal of Statistical Software, 59*(10), 1–23. <https://doi.org/10.18637/jss.v059.i10>
- Devillers, R., & Jeansoulin, R. (Eds.). (2006). *Fundamentals of Spatial Data Quality*. ISTE.
- QGIS Project. (s. f.). *Manual de usuario: Trabajar con la tabla de atributos*. <https://docs.qgis.org/latest/es/docs/user_manual/working_with_vector/attribute_table.html>
- QGIS Project. (s. f.). *Manual de usuario: Panel de resumen estadístico*. <https://docs.qgis.org/latest/es/docs/user_manual/introduction/general_tools.html#statistical-summary-panel>
