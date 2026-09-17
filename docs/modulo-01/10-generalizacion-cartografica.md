---
title: 1.10 Generalización cartográfica
description: Qué es la generalización, por qué es necesaria, operaciones de selección, simplificación, agregación, desplazamiento, exageración y clasificación, y sus consecuencias al usar datos en un SIG.
---

# 1.10 Generalización cartográfica

!!! abstract "Objetivos de aprendizaje"

    Al finalizar este tema, el estudiante será capaz de:

    - Explicar qué es la generalización cartográfica y por qué es inevitable al reducir la escala.
    - Describir las operaciones de selección, simplificación, agregación, desplazamiento, exageración y clasificación.
    - Comprender el funcionamiento básico de un algoritmo de simplificación de líneas.
    - Relacionar la generalización con la escala y el nivel de detalle.
    - Reconocer las consecuencias de usar datos generalizados en análisis espaciales.
    - Explicar por qué los datos no deben usarse indiscriminadamente a cualquier escala.

---

## ¿Qué es la generalización?

En el tema 1.9 vimos que una ciudad puede representarse como edificios individuales, como manzanos, como una mancha urbana o como un simple punto, según la escala. El proceso que transforma una representación en otra se llama **generalización**.

!!! info "Definición"

    La **generalización cartográfica** es el proceso de **seleccionar y representar de forma simplificada** los elementos geográficos, adaptando su cantidad, forma y simbolización a la **escala** y al **propósito** del mapa.

La generalización **no es un defecto** ni un error: es una operación **necesaria e intencional**. Un mapa sin generalizar sería ilegible.

### ¿Por qué es necesaria?

Hay dos razones principales:

**1. El espacio disponible se reduce muy rápido.** Como vimos en el tema 1.8, las superficies se reducen con el cuadrado de la escala.

| Escala | Espacio que ocupa 1 km² en el mapa |
|---|---|
| 1:5 000 | 20 × 20 cm = 400 cm² |
| 1:25 000 | 4 × 4 cm = 16 cm² |
| 1:100 000 | 1 × 1 cm = 1 cm² |
| 1:1 000 000 | 1 × 1 mm = 1 mm² |

Todo lo que había en 400 cm² a escala 1:5 000 tiene que caber en **1 mm²** a escala 1:1 000 000.

**2. Los símbolos no pueden reducirse indefinidamente.** Una línea, un texto o un símbolo tienen un **tamaño mínimo** para ser legibles, sin importar la escala.

!!! example "Una vía que ocupa más que la realidad"

    Una carretera se dibuja con una línea de **0,5 mm** de grosor para que se vea bien. A escala **1:100 000**, esa línea equivale a **50 m** sobre el terreno, aunque la carretera real mida 8 m de ancho.

    Si al lado hay un río y una hilera de viviendas, sus símbolos **no caben** en su posición real: se superponen. Hay que decidir qué mostrar, qué eliminar y qué mover.

### La ley de selección de Töpfer

En 1966, los cartógrafos Friedrich Töpfer y Wolfgang Pillewizer propusieron una regla empírica para estimar **cuántos elementos** conviene conservar al reducir la escala, conocida como **ley radical** o **ley de selección**:

```text
n₂ = n₁ × √(D₁ / D₂)
```

donde **n₁** es el número de elementos en el mapa original (escala 1:D₁) y **n₂**, el número de elementos recomendado en el mapa derivado (escala 1:D₂).

!!! example "Aplicar la ley de Töpfer"

    Un mapa a escala **1:25 000** muestra **1 000 localidades**. ¿Cuántas conviene mostrar a escala **1:100 000**?

    ```text
    n₂ = 1 000 × √(25 000 / 100 000)
       = 1 000 × √0,25
       = 1 000 × 0,5
       = 500 localidades
    ```

    Es una regla **orientativa**: indica cuántos elementos conservar, pero no **cuáles**. Esa decisión depende del propósito y de la importancia de cada elemento.

---

## Generalización cartográfica y generalización de datos

En un SIG conviene distinguir dos tipos de generalización:

| Tipo | Qué se modifica | Objetivo | Ejemplo |
|---|---|---|---|
| **Cartográfica** (o gráfica) | La **representación visual** | Que el mapa sea legible a una escala | Desplazar un símbolo, ocultar etiquetas, engrosar una línea |
| **De datos** (o del modelo) | Los **datos** mismos: geometrías y atributos | Crear una versión más simple para otra escala o para agilizar un análisis | Simplificar los límites municipales, disolver manzanos en áreas urbanas |

!!! warning "La diferencia importa"

    La generalización **cartográfica** no altera los datos: solo cambia cómo se ven. La generalización **de datos** crea **nuevas geometrías** con menos información, y esa información **no se puede recuperar** después.

    **Guarda siempre los datos originales** y trabaja la versión generalizada como un archivo aparte.

---

## Operaciones de generalización

La generalización se descompone en un conjunto de **operaciones**. Los autores las clasifican de diversas formas; aquí veremos las seis más importantes.

