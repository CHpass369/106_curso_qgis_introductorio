---
title: 3.3 Diseñar formularios de captura
description: Diseño de formularios de atributos en QGIS mediante alias, widgets, listas de valores, valores predeterminados y restricciones para prevenir errores durante la captura de información.
---

# 3.3 Diseñar formularios de captura

En la lección 3.1 pasaste dos horas corrigiendo `salud`, `SALUD` y `Salud `, capacidades `-1` y códigos repetidos. Todos esos errores tienen algo en común: **se podían haber evitado al capturar**. Un buen formulario no deja escribir `SALUD ` porque ofrece una lista; no acepta `-1` porque tiene una regla; no repite códigos porque los genera solo. Prevenir es mucho más barato que auditar.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Configurar **alias** y **widgets** adecuados para cada campo.
    - Usar **mapas de valores**, casillas, fechas y rangos.
    - Definir **valores predeterminados** con expresiones (`uuid()`, `now()`, `@user_account_name`).
    - Aplicar **restricciones** (`NOT NULL`, `UNIQUE`, expresiones) con mensajes claros.
    - Organizar el formulario con el **diseñador de arrastrar y soltar**.
    - **Probar** el formulario con casos válidos e inválidos.

    **Tiempo:** 2 h (30 min de lectura · 90 de práctica) · **Datos:** nueva capa en `datos/trabajo/verificacion_campo.gpkg` · **Producto:** capa `visitas` con formulario probado y un estilo `.qml` reutilizable (también en QField).

---

## Idea central

### Prevenir en la captura

| Error que corregiste en 3.1 | Cómo lo previene el formulario |
|---|---|
| `salud`, `SALUD`, `Salud ` | **Mapa de valores**: el usuario elige de una lista |
| Capacidad `-1`, `S/D` | Campo **entero** + widget **Rango** + restricción `> 0` |
| Códigos repetidos | Valor predeterminado `uuid()` + restricción **única** |
| Nombres vacíos | Restricción **no nula** con mensaje |
| Fechas en mil formatos | Widget **Fecha/Hora** con formato fijo |
| «¿Quién cargó esto?» | Predeterminado `@user_account_name` y `now()` |

### Tres piezas de cada campo

| Pieza | Qué controla | Dónde se configura |
|---|---|---|
| **Tipo de dato** | Qué se puede guardar (texto, entero, fecha) | Al crear la capa |
| **Widget** | Cómo se introduce (lista, casilla, calendario) | **Propiedades ▸ Formulario de atributos** |
| **Restricción** | Qué valores se aceptan | Mismo lugar, sección **Restricciones** |

!!! danger "El tipo de dato es la primera restricción"

    Si `capacidad` se crea como **texto**, ningún widget evitará del todo que alguien escriba `S/D`. Diseña los tipos **antes** de capturar.

### Restricciones duras y suaves

- **Dura** (*hard*): el formulario **no se guarda** hasta corregir. Úsala para lo que haría inválido el dato.
- **Suave** (*soft*): muestra una advertencia, pero permite guardar. Úsala para lo **sospechoso** que podría ser real.

---

## Hazlo conmigo

### Paso 1 · Diseñar la tabla

Crea `datos/trabajo/verificacion_campo.gpkg ▸ visitas` (**Punto**, EPSG:32719) con estos campos:

| Campo | Tipo | Alias | Widget | Predeterminado | Restricción |
|---|---|---|---|---|---|
| `uuid` | Texto | Identificador | Edición de texto (no editable) | `uuid()` | No nulo, único |
| `id_equip` | Texto | Código del establecimiento | Edición de texto | — | Expresión: `regexp_match("id_equip", '^EQ-[0-9]{4}$')` |
| `tipo` | Texto | Sector | **Mapa de valores** | — | No nulo |
| `estado` | Texto | Estado | **Mapa de valores** | `'ACTIVO'` | No nulo |
| `capacidad` | Entero | Capacidad (camas o plazas) | **Rango** 1–5000 | — | Expresión condicional (paso 4) |
| `agua_potable` | Booleano | ¿Tiene agua potable? | **Casilla de verificación** | `false` | — |
| `fecha_visita` | Fecha y hora | Fecha de visita | **Fecha/Hora** | `now()` | No nulo |
| `observador` | Texto | Observador | Edición de texto (no editable) | `@user_account_name` | — |
| `foto` | Texto | Fotografía | **Adjunto** (ruta relativa) | — | — |
| `observacion` | Texto | Observaciones | Edición de texto **multilínea** | — | — |

