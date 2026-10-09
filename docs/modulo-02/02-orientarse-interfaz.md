---
title: 2.2 Orientarse y trabajar con fluidez
description: Ventana principal de QGIS, navegación por el mapa, paneles, navegador, localizador, identificación y medición, marcadores espaciales, y orden y agrupación de capas.
---

# 2.2 Orientarse y trabajar con fluidez

Te incorporas a un equipo que trabajará en Cochabamba y mañana hay reunión. Necesitas **moverte con soltura** por el mapa, encontrar en segundos una herramienta o un lugar, consultar qué hay en cada sitio y dejar **marcados** los lugares clave para que todo el equipo los vea. Esta lección es tu mapa de la interfaz de QGIS.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Reconocer las partes de la ventana de QGIS y organizar los paneles.
    - Navegar por el mapa y leer la barra de estado.
    - Encontrar datos con el **navegador** y casi cualquier cosa con el **localizador**.
    - Consultar atributos y medir, distinguiendo valores almacenados de valores calculados.
    - Crear marcadores espaciales del proyecto y del usuario.
    - Ordenar, agrupar y nombrar capas con claridad.

    **Tiempo:** 75 min (25 de lectura · 50 de práctica) · **Datos:** `proyectos/curso_qgis_base.qgz` · **Producto:** proyecto con seis marcadores de Cochabamba y capas organizadas.

---

## Idea central

### La ventana principal

!!! captura "Captura pendiente · 2.2-01"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-01-ventana-principal.png`
    - **Qué mostrar:** La ventana principal de QGIS con el proyecto base de Cochabamba abierto, con números sobre cada parte que coincidan con la tabla.

| N.º | Parte | Función |
|---|---|---|
| 1 | **Barra de menús** | Todas las funciones, organizadas por tema |
| 2 | **Barras de herramientas** | Botones de navegación, selección, edición, identificación |
| 3 | **Panel Capas** | Capas del proyecto, su orden, visibilidad y grupos |
| 4 | **Panel Navegador** | Explorador de archivos, bases de datos y servicios |
| 5 | **Vista del mapa** | El lienzo donde se dibujan las capas |
| 6 | **Localizador** | Buscador de capas, herramientas, entidades y lugares (++ctrl+k++) |
| 7 | **Barra de estado** | Coordenadas del cursor, escala, rotación, SRC del proyecto y mensajes |

### Tres distinciones que evitan errores

| Distinción | Qué debes recordar |
|---|---|
| **Coordenada de la barra de estado** | Está en el **SRC del proyecto**, no en el de cada capa |
| **Atributo almacenado frente a valor derivado** | Un campo `area_km2` se guardó en algún momento con algún método; el área que calcula **Identificar** se obtiene ahora, de la geometría, y depende del SRC y la configuración de medición |
| **Quitar una capa frente a borrar un archivo** | **Eliminar capa** solo la quita del proyecto; borrar el archivo deja la capa **no disponible** ([2.3](03-gestionar-proyectos.md)) |

!!! tip "Un espacio de trabajo para cada tarea"

    No abras todos los paneles. **Capas** y **Navegador** para organizar datos; **Estilo de capas** (++f7++) para simbolizar; **Caja de herramientas de Procesos** (++ctrl+alt+t++) para analizar. ++ctrl+tab++ oculta todos los paneles a la vez.

---

## Hazlo conmigo

### Paso 1 · Abrir el proyecto base y tu carpeta en Favoritos

1. Abre `curso-qgis/proyectos/curso_qgis_base.qgz`.
2. En el panel **Navegador**, busca la carpeta `curso-qgis/`, haz clic derecho ▸ **Añadir a Favoritos**.
3. Desde **Favoritos**, arrastra `datos/originales/limites.gpkg` ▸ `zonas_analisis` al mapa.

!!! captura "Captura pendiente · 2.2-06"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-06-favoritos-arrastrar.gif`
    - **Qué mostrar:** Agregar la carpeta `curso-qgis/` a **Favoritos** y arrastrar una capa de `limites.gpkg` desde el navegador hasta el mapa.

