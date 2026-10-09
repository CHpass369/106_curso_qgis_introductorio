---
title: 4.6 Resolver el etiquetado de mapas complejos
description: Configuración avanzada de etiquetas mediante expresiones, prioridades, obstáculos, escalas, máscaras, llamadas y revisión de etiquetas no colocadas en QGIS.
---

# 4.6 Resolver el etiquetado de mapas complejos

En el centro de Cochabamba hay más de 200 establecimientos en un par de kilómetros cuadrados. Si etiquetas todos, el mapa se convierte en sopa de letras; si QGIS decide solo, oculta justo el hospital que necesitabas nombrar. Un buen etiquetado **elige qué nombrar**, **dónde ponerlo** y **qué sacrificar**, con reglas explícitas.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Construir etiquetas con **expresiones** (texto combinado, formato condicional).
    - Usar **reglas** para etiquetar distinto cada tipo de entidad.
    - Controlar **prioridad**, **obstáculos** y **colocación**.
    - Usar **máscaras** y **llamadas** (*callouts*) para despejar zonas densas.
    - Revisar las **etiquetas no colocadas** antes de exportar.

    **Tiempo:** 90 min (25 de lectura · 65 de práctica) · **Datos:** equipamientos, comunas, vías, ríos · **Producto:** etiquetado del centro a 1:10 000 y de la lámina municipal.

---

## Idea central

### Jerarquía tipográfica

| Elemento | Tamaño | Estilo | Por qué |
|---|---|---|---|
| Comunas | 9–11 pt | MAYÚSCULAS, espaciado amplio, gris | Áreas extensas: nombre «repartido» |
| Hospitales | 8 pt | Negrita, color del símbolo | Prioridad alta |
| Otros establecimientos | 7 pt | Normal | Solo de cerca |
| Ríos | 7–8 pt | *Cursiva*, azul, siguiendo la línea | Convención hidrográfica |
| Vías | 6,5–7 pt | Normal, sobre la línea | Solo las principales |

### Reglas del buen etiquetado

1. **No todo se etiqueta.** Elige según el mensaje (brief) y la escala.
2. **La etiqueta pertenece claramente a su objeto**: arriba a la derecha del punto es la posición preferida.
3. **Las etiquetas no tapan la figura**: usa obstáculos.
4. **Ninguna etiqueta importante queda sin colocar**: revísalo.

### Herramientas clave de QGIS

| Problema | Herramienta | Dónde |
|---|---|---|
| Etiquetar distinto según el tipo | **Etiquetas basadas en reglas** | Propiedades ▸ Etiquetas |
| El hospital debe ganar el espacio | **Prioridad** (0–10) | Etiquetas ▸ Representación |
| Las etiquetas tapan las zonas sin cobertura | **Obstáculo** | Etiquetas ▸ Representación (en la capa obstáculo) |
| Texto ilegible sobre vías | **Búfer** o **máscara** | Etiquetas ▸ Búfer / Máscaras |
| Demasiados puntos juntos | **Llamada** (*callout*) | Etiquetas ▸ Llamadas |
| ¿Qué etiquetas no entraron? | **Mostrar etiquetas no colocadas** | Barra de etiquetado |

---

## Hazlo conmigo

### Paso 1 · Expresiones de etiqueta

En los equipamientos de salud, usa esta expresión:

```sql
CASE
  WHEN "subtipo" = 'hospital' THEN upper("nombre")
  ELSE "nombre"
END
```

Y, para omitir los que no tienen nombre, en **Representación ▸ Mostrar etiqueta** (definido por datos): `"nombre" IS NOT NULL`.

### Paso 2 · Reglas por tipo

**Etiquetas basadas en reglas**:

| Regla | Formato | Escala visible | Prioridad |
|---|---|---|---|
| `"subtipo" = 'hospital'` | 8 pt negrita, rojo oscuro | Hasta 1:50 000 | 10 |
| `"subtipo" = 'clinica'` | 7 pt | Hasta 1:15 000 | 6 |
| `"tipo" = 'educacion' AND "subtipo" = 'universidad'` | 7 pt, azul oscuro | Hasta 1:25 000 | 7 |
| Resto | 6,5 pt | Hasta 1:8 000 | 3 |

