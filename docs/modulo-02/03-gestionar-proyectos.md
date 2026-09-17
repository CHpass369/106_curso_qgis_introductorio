---
title: 2.3 Comprender y gestionar proyectos
description: Proyectos y fuentes de datos en QGIS, formatos QGS y QGZ, guardado, propiedades, rutas relativas, recuperación de capas y preparación de proyectos para compartir.
---

# 2.3 Comprender y gestionar proyectos

!!! abstract "Objetivos de aprendizaje"

    Al finalizar esta lección, el estudiante será capaz de:

    - Distinguir el **proyecto**, las **fuentes de datos** y los **productos exportados**.
    - Crear, abrir y guardar proyectos, comprendiendo las diferencias entre **Guardar** y **Guardar como**.
    - Configurar las propiedades básicas y documentar el propósito de un proyecto.
    - Organizar archivos y explicar cómo funcionan las **rutas relativas y absolutas**.
    - Recuperar capas con fuentes no disponibles sin perder su configuración.
    - Preparar y comprobar una copia del trabajo antes de compartirla.

!!! note "Antes de empezar"

    - **Entorno:** QGIS con el perfil `curso-qgis`. Los procedimientos toman como referencia **QGIS 3.44**; algunas traducciones de los botones pueden variar.
    - **Punto de partida:** el proyecto de la [lección 2.2](02-orientarse-interfaz.md), o un proyecto con al menos una capa vectorial **local** que puedas consultar.
    - **Datos:** una copia de esa capa y sus archivos asociados. No necesitas descargar datos nuevos ni modificar los originales.
    - **Conexión a internet:** solo si conservas un mapa base o un servicio web. La práctica principal se realiza con archivos locales.
    - **Tiempo orientativo:** entre **90 y 120 minutos**, incluida la práctica. Es una estimación para trabajo autónomo.

---

## Un mapa que se ve, pero no viaja

Imagina esta situación: terminas de organizar un mapa del municipio, guardas `municipio.qgz` y se lo envías a una compañera. En tu computadora funciona; en la suya aparecen capas no disponibles.

El problema puede estar en **qué enviaste**: el proyecto recuerda dónde están los datos, pero guardar el proyecto **no incorpora automáticamente esos archivos**.

En esta lección prepararás un trabajo que puedas cerrar, volver a abrir y trasladar. La comprobación final será sencilla: **abrirlo desde otra ubicación y verificar que consulta los datos de la copia**.

---

## Proyecto, datos y productos

### Tres elementos con funciones distintas

Un **proyecto de QGIS** organiza cómo trabajas con la información: qué capas utilizas, dónde se encuentran, cómo se representan y qué vistas has preparado.

Las **fuentes de datos** contienen la información consultada: geometrías, atributos, píxeles o recursos de un servicio. Un **producto exportado**, como una imagen o un PDF, comunica una representación del trabajo.

| Elemento | Ejemplo | Pregunta que ayuda a responder |
|---|---|---|
| **Proyecto** | `municipio.qgz` | ¿Cómo está organizado y representado este trabajo? |
| **Fuente vectorial** | `limites.gpkg` | ¿Cuáles son las geometrías y los atributos de los municipios? |
| **Fuente ráster** | `elevacion.tif` | ¿Qué valor tiene cada píxel de la superficie? |
| **Servicio web** | Un mapa base XYZ | ¿Qué información puedo solicitar al servidor? |
| **Producto exportado** | `mapa_municipio.pdf` | ¿Qué mapa quiero entregar para su lectura? |

