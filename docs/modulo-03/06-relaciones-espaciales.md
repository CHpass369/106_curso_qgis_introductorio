---
title: 3.6 Traducir preguntas en relaciones espaciales
description: Resolución de preguntas territoriales mediante predicados espaciales, selección por ubicación, conteos, uniones y resúmenes por zona en QGIS.
---

# 3.6 Traducir preguntas en relaciones espaciales

¿Cuántos establecimientos de salud hay en cada comuna? La respuesta revela una desigualdad enorme: **113** en Adela Zamudio y **10** en Alejo Calatayud, con casi la misma población. Es decir, unos **1 100 habitantes por establecimiento** frente a más de **11 000**. Para llegar a ese número no hace falta ninguna tabla nueva: basta con preguntar al SIG **qué está dentro de qué**. Esta lección te enseña a traducir preguntas como esa en **relaciones espaciales**.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Traducir preguntas territoriales en **predicados espaciales** (interseca, contiene, está dentro, toca…).
    - Usar **Seleccionar por localización** y **Contar puntos en polígono**.
    - Transferir atributos con **Unir atributos por localización** y resumirlos con **…(resumen)**.
    - Manejar los casos difíciles: entidades sobre el límite, coincidencias múltiples y entidades sin pareja.

    **Tiempo:** 2 h (30 min de lectura · 90 de práctica) · **Datos:** `comunas`, `zonas_analisis`, `equipamientos` auditado · **Producto:** `datos/trabajo/relaciones.gpkg` con conteos por comuna y comuna asignada a cada establecimiento.

---

## Idea central

### De la pregunta al predicado

| Pregunta | Predicado | En QGIS |
|---|---|---|
| ¿Qué establecimientos están **en** la comuna X? | **está dentro** (*within*) | Seleccionar por localización |
| ¿Qué comunas **contienen** un hospital? | **contiene** (*contains*) | Seleccionar por localización |
| ¿Qué vías **cruzan** el río Rocha? | **cruza** (*crosses*) | Seleccionar por localización |
| ¿Qué comunas **limitan** con Tunari? | **toca** (*touches*) | Seleccionar por localización |
| ¿Qué zonas **tienen algo que ver** con la comuna? | **interseca** (*intersects*) | El más amplio |
| ¿Cuántos establecimientos hay **por** comuna? | contiene + **conteo** | Contar puntos en polígono |
| ¿En qué comuna está **cada** establecimiento? | está dentro + **transferencia** | Unir atributos por localización |

!!! captura "Captura pendiente · 3.6-01"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-03/3-6/3-6-01-predicados.png`
    - **Qué mostrar:** Diagrama de los predicados espaciales con ejemplos de comunas, zonas, vías y establecimientos de Cochabamba.

!!! tip "Predice antes de ejecutar"

    Antes de pulsar **Ejecutar**, escribe cuántas entidades esperas. Si el resultado se aleja mucho de tu predicción, revisa el predicado, el orden de las capas o los SRC.

### Los casos difíciles

| Caso | Ejemplo | Qué hacer |
|---|---|---|
| **Sobre el límite** | Un punto exactamente en el borde entre dos comunas | *Interseca* lo cuenta en ambas; *está dentro*, en ninguna |
| **Coincidencias múltiples** | Una zona que cruza dos comunas | Decide: ¿primera coincidencia, la de mayor superposición o todas? |
| **Sin pareja** | Un establecimiento fuera de toda comuna | Debe quedar **visible**, no desaparecer |
| **Centroide engañoso** | El centroide de una zona en forma de «C» cae fuera de ella | Usa **punto en la superficie** (`point_on_surface`) |

!!! danger "Un conteo no es una cobertura"

    Que Molle tenga 15 establecimientos de salud **dentro** no significa que sus habitantes estén bien atendidos: pueden estar todos en una esquina, o puede haber muchos justo al otro lado del límite. La **proximidad** se estudia en [3.7](07-proximidad-superposicion.md).

---

## Hazlo conmigo

### Paso 1 · Seleccionar por localización

1. **Procesos ▸ Seleccionar por localización** (o **Vectorial ▸ Herramientas de investigación**).
2. **Seleccionar objetos de:** `equipamientos` · **donde los objetos:** *están dentro* · **comparando con:** `Comunas` con **solo los objetos seleccionados** (selecciona antes Alejo Calatayud).
3. Predicción: ¿cuántos? Resultado: **62** (10 de salud, 52 de educación).

!!! captura "Captura pendiente · 3.6-03"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-6/3-6-03-seleccionar-localizacion.gif`
    - **Qué mostrar:** Seleccionar una comuna, ejecutar Seleccionar por localización con el predicado está dentro y ver los establecimientos seleccionados.

