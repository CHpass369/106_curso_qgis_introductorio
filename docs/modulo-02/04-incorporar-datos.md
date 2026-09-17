---
title: 2.4 Incorporar datos y reconocer sus diferencias
description: Incorporación e inspección de datos vectoriales y ráster en QGIS; diferencias entre GeoPackage, Shapefile, GeoJSON y GeoTIFF; geometrías, extensión, campos, bandas y metadatos.
---

# 2.4 Incorporar datos y reconocer sus diferencias

!!! abstract "Objetivos de aprendizaje"

    Al finalizar esta lección, el estudiante será capaz de:

    - Diferenciar datos **vectoriales** y **ráster** a partir de su estructura.
    - Reconocer las características principales de **GeoPackage, Shapefile, GeoJSON y GeoTIFF**.
    - Incorporar fuentes de datos al proyecto utilizando el **panel Navegador** y las herramientas para añadir capas.
    - Identificar el **tipo de geometría**, número de entidades, extensión y campos de una capa vectorial.
    - Identificar las **dimensiones, resolución, bandas, tipo de dato y valores NoData** de una capa ráster.
    - Consultar información básica sobre el **SRC** y los metadatos de una fuente.
    - Elaborar un **inventario de datos** antes de utilizarlos.
    - Decidir si una fuente puede utilizarse directamente, requiere preparación o no resulta adecuada para el trabajo.

!!! note "Antes de empezar"

    - **Entorno:** QGIS con el perfil `curso-qgis`. Los procedimientos toman como referencia **QGIS 3.44**; algunos nombres de botones pueden variar según la traducción utilizada.
    - **Punto de partida:** el proyecto organizado durante la [lección 2.3](03-gestionar-proyectos.md).
    - **Datos:** para aprovechar completamente la práctica conviene disponer de al menos una fuente en cada uno de estos formatos:
        - GeoPackage (`.gpkg`)
        - Shapefile (`.shp` y archivos asociados)
        - GeoJSON (`.geojson`)
        - GeoTIFF (`.tif`)
    - **Edición:** no modificaremos todavía las geometrías ni los valores originales. El objetivo es **observar, describir y evaluar**.
    - **SRC:** en esta lección solo reconoceremos qué sistema tiene cada fuente. Los sistemas de referencia se estudiarán con mayor profundidad en la lección **2.6**.
    - **Tiempo orientativo:** entre **90 y 120 minutos**, incluida la práctica.

---

## No todo archivo geográfico contiene lo mismo

Imagina que recibes una carpeta denominada `datos_municipio/` con estos archivos:

```text
datos_municipio/
├── limites.gpkg
├── rios.shp
├── rios.dbf
├── rios.shx
├── rios.prj
├── equipamientos.geojson
└── elevacion.tif
```

Todos contienen información geográfica, pero **no representan los datos de la misma manera**.

`limites.gpkg`, `rios.shp` y `equipamientos.geojson` pueden almacenar **entidades vectoriales**. `elevacion.tif`, en cambio, puede representar una superficie mediante una matriz de **píxeles**.

Antes de utilizar cualquiera de ellos necesitas responder preguntas como:

- ¿Qué fenómeno representa?
- ¿Es vectorial o ráster?
- ¿Qué geometría contiene?
- ¿Cuál es su extensión territorial?
- ¿Qué atributos tiene?
- ¿Cuál es su sistema de referencia?
- ¿De dónde proviene?
- ¿Está completo?
- ¿Tiene la resolución o nivel de detalle necesario?
- ¿Es adecuado para el análisis que realizaré?

La tarea de esta lección consiste en pasar de **“tengo varios archivos”** a **“sé qué datos tengo y para qué pueden utilizarse”**.

!!! captura "Captura pendiente · 2.4-01"

    - **Tipo:** Imagen (PNG) compuesta
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-01-datos-recibidos.png`
    - **Qué mostrar:** Una carpeta con archivos GPKG, Shapefile, GeoJSON y GeoTIFF junto a QGIS.
    - **Sugerencia:** Diferenciar visualmente los archivos de una fuente vectorial y el archivo ráster, sin presentar todavía demasiados conceptos.

---

## Dos modelos fundamentales: vectorial y ráster

### Datos vectoriales

El modelo vectorial representa objetos mediante **geometrías** asociadas a registros de una tabla.

Sus tres formas básicas son:

| Geometría | Representa normalmente | Ejemplos |
|---|---|---|
| **Punto** | Objetos cuya posición es lo importante | Pozos, árboles, paradas, establecimientos |
| **Línea** | Elementos con recorrido o longitud | Ríos, calles, tuberías |
| **Polígono** | Objetos con superficie delimitada | Municipios, predios, lagunas |

Cada entidad puede tener información descriptiva almacenada en **campos**.

Por ejemplo:

| id | nombre | poblacion | geometría |
|---:|---|---:|---|
| 1 | Distrito Norte | 28450 | Polígono |
| 2 | Distrito Centro | 41520 | Polígono |
| 3 | Distrito Sur | 33110 | Polígono |

La geometría responde principalmente a **dónde está y qué forma tiene** el objeto.

Los atributos permiten responder **qué sabemos sobre él**.

!!! tip "Entidad no significa solamente geometría"

    Una entidad vectorial combina normalmente una **geometría** con un registro de **atributos**. Dos polígonos pueden tener formas similares pero representar objetos diferentes por sus atributos, fecha o procedencia.

---

### Datos ráster

Un ráster organiza el espacio mediante una matriz regular de **celdas o píxeles**.

Cada píxel almacena uno o varios valores.

Ejemplos frecuentes:

- imágenes satelitales;
- fotografías aéreas;
- modelos digitales de elevación;
- temperatura;
- precipitación;
- cobertura del suelo;
- pendientes;
- índices de vegetación.

Una estructura simplificada podría imaginarse así:

```text
1250  1252  1255  1258
1248  1251  1254  1257
1246  1249  1253  1256
1244  1247  1250  1254
```

En un modelo digital de elevación, cada número podría representar una **altitud**.

En una imagen satelital, diferentes bandas pueden representar distintas regiones del espectro electromagnético.

!!! captura "Captura pendiente · 2.4-02"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-02-vector-raster.png`
    - **Qué mostrar:** A la izquierda puntos, líneas y polígonos; a la derecha una cuadrícula ráster ampliada hasta distinguir los píxeles.
    - **Sugerencia:** Representar aproximadamente la misma zona para facilitar la comparación.