!!! captura "Captura pendiente · 2.3-01"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-01-proyecto-datos-producto.png`
    - **Qué mostrar:** El archivo `.qgz`, una fuente `.gpkg` y un PDF en sus carpetas; junto a ellos, QGIS con la capa cargada. Señalar sus funciones con los rótulos **Proyecto**, **Datos** y **Producto**.
    - **Sugerencia:** Usar nombres de ejemplo y ocultar rutas personales.

### Qué sucede cuando cambias algo

| Acción | Qué cambia | Qué debes conservar |
|---|---|---|
| Cambiar el color o el nombre visible de una capa | Su configuración en el proyecto | El proyecto actualizado |
| Reordenar capas, crear grupos o guardar marcadores del proyecto | La organización del trabajo | El proyecto actualizado |
| Editar y guardar un atributo o una geometría | La fuente de datos editada | Los datos actualizados |
| Quitar del panel una capa local guardada | La lista de capas del proyecto | Su archivo sigue en la carpeta |
| Exportar el mapa a una imagen | Se crea un producto de salida | La imagen, además del proyecto y los datos si quieres seguir trabajando |

!!! warning "Dos proyectos pueden utilizar los mismos datos"

    Puedes tener `municipio_borrador.qgz` y `municipio_revision.qgz` con colores distintos, pero ambos pueden apuntar a **la misma capa**. Si editas y guardas sus datos desde uno, el otro leerá esos cambios. **Guardar como** crea otro proyecto; no crea una copia independiente de sus fuentes.

---

## Los formatos QGS y QGZ

QGIS guarda los proyectos principalmente en dos formatos:

| Formato | Característica | Uso en el curso |
|---|---|---|
| **`.qgs`** | Descripción del proyecto en XML, un formato de texto estructurado | Reconocerlo cuando recibas proyectos existentes |
| **`.qgz`** | Archivo comprimido que contiene el proyecto y puede incluir su almacenamiento auxiliar | Formato habitual para guardar los ejercicios |

El almacenamiento auxiliar puede contener ajustes vinculados a entidades, como determinadas posiciones de etiquetas. **No equivale a las capas originales** del trabajo.

!!! danger "Un QGZ no es una entrega completa por sí mismo"

    Que el archivo esté comprimido **no significa** que incluya automáticamente tus GeoPackage, imágenes, tablas o archivos Shapefile. Antes de enviarlo, comprueba qué fuentes y recursos necesita.

??? info "Para saber más: el almacenamiento auxiliar"

    El almacenamiento auxiliar utiliza una base de datos `.qgd`. En un proyecto QGZ puede guardarse dentro del archivo comprimido; con QGS se mantiene como archivo separado. Si tu proyecto QGS tiene un `.qgd` asociado, consérvalo junto a él. No necesitas abrir ni editar manualmente estos archivos para realizar la lección.

---

## Crear, guardar y volver a abrir

### Operaciones básicas

| Acción | Menú | Atajo habitual |
|---|---|---|
| Crear un proyecto | **Proyecto ▸ Nuevo** | ++ctrl+n++ |
| Abrir uno existente | **Proyecto ▸ Abrir…** | ++ctrl+o++ |
| Guardar el proyecto actual | **Proyecto ▸ Guardar** | ++ctrl+s++ |
| Guardar con otro nombre o ubicación | **Proyecto ▸ Guardar como…** | ++ctrl+shift+s++ |

Los atajos se pueden personalizar. Si uno no coincide con tu instalación, consulta **Configuración ▸ Atajos de teclado**.

### Guardar con intención

1. Abre el proyecto de la lección anterior.
2. Usa **Guardar como…** y elige `proyectos/reto_2-3_gestion.qgz` dentro de tu carpeta de trabajo.
3. Comprueba el **nombre y la ubicación** seleccionados antes de aceptar.
4. Cambia un nombre visible de capa o crea un grupo.
5. Guarda de nuevo con ++ctrl+s++.
6. Cierra el proyecto y ábrelo desde el archivo que acabas de guardar.

**Resultado esperado:** reaparecen las capas y la organización guardada. Si una fuente no está disponible, conserva la capa en el proyecto y revisa su ubicación siguiendo la sección de recuperación.

!!! captura "Captura pendiente · 2.3-02"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-02-guardar-reabrir.gif`
    - **Qué mostrar:** Abrir **Guardar como**, elegir la carpeta `proyectos/`, guardar el QGZ, cambiar un nombre de capa, guardar y volver a abrir el archivo.
    - **Sugerencia:** Mostrar el nombre del archivo al inicio y al final para comprobar que se abrió la copia correcta.