<figure class="figura">
<svg viewBox="0 0 720 340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Operaciones de generalización: selección, simplificación, agregación, desplazamiento, exageración y clasificación">
<text x="120" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="currentColor">Selección</text>
<rect x="20" y="38" width="90" height="90" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/>
<rect x="130" y="38" width="90" height="90" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/>
<line x1="113" y1="83.0" x2="121" y2="83.0" stroke="currentColor" stroke-width="1.8"/>
<polygon points="127,83.0 120,78.0 120,88.0" fill="currentColor"/>
<text x="120" y="148" text-anchor="middle" font-size="11" fill="currentColor">Se conservan los más relevantes</text>
<circle cx="41.5" cy="96.3" r="4" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="63.5" cy="63.1" r="9" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="173.5" cy="63.1" r="9" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="86.5" cy="83.9" r="3.5" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="85.2" cy="49.0" r="7" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="195.2" cy="49.0" r="7" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="34.8" cy="103.6" r="3.5" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="94.5" cy="96.6" r="7" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="204.5" cy="96.6" r="7" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="99.8" cy="99.7" r="7" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="209.8" cy="99.7" r="7" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="73.1" cy="50.4" r="6" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="183.1" cy="50.4" r="6" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="67.8" cy="96.6" r="6" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="177.8" cy="96.6" r="6" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="31.6" cy="99.9" r="2.5" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="38.7" cy="113.0" r="9" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="148.7" cy="113.0" r="9" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="41.3" cy="99.0" r="7" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="151.3" cy="99.0" r="7" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="63.9" cy="61.1" r="2" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="62.9" cy="105.4" r="2.5" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="84.6" cy="62.6" r="2.5" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="38.6" cy="81.3" r="7" fill="#3f6fd8" fill-opacity="0.8"/>
<circle cx="148.6" cy="81.3" r="7" fill="#3f6fd8" fill-opacity="0.8"/>
<text x="360" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="currentColor">Simplificación</text>
<rect x="260" y="38" width="90" height="90" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/>
<rect x="370" y="38" width="90" height="90" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/>
<line x1="353" y1="83.0" x2="361" y2="83.0" stroke="currentColor" stroke-width="1.8"/>
<polygon points="367,83.0 360,78.0 360,88.0" fill="currentColor"/>
<text x="360" y="148" text-anchor="middle" font-size="11" fill="currentColor">Se eliminan vértices innecesarios</text>
<polygon points="332.6,83.0 340.8,86.1 342.1,89.5 338.9,92.1 337.7,94.9 336.3,97.6 332.8,99.0 333.2,102.8 325.7,100.4 320.5,98.5 318.6,99.2 319.8,104.1 319.4,107.9 316.2,107.0 314.9,110.1 313.3,113.9 311.2,118.3 307.9,116.1 305.0,119.9 301.9,118.8 299.0,117.3 297.5,111.0 296.0,107.7 294.3,106.0 290.9,107.4 291.9,101.7 288.8,102.3 287.9,100.1 286.0,98.9 282.8,98.5 274.2,100.8 271.3,98.7 272.2,94.9 269.0,92.6 269.5,89.3 269.4,86.1 271.3,83.0 278.4,80.7 276.1,77.9 278.1,75.8 281.7,74.5 279.5,71.1 281.7,69.5 281.7,66.7 282.0,63.7 278.7,56.7 283.8,57.8 286.3,56.4 286.2,50.4 289.9,50.7 294.4,54.0 296.9,52.9 301.1,60.8 303.0,60.5 305.0,60.7 307.1,59.2 309.1,59.8 311.5,58.8 315.2,55.0 320.5,49.8 324.5,49.2 326.8,51.9 327.8,55.8 327.8,60.2 332.4,60.0 329.3,66.0 330.0,68.6 324.3,74.0 325.5,75.5 331.0,76.0 332.3,78.2 335.4,80.3" fill="#2e9e5b" fill-opacity="0.3" stroke="#2e9e5b" stroke-width="1.2"/>
<polygon points="442.6,83.0 452.1,89.5 443.2,102.8 428.6,99.2 429.4,107.9 415.0,119.9 401.9,101.7 381.3,98.7 381.3,83.0 391.7,74.5 388.7,56.7 396.3,56.4 396.2,50.4 415.0,60.7 434.5,49.2 442.4,60.0 434.3,74.0" fill="#2e9e5b" fill-opacity="0.3" stroke="#2e9e5b" stroke-width="1.2"/>
<text x="600" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="currentColor">Agregación</text>
<rect x="500" y="38" width="90" height="90" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/>
<rect x="610" y="38" width="90" height="90" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/>
<line x1="593" y1="83.0" x2="601" y2="83.0" stroke="currentColor" stroke-width="1.8"/>
<polygon points="607,83.0 600,78.0 600,88.0" fill="currentColor"/>
<text x="600" y="148" text-anchor="middle" font-size="11" fill="currentColor">Elementos cercanos se unen</text>
<rect x="514.0" y="58.0" width="11.4" height="10.7" fill="currentColor" fill-opacity="0.55"/>
<rect x="514.0" y="75.0" width="11.3" height="12.4" fill="currentColor" fill-opacity="0.55"/>
<rect x="514.0" y="92.0" width="10.2" height="11.1" fill="currentColor" fill-opacity="0.55"/>
<rect x="531.0" y="58.0" width="10.1" height="12.1" fill="currentColor" fill-opacity="0.55"/>
<rect x="531.0" y="75.0" width="9.0" height="11.7" fill="currentColor" fill-opacity="0.55"/>
<rect x="531.0" y="92.0" width="12.8" height="9.1" fill="currentColor" fill-opacity="0.55"/>
<rect x="548.0" y="58.0" width="11.4" height="11.6" fill="currentColor" fill-opacity="0.55"/>
<rect x="548.0" y="75.0" width="12.4" height="11.3" fill="currentColor" fill-opacity="0.55"/>
<rect x="548.0" y="92.0" width="10.0" height="10.6" fill="currentColor" fill-opacity="0.55"/>
<rect x="565.0" y="58.0" width="12.8" height="12.6" fill="currentColor" fill-opacity="0.55"/>
<rect x="565.0" y="75.0" width="9.5" height="9.4" fill="currentColor" fill-opacity="0.55"/>
<rect x="565.0" y="92.0" width="9.4" height="9.1" fill="currentColor" fill-opacity="0.55"/>
<rect x="622" y="56" width="68" height="53" rx="6" fill="currentColor" fill-opacity="0.35" stroke="currentColor" stroke-opacity="0.6"/>
<text x="120" y="199" text-anchor="middle" font-size="14" font-weight="bold" fill="currentColor">Desplazamiento</text>
<rect x="20" y="213" width="90" height="90" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/>
<rect x="130" y="213" width="90" height="90" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/>
<line x1="113" y1="258.0" x2="121" y2="258.0" stroke="currentColor" stroke-width="1.8"/>
<polygon points="127,258.0 120,253.0 120,263.0" fill="currentColor"/>
<text x="120" y="323" text-anchor="middle" font-size="11" fill="currentColor">Se separan símbolos superpuestos</text>
<path d="M 20 255 C 50 249, 80 263, 110 255" fill="none" stroke="#8a8a8a" stroke-width="5"/>
<path d="M 20 263 C 50 257, 80 269, 110 263" fill="none" stroke="#3f6fd8" stroke-width="4"/>
<path d="M 130 241 C 160 235, 190 249, 220 241" fill="none" stroke="#8a8a8a" stroke-width="5"/>
<path d="M 130 279 C 160 273, 190 285, 220 279" fill="none" stroke="#3f6fd8" stroke-width="4"/>
<rect x="60" y="251" width="12" height="12" fill="#e0823d" stroke="#000" stroke-width="0.8"/>
<rect x="170" y="255" width="12" height="12" fill="#e0823d" stroke="#000" stroke-width="0.8"/>
<text x="360" y="199" text-anchor="middle" font-size="14" font-weight="bold" fill="currentColor">Exageración</text>
<rect x="260" y="213" width="90" height="90" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/>
<rect x="370" y="213" width="90" height="90" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/>
<line x1="353" y1="258.0" x2="361" y2="258.0" stroke="currentColor" stroke-width="1.8"/>
<polygon points="367,258.0 360,253.0 360,263.0" fill="currentColor"/>
<text x="360" y="323" text-anchor="middle" font-size="11" fill="currentColor">Se amplía lo importante</text>
<polygon points="260.0,213.0 315.0,213.0 305.0,243.0 320.0,268.0 300.0,303.0 260.0,303.0" fill="#2e9e5b" fill-opacity="0.3" stroke="none"/>
<circle cx="334" cy="248" r="1.6" fill="#2e9e5b" fill-opacity="0.8"/>
<path d="M 280 303 C 285 273, 270 253, 290 223" fill="none" stroke="#3f6fd8" stroke-width="1"/>
<polygon points="370.0,213.0 425.0,213.0 415.0,243.0 430.0,268.0 410.0,303.0 370.0,303.0" fill="#2e9e5b" fill-opacity="0.3" stroke="none"/>
<circle cx="444" cy="248" r="5" fill="#2e9e5b" fill-opacity="0.8"/>
<path d="M 390 303 C 395 273, 380 253, 400 223" fill="none" stroke="#3f6fd8" stroke-width="3.5"/>
<text x="600" y="199" text-anchor="middle" font-size="14" font-weight="bold" fill="currentColor">Clasificación</text>
<rect x="500" y="213" width="90" height="90" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/>
<rect x="610" y="213" width="90" height="90" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/>
<line x1="593" y1="258.0" x2="601" y2="258.0" stroke="currentColor" stroke-width="1.8"/>
<polygon points="607,258.0 600,253.0 600,263.0" fill="currentColor"/>
<text x="600" y="323" text-anchor="middle" font-size="11" fill="currentColor">Se agrupan categorías similares</text>
<rect x="500" y="213" width="30" height="30" fill="#e6550d" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="610" y="213" width="30" height="30" fill="#e6550d" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="530" y="213" width="30" height="30" fill="#fc8d62" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="640" y="213" width="30" height="30" fill="#e6550d" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="560" y="213" width="30" height="30" fill="#d95f02" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="670" y="213" width="30" height="30" fill="#e6550d" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="500" y="243" width="30" height="30" fill="#66c2a5" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="610" y="243" width="30" height="30" fill="#2ca25f" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="530" y="243" width="30" height="30" fill="#6a51a3" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="640" y="243" width="30" height="30" fill="#6a51a3" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="560" y="243" width="30" height="30" fill="#7570b3" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="670" y="243" width="30" height="30" fill="#6a51a3" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="500" y="273" width="30" height="30" fill="#1b9e77" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="610" y="273" width="30" height="30" fill="#2ca25f" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="530" y="273" width="30" height="30" fill="#2ca25f" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="640" y="273" width="30" height="30" fill="#2ca25f" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="560" y="273" width="30" height="30" fill="#8da0cb" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
<rect x="670" y="273" width="30" height="30" fill="#6a51a3" fill-opacity="0.85" stroke="#fff" stroke-width="1"/>
</svg><figcaption>Las seis operaciones principales de generalización. Cada par muestra el antes y el después.</figcaption>
</figure>

### Selección

Consiste en **decidir qué elementos se representan** y cuáles se omiten.

- Es la **primera** y más importante operación de generalización.
- Se basa en criterios de **tamaño**, **importancia** o **relevancia para el tema**.
- Ejemplos: mostrar solo los ríos permanentes, las localidades con más de 2 000 habitantes o las vías pavimentadas.

!!! note "Selección no es lo mismo que olvido"

    Omitir un elemento debe ser una **decisión consciente y justificada**. Un mapa de acceso a servicios de salud que omite los caminos vecinales, por ser "secundarios", puede ocultar precisamente la información que el mapa necesitaba mostrar.

### Simplificación

Consiste en **reducir la cantidad de vértices** de líneas y contornos, eliminando los detalles que no se perciben a la escala de destino, pero **conservando la forma esencial**.

- Se aplica a ríos, costas, límites, curvas de nivel y contornos de polígonos.
- Reduce el tamaño de los archivos y acelera la visualización y el análisis.
- Relacionada con ella está el **suavizado**, que no elimina vértices sino que redondea los ángulos para dar un aspecto más natural.

La veremos en detalle más adelante.

### Agregación

Consiste en **unir varios elementos cercanos** en uno solo, generalmente de mayor tamaño o de otra categoría.

- Edificios individuales que se convierten en un **manzano**.
- Manzanos que se convierten en una **área urbana**.
- Pequeñas parcelas de cultivo que se convierten en una **zona agrícola**.
- Varios puntos muy próximos que se reemplazan por un único símbolo.

Una variante es el **colapso**: un elemento cambia a una geometría de menor dimensión. Por ejemplo, una ciudad que pasa de **polígono a punto**, o un río que pasa de **polígono a línea**.

### Desplazamiento

Consiste en **mover ligeramente** los símbolos que se superponen o están demasiado cerca, para que se puedan distinguir.

- Separar una vía, un río y una línea férrea que corren paralelos por un valle angosto.
- Alejar el símbolo de una escuela para que no quede encima de la vía.

