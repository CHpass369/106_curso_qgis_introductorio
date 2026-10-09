---
title: 2.8 Seleccionar, filtrar y extraer información
description: Selección manual y por expresión, filtros de capa, operadores básicos y exportación de entidades seleccionadas en QGIS para construir subconjuntos de información.
---

# 2.8 Seleccionar, filtrar y extraer información

El Servicio Departamental de Salud quiere verificar en terreno **todos los hospitales y clínicas con nombre registrado**, y necesita además un mapa de las **zonas más densas** de dos comunas. Podrías hacer clic en cada punto… o escribir una **expresión** que cualquiera pueda repetir mañana y obtener exactamente el mismo resultado. Esa es la diferencia entre trabajar y trabajar de forma **reproducible**.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Distinguir **seleccionar**, **filtrar** y **extraer**.
    - Seleccionar entidades desde el mapa, desde la tabla y **por expresión**.
    - Escribir expresiones con comparaciones, `AND`/`OR`, `IN`, `BETWEEN`, `ILIKE` y `NULL`.
    - Aplicar un **filtro de capa** y reconocer su indicador.
    - **Exportar** un subconjunto a un GeoPackage documentado.

    **Tiempo:** 90 min (25 de lectura · 65 de práctica) · **Datos:** `datos/trabajo/equipamientos.gpkg` (de [2.5](05-tablas-coordenadas.md)), `limites.gpkg ▸ zonas_analisis` · **Producto:** `datos/trabajo/verificacion_salud.gpkg`.

---

## Idea central

### Tres operaciones, tres efectos

| | **Seleccionar** | **Filtrar** | **Extraer** |
|---|---|---|---|
| Qué hace | Marca entidades (en amarillo) | Oculta las que no cumplen una condición | Crea una **nueva capa** con un subconjunto |
| ¿Modifica la fuente? | No | No | No (crea otra) |
| ¿Dura? | Hasta que cambias la selección | Se guarda en el proyecto | Es un archivo nuevo |
| Indicador | Recuento «seleccionadas» | Ícono de embudo junto a la capa | Una capa más |
| Para qué | Investigar, contar, preparar un paso | Trabajar solo con parte de los datos | Entregar o analizar un subconjunto |

!!! captura "Captura pendiente · 2.8-01"

    - **Tipo:** Imagen (PNG) conceptual
    - **Archivo:** `assets/images/modulo-02/2-8/2-8-01-seleccionar-filtrar-extraer.png`
    - **Qué mostrar:** Tres diagramas simples comparando selección, filtro y extracción sobre la capa de equipamientos.

!!! danger "Un filtro olvidado da resultados incompletos"

    Si una capa tiene un filtro activo, **todo** lo que hagas con ella (contar, analizar, exportar) usará solo las entidades visibles. Revisa siempre el **ícono de embudo** antes de analizar.

### La gramática de las expresiones

| Elemento | Se escribe | Ejemplo |
|---|---|---|
| Nombre de campo | Entre **comillas dobles** | `"subtipo"` |
| Texto | Entre **comillas simples** | `'hospital'` |
| Número | Sin comillas | `5000` |
| Comparación | `=`, `<>`, `>`, `>=`, `<`, `<=` | `"pob_2020" >= 5000` |
| Varias condiciones | `AND`, `OR`, `NOT` | `"tipo" = 'salud' AND "subtipo" = 'hospital'` |
| Lista | `IN (…)`, `NOT IN (…)` | `"subtipo" IN ('hospital', 'clinica')` |
| Rango | `BETWEEN … AND …` | `"pob_2020" BETWEEN 1000 AND 3000` |
| Patrón de texto | `ILIKE` con `%` | `"nombre" ILIKE '%unidad educativa%'` |
| Ausencia de valor | `IS NULL`, `IS NOT NULL` | `"nombre" IS NOT NULL` |

!!! warning "Tres trampas habituales"

    - `"nombre" = 'NULL'` busca el **texto** «NULL». Para la ausencia de valor usa `IS NULL`.
    - `'hospital'` con comillas dobles se interpreta como un **campo** llamado hospital.
    - `A OR B AND C` se evalúa como `A OR (B AND C)`. **Usa paréntesis** siempre que mezcles `AND` y `OR`.

---

## Hazlo conmigo

### Paso 1 · Seleccionar desde el mapa y desde la tabla

