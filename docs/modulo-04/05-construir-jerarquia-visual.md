---
title: 4.5 Construir una jerarquía visual
description: Uso de figura y fondo, contraste, tamaño, grosor, transparencia, orden de dibujo, simbología por reglas y estilos reutilizables para construir jerarquía cartográfica en QGIS.
---

# 4.5 Construir una jerarquía visual

Los dos mapas de abajo tienen **exactamente las mismas capas**. En el de la izquierda, todo grita a la vez: zonas verdes, moradas y amarillas con bordes negros, vías rojas, ríos cian, puntos naranjas. En el de la derecha, en dos segundos ves lo importante: **las zonas naranjas son las que no tienen cobertura**. La diferencia no es el «gusto»: es la **jerarquía visual**, el orden en que el ojo lee el mapa.

![Antes y después: mismas capas, distinta jerarquía visual](../assets/images/mapas/4-5-jerarquia-antes-despues.png){ loading=lazy }

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Separar **figura** (tema) de **fondo** (contexto).
    - Usar contraste de **valor**, **saturación**, **tamaño** y **grosor** para ordenar la lectura.
    - Controlar el **orden de dibujo** y la **transparencia**.
    - Aplicar **niveles de jerarquía** con estilos reutilizables.

    **Tiempo:** 75 min (20 de lectura · 55 de práctica) · **Datos:** zonas con estado de cobertura (3.7), comunas, vías, ríos, establecimientos · **Producto:** estilos `.qml` de tres niveles para la lámina del Concejo.

---

## Idea central

### Tres niveles de lectura

| Nivel | Qué es | En el caso | Cómo se logra |
|---|---|---|---|
| **1 · Figura** | El mensaje | Zonas sin cobertura | Color saturado, contraste alto |
| **2 · Apoyo** | Lo que explica la figura | Establecimientos de salud, comunas | Color oscuro neutro, tamaño medio |
| **3 · Fondo** | Orientación | Vías principales, ríos, resto de zonas | Grises, líneas finas, transparencia |

!!! tip "La regla del entrecerrar"

    Entrecierra los ojos (o desenfoca la imagen): lo que todavía ves es tu nivel 1. Si ves «todo» o «nada», la jerarquía falló.

### Herramientas de contraste

| Variable | Más jerarquía | Menos jerarquía |
|---|---|---|
| **Valor** (luminosidad) | Oscuro sobre claro | Gris medio |
| **Saturación** | Color puro | Color apagado o gris |
| **Tamaño / grosor** | Grande, grueso | Pequeño, fino |
| **Borde** | Definido | Sin borde o blanco |
| **Opacidad** | Opaco | Transparente |
| **Orden** | Arriba | Abajo |

!!! warning "Un solo color fuerte"

    Si dos capas usan colores saturados, compiten. Reserva **un** color de acento para la figura y construye el resto con grises y un color neutro oscuro.

---

## Hazlo conmigo

### Paso 1 · Empezar en gris

Pon **todas** las capas en grises (zonas gris claro sin borde, vías gris medio 0,3 mm, ríos gris azulado 0,4 mm, comunas con borde gris oscuro sin relleno). Un mapa en gris es la mejor base: ahora todo es fondo.

### Paso 2 · Levantar la figura

1. Zonas ▸ **Categorizado** por `estado`.
2. `no_cubierta`: naranja saturado (`#ea580c`), borde blanco 0,2 mm.
3. `cubierta`: gris claro (`#e5e7eb`). `sin_poblacion`: casi blanco.

### Paso 3 · Ajustar el apoyo

1. Establecimientos de salud: círculo azul oscuro (`#1e3a8a`) 1,6 mm con borde blanco. **No** rojo: competiría con el naranja.
2. Comunas: borde gris oscuro 0,5 mm y etiqueta en mayúsculas espaciadas, gris.

### Paso 4 · Hundir el fondo

1. Vías: solo troncales y principales ([4.2](02-preparar-informacion-escala-salida.md)), gris `#9ca3af`, 0,35 mm.
2. Ríos: solo `tipo = 'rio'`, azul muy claro.
3. **Orden de dibujo**: establecimientos ▸ comunas ▸ ríos ▸ vías ▸ zonas.

