---
title: Glosario
description: Términos clave del curso con su definición breve, equivalente en inglés y lección donde se desarrollan.
---

# Glosario

Definiciones breves de los términos usados en el curso. El término en **negrita** es el que usamos siempre; entre paréntesis, el equivalente inglés que encontrarás en documentación y foros.

[A](#a) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [I](#i) · [L](#l) · [M](#m) · [N](#n) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w)

---

## A

**Atlas** (*atlas*)
:   Conjunto de mapas generados automáticamente a partir de una composición y una capa de cobertura: una página por entidad. → [4.10](modulo-04/10-producir-atlas-territorial.md)

**Atributo** (*attribute*)
:   Dato descriptivo asociado a una entidad, almacenado en un campo de la tabla de atributos. → [1.12](modulo-01/12-dato-geoespacial.md)

**Autoensamblado** (*snapping*)
:   Ajuste automático de un vértice a otro vértice o segmento cercano durante la edición, para evitar huecos y superposiciones. → [3.2](modulo-03/02-digitalizar-editar-precision.md)

## C

**Campo virtual** (*virtual field*)
:   Campo calculado mediante una expresión que se actualiza solo y no se guarda en la fuente de datos. → [3.4](modulo-03/04-construir-indicadores-expresiones.md)

**Capa** (*layer*)
:   Representación en un proyecto QGIS de una fuente de datos, con su estilo y propiedades. La capa no *es* el dato: apunta a él. → [2.3](modulo-02/03-gestionar-proyectos.md)

**Cardinalidad** (*cardinality*)
:   Número de registros de una tabla que corresponden a un registro de otra: uno a uno, uno a muchos, muchos a muchos. → [3.5](modulo-03/05-integrar-tablas.md)

**Clasificación** (*classification*)
:   Agrupación de valores en clases para su representación: intervalos iguales, cuantiles, rupturas naturales (Jenks), etc. → [4.4](modulo-04/04-evaluar-clasificaciones-colores.md)

**Composición de impresión** (*print layout*)
:   Página diseñada en QGIS que combina mapas, leyenda, escala, títulos y otros elementos para imprimir o exportar. → [4.7](modulo-04/07-disenar-composicion-reutilizable.md)

**Coropleta** (*choropleth*)
:   Mapa que colorea unidades de área según el valor de una variable, normalmente una tasa o densidad. → [4.3](modulo-04/03-elegir-representacion-tematica.md)

## D

**Datum** (*datum*)
:   Conjunto de parámetros que fija la posición y orientación de un elipsoide respecto de la Tierra. → [1.3](modulo-01/03-fundamentos-geodesia.md)

**Digitalizar** (*digitize*)
:   Crear geometrías vectoriales dibujándolas sobre una referencia (imagen, mapa escaneado). → [3.2](modulo-03/02-digitalizar-editar-precision.md)

## E

**Elipsoide** (*ellipsoid*)
:   Superficie matemática que aproxima la forma de la Tierra y sirve de base para las coordenadas geográficas. → [1.3](modulo-01/03-fundamentos-geodesia.md)

**Entidad** (*feature*)
:   Cada elemento de una capa vectorial: una geometría más sus atributos (una fila de la tabla). → [1.12](modulo-01/12-dato-geoespacial.md)

**EPSG** (*EPSG code*)
:   Código numérico que identifica un sistema de referencia en el registro de la IOGP. Ej.: EPSG:4326 (WGS 84), EPSG:32719 (WGS 84 / UTM 19 S). → [1.4](modulo-01/04-sistemas-referencia.md)

**Escala** (*scale*)
:   Relación entre una distancia en el mapa y la distancia correspondiente en el terreno. 1:50 000 es una escala *mayor* que 1:250 000. → [1.8](modulo-01/08-escala-cartografica.md)

**Estadísticas zonales** (*zonal statistics*)
:   Resumen de los valores de un ráster (media, máximo…) dentro de cada polígono de una capa. → [3.9](modulo-03/09-relieve-estadisticas-zonales.md)

**Exactitud** (*accuracy*)
:   Cercanía de un valor medido al valor verdadero. No confundir con *precisión*. → [1.9](modulo-01/09-escala-resolucion-precision.md)

**Expresión** (*expression*)
:   Fórmula escrita en el lenguaje de expresiones de QGIS para calcular, filtrar o etiquetar. → [3.4](modulo-03/04-construir-indicadores-expresiones.md)

## F

**Filtro de capa** (*layer filter, provider filter*)
:   Condición que limita qué entidades de la fuente muestra una capa, sin borrar datos. → [2.8](modulo-02/08-seleccionar-filtrar.md)

## G

**Generalización** (*generalization*)
:   Conjunto de operaciones (selección, simplificación, agregación, desplazamiento…) que adaptan los datos a una escala menor. → [1.10](modulo-01/10-generalizacion-cartografica.md)

**Geoide** (*geoid*)
:   Superficie equipotencial del campo gravitatorio que coincide aproximadamente con el nivel medio del mar; referencia de las alturas ortométricas. → [1.3](modulo-01/03-fundamentos-geodesia.md)

**GeoPackage** (*GeoPackage*)
:   Formato abierto del OGC basado en SQLite que guarda varias capas vectoriales, ráster y estilos en un solo archivo `.gpkg`. Formato recomendado en el curso. → [2.4](modulo-02/04-incorporar-datos.md)

**Georreferenciar** (*georeference*)
:   Asignar coordenadas a una imagen o mapa escaneado mediante puntos de control. → [3.10](modulo-03/10-georreferenciar-mapas-historicos.md)

**GNSS** (*Global Navigation Satellite System*)
:   Sistemas de posicionamiento por satélite: GPS, GLONASS, Galileo, BeiDou. → [1.14](modulo-01/14-sig-otras-geotecnologias.md)

## I

**IDE · Infraestructura de datos espaciales** (*SDI*)
:   Conjunto de políticas, estándares, servicios y datos que permiten compartir información geográfica. En Bolivia: GeoBolivia. → [1.15](modulo-01/15-ecosistema-geotecnologias.md)

## L

**LTR** (*Long Term Release*)
:   Versión de QGIS con soporte extendido, recomendada para instituciones y cursos. → [2.1](modulo-02/01-entorno-trabajo.md)

## M

**Metadatos** (*metadata*)
:   Datos sobre los datos: origen, fecha, SRC, escala, calidad, licencia, responsable. → [1.12](modulo-01/12-dato-geoespacial.md)

**Modelador gráfico** (*Graphical Modeler*)
:   Herramienta de QGIS para encadenar algoritmos de Procesos en un flujo reutilizable. → [3.11](modulo-03/11-procedimientos-reproducibles.md)

**MDE · Modelo digital de elevación** (*DEM*)
:   Ráster cuyas celdas almacenan la altura del terreno. → [3.9](modulo-03/09-relieve-estadisticas-zonales.md)

## N

**NoData** (*NoData*)
:   Valor de celda que indica ausencia de dato en un ráster. → [2.10](modulo-02/10-explorar-raster.md)

**NULL** (*NULL*)
:   Ausencia de valor en un campo. No es lo mismo que cero ni que texto vacío. → [2.7](modulo-02/07-leer-datos.md)

## P

**Precisión** (*precision*)
:   Grado de repetibilidad o detalle de una medición. Un dato puede ser muy preciso y poco exacto. → [1.9](modulo-01/09-escala-resolucion-precision.md)

**Predicado espacial** (*spatial predicate*)
:   Relación geométrica que se evalúa entre dos entidades: interseca, contiene, está dentro, toca, cruza, se superpone, disjunto. → [3.6](modulo-03/06-relaciones-espaciales.md)

**Procesos** (*Processing*)
:   Marco de QGIS que reúne los algoritmos de análisis en la caja de herramientas de Procesos. → [3.11](modulo-03/11-procedimientos-reproducibles.md)

**Proyección cartográfica** (*map projection*)
:   Transformación matemática de coordenadas del elipsoide a un plano. Siempre introduce deformaciones. → [1.5](modulo-01/05-proyecciones-cartograficas.md)

**Proyecto** (*project*)
:   Archivo `.qgz` que guarda capas, estilos, composiciones y referencias a las fuentes de datos, pero no los datos mismos. → [2.3](modulo-02/03-gestionar-proyectos.md)

## R

**Ráster** (*raster*)
:   Modelo que representa el espacio como una matriz de celdas (píxeles) con un valor cada una. Invariable en plural: «los ráster». → [1.11](modulo-01/11-modelos-representacion.md)

**Remuestreo** (*resampling*)
:   Cálculo de nuevos valores de celda al cambiar la resolución o el SRC de un ráster: vecino más cercano, bilineal, cúbico. → [3.8](modulo-03/08-preparar-combinar-raster.md)

**Reproyectar** (*reproject, transform*)
:   Recalcular las coordenadas de un dato de un SRC a otro. Cambia los números. No confundir con *asignar* un SRC. → [2.6](modulo-02/06-problemas-coordenadas.md)

**Resolución** (*resolution*)
:   Tamaño del menor detalle que un dato puede distinguir; en un ráster, el tamaño de la celda. → [1.9](modulo-01/09-escala-resolucion-precision.md)

**Ruta relativa** (*relative path*)
:   Ruta a un archivo expresada desde la carpeta del proyecto; permite mover o compartir el proyecto sin romper capas. → [2.3](modulo-02/03-gestionar-proyectos.md)

**RMSE · Error medio cuadrático** (*Root Mean Square Error*)
:   Medida de exactitud posicional que resume las diferencias entre posiciones medidas y de referencia. → [1.9](modulo-01/09-escala-resolucion-precision.md)

## S

**SIG · Sistema de Información Geográfica** (*GIS*)
:   Sistema de personas, métodos, datos, software y hardware para capturar, gestionar, analizar y representar información localizada. → [1.1](modulo-01/01-sistemas-informacion-geografica.md)

**SIRGAS** (*Sistema de Referencia Geocéntrico para las Américas*)
:   Marco de referencia regional; en Bolivia se materializa mediante MARGEN-SIRGAS, a cargo del IGM. → [1.4](modulo-01/04-sistemas-referencia.md)

**SRC · Sistema de referencia de coordenadas** (*CRS, Coordinate Reference System*)
:   Definición completa que permite interpretar coordenadas: datum, elipsoide y, si es proyectado, la proyección y sus parámetros. Es el término usado en la interfaz de QGIS en español. → [1.4](modulo-01/04-sistemas-referencia.md)

**Asignar un SRC** (*assign / set CRS*)
:   Declarar en qué SRC están las coordenadas de un dato, sin cambiarlas. Solo corrige si la declaración anterior era errónea. → [2.6](modulo-02/06-problemas-coordenadas.md)

**Simbología** (*symbology*)
:   Reglas que definen cómo se dibujan las entidades: simple, categorizada, graduada, por reglas. → [2.9](modulo-02/09-simbologia-etiquetas.md)

## T

**Tabla de atributos** (*attribute table*)
:   Vista tabular de las entidades de una capa vectorial: una fila por entidad, una columna por campo. → [2.7](modulo-02/07-leer-datos.md)

**Topología** (*topology*)
:   Relaciones de vecindad, conectividad y contención entre geometrías, y reglas que las validan (sin huecos, sin superposiciones). → [1.12](modulo-01/12-dato-geoespacial.md)

## U

**Unión espacial** (*spatial join*)
:   Transferencia de atributos de una capa a otra según una relación espacial. → [3.6](modulo-03/06-relaciones-espaciales.md)

**Unión por atributos** (*table join*)
:   Combinación de dos tablas mediante un campo clave común. → [3.5](modulo-03/05-integrar-tablas.md)

**UTM · Universal Transversa de Mercator** (*UTM*)
:   Sistema de 60 zonas de 6° con proyección transversa de Mercator. Bolivia ocupa las zonas 19, 20 y 21 Sur. → [1.6](modulo-01/06-sistema-utm.md)

## V

**Vectorial** (*vector*)
:   Modelo que representa objetos discretos mediante puntos, líneas y polígonos definidos por coordenadas. → [1.11](modulo-01/11-modelos-representacion.md)

## W

**WFS / WMS / WMTS** (*Web Feature / Map / Map Tile Service*)
:   Estándares OGC para servir entidades vectoriales (WFS), imágenes de mapa (WMS) o teselas (WMTS) por internet. → [2.11](modulo-02/11-servicios-web.md)

**WGS 84** (*World Geodetic System 1984*)
:   Sistema de referencia global del GPS. Como SRC geográfico: EPSG:4326. → [1.4](modulo-01/04-sistemas-referencia.md)
