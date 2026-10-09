---
title: 2.3 Comprender y gestionar proyectos
description: Proyectos y fuentes de datos en QGIS, formatos QGS y QGZ, guardado, propiedades, rutas relativas, recuperación de capas y preparación de proyectos para compartir.
---

# 2.3 Comprender y gestionar proyectos

Terminas tu mapa de Cochabamba, guardas `exploracion.qgz` y se lo envías a una compañera. En tu computadora funciona; en la suya aparece un mensaje de **capas no disponibles**. ¿Qué falló? Que el proyecto **recuerda dónde están los datos**, pero no los lleva consigo. En esta lección aprenderás a preparar un trabajo que se pueda cerrar, mover, reparar y entregar.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Distinguir **proyecto**, **fuentes de datos** y **productos exportados**.
    - Guardar con intención y documentar un proyecto con sus propiedades y metadatos.
    - Explicar y configurar **rutas relativas**.
    - **Reparar** capas cuya fuente cambió de lugar, sin perder su configuración.
    - Comprobar una entrega **desde otra ubicación**.

    **Tiempo:** 90 min (25 de lectura · 65 de práctica) · **Datos:** `proyectos/reto_2-2_exploracion.qgz` · **Producto:** entrega comprimida y comprobada, con `LEEME.txt`.

---

## Idea central

### Proyecto, datos y productos

| Elemento | Ejemplo en el curso | Responde a… |
|---|---|---|
| **Proyecto** | `proyectos/curso_qgis_base.qgz` | ¿Cómo está organizado y representado el trabajo? |
| **Fuente vectorial** | `datos/originales/limites.gpkg` | ¿Cuáles son las geometrías y atributos? |
| **Fuente ráster** | `datos/originales/dem_copernicus_30m.tif` | ¿Qué valor tiene cada celda? |
| **Servicio web** | Mapa base OpenStreetMap (XYZ) | ¿Qué puedo pedirle al servidor? |
| **Producto exportado** | `salidas/mapa_comunas.pdf` | ¿Qué entrego para su lectura? |

!!! captura "Captura pendiente · 2.3-01"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-01-proyecto-datos-producto.png`
    - **Qué mostrar:** El archivo `.qgz`, una fuente `.gpkg` y un PDF en sus carpetas; junto a ellos, QGIS con la capa cargada. Rótulos **Proyecto**, **Datos** y **Producto**.

| Si haces esto… | …cambia | …y debes conservar |
|---|---|---|
| Cambias el color o el nombre visible de una capa | El proyecto | El proyecto guardado |
| Editas y guardas un atributo o una geometría | La fuente de datos | Los datos |
| Quitas una capa del panel | La lista de capas del proyecto | Nada se borra: el archivo sigue ahí |
| Exportas un mapa | Se crea un producto | El producto, el proyecto y los datos |

!!! danger "Un QGZ no es una entrega completa"

    El `.qgz` es un archivo comprimido, pero **no incluye** tus GeoPackage, imágenes ni tablas: solo sus **referencias**. Y **Guardar como** crea otro proyecto que sigue apuntando **a los mismos datos**: si editas desde uno, el otro verá los cambios.

### Rutas absolutas y relativas

Una **ruta** indica dónde está un archivo. Desde `proyectos/reto_2-3_gestion.qgz`, la capa de límites se alcanza así:

| Tipo | Ruta | Al trasladar el trabajo… |
|---|---|---|
| **Absoluta** | `C:/curso-qgis/datos/originales/limites.gpkg` | Busca esa ubicación exacta, que puede no existir en otro equipo |
| **Relativa** | `../datos/originales/limites.gpkg` | Funciona mientras se conserve la relación entre proyecto y datos |

Se lee: `..` = subir de `proyectos/` a `curso-qgis/`; luego entrar a `datos/originales/` y abrir `limites.gpkg`.

!!! captura "Captura pendiente · 2.3-05"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-05-ruta-relativa.png`
    - **Qué mostrar:** El árbol de carpetas del curso con una flecha que parte de `proyectos/`, sube un nivel y entra en `datos/originales/`.

!!! warning "Relativa no significa incluida"

    `../../otra_carpeta/limites.gpkg` también es relativa, pero depende de un archivo **fuera** de lo que vas a entregar. La opción **Relativas** no copia datos ni reúne dependencias dispersas.

| Si… | …entonces |
|---|---|
| Copias `curso-qgis/` completa | Las rutas relativas siguen funcionando |
| Envías solo el `.qgz` | Faltan las fuentes locales |
| Renombras `datos/originales/` | El proyecto busca una carpeta que ya no existe |
| Cambias el título del proyecto | No se mueve ni renombra ningún archivo |

---

## Hazlo conmigo

### Paso 1 · Guardar con intención

