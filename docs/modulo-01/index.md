---
title: Módulo 1 · Introducción teórico-conceptual a los SIG
description: Presentación del Módulo 1. Objetivos, estructura, secuencia conceptual, forma de estudio y proyecto integrador.
---

# Módulo 1 · Introducción teórico-conceptual a los SIG

!!! quote ""

    **Primero entender qué estamos representando; después aprender a hacerlo con la herramienta.**

---

## Presentación

Es muy común que un curso de SIG empiece así: *abrir QGIS, cargar una capa, cambiar la simbología*. En pocos minutos se obtiene un mapa, y parece que ya se "sabe SIG".

Pero muy pronto aparecen los problemas: capas que no se superponen, áreas calculadas en grados, datos que se ven en medio del océano, análisis que mezclan escalas incompatibles, resultados con muchos decimales y poca confiabilidad. Todos esos errores tienen algo en común: **no son problemas del software, sino de conceptos**.

Este módulo construye esa base conceptual **antes de abrir el programa**. A lo largo de 15 temas, responderemos seis preguntas que un profesional debe hacerse frente a cualquier dato geográfico:

<div class="grid cards" markdown>

-   :material-map-search-outline:{ .lg .middle } **¿Qué estamos representando?**

    ---

    El territorio, sus objetos, fenómenos y procesos.

-   :material-earth:{ .lg .middle } **¿Bajo qué referencia?**

    ---

    La forma de la Tierra, los sistemas de referencia y las proyecciones.

-   :material-ruler-square:{ .lg .middle } **¿A qué escala?**

    ---

    La relación entre el mapa y la realidad, y el nivel de detalle.

-   :material-crosshairs-gps:{ .lg .middle } **¿Con qué precisión?**

    ---

    La resolución, la exactitud y la generalización de los datos.

-   :material-vector-square:{ .lg .middle } **¿Mediante qué modelo?**

    ---

    Los modelos vectorial y ráster, y la estructura del dato geoespacial.

-   :material-check-decagram-outline:{ .lg .middle } **¿Con qué calidad?**

    ---

    La aptitud de los datos para el uso que les queremos dar.

</div>

Con esa base, el software deja de ser un conjunto de botones y se convierte en lo que realmente es: **una herramienta para aplicar estos conceptos**.

---

## Objetivos del módulo

!!! abstract "Al finalizar el Módulo 1, el estudiante será capaz de:"

    1. Explicar qué es un Sistema de Información Geográfica y reconocerlo como un **sistema**, no solo como un software.
    2. Comprender cómo se **modela** el territorio para representarlo en un SIG.
    3. Explicar la relación entre la **forma de la Tierra**, el **datum**, los **sistemas de referencia** y las **proyecciones**.
    4. Interpretar y utilizar correctamente **coordenadas geográficas** y **UTM**, en particular en el territorio boliviano.
    5. Aplicar los principios de la **cartografía** y calcular y utilizar correctamente la **escala**.
    6. Diferenciar **escala, resolución, precisión, exactitud y nivel de detalle**, y comprender los efectos de la **generalización**.
    7. Describir los **modelos de representación** y los componentes de un **dato geoespacial**.
    8. Evaluar la **calidad** de la información geográfica y su aptitud para un uso determinado.
    9. Situar el SIG dentro del **ecosistema actual de geotecnologías**.

---

## La secuencia conceptual

Los temas del módulo no son independientes: cada uno se apoya en los anteriores. Por eso se recomienda estudiarlos **en orden**.

<div class="concept-snake">

  <div class="concept-node n1" data-step="01">
    Territorio
  </div>

  <div class="concept-arrow a1">→</div>

  <div class="concept-node n2" data-step="02">
    Forma de la Tierra
  </div>

  <div class="concept-arrow a2">→</div>

  <div class="concept-node n3" data-step="03">
    Geodesia
  </div>

  <div class="concept-arrow a3">→</div>

  <div class="concept-node n4" data-step="04">
    Datum
  </div>


  <div class="concept-arrow down1">↓</div>


  <div class="concept-node n5" data-step="05">
    Sistema de referencia
  </div>

  <div class="concept-arrow a4">←</div>

  <div class="concept-node n6" data-step="06">
    Proyección
  </div>

  <div class="concept-arrow a5">←</div>

  <div class="concept-node n7" data-step="07">
    Coordenadas
  </div>

  <div class="concept-arrow a6">←</div>

  <div class="concept-node n8" data-step="08">
    Cartografía
  </div>


  <div class="concept-arrow down2">↓</div>


  <div class="concept-node n9" data-step="09">
    Escala
  </div>

  <div class="concept-arrow a7">→</div>

  <div class="concept-node n10" data-step="10">
    Modelo espacial
  </div>

  <div class="concept-arrow a8">→</div>

  <div class="concept-node n11" data-step="11">
    Dato geoespacial
  </div>

  <div class="concept-arrow a9">→</div>

  <div class="concept-node n12" data-step="12">
    SIG
  </div>


  <div class="concept-arrow down3">↓</div>


  <div class="concept-node n13 concept-final" data-step="13">
    Análisis espacial
  </div>