---

## Vector y ráster responden preguntas diferentes

| Característica | Vector | Ráster |
|---|---|---|
| Unidad principal | Entidad | Píxel |
| Estructura espacial | Punto, línea o polígono | Matriz de celdas |
| Información descriptiva | Campos y atributos | Valores de píxel y bandas |
| Ejemplo | Predios | Imagen aérea |
| Cantidad característica | Número de entidades | Filas × columnas |
| Detalle espacial | Geometría | Tamaño del píxel |
| Consulta típica | ¿Qué atributos tiene este predio? | ¿Qué valor tiene este píxel? |

No existe un modelo universalmente “mejor”.

La elección depende del fenómeno, del origen de los datos y del análisis que necesitas realizar.

---

## El formato no es lo mismo que el modelo de datos

**Vectorial** y **ráster** describen formas de representar información.

**GeoPackage**, **Shapefile**, **GeoJSON** y **GeoTIFF** son formatos utilizados para almacenarla.

En esta lección trabajaremos principalmente con:

| Formato | Extensión habitual | Tipo principal | Característica |
|---|---|---|---|
| **GeoPackage** | `.gpkg` | Vectorial y otros contenidos | Contenedor basado en SQLite |
| **Shapefile** | `.shp` + archivos asociados | Vectorial | Conjunto compuesto por varios archivos |
| **GeoJSON** | `.geojson`, `.json` | Vectorial | Formato de texto basado en JSON |
| **GeoTIFF** | `.tif`, `.tiff` | Ráster | Imagen ráster con información geográfica |

!!! warning "La extensión no cuenta toda la historia"

    Reconocer `.shp` o `.tif` ayuda a identificar un formato, pero no permite saber automáticamente **qué representa**, cuál es su fecha, qué calidad tiene o si resulta adecuado para tu trabajo. Debes inspeccionar también su contenido y metadatos.

---

# GeoPackage

## Un archivo que puede contener varias capas

Un **GeoPackage**, normalmente identificado mediante `.gpkg`, funciona como un contenedor basado en SQLite.

Un mismo archivo puede contener varias capas.

Por ejemplo:

```text
municipio.gpkg
├── distritos
├── vias
├── establecimientos_salud
└── areas_verdes
```

Por esta razón debes distinguir:

- el **archivo GeoPackage**;
- la **capa interna** que quieres utilizar.

Al incorporar un GeoPackage con varias capas, QGIS puede solicitarte seleccionar cuáles quieres añadir.

