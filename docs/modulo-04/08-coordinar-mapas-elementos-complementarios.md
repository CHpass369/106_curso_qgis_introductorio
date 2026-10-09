---
title: 4.8 Coordinar mapas y elementos complementarios
description: Coordinación de mapa principal, localizador, vistas de detalle, temas de mapa, leyendas, escalas y cuadrículas dentro de una misma composición cartográfica en QGIS.
---

# 4.8 Coordinar mapas y elementos complementarios

Un concejal que no conoce Cochabamba mira tu lámina y pregunta: «¿esto dónde queda?». Otro quiere ver de cerca el centro, donde todo se amontona. Una lámina profesional responde ambas preguntas **en la misma página**: un **localizador** que sitúa el municipio en la región y, si hace falta, un **detalle** ampliado. El reto es que los tres mapas trabajen juntos sin confundir al lector.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Agregar un **mapa de localización** con el **marco de extensión** del mapa principal.
    - Crear un **mapa de detalle** con su propio tema y escala.
    - Vincular **leyendas** y **barras de escala** al mapa correcto.
    - Agregar una **cuadrícula** de coordenadas cuando el uso lo requiere.
    - Mantener la coherencia visual entre mapas de una misma lámina.

    **Tiempo:** 75 min (20 de lectura · 55 de práctica) · **Datos:** el proyecto y la plantilla de 4.7 · **Producto:** lámina con mapa principal, localizador y detalle.

---

## Idea central

### Cada mapa, una función

| Mapa | Pregunta | Escala | Contenido mínimo |
|---|---|---|---|
| **Principal** | ¿Qué pasa? | 1:90 000 | El tema completo |
| **Localizador** | ¿Dónde queda? | 1:400 000 o menor | Municipios vecinos en gris, el municipio destacado, el marco del principal |
| **Detalle** | ¿Qué pasa aquí, de cerca? | 1:15 000 | Tema + nombres; su marco indicado en el principal |

!!! warning "Coherencia entre mapas"

    Los mismos objetos deben verse **igual** en todos los mapas (mismo color para «sin cobertura»), y cada barra de escala debe pertenecer a **su** mapa. Si el detalle tiene otra escala, márcalo con un recuadro en el principal y rotúlalo.

### Temas del mapa

Un **tema del mapa** guarda qué capas están visibles y con qué estilo. Cada mapa de la composición puede **seguir un tema** distinto, así el localizador muestra solo municipios y el detalle muestra nombres que el principal oculta ([4.2](02-preparar-informacion-escala-salida.md)).

---

## Hazlo conmigo

### Paso 1 · Temas para cada mapa

Crea tres temas en el panel Capas:

| Tema | Capas visibles |
|---|---|
| `principal` | Zonas por estado, establecimientos, comunas, vías principales, ríos |
| `localizador` | Municipios metropolitanos (gris), límite municipal (naranja) |
| `detalle_centro` | Lo de `principal` + vías secundarias y locales + etiquetas de establecimientos |

### Paso 2 · Localizador con marco de extensión

1. En la lámina de 4.7, **Añadir mapa** en el panel lateral (77 × 55 mm).
2. **Seguir tema del mapa:** `localizador`. Encuadra la región metropolitana.
3. **Vistas generales ▸ +** ▸ **Marco de mapa:** el mapa principal. Estilo: borde negro 0,6 mm sin relleno.
4. Rótulo debajo: «Localización en la región metropolitana».

!!! captura "Captura pendiente · 4.8-03"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-04/4-8/4-8-03-vista-general.png`
    - **Qué mostrar:** Las propiedades del mapa localizador con la vista general vinculada al mapa principal.

### Paso 3 · Mapa de detalle

1. Reduce un poco el panel o crea una variante A3 para tener espacio.
2. **Añadir mapa** · **Seguir tema:** `detalle_centro` · escala 1:15 000 centrada en la plaza principal.
3. En el **mapa principal**, agrega una vista general con el marco del **detalle** y una etiqueta «A».
4. Rotula el detalle: «A · Centro de la ciudad (1:15 000)».

### Paso 4 · Escalas y leyendas vinculadas

- Una barra de escala por mapa con escala distinta, vinculada a **su** mapa en **Propiedades ▸ Mapa**.
- Una sola leyenda vinculada al principal: si el detalle usa los mismos símbolos, no la dupliques.

### Paso 5 · Cuadrícula (si hace falta)

Para un uso técnico (red de salud, trabajo de campo), agrega al principal **Cuadrículas ▸ +** · intervalo 2 000 m · marcos con coordenadas UTM cada 2 km · fuente 6 pt. Para el Concejo, **no**: es ruido.

!!! captura "Captura pendiente · 4.8-06"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-04/4-8/4-8-06-cuadricula.png`
    - **Qué mostrar:** Una cuadrícula UTM de 2 km con anotaciones en el marco del mapa principal.

---

## Inténtalo tú

!!! example "Reto 4.8 · Lámina con dos mapas independientes"

    Diseña una lámina A3 horizontal con **dos mapas del mismo tamaño** lado a lado: **cobertura de salud** y **cobertura de educación** (con el criterio de 3.4 o 3.7).

    - Misma escala, misma extensión y mismo estilo de fondo, para que sean **comparables**.
    - Un único localizador para ambos.
    - Un título general que diga qué comparar y un subtítulo en cada mapa.

    Explica en tres líneas qué diferencia muestra la comparación.

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Función | Cada mapa responde una pregunta distinta y está rotulado |
| Vínculos | El localizador muestra el marco del principal; el principal, el del detalle |
| Escalas | Cada barra está vinculada a su mapa |
| Coherencia | Mismos símbolos para los mismos objetos en todos los mapas |
| Comparabilidad (reto) | Los dos mapas comparten escala, extensión y clasificación |

### Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| El marco no aparece en el localizador | Vista general no vinculada | Vincula al mapa principal |
| La barra de escala indica otra escala | Vinculada al mapa equivocado | Revisa **Mapa** en sus propiedades |
| El localizador muestra todo el proyecto | No sigue un tema | **Seguir tema del mapa** |
| Dos mapas «comparables» con clases distintas | Clasificación por mapa | Clases fijas comunes (4.4) |

---

## Comprueba lo aprendido

??? question "1. ¿Para qué sirve un mapa de localización?"

    Para situar el área del mapa principal en un contexto mayor que el lector reconozca.

??? question "2. ¿Qué es una vista general (*overview*) en el diseñador?"

    El marco que muestra, sobre un mapa, la extensión de otro mapa de la composición.

??? question "3. ¿Por qué cada mapa debe tener su propia barra de escala si las escalas difieren?"

    Porque una barra solo es válida para el mapa al que está vinculada.

??? question "4. Repaso de 4.5 · ¿Qué nivel de jerarquía tiene el localizador?"

    **Apoyo o fondo**: debe ser discreto y no competir con el mapa principal.

---

## Tu proyecto

La lámina del Concejo queda completa: principal, localizador y, si lo necesitas, detalle del área más crítica (por ejemplo, el sur de Itocta). Exporta la versión final para el taller 4.12.

---

## Referencias

- Dent, B. D., Torguson, J. S., & Hodler, T. W. (2009). *Cartography: Thematic Map Design* (6.ª ed.). McGraw-Hill.
- Peterson, G. N. (2020). *GIS Cartography* (3.ª ed.). CRC Press.
- QGIS Project. (s. f.). *Manual de usuario: El elemento mapa (vistas generales y cuadrículas)*. <https://docs.qgis.org/latest/es/docs/user_manual/print_composer/composer_items/composer_map.html>
