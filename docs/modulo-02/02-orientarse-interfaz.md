---
title: 2.2 Orientarse y trabajar con fluidez
description: Ventana principal de QGIS, navegación por el mapa, paneles, navegador, localizador, identificación y medición, marcadores espaciales, y orden y agrupación de capas.
---

# 2.2 Orientarse y trabajar con fluidez

!!! abstract "Objetivos de aprendizaje"

    Al finalizar esta lección, el estudiante será capaz de:

    - Reconocer las partes de la ventana principal de QGIS y organizar su espacio de trabajo.
    - Navegar por el mapa con el ratón, el teclado y la barra de estado.
    - Encontrar datos con el **navegador** y herramientas o lugares con el **localizador**.
    - Consultar información de las entidades y medir sobre el mapa.
    - Crear y administrar **marcadores espaciales**, distinguiendo los del proyecto y los del usuario.
    - Ordenar, agrupar y nombrar capas de forma clara.

!!! note "Antes de empezar"

    - **Entorno:** QGIS abierto con el perfil `curso-qgis` (lección **2.1**).
    - **Datos:** la capa de límites municipales incluida en los [datos del curso](../descargas/index.md), guardada en `datos/originales/`.
    - **Conexión a internet:** necesaria para el mapa base de OpenStreetMap y la búsqueda de lugares.

---

## La ventana principal

Antes de trabajar con fluidez, conviene conocer **cómo está organizada** la ventana de QGIS.

!!! captura "Captura pendiente · 2.2-01"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-01-ventana-principal.png`
    - **Qué mostrar:** La ventana principal de QGIS con un proyecto abierto (mapa base y una capa), con **números** sobre cada parte, que coincidan con la tabla de abajo.
    - **Sugerencia:** Usa círculos numerados del mismo color que las figuras del curso.

| N.º | Parte | Función |
|---|---|---|
| 1 | **Barra de menús** | Acceso a todas las funciones de QGIS, organizadas por tema |
| 2 | **Barras de herramientas** | Botones para las funciones más usadas: navegación, selección, edición, identificación |
| 3 | **Panel Capas** | Lista de las capas del proyecto, su orden, visibilidad y agrupación |
| 4 | **Panel Navegador** | Explorador de archivos, bases de datos y servicios para incorporar datos |
| 5 | **Vista del mapa** | El lienzo donde se dibujan las capas |
| 6 | **Localizador** | Buscador rápido de capas, herramientas, entidades y lugares |
| 7 | **Barra de estado** | Coordenadas del cursor, escala, rotación, sistema de referencia del proyecto y mensajes |

!!! tip "Ver más del mapa"

    - ++ctrl+tab++ oculta o muestra **todos los paneles** a la vez, para ganar espacio en el mapa.
    - ++f11++ activa el **modo de pantalla completa**.

---

## Navegar por el mapa

### Herramientas de navegación

| Herramienta | Qué hace | Atajo o gesto |
|---|---|---|
| **Desplazar mapa** | Mueve la vista arrastrando el mapa | Mantener ++space++ y mover el ratón, o arrastrar con la **rueda** presionada |
| **Acercar / Alejar** | Cambia la escala de la vista | **Rueda del ratón** |
| **Zoom general** | Muestra la extensión de todas las capas del proyecto | ++ctrl+shift+f++ |
| **Zoom a la capa** | Muestra la extensión de una capa | Clic derecho sobre la capa ▸ **Zoom a la capa** |
| **Zoom a la selección** | Muestra las entidades seleccionadas | Botón de la barra de navegación |
| **Zoom anterior / siguiente** | Vuelve a las vistas anteriores, como el botón *atrás* de un navegador web | Botones de la barra de navegación |
| **Actualizar** | Vuelve a dibujar el mapa | ++f5++ |

!!! captura "Captura pendiente · 2.2-02"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-02-navegar-mapa.gif`
    - **Qué mostrar:** Acercar con la rueda del ratón, desplazar el mapa manteniendo la barra espaciadora, usar **Zoom a la capa** desde el panel Capas y volver con **Zoom anterior**.
    - **Sugerencia:** Muestra en pantalla las teclas presionadas o menciónalas en el pie de figura.