### Reconocer cambios pendientes

Un **asterisco `*` en la barra de título** indica cambios pendientes en el proyecto. Los avisos al cerrar ayudan a decidir si guardarlos, pero no sustituyen un hábito de guardado.

!!! tip "Guarda en momentos reconocibles"

    Guarda después de completar una tarea: organizar capas, preparar una vista o corregir una ruta. Antes de una modificación importante, conserva una copia con un nombre que explique su función, por ejemplo `municipio_antes_revision.qgz`.

La lista **Abrir reciente** es un acceso rápido, no un respaldo. Una entrada puede seguir apareciendo aunque hayas movido el archivo.

---

## Propiedades del proyecto

Abre **Proyecto ▸ Propiedades…**. Estas opciones pertenecen al trabajo actual; las preferencias generales de **Configuración ▸ Opciones** se guardan en el perfil de usuario.

| Configuración | Qué conviene revisar ahora | Qué significa para el trabajo |
|---|---|---|
| **General: título** | Un nombre comprensible, como `Exploración territorial del municipio` | Describe el proyecto; no cambia por sí mismo el nombre del archivo |
| **General: guardar rutas** | Relativas o absolutas | Determina cómo se registran las ubicaciones de archivos |
| **General: inicio del proyecto** | Carpeta usada como acceso desde el Navegador | Facilita localizar recursos; no los mueve |
| **Metadatos** | Título, autor, resumen y palabras clave | Explica el propósito y contexto del proyecto |
| **SRC** | Sistema de referencia del proyecto | Define el marco de representación; se trabajará en la lección **2.6** |
| **General: mediciones** | Elipsoide y unidades de distancia y superficie | Ayuda a interpretar mediciones; se profundizará en la lección **2.6** |

!!! captura "Captura pendiente · 2.3-03"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-03-propiedades-general.png`
    - **Qué mostrar:** La sección **General** de las propiedades del proyecto, destacando título, inicio del proyecto y guardado de rutas.
    - **Sugerencia:** Numerar solo esos tres controles para evitar sobrecargar la captura.

### Escribir metadatos útiles

Un resumen debe permitir que otra persona entienda el trabajo sin preguntarte cómo lo preparaste. Por ejemplo:

> Proyecto de exploración de límites municipales para la práctica 2.3. Reúne una capa local y marcadores de lugares de interés. Se utiliza para aprender a organizar y trasladar proyectos; no constituye una delimitación oficial elaborada por el estudiante.

Añade el autor y palabras clave pertinentes. En una nota de entrega registra también la procedencia, fecha y condiciones de uso de las capas. **Describir el proyecto no reemplaza documentar cada fuente**, como vimos en el tema 1.12.

!!! captura "Captura pendiente · 2.3-04"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-04-metadatos.png`
    - **Qué mostrar:** La pestaña **Metadatos** con título, autor de ejemplo, resumen y palabras clave del ejercicio.

!!! note "El inicio del proyecto no cambia la base de las rutas"

    Por defecto, el inicio del proyecto corresponde a su carpeta. Puedes establecer otro acceso para el Navegador, pero las rutas relativas de esta lección se interpretan respecto de **la ubicación del archivo de proyecto**, no de ese acceso personalizado.

---

## Organizar las carpetas antes de compartir

Para el ejercicio utilizaremos esta estructura. Los nombres de los datos son **ejemplos**: adáptalos a tu capa local.

```text
trabajo_municipio/
├── proyectos/
│   └── reto_2-3_gestion.qgz
├── datos/
│   ├── originales/
│   │   └── limites.gpkg
│   └── trabajo/
├── recursos/
├── salidas/
└── LEEME.txt
```

| Carpeta o archivo | Qué guardar |
|---|---|
| **`proyectos/`** | Archivos QGIS con nombres que distingan ejercicios o versiones |
| **`datos/originales/`** | Copias de los datos recibidos, conservadas sin editar |
| **`datos/trabajo/`** | Datos derivados o copias que vayas a modificar en lecciones posteriores |
| **`recursos/`** | Imágenes y símbolos externos que utilice el proyecto |
| **`salidas/`** | Mapas exportados y otros resultados de entrega |
| **`LEEME.txt`** | Instrucciones para abrir el trabajo, fuentes y comprobaciones realizadas |

!!! tip "Nombres que ayudan a trabajar"

    Usa nombres breves y descriptivos para archivos, como `limites_municipales.gpkg`. Evita cadenas ambiguas como `final_final_ahora_si.qgz`. En el panel Capas puedes usar títulos más legibles, como **Límites municipales**, sin renombrar el archivo.

!!! warning "Un conjunto de datos puede tener varios archivos"

    Si utilizas un Shapefile, copia **todos sus archivos asociados**, no solamente el `.shp`: geometrías, tabla, índices y definición del SRC pueden estar en archivos separados. En la lección **2.4** se estudiarán las diferencias entre formatos.

---

## Rutas absolutas y relativas

Una **ruta** indica dónde se encuentra un archivo. Entenderla te permitirá explicar por qué un proyecto funciona en una computadora y falla en otra.

### Leer una ruta relativa

Con la estructura anterior, desde `proyectos/reto_2-3_gestion.qgz` se llega a los datos mediante:

```text
../datos/originales/limites.gpkg
```

Se interpreta así:

1. `..`: subir desde `proyectos/` a `trabajo_municipio/`.
2. `datos/originales/`: entrar en esas carpetas.
3. `limites.gpkg`: abrir el archivo indicado.

| Tipo | Ejemplo | Qué ocurre al trasladar el trabajo |
|---|---|---|
| **Absoluta** | `C:/curso/trabajo_municipio/datos/originales/limites.gpkg` | Busca esa ubicación exacta; puede no existir en otro equipo |
| **Relativa** | `../datos/originales/limites.gpkg` | Sigue funcionando si se conserva la relación entre proyecto y datos |

En Linux, una ruta absoluta puede comenzar por `/home/`; en Windows suele incluir una unidad. El principio es el mismo.

!!! captura "Captura pendiente · 2.3-05"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-05-ruta-relativa.png`
    - **Qué mostrar:** El árbol de carpetas del ejercicio con una flecha que parte de `proyectos/`, sube un nivel y entra en `datos/originales/`.
    - **Sugerencia:** Incluir `../datos/originales/limites.gpkg` junto al recorrido.

### Configurar y comprobar las rutas

1. Guarda primero el proyecto en su ubicación definitiva dentro del ejercicio.
2. En **Proyecto ▸ Propiedades… ▸ General**, establece **Guardar rutas** en **Relativas**.
3. Aplica el cambio y guarda el proyecto.
4. Comprueba que las capas apuntan a archivos dentro de tu carpeta de trabajo. Puedes consultar su origen en **Propiedades de la capa ▸ Información**.
5. Prueba una copia en otra ubicación, como se indica en el reto.

!!! warning "Relativo no significa incluido"

    Una ruta como `../../otra_carpeta/limites.gpkg` sigue siendo relativa, pero depende de un archivo **fuera** de la carpeta que piensas entregar. La opción **Relativas** no copia los datos ni reúne dependencias dispersas.

### Qué movimientos mantienen los enlaces

| Cambio | Resultado que debes esperar |
|---|---|
| Copiar `trabajo_municipio/` completa conservando su estructura | Las rutas relativas internas pueden resolverse desde la nueva ubicación |
| Enviar solo el `.qgz` | Faltarán las fuentes locales que el destinatario no tenga |
| Renombrar `datos/originales/` sin actualizar referencias | El proyecto buscará una carpeta que ya no existe con ese nombre |
| Elegir **Guardar como** en otra carpeta | Cambia la ubicación del proyecto; sus fuentes siguen siendo las mismas hasta que las cambies |
| Cambiar el título en las propiedades | No traslada ni renombra archivos |

---

## Recuperar capas con fuentes no disponibles

Una capa no disponible significa que QGIS **no puede acceder a su fuente**. Puede haberse movido un archivo, desconectado una unidad o interrumpido un servicio.

### Diagnosticar antes de cambiar

1. Identifica **qué capa** falla y **qué fuente** esperaba encontrar.
2. Si es un archivo, comprueba que existe y que puedes acceder a su carpeta.
3. Si es un servicio, comprueba la conexión y la disponibilidad o los permisos del servidor.
4. Si el archivo fue trasladado, localiza **el mismo conjunto de datos** en su nueva ubicación.

Un mapa vacío sin avisos también puede deberse a la escala, el orden de capas o la extensión visible. Revisa esas posibilidades de la lección 2.2 antes de cambiar una fuente.

### Reparar el vínculo

Al abrir un proyecto con fuentes ausentes, QGIS presenta un diálogo de **capas no disponibles**. Selecciona la capa afectada, busca su archivo y **aplica los cambios**.

También puedes conservar las capas no disponibles y repararlas después mediante el indicador junto a la capa o la opción **Reparar fuente de datos…** de su menú contextual. Los rótulos pueden aparecer como *Handle Unavailable Layers* y *Repair Data Source…* si la interfaz está en inglés.

!!! captura "Captura pendiente · 2.3-06"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-06-reparar-fuente.gif`
    - **Qué mostrar:** Un proyecto de práctica con una fuente trasladada, la selección de su nueva ubicación y la reaparición de la capa conservando su nombre y estilo.
    - **Sugerencia:** Mostrar el nombre antiguo y el nuevo de la carpeta; realizar la demostración sobre una copia.

!!! danger "Una capa parecida no es necesariamente la correcta"

    No sustituyas la fuente por cualquier archivo con un nombre similar. Compara **tipo de geometría, campos, número de entidades, extensión y procedencia**. Una capa de otra fecha puede abrirse y mostrar un mapa convincente, pero representar información diferente.

Después de reparar, revisa atributos, simbología y ubicación; guarda y vuelve a abrir. Reparar el vínculo conserva la configuración existente y evita reconstruirla al quitar y volver a cargar la capa.

---

## Guardar el proyecto, los datos y los cambios de edición

Guardar tiene varios significados durante el trabajo con SIG:

| Situación | Qué debes hacer |
|---|---|
| Organizaste capas o cambiaste su representación | Guardar el **proyecto** |
| Modificaste atributos o geometrías de una capa persistente | Confirmar y guardar las **ediciones de esa capa** |
| Creaste una capa temporal en memoria | Guardarla en una **fuente persistente**, por ejemplo un GeoPackage |
| Guardaste una capa temporal en un archivo nuevo | Comprobar que el proyecto utiliza la fuente persistente y guardar el proyecto |

!!! warning "El proyecto no convierte una capa temporal en permanente"

    Una capa temporal en memoria puede perder sus entidades al cerrar la sesión. Si quieres conservarla, utiliza la opción para **hacerla permanente** o expórtala a un archivo. No dependas únicamente de guardar el QGZ.

La edición y la creación de capas se desarrollarán en el módulo 3. Por ahora, reconoce las capas temporales y distingue los controles de **guardar ediciones** del guardado del proyecto. Si QGIS pide confirmar cambios, lee a qué elemento se refiere antes de aceptar o descartar.

!!! captura "Captura pendiente · 2.3-07"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-07-temporal-persistente.png`
    - **Qué mostrar:** El indicador de una capa temporal y la acción disponible para hacerla permanente, con el destino de ejemplo `datos/trabajo/observaciones.gpkg`.

---

## Copias de respaldo y entregas

### Respaldar lo necesario

Una copia del proyecto permite recuperar su organización; una copia de los datos permite recuperar su contenido. Para proteger el trabajo completo, conserva **ambos**, junto con los recursos externos utilizados.

??? info "La copia automática de un proyecto QGS"

    El manual documenta una copia con extensión **`.qgs~`** al guardar proyectos QGS. Es un respaldo del proyecto, no de sus capas. No presupongas que existe un respaldo equivalente del QGZ ni que ese mecanismo sustituye tus copias del trabajo completo.

Antes de copiar carpetas con datos abiertos, guarda las ediciones pendientes y cierra QGIS. Evita modificar simultáneamente el mismo archivo desde varias copias de la aplicación durante este ejercicio.

### Preparar la entrega

- **Proyecto:** identifica cuál es el archivo que debe abrirse.
- **Datos:** incluye todas las fuentes locales necesarias y revisa sus permisos de uso.
- **Recursos:** incorpora imágenes y símbolos externos empleados; anota tipografías o complementos necesarios si los hubiera.
- **Servicios:** documenta cuáles requieren internet, permisos o autenticación. No incluyas contraseñas en la nota de entrega.
- **Instrucciones:** indica la versión de QGIS utilizada, el propósito del proyecto y las comprobaciones realizadas.

!!! note "Una conexión web sigue siendo una conexión web"

    Copiar la carpeta o comprimirla en ZIP no descarga un mapa base ni convierte un servicio en datos sin conexión. Distingue las capas locales imprescindibles de los recursos en línea que solo aportan contexto.

Puedes comprimir la carpeta completa para enviarla. Quien la reciba deberá **extraerla antes de abrir el proyecto**. Comprueba también la copia extraída: comprimir un trabajo incompleto no corrige sus dependencias.

??? tip "Para saber más: plantillas de proyecto"

    Una plantilla permite reutilizar una organización inicial, por ejemplo grupos y propiedades comunes. QGIS permite configurar una carpeta de plantillas en **Configuración ▸ Opciones ▸ General** y utilizarlas desde **Proyecto ▸ Nuevo a partir de plantilla**. Comprueba sus fuentes: una plantilla tampoco crea copias independientes de los datos que referencia.

---

## Reto práctico

!!! example "Reto 2.3 — Trasladar, reparar y entregar un proyecto"

    **Situación:** el equipo necesita continuar tu exploración en otra computadora. Debes entregar un proyecto que utilice sus propias copias de datos y explicar cómo resolviste un cambio de ubicación.

    **1. Preparar una copia de trabajo**

    - Guarda el proyecto de la lección 2.2 y cierra QGIS.
    - Crea `trabajo_municipio/` con la estructura propuesta. Copia allí el proyecto y la capa local necesaria, con todos sus archivos asociados. Conserva intactos los originales.
    - Abre el proyecto copiado y guárdalo como `proyectos/reto_2-3_gestion.qgz`.
    - Si hay otras capas locales, incluye también sus datos o quítalas **solo de esta copia del proyecto**. Mantén al menos una capa vectorial local.
    - Comprueba el origen de cada capa. Si todavía apunta a los datos originales externos, cambia su fuente desde **Propiedades de la capa ▸ Fuente**, seleccionando la copia correspondiente y conservando la misma capa interna si el archivo contiene varias.

    **2. Documentar y guardar**

    - Configura rutas relativas, un título comprensible y un resumen en los metadatos.
    - Conserva los grupos y marcadores del proyecto. Guarda el trabajo.
    - Anota tres controles de tu capa: número de entidades, nombres de dos campos y valor de un atributo de una entidad identificable.
    - Guarda los cambios pendientes y cierra QGIS.

    **3. Probar la portabilidad**

    - Copia **toda** `trabajo_municipio/` a otra ubicación, por ejemplo dentro de `prueba_entrega/`.
    - Abre explícitamente `prueba_entrega/trabajo_municipio/proyectos/reto_2-3_gestion.qgz`.
    - Comprueba que no faltan capas locales y que sus fuentes están dentro de `prueba_entrega/trabajo_municipio/`. Ver el mapa no basta: podría estar leyendo los archivos originales.
    - Revisa grupos, marcadores y los tres controles anotados. Cierra QGIS.

    **4. Simular una fuente trasladada y repararla**

    - Trabaja **solo en `prueba_entrega/trabajo_municipio/`**. Renombra su carpeta `datos/originales/` como `datos/originales_reubicados/`; no borres archivos.
    - Abre el proyecto de esa copia y observa qué fuente esperaba encontrar.
    - Repara el vínculo seleccionando el mismo archivo en la carpeta renombrada. Si fallan varias capas, comprueba y corrige cada una.
    - Verifica nombres, estilos, atributos y controles; guarda, cierra y vuelve a abrir.
    - Explica por qué funcionó el traslado completo del paso 3 y por qué el cambio interno del paso 4 exigió reparar rutas.

    **5. Preparar la entrega final**

    - En `LEEME.txt`, indica qué proyecto abrir, versión de QGIS, fuentes y condiciones de uso conocidas. Registra el cambio de carpeta y la reparación.
    - Si mantuviste un mapa base web, desactívalo y comprueba que la capa local sigue siendo utilizable. Describe la dependencia de internet por separado.
    - Con QGIS cerrado, comprime la carpeta reparada. Extráela en una tercera ubicación, abre su proyecto y comprueba que usa los datos de esa extracción.

    **Entregables:**

    - La carpeta reparada y comprobada, comprimida en ZIP, con proyecto, datos y `LEEME.txt`.
    - Una captura del proyecto abierto desde la entrega extraída.
    - Un breve registro con el origen comprobado de la capa, los tres controles y la explicación de la reparación.

!!! captura "Captura pendiente · 2.3-08"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-3/2-3-08-entrega-comprobada.png`
    - **Qué mostrar:** El proyecto abierto desde la entrega extraída y la información de una capa con su ruta dentro de esa carpeta. Resaltar el tramo relativo al ejercicio, ocultando información personal.

??? success "Criterios de evaluación del reto"

    | Criterio | Se cumple si... |
    |---|---|
    | Independencia | Las fuentes locales de la entrega apuntan a sus propias copias |
    | Organización | La carpeta distingue proyectos, datos, recursos y salidas |
    | Documentación | El título, resumen y LEEME permiten entender el trabajo y abrirlo |
    | Recuperación | La fuente reubicada vuelve a funcionar conservando la configuración de la capa |
    | Verificación | Coinciden los controles antes y después del traslado y la reparación |
    | Entrega | El ZIP extraído se abre sin fuentes locales ausentes y las dependencias web están identificadas |

---

## Problemas frecuentes

| Problema | Causa probable | Solución |
|---|---|---|
| Envié el QGZ y faltan capas | No se incluyeron las fuentes externas | Entrega proyecto y datos con una estructura comprobada |
| La copia funciona solo en mi equipo | Sigue apuntando a archivos fuera de la entrega | Revisa el origen de cada capa y vincula las copias internas |
| Las rutas son relativas, pero falta una capa | Cambió una carpeta interna o la fuente estaba fuera de la carpeta entregada | Localiza el mismo archivo, repara la ruta y vuelve a guardar |
| Cambié el título y el archivo conserva su nombre | Título y nombre de archivo son elementos diferentes | Usa **Guardar como** si necesitas otro nombre de archivo |
| Desaparecieron datos de una capa temporal | No se guardaron en una fuente persistente | Busca si existe una exportación guardada; para próximos trabajos, hazla permanente antes de cerrar |
| El mapa aparece tras reparar, pero los atributos no coinciden | Se eligió otra versión o capa interna | Contrasta campos, entidades y procedencia; enlaza la fuente correcta |
| El mapa base no funciona sin internet | Es un servicio remoto | Comprueba las capas locales por separado y documenta esa dependencia |

---

## Ideas clave

!!! success "Para recordar"

    - El **proyecto** organiza el trabajo; las **fuentes** contienen los datos y los **productos** comunican resultados.
    - Un **QGZ no reúne automáticamente las capas externas**.
    - **Guardar como** crea otro proyecto, pero sus datos pueden seguir siendo compartidos con el anterior.
    - Las **rutas relativas** se interpretan desde el archivo de proyecto y requieren conservar la estructura entre carpetas.
    - **Reparar una fuente** exige encontrar los datos correctos y comprobarlos, no solo lograr que aparezca un mapa.
    - El proyecto, las **ediciones de capas** y los **datos temporales** requieren decisiones de guardado diferentes.
    - Una entrega se comprueba **desde otra ubicación**, revisando las fuentes que realmente utiliza.

---

## Autoevaluación

??? question "1. Tu proyecto pesa muy poco, pero utiliza una imagen de varios cientos de megabytes. ¿Se ha comprimido toda la imagen dentro del QGZ?"

    No debes deducirlo del tamaño ni de la extensión. En el trabajo habitual, el proyecto conserva la referencia a la imagen externa. Revisa su origen e incluye el archivo si debe viajar con la entrega.

??? question "2. Guardaste una segunda versión del proyecto y editaste un atributo. ¿Por qué aparece modificado también en la primera?"

    Ambos proyectos pueden consultar la **misma fuente de datos**. Guardar como duplica la configuración del proyecto, pero no copia la capa. Para trabajar de manera independiente, necesitas una copia de los datos y comprobar que el segundo proyecto la utiliza.

??? question "3. El proyecto está en proyectos/mapa.qgz y los datos en datos/originales/limites.gpkg, bajo una misma carpeta principal. ¿Cuál es la ruta relativa?"

    `../datos/originales/limites.gpkg`: subir un nivel desde `proyectos/` y entrar en `datos/originales/`. Si trasladas la carpeta principal completa conservando esa estructura, la relación sigue siendo válida.

??? question "4. Copias una carpeta, abres su proyecto y el mapa se ve bien. ¿Qué falta comprobar?"

    El **origen de las capas**: podrían seguir leyendo archivos de la ubicación anterior. Además, comprueba atributos, marcadores, recursos externos y cualquier dependencia de servicios web.

??? question "5. Tras reparar una ruta aparece un mapa, pero falta un campo que se usaba para etiquetar. ¿Darías la reparación por terminada?"

    No. Puede haberse elegido otro conjunto de datos o una capa interna distinta. Comprueba procedencia, campos, número de entidades y extensión antes de guardar la reparación como válida.

??? question "6. ¿Qué diferencia hay entre guardar el proyecto y hacer permanente una capa temporal?"

    Guardar el proyecto conserva su configuración. Hacer permanente una capa temporal escribe sus datos en una fuente persistente. Después hay que verificar que el proyecto usa esa fuente y guardar la configuración actualizada.

---

## Referencias

- QGIS Project. *Manual de usuario 3.44: Trabajar con archivos de proyecto y gestionar rutas rotas*. [Consultar el manual](https://docs.qgis.org/3.44/es/docs/user_manual/introduction/project_files.html).
- QGIS Project. *Manual de usuario 3.44: Configuración de QGIS y propiedades del proyecto*. [Consultar propiedades y opciones](https://docs.qgis.org/3.44/es/docs/user_manual/introduction/qgis_configuration.html).
- QGIS Project. *Manual de usuario 3.44: Propiedades vectoriales, información y cambio de fuente*. [Consultar el origen de las capas](https://docs.qgis.org/3.44/en/docs/user_manual/working_with_vector/vector_properties.html#source-properties).
- QGIS Project. *Manual de usuario 3.44: Formatos de archivos de QGIS, QGS y QGZ*. [Consultar los formatos](https://docs.qgis.org/3.44/es/docs/user_manual/appendices/qgis_file_formats.html).
- QGIS Project. *Manual de usuario 3.44: Crear nuevas capas vectoriales y capas temporales*. [Consultar creación de capas](https://docs.qgis.org/3.44/es/docs/user_manual/managing_data_source/create_layers.html).
- QGIS Project. *Manual de usuario 3.44: Edición y guardado de capas*. [Consultar edición de datos](https://docs.qgis.org/3.44/es/docs/user_manual/working_with_vector/editing_geometry_attributes.html).

En la próxima lección, **2.4 Incorporar datos y reconocer sus diferencias**, utilizaremos esta organización para examinar formatos, geometrías, atributos y metadatos antes de incorporar nuevas fuentes al proyecto.