!!! danger "El desplazamiento sacrifica exactitud posicional"

    Un elemento desplazado **ya no está en su posición real**. Es aceptable en un mapa, porque mejora la legibilidad, pero **no se deben medir distancias** ni hacer análisis de proximidad sobre elementos desplazados.

### Exageración

Consiste en **ampliar** o **realzar** elementos que, por su tamaño real, desaparecerían a la escala del mapa, pero que son **importantes** para el propósito.

- Un puente, un paso de montaña o una estrecha quebrada que es el único acceso a una comunidad.
- Una pequeña isla o una laguna que sirve de referencia.
- Una curva muy cerrada de un camino, que se dibuja más abierta para que se perciba.

La exageración, como el desplazamiento, **distorsiona intencionalmente** la geometría en favor de la comunicación.

### Clasificación

Consiste en **agrupar elementos con características similares** en una misma categoría, reduciendo el detalle **temático**.

- Uso de suelo en 40 subclases que se reagrupa en 6 clases.
- Vías clasificadas en 10 tipos que se simplifican en principales y secundarias.
- Valores continuos (pendiente en grados) agrupados en rangos (plana, moderada, escarpada).

Es la generalización del **nivel de detalle temático** que vimos en el tema 1.9.

### Resumen de operaciones

| Operación | Qué modifica | Afecta la exactitud posicional | Herramientas en QGIS |
|---|---|---|---|
| **Selección** | Cantidad de elementos | No | Filtros, selección por expresión, extracción por atributos |
| **Simplificación** | Cantidad de vértices | Sí, ligeramente | *Simplificar*, *Suavizar*, `v.generalize` de GRASS |
| **Agregación** | Número y forma de elementos | Sí | *Disolver*, *Agregar*, *Centroides* (colapso) |
| **Desplazamiento** | Posición de símbolos | Sí, intencionalmente | Renderizador de desplazamiento de puntos, ubicación de etiquetas |
| **Exageración** | Tamaño o forma | Sí, intencionalmente | Tamaños de símbolos en unidades de mapa o milímetros |
| **Clasificación** | Categorías temáticas | No | Simbología categorizada o graduada, *Reclasificar por tabla* |

---

## La simplificación de líneas

La simplificación es la operación de generalización que más se automatiza en los SIG. Entender cómo funciona ayuda a usarla correctamente.

### El algoritmo de Douglas-Peucker

Publicado en 1973 por David Douglas y Thomas Peucker, es el algoritmo de simplificación más conocido. Funciona así:

1. Se traza una **línea recta** entre el primer y el último vértice.
2. Se busca el vértice **más alejado** de esa recta.
3. Si su distancia es **menor que una tolerancia** definida por el usuario, se eliminan todos los vértices intermedios.
4. Si es **mayor**, ese vértice se conserva y se repite el proceso en cada uno de los dos tramos resultantes.

El resultado depende casi por completo de la **tolerancia**: cuanto mayor es, más vértices se eliminan.