### La barra de estado

La barra de estado ofrece información y controles que se usan constantemente:

| Elemento | Qué muestra o permite hacer |
|---|---|
| **Coordenada** | La posición del cursor en el **SRC del proyecto**. Al hacer clic en su ícono, alterna con la extensión de la vista |
| **Escala** | La escala de visualización actual. Se puede **escribir** una escala para ir directamente a ella (tema 1.8) |
| **Lupa** | Amplía la vista sin cambiar la escala del mapa |
| **Rotación** | Gira la vista del mapa |
| **Representar** | Activa o desactiva el dibujo del mapa, útil con capas muy pesadas |
| **SRC del proyecto** | Muestra el código del sistema de referencia del proyecto. Al hacer clic, abre sus propiedades |
| **Mensajes** | Registro de avisos y errores de QGIS |

!!! captura "Captura pendiente · 2.2-03"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-03-barra-estado.png`
    - **Qué mostrar:** La barra de estado completa, con cada elemento resaltado: coordenada, escala, lupa, rotación, casilla de representar, SRC del proyecto y mensajes.
    - **Sugerencia:** Recorta solo la barra de estado y amplíala para que se lean los textos.

!!! warning "La coordenada que ves depende del SRC del proyecto"

    La barra de estado muestra las coordenadas en el **sistema de referencia del proyecto**, no en el de cada capa. Si el proyecto está en EPSG:3857 (el de los mapas base web), verás valores en metros de Pseudo-Mercator, **no** coordenadas UTM ni grados. Veremos cómo manejar esto en la lección **2.6**.

---

## Paneles

Los **paneles** son ventanas acopladas que se pueden **abrir**, **cerrar**, **mover** y **agrupar** según lo que se esté haciendo.

### Abrir y organizar paneles

- **Abrir o cerrar:** menú **Ver ▸ Paneles**, o **clic derecho** sobre el área de las barras de herramientas.
- **Mover:** arrastrar el panel desde su barra de título hasta otro borde de la ventana.
- **Agrupar en pestañas:** soltar un panel encima de otro.
- **Flotar:** hacer doble clic en la barra de título del panel, útil con dos monitores.

!!! captura "Captura pendiente · 2.2-04"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-04-organizar-paneles.gif`
    - **Qué mostrar:** Abrir un panel desde **Ver ▸ Paneles**, arrastrarlo a otro borde, agruparlo en pestañas con otro panel y dejarlo flotando.

### Paneles más usados

| Panel | Para qué sirve | Atajo |
|---|---|---|
| **Capas** | Administrar las capas del proyecto | ++ctrl+1++ |
| **Navegador** | Explorar y agregar datos | ++ctrl+2++ |
| **Estilo de capas** | Cambiar la simbología sin abrir las propiedades | ++f7++ |
| **Caja de herramientas de Procesos** | Buscar y ejecutar herramientas de análisis | ++ctrl+alt+t++ |
| **Resultados de la identificación** | Ver los atributos de las entidades consultadas | Se abre al identificar |
| **Orden de capas** | Controlar el orden de dibujo independientemente de la lista de capas | — |
| **Registro de mensajes** | Revisar avisos y errores | — |

!!! tip "Un espacio de trabajo para cada tarea"

    No hace falta tener todos los paneles abiertos. Mantén visibles solo los que usas en cada etapa: **Capas** y **Navegador** para organizar datos; **Estilo de capas** para simbolizar; la **Caja de herramientas** para analizar. Un espacio de trabajo despejado ayuda a concentrarse en el mapa.

---

## El navegador

El panel **Navegador** es la puerta de entrada a los datos. Funciona como un explorador de archivos, pero **especializado en información geográfica**: reconoce formatos espaciales, bases de datos y servicios.