1. Agrega `datos/trabajo/equipamientos.gpkg` y activa la capa.
2. Herramienta **Seleccionar objetos espaciales** (barra de selección): haz clic en un punto; con ++ctrl++ añade otros; arrastra un rectángulo sobre el centro.
3. Abre la tabla (++f6++): las filas seleccionadas están resaltadas. **Mapa y tabla comparten la selección.**
4. Limpia todo con **Deseleccionar objetos de todas las capas** (++ctrl+alt+a++).

!!! captura "Captura pendiente · 2.8-02"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-8/2-8-02-seleccion-manual.gif`
    - **Qué mostrar:** Seleccionar varios puntos desde el mapa y observar cómo sus filas quedan seleccionadas en la tabla.

### Paso 2 · Seleccionar por expresión, construyendo de a poco

Abre **Seleccionar por expresión** (++ctrl+f3++). Construye la consulta **una condición a la vez** y anota cuántas entidades selecciona cada versión:

| Versión | Expresión | Seleccionadas |
|---|---|---|
| 1 | `"tipo" = 'salud'` | 173 |
| 2 | `"subtipo" IN ('hospital', 'clinica')` | 139 |
| 3 | `"subtipo" IN ('hospital', 'clinica') AND "nombre" IS NOT NULL AND trim("nombre") <> ''` | 128 |

!!! captura "Captura pendiente · 2.8-03"

    - **Tipo:** Imagen (PNG) anotada
    - **Archivo:** `assets/images/modulo-02/2-8/2-8-03-seleccionar-expresion.png`
    - **Qué mostrar:** El diálogo **Seleccionar por expresión** con la versión 3, la lista de campos, el botón **Todos los valores únicos** y la vista previa del resultado.

!!! tip "Usa el panel central del diálogo"

    En **Campos y valores**, haz doble clic sobre un campo para insertarlo con sus comillas, y pulsa **Todos únicos** para ver los valores reales. Así evitas escribir `'Hospital'` cuando el dato dice `'hospital'`.

Los botones del diálogo permiten **reemplazar** la selección, **añadir** a ella, **eliminar** de ella o **seleccionar dentro de la selección** actual.

### Paso 3 · Buscar texto

```sql
"nombre" ILIKE '%unidad educativa%'
```

`ILIKE` ignora mayúsculas; `%` reemplaza cualquier cantidad de caracteres. Debe seleccionar **214** establecimientos. Prueba la diferencia con `LIKE`.

### Paso 4 · Filtrar una capa

1. Agrega `limites.gpkg ▸ zonas_analisis`.
2. Clic derecho ▸ **Filtrar…** y escribe:

    ```sql
    "pob_2020" / "area_km2" >= 5000
    ```

3. Acepta. Solo quedan **61** zonas y aparece el **embudo** junto al nombre de la capa.
4. Abre la tabla: ¡también tiene 61 filas! El filtro afecta a todo.
5. Quita el filtro (clic en el embudo ▸ borra la expresión) antes de continuar.

!!! captura "Captura pendiente · 2.8-04"

    - **Tipo:** Imagen (PNG) compuesta
    - **Archivo:** `assets/images/modulo-02/2-8/2-8-04-filtro-capa.png`
    - **Qué mostrar:** El Constructor de consultas con la expresión de densidad y, después, la capa con el indicador de filtro activo.

### Paso 5 · Extraer y documentar

1. Vuelve a seleccionar los **128** hospitales y clínicas con nombre (versión 3).
2. Clic derecho sobre la capa ▸ **Exportar ▸ Guardar objetos seleccionados como…**
3. **Formato:** GeoPackage · **Archivo:** `datos/trabajo/verificacion_salud.gpkg` · **Capa:** `hospitales_clinicas`.
4. En **Propiedades ▸ Metadatos** de la nueva capa, escribe en el resumen la **expresión** usada, la fecha y la fuente.

!!! captura "Captura pendiente · 2.8-05"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-8/2-8-05-exportar-seleccion.gif`
    - **Qué mostrar:** Selección validada → **Exportar** → **Guardar objetos seleccionados como** → nueva capa en `datos/trabajo/`.

!!! success "Reproducible = la expresión está escrita"

    Una selección hecha con clics no se puede repetir con exactitud. Una expresión guardada en los metadatos, sí: cualquiera puede obtener **las mismas 128** entidades.

---

## Inténtalo tú