!!! captura "Captura pendiente · 2.4-03"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-03-geopackage-capas.gif`
    - **Qué mostrar:** Expandir un `.gpkg` desde el Navegador y observar varias capas internas; añadir solamente una.
    - **Sugerencia:** Mantener visible el nombre del archivo y los nombres de las capas para reforzar la diferencia entre contenedor y capa.

### Ventajas para el trabajo cotidiano

GeoPackage resulta especialmente práctico porque:

- puede reunir varias capas en un único archivo;
- mantiene geometrías y atributos juntos;
- admite nombres y estructuras de campos más flexibles que formatos antiguos;
- facilita trasladar conjuntos de datos;
- puede utilizar índices espaciales;
- es ampliamente compatible con QGIS y otras herramientas SIG.

En este curso será normalmente el **formato de trabajo preferido para datos vectoriales locales**, salvo que una actividad requiera otro.

!!! warning "Un solo archivo puede contener muchas cosas"

    Copiar `municipio.gpkg` suele ser suficiente para trasladar las capas almacenadas dentro del contenedor, pero eso no significa que todas las capas tengan la misma procedencia, fecha o propósito. Debes documentarlas individualmente cuando corresponda.

---

# Shapefile

## Una fuente formada por varios archivos

Aunque habitualmente hablamos de “un Shapefile”, una fuente Shapefile está compuesta por varios archivos relacionados.

Como mínimo encontrarás normalmente:

```text
rios.shp
rios.shx
rios.dbf
```

Pueden existir además otros archivos como:

```text
rios.prj
rios.cpg
rios.qix
```

Entre los componentes más habituales:

| Extensión | Función general |
|---|---|
| `.shp` | Geometrías |
| `.dbf` | Tabla de atributos |
| `.shx` | Índice que relaciona las geometrías |
| `.prj` | Información sobre el sistema de referencia |
| `.cpg` | Información de codificación de caracteres |
| `.qix` | Índice espacial utilizado para acelerar determinadas consultas |

!!! danger "No copies solamente el SHP"

    Si recibes `rios.shp`, no debes asumir que ese único archivo constituye toda la fuente. Conserva juntos sus archivos asociados.

Esta particularidad ya apareció en la lección anterior al preparar proyectos para compartir. Ahora puedes explicar **por qué** era necesario hacerlo.

### Limitaciones que debes reconocer

Shapefile continúa siendo ampliamente utilizado y resulta útil para intercambio con sistemas antiguos, pero tiene restricciones heredadas de su diseño.

Entre ellas pueden aparecer:

- limitaciones en nombres de campos;
- restricciones en determinados tipos de atributos;
- dependencia de varios archivos;
- problemas de codificación cuando falta información complementaria;
- menor flexibilidad que formatos modernos.

!!! note "Shapefile no significa dato incorrecto"

    Una fuente Shapefile puede ser perfectamente válida. El formato por sí solo no determina la calidad de la información. La decisión depende de su contenido, integridad, procedencia y del trabajo que necesitas realizar.

---

# GeoJSON

## Información geográfica escrita como texto

GeoJSON representa entidades geográficas utilizando estructuras **JSON**.

Un fragmento simplificado puede tener esta forma:

```json
{
  "type": "Feature",
  "properties": {
    "nombre": "Plaza principal"
  },
  "geometry": {
    "type": "Point",
    "coordinates": [-66.15, -17.39]
  }
}
```

No necesitas editar manualmente este contenido durante la práctica.

Lo importante es reconocer que GeoJSON es un formato de texto y que resulta frecuente en:

- aplicaciones web;
- APIs;
- intercambio de información;
- publicación de datos;
- flujos de trabajo con programación.

!!! captura "Captura pendiente · 2.4-04"

    - **Tipo:** Imagen (PNG) compuesta
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-04-geojson-texto-qgis.png`
    - **Qué mostrar:** El mismo GeoJSON abierto como texto y representado en QGIS.
    - **Sugerencia:** Resaltar `properties`, `geometry` y `coordinates`, sin convertir la captura en una clase de programación.

!!! note "GeoJSON y sistemas de referencia"

    Algunas variantes históricas permiten declarar sistemas de referencia de diferentes maneras. Cuando se trabaja conforme a **RFC 7946**, GeoJSON utiliza coordenadas geográficas WGS 84. No asumas el SRC solamente por la apariencia del mapa: revisa cómo QGIS interpreta la fuente.

---

# GeoTIFF

## Una imagen que conoce su posición geográfica

Un archivo TIFF convencional contiene una imagen.

Un **GeoTIFF** puede incorporar además información necesaria para situar el ráster en el espacio geográfico.

Por ejemplo:

```text
elevacion.tif
```

podría contener:

- 2 000 columnas;
- 1 500 filas;
- tamaño de píxel de 10 m;
- una banda;
- valores de elevación;
- un determinado sistema de referencia.

Otro GeoTIFF podría contener una imagen multibanda obtenida mediante un sensor remoto.

Por eso saber que un archivo es `.tif` todavía no responde qué información contiene.

---

## Las bandas

Una capa ráster puede tener **una o varias bandas**.

Ejemplos:

| Dataset | Bandas posibles |
|---|---|
| Modelo digital de elevación | 1 banda |
| Clasificación de cobertura | 1 banda |
| Fotografía RGB | 3 bandas |
| Imagen satelital multiespectral | Varias bandas |

En QGIS puedes revisar el número de bandas desde **Propiedades de la capa ▸ Información**.

!!! captura "Captura pendiente · 2.4-05"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-05-raster-informacion.png`
    - **Qué mostrar:** Propiedades de un GeoTIFF destacando dimensiones, número de bandas, tipo de dato, tamaño de píxel, extensión y SRC.
    - **Sugerencia:** Numerar solamente las propiedades que el estudiante deberá registrar posteriormente en su inventario.

---

# Incorporar datos al proyecto

QGIS permite incorporar información desde diferentes lugares de la interfaz.

Para esta práctica utilizaremos principalmente dos métodos:

1. **Panel Navegador**
2. **Añadir capa / Administrador de fuentes de datos**

---

## Utilizar el panel Navegador

El Navegador permite explorar carpetas y determinadas fuentes sin incorporarlas inmediatamente al proyecto.

### Procedimiento

1. Localiza la carpeta `datos/originales/`.
2. Expándela en el panel **Navegador**.
3. Observa los archivos disponibles.
4. Si encuentras un GeoPackage, expándelo para observar sus capas internas.
5. Arrastra una capa hasta el lienzo o haz doble clic para incorporarla.
6. Observa cómo aparece en el panel **Capas**.

!!! tip "Navegador y Capas cumplen funciones diferentes"

    **Navegador** muestra fuentes que puedes explorar.

    **Capas** muestra los elementos incorporados al proyecto actual.

Una fuente puede existir en el Navegador sin formar parte de tu proyecto.

---

## Utilizar Añadir capa

También puedes utilizar las acciones de **Capa ▸ Añadir capa** o el **Administrador de fuentes de datos**.

Dependiendo del tipo de fuente encontrarás opciones específicas para:

- vector;
- ráster;
- texto delimitado;
- bases de datos;
- servicios web;
- otras fuentes.

Para los archivos de esta lección, QGIS suele poder reconocer automáticamente el proveedor correspondiente.

!!! captura "Captura pendiente · 2.4-06"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-06-incorporar-datos.gif`
    - **Qué mostrar:** Incorporar un GPKG, un Shapefile, un GeoJSON y un GeoTIFF, alternando entre Navegador y Administrador de fuentes.
    - **Sugerencia:** Evitar configurar simbología; el objetivo del GIF es mostrar cómo se incorporan las fuentes.