!!! captura "Captura pendiente · 4.5-05"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-04/4-5/4-5-05-jerarquia-paso-a-paso.gif`
    - **Qué mostrar:** Partir de un mapa todo en gris y levantar progresivamente la figura y el apoyo.

### Paso 5 · Efectos con moderación

- **Transparencia** de capa (Propiedades ▸ Simbología ▸ Representación de capa) para el sombreado o el mapa base.
- **Modo de mezcla** *Multiplicar* para combinar un sombreado con colores sin apagarlos.
- **Efectos de dibujo** (sombra, resplandor exterior): solo si ayudan a separar figura y fondo, nunca como decoración.

### Paso 6 · Guardar los niveles

Guarda los estilos como `estilos/jerarquia_figura_zonas.qml`, `estilos/jerarquia_apoyo_salud.qml` y `estilos/jerarquia_fondo_vias.qml`. Los reutilizarás en la composición y en el atlas.

---

## Inténtalo tú

!!! example "Reto 4.5 · Tres niveles de jerarquía para el brief B"

    El atlas de la red de salud (brief B) tiene otro mensaje: «estas son las zonas sin cobertura **de tu comuna**». Diseña la jerarquía:

    1. ¿Qué pasa con las comunas vecinas? (Pista: deben estar presentes pero «apagadas».)
    2. ¿Qué nivel tienen los nombres de los establecimientos?
    3. ¿Cómo distingues la comuna del atlas del resto?

    Aplica tu diseño, haz la **prueba de entrecerrar los ojos** y explica qué cambiaste respecto de la lámina del Concejo.

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Figura | El mensaje se identifica en 2 segundos (prueba con otra persona) |
| Acento | Un solo color saturado en todo el mapa |
| Fondo | Vías y ríos orientan sin competir |
| Orden | Puntos sobre líneas sobre polígonos |
| Reutilización | Tres estilos `.qml` guardados y aplicables |

### Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| «No sé dónde mirar» | Varios colores saturados | Un acento, el resto en grises |
| El tema «desaparece» bajo las vías | Orden de dibujo incorrecto o vías demasiado gruesas | Reordenar; adelgazar el fondo |
| Mapa «sucio» | Bordes negros en todos los polígonos | Bordes blancos o sin borde |
| Rojo y verde juntos | Paleta no accesible | Naranja/azul, o variar la luminosidad |

---

## Comprueba lo aprendido

??? question "1. ¿Qué es la figura en un mapa temático?"

    El elemento que transmite el **mensaje**; debe destacar sobre el resto.

??? question "2. ¿Por qué empezar diseñando todo en gris?"

    Porque así todo es fondo, y puedes **levantar** con intención solo lo importante.

??? question "3. ¿Por qué los establecimientos son azules y no rojos en la lámina?"

    Porque el rojo competiría con el naranja de la figura; el azul oscuro apoya sin competir.

??? question "4. Repaso de 1.7 · ¿Qué variable visual es más efectiva para ordenar niveles?"

    El **valor** (luminosidad) y el **tamaño**.

---

## Tu proyecto

Aplica la jerarquía a la lámina del Concejo y somételo a la prueba de los 30 segundos de [4.1](01-definir-encargo-cartografico.md). Anota qué entendió tu lector de prueba.

---

## Referencias

- Dent, B. D., Torguson, J. S., & Hodler, T. W. (2009). *Cartography: Thematic Map Design* (6.ª ed., cap. sobre jerarquía visual). McGraw-Hill.
- MacEachren, A. M. (1995). *How Maps Work: Representation, Visualization, and Design*. Guilford Press.
- Brewer, C. A. (2016). *Designing Better Maps* (2.ª ed.). Esri Press.
- QGIS Project. (s. f.). *Manual de usuario: Representación de capa y modos de mezcla*. <https://docs.qgis.org/latest/es/docs/user_manual/working_with_vector/vector_properties.html#layer-rendering>