!!! example "Reto 2.8 · Dos subconjuntos para dos equipos"

    **A · Equipo de salud.** Extrae a `verificacion_salud.gpkg ▸ zonas_prioritarias` las zonas de análisis que cumplan **a la vez**:

    - pertenecen a las comunas **Adela Zamudio (C01)** o **Alejo Calatayud (C02)**;
    - tienen una densidad de **5 000 hab./km² o más**.

    Escribe la expresión completa, con paréntesis. ¿Cuántas zonas obtienes?

    **B · Equipo de educación.** Usando **solo expresiones**, responde:

    1. ¿Cuántas escuelas (`subtipo = 'escuela'`) tienen nombre registrado?
    2. ¿Cuántos establecimientos de cualquier tipo **no** tienen nombre?
    3. ¿Cuántas zonas tienen entre 1 000 y 3 000 habitantes? (usa `BETWEEN`)

    **Entregables:** el GeoPackage con dos capas y `documentos/consultas_2-8.md` con cada expresión y su resultado.

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| A | La expresión usa paréntesis y obtiene **28** zonas |
| B1 | 270 escuelas con nombre |
| B2 | 104 establecimientos sin nombre (`IS NULL` **o** vacío) |
| Filtros | Ninguna capa quedó con un filtro olvidado |
| Documentación | Cada subconjunto tiene su expresión en los metadatos |

??? tip "Pista para A"

    ```sql
    ("cod_comuna" IN ('C01', 'C02')) AND ("pob_2020" / "area_km2" >= 5000)
    ```

### Errores frecuentes

| Síntoma | Causa probable | Solución |
|---|---|---|
| La expresión no selecciona nada | Mayúsculas o espacios distintos en el valor | Revisa **Todos únicos**; usa `lower(trim(...))` |
| «Columna no encontrada» | Texto con comillas dobles | Texto con comillas **simples** |
| Resultados de más | `AND`/`OR` sin paréntesis | Agrupa las condiciones |
| `IS NULL` no encuentra vacíos | Son cadenas vacías | `OR trim("campo") = ''` |
| Exporté todo en vez de la selección | Usé **Guardar objetos como** | Usa **Guardar objetos seleccionados como** |
| El análisis «perdió» entidades | Filtro activo | Revisa el embudo |

---

## Comprueba lo aprendido

??? question "1. ¿Qué diferencia hay entre filtrar y seleccionar?"

    Seleccionar **marca** entidades sin ocultar las demás; filtrar **oculta** las que no cumplen la condición, y afecta a todo lo que se haga con la capa.

??? question "2. ¿Por qué `\"subtipo\" = \"hospital\"` no funciona?"

    Porque con comillas dobles `"hospital"` se interpreta como un **campo**. El texto va entre comillas simples.

??? question "3. ¿Qué devuelve `\"tipo\" = 'salud' OR \"tipo\" = 'educacion' AND \"nombre\" IS NULL`?"

    **Todos** los de salud, más los de educación sin nombre, porque `AND` se evalúa antes que `OR`. Probablemente querías paréntesis.

??? question "4. ¿Exportar una selección modifica la capa original?"

    No. Crea un archivo nuevo con las entidades seleccionadas.

??? question "5. ¿Por qué conviene guardar la expresión en los metadatos?"

    Para que el subconjunto sea **reproducible** y verificable por otra persona.

??? question "6. Repaso de 2.7 · ¿Por qué `\"Capacidad\" > 50` falla en el CSV con errores?"

    Porque `Capacidad` es **texto** (contiene `S/D`). Primero habría que convertirlo a número y decidir qué hacer con los códigos.

---

## Tu proyecto

Escribe las expresiones que definen tu **población objetivo** en el caso conductor: ¿qué establecimientos cuentan como «servicio de salud» para medir acceso (¿solo hospitales y clínicas, o también consultorios?) y qué zonas consideras «habitadas»? Esa decisión, documentada, será la base del análisis de cobertura de [3.7](../modulo-03/07-proximidad-superposicion.md).

---

## Referencias

- Ramakrishnan, R., & Gehrke, J. (2003). *Database Management Systems* (3.ª ed., cap. 5: SQL). McGraw-Hill.
- QGIS Project. (s. f.). *Manual de usuario: Expresiones*. <https://docs.qgis.org/latest/es/docs/user_manual/expressions/expression.html>
- QGIS Project. (s. f.). *Manual de usuario: Lista de funciones*. <https://docs.qgis.org/latest/es/docs/user_manual/expressions/functions_list.html>
- QGIS Project. (s. f.). *Manual de usuario: Constructor de consultas*. <https://docs.qgis.org/latest/es/docs/user_manual/working_with_vector/vector_properties.html#query-builder>
- QGIS Project. (s. f.). *Manual de entrenamiento: Seleccionar y filtrar*. <https://docs.qgis.org/latest/es/docs/training_manual/>