---

# Inspeccionar antes de utilizar

Que una capa aparezca correctamente en el mapa **no demuestra que sea la fuente adecuada**.

Para una primera evaluación revisaremos al menos:

### Si es vectorial

- formato;
- nombre de la capa;
- tipo de geometría;
- número de entidades;
- extensión;
- sistema de referencia;
- campos;
- tipos de campos;
- valores de ejemplo;
- procedencia y metadatos.

### Si es ráster

- formato;
- número de columnas;
- número de filas;
- tamaño de píxel;
- número de bandas;
- tipo de dato;
- valores NoData;
- extensión;
- sistema de referencia;
- metadatos y procedencia.

Estos elementos constituyen una **ficha mínima de reconocimiento**.

---

# Reconocer la geometría

Haz clic derecho sobre una capa vectorial y abre:

**Propiedades ▸ Información**

Localiza su tipo de geometría.

Podrás encontrar denominaciones relacionadas con:

- Point;
- MultiPoint;
- LineString;
- MultiLineString;
- Polygon;
- MultiPolygon.

En esta etapa no necesitas memorizar todas sus variantes.

Lo importante es distinguir inicialmente:

**punto → línea → polígono**

y reconocer que pueden existir geometrías **simples** y **multipartes**.

!!! tip "La apariencia puede engañar"

    No determines el tipo de geometría solamente mirando el mapa. Un punto con un símbolo muy grande puede parecer una superficie y un polígono muy pequeño puede parecer un punto. Consulta las propiedades de la fuente.

---

## Geometría y fenómeno deben tener sentido juntos

Imagina una capa llamada:

```text
hospitales
```

Si su geometría es de tipo punto, puede ser completamente razonable para determinadas escalas de trabajo.

Ahora imagina:

```text
limites_municipales
```

pero la capa contiene solamente puntos.

No necesariamente está dañada, pero debes investigar qué representan realmente esos puntos antes de utilizarla como delimitación administrativa.

!!! question "Pregunta de control"

    Una capa se llama `rios`, pero contiene polígonos.

    ¿Está necesariamente equivocada?

    No. Podría representar superficies de cuerpos de agua o cauces delimitados. **El nombre de la capa no es suficiente para determinar su significado.**

---

# El número de entidades

Para una capa vectorial es útil registrar cuántos objetos contiene.

Por ejemplo:

```text
Capa: establecimientos_salud
Entidades: 84
```

Este número puede utilizarse como un primer control.

Si posteriormente recibes otra versión con solamente 12 entidades, existe una diferencia que debes investigar.

!!! warning "Cantidad no equivale a calidad"

    Dos capas pueden tener exactamente el mismo número de entidades y contener información diferente. El conteo es un control útil, pero debe combinarse con geometría, atributos, extensión, fecha y procedencia.

---

# Comprender la extensión

La **extensión espacial** o *extent* es el rectángulo mínimo que contiene espacialmente una capa.

Puede expresarse mediante valores como:

```text
X mínima
X máxima
Y mínima
Y máxima
```

Visualmente:

```text
┌─────────────────────────────┐
│                             │
│       datos de la capa      │
│           ● ●               │
│      ●          ●           │
│          ●                  │
│                             │
└─────────────────────────────┘
```

El rectángulo exterior representa aproximadamente la **extensión**.

!!! danger "Extensión no significa cobertura completa"

    Una capa puede tener una extensión que abarque todo un municipio y contener solamente cinco puntos dentro de él.

Por ello debes diferenciar:

**extensión espacial**

de

**cobertura efectiva de los datos**.

---

## Detectar extensiones sospechosas

Supongamos que esperas datos correspondientes únicamente a un municipio, pero al usar:

**Zoom a la capa**

el mapa muestra prácticamente todo el continente.

Podría existir:

- una entidad localizada incorrectamente;
- una geometría anómala;
- un problema relacionado con coordenadas;
- una fuente que contiene información de un territorio mucho mayor.

Todavía no corregiremos estos problemas.

Por ahora debes **detectarlos y documentarlos**.