!!! captura "Captura pendiente · 2.2-05"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-05-panel-navegador.png`
    - **Qué mostrar:** El panel Navegador con sus principales entradas visibles: **Favoritos**, **Marcadores espaciales**, **Inicio del proyecto**, carpetas del sistema, **GeoPackage** y **XYZ Tiles** desplegado con **OpenStreetMap**.

| Entrada | Contenido |
|---|---|
| **Favoritos** | Carpetas marcadas para acceder rápidamente |
| **Marcadores espaciales** | Lugares guardados del proyecto y del usuario |
| **Inicio del proyecto** | La carpeta donde está guardado el proyecto actual |
| **Carpetas del sistema** | Unidades y carpetas de la computadora |
| **GeoPackage, SpatiaLite, PostgreSQL...** | Conexiones a bases de datos |
| **WMS/WMTS, WFS, XYZ Tiles...** | Conexiones a servicios de internet (lección **2.11**) |

### Trabajar con el navegador

- **Agregar una capa:** **arrastrar** el archivo al mapa o al panel Capas, o hacer **doble clic** sobre él.
- **Agregar una carpeta a Favoritos:** clic derecho sobre la carpeta ▸ **Añadir a Favoritos**.
- **Filtrar:** usar el cuadro de búsqueda del panel para encontrar un archivo por su nombre.
- **Ver información antes de cargar:** clic derecho sobre una capa ▸ **Propiedades de la capa**, para revisar su SRC, geometría o campos.

!!! captura "Captura pendiente · 2.2-06"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-06-favoritos-arrastrar.gif`
    - **Qué mostrar:** Agregar la carpeta `curso-qgis/` a **Favoritos** y arrastrar la capa de límites municipales desde el navegador hasta el mapa.

!!! tip "Tu carpeta del curso en Favoritos"

    Agrega la carpeta `curso-qgis/` a **Favoritos** desde el primer día. Así tendrás siempre a mano tus datos, sin recorrer todo el sistema de archivos. Como los favoritos se guardan en el **perfil de usuario**, estarán disponibles en todos tus proyectos del curso.

---

## El localizador

El **localizador** es la barra de búsqueda de la esquina inferior izquierda. Es, probablemente, **la herramienta que más acelera el trabajo** en QGIS.

Se activa con ++ctrl+k++. Al escribir, busca simultáneamente en capas, herramientas, entidades, marcadores y opciones.

!!! captura "Captura pendiente · 2.2-07"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-07-localizador-herramienta.gif`
    - **Qué mostrar:** Presionar ++ctrl+k++, escribir *buffer* (o *área de influencia*) y abrir la herramienta directamente desde los resultados.

### Filtros y prefijos

Para buscar solo en un tipo de elemento, se escribe un **prefijo** seguido de un espacio y el texto a buscar:

| Prefijo | Busca en | Ejemplo |
|---|---|---|
| `l` | Capas del proyecto | `l limites` |
| `a` | Herramientas de procesamiento | `a recortar` |
| `f` | Entidades de la capa activa | `f Sacaba` |
| `af` | Entidades de todas las capas | `af unidad educativa` |
| `b` | Marcadores espaciales | `b plaza` |
| `go` | Ir a una coordenada | `go -17.3935, -66.1570` |
| `=` | Calculadora | `= 1250 * 0.5` |
| `set` | Opciones y configuraciones | `set idioma` |
| `>` | Búsqueda de lugares en OpenStreetMap (Nominatim) | `> Cochabamba` |

!!! note "Verifica los filtros disponibles"

    La lista completa de filtros, sus prefijos y si están activos se puede consultar y modificar en **Configuración ▸ Opciones ▸ Localizador**. Algunos filtros, como la búsqueda de lugares, pueden estar desactivados por defecto o variar entre versiones.

### Buscar lugares e ir a coordenadas

!!! captura "Captura pendiente · 2.2-08"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-08-localizador-lugares.gif`
    - **Qué mostrar:** Buscar un municipio con el prefijo `>` y hacer clic en el resultado para acercar el mapa; luego usar `go` con una coordenada y mostrar cómo QGIS indica la interpretación antes de ir.