<figure class="figura">
<svg viewBox="0 0 720 410" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Simplificación de una línea con el algoritmo de Douglas-Peucker a dos tolerancias">
<path d="M 50.0 97.3 L 53.9 102.2 L 57.8 106.4 L 61.6 110.2 L 65.5 111.5 L 69.4 113.6 L 73.2 109.8 L 77.1 111.2 L 81.0 112.1 L 84.9 109.1 L 88.8 108.5 L 92.6 103.4 L 96.5 103.9 L 100.4 102.3 L 104.2 103.6 L 108.1 104.3 L 112.0 102.8 L 115.9 104.9 L 119.8 106.5 L 123.6 110.3 L 127.5 110.2 L 131.4 107.5 L 135.2 109.7 L 139.1 105.6 L 143.0 106.0 L 146.9 101.8 L 150.8 99.2 L 154.6 101.4 L 158.5 97.3 L 162.4 96.9 L 166.2 100.7 L 170.1 101.6 L 174.0 101.2 L 177.9 107.2 L 181.8 108.6 L 185.6 112.7 L 189.5 114.0 L 193.4 120.2 L 197.2 121.4 L 201.1 124.2 L 205.0 124.7 L 208.9 122.1 L 212.8 121.9 L 216.6 120.3 L 220.5 119.3 L 224.4 118.2 L 228.2 118.9 L 232.1 120.3 L 236.0 118.2 L 239.9 122.1 L 243.8 121.8 L 247.6 123.0 L 251.5 126.3 L 255.4 125.4 L 259.2 124.4 L 263.1 124.1 L 267.0 123.0 L 270.9 117.1 L 274.8 117.3 L 278.6 108.4 L 282.5 106.7 L 286.4 102.1 L 290.2 93.6 L 294.1 92.6 L 298.0 87.0 L 301.9 85.0 L 305.8 80.2 L 309.6 78.8 L 313.5 78.3 L 317.4 80.9 L 321.2 76.6 L 325.1 77.9 L 329.0 77.2 L 332.9 75.2 L 336.8 70.0 L 340.6 67.1 L 344.5 64.7 L 348.4 62.7 L 352.2 56.9 L 356.1 57.5 L 360.0 56.1 L 363.9 55.8 L 367.8 52.4 L 371.6 57.7 L 375.5 55.8 L 379.4 59.4 L 383.2 63.3 L 387.1 67.3 L 391.0 67.0 L 394.9 71.2 L 398.8 70.5 L 402.6 69.6 L 406.5 69.0 L 410.4 67.2 L 414.2 65.2 L 418.1 63.8 L 422.0 64.6 L 425.9 64.7 L 429.8 60.2 L 433.6 59.5 L 437.5 64.0 L 441.4 62.7 L 445.2 63.1 L 449.1 63.3 L 453.0 65.6 L 456.9 66.8 L 460.8 64.7 L 464.6 63.2 L 468.5 59.5 L 472.4 60.6 L 476.2 53.4 L 480.1 51.9 L 484.0 50.0 L 487.9 43.7 L 491.8 43.9 L 495.6 43.2 L 499.5 41.1 L 503.4 42.0 L 507.2 40.0 L 511.1 43.3 L 515.0 44.2 L 518.9 49.7 L 522.8 49.6 L 526.6 52.3 L 530.5 56.4 L 534.4 56.9 L 538.2 58.3 L 542.1 56.4 L 546.0 57.0 L 549.9 58.7 L 553.8 58.6 L 557.6 59.3 L 561.5 62.3 L 565.4 64.3 L 569.2 69.4 L 573.1 76.8 L 577.0 81.8 L 580.9 85.6 L 584.8 90.1 L 588.6 94.1 L 592.5 97.0 L 596.4 100.9 L 600.2 105.3 L 604.1 107.0 L 608.0 105.2 L 611.9 107.0 L 615.8 106.5 L 619.6 105.6 L 623.5 105.2 L 627.4 105.6 L 631.2 104.4 L 635.1 106.9 L 639.0 106.5 L 642.9 109.1 L 646.8 112.1 L 650.6 113.3 L 654.5 112.6 L 658.4 115.9 L 662.2 114.3 L 666.1 112.9 L 670.0 108.5" fill="none" stroke="#3f6fd8" stroke-width="2.2" stroke-linejoin="round"/>
<circle cx="50.0" cy="97.3" r="1.5" fill="#e0823d"/>
<circle cx="53.9" cy="102.2" r="1.5" fill="#e0823d"/>
<circle cx="57.8" cy="106.4" r="1.5" fill="#e0823d"/>
<circle cx="61.6" cy="110.2" r="1.5" fill="#e0823d"/>
<circle cx="65.5" cy="111.5" r="1.5" fill="#e0823d"/>
<circle cx="69.4" cy="113.6" r="1.5" fill="#e0823d"/>
<circle cx="73.2" cy="109.8" r="1.5" fill="#e0823d"/>
<circle cx="77.1" cy="111.2" r="1.5" fill="#e0823d"/>
<circle cx="81.0" cy="112.1" r="1.5" fill="#e0823d"/>
<circle cx="84.9" cy="109.1" r="1.5" fill="#e0823d"/>
<circle cx="88.8" cy="108.5" r="1.5" fill="#e0823d"/>
<circle cx="92.6" cy="103.4" r="1.5" fill="#e0823d"/>
<circle cx="96.5" cy="103.9" r="1.5" fill="#e0823d"/>
<circle cx="100.4" cy="102.3" r="1.5" fill="#e0823d"/>
<circle cx="104.2" cy="103.6" r="1.5" fill="#e0823d"/>
<circle cx="108.1" cy="104.3" r="1.5" fill="#e0823d"/>
<circle cx="112.0" cy="102.8" r="1.5" fill="#e0823d"/>
<circle cx="115.9" cy="104.9" r="1.5" fill="#e0823d"/>
<circle cx="119.8" cy="106.5" r="1.5" fill="#e0823d"/>
<circle cx="123.6" cy="110.3" r="1.5" fill="#e0823d"/>
<circle cx="127.5" cy="110.2" r="1.5" fill="#e0823d"/>
<circle cx="131.4" cy="107.5" r="1.5" fill="#e0823d"/>
<circle cx="135.2" cy="109.7" r="1.5" fill="#e0823d"/>
<circle cx="139.1" cy="105.6" r="1.5" fill="#e0823d"/>
<circle cx="143.0" cy="106.0" r="1.5" fill="#e0823d"/>
<circle cx="146.9" cy="101.8" r="1.5" fill="#e0823d"/>
<circle cx="150.8" cy="99.2" r="1.5" fill="#e0823d"/>
<circle cx="154.6" cy="101.4" r="1.5" fill="#e0823d"/>
<circle cx="158.5" cy="97.3" r="1.5" fill="#e0823d"/>
<circle cx="162.4" cy="96.9" r="1.5" fill="#e0823d"/>
<circle cx="166.2" cy="100.7" r="1.5" fill="#e0823d"/>
<circle cx="170.1" cy="101.6" r="1.5" fill="#e0823d"/>
<circle cx="174.0" cy="101.2" r="1.5" fill="#e0823d"/>
<circle cx="177.9" cy="107.2" r="1.5" fill="#e0823d"/>
<circle cx="181.8" cy="108.6" r="1.5" fill="#e0823d"/>
<circle cx="185.6" cy="112.7" r="1.5" fill="#e0823d"/>
<circle cx="189.5" cy="114.0" r="1.5" fill="#e0823d"/>
<circle cx="193.4" cy="120.2" r="1.5" fill="#e0823d"/>
<circle cx="197.2" cy="121.4" r="1.5" fill="#e0823d"/>
<circle cx="201.1" cy="124.2" r="1.5" fill="#e0823d"/>
<circle cx="205.0" cy="124.7" r="1.5" fill="#e0823d"/>
<circle cx="208.9" cy="122.1" r="1.5" fill="#e0823d"/>
<circle cx="212.8" cy="121.9" r="1.5" fill="#e0823d"/>
<circle cx="216.6" cy="120.3" r="1.5" fill="#e0823d"/>
<circle cx="220.5" cy="119.3" r="1.5" fill="#e0823d"/>
<circle cx="224.4" cy="118.2" r="1.5" fill="#e0823d"/>
<circle cx="228.2" cy="118.9" r="1.5" fill="#e0823d"/>
<circle cx="232.1" cy="120.3" r="1.5" fill="#e0823d"/>
<circle cx="236.0" cy="118.2" r="1.5" fill="#e0823d"/>
<circle cx="239.9" cy="122.1" r="1.5" fill="#e0823d"/>
<circle cx="243.8" cy="121.8" r="1.5" fill="#e0823d"/>
<circle cx="247.6" cy="123.0" r="1.5" fill="#e0823d"/>
<circle cx="251.5" cy="126.3" r="1.5" fill="#e0823d"/>
<circle cx="255.4" cy="125.4" r="1.5" fill="#e0823d"/>
<circle cx="259.2" cy="124.4" r="1.5" fill="#e0823d"/>
<circle cx="263.1" cy="124.1" r="1.5" fill="#e0823d"/>
<circle cx="267.0" cy="123.0" r="1.5" fill="#e0823d"/>
<circle cx="270.9" cy="117.1" r="1.5" fill="#e0823d"/>
<circle cx="274.8" cy="117.3" r="1.5" fill="#e0823d"/>
<circle cx="278.6" cy="108.4" r="1.5" fill="#e0823d"/>
<circle cx="282.5" cy="106.7" r="1.5" fill="#e0823d"/>
<circle cx="286.4" cy="102.1" r="1.5" fill="#e0823d"/>
<circle cx="290.2" cy="93.6" r="1.5" fill="#e0823d"/>
<circle cx="294.1" cy="92.6" r="1.5" fill="#e0823d"/>
<circle cx="298.0" cy="87.0" r="1.5" fill="#e0823d"/>
<circle cx="301.9" cy="85.0" r="1.5" fill="#e0823d"/>
<circle cx="305.8" cy="80.2" r="1.5" fill="#e0823d"/>
<circle cx="309.6" cy="78.8" r="1.5" fill="#e0823d"/>
<circle cx="313.5" cy="78.3" r="1.5" fill="#e0823d"/>
<circle cx="317.4" cy="80.9" r="1.5" fill="#e0823d"/>
<circle cx="321.2" cy="76.6" r="1.5" fill="#e0823d"/>
<circle cx="325.1" cy="77.9" r="1.5" fill="#e0823d"/>
<circle cx="329.0" cy="77.2" r="1.5" fill="#e0823d"/>
<circle cx="332.9" cy="75.2" r="1.5" fill="#e0823d"/>
<circle cx="336.8" cy="70.0" r="1.5" fill="#e0823d"/>
<circle cx="340.6" cy="67.1" r="1.5" fill="#e0823d"/>
<circle cx="344.5" cy="64.7" r="1.5" fill="#e0823d"/>
<circle cx="348.4" cy="62.7" r="1.5" fill="#e0823d"/>
<circle cx="352.2" cy="56.9" r="1.5" fill="#e0823d"/>
<circle cx="356.1" cy="57.5" r="1.5" fill="#e0823d"/>
<circle cx="360.0" cy="56.1" r="1.5" fill="#e0823d"/>
<circle cx="363.9" cy="55.8" r="1.5" fill="#e0823d"/>
<circle cx="367.8" cy="52.4" r="1.5" fill="#e0823d"/>
<circle cx="371.6" cy="57.7" r="1.5" fill="#e0823d"/>
<circle cx="375.5" cy="55.8" r="1.5" fill="#e0823d"/>
<circle cx="379.4" cy="59.4" r="1.5" fill="#e0823d"/>
<circle cx="383.2" cy="63.3" r="1.5" fill="#e0823d"/>
<circle cx="387.1" cy="67.3" r="1.5" fill="#e0823d"/>
<circle cx="391.0" cy="67.0" r="1.5" fill="#e0823d"/>
<circle cx="394.9" cy="71.2" r="1.5" fill="#e0823d"/>
<circle cx="398.8" cy="70.5" r="1.5" fill="#e0823d"/>
<circle cx="402.6" cy="69.6" r="1.5" fill="#e0823d"/>
<circle cx="406.5" cy="69.0" r="1.5" fill="#e0823d"/>
<circle cx="410.4" cy="67.2" r="1.5" fill="#e0823d"/>
<circle cx="414.2" cy="65.2" r="1.5" fill="#e0823d"/>
<circle cx="418.1" cy="63.8" r="1.5" fill="#e0823d"/>
<circle cx="422.0" cy="64.6" r="1.5" fill="#e0823d"/>
<circle cx="425.9" cy="64.7" r="1.5" fill="#e0823d"/>
<circle cx="429.8" cy="60.2" r="1.5" fill="#e0823d"/>
<circle cx="433.6" cy="59.5" r="1.5" fill="#e0823d"/>
<circle cx="437.5" cy="64.0" r="1.5" fill="#e0823d"/>
<circle cx="441.4" cy="62.7" r="1.5" fill="#e0823d"/>
<circle cx="445.2" cy="63.1" r="1.5" fill="#e0823d"/>
<circle cx="449.1" cy="63.3" r="1.5" fill="#e0823d"/>
<circle cx="453.0" cy="65.6" r="1.5" fill="#e0823d"/>
<circle cx="456.9" cy="66.8" r="1.5" fill="#e0823d"/>
<circle cx="460.8" cy="64.7" r="1.5" fill="#e0823d"/>
<circle cx="464.6" cy="63.2" r="1.5" fill="#e0823d"/>
<circle cx="468.5" cy="59.5" r="1.5" fill="#e0823d"/>
<circle cx="472.4" cy="60.6" r="1.5" fill="#e0823d"/>
<circle cx="476.2" cy="53.4" r="1.5" fill="#e0823d"/>
<circle cx="480.1" cy="51.9" r="1.5" fill="#e0823d"/>
<circle cx="484.0" cy="50.0" r="1.5" fill="#e0823d"/>
<circle cx="487.9" cy="43.7" r="1.5" fill="#e0823d"/>
<circle cx="491.8" cy="43.9" r="1.5" fill="#e0823d"/>
<circle cx="495.6" cy="43.2" r="1.5" fill="#e0823d"/>
<circle cx="499.5" cy="41.1" r="1.5" fill="#e0823d"/>
<circle cx="503.4" cy="42.0" r="1.5" fill="#e0823d"/>
<circle cx="507.2" cy="40.0" r="1.5" fill="#e0823d"/>
<circle cx="511.1" cy="43.3" r="1.5" fill="#e0823d"/>
<circle cx="515.0" cy="44.2" r="1.5" fill="#e0823d"/>
<circle cx="518.9" cy="49.7" r="1.5" fill="#e0823d"/>
<circle cx="522.8" cy="49.6" r="1.5" fill="#e0823d"/>
<circle cx="526.6" cy="52.3" r="1.5" fill="#e0823d"/>
<circle cx="530.5" cy="56.4" r="1.5" fill="#e0823d"/>
<circle cx="534.4" cy="56.9" r="1.5" fill="#e0823d"/>
<circle cx="538.2" cy="58.3" r="1.5" fill="#e0823d"/>
<circle cx="542.1" cy="56.4" r="1.5" fill="#e0823d"/>
<circle cx="546.0" cy="57.0" r="1.5" fill="#e0823d"/>
<circle cx="549.9" cy="58.7" r="1.5" fill="#e0823d"/>
<circle cx="553.8" cy="58.6" r="1.5" fill="#e0823d"/>
<circle cx="557.6" cy="59.3" r="1.5" fill="#e0823d"/>
<circle cx="561.5" cy="62.3" r="1.5" fill="#e0823d"/>
<circle cx="565.4" cy="64.3" r="1.5" fill="#e0823d"/>
<circle cx="569.2" cy="69.4" r="1.5" fill="#e0823d"/>
<circle cx="573.1" cy="76.8" r="1.5" fill="#e0823d"/>
<circle cx="577.0" cy="81.8" r="1.5" fill="#e0823d"/>
<circle cx="580.9" cy="85.6" r="1.5" fill="#e0823d"/>
<circle cx="584.8" cy="90.1" r="1.5" fill="#e0823d"/>
<circle cx="588.6" cy="94.1" r="1.5" fill="#e0823d"/>
<circle cx="592.5" cy="97.0" r="1.5" fill="#e0823d"/>
<circle cx="596.4" cy="100.9" r="1.5" fill="#e0823d"/>
<circle cx="600.2" cy="105.3" r="1.5" fill="#e0823d"/>
<circle cx="604.1" cy="107.0" r="1.5" fill="#e0823d"/>
<circle cx="608.0" cy="105.2" r="1.5" fill="#e0823d"/>
<circle cx="611.9" cy="107.0" r="1.5" fill="#e0823d"/>
<circle cx="615.8" cy="106.5" r="1.5" fill="#e0823d"/>
<circle cx="619.6" cy="105.6" r="1.5" fill="#e0823d"/>
<circle cx="623.5" cy="105.2" r="1.5" fill="#e0823d"/>
<circle cx="627.4" cy="105.6" r="1.5" fill="#e0823d"/>
<circle cx="631.2" cy="104.4" r="1.5" fill="#e0823d"/>
<circle cx="635.1" cy="106.9" r="1.5" fill="#e0823d"/>
<circle cx="639.0" cy="106.5" r="1.5" fill="#e0823d"/>
<circle cx="642.9" cy="109.1" r="1.5" fill="#e0823d"/>
<circle cx="646.8" cy="112.1" r="1.5" fill="#e0823d"/>
<circle cx="650.6" cy="113.3" r="1.5" fill="#e0823d"/>
<circle cx="654.5" cy="112.6" r="1.5" fill="#e0823d"/>
<circle cx="658.4" cy="115.9" r="1.5" fill="#e0823d"/>
<circle cx="662.2" cy="114.3" r="1.5" fill="#e0823d"/>
<circle cx="666.1" cy="112.9" r="1.5" fill="#e0823d"/>
<circle cx="670.0" cy="108.5" r="1.5" fill="#e0823d"/>
<text x="50" y="21" font-size="14" font-weight="bold" fill="currentColor">Línea original</text>
<text x="690" y="21" text-anchor="end" font-size="12" fill="currentColor">161 vértices · longitud 100 %</text>
<path d="M 50.0 227.3 L 69.4 243.6 L 100.4 232.3 L 112.0 232.8 L 123.6 240.3 L 135.2 239.7 L 162.4 226.9 L 174.0 231.2 L 201.1 254.2 L 236.0 248.2 L 251.5 256.3 L 274.8 247.3 L 290.2 223.6 L 305.8 210.2 L 329.0 207.2 L 352.2 186.9 L 367.8 182.4 L 394.9 201.2 L 433.6 189.5 L 437.5 194.0 L 456.9 196.8 L 472.4 190.6 L 487.9 173.7 L 507.2 170.0 L 530.5 186.4 L 557.6 189.3 L 565.4 194.3 L 577.0 211.8 L 604.1 237.0 L 631.2 234.4 L 658.4 245.9 L 670.0 238.5" fill="none" stroke="#3f6fd8" stroke-width="2.2" stroke-linejoin="round"/>
<circle cx="50.0" cy="227.3" r="2.6" fill="#e0823d"/>
<circle cx="69.4" cy="243.6" r="2.6" fill="#e0823d"/>
<circle cx="100.4" cy="232.3" r="2.6" fill="#e0823d"/>
<circle cx="112.0" cy="232.8" r="2.6" fill="#e0823d"/>
<circle cx="123.6" cy="240.3" r="2.6" fill="#e0823d"/>
<circle cx="135.2" cy="239.7" r="2.6" fill="#e0823d"/>
<circle cx="162.4" cy="226.9" r="2.6" fill="#e0823d"/>
<circle cx="174.0" cy="231.2" r="2.6" fill="#e0823d"/>
<circle cx="201.1" cy="254.2" r="2.6" fill="#e0823d"/>
<circle cx="236.0" cy="248.2" r="2.6" fill="#e0823d"/>
<circle cx="251.5" cy="256.3" r="2.6" fill="#e0823d"/>
<circle cx="274.8" cy="247.3" r="2.6" fill="#e0823d"/>
<circle cx="290.2" cy="223.6" r="2.6" fill="#e0823d"/>
<circle cx="305.8" cy="210.2" r="2.6" fill="#e0823d"/>
<circle cx="329.0" cy="207.2" r="2.6" fill="#e0823d"/>
<circle cx="352.2" cy="186.9" r="2.6" fill="#e0823d"/>
<circle cx="367.8" cy="182.4" r="2.6" fill="#e0823d"/>
<circle cx="394.9" cy="201.2" r="2.6" fill="#e0823d"/>
<circle cx="433.6" cy="189.5" r="2.6" fill="#e0823d"/>
<circle cx="437.5" cy="194.0" r="2.6" fill="#e0823d"/>
<circle cx="456.9" cy="196.8" r="2.6" fill="#e0823d"/>
<circle cx="472.4" cy="190.6" r="2.6" fill="#e0823d"/>
<circle cx="487.9" cy="173.7" r="2.6" fill="#e0823d"/>
<circle cx="507.2" cy="170.0" r="2.6" fill="#e0823d"/>
<circle cx="530.5" cy="186.4" r="2.6" fill="#e0823d"/>
<circle cx="557.6" cy="189.3" r="2.6" fill="#e0823d"/>
<circle cx="565.4" cy="194.3" r="2.6" fill="#e0823d"/>
<circle cx="577.0" cy="211.8" r="2.6" fill="#e0823d"/>
<circle cx="604.1" cy="237.0" r="2.6" fill="#e0823d"/>
<circle cx="631.2" cy="234.4" r="2.6" fill="#e0823d"/>
<circle cx="658.4" cy="245.9" r="2.6" fill="#e0823d"/>
<circle cx="670.0" cy="238.5" r="2.6" fill="#e0823d"/>
<text x="50" y="151" font-size="14" font-weight="bold" fill="currentColor">Tolerancia de 5 m</text>
<text x="690" y="151" text-anchor="end" font-size="12" fill="currentColor">32 vértices · longitud 94 %</text>
<path d="M 50.0 357.3 L 69.4 373.6 L 162.4 356.9 L 251.5 386.3 L 352.2 316.9 L 456.9 326.8 L 507.2 300.0 L 604.1 367.0 L 670.0 368.5" fill="none" stroke="#3f6fd8" stroke-width="2.2" stroke-linejoin="round"/>
<circle cx="50.0" cy="357.3" r="2.6" fill="#e0823d"/>
<circle cx="69.4" cy="373.6" r="2.6" fill="#e0823d"/>
<circle cx="162.4" cy="356.9" r="2.6" fill="#e0823d"/>
<circle cx="251.5" cy="386.3" r="2.6" fill="#e0823d"/>
<circle cx="352.2" cy="316.9" r="2.6" fill="#e0823d"/>
<circle cx="456.9" cy="326.8" r="2.6" fill="#e0823d"/>
<circle cx="507.2" cy="300.0" r="2.6" fill="#e0823d"/>
<circle cx="604.1" cy="367.0" r="2.6" fill="#e0823d"/>
<circle cx="670.0" cy="368.5" r="2.6" fill="#e0823d"/>
<text x="50" y="281" font-size="14" font-weight="bold" fill="currentColor">Tolerancia de 25 m</text>
<text x="690" y="281" text-anchor="end" font-size="12" fill="currentColor">9 vértices · longitud 88 %</text>
</svg><figcaption>Una misma línea simplificada con el algoritmo de Douglas-Peucker a dos tolerancias. Los puntos naranjas son los vértices conservados.</figcaption>
</figure>