!!! captura "Captura pendiente · 2.4-07"

    - **Tipo:** Imagen (PNG) comparativa
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-07-extension.png`
    - **Qué mostrar:** Una capa con extensión razonable y otra con una entidad anómala que amplía enormemente su extensión.
    - **Sugerencia:** Utilizar el mismo lienzo y remarcar el rectángulo conceptual de extensión.

---

# Examinar los campos

Abre la **tabla de atributos** de una capa vectorial.

Encontrarás columnas como:

```text
id
nombre
categoria
poblacion
fecha
```

Cada columna corresponde a un **campo**.

Cada fila representa normalmente una **entidad**.

---

## El nombre del campo no define su contenido

Un campo denominado:

```text
POBLACION
```

podría contener números enteros.

Pero también podría haber sido creado como texto:

```text
"12450"
"9820"
"15003"
```

Visualmente parecen números, pero su **tipo de dato** puede impedir determinadas operaciones matemáticas.

Por ello debes comprobar:

- nombre del campo;
- tipo;
- longitud o precisión cuando corresponda;
- valores de ejemplo;
- presencia de valores nulos.

---

## Tipos habituales de campos

| Tipo conceptual | Ejemplo |
|---|---|
| Entero | `1532` |
| Decimal | `17.42` |
| Texto | `Distrito Norte` |
| Fecha | `2026-09-16` |
| Fecha y hora | `2026-09-16 10:35` |
| Booleano | verdadero / falso |

Los tipos disponibles dependen también del formato utilizado.

!!! warning "Vacío, cero y NULL no significan necesariamente lo mismo"

    - `0` puede ser un valor numérico válido.
    - `""` puede representar texto vacío.
    - `NULL` representa ausencia de valor.

    No reemplaces automáticamente uno por otro sin entender el significado del campo.

---

# Inspeccionar un ráster

Para una capa GeoTIFF abre:

**Propiedades ▸ Información**

Registra como mínimo:

```text
Columnas:
Filas:
Número de bandas:
Tipo de dato:
Tamaño de píxel:
NoData:
Extensión:
SRC:
```

---

## Filas y columnas

Un ráster de:

```text
3000 columnas × 2000 filas
```

contiene:

```text
6 000 000 de píxeles
```

por banda.

Esto permite comenzar a comprender por qué determinados ráster pueden ocupar mucho espacio o requerir más procesamiento.

---

# Tamaño de píxel y resolución espacial

El tamaño de cada píxel está relacionado con el nivel de detalle espacial que puede representar el ráster.

Por ejemplo, en un sistema de coordenadas cuyas unidades sean metros:

```text
10 × 10 m
```

significaría que cada píxel representa aproximadamente una celda de diez metros por diez metros.

Otro ráster podría tener:

```text
30 × 30 m
```

Los dos pueden representar la misma región, pero con diferente nivel de detalle.

!!! danger "Más píxeles no significa automáticamente mejor información"

    La resolución debe evaluarse junto con la fuente, el método de captura, la fecha, la precisión y el propósito del trabajo. Aumentar artificialmente el número de píxeles no genera nuevos detalles reales.

---

# El tipo de dato del ráster

Los píxeles también tienen un **tipo de dato**.

Puedes encontrar, entre otros:

```text
Byte
UInt16
Int16
UInt32
Float32
Float64
```

Estos tipos determinan qué clases y rangos de valores pueden almacenarse.

Un ráster categórico podría utilizar valores enteros como:

```text
1 = bosque
2 = cultivo
3 = urbano
4 = agua
```

Un modelo de elevación puede requerir valores con decimales.

En esta etapa no es necesario memorizar todos los tipos numéricos; debes aprender a **reconocerlos y registrarlos**.

---

# Valores NoData

Un ráster puede contener zonas donde no existe un valor válido.

Estas zonas pueden identificarse mediante un valor **NoData**.

Por ejemplo:

```text
-9999
```

podría estar reservado para indicar ausencia de información.

Eso no significa necesariamente que `-9999` represente una medición real.

!!! warning "NoData no es cero"

    Un píxel con valor `0` puede contener una observación válida.

    Un píxel definido como **NoData** indica que el dataset no proporciona allí un valor válido.

---

# Reconocer el sistema de referencia

Tanto las fuentes vectoriales como los ráster pueden tener asociado un **Sistema de Referencia de Coordenadas (SRC)**.

En esta lección registra:

```text
Nombre del SRC
Código EPSG, si existe
Unidades
```

Por ejemplo:

```text
EPSG:4326
```

o:

```text
EPSG:32719
```

No necesitas todavía explicar sus diferencias matemáticas.

Eso se desarrollará en la lección **2.6**.

!!! danger "Que las capas coincidan visualmente no demuestra que tengan el mismo SRC"

    QGIS puede realizar transformaciones para representar conjuntamente capas con sistemas diferentes. Consulta siempre la información de cada fuente.

---

# Metadatos: datos acerca de los datos

Conocer geometrías y campos no es suficiente.

También necesitas saber:

- quién produjo la información;
- qué institución es responsable;
- cuándo fue creada;
- cuándo fue actualizada;
- qué representa exactamente;
- cómo fue obtenida;
- qué precisión tiene;
- qué restricciones de uso existen;
- cuál es su licencia;
- para qué propósito fue producida.

Esta información constituye parte de los **metadatos**.

---

## Un archivo sin contexto pierde valor

Compara estos dos casos:

```text
calles.shp
```

frente a:

```text
Fuente: Gobierno Autónomo Municipal
Contenido: red vial municipal
Fecha de actualización: agosto de 2026
Método: restitución y verificación de campo
SRC: EPSG:32719
Responsable: Unidad SIG
Uso: planificación municipal
```

En ambos casos puedes abrir el archivo.

Pero solamente en el segundo puedes comenzar a evaluar con mayor fundamento **qué representa y si resulta apropiado**.

!!! note "Metadatos incompletos también son información"

    Si desconoces la fecha, responsable o método de producción, no inventes esos valores.

    Registra:

    **No disponible**

    o:

    **Por verificar**

La ausencia de documentación debe formar parte de la evaluación.

---

# Procedencia y linaje

La **procedencia** indica de dónde provienen los datos.

El **linaje** describe cómo fueron producidos o transformados.

Por ejemplo:

```text
Fuente original:
Catastro municipal 2025