1. Abre `proyectos/reto_2-2_exploracion.qgz`.
2. **Proyecto ▸ Guardar como…** ▸ `proyectos/reto_2-3_gestion.qgz`. Revisa nombre y carpeta antes de aceptar.
3. Cambia el nombre visible de una capa. Observa el **asterisco `*`** en la barra de título: hay cambios sin guardar.
4. Guarda con ++ctrl+s++, cierra el proyecto y vuelve a abrirlo.

!!! captura "Captura pendiente · 2.3-02"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-02-guardar-reabrir.gif`
    - **Qué mostrar:** Abrir **Guardar como**, elegir la carpeta `proyectos/`, guardar el QGZ, cambiar un nombre de capa, guardar y volver a abrir el archivo.

!!! tip "Guarda en momentos reconocibles"

    Guarda al terminar cada tarea. Antes de un cambio importante, conserva una copia con nombre descriptivo: `exploracion_antes_revision.qgz`. La lista **Abrir reciente** es un acceso rápido, **no** un respaldo.

### Paso 2 · Documentar el proyecto

Abre **Proyecto ▸ Propiedades…**:

| Pestaña | Qué completar |
|---|---|
| **General ▸ Título** | `Exploración territorial de Cochabamba` |
| **General ▸ Guardar rutas** | **Relativas** |
| **Metadatos** | Autor, resumen y palabras clave |
| **SRC** | Debe ser EPSG:32719 (lo verás a fondo en [2.6](06-problemas-coordenadas.md)) |

Un buen resumen permite entender el trabajo sin preguntarte. Por ejemplo:

> Proyecto de exploración de Cochabamba para la práctica 2.3. Reúne límites, comunas, red vial y marcadores de lugares de interés. Datos de OpenStreetMap; no constituye una delimitación oficial.

!!! captura "Captura pendiente · 2.3-03"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-03-propiedades-general.png`
    - **Qué mostrar:** La sección **General** de las propiedades del proyecto, destacando título, inicio del proyecto y guardado de rutas.

!!! captura "Captura pendiente · 2.3-04"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-04-metadatos.png`
    - **Qué mostrar:** La pestaña **Metadatos** con título, autor de ejemplo, resumen y palabras clave del ejercicio.

### Paso 3 · Comprobar de dónde lee cada capa

Para cada capa: clic derecho ▸ **Propiedades ▸ Información**. La ruta debe estar **dentro** de `curso-qgis/`. Ver el mapa no basta: una capa puede estar leyendo una copia antigua en otra carpeta.

### Paso 4 · Simular un traslado y repararlo

1. Cierra QGIS. Copia **toda** la carpeta `curso-qgis/` a `prueba_entrega/curso-qgis/`.
2. **En la copia**, renombra `datos/originales/` como `datos/originales_reubicados/`.
3. Abre `prueba_entrega/curso-qgis/proyectos/reto_2-3_gestion.qgz`. Aparece el diálogo de **capas no disponibles**.
4. Selecciona cada capa afectada, busca el **mismo archivo** en la carpeta renombrada y aplica los cambios. También puedes repararla después con clic derecho ▸ **Reparar fuente de datos…**
5. Verifica nombre, estilo y atributos; guarda, cierra y vuelve a abrir.

!!! captura "Captura pendiente · 2.3-06"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-06-reparar-fuente.gif`
    - **Qué mostrar:** Un proyecto con una fuente trasladada, la selección de su nueva ubicación y la reaparición de la capa conservando nombre y estilo.

!!! danger "Una capa parecida no es necesariamente la correcta"

    Antes de enlazar, compara **tipo de geometría, campos, número de entidades, extensión y procedencia**. Un archivo de otra fecha puede mostrar un mapa convincente con información distinta.

### Paso 5 · Distinguir los tres «guardar»

| Situación | Qué hacer |
|---|---|
| Organizaste capas o cambiaste su estilo | Guardar el **proyecto** |
| Editaste atributos o geometrías | Guardar las **ediciones de la capa** |
| Creaste una capa **temporal** (en memoria) | Hacerla **permanente** en un GeoPackage; guardar el proyecto no basta |