!!! tip "¿Qué tolerancia usar?"

    Una referencia práctica es la **precisión gráfica** de la escala de destino (tema 1.8): **0,2 mm × D**.

    - Para un mapa a escala **1:25 000**, una tolerancia de unos **5 m**.
    - Para un mapa a escala **1:100 000**, una tolerancia de unos **20 m**.

    Con esos valores, los vértices eliminados corresponden a detalles que **no se percibirían** a esa escala.

??? info "Para saber más: otros algoritmos"

    - **Visvalingam-Whyatt** (1993): elimina primero los vértices que forman los **triángulos de menor área** con sus vecinos. Suele producir formas más naturales que Douglas-Peucker con la misma cantidad de vértices.
    - **Suavizado de Chaikin:** no simplifica, sino que **redondea** los ángulos cortando las esquinas de forma iterativa. QGIS lo usa en su herramienta *Suavizar*.
    - **Algoritmos con desplazamiento:** además de simplificar, desplazan elementos para evitar conflictos. GRASS GIS ofrece varios de ellos en `v.generalize`.

### El problema de la topología

!!! danger "Simplificar polígonos vecinos por separado"

    Si se simplifican los límites de municipios o predios **cada uno por separado**, el algoritmo puede eliminar vértices distintos en el lado de cada vecino. El resultado son **huecos** y **superposiciones** entre polígonos que antes compartían un límite perfecto.

    Para evitarlo, se deben usar herramientas que **respeten la topología**, es decir, que simplifiquen los límites compartidos **una sola vez**, como `v.generalize` de GRASS GIS (disponible desde QGIS) o las funciones topológicas de PostGIS.

---

## Generalización y escala

La generalización es la respuesta directa al cambio de escala. Retomando el ejemplo del temario:

<figure class="figura">
<svg viewBox="0 0 720 340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Generalización de una zona urbana desde edificios individuales hasta un área urbana">
<rect x="20" y="35" width="250" height="250" fill="#2e9e5b" fill-opacity="0.07" stroke="currentColor" stroke-width="1.3"/>
<path d="M 20 280.0 C 95.0 272.5, 195.0 285.0, 270 272.5" fill="none" stroke="#3f6fd8" stroke-width="7.5"/>
<rect x="40.0" y="55.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="42.0" y="56.5" width="8.4" height="10.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="51.6" y="56.5" width="7.1" height="13.1" fill="currentColor" fill-opacity="0.6"/>
<rect x="59.9" y="56.5" width="6.5" height="11.3" fill="currentColor" fill-opacity="0.6"/>
<rect x="67.7" y="56.5" width="10.1" height="9.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="42.0" y="86.7" width="8.7" height="11.8" fill="currentColor" fill-opacity="0.6"/>
<rect x="52.0" y="87.9" width="6.7" height="10.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="59.9" y="87.5" width="9.3" height="11.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="70.4" y="89.0" width="9.4" height="9.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="41.5" y="75.5" width="12.6" height="8.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="74.3" y="75.6" width="9.2" height="8.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="40.0" y="110.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="42.0" y="111.5" width="7.6" height="12.8" fill="currentColor" fill-opacity="0.6"/>
<rect x="50.9" y="111.5" width="7.3" height="13.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="59.4" y="111.5" width="10.0" height="9.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="70.7" y="111.5" width="8.0" height="11.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="42.0" y="142.6" width="6.6" height="10.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="49.8" y="144.2" width="10.1" height="9.3" fill="currentColor" fill-opacity="0.6"/>
<rect x="61.2" y="144.1" width="8.9" height="9.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="71.4" y="140.3" width="8.8" height="13.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="41.5" y="128.6" width="9.2" height="6.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="41.5" y="136.5" width="13.4" height="8.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="70.0" y="132.4" width="13.5" height="8.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="40.0" y="165.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="42.0" y="166.5" width="8.9" height="9.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="52.2" y="166.5" width="7.6" height="13.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="61.0" y="166.5" width="10.5" height="9.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="72.7" y="166.5" width="9.3" height="13.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="42.0" y="196.7" width="7.4" height="11.8" fill="currentColor" fill-opacity="0.6"/>
<rect x="50.7" y="197.9" width="6.7" height="10.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="58.6" y="196.8" width="9.2" height="11.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="69.1" y="199.3" width="9.6" height="9.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="41.5" y="186.2" width="13.7" height="8.1" fill="currentColor" fill-opacity="0.6"/>
<rect x="73.7" y="177.9" width="9.8" height="8.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="73.1" y="187.4" width="10.4" height="8.3" fill="currentColor" fill-opacity="0.6"/>
<rect x="95.0" y="55.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="97.0" y="56.5" width="6.9" height="12.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="105.2" y="56.5" width="6.6" height="12.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="113.0" y="56.5" width="9.7" height="11.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="124.0" y="56.5" width="9.3" height="10.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="97.0" y="87.6" width="9.5" height="10.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="107.7" y="84.9" width="7.4" height="13.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="116.4" y="87.9" width="8.1" height="10.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="125.7" y="87.9" width="9.9" height="10.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="96.5" y="78.5" width="13.6" height="6.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="129.4" y="68.7" width="9.1" height="6.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="127.8" y="76.5" width="10.7" height="7.3" fill="currentColor" fill-opacity="0.6"/>
<rect x="95.0" y="110.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="97.0" y="111.5" width="7.9" height="9.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="106.2" y="111.5" width="8.7" height="9.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="116.2" y="111.5" width="6.8" height="11.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="124.3" y="111.5" width="9.3" height="9.1" fill="currentColor" fill-opacity="0.6"/>
<rect x="97.0" y="141.2" width="8.3" height="12.3" fill="currentColor" fill-opacity="0.6"/>
<rect x="106.6" y="142.8" width="9.6" height="10.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="117.4" y="143.9" width="10.0" height="9.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="96.5" y="123.3" width="9.0" height="6.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="96.5" y="131.4" width="9.6" height="8.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="128.9" y="122.9" width="9.6" height="6.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="127.0" y="130.7" width="11.5" height="8.3" fill="currentColor" fill-opacity="0.6"/>
<rect x="95.0" y="165.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="97.0" y="166.5" width="8.4" height="13.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="106.7" y="166.5" width="8.6" height="13.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="116.6" y="166.5" width="6.6" height="13.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="124.4" y="166.5" width="10.1" height="11.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="97.0" y="197.1" width="8.6" height="11.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="106.8" y="199.4" width="10.1" height="9.1" fill="currentColor" fill-opacity="0.6"/>
<rect x="118.2" y="197.0" width="9.1" height="11.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="128.6" y="196.1" width="7.7" height="12.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="96.5" y="177.6" width="11.0" height="9.3" fill="currentColor" fill-opacity="0.6"/>
<rect x="96.5" y="188.2" width="11.9" height="8.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="126.6" y="184.9" width="11.9" height="9.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="95.0" y="220.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="97.0" y="221.5" width="8.9" height="11.8" fill="currentColor" fill-opacity="0.6"/>
<rect x="107.1" y="221.5" width="9.2" height="10.8" fill="currentColor" fill-opacity="0.6"/>
<rect x="117.6" y="221.5" width="6.8" height="9.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="125.6" y="221.5" width="8.9" height="9.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="97.0" y="253.0" width="6.8" height="10.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="105.0" y="252.1" width="8.4" height="11.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="114.6" y="250.9" width="6.6" height="12.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="122.5" y="250.8" width="7.8" height="12.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="96.5" y="243.8" width="10.5" height="6.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="124.9" y="238.7" width="13.6" height="10.3" fill="currentColor" fill-opacity="0.6"/>
<rect x="150.0" y="55.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="152.0" y="56.5" width="8.4" height="11.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="161.6" y="56.5" width="8.0" height="11.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="170.8" y="56.5" width="7.4" height="10.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="179.5" y="56.5" width="8.6" height="9.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="152.0" y="85.0" width="8.3" height="13.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="161.5" y="89.2" width="6.6" height="9.3" fill="currentColor" fill-opacity="0.6"/>
<rect x="169.3" y="89.5" width="9.7" height="9.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="180.3" y="85.5" width="7.5" height="13.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="151.5" y="75.2" width="12.8" height="7.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="151.5" y="84.1" width="12.7" height="10.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="180.2" y="68.4" width="13.3" height="10.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="184.3" y="79.6" width="9.2" height="10.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="150.0" y="110.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="152.0" y="111.5" width="8.9" height="11.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="162.2" y="111.5" width="7.9" height="12.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="171.3" y="111.5" width="8.1" height="9.8" fill="currentColor" fill-opacity="0.6"/>
<rect x="180.7" y="111.5" width="7.6" height="11.1" fill="currentColor" fill-opacity="0.6"/>
<rect x="152.0" y="141.9" width="8.9" height="11.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="162.2" y="143.8" width="8.3" height="9.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="171.7" y="143.1" width="8.1" height="10.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="181.1" y="142.0" width="7.2" height="11.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="151.5" y="130.9" width="10.4" height="9.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="183.7" y="122.8" width="9.8" height="9.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="183.1" y="133.5" width="10.4" height="8.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="150.0" y="165.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="152.0" y="166.5" width="8.4" height="13.1" fill="currentColor" fill-opacity="0.6"/>
<rect x="161.6" y="166.5" width="7.8" height="12.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="170.7" y="166.5" width="8.6" height="9.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="180.5" y="166.5" width="9.4" height="10.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="152.0" y="199.4" width="8.6" height="9.1" fill="currentColor" fill-opacity="0.6"/>
<rect x="161.9" y="195.1" width="6.5" height="13.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="169.7" y="199.0" width="6.7" height="9.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="177.6" y="199.3" width="7.2" height="9.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="151.5" y="188.7" width="12.2" height="7.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="181.9" y="184.5" width="11.6" height="10.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="150.0" y="220.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="152.0" y="221.5" width="10.0" height="12.1" fill="currentColor" fill-opacity="0.6"/>
<rect x="163.2" y="221.5" width="10.1" height="12.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="174.6" y="221.5" width="7.6" height="9.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="183.4" y="221.5" width="8.3" height="12.1" fill="currentColor" fill-opacity="0.6"/>
<rect x="152.0" y="253.1" width="7.4" height="10.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="160.7" y="253.0" width="9.5" height="10.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="171.4" y="252.0" width="8.9" height="11.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="181.6" y="254.6" width="10.2" height="8.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="151.5" y="240.9" width="9.8" height="7.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="151.5" y="249.2" width="13.3" height="8.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="179.8" y="241.1" width="13.7" height="9.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="205.0" y="110.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="207.0" y="111.5" width="8.5" height="9.1" fill="currentColor" fill-opacity="0.6"/>
<rect x="216.7" y="111.5" width="9.7" height="10.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="227.7" y="111.5" width="8.4" height="11.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="237.3" y="111.5" width="10.4" height="11.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="207.0" y="139.9" width="10.2" height="13.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="218.4" y="143.0" width="6.8" height="10.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="226.5" y="140.9" width="10.1" height="12.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="206.5" y="131.8" width="9.6" height="10.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="238.3" y="133.2" width="10.2" height="7.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="205.0" y="165.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="207.0" y="166.5" width="9.6" height="11.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="217.9" y="166.5" width="10.4" height="9.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="229.5" y="166.5" width="7.2" height="9.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="237.9" y="166.5" width="8.8" height="9.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="207.0" y="197.1" width="9.2" height="11.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="217.4" y="195.5" width="8.8" height="13.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="227.5" y="195.1" width="9.7" height="13.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="238.4" y="197.9" width="7.1" height="10.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="206.5" y="178.6" width="11.2" height="7.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="206.5" y="187.5" width="13.0" height="7.2" fill="currentColor" fill-opacity="0.6"/>
<rect x="236.7" y="178.6" width="11.8" height="7.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="238.0" y="187.4" width="10.5" height="10.3" fill="currentColor" fill-opacity="0.6"/>
<rect x="205.0" y="220.0" width="45.0" height="45.0" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="0.6"/>
<rect x="207.0" y="221.5" width="6.7" height="11.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="215.0" y="221.5" width="7.7" height="13.0" fill="currentColor" fill-opacity="0.6"/>
<rect x="224.0" y="221.5" width="7.3" height="8.8" fill="currentColor" fill-opacity="0.6"/>
<rect x="232.6" y="221.5" width="8.4" height="9.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="207.0" y="251.6" width="7.2" height="11.9" fill="currentColor" fill-opacity="0.6"/>
<rect x="215.5" y="252.9" width="10.2" height="10.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="227.0" y="253.1" width="9.1" height="10.4" fill="currentColor" fill-opacity="0.6"/>
<rect x="237.3" y="252.0" width="10.2" height="11.5" fill="currentColor" fill-opacity="0.6"/>
<rect x="206.5" y="238.5" width="13.0" height="6.6" fill="currentColor" fill-opacity="0.6"/>
<rect x="206.5" y="246.3" width="10.5" height="9.3" fill="currentColor" fill-opacity="0.6"/>
<rect x="236.9" y="240.6" width="11.6" height="6.7" fill="currentColor" fill-opacity="0.6"/>
<rect x="235.5" y="248.6" width="13.0" height="8.5" fill="currentColor" fill-opacity="0.6"/>
<line x1="20" y1="160.0" x2="270" y2="160.0" stroke="#e0823d" stroke-width="8.8"/>
<line x1="145.0" y1="35" x2="145.0" y2="285" stroke="#e0823d" stroke-width="8.8"/>
<text x="145.0" y="309" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">1:5 000</text>
<text x="145.0" y="328" text-anchor="middle" font-size="12" fill="currentColor">Edificios individuales</text>
<rect x="355" y="135" width="150" height="150" fill="#2e9e5b" fill-opacity="0.07" stroke="currentColor" stroke-width="1.3"/>
<path d="M 355 282.0 C 400.0 277.5, 460.0 285.0, 505 277.5" fill="none" stroke="#3f6fd8" stroke-width="4.5"/>
<rect x="367.0" y="147.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="367.0" y="180.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="367.0" y="213.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="400.0" y="147.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="400.0" y="180.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="400.0" y="213.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="400.0" y="246.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="433.0" y="147.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="433.0" y="180.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="433.0" y="213.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="433.0" y="246.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="466.0" y="180.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="466.0" y="213.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<rect x="466.0" y="246.0" width="27.0" height="27.0" fill="currentColor" fill-opacity="0.4"/>
<line x1="355" y1="210.0" x2="505" y2="210.0" stroke="#e0823d" stroke-width="2.2"/>
<line x1="430.0" y1="135" x2="430.0" y2="285" stroke="#e0823d" stroke-width="2.2"/>
<text x="430.0" y="309" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">1:25 000</text>
<text x="430.0" y="328" text-anchor="middle" font-size="12" fill="currentColor">Manzanos y vías</text>
<rect x="590" y="195" width="90" height="90" fill="#2e9e5b" fill-opacity="0.07" stroke="currentColor" stroke-width="1.3"/>
<path d="M 590 283.2 C 617.0 280.5, 653.0 285.0, 680 280.5" fill="none" stroke="#3f6fd8" stroke-width="2.7"/>
<polygon points="595.4,200.4 654.8,200.4 654.8,220.2 674.6,220.2 674.6,277.8 615.2,277.8 615.2,259.8 595.4,259.8" fill="currentColor" fill-opacity="0.4" stroke="currentColor" stroke-opacity="0.6" stroke-width="1" stroke-linejoin="round"/>
<line x1="590" y1="240.0" x2="680" y2="240.0" stroke="#e0823d" stroke-width="1.4"/>
<line x1="635.0" y1="195" x2="635.0" y2="285" stroke="#e0823d" stroke-width="1.4"/>
<text x="635.0" y="309" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">1:100 000</text>
<text x="635.0" y="328" text-anchor="middle" font-size="12" fill="currentColor">Área urbana</text>
<line x1="287" y1="210" x2="331" y2="210" stroke="currentColor" stroke-width="2"/>
<polygon points="341,210 329,204 329,216" fill="currentColor"/>
<text x="314" y="200" text-anchor="middle" font-size="11" fill="currentColor">generalización</text>
<line x1="522" y1="240" x2="566" y2="240" stroke="currentColor" stroke-width="2"/>
<polygon points="576,240 564,234 564,246" fill="currentColor"/>
<text x="549" y="230" text-anchor="middle" font-size="11" fill="currentColor">generalización</text>
</svg><figcaption>Una misma zona urbana generalizada para tres escalas. Los tamaños de los recuadros son ilustrativos, no proporcionales. Datos ficticios.</figcaption>
</figure>

Del paso de edificios individuales a área urbana participan **casi todas las operaciones**: se **seleccionan** las vías principales, se **agregan** los edificios en manzanos y los manzanos en una mancha urbana, se **simplifica** su contorno y se **exagera** el grosor de las vías para que sigan siendo visibles.

### Cómo cambia la representación de cada elemento

| Elemento | 1:5 000 | 1:25 000 | 1:100 000 | 1:1 000 000 |
|---|---|---|---|---|
| **Construcciones** | Edificios individuales con su forma | Edificios simplificados o manzanos | Área urbana | No se representan |
| **Vías** | Calzadas como polígonos o líneas dobles | Líneas con jerarquía de tipos | Solo vías principales | Solo carreteras principales |
| **Ríos** | Polígonos con sus márgenes | Polígonos para ríos anchos, líneas para el resto | Líneas simplificadas, solo ríos principales | Solo los grandes ríos |
| **Localidades** | Manzanos y predios | Manzanos | Mancha urbana | Punto con nombre |
| **Límites administrativos** | Trazado detallado | Trazado detallado | Trazado simplificado | Trazado muy simplificado |

---

## Consecuencias al usar datos generalizados

Esta es la parte más importante del tema para quien trabaja con un SIG. **Los datos generalizados llevan consigo todas las decisiones de generalización**, y eso afecta cualquier análisis que se haga con ellos.

### Las longitudes y los perímetros cambian

Una línea simplificada es **más corta** que la original, porque pierde sus curvas. En el ejemplo de Douglas-Peucker de este tema, la línea conservó el **94 %** de su longitud con una tolerancia de 5 m, y solo el **88 %** con una tolerancia de 25 m.

!!! example "¿Cuánto mide un río?"

    La longitud de un río, de una costa o de un límite **depende de la escala** a la que se midió. Cuanto más detallada es la representación, más curvas aparecen y **mayor** es la longitud medida.

    El matemático Benoît Mandelbrot planteó este problema en 1967 con una pregunta célebre: *¿cuánto mide la costa de Gran Bretaña?* La respuesta es que **no tiene una única longitud**: depende de la escala de medición.

    Por eso, al informar la longitud de un río o el perímetro de un área, es necesario indicar **a partir de qué datos y a qué escala** se midió.

### Las posiciones pueden estar desplazadas

Los elementos **desplazados** o **exagerados** ya no ocupan su posición real. Medir distancias entre ellos, o cruzarlos con datos de mayor detalle, produce errores.

### Mezclar datos de distinta generalización produce incoherencias

Cuando se superponen capas generalizadas para escalas muy distintas, aparecen situaciones imposibles:

- Escuelas levantadas con GNSS que caen **dentro de un río** simplificado a partir de un mapa 1:250 000.
- Predios catastrales que quedan **fuera del límite municipal** porque el límite fue simplificado para un mapa nacional.
- Vías detalladas que **no cruzan** los puentes de una capa de ríos generalizada.
- Superficies de áreas protegidas que **no coinciden** entre dos fuentes, aunque ambas sean oficiales.

!!! danger "La idea central del tema"

    **Los datos no deben utilizarse indiscriminadamente a cualquier escala.** Una capa generalizada para 1:100 000 no se vuelve apta para 1:5 000 por más que el SIG permita acercarse. Antes de usar un dato, hay que preguntarse **para qué escala fue elaborado** y **qué generalización se le aplicó**.

### Generalización en la visualización

Los SIG y los mapas web aplican generalización **de forma automática** para mostrar los datos con fluidez:

- Los mapas web basados en **teselas vectoriales** (como los de OpenStreetMap o los mapas base comerciales) almacenan versiones generalizadas distintas para cada **nivel de acercamiento**.
- QGIS puede **simplificar la geometría al dibujarla** en pantalla para acelerar la visualización. Esta opción, configurable en las propiedades de la capa, **solo afecta cómo se ve**: los datos no se modifican.
- También permite definir **rangos de escala** en los que cada capa es visible, que es una forma sencilla de selección.

---

## Buenas prácticas

!!! tip "Recomendaciones para trabajar con generalización"

    1. **Conserva los datos originales** y guarda las versiones generalizadas como archivos aparte, indicando la escala de destino en su nombre o en sus metadatos.
    2. **Define la escala de destino** antes de generalizar y elige las tolerancias en función de ella.
    3. **Analiza con los datos más detallados** disponibles y **generaliza para representar** los resultados, no al revés.
    4. **Respeta la topología** al simplificar polígonos que comparten límites.
    5. **No midas** distancias, longitudes ni áreas sobre elementos desplazados, exagerados o muy simplificados.
    6. **Documenta** en los metadatos qué operaciones de generalización se aplicaron y con qué parámetros.
    7. **Averigua la escala de origen** de los datos que descargas o recibes antes de combinarlos con otros.

---

## Ideas clave

!!! success "Para recordar"

    - La **generalización** adapta la cantidad, la forma y la simbolización de los elementos a la **escala** y al **propósito** del mapa. Es necesaria e intencional.
    - Es inevitable porque el espacio se reduce con el **cuadrado de la escala** y los símbolos tienen un **tamaño mínimo**.
    - Sus operaciones principales son **selección**, **simplificación**, **agregación**, **desplazamiento**, **exageración** y **clasificación**.
    - La **generalización de datos** elimina información que **no se puede recuperar**.
    - Los algoritmos como **Douglas-Peucker** simplifican según una **tolerancia**, que conviene relacionar con la precisión gráfica de la escala de destino.
    - Los datos generalizados alteran **longitudes, perímetros, áreas y posiciones**.
    - **Los datos no deben usarse indiscriminadamente a cualquier escala.**

---

## Autoevaluación

??? question "1. ¿Por qué la generalización es inevitable al reducir la escala de un mapa?"

    Porque el **espacio disponible** se reduce con el cuadrado de la escala, mientras que los **símbolos, líneas y textos** tienen un tamaño mínimo para ser legibles. No es posible mostrar todos los elementos con todo su detalle en un espacio mucho menor.

??? question "2. Identifica la operación de generalización en cada caso"

    - Los manzanos de una ciudad se unen en una sola mancha urbana → **Agregación**.
    - En un mapa departamental solo se muestran las localidades con más de 5 000 habitantes → **Selección**.
    - Un río con 5 000 vértices se reduce a 300 vértices → **Simplificación**.
    - Una línea férrea paralela a una carretera se dibuja algo separada de ella → **Desplazamiento**.
    - Las 15 clases de cobertura vegetal se reagrupan en bosque, matorral y pastizal → **Clasificación**.
    - Un puente angosto se dibuja más grande de lo que sería a escala → **Exageración**.

??? question "3. Según la ley de Töpfer, si un mapa a escala 1:50 000 muestra 400 comunidades, ¿cuántas convendría mostrar a escala 1:200 000?"

    ```text
    n₂ = 400 × √(50 000 / 200 000) = 400 × √0,25 = 400 × 0,5 = 200 comunidades
    ```

??? question "4. ¿Qué tolerancia de simplificación usarías para preparar los límites municipales de un mapa a escala 1:250 000?"

    Una referencia es la precisión gráfica de esa escala:

    ```text
    0,2 mm × 250 000 = 50 000 mm = 50 m
    ```

    Una tolerancia del orden de **50 m** eliminaría detalles que no se perciben a esa escala.

??? question "5. Después de simplificar los límites de los distritos de un municipio con la herramienta Simplificar, aparecen huecos entre ellos. ¿Por qué ocurre y cómo se evita?"

    Porque la herramienta simplificó **cada polígono por separado**, eliminando vértices diferentes a cada lado del límite compartido. Se evita usando herramientas que **respetan la topología**, como `v.generalize` de GRASS GIS, que simplifican cada límite compartido una sola vez.

??? question "6. Dos informes indican longitudes distintas para el mismo río: 312 km y 287 km. ¿Puede que ambos sean correctos?"

    **Sí.** La longitud de un río depende de la **escala y el nivel de generalización** de los datos con los que se midió. Un río digitalizado a mayor detalle conserva más curvas y resulta más largo. Por eso es necesario indicar la fuente y la escala de medición.

??? question "7. Un técnico calcula la distancia entre un pozo levantado con GNSS y un río tomado de un mapa nacional, y concluye que el pozo está a 120 m del río. ¿Es confiable ese resultado?"

    **No.** La capa del río está generalizada para una escala pequeña: fue **simplificada** y, posiblemente, **desplazada**, con errores que pueden superar los 100 m. Para ese análisis se necesita una capa de ríos de un nivel de detalle compatible con la exactitud del pozo.

---

## Actividad propuesta

!!! example "Actividad 1.10 — Generalizar el proyecto integrador (sin software)"

    Retoma las capas y la escala de trabajo definidas en las actividades anteriores y desarrolla lo siguiente:

    1. Imagina que debes producir **dos mapas** de tu área de estudio: uno a la **escala de trabajo** y otro a una escala **cuatro veces menor** (por ejemplo, 1:10 000 y 1:40 000).
    2. Aplica la **ley de Töpfer** para estimar cuántos elementos de tu capa más numerosa deberían mostrarse en el segundo mapa.
    3. Para cada capa, indica qué **operaciones de generalización** aplicarías al pasar al segundo mapa y con qué criterio.
    4. Calcula la **tolerancia de simplificación** adecuada para la escala del segundo mapa.
    5. Revisa las fuentes de la **Actividad 1.4**: ¿alguna capa ya viene **generalizada** para una escala menor que la de tu proyecto? ¿Qué problemas podría causar en tu análisis?
    6. Define qué análisis harás con los **datos originales** y qué productos se elaborarán con **datos generalizados**.

---

## Referencias

- Burghardt, D., Duchêne, C., & Mackaness, W. (Eds.). (2014). *Abstracting Geographic Information in a Data Rich World: Methodologies and Applications of Map Generalisation*. Springer.
- Douglas, D. H., & Peucker, T. K. (1973). Algorithms for the reduction of the number of points required to represent a digitized line or its caricature. *Cartographica: The International Journal for Geographic Information and Geovisualization*, 10(2), 112–122.
- Mandelbrot, B. (1967). How long is the coast of Britain? Statistical self-similarity and fractional dimension. *Science*, 156(3775), 636–638.
- McMaster, R. B., & Shea, K. S. (1992). *Generalization in Digital Cartography*. Association of American Geographers.
- Olaya, V. (2020). *Sistemas de Información Geográfica*. Libro libre disponible en línea.
- Töpfer, F., & Pillewizer, W. (1966). The principles of selection. *The Cartographic Journal*, 3(1), 10–16.
- Visvalingam, M., & Whyatt, J. D. (1993). Line generalisation by repeated elimination of points. *The Cartographic Journal*, 30(1), 46–51.