Proceso:
Selección de predios urbanos

Transformación:
Reproyección y corrección geométrica

Producto:
predios_urbanos_2026.gpkg
```

Esto permite diferenciar un dato original de un producto derivado.

---

# Construir un inventario de datos

Antes de comenzar un análisis crea una tabla de inventario.

Una estructura básica puede ser:

| ID | Archivo / capa | Tipo | Formato | Geometría / bandas | Entidades / dimensiones | SRC | Fecha | Procedencia | Estado |
|---:|---|---|---|---|---|---|---|---|---|
| 01 | distritos | Vector | GPKG | Polígono | 12 entidades | EPSG:… | 2026 | GAMS | Utilizable |
| 02 | rios | Vector | Shapefile | Línea | 356 entidades | EPSG:… | N/D | N/D | Revisar |
| 03 | equipamientos | Vector | GeoJSON | Punto | 84 entidades | EPSG:… | 2026 | Levantamiento | Utilizable |
| 04 | elevacion.tif | Ráster | GeoTIFF | 1 banda | 2000 × 1500 | EPSG:… | N/D | N/D | Revisar |

Esta tabla no sustituye los metadatos completos.

Funciona como un **inventario operativo** para conocer rápidamente qué has recibido.

---

# Clasificar el estado de una fuente

Para el curso utilizaremos tres estados sencillos:

| Estado | Significado |
|---|---|
| **Utilizable** | Tiene información suficiente y cumple las necesidades inmediatas |
| **Revisar / preparar** | Puede servir, pero existe algún aspecto que debe verificarse o corregirse |
| **No utilizar por ahora** | No cumple los requisitos del trabajo o su significado no puede verificarse |

!!! warning "No utilizar no significa eliminar"

    Una fuente que no sirve para un análisis determinado puede ser útil posteriormente.

    Conserva los originales y documenta la razón de tu decisión.

---

# Criterios para decidir si un dato sirve

Antes de incorporar definitivamente una fuente a tu flujo de trabajo, pregunta:

### Contenido

- ¿Representa el fenómeno que necesito?
- ¿La geometría es apropiada?
- ¿Tiene los campos necesarios?
- ¿Las bandas representan las variables requeridas?

### Cobertura

- ¿Cubre mi área de estudio?
- ¿Tiene entidades fuera de la zona esperada?
- ¿La extensión parece razonable?

### Escala y detalle

- ¿El nivel de detalle es adecuado?
- ¿El tamaño de píxel permite el análisis previsto?
- ¿El dato fue creado para una escala compatible con mi trabajo?

### Temporalidad

- ¿De qué fecha son los datos?
- ¿Representan el período que necesito?
- ¿Existe una versión más reciente?

### Referencia espacial

- ¿Conozco su SRC?
- ¿Las unidades son apropiadas?
- ¿Existe información suficiente para interpretarlo correctamente?

### Procedencia

- ¿Quién produjo los datos?
- ¿Conozco el método?
- ¿Puedo verificar su fuente?

### Uso

- ¿Tengo permiso para utilizarlo?
- ¿Existen restricciones para publicarlo o redistribuirlo?

---

# Un ejemplo de decisión

Supongamos que necesitas localizar establecimientos de salud existentes en 2026.

Recibes:

```text
hospitales_2015.shp
establecimientos_2026.gpkg
centros_salud.geojson
```

No deberías elegir automáticamente el GeoPackage solo porque sea un formato más moderno.

Debes comparar:

| Criterio | hospitales_2015 | establecimientos_2026 | centros_salud |
|---|---|---|---|
| Fecha | 2015 | 2026 | Desconocida |
| Geometría | Punto | Punto | Punto |
| Procedencia | Conocida | Conocida | Desconocida |
| Cobertura | Parcial | Municipal | Municipal |
| Campos requeridos | Parciales | Completos | Parciales |

La elección debe fundamentarse principalmente en el **contenido y adecuación de los datos**, no solo en su extensión de archivo.

---

# Flujo mínimo de inspección

Cuando recibas una nueva fuente geográfica utiliza esta secuencia:

```text
RECIBIR
   │
   ▼
IDENTIFICAR FORMATO
   │
   ▼
INCORPORAR EN QGIS
   │
   ▼
IDENTIFICAR MODELO
Vector / Ráster
   │
   ▼
REVISAR ESTRUCTURA
   │
   ├── Vector:
   │   geometría
   │   entidades
   │   campos
   │
   └── Ráster:
       dimensiones
       bandas
       píxel
       tipo de dato
   │
   ▼