### Paso 2 · Contar por comuna

1. **Procesos ▸ Contar puntos en polígono** · **Polígonos:** `Comunas` · **Puntos:** `equipamientos` filtrados a `"tipo" = 'salud'` · **Campo de conteo:** `n_salud`.
2. Repite con educación (`n_educacion`).
3. Une la población (lección [3.5](05-integrar-tablas.md)) y calcula `hab_por_salud`.

Deberías obtener:

| Comuna | Población 2020 | Salud | Educación | Hab. por establecimiento de salud |
|---|---|---|---|---|
| Adela Zamudio | 123 184 | 113 | 254 | 1 090 |
| Alejo Calatayud | 113 777 | 10 | 52 | 11 378 |
| Itocta | 120 331 | 12 | 42 | 10 028 |
| Molle | 90 750 | 15 | 58 | 6 050 |
| Tunari | 91 696 | 8 | 31 | 11 462 |
| Valle Hermoso | 62 459 | 15 | 51 | 4 164 |
| **Total** | **602 197** | **173** | **488** | **3 481** |

!!! captura "Captura pendiente · 3.6-05"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-03/3-6/3-6-05-contar-puntos.png`
    - **Qué mostrar:** El algoritmo Contar puntos en polígono con sus parámetros y la tabla resultante por comuna.

### Paso 3 · Asignar a cada establecimiento su comuna

1. **Procesos ▸ Unir atributos por localización** · **Capa base:** `equipamientos` · **Unir con:** `Comunas` · **Predicado:** *interseca* · **Campos a añadir:** `cod_comuna`, `nombre` · **Tipo:** *uno a uno (primera coincidencia)*.
2. Marca **Descartar registros que no se pudieron unir** ▸ **No**, y guarda los no unidos aparte.
3. Comprueba: 661 establecimientos con comuna y **0** sin pareja.

!!! captura "Captura pendiente · 3.6-07"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-6/3-6-07-unir-localizacion.gif`
    - **Qué mostrar:** Unir atributos por localización con la salida de registros no unidos.

### Paso 4 · Resumir valores de otra capa

**Unir atributos por localización (resumen)** calcula estadísticas de las entidades que coinciden. Por ejemplo, población de las zonas por comuna:

- **Capa base:** `Comunas` · **Unir con:** `zonas_analisis` · **Predicado:** *contiene*
- **Campos a resumir:** `pob_2020` · **Resúmenes:** *suma*, *máximo*

¿Coincide la suma con la de la relación de [3.5](05-integrar-tablas.md)? Si eliges *interseca* en lugar de *contiene*, las zonas que tocan dos comunas se suman **dos veces**: compruébalo.

### Paso 5 · Casos límite

1. Crea una **zona de revisión** a lo largo de los límites:
    - **Procesos ▸ Contorno** (*Boundary*) sobre `Comunas`: convierte los polígonos en líneas de borde.
    - **Procesos ▸ Buffer** de 20 m sobre esas líneas.
    - **Seleccionar por localización**: `equipamientos` que *están dentro* de la zona de revisión.

    Son los registros cuya comuna depende de unos pocos metros: un error de posición de 20 m podría cambiarlos de comuna.

2. Revisa visualmente esos casos y documenta cómo los asignaste.

---

## Inténtalo tú