!!! warning "Dos precauciones al buscar lugares y coordenadas"

    - **La búsqueda de lugares** usa datos de **OpenStreetMap**: los resultados dependen de cómo está cargada la información en esa plataforma y requieren conexión a internet. Sirve para **orientarse**, no como fuente oficial de límites o ubicaciones.
    - **Al ir a una coordenada**, revisa cómo la interpreta QGIS en el resultado del localizador: el **orden** de latitud y longitud y el **sistema de referencia** importan (temas 1.3 y 1.4). Un error de orden puede llevarte al otro lado del planeta.

---

## Identificar y medir

### La herramienta Identificar

La herramienta **Identificar objetos espaciales** (++ctrl+shift+i++) muestra los **atributos** de las entidades en las que se hace clic, en el panel **Resultados de la identificación**.

!!! captura "Captura pendiente · 2.2-09"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-09-identificar.gif`
    - **Qué mostrar:** Activar **Identificar**, hacer clic sobre un municipio y desplegar sus atributos en el panel de resultados; luego cambiar el modo de identificación.

#### Modos de identificación

| Modo | Qué consulta |
|---|---|
| **Capa actual** | Solo la capa seleccionada en el panel Capas |
| **De arriba abajo, detenerse en la primera** | La primera capa visible que tenga una entidad en ese lugar |
| **De arriba abajo** | Todas las capas visibles con entidades en ese lugar |
| **Selección de capas** | Muestra un menú para elegir qué capa consultar |

#### Información derivada

Además de los atributos, el panel de resultados incluye un grupo **(Derivado)** con información que QGIS **calcula** a partir de la geometría: coordenadas del punto consultado, **longitud**, **perímetro**, **área**, número de partes y vértices.

!!! captura "Captura pendiente · 2.2-10"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-10-resultados-derivado.png`
    - **Qué mostrar:** El panel **Resultados de la identificación** con los atributos de un municipio y el grupo **(Derivado)** desplegado, mostrando área y perímetro.

!!! danger "Atributos almacenados frente a valores calculados"

    Un campo de la tabla llamado `superficie` es un **valor almacenado**: puede estar desactualizado o haberse calculado con otro método. El **área derivada** es un **valor calculado** en ese momento a partir de la geometría, y depende del **SRC** y de la configuración de **medición** del proyecto. Si ambos valores no coinciden, no siempre hay un error: hay que averiguar **cómo se obtuvo cada uno** (temas 1.12 y 1.13).

!!! tip "Identificar también funciona en ráster"

    Al hacer clic sobre una capa ráster, la herramienta muestra el **valor de cada banda** en ese píxel: por ejemplo, la elevación de un modelo digital. Lo usaremos en la lección **2.10**.

### Medir

Las herramientas de **medición** (++ctrl+shift+m++ para medir líneas) permiten medir **distancias**, **áreas** y **ángulos** directamente sobre el mapa.

!!! captura "Captura pendiente · 2.2-11 (opcional)"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-11-medir.gif`
    - **Qué mostrar:** Medir una distancia entre dos puntos del municipio y alternar en la ventana de resultados entre medición **cartesiana** y **elipsoidal**.

!!! warning "Medir con criterio"

    La ventana de medición permite elegir entre medición **cartesiana** (sobre el plano de la proyección) y **elipsoidal** (sobre el elipsoide). Si el proyecto está en un SRC geográfico o en Pseudo-Mercator, la medición cartesiana **no es confiable** (temas 1.4 y 1.5). Estudiaremos la configuración de mediciones en la lección **2.6**.

---

## Marcadores espaciales

Un **marcador espacial** guarda una **extensión del mapa** con un nombre, para volver a ella con un clic. Es útil para lugares que se revisan con frecuencia: el centro del municipio, una zona de riesgo, un área de estudio.

### Crear un marcador

1. Encuadra el mapa en el lugar que quieres guardar.
2. Presiona ++ctrl+b++ o usa **Ver ▸ Nuevo marcador espacial**.
3. Completa los datos:
    - **Nombre:** descriptivo, por ejemplo `Plaza principal`.
    - **Grupo:** para organizar varios marcadores, por ejemplo `Equipamientos`.
    - **Extensión y SRC:** se completan con la vista actual.
    - **Guardado en:** marcadores del **proyecto** o del **usuario**.
4. Guarda el marcador.

!!! captura "Captura pendiente · 2.2-12"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-12-crear-marcador.gif`
    - **Qué mostrar:** Encuadrar un lugar, presionar ++ctrl+b++, completar nombre y grupo, elegir **Guardado en: Marcadores del proyecto** y guardar.