!!! captura "Captura pendiente · 3.3-01"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-03/3-3/3-3-01-formulario-atributos.png`
    - **Qué mostrar:** Pestaña **Formulario de atributos** de la capa `visitas` con la lista de campos, el widget seleccionado, el valor predeterminado y las restricciones.

### Paso 2 · Listas de valores

En `tipo` ▸ **Mapa de valores**:

| Valor (se guarda) | Descripción (se muestra) |
|---|---|
| `salud` | Salud |
| `educacion` | Educación |

En `estado`: `ACTIVO` → *Activo*, `CERRADO` → *Cerrado*, `EN_OBRAS` → *En obras*.

!!! captura "Captura pendiente · 3.3-03"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-3/3-3-03-mapa-valores.gif`
    - **Qué mostrar:** Configurar un mapa de valores con valor guardado y descripción mostrada.

!!! tip "Lo que se guarda y lo que se muestra"

    El **valor** es para la base (sin tildes, sin espacios, estable); la **descripción** es para las personas. Así la base es consistente y el formulario, amable.

### Paso 3 · Valores predeterminados

En `uuid`, **Valor predeterminado:** `uuid()` y desmarca **Editable**. En `fecha_visita`, `now()`. En `observador`, `@user_account_name`.

!!! captura "Captura pendiente · 3.3-06"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-3/3-3-06-predeterminado-now.gif`
    - **Qué mostrar:** Configurar `now()` como valor predeterminado y comprobarlo al crear una entidad.

!!! info "¿Por qué `uuid()` y no 1, 2, 3…?"

    Si dos personas capturan sin conexión en QField, ambas crearían el «registro 15». Un **UUID** se genera de forma independiente en cada dispositivo sin repetirse ([1.12](../modulo-01/12-dato-geoespacial.md)).

### Paso 4 · Restricciones con mensaje

| Campo | Expresión | Mensaje | Tipo |
|---|---|---|---|
| `id_equip` | `regexp_match("id_equip", '^EQ-[0-9]{4}$')` | «El código debe tener el formato EQ-0000» | Dura |
| `capacidad` | `"estado" = 'CERRADO' OR "capacidad" > 0` | «Un establecimiento activo debe tener capacidad mayor que 0» | Dura |
| `capacidad` | `"capacidad" IS NULL OR "capacidad" < 2000` | «Capacidad inusualmente alta: verifica» | **Suave** |
| `fecha_visita` | `"fecha_visita" <= now()` | «La fecha de visita no puede ser futura» | Dura |

!!! captura "Captura pendiente · 3.3-10"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-03/3-3/3-3-10-mensaje-restriccion.png`
    - **Qué mostrar:** Una restricción por expresión con su descripción y la casilla de imponer la restricción.

### Paso 5 · Organizar con arrastrar y soltar

En **Formulario de atributos**, cambia el diseño a **Diseñador de arrastrar y soltar** y crea dos pestañas:

- **Identificación:** `id_equip`, `tipo`, `estado`, `uuid`.
- **Verificación:** `capacidad`, `agua_potable`, `fecha_visita`, `observador`, `foto`, `observacion`.

Agrega una **visibilidad condicional** al grupo de capacidad: solo visible si `"estado" <> 'CERRADO'`.

!!! captura "Captura pendiente · 3.3-13"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-3/3-3-13-arrastrar-soltar.gif`
    - **Qué mostrar:** Crear pestañas en el diseñador de arrastrar y soltar y mover campos a cada una.

### Paso 6 · Probar como un usuario descuidado

Activa la edición y crea entidades. Intenta, a propósito:

| Prueba | Resultado esperado |
|---|---|
| Dejar `tipo` vacío | No se puede guardar |
| Escribir `EQ-12` en el código | Mensaje de formato |
| Capacidad `-25` | El widget no lo permite |
| Capacidad `3000` | Advertencia suave, se puede guardar |
| Estado *Cerrado* | El grupo de capacidad desaparece |
| Copiar un `uuid` de otra entidad | No se puede guardar (único) |

!!! captura "Captura pendiente · 3.3-16"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-3/3-3-16-pruebas-invalidas.gif`
    - **Qué mostrar:** Intentos de guardar entidades inválidas y los mensajes de restricción correspondientes.