REVISAR EXTENSIÓN Y SRC
   │
   ▼
REVISAR METADATOS
   │
   ▼
REGISTRAR EN INVENTARIO
   │
   ▼
DECIDIR
Utilizar / Revisar / No utilizar
```

!!! success "Principio de trabajo"

    **No empieces un análisis importante con datos que todavía no has identificado.**

---

## Reto práctico

!!! example "Reto 2.4 — Inventariar y evaluar un paquete de datos"

    **Situación:** recibiste varias fuentes geográficas para preparar un proyecto municipal. Antes de trabajar con ellas debes determinar qué contiene cada una, registrar sus características y justificar cuáles pueden utilizarse.

    **1. Preparar el proyecto**

    - Abre el proyecto creado durante la lección 2.3.
    - Guarda una nueva versión como:

      `proyectos/reto_2-4_inventario.qgz`

    - Comprueba que utiliza rutas relativas.
    - No modifiques los archivos almacenados en `datos/originales/`.

    **2. Incorporar las fuentes**

    Incorpora al menos:

    - un GeoPackage;
    - un Shapefile;
    - un GeoJSON;
    - un GeoTIFF.

    Utiliza tanto el **panel Navegador** como las herramientas de **Añadir capa**.

    **3. Inspeccionar los datos vectoriales**

    Para cada capa registra:

    - archivo;
    - nombre de capa;
    - formato;
    - geometría;
    - número de entidades;
    - extensión;
    - SRC;
    - nombres de al menos tres campos;
    - tipo de esos campos;
    - tres valores de ejemplo;
    - procedencia conocida.

    **4. Inspeccionar el GeoTIFF**

    Registra:

    - archivo;
    - dimensiones;
    - número de bandas;
    - tipo de dato;
    - tamaño de píxel;
    - valores NoData, si están definidos;
    - extensión;
    - SRC;
    - información disponible sobre procedencia.

    **5. Comparar las extensiones**

    - Utiliza **Zoom a la capa** para cada fuente.
    - Determina si todas corresponden aproximadamente al área esperada.
    - Registra cualquier extensión que parezca anómala.
    - No corrijas todavía los datos.

    **6. Crear el inventario**

    Completa una tabla con:

    | ID | Fuente | Tipo | Formato | Geometría / bandas | Cantidad | SRC | Procedencia | Estado |
    |---:|---|---|---|---|---|---|---|---|

    Para **Estado**, utiliza solamente:

    - Utilizable
    - Revisar / preparar
    - No utilizar por ahora

    **7. Justificar**

    Para cada fuente escribe una frase breve explicando tu decisión.

    Ejemplo:

    > **Revisar / preparar:** la capa contiene los campos necesarios, pero no se dispone de información sobre su fecha de actualización.

    **8. Guardar**

    - Guarda el proyecto.
    - Conserva el inventario dentro de la carpeta de trabajo.
    - No sobrescribas ni conviertas todavía los datos originales.

    **Entregables:**

    - `reto_2-4_inventario.qgz`
    - inventario de datos;
    - una captura con las cuatro fuentes incorporadas;
    - una captura de la información de una capa vectorial;
    - una captura de la información del GeoTIFF;
    - justificación del estado asignado a cada fuente.

!!! captura "Captura pendiente · 2.4-08"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-4/2-4-08-inventario-final.png`
    - **Qué mostrar:** QGIS con las fuentes incorporadas y, junto a él, la tabla de inventario completada.
    - **Sugerencia:** Utilizar pocos registros y texto legible; la captura debe mostrar el método, no toda la tabla del estudiante.

??? success "Criterios de evaluación del reto"

    | Criterio | Se cumple si... |
    |---|---|
    | Identificación | Distingue correctamente fuentes vectoriales y ráster |
    | Formatos | Reconoce GPKG, Shapefile, GeoJSON y GeoTIFF |
    | Vector | Registra geometría, entidades y campos |
    | Ráster | Registra dimensiones, bandas, píxel y tipo de dato |
    | Cobertura | Examina extensión y detecta posibles anomalías |
    | Referencia | Registra el SRC sin asumirlo visualmente |
    | Metadatos | Identifica procedencia y señala información desconocida |
    | Inventario | Todas las fuentes están registradas de forma homogénea |
    | Decisión | Cada fuente tiene un estado acompañado de una justificación |
    | Conservación | Los datos originales permanecen sin modificar |

---

# Problemas frecuentes

| Problema | Posible causa | Qué revisar |
|---|---|---|
| Solo recibí `datos.shp` | Faltan componentes del Shapefile | Solicita también `.dbf`, `.shx` y archivos complementarios |
| El GeoPackage muestra varias capas | Es un contenedor | Identifica cuál capa interna necesitas |
| La capa aparece muy lejos de las demás | Extensión o coordenadas inesperadas | Comprueba extensión y SRC |
| Hay números que no puedo sumar | El campo puede ser de tipo texto | Comprueba el tipo del campo |
| Algunos caracteres aparecen incorrectos | Problema de codificación | Revisa formato, archivos complementarios y procedencia |
| El ráster tiene zonas vacías | Pueden ser valores NoData | Consulta sus propiedades |
| El TIFF abre, pero no sé qué representa | Falta información temática | Revisa metadatos y procedencia |
| El mapa se ve correctamente | Eso no garantiza que el dato sea adecuado | Revisa contenido, fecha, atributos, cobertura y fuente |
| Dos capas tienen el mismo nombre | Pueden ser versiones diferentes | Compara origen, fecha, entidades, campos y extensión |
| No conozco la fecha de una capa | Metadatos incompletos | Registra `No disponible` o `Por verificar` |