!!! example "Reto 3.6 · Matriz pregunta → predicado → resultado"

    Responde con herramientas de relaciones espaciales y completa la matriz en `documentos/relaciones_3-6.md`:

    | Pregunta | Predicado | Herramienta | Predicción | Resultado |
    |---|---|---|---|---|
    | ¿Qué comunas limitan con Tunari? | | | | |
    | ¿Cuántas zonas de análisis **cruzan** el límite entre dos comunas? | | | | |
    | ¿Cuántas vías principales cruzan algún río? | | | | |
    | ¿Cuántas escuelas hay en cada zona de prioridad alta (3.4)? | | | | |
    | ¿Qué zonas habitadas no contienen **ningún** establecimiento de educación? | | | | |

    Para la última pregunta, haz un mapa y compáralo con el de salud: ¿coinciden las zonas desatendidas?

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Predicados | Cada pregunta usa el predicado correcto, justificado |
| Conteos | La tabla por comuna coincide con la del paso 2 |
| Asignación | 661 establecimientos con comuna; ninguno perdido |
| Resúmenes | Distingues *contiene* de *interseca* y explicas la diferencia en la suma |
| Casos límite | Identificaste y documentaste los registros sobre los bordes |

### Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| Conteos duplicados | *Interseca* con polígonos que se tocan | Usa *contiene* o *está dentro* |
| Faltan entidades en el resultado | Se descartaron las no unidas | Guarda los no unidos y revísalos |
| Resultado vacío | SRC distintos sin reproyectar, o capas invertidas | Revisa el orden «seleccionar de… comparando con…» |
| Una zona aparece en dos comunas | Coincidencia múltiple | Elige *mayor superposición* |
| Muy lento | Sin índice espacial | **Procesos ▸ Crear índice espacial** |

---

## Comprueba lo aprendido

??? question "1. ¿Qué diferencia hay entre *interseca* y *está dentro*?"

    *Interseca* es verdadero si comparten **cualquier** punto (incluido el borde); *está dentro* exige que toda la geometría esté en el interior de la otra.

??? question "2. Un punto cae exactamente sobre el límite entre dos comunas. ¿En cuál lo cuenta cada predicado?"

    *Interseca*: en **ambas**. *Está dentro*: en **ninguna**. Hay que decidir una regla y documentarla.

??? question "3. ¿Por qué el centroide no siempre representa pertenencia?"

    Porque en polígonos cóncavos o con forma de «C» el centroide puede caer **fuera**. `point_on_surface` garantiza un punto interior.

??? question "4. ¿Qué te dice el indicador «habitantes por establecimiento» por comuna y qué no?"

    Muestra la **desigualdad de oferta** entre comunas; no dice si la población está **cerca** de los servicios ni qué tamaño tienen.

??? question "5. Repaso de 1.2 · ¿Qué es una relación espacial topológica?"

    Una relación que se mantiene aunque deformes el espacio sin romperlo: contención, adyacencia, intersección. No depende de distancias.

---

## Tu proyecto

La tabla por comuna es tu primer **resultado cuantitativo** del caso conductor. Escribe un párrafo que la interprete con cuidado: qué muestra, qué no muestra y qué limitaciones de los datos podrían cambiarla (omisiones de OSM, población modelada, establecimientos privados frente a públicos).

---

## Referencias

- Egenhofer, M. J., & Herring, J. (1990). *Categorizing binary topological relations between regions, lines, and points in geographic databases* (Technical report). University of Maine.
- Clementini, E., Di Felice, P., & van Oosterom, P. (1993). A small set of formal topological relationships suitable for end-user interaction. En D. Abel & B. C. Ooi (Eds.), *Advances in Spatial Databases* (pp. 277–295). Springer. <https://doi.org/10.1007/3-540-56869-7_16>
- Open Geospatial Consortium. (2011). *OpenGIS Implementation Standard for Geographic information — Simple feature access — Part 1: Common architecture* (OGC 06-103r4). <https://www.ogc.org/standards/sfa>
- QGIS Project. (s. f.). *Algoritmos de Procesos: Selección y unión por localización*. <https://docs.qgis.org/latest/es/docs/user_manual/processing_algs/qgis/vectorselection.html>