Guarda el estilo (incluye el formulario) como `estilos/visitas_formulario.qml`.

??? info "Para saber más · el mismo formulario en el celular"

    **QField** (<https://qfield.org>) abre proyectos de QGIS en Android e iOS y respeta widgets, predeterminados y restricciones. Empaqueta el proyecto con el complemento **QFieldSync** y lleva el formulario a terreno sin rediseñarlo.

---

## Inténtalo tú

!!! example "Reto 3.3 · Formulario para áreas verdes"

    Diseña el formulario de la capa `areas_verdes` de [3.2](02-digitalizar-editar-precision.md) para que un técnico municipal pueda capturar sin errores:

    - `tipo` con lista (`plaza`, `parque`, `ribera`, `cancha`).
    - `estado` (`bueno`, `regular`, `malo`) obligatorio.
    - `superficie_m2` **no editable**, calculada automáticamente con el predeterminado `$area` y **Aplicar valor predeterminado al actualizar**.
    - `tiene_juegos` (casilla) y `tiene_iluminacion` (casilla).
    - Una restricción suave que advierta si la superficie es menor de 50 m² («¿es realmente un área verde?»).

    Prueba el formulario con **cinco casos inválidos** y documenta qué ocurrió en cada uno.

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Tipos | Cada campo tiene el tipo adecuado (entero, booleano, fecha) |
| Widgets | Listas para dominios cerrados, casillas para sí/no, calendario para fechas |
| Predeterminados | `uuid()`, `now()` y `$area` se completan solos |
| Restricciones | Las duras bloquean, las suaves advierten, todas con mensaje claro |
| Pruebas | Cinco casos inválidos documentados con su resultado |
| Reutilización | El `.qml` aplica el formulario completo a otra capa con los mismos campos |

### Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| La lista guarda «Salud» con mayúscula | Se invirtieron valor y descripción | El **valor** va a la izquierda |
| `now()` no se actualiza al editar | Solo se aplica al crear | Marca **Aplicar valor predeterminado al actualizar** si corresponde |
| La restricción no bloquea | No está marcada como **impuesta** | Activa **Imponer restricción de expresión** |
| El adjunto se rompe en otro equipo | Ruta absoluta | Configura rutas **relativas al proyecto** |

---

## Comprueba lo aprendido

??? question "1. ¿Por qué un mapa de valores previene errores de consistencia?"

    Porque el usuario **elige** de una lista cerrada en lugar de escribir: no hay variantes de mayúsculas, tildes ni espacios.

??? question "2. ¿Cuándo usarías una restricción suave en lugar de una dura?"

    Cuando el valor es **sospechoso pero posible** (una capacidad muy alta): conviene advertir sin impedir el registro.

??? question "3. ¿Qué ventaja tiene `uuid()` sobre un número consecutivo?"

    Se genera sin coordinación entre dispositivos y no se repite, aunque varias personas capturen sin conexión.

??? question "4. ¿El formulario corrige los datos que ya existían?"

    No. Las restricciones actúan sobre lo que se **crea o edita**; los datos previos se auditan aparte (3.1).

??? question "5. Repaso de 3.1 · ¿Qué dos hallazgos de la auditoría no puede prevenir ningún formulario?"

    Por ejemplo, que un establecimiento **no esté registrado** (omisión) o que una ubicación esté **mal colocada pero sea válida**. Esos requieren verificación en terreno.

---

## Tu proyecto

Este formulario es la herramienta para **verificar en terreno** los establecimientos que quedaron con limitaciones en 3.1. Si tienes un celular Android o iOS, prueba el proyecto en QField y registra una visita real o simulada.

---

## Referencias

- Haklay, M. (2013). Citizen science and volunteered geographic information: Overview and typology of participation. En D. Sui, S. Elwood & M. Goodchild (Eds.), *Crowdsourcing Geographic Knowledge* (pp. 105–122). Springer. <https://doi.org/10.1007/978-94-007-4587-2_7>
- QGIS Project. (s. f.). *Manual de usuario: Propiedades del formulario de atributos*. <https://docs.qgis.org/latest/es/docs/user_manual/working_with_vector/vector_properties.html#attributes-form-properties>
- QGIS Project. (s. f.). *Manual de usuario: Funciones de expresiones*. <https://docs.qgis.org/latest/es/docs/user_manual/expressions/functions_list.html>
- OPENGIS.ch. (s. f.). *Documentación de QField*. <https://docs.qfield.org>