### ¿Proyecto o usuario?

Esta decisión aplica directamente la distinción de la lección **2.1**:

| Guardado en | Dónde queda | Viaja con el proyecto | Úsalo para |
|---|---|---|---|
| **Marcadores del proyecto** | Dentro del archivo `.qgz` | Sí | Lugares relevantes **para ese trabajo**, que otras personas también necesitan |
| **Marcadores del usuario** | En el perfil de usuario | No | Lugares que **tú** usas en muchos proyectos distintos |

!!! example "Un caso típico"

    Preparas un proyecto de zonas de riesgo para el equipo municipal y guardas marcadores de las quebradas más críticas como **marcadores del usuario**. Envías el proyecto y tus colegas **no los ven**. Debiste guardarlos como **marcadores del proyecto**.

### Administrar marcadores

El **administrador de marcadores espaciales** (++ctrl+shift+b++) permite:

- **Ir** a un marcador con doble clic.
- **Editar** su nombre, grupo o extensión.
- **Eliminar** marcadores.
- **Exportar** e **importar** marcadores en un archivo, para compartirlos o respaldarlos.

Los marcadores también aparecen en el **Navegador** y se pueden buscar en el **localizador** con el prefijo `b`.

!!! captura "Captura pendiente · 2.2-13"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-13-administrador-marcadores.png`
    - **Qué mostrar:** El administrador de marcadores espaciales con varios marcadores organizados en grupos, diferenciando los del proyecto y los del usuario, y los botones de importar y exportar visibles.

---

## Ordenar y agrupar capas

Un panel de capas ordenado hace que el proyecto sea **fácil de entender**, para ti y para quien lo reciba.

### Orden de dibujo

Las capas se dibujan **de abajo hacia arriba**: la capa que está **arriba** en la lista se dibuja **encima** de las demás.

!!! tip "Un orden que casi siempre funciona"

    De arriba abajo: **etiquetas y puntos**, **líneas**, **polígonos**, **ráster** y **mapas base**. Así, los elementos pequeños no quedan tapados por los grandes. Recuerda también la **jerarquía visual** del tema 1.7.

### Grupos

Los **grupos** reúnen capas relacionadas, como carpetas dentro del panel Capas.

- **Crear un grupo:** botón **Añadir grupo** del panel Capas, o seleccionar varias capas ▸ clic derecho ▸ **Agrupar seleccionadas**.
- **Mover capas:** arrastrarlas dentro o fuera del grupo.
- **Encender o apagar** todas las capas de un grupo con su casilla.
- **Grupo mutuamente excluyente:** clic derecho sobre el grupo ▸ **Grupo mutuamente excluyente**. Solo una de sus capas puede estar visible a la vez. Muy útil para **mapas base** alternativos.

!!! captura "Captura pendiente · 2.2-14"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-14-agrupar-ordenar.gif`
    - **Qué mostrar:** Crear los grupos `Referencia` y `Mapas base`, arrastrar capas a cada uno, cambiar el orden de dibujo y convertir `Mapas base` en grupo mutuamente excluyente.

### Buenas prácticas en el panel Capas

| Práctica | Cómo hacerlo | Por qué |
|---|---|---|
| **Nombres claros** | Clic derecho ▸ **Cambiar nombre de capa**: `Límites municipales`, no `lim_mun_v3` | El nombre de la capa en el proyecto puede ser distinto al del archivo y debe entenderse |
| **Grupos por función** | Por ejemplo: `Tema`, `Referencia`, `Mapas base` | Refleja la jerarquía del mapa |
| **Contar entidades** | Clic derecho ▸ **Mostrar recuento de objetos** | Permite detectar capas vacías o incompletas |
| **Filtrar la leyenda** | Opción **Filtrar leyenda por contenido del mapa** | Muestra solo lo visible en la vista actual |
| **Revisar los indicadores** | Íconos junto al nombre de la capa | Avisan de filtros aplicados, capas temporales o **fuentes no disponibles** |

!!! danger "Quitar una capa no es borrar el archivo"

    **Eliminar capa** en el panel Capas solo **quita la capa del proyecto**: el archivo sigue intacto en su carpeta. Es la diferencia entre **proyecto** y **fuente de datos** que estudiaremos en la lección **2.3**. Del mismo modo, borrar un archivo desde el explorador **no lo quita** del proyecto: la capa quedará como **no disponible**.

!!! captura "Captura pendiente · 2.2-15"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-15-panel-capas-ordenado.png`
    - **Qué mostrar:** Un panel Capas bien organizado: grupos con nombres claros, capas renombradas, recuento de entidades visible y un grupo mutuamente excluyente de mapas base.
    - **Sugerencia:** Si puedes, muéstralo junto a un panel desordenado (capas con nombres de archivo, sin grupos) para comparar.

??? info "Para saber más: temas del mapa"

    Los **temas del mapa** guardan combinaciones de **capas visibles** y **estilos**, para alternar rápidamente entre distintas vistas del mismo proyecto: por ejemplo, *vista de riesgo*, *vista de equipamientos* y *vista de referencia*. Se administran desde el ícono del **ojo** en la parte superior del panel Capas, y se usan también al preparar mapas para imprimir.

---

## Atajos de teclado útiles

| Acción | Atajo |
|---|---|
| Nuevo proyecto | ++ctrl+n++ |
| Abrir proyecto | ++ctrl+o++ |
| Guardar proyecto | ++ctrl+s++ |
| Guardar proyecto como | ++ctrl+shift+s++ |
| Administrador de fuentes de datos | ++ctrl+l++ |
| Localizador | ++ctrl+k++ |
| Identificar objetos espaciales | ++ctrl+shift+i++ |
| Medir línea | ++ctrl+shift+m++ |
| Zoom general | ++ctrl+shift+f++ |
| Nuevo marcador espacial | ++ctrl+b++ |
| Administrador de marcadores espaciales | ++ctrl+shift+b++ |
| Panel Capas / Navegador | ++ctrl+1++ / ++ctrl+2++ |
| Panel Estilo de capas | ++f7++ |
| Caja de herramientas de Procesos | ++ctrl+alt+t++ |
| Ocultar o mostrar todos los paneles | ++ctrl+tab++ |
| Pantalla completa | ++f11++ |
| Actualizar el mapa | ++f5++ |

!!! note "Personalizar atajos"

    Los atajos se pueden consultar y modificar en **Configuración ▸ Atajos de teclado**. Allí también se puede **buscar** una acción para conocer su atajo, que puede variar ligeramente entre versiones.

!!! captura "Captura pendiente · 2.2-16 (opcional)"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-16-atajos-teclado.png`
    - **Qué mostrar:** La ventana **Configuración ▸ Atajos de teclado** con una búsqueda aplicada (por ejemplo, *marcador*) y el atajo correspondiente visible.

---

## Reto práctico

!!! example "Reto 2.2 — Explorar un municipio y guardar sus lugares de interés"

    **Situación:** te incorporas a un equipo técnico que trabajará en un municipio que no conoces. Antes de la primera reunión, debes explorar el territorio y preparar un proyecto con los **lugares de interés** ya marcados, para que el equipo pueda revisarlos.

    **1. Preparar el proyecto**

    - Crea un proyecto nuevo con el perfil `curso-qgis`.
    - Agrega la carpeta `curso-qgis/` a **Favoritos** del navegador.
    - Desde el navegador, agrega el mapa base **OpenStreetMap** (XYZ Tiles) y la capa de **límites municipales** de los datos del curso.
    - Guarda el proyecto como `proyectos/reto_2-2_exploracion.qgz`.

    **2. Encontrar el municipio**

    - Usa el **localizador** para encontrar el municipio asignado (o el tuyo), mediante la búsqueda de lugares o buscando la entidad en la capa de límites.
    - Con la herramienta **Identificar**, consulta sus atributos y anota su **nombre**, su **código** y la **superficie** que indica la tabla.
    - Compara esa superficie con el **área derivada** que calcula QGIS. ¿Coinciden? Anota una posible explicación.

    **3. Marcar lugares de interés**

    Crea **al menos seis marcadores espaciales del proyecto**, organizados en **dos grupos o más**. Por ejemplo:

    - `Centros urbanos`: plaza principal, centro poblado secundario.
    - `Equipamientos`: hospital, unidad educativa, mercado.
    - `Riesgos o ambiente`: río, quebrada, área protegida, zona de expansión urbana.

    Además, crea **un marcador del usuario** con la ubicación de tu institución o de tu hogar.

    **4. Organizar el proyecto**

    - Crea los grupos `Referencia` y `Mapas base`, y ordena las capas correctamente.
    - Renombra las capas con nombres claros.
    - Activa el **recuento de objetos** de la capa de límites.
    - Guarda el proyecto.

    **5. Compartir y verificar**

    - **Exporta** los marcadores del proyecto a un archivo en `salidas/`.
    - Intercambia el proyecto con un compañero: ¿ve tus seis marcadores del proyecto? ¿Ve tu marcador del usuario? Explica por qué.

    **Entregables:**

    - El proyecto `reto_2-2_exploracion.qgz`.
    - El archivo de marcadores exportado.
    - Un breve texto (media página) con los datos del municipio, la comparación de superficies y la respuesta del paso 5.

??? success "Criterios de evaluación del reto"

    | Criterio | Se cumple si... |
    |---|---|
    | Localización | Se encontró el municipio y se registraron correctamente sus datos |
    | Análisis | Se compararon la superficie almacenada y la derivada, con una explicación razonable |
    | Marcadores | Hay al menos seis marcadores del proyecto en dos grupos o más, con nombres claros, y un marcador del usuario |
    | Organización | Las capas están agrupadas, ordenadas y con nombres comprensibles |
    | Comprensión | Se explica correctamente la diferencia entre marcadores del proyecto y del usuario |

---

## Problemas frecuentes

| Problema | Causa probable | Solución |
|---|---|---|
| Desapareció un panel | Se cerró o quedó oculto con ++ctrl+tab++ | **Ver ▸ Paneles**, o presiona ++ctrl+tab++ |
| El mapa base de OpenStreetMap no se ve | Sin conexión a internet, o la capa está debajo de otra capa opaca | Verifica la conexión y el orden de las capas |
| La búsqueda de lugares no devuelve resultados | Filtro desactivado, sin internet o lugar no registrado en OpenStreetMap | Revisa **Configuración ▸ Opciones ▸ Localizador** y prueba otro nombre |
| Identificar no muestra nada | Está en modo **Capa actual** con otra capa seleccionada, o se hizo clic fuera de las entidades | Cambia el modo o selecciona la capa correcta |
| El compañero no ve mis marcadores | Se guardaron como **marcadores del usuario** | Guárdalos como **marcadores del proyecto** o expórtalos |
| Una capa no se ve aunque está activada | Está debajo de otra capa, fuera de la vista o tiene visibilidad por escala | Revisa el orden, usa **Zoom a la capa** y verifica su rango de escalas |
| Las coordenadas de la barra de estado "no tienen sentido" | Se muestran en el SRC del proyecto, no en el de la capa | Revisa el SRC del proyecto (lección **2.6**) |