!!! captura "Captura pendiente · 2.3-07"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-07-temporal-persistente.png`
    - **Qué mostrar:** El indicador de una capa temporal y la acción para hacerla permanente, con el destino `datos/trabajo/observaciones.gpkg`.

??? info "Para saber más · QGS, QGZ, almacenamiento auxiliar y plantillas"

    - **`.qgs`** es el proyecto en XML (texto); **`.qgz`** es un ZIP que contiene el `.qgs` y, si existe, el **almacenamiento auxiliar** (`.qgd`), donde QGIS guarda, por ejemplo, posiciones de etiquetas movidas a mano. Con `.qgs`, el `.qgd` queda como archivo aparte: consérvalo junto al proyecto.
    - Al guardar un `.qgs`, QGIS crea una copia `.qgs~` del proyecto (no de los datos).
    - Las **plantillas de proyecto** (**Proyecto ▸ Nuevo a partir de plantilla**) reutilizan grupos y propiedades; tampoco copian datos.

---

## Inténtalo tú

!!! example "Reto 2.3 · Entregar un proyecto que funcione en cualquier computadora"

    1. Prepara `reto_2-3_gestion.qgz` con rutas relativas, título, resumen y marcadores del proyecto.
    2. Anota **tres controles** de la capa `Comunas`: número de entidades (6), nombres de dos campos y el `area_km2` de Tunari.
    3. Escribe `LEEME.txt` en la raíz de la carpeta: qué proyecto abrir, versión de QGIS, fuentes y licencias (ver `datos/originales/LEEME.md`), y qué capas requieren internet.
    4. Desactiva el mapa base y comprueba que las capas locales siguen funcionando.
    5. Con QGIS cerrado, **comprime** la carpeta. Extráela en una **tercera** ubicación, abre el proyecto y comprueba que lee los datos **de esa extracción** y que los tres controles coinciden.

    **Entregables:** el ZIP, una captura del proyecto abierto desde la extracción con la ruta de una capa visible, y un párrafo que explique por qué el traslado completo funcionó y el renombrado del paso 4 exigió reparar.

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Independencia | Todas las capas locales apuntan a archivos **dentro** de la entrega |
| Documentación | Título, resumen y `LEEME.txt` permiten abrir y entender el trabajo |
| Recuperación | La fuente reubicada vuelve a funcionar conservando nombre y estilo |
| Verificación | Los tres controles coinciden antes y después del traslado |
| Dependencias | Los servicios web están identificados por separado |

### Errores frecuentes

| Síntoma | Causa probable | Solución |
|---|---|---|
| Envié el QGZ y faltan capas | No se incluyeron las fuentes | Entrega proyecto **y** datos con su estructura |
| Solo funciona en mi equipo | Hay capas que apuntan fuera de la entrega | Revisa el origen de cada capa y enlaza las copias internas |
| Rutas relativas, pero falta una capa | Cambió una carpeta interna | Repara la fuente y guarda |
| Tras reparar, faltan campos | Se eligió otra versión u otra capa interna | Compara campos, entidades y procedencia |
| Desaparecieron los datos de una capa temporal | Nunca se guardaron en un archivo | Hazla permanente antes de cerrar |
| El mapa base no se ve sin internet | Es un servicio remoto | Documenta la dependencia |

---

## Comprueba lo aprendido

??? question "1. Tu proyecto pesa poco pero usa una imagen de 500 MB. ¿Está la imagen dentro del QGZ?"

    No. El proyecto guarda la **referencia** a la imagen. Si debe viajar, inclúyela en la entrega.

??? question "2. Guardaste una segunda versión del proyecto y editaste un atributo. ¿Por qué cambió también en la primera?"

    Porque ambos proyectos leen **la misma fuente**. **Guardar como** duplica la configuración, no los datos. Para trabajar de forma independiente necesitas copiar los datos y enlazar la copia.

??? question "3. Proyecto en `proyectos/mapa.qgz`, datos en `datos/originales/limites.gpkg`. ¿Cuál es la ruta relativa?"

    `../datos/originales/limites.gpkg`.

??? question "4. Copias una carpeta, abres su proyecto y el mapa se ve bien. ¿Qué falta comprobar?"

    El **origen real** de cada capa: podría seguir leyendo los archivos de la ubicación anterior.

??? question "5. Tras reparar una ruta aparece el mapa, pero falta un campo que usabas para etiquetar. ¿Terminaste?"

    No. Probablemente enlazaste otro conjunto de datos o otra capa interna del GeoPackage. Verifica antes de guardar.

??? question "6. Repaso de 1.12 · ¿Por qué el resumen del proyecto no reemplaza a los metadatos de cada fuente?"

    Porque describe el **trabajo**, no la **procedencia, fecha, SRC, calidad y licencia** de cada dato. Cada fuente necesita su propia documentación.

---

## Tu proyecto

A partir de ahora, **todo** tu trabajo del caso conductor vive en `curso-qgis/` y cada entrega se comprueba desde otra carpeta antes de enviarse. Añade a tu `LEEME.txt` una sección «Historial» donde registrarás, lección a lección, qué datos derivados creas en `datos/trabajo/`.

---

## Referencias

- Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLOS Computational Biology, 13*(6), e1005510. <https://doi.org/10.1371/journal.pcbi.1005510>
- QGIS Project. (s. f.). *Manual de usuario: Trabajar con archivos de proyecto*. <https://docs.qgis.org/latest/es/docs/user_manual/introduction/project_files.html>
- QGIS Project. (s. f.). *Manual de usuario: Configuración de QGIS*. <https://docs.qgis.org/latest/es/docs/user_manual/introduction/qgis_configuration.html>
- QGIS Project. (s. f.). *Manual de usuario: Formatos de archivo de QGIS*. <https://docs.qgis.org/latest/es/docs/user_manual/appendices/qgis_file_formats.html>
- QGIS Project. (s. f.). *Manual de usuario: Crear capas nuevas*. <https://docs.qgis.org/latest/es/docs/user_manual/managing_data_source/create_layers.html>