!!! captura "Captura pendiente · 4.6-03"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-04/4-6/4-6-03-reglas-etiquetas.png`
    - **Qué mostrar:** El panel de etiquetas basadas en reglas con cuatro reglas, sus escalas y prioridades.

### Paso 3 · Obstáculos y colocación

1. En la capa de **zonas no cubiertas**, elige en **Etiquetas** el modo **Bloqueo** (*Blocking*): la capa no muestra etiquetas, pero sus entidades actúan como **obstáculos**. Así ninguna etiqueta tapará la figura.
2. Ríos: **Colocación ▸ Curvada**, repetir cada 100 mm, cursiva azul.
3. Comunas: **Horizontal** con **espaciado de letras** 2 y prioridad baja (si chocan con un hospital, cede la comuna).

### Paso 4 · Máscaras en lugar de búferes gruesos

Un búfer blanco grueso «perfora» el mapa. Una **máscara** solo oculta lo que elijas:

1. Etiquetas de hospitales ▸ **Máscara** ▸ activa, tamaño 1 mm.
2. En la capa **vías** ▸ **Máscaras** ▸ marca que la máscara de las etiquetas de hospitales oculte las vías.

El texto queda limpio sobre las calles sin tapar las zonas de color.

!!! captura "Captura pendiente · 4.6-05"

    - **Tipo:** PNG comparativo
    - **Archivo:** `assets/images/modulo-04/4-6/4-6-05-bufer-vs-mascara.png`
    - **Qué mostrar:** La misma etiqueta con búfer blanco grueso y con máscara que oculta solo las vías.

### Paso 5 · Llamadas en el centro denso

En el centro, activa **Llamadas** (*callouts*) en las etiquetas de hospitales: tipo **Línea simple**, desde el punto más cercano. Mueve a mano las etiquetas que lo necesiten con la **barra de etiquetado** (las posiciones se guardan en el almacenamiento auxiliar del proyecto, [2.3](../modulo-02/03-gestionar-proyectos.md)).

### Paso 6 · Revisar lo no colocado

Activa **Mostrar etiquetas no colocadas** (barra de etiquetado): aparecen en rojo. Si un hospital está en rojo, sube su prioridad, reduce otras etiquetas o usa una llamada. **Ningún hospital** debe quedar sin etiqueta.

!!! captura "Captura pendiente · 4.6-07"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-04/4-6/4-6-07-no-colocadas.gif`
    - **Qué mostrar:** Activar Mostrar etiquetas no colocadas, detectar un hospital en rojo y resolverlo subiendo su prioridad.

---

## Inténtalo tú

!!! example "Reto 4.6 · El centro a 1:10 000"

    Etiqueta el centro de la ciudad (comuna Adela Zamudio) a 1:10 000 para una ficha impresa A4:

    - **Todos** los hospitales y clínicas con nombre, sin etiquetas no colocadas.
    - Las vías troncales y principales con su nombre.
    - El río Rocha.
    - Ninguna etiqueta tapa un símbolo de establecimiento.

    Exporta la ficha y una captura con **Mostrar etiquetas no colocadas** activado para demostrar que no quedan pendientes.

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Selección | Solo se etiqueta lo que apoya el mensaje a esa escala |
| Jerarquía tipográfica | Hospitales > clínicas > resto; comunas y ríos con estilo propio |
| Legibilidad | Ningún texto menor de 6 pt; sin solapes; contraste suficiente |
| Prioridad | Ningún hospital sin colocar |
| Limpieza | Máscaras en vez de búferes gruesos; llamadas donde hay densidad |

### Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| Faltan etiquetas importantes | Prioridad baja o conflictos | Sube la prioridad; revisa no colocadas |
| Etiquetas lejos de su punto | Colocación libre | Modo **cartográfico** alrededor del punto |
| Nombres de río al revés | Colocación sin orientación | **Curvada** con «sobre la línea» y orientación |
| Las posiciones manuales se perdieron | Proyecto sin almacenamiento auxiliar | Guarda como `.qgz` |
| Etiquetas «NULL» | Entidades sin nombre | Condición `"nombre" IS NOT NULL` |

---

## Comprueba lo aprendido

??? question "1. ¿Qué diferencia hay entre un búfer y una máscara?"

    El búfer dibuja un halo que tapa **todo** lo que hay debajo; la máscara oculta solo las capas que elijas.

??? question "2. ¿Para qué sirve declarar una capa como obstáculo?"

    Para que el motor de etiquetado **evite** colocar etiquetas sobre ella.

??? question "3. ¿Por qué los ríos se rotulan en cursiva azul?"

    Por convención cartográfica: la hidrografía se distingue tipográficamente.

??? question "4. Repaso de 4.2 · ¿Por qué no etiquetar los 661 establecimientos a 1:100 000?"

    Porque no caben: el texto se superpondría y el mapa sería ilegible a esa escala.

---

## Tu proyecto

Decide el etiquetado de la lámina del Concejo: probablemente solo **comunas** y quizá los **hospitales**. Escríbelo en el brief: menos etiquetas también es una decisión de diseño.

---

## Referencias

- Imhof, E. (1975). Positioning names on maps. *The American Cartographer, 2*(2), 128–144. <https://doi.org/10.1559/152304075784313304>
- Tyner, J. A. (2010). *Principles of Map Design* (cap. sobre tipografía). Guilford Press.
- QGIS Project. (s. f.). *Manual de usuario: Propiedades de etiquetas*. <https://docs.qgis.org/latest/es/docs/user_manual/working_with_vector/vector_properties.html#labels-properties>
- QGIS Project. (s. f.). *Manual de usuario: Máscaras*. <https://docs.qgis.org/latest/es/docs/user_manual/working_with_vector/vector_properties.html#masks-properties>