Los Favoritos se guardan en tu **perfil**: estarán en todos tus proyectos del curso.

??? info "Para saber más · entradas del Navegador"

    | Entrada | Contenido |
    |---|---|
    | **Favoritos** | Carpetas marcadas para acceso rápido |
    | **Marcadores espaciales** | Lugares guardados del proyecto y del usuario |
    | **Inicio del proyecto** | La carpeta donde está guardado el proyecto |
    | **GeoPackage, PostgreSQL…** | Conexiones a bases de datos |
    | **WMS/WMTS, WFS, XYZ Tiles** | Servicios de internet ([2.11](11-servicios-web.md)) |

    Con clic derecho ▸ **Propiedades de la capa** puedes revisar el SRC, la geometría y los campos **antes** de cargar un archivo.

### Paso 2 · Navegar por el mapa

| Acción | Cómo |
|---|---|
| Desplazar | Mantén ++space++ y mueve el ratón, o arrastra con la rueda presionada |
| Acercar o alejar | Rueda del ratón |
| Ver todo el proyecto | ++ctrl+shift+f++ |
| Ver una capa | Clic derecho sobre la capa ▸ **Zoom a la capa** |
| Volver a la vista anterior | Botón **Zoom anterior** |
| Redibujar | ++f5++ |

Prueba: acércate al centro de la ciudad, vuelve con **Zoom anterior** y luego haz **Zoom a la capa** sobre `Comunas`.

!!! captura "Captura pendiente · 2.2-02"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-02-navegar-mapa.gif`
    - **Qué mostrar:** Acercar con la rueda del ratón, desplazar con la barra espaciadora, usar **Zoom a la capa** desde el panel Capas y volver con **Zoom anterior**.

### Paso 3 · Leer la barra de estado

1. Mueve el cursor sobre la plaza principal. La **coordenada** debe rondar **E 802 100, N 8 075 100**: el proyecto está en **EPSG:32719** (UTM 19 S).
2. Escribe `25000` en la casilla **Escala** y presiona ++enter++.
3. Haz clic en el código **EPSG:32719** de la esquina: se abren las propiedades del SRC del proyecto.

!!! captura "Captura pendiente · 2.2-03"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-03-barra-estado.png`
    - **Qué mostrar:** La barra de estado completa, con coordenada, escala, lupa, rotación, casilla de representar, SRC del proyecto y mensajes resaltados.

!!! warning "La coordenada depende del SRC del proyecto"

    Si el proyecto estuviera en EPSG:3857 (el de los mapas base web), verías metros de Pseudo-Mercator, **no** UTM ni grados. Lo trabajaremos en [2.6](06-problemas-coordenadas.md).

### Paso 4 · Organizar los paneles

- **Abrir o cerrar:** **Ver ▸ Paneles**, o clic derecho sobre las barras de herramientas.
- **Mover:** arrastra el panel por su barra de título a otro borde.
- **Agrupar en pestañas:** suelta un panel sobre otro.
- **Flotar:** doble clic en su barra de título (útil con dos monitores).

Abre el panel **Estilo de capas** (++f7++) y acóplalo junto a **Capas**.

!!! captura "Captura pendiente · 2.2-04"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-04-organizar-paneles.gif`
    - **Qué mostrar:** Abrir un panel desde **Ver ▸ Paneles**, arrastrarlo a otro borde, agruparlo en pestañas con otro panel y dejarlo flotando.

### Paso 5 · Encontrarlo todo con el localizador

Presiona ++ctrl+k++ y escribe. Con un **prefijo** y un espacio acotas la búsqueda:

| Prefijo | Busca en | Pruébalo |
|---|---|---|
| `l` | Capas del proyecto | `l comunas` |
| `a` | Herramientas de Procesos | `a buffer` |
| `f` | Entidades de la capa activa | `f Tunari` (con `Comunas` activa) |
| `b` | Marcadores espaciales | `b plaza` |
| `go` | Ir a una coordenada | `go -17.3935, -66.1570` |
| `=` | Calculadora | `= 3 * 1.5` |
| `>` | Lugares de OpenStreetMap | `> Laguna Alalay` |

!!! captura "Captura pendiente · 2.2-07"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-07-localizador-herramienta.gif`
    - **Qué mostrar:** Presionar ++ctrl+k++, escribir *buffer* y abrir la herramienta directamente desde los resultados.