---

# Ideas clave

!!! success "Para recordar"

    - Los datos geográficos pueden organizarse principalmente mediante modelos **vectoriales** y **ráster**.
    - Punto, línea y polígono son geometrías vectoriales; los ráster se organizan mediante **píxeles**.
    - **GeoPackage, Shapefile, GeoJSON y GeoTIFF son formatos**, no fenómenos geográficos.
    - Un GeoPackage puede contener **varias capas** dentro de un único archivo.
    - Un Shapefile depende de **varios archivos relacionados**.
    - GeoJSON es un formato de texto ampliamente utilizado para intercambio y aplicaciones web.
    - GeoTIFF puede almacenar información geográfica y una o varias **bandas ráster**.
    - La **extensión** indica los límites espaciales generales de un dataset, pero no garantiza una cobertura completa.
    - Los **campos** tienen tipos de datos que condicionan las operaciones que pueden realizarse.
    - En un ráster debes reconocer al menos dimensiones, bandas, tamaño de píxel, tipo de dato y NoData.
    - Que una capa aparezca correctamente en el mapa **no demuestra que sea apropiada** para el análisis.
    - Los metadatos permiten comprender **qué representa, quién produjo y cuándo fue creado** un conjunto de datos.
    - Cuando recibas información nueva, **inventaría primero y analiza después**.

---

# Autoevaluación

??? question "1. Recibes `predios.shp` y copias únicamente ese archivo. ¿Tienes necesariamente toda la fuente?"

    No. Un Shapefile utiliza varios archivos asociados. Como mínimo suelen intervenir `.shp`, `.shx` y `.dbf`; pueden existir además archivos relacionados con el SRC, codificación e índices.

??? question "2. Un archivo `municipio.gpkg` aparece una sola vez en la carpeta, pero QGIS muestra cinco capas. ¿Es un error?"

    No. GeoPackage funciona como un contenedor y puede almacenar varias capas dentro del mismo archivo.

??? question "3. Una capa de establecimientos tiene geometría de puntos y otra de municipios tiene polígonos. ¿Qué describe esa diferencia?"

    Describe cómo se representan espacialmente sus entidades. Los establecimientos se representan mediante posiciones puntuales y los municipios mediante superficies delimitadas.

??? question "4. Dos capas coinciden perfectamente en el lienzo. ¿Puedes concluir que utilizan el mismo SRC?"

    No. QGIS puede transformar datos durante la representación. Debes consultar el SRC de cada fuente.

??? question "5. ¿La extensión de una capa permite saber que existen datos en cada lugar situado dentro de ese rectángulo?"

    No. La extensión representa el rectángulo que contiene el conjunto de datos. No implica cobertura continua.

??? question "6. Un campo contiene `10`, `20` y `30`, pero está definido como texto. ¿Por qué importa?"

    Porque su apariencia no determina su tipo. Determinadas operaciones numéricas requieren valores almacenados mediante tipos numéricos.

??? question "7. ¿Cuál es una diferencia básica entre una tabla vectorial y un ráster?"

    Una capa vectorial relaciona entidades geométricas con atributos. Un ráster organiza valores mediante una matriz de píxeles y puede contener una o varias bandas.

??? question "8. ¿Qué significa NoData en un ráster?"

    Indica ubicaciones donde el dataset no proporciona un valor válido. No debe confundirse automáticamente con el valor numérico cero.

??? question "9. Recibes dos capas técnicamente correctas: una de 2014 y otra de 2026. ¿Cuál debes utilizar?"

    No puede decidirse únicamente por el formato ni por la fecha. Debes comparar el período requerido por el trabajo, contenido, cobertura, procedencia, metodología y demás requisitos.

??? question "10. ¿Para qué sirve un inventario antes de comenzar un análisis?"

    Permite registrar de forma homogénea qué información existe, cuáles son sus características, qué problemas deben revisarse y qué fuentes resultan adecuadas para el trabajo.

---

# Referencias

- QGIS Project. *Manual de usuario 3.44: Abriendo datos*.
- QGIS Project. *Manual de usuario 3.44: Explorando formatos y campos de datos*.
- QGIS Project. *Manual de usuario 3.44: Propiedades de capas ráster*.
- QGIS Project. *Manual de usuario 3.44: Propiedades de capas vectoriales*.
- GDAL Project. *Documentación de controladores vectoriales y ráster*.
- Open Geospatial Consortium. *GeoPackage Encoding Standard*.
- IETF. *RFC 7946 — The GeoJSON Format*.

---

En la próxima etapa del curso, los datos ya no se tratarán simplemente como archivos que pueden abrirse. A partir de este inventario podremos comenzar a **seleccionar, preparar y transformar fuentes de manera controlada**, conservando siempre los originales y documentando los cambios realizados.