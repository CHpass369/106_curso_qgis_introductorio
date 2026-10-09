---
title: 3.2 Digitalizar y editar con precisión
description: Creación y edición precisa de geometrías vectoriales mediante vértices, autoensamblado, rastreo, digitalización avanzada, división, combinación y control topológico en QGIS.
---

# 3.2 Digitalizar y editar con precisión

El municipio quiere dividir la comuna Alejo Calatayud en **sectores de atención de salud** que no se superpongan ni dejen huecos: cada vivienda debe pertenecer a un sector y solo a uno. Dibujar polígonos es fácil; dibujarlos **para que encajen exactamente** es otra cosa. Un vértice a 30 cm del vecino crea una franja de nadie que nadie ve en pantalla y que arruina cualquier conteo posterior.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Preparar una sesión de edición en una capa GeoPackage.
    - Crear y modificar puntos, líneas y polígonos con el **editor de vértices**.
    - Usar **autoensamblado**, **rastreo** y **evitar superposiciones** para compartir límites.
    - Dibujar con medidas exactas mediante **digitalización avanzada**.
    - Dividir, combinar y remodelar entidades.
    - Comprobar **validez** y **topología** al terminar.

    **Tiempo:** 2 h (30 min de lectura · 90 de práctica) · **Datos:** `limites.gpkg`, `vias.gpkg`, `sentinel2_2025-07-16.tif`, mapa base OSM · **Producto:** `datos/trabajo/digitalizacion.gpkg` con `sectores_salud` y `areas_verdes`.

---

## Idea central

### Digitalizar es interpretar

Cada vértice es una **decisión**: dónde termina un parque, por dónde pasa un límite. La calidad depende de la **referencia** (imagen de 10 m o mapa base), de la **escala de trabajo** y de las **reglas** que sigas.

| Concepto | En digitalización significa |
|---|---|
| **Precisión** | Qué tan finos son tus vértices (¿a 0,1 m o a 5 m?) |
| **Exactitud** | Qué tan cerca están del límite real |
| **Nivel de detalle** | Cuántos vértices necesitas para la escala de uso |

!!! warning "No digitalices más fino que tu referencia"

    Sobre Sentinel-2 (10 m), una precisión de centímetros es **falsa precisión** ([1.9](../modulo-01/09-escala-resolucion-precision.md)). Trabaja a una escala de 1:5 000 a 1:10 000 y documenta la referencia usada.

### Dos polígonos «vecinos» pueden no tocarse

| Problema | Qué es | Consecuencia |
|---|---|---|
| **Hueco** (*gap*) | Espacio sin polígono entre dos vecinos | Viviendas que no pertenecen a ningún sector |
| **Solapamiento** (*overlap*) | Área cubierta por dos polígonos | Viviendas contadas dos veces |
| **Vértice casi coincidente** | Dos vértices a centímetros | Huecos y solapamientos microscópicos |

Las herramientas que lo evitan:

| Herramienta | Qué hace | Dónde |
|---|---|---|
| **Autoensamblado** (*snapping*) | Atrae el cursor a vértices o segmentos cercanos | Barra **Autoensamblado** (imán) |
| **Rastreo** (*tracing*) | Sigue automáticamente el borde de otra geometría | ++t++ con autoensamblado activo |
| **Evitar superposición** | Recorta lo nuevo contra lo existente | Opciones avanzadas de autoensamblado |
| **Edición topológica** | Mover un vértice compartido mueve ambos polígonos | Botón de edición topológica |

### Validez no es topología

- **Validez**: cada geometría está bien formada (anillos cerrados, sin autointersecciones). Se comprueba con **Comprobar validez**.
- **Topología**: las geometrías se relacionan como deben (sin huecos ni solapamientos entre vecinos). Se comprueba con el **Comprobador de topología** o con reglas de Procesos.

---

## Hazlo conmigo

### Paso 1 · Preparar la sesión

1. **Capa ▸ Crear capa ▸ Nueva capa GeoPackage…** ▸ archivo `datos/trabajo/digitalizacion.gpkg` · capa `sectores_salud` · **Polígono** · **EPSG:32719** · campos `id_sector` (texto) y `nombre` (texto).
2. Crea en el mismo archivo `areas_verdes` (polígono) con `nombre` y `tipo`.
3. Agrega como referencia: `Comunas` (filtro `"cod_comuna" = 'C02'`), `vias.gpkg` y el mapa base OSM.
4. Configura **Proyecto ▸ Opciones de autoensamblado**: capas `sectores_salud`, `Comunas` y `vías` · tipo **Vértice y segmento** · tolerancia **10 px**.
5. Activa **Evitar superposición** en `sectores_salud`.

!!! captura "Captura pendiente · 3.2-05"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-03/3-2/3-2-05-autoensamblado.png`
    - **Qué mostrar:** Configuración avanzada de autoensamblado con capas, tipo, tolerancia y la opción Evitar superposición.

!!! tip "Tolerancia en píxeles o en metros"

    En **píxeles**, la atracción es la misma a cualquier escala de pantalla; en **unidades del mapa** (metros) es fija en el terreno. Para digitalizar a escalas variables, usa píxeles.

### Paso 2 · Primer sector siguiendo límites existentes

1. Activa la edición (++ctrl+e++) y **Añadir polígono** (++ctrl+period++).
2. Haz clic en un vértice del límite de la comuna, presiona ++t++ (rastreo) y haz clic más adelante: el borde se copia exactamente.
3. Cierra el sector siguiendo una **vía principal** como límite interno (también con rastreo).
4. Clic derecho para terminar; completa `id_sector = S01`.

!!! captura "Captura pendiente · 3.2-09"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-2/3-2-09-rastreo.gif`
    - **Qué mostrar:** Crear un polígono nuevo reutilizando el borde de la comuna y una vía mediante rastreo.

### Paso 3 · Sector vecino sin huecos ni solapamientos

1. Dibuja `S02` **pasándote** a propósito sobre `S01`.
2. Al cerrarlo, **Evitar superposición** recorta automáticamente la parte que invadía `S01`: el límite compartido queda idéntico.
3. Repite hasta cubrir la comuna con 4 sectores.

!!! captura "Captura pendiente · 3.2-11"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-2/3-2-11-evitar-superposicion.gif`
    - **Qué mostrar:** Creación de un polígono superpuesto y su ajuste automático al vecino.

### Paso 4 · Medidas exactas con digitalización avanzada

Las áreas verdes de un proyecto municipal suelen tener dimensiones de plano. Dibuja una plaza de **80 × 60 m**:

1. Abre el panel **Digitalización avanzada** (botón de escuadra).
2. Haz clic en el primer vértice; escribe ++d++ `80` ++enter++ y ++a++ `0` ++enter++ para el primer lado.
3. Continúa con `d 60` y ángulo relativo `90`, etc.

!!! captura "Captura pendiente · 3.2-07"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-03/3-2/3-2-07-digitalizacion-avanzada.png`
    - **Qué mostrar:** Panel de Digitalización avanzada con distancia y ángulo bloqueados durante la captura.

### Paso 5 · Editar: vértices, dividir, combinar, remodelar

| Necesitas… | Herramienta |
|---|---|
| Mover, agregar o borrar vértices | **Herramienta de vértices** (doble clic en un segmento agrega uno; ++delete++ borra) |
| Partir un sector en dos | **Dividir objetos espaciales** (dibuja una línea que lo atraviese) |
| Unir dos sectores | Selecciónalos ▸ **Combinar objetos espaciales seleccionados** (elige los atributos que quedan) |
| Corregir un tramo del borde | **Remodelar objetos espaciales** |
| Mover un límite compartido | Activa **Edición topológica** y mueve el vértice |

!!! captura "Captura pendiente · 3.2-10"

    - **Tipo:** GIF comparativo
    - **Archivo:** `assets/images/modulo-03/3-2/3-2-10-edicion-topologica.gif`
    - **Qué mostrar:** Mover un vértice compartido sin y con edición topológica: en el primer caso se abre un hueco; en el segundo ambos polígonos se ajustan.

Guarda las ediciones (++ctrl+s++ sobre la capa) cada vez que completes un sector.

### Paso 6 · Controlar validez y topología

1. **Procesos ▸ Comprobar validez** sobre `sectores_salud`: todas deben salir en la salida **válida**.
2. **Vectorial ▸ Comprobador de topología** (complemento del núcleo; actívalo si no aparece) ▸ reglas:
    - `sectores_salud` **no debe tener solapamientos**.
    - `sectores_salud` **no debe tener huecos**.
3. Corrige lo que aparezca y vuelve a validar.

!!! note "Si no encuentras el Comprobador de topología"

    En la caja de **Procesos**, busca *huecos* y *solapamientos*: los algoritmos de **Comprobar geometría** detectan ambos problemas y generan una capa de errores.

!!! captura "Captura pendiente · 3.2-17"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-2/3-2-17-topologia.gif`
    - **Qué mostrar:** Configurar reglas en el Comprobador de topología, ejecutarlo y localizar un hueco.

??? info "Para saber más · comprobar la cobertura total"

    Calcula la suma de las áreas de los sectores (`sum($area)`) y compárala con el área de la comuna Alejo Calatayud (35,34 km²). Si difieren más de unos m², hay huecos o partes fuera de la comuna.

---

## Inténtalo tú

!!! example "Reto 3.2 · Áreas verdes de una zona sin cobertura"

    Elige una de las zonas de análisis **habitadas y sin establecimiento de salud cercano** que intuiste en [2.9](../modulo-02/09-simbologia-etiquetas.md). Sobre la imagen Sentinel-2 en **falso color** ([2.10](../modulo-02/10-explorar-raster.md)) y el mapa base:

    1. Digitaliza **todas las áreas verdes públicas** (parques, plazas, riberas) de esa zona en `areas_verdes`.
    2. Usa autoensamblado para que ninguna área invada una vía.
    3. Registra en `tipo`: `plaza`, `parque` o `ribera`.
    4. Calcula la superficie verde por habitante de la zona: `sum($area) / pob_2020`.

    **Entregable:** las capas editadas, la validación sin errores y una captura del resultado sobre la imagen.

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Cobertura | Los sectores cubren la comuna sin huecos ni solapamientos (Comprobador de topología sin errores) |
| Precisión adecuada | Escala de trabajo y referencia documentadas; sin vértices innecesarios |
| Validez | Todas las geometrías válidas |
| Atributos | `id_sector` único; `tipo` con valores del dominio |
| Trazabilidad | En los metadatos de la capa constan la referencia, la escala y la fecha |

### Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| El cursor no «se pega» | Autoensamblado apagado o capa no incluida | Revisa la barra de autoensamblado |
| Se pega a todo y no puedo dibujar | Tolerancia demasiado alta | Bájala a 5–10 px |
| Aparece una franja entre sectores | Dibujaste el borde a mano dos veces | Usa rastreo o evitar superposición |
| «Geometría no válida» | El borde se cruza a sí mismo | Corrige con la herramienta de vértices o **Corregir geometrías** |
| Mover un límite abrió un hueco | Edición topológica desactivada | Actívala antes de mover vértices compartidos |

---

## Comprueba lo aprendido

??? question "1. ¿Qué diferencia hay entre autoensamblado y rastreo?"

    El autoensamblado **atrae un vértice** a otro elemento; el rastreo **sigue todo un tramo** del borde existente con un solo clic.

??? question "2. ¿Por qué una geometría válida puede tener problemas topológicos?"

    Porque la validez se evalúa en **cada** geometría; la topología, en la **relación** entre geometrías.

??? question "3. ¿Qué herramienta usas para partir un polígono en dos?"

    **Dividir objetos espaciales**.

??? question "4. ¿Por qué no conviene digitalizar a 1:500 sobre una imagen de 10 m?"

    Porque crearías vértices más precisos que la información de la referencia: falsa precisión.

??? question "5. Repaso de 1.12 · ¿Qué regla topológica garantiza que cada vivienda pertenezca a un solo sector?"

    Que los sectores **no se superpongan** y **no dejen huecos** dentro del área a cubrir: una **partición** completa del territorio.

---

## Tu proyecto

Guarda tus áreas verdes: en [3.12](12-laboratorio-decision-territorial.md) podrás usarlas como criterio adicional para proponer dónde ubicar un nuevo centro de salud.

---

## Referencias

- Longley, P. A., Goodchild, M. F., Maguire, D. J., & Rhind, D. W. (2015). *Geographic Information Science and Systems* (4.ª ed., cap. 8: Data collection). Wiley.
- Theobald, D. M. (2001). Topology revisited: Representing spatial relations. *International Journal of Geographical Information Science, 15*(8), 689–705. <https://doi.org/10.1080/13658810110074519>
- QGIS Project. (s. f.). *Manual de usuario: Edición*. <https://docs.qgis.org/latest/es/docs/user_manual/working_with_vector/editing_geometry_attributes.html>
- QGIS Project. (s. f.). *Manual de usuario: Complemento Comprobador de topología*. <https://docs.qgis.org/latest/es/docs/user_manual/plugins/core_plugins/plugins_topology_checker.html>