!!! captura "Captura pendiente · 2.2-08"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-08-localizador-lugares.gif`
    - **Qué mostrar:** Buscar un lugar con el prefijo `>` y acercar el mapa; luego usar `go` con una coordenada y mostrar cómo QGIS indica la interpretación antes de ir.

!!! warning "Dos precauciones"

    - La búsqueda `>` usa **OpenStreetMap**: sirve para **orientarse**, no como fuente oficial.
    - Con `go`, revisa cómo interpreta QGIS el **orden** latitud/longitud. Un error de orden te lleva al otro lado del planeta ([2.5](05-tablas-coordenadas.md)).

Los filtros disponibles se configuran en **Configuración ▸ Opciones ▸ Localizador**.

### Paso 6 · Identificar y medir

1. Activa **Identificar objetos espaciales** (++ctrl+shift+i++) y haz clic sobre la comuna **Adela Zamudio**.
2. En **Resultados de la identificación**, lee el atributo `area_km2`.
3. Despliega el grupo **(Derivado)** y lee el **Área** que calcula QGIS. ¿Coinciden exactamente?

!!! captura "Captura pendiente · 2.2-10"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-10-resultados-derivado.png`
    - **Qué mostrar:** El panel **Resultados de la identificación** con los atributos de una comuna y el grupo **(Derivado)** desplegado, mostrando área y perímetro.

??? question "¿Por qué difieren un poco?"

    `area_km2` se calculó **sobre el plano UTM 19 S**. QGIS, por defecto, mide **sobre el elipsoide**. Cochabamba está a unos 300 km del meridiano central de la zona 19, donde el factor de escala de UTM agranda las superficies alrededor de un 0,14 %. Ninguno de los dos valores está «mal»: se obtuvieron de forma distinta ([1.6](../modulo-01/06-sistema-utm.md)).

Ahora mide: ++ctrl+shift+m++, haz clic en la plaza principal y doble clic en la Laguna Alalay. En la ventana de medición alterna entre **Cartesiana** y **Elipsoidal**.

| Modo de identificación | Qué consulta |
|---|---|
| **Capa actual** | Solo la capa seleccionada en el panel Capas |
| **De arriba abajo, detenerse en la primera** | La primera capa visible con entidad en ese lugar |
| **De arriba abajo** | Todas las capas visibles |

!!! tip "Identificar también funciona en ráster"

    Sobre el DEM, muestra la **elevación** de la celda. Lo usarás en [2.10](10-explorar-raster.md).

### Paso 7 · Guardar lugares con marcadores espaciales

Un **marcador espacial** guarda una **extensión del mapa** con un nombre.

1. Encuadra la plaza principal.
2. Presiona ++ctrl+b++.
3. **Nombre:** `Plaza 14 de Septiembre` · **Grupo:** `Centros urbanos` · **Guardado en:** **Marcadores del proyecto**.
4. Guarda. Abre el administrador con ++ctrl+shift+b++ y comprueba que aparece.

!!! captura "Captura pendiente · 2.2-12"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-12-crear-marcador.gif`
    - **Qué mostrar:** Encuadrar un lugar, presionar ++ctrl+b++, completar nombre y grupo, elegir **Guardado en: Marcadores del proyecto** y guardar.

| Guardado en | Dónde queda | ¿Viaja con el proyecto? | Úsalo para |
|---|---|---|---|
| **Marcadores del proyecto** | Dentro del `.qgz` | Sí | Lugares de **ese** trabajo que otros necesitan |
| **Marcadores del usuario** | En tu perfil | No | Lugares que **tú** usas en muchos proyectos |

### Paso 8 · Ordenar y agrupar capas

Las capas se dibujan **de abajo hacia arriba**. Un orden que casi siempre funciona: **puntos** ▸ **líneas** ▸ **polígonos** ▸ **ráster** ▸ **mapas base**.

1. Renombra `zonas_analisis` como **Zonas de análisis** (clic derecho ▸ **Cambiar nombre de capa**).
2. Muévela al grupo **Referencia**.
3. Activa **Mostrar recuento de objetos** en `Comunas`: debe indicar **6**.
4. Agrega el mapa base **OpenStreetMap** desde **Navegador ▸ XYZ Tiles**, crea un grupo **Mapas base** y márcalo como **Grupo mutuamente excluyente**.

!!! captura "Captura pendiente · 2.2-14"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-2/2-2-14-agrupar-ordenar.gif`
    - **Qué mostrar:** Crear los grupos `Referencia` y `Mapas base`, arrastrar capas, cambiar el orden de dibujo y convertir `Mapas base` en grupo mutuamente excluyente.

??? info "Para saber más · temas del mapa y atajos"

    Los **temas del mapa** (ícono del ojo en el panel Capas) guardan combinaciones de capas visibles y estilos, para alternar entre vistas del mismo proyecto. Los usarás en las composiciones del Módulo 4.

    | Acción | Atajo |
    |---|---|
    | Nuevo / abrir / guardar proyecto | ++ctrl+n++ / ++ctrl+o++ / ++ctrl+s++ |
    | Administrador de fuentes de datos | ++ctrl+l++ |
    | Localizador | ++ctrl+k++ |
    | Identificar | ++ctrl+shift+i++ |
    | Medir línea | ++ctrl+shift+m++ |
    | Nuevo marcador / administrador | ++ctrl+b++ / ++ctrl+shift+b++ |
    | Panel Capas / Navegador | ++ctrl+1++ / ++ctrl+2++ |
    | Estilo de capas | ++f7++ |
    | Caja de herramientas de Procesos | ++ctrl+alt+t++ |
    | Ocultar paneles / pantalla completa | ++ctrl+tab++ / ++f11++ |

    Consulta y modifica todos en **Configuración ▸ Atajos de teclado**.

---

## Inténtalo tú

!!! example "Reto 2.2 · Preparar la reunión del equipo"

    Guarda el proyecto como `proyectos/reto_2-2_exploracion.qgz` y deja listo lo siguiente, **sin mirar los pasos anteriores**:

    1. **Seis marcadores del proyecto** en al menos dos grupos. Sugerencias:
        - `Centros urbanos`: Plaza 14 de Septiembre, La Cancha.
        - `Equipamientos`: Hospital Viedma, Universidad Mayor de San Simón.
        - `Ambiente y riesgo`: Laguna Alalay, río Rocha, torrenteras del Parque Tunari.
    2. **Un marcador del usuario** con la ubicación de tu institución u hogar.
    3. **Capas organizadas**: grupos `Referencia`, `Red vial e hidrografía`, `Ráster` y `Mapas base`, con nombres claros y orden lógico.
    4. Para cada comuna, anota su `area_km2` y su área **derivada**. ¿Qué comuna es más grande? ¿Cuánto difieren ambos valores en porcentaje?
    5. **Exporta** los marcadores del proyecto a `salidas/marcadores_cochabamba.xml` e intercambia el proyecto con un compañero: ¿ve tus seis marcadores? ¿Y el del usuario? ¿Por qué?

    **Entregables:** el proyecto, el archivo de marcadores y media página con las respuestas de los puntos 4 y 5.

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Marcadores | Hay seis marcadores del proyecto en dos o más grupos y uno del usuario |
| Organización | Grupos con nombres claros, capas renombradas y orden de dibujo lógico |
| Análisis | La tabla de áreas está completa y la diferencia (≈ 0,1 %) se explica por el método de cálculo |
| Comprensión | Se explica por qué el compañero no ve el marcador del usuario |