---

## Ideas clave

!!! success "Para recordar"

    - La ventana de QGIS se organiza en **menús**, **barras de herramientas**, **paneles**, **vista del mapa**, **localizador** y **barra de estado**.
    - Los paneles se pueden **abrir, mover, agrupar y ocultar**; ++ctrl+tab++ oculta todos a la vez.
    - El **navegador** es la puerta de entrada a los datos; agrega tu carpeta del curso a **Favoritos**.
    - El **localizador** (++ctrl+k++) busca capas, herramientas, entidades, marcadores y lugares; los **prefijos** acotan la búsqueda.
    - **Identificar** muestra atributos almacenados y valores **derivados** calculados a partir de la geometría.
    - Los **marcadores del proyecto** viajan con el `.qgz`; los **del usuario** quedan en tu perfil.
    - Las capas se dibujan de **abajo hacia arriba**. **Grupos**, **nombres claros** y un **orden lógico** hacen comprensible el proyecto.
    - **Quitar una capa no borra el archivo**, y **borrar un archivo no quita la capa** del proyecto.

---

## Autoevaluación

??? question "1. ¿Cómo encontrarías rápidamente la herramienta para recortar una capa si no sabes en qué menú está?"

    Con el **localizador**: presionar ++ctrl+k++ y escribir *recortar*, o usar el prefijo `a` para buscar solo entre las herramientas de procesamiento (`a recortar`).

??? question "2. En modo de identificación Capa actual, haces clic sobre una escuela y no aparece nada. ¿Qué pudo pasar?"

    Probablemente la capa **seleccionada** en el panel Capas no es la de escuelas, así que la herramienta consultó otra capa. Hay que seleccionar la capa correcta o cambiar el modo a **De arriba abajo**.

??? question "3. ¿Qué diferencia hay entre un marcador espacial del proyecto y uno del usuario?"

    El **marcador del proyecto** se guarda dentro del archivo `.qgz` y lo ve cualquier persona que abra el proyecto. El **marcador del usuario** se guarda en el **perfil de usuario** y solo está disponible para quien lo creó, en cualquier proyecto que abra con ese perfil.

??? question "4. Una capa de puntos está activada pero no se ve, aunque sus datos están en la vista actual. ¿Qué revisarías primero?"

    El **orden de dibujo**: probablemente está **debajo** de una capa de polígonos o de un mapa base opaco. También conviene revisar si tiene configurada una **visibilidad por escala**.

??? question "5. La superficie almacenada en la tabla de un municipio y el área derivada que muestra Identificar no coinciden. ¿Significa que hay un error?"

    **No necesariamente.** La superficie almacenada pudo calcularse con **otra geometría** (por ejemplo, más detallada), con **otro sistema de referencia** o **método**, o en otra fecha. El área derivada depende del **SRC** y de la **configuración de mediciones** del proyecto. Hay que averiguar cómo se obtuvo cada valor antes de concluir.

??? question "6. Eliminas una capa del panel Capas por error. ¿Perdiste los datos?"

    **No.** Eliminar una capa del panel solo la **quita del proyecto**; el archivo sigue en su carpeta y se puede volver a agregar desde el navegador.

---

## Referencias

- QGIS Project. *Manual de usuario: Interfaz de QGIS*. <https://docs.qgis.org/latest/es/docs/user_manual/introduction/qgis_gui.html>
- QGIS Project. *Manual de usuario: Herramientas generales*. <https://docs.qgis.org/latest/es/docs/user_manual/introduction/general_tools.html>
- QGIS Project. *Manual de usuario: Abrir datos (panel Navegador)*. <https://docs.qgis.org/latest/es/docs/user_manual/managing_data_source/opening_data.html>
- OpenStreetMap Foundation. *Nominatim Usage Policy*. <https://operations.osmfoundation.org/policies/nominatim/>