</div>

---

## Estructura del módulo

El módulo se organiza en **cinco bloques temáticos**.

### Bloque 1 · SIG y territorio

¿Qué es un SIG y qué es lo que realmente representa?

<div class="grid cards" markdown>

-   **1.1 Sistemas de Información Geográfica**

    ---

    Qué es un SIG, qué problemas resuelve, sus componentes y por qué es un sistema y no solo un software.

    [:octicons-arrow-right-24: Ir al tema](01-sistemas-informacion-geografica.md)

-   **1.2 Espacio geográfico y territorio**

    ---

    Objetos, fenómenos y procesos; localización; relaciones espaciales; abstracción y modelización.

    [:octicons-arrow-right-24: Ir al tema](02-espacio-geografico.md)

</div>

### Bloque 2 · Geodesia y sistemas de referencia

¿Cómo se ubica con exactitud un punto sobre la Tierra?

<div class="grid cards" markdown>

-   **1.3 Fundamentos de Geodesia**

    ---

    Geoide, elipsoide, latitud y longitud, alturas elipsoidal y ortométrica, datum geodésico.

    [:octicons-arrow-right-24: Ir al tema](03-fundamentos-geodesia.md)

-   **1.4 Sistemas de Referencia de Coordenadas**

    ---

    CRS geográficos y proyectados, WGS 84, SIRGAS, MARGEN-SIRGAS, códigos EPSG e identificación de un CRS.

    [:octicons-arrow-right-24: Ir al tema](04-sistemas-referencia.md)

-   **1.5 Proyecciones cartográficas**

    ---

    Superficies desarrollables, propiedades, deformaciones y criterios para elegir una proyección.

    [:octicons-arrow-right-24: Ir al tema](05-proyecciones-cartograficas.md)

-   **1.6 Sistema UTM**

    ---

    Zonas, meridiano central, falso Este y falso Norte, zonas de Bolivia y selección de la zona adecuada.

    [:octicons-arrow-right-24: Ir al tema](06-sistema-utm.md)

</div>

### Bloque 3 · Cartografía y escala

¿Cómo se representa y se comunica el territorio?

<div class="grid cards" markdown>

-   **1.7 Fundamentos de Cartografía**

    ---

    El mapa como modelo y lenguaje, variables visuales, elementos del mapa, simbología y jerarquía visual.

    [:octicons-arrow-right-24: Ir al tema](07-fundamentos-cartografia.md)

-   **1.8 Escala cartográfica**

    ---

    Escalas numérica, verbal y gráfica; cálculos; escalas grandes y pequeñas; la escala en un SIG.

    [:octicons-arrow-right-24: Ir al tema](08-escala-cartografica.md)

-   **1.9 Escala, resolución y precisión**

    ---

    Resolución, precisión, exactitud y nivel de detalle; tipos de error; RMSE; falsa precisión.

    [:octicons-arrow-right-24: Ir al tema](09-escala-resolucion-precision.md)

-   **1.10 Generalización cartográfica**

    ---

    Selección, simplificación, agregación, desplazamiento, exageración y clasificación, y sus consecuencias.

    [:octicons-arrow-right-24: Ir al tema](10-generalizacion-cartografica.md)

</div>

### Bloque 4 · Datos geoespaciales

¿Cómo se estructura la información geográfica y cómo se evalúa?

<div class="grid cards" markdown>

-   **1.11 Modelos de representación espacial**

    ---

    Modelo vectorial y modelo ráster, sus ventajas, limitaciones y criterios de elección.

    [:octicons-arrow-right-24: Ir al tema](11-modelos-representacion.md)

-   **1.12 El dato geoespacial**

    ---

    Geometría, atributos, identificadores, topología, relaciones espaciales y metadatos.

    [:octicons-arrow-right-24: Ir al tema](12-dato-geoespacial.md)

-   **1.13 Calidad de la información geográfica**

    ---

    Elementos de calidad, evaluación, propagación del error y comunicación de la incertidumbre.

    [:octicons-arrow-right-24: Ir al tema](13-calidad-informacion.md)

</div>

### Bloque 5 · Panorama geotecnológico

¿Dónde se sitúa el SIG entre las demás tecnologías?

<div class="grid cards" markdown>

-   **1.14 SIG y otras geotecnologías**

    ---

    CAD, cartografía, GNSS, teledetección, fotogrametría y bases de datos espaciales.

    [:octicons-arrow-right-24: Ir al tema](14-sig-otras-geotecnologias.md)

-   **1.15 Ecosistema de geotecnologías**

    ---

    SIG de escritorio, móvil y web, IDE, nube, automatización, ciencia de datos y GeoAI.

    [:octicons-arrow-right-24: Ir al tema](15-ecosistema-geotecnologias.md)

</div>

---

## Cómo está organizado cada tema

Todos los temas siguen una estructura común, pensada para facilitar el estudio:

| Sección | Para qué sirve |
|---|---|
| **Objetivos de aprendizaje** | Indican qué deberías poder hacer al terminar el tema |
| **Desarrollo** | Explica los conceptos con definiciones, figuras, tablas y ejemplos |
| **Ideas clave** | Resumen los conceptos que no debes olvidar |
| **Autoevaluación** | Preguntas con respuesta desplegable para comprobar lo aprendido |
| **Actividad propuesta** | Aplica el tema al proyecto integrador |
| **Referencias** | Fuentes para profundizar |

### Convenciones de esta documentación

A lo largo del material encontrarás recuadros de distintos colores. Cada uno tiene un propósito:

!!! info "Definición"

    Presenta la definición formal de un concepto.

!!! tip "Consejo"

    Ofrece recomendaciones prácticas, atajos o formas de recordar un concepto.

!!! example "Ejemplo"

    Muestra un caso concreto, un cálculo resuelto o una aplicación real.

!!! warning "Precaución"

    Advierte sobre errores frecuentes o situaciones que requieren cuidado.

!!! danger "Idea fundamental o error grave"

    Destaca una idea central del tema o un error con consecuencias importantes.

!!! note "Nota"

    Aporta aclaraciones o conexiones con otros temas.

??? info "Para saber más"

    Los recuadros **desplegables** contienen contenido complementario: historia, detalles técnicos o temas avanzados. No son imprescindibles para seguir el curso.

---

## El proyecto integrador

!!! example "Aprender aplicando desde el primer tema"

    Cada tema termina con una **actividad sin software** que aplica los conceptos a un **problema territorial real** elegido por el estudiante: en su municipio, su institución o su área de trabajo.

    Actividad tras actividad, el estudiante va construyendo la **base conceptual de su propio proyecto SIG**: define el problema, modela el territorio, elige el sistema de referencia y la escala, evalúa sus datos y diseña su flujo de trabajo. Cuando llegue a QGIS, ya sabrá **qué quiere hacer y por qué**.

| Actividad | Tema | Producto |
|---|---|---|
| 1.1 | Identificar un problema espacial | Problema territorial y preguntas espaciales |
| 1.2 | Modelar el problema | Territorio, objetos, fenómenos, procesos y modelo conceptual |
| 1.3 | Revisar las referencias geodésicas | Coordenadas de referencia y datum de las fuentes |
| 1.4 | Inventario de sistemas de referencia | Tabla de datos con su CRS y CRS de trabajo propuesto |
| 1.5 | Elegir la proyección | Proyección para análisis, mapas y web |
| 1.6 | Definir la zona UTM | Zona, meridiano central y códigos EPSG |
| 1.7 | Diseñar el mapa | Propósito, simbología, jerarquía y boceto del mapa |
| 1.8 | Trabajar con escalas | Escala de trabajo y precisión gráfica |
| 1.9 | Evaluar la aptitud de los datos | Tabla de resolución, exactitud y aptitud de cada dato |
| 1.10 | Generalizar | Operaciones y tolerancias para una escala menor |
| 1.11 | Definir el modelo lógico | Modelo vectorial o ráster, geometrías y formatos |
| 1.12 | Documentar un dato | Diccionario de datos, reglas topológicas y metadatos |
| 1.13 | Plan de calidad | Requisitos, evaluación, propagación del error y linaje |
| 1.14 | Mapa de geotecnologías | Flujo de datos entre geotecnologías |
| 1.15 | Ecosistema del proyecto | Ecosistema tecnológico y síntesis final del proyecto |