### Errores frecuentes

| Síntoma | Causa probable | Solución |
|---|---|---|
| Desapareció un panel | Se cerró o se ocultó con ++ctrl+tab++ | **Ver ▸ Paneles** o ++ctrl+tab++ |
| El mapa base no se ve | Sin internet, o está debajo de una capa opaca | Revisa la conexión y el orden |
| Identificar no muestra nada | Modo **Capa actual** con otra capa seleccionada | Selecciona la capa o cambia el modo |
| El compañero no ve mis marcadores | Se guardaron como **del usuario** | Guárdalos en el proyecto o expórtalos |
| Una capa activada no se ve | Está debajo de otra, fuera de vista o con visibilidad por escala | Revisa el orden, **Zoom a la capa** y el rango de escalas |
| Las coordenadas «no tienen sentido» | Están en el SRC del proyecto | Revisa el SRC del proyecto ([2.6](06-problemas-coordenadas.md)) |

---

## Comprueba lo aprendido

??? question "1. ¿Cómo encontrarías la herramienta para recortar una capa si no sabes en qué menú está?"

    Con el **localizador**: ++ctrl+k++ y escribe *recortar*, o `a recortar` para buscar solo entre las herramientas de Procesos.

??? question "2. En modo Capa actual haces clic sobre una escuela y no aparece nada. ¿Qué pasó?"

    La capa **seleccionada** en el panel Capas no es la de escuelas. Selecciona la correcta o cambia el modo a **De arriba abajo**.

??? question "3. ¿Qué diferencia hay entre un marcador del proyecto y uno del usuario?"

    El del **proyecto** se guarda en el `.qgz` y lo ve cualquiera que abra el proyecto. El del **usuario** se guarda en tu **perfil** y solo lo ves tú, en cualquier proyecto.

??? question "4. Una capa de puntos activada no se ve, aunque sus datos están en la vista. ¿Qué revisas primero?"

    El **orden de dibujo**: probablemente está **debajo** de polígonos o de un mapa base opaco. Después, si tiene **visibilidad por escala**.

??? question "5. La superficie almacenada y el área derivada no coinciden. ¿Hay un error?"

    **No necesariamente.** Pudieron calcularse con otra geometría, otro SRC, otro método (plano o elipsoide) u otra fecha. Averigua cómo se obtuvo cada valor antes de concluir.

??? question "6. Eliminas una capa del panel Capas por error. ¿Perdiste los datos?"

    **No.** Solo la quitaste del proyecto; el archivo sigue en su carpeta.

??? question "7. Repaso de 1.8 · Escribes 25000 en la casilla de escala. ¿Cuántos metros del terreno representa 1 cm de la pantalla?"

    **250 m** (25 000 cm). Recuerda que en pantalla la escala es aproximada: depende de la resolución del monitor.

---

## Tu proyecto

Crea en tu proyecto los marcadores de los **lugares críticos del caso conductor**: dos zonas que creas con buen acceso a servicios y dos que sospeches que tienen mal acceso. En la lección [3.7](../modulo-03/07-proximidad-superposicion.md) comprobarás si tu intuición coincide con el análisis.

---

## Referencias

- Cutts, A., & Graser, A. (2018). *Learning QGIS* (4.ª ed.). Packt.
- QGIS Project. (s. f.). *Manual de usuario: Interfaz de QGIS*. <https://docs.qgis.org/latest/es/docs/user_manual/introduction/qgis_gui.html>
- QGIS Project. (s. f.). *Manual de usuario: Herramientas generales*. <https://docs.qgis.org/latest/es/docs/user_manual/introduction/general_tools.html>
- QGIS Project. (s. f.). *Manual de usuario: Abrir datos*. <https://docs.qgis.org/latest/es/docs/user_manual/managing_data_source/opening_data.html>
- OpenStreetMap Foundation. (s. f.). *Nominatim Usage Policy*. <https://operations.osmfoundation.org/policies/nominatim/>