!!! tip "Elige bien tu problema"

    Un buen problema para el proyecto integrador:

    - Es **real** y tiene relevancia para una institución o una comunidad.
    - Es **espacial**: su respuesta cambia según la ubicación (tema 1.1).
    - Tiene un **área de estudio acotada**, como un municipio, un distrito o una cuenca.
    - Cuenta con **datos disponibles** o que se pueden conseguir.

    *Ejemplos:* cobertura de unidades educativas en un distrito, zonas de riesgo de inundación en un área urbana, cambio de uso de suelo en una cuenca, accesibilidad a centros de salud en un municipio rural.

---

## Recomendaciones para el estudio

- **Sigue el orden de los temas.** Los conceptos se construyen unos sobre otros.
- **Haz los cálculos a mano.** Las conversiones de coordenadas, las escalas y el RMSE se entienden mucho mejor al calcularlos que al leerlos.
- **Responde la autoevaluación antes de desplegar las respuestas.**
- **No saltes las actividades.** El proyecto integrador es el hilo conductor del curso.
- **Relaciona los temas con tu realidad.** Busca en tu trabajo o tu municipio ejemplos de cada concepto.
- **Vuelve a este módulo** cuando, más adelante, algo no funcione en QGIS: la respuesta casi siempre está en un concepto de aquí.

!!! note "Materiales necesarios"

    Para este módulo **no se necesita software**. Basta con:

    - Una **calculadora** (la de la computadora o el celular sirve).
    - Un **cuaderno** o documento para el proyecto integrador.
    - Opcionalmente, una **carta topográfica** impresa y un **celular con GNSS** para algunas actividades.

---

## Al terminar el módulo

!!! success "Estarás preparado para el Módulo 2 si puedes:"

    - Explicar por qué una coordenada sin sistema de referencia no es una ubicación.
    - Diferenciar un CRS geográfico de uno proyectado y elegir la zona UTM correcta para un lugar de Bolivia.
    - Calcular distancias y superficies a partir de una escala.
    - Explicar la diferencia entre precisión y exactitud.
    - Decidir si un dato es adecuado para una escala y un propósito determinados.
    - Describir los componentes de un dato geoespacial y elaborar sus metadatos básicos.
    - Explicar por qué un análisis nunca puede ser mejor que los datos que lo sustentan.

En el **Módulo 2** comenzaremos a trabajar con **QGIS**: instalación, interfaz y proyectos. Y en el **Módulo 3** aplicaremos en el software todo lo que aprendimos sobre sistemas de referencia.

---

## Bibliografía general del módulo

Estas obras sirven de referencia para todo el módulo. Cada tema incluye, además, sus referencias específicas.

- Burrough, P. A., & McDonnell, R. A. (1998). *Principles of Geographical Information Systems*. Oxford University Press.
- Kraak, M.-J., & Ormeling, F. (2020). *Cartography: Visualization of Geospatial Data* (4.ª ed.). CRC Press.
- Longley, P. A., Goodchild, M. F., Maguire, D. J., & Rhind, D. W. (2015). *Geographic Information Science and Systems* (4.ª ed.). Wiley.
- Olaya, V. (2016). *Introducción a los Sistemas de Información Geográfica*. Versión resumida y libre, pensada como texto de lectura. <https://volaya.github.io/gis-book/es/>
- Olaya, V. (2020). *Sistemas de Información Geográfica*. Libro libre de consulta disponible en línea. <https://volaya.github.io/libro-sig/>
- Snyder, J. P. (1987). *Map Projections: A Working Manual* (U.S. Geological Survey Professional Paper 1395). U.S. Government Printing Office.
- Torge, W., & Müller, J. (2012). *Geodesy* (4.ª ed.). De Gruyter.
