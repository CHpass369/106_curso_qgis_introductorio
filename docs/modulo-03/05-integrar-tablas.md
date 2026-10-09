---
title: 3.5 Integrar tablas sin perder información
description: Integración de información en QGIS mediante claves, cardinalidad, uniones, relaciones uno a muchos, detección de registros sin correspondencia y agregaciones sobre registros relacionados.
---

# 3.5 Integrar tablas sin perder información

La oficina de estadística te envía una planilla con la población de cada comuna. La unes a la capa de comunas por el código y… **tres comunas quedan vacías**. ¿Faltan datos? No: en la planilla los códigos dicen `C1`, ` C02` y `c03`, mientras la capa dice `C01`, `C02` y `C03`. Para la computadora no son iguales. Y hay una comuna `C07` que no existe en el mapa, y `C05` aparece **dos veces**. Integrar tablas es fácil; integrarlas **sin perder ni duplicar información** requiere método.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Identificar **claves** y comprobar su tipo, formato y unicidad.
    - Reconocer la **cardinalidad**: uno a uno, uno a muchos, muchos a muchos.
    - Hacer **uniones** (*joins*) y detectar registros **sin correspondencia**.
    - Crear **relaciones** uno a muchos y resumirlas con `relation_aggregate`.
    - Decidir cuándo unir y cuándo relacionar.

    **Tiempo:** 2 h (30 min de lectura · 90 de práctica) · **Datos:** `limites.gpkg`, `datos/originales/poblacion_comunas.csv`, `datos/ejercicios/poblacion_comunas_claves.csv` · **Producto:** `comunas` con población unida y una relación comuna → zonas.

---

## Idea central

### La clave lo es todo

Una **clave** es el campo que identifica cada registro y permite emparejar tablas. Para que dos claves coincidan deben tener **el mismo valor exacto y el mismo tipo**:

| Capa | Tabla | ¿Coinciden? | Por qué |
|---|---|---|---|
| `C01` | `C01` | Sí | |
| `C01` | `C1` | No | Formato distinto |
| `C02` | ` C02` | No | Espacio inicial |
| `C03` | `c03` | No | Mayúsculas |
| `5` (entero) | `"5"` (texto) | Depende | Tipos distintos: QGIS puede no emparejarlos |

### Cardinalidad

| Relación | Ejemplo | Herramienta adecuada |
|---|---|---|
| **1 : 1** | Comuna ↔ su población | **Unión** |
| **1 : N** | Comuna → sus zonas; establecimiento → sus visitas | **Relación** (o agregación) |
| **N : N** | Establecimientos ↔ programas de salud | Tabla intermedia |

!!! danger "Una unión 1 : N pierde información en silencio"

    La unión de QGIS toma **la primera** coincidencia. Si `C05` aparece dos veces en la tabla, una de las filas se ignora **sin aviso**. Comprueba la unicidad de la clave **antes** de unir.

### Unir no es copiar

Una unión de QGIS es **virtual**: los campos unidos aparecen en la tabla mientras el proyecto mantenga la unión. Para que sean permanentes, **exporta** la capa o usa el algoritmo **Unir atributos por valor de campo**.

---

## Hazlo conmigo

### Paso 1 · Revisar las claves antes de unir

1. Carga `poblacion_comunas.csv` como **texto delimitado sin geometría** (separador `;`).
2. Compara los campos: `comunas.cod_comuna` (texto) y `poblacion_comunas.cod_comuna` (texto). ¿Ambos con el formato `C00`?
3. Comprueba la unicidad en la tabla con **Seleccionar por expresión**: `count("cod_comuna", "cod_comuna") > 1` → 0 registros.

!!! captura "Captura pendiente · 3.5-01"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-03/3-5/3-5-01-tipos-claves.png`
    - **Qué mostrar:** Las propiedades de los campos clave de la capa y de la tabla, con su tipo y valores de ejemplo.

### Paso 2 · Unión 1 : 1

1. `Comunas` ▸ **Propiedades ▸ Uniones** ▸ **+**.
2. **Capa de unión:** `poblacion_comunas` · **Campo de unión:** `cod_comuna` · **Campo destino:** `cod_comuna`.
3. **Campos unidos:** solo `pob_2020` · **Prefijo:** `t_`.
4. Abre la tabla: las 6 comunas tienen `t_pob_2020`. Adela Zamudio: **123 184**.

!!! captura "Captura pendiente · 3.5-03"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-5/3-5-03-crear-union.gif`
    - **Qué mostrar:** Crear la unión entre comunas y la tabla de población y comprobar el campo unido en la tabla de atributos.

### Paso 3 · El caso real: claves imperfectas

1. Carga `datos/ejercicios/poblacion_comunas_claves.csv`. Únela a `Comunas` por `codigo` = `cod_comuna`.
2. Selecciona las comunas sin correspondencia:

    ```sql
    "t2_pob_2020" IS NULL
    ```

    Resultado: **3** comunas (C01, C02, C03).

3. Busca los registros de la **tabla** que no tienen comuna: `C07`. Y los **duplicados**: `C05` aparece dos veces.

!!! captura "Captura pendiente · 3.5-08"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-5/3-5-08-detectar-huerfanos.gif`
    - **Qué mostrar:** Localizar las comunas sin correspondencia y los registros de la tabla que no encuentran pareja.

4. **Corrige la clave sin tocar el original**: en la tabla (o en una copia), crea un campo virtual normalizado y úsalo para unir:

    ```sql
    'C' || lpad(regexp_replace(upper(trim("codigo")), '[^0-9]', ''), 2, '0')
    ```

    `C1` → `C01`, ` C02` → `C02`, `c03` → `C03`.

5. Repite la unión con la clave normalizada: 6 de 6 comunas emparejadas. Documenta `C07` (sin comuna en el mapa) y el duplicado de `C05`.

!!! tip "Contar antes y después"

    Registra: filas en la tabla (8), comunas en la capa (6), emparejadas antes de normalizar (3) y después (6), registros huérfanos (1), duplicados (1). Si los números no cierran, falta algo.

### Paso 4 · Relación 1 : N: comuna → zonas

Cada comuna contiene muchas zonas de análisis. No se «unen»: se **relacionan**.

1. **Proyecto ▸ Propiedades ▸ Relaciones ▸ Añadir relación**.
2. **Padre (referenciada):** `Comunas`, campo `cod_comuna` · **Hija (que referencia):** `Zonas de análisis`, campo `cod_comuna` · **Nombre:** `comuna_zonas`.
3. Abre el formulario de una comuna (Identificar): aparece la **lista de sus zonas**.

!!! captura "Captura pendiente · 3.5-05"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-03/3-5/3-5-05-crear-relacion.png`
    - **Qué mostrar:** La ventana de relaciones con la capa padre, la capa hija, los campos clave y el nombre de la relación.

### Paso 5 · Resumir la relación

En `Comunas`, crea campos virtuales:

```sql
relation_aggregate('comuna_zonas', 'count', "cod_zona")          -- número de zonas
relation_aggregate('comuna_zonas', 'sum', "pob_2020")            -- población
relation_aggregate('comuna_zonas', 'count', "cod_zona", filter:="pob_2020" = 0)  -- zonas deshabitadas
```

Comprueba: Itocta tiene **155** zonas y Adela Zamudio **22**. La población sumada debe coincidir con `t_pob_2020` de la unión: si no coincide, una de las dos fuentes está mal.

!!! captura "Captura pendiente · 3.5-09"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-03/3-5/3-5-09-relation-aggregate-count.gif`
    - **Qué mostrar:** Crear un campo virtual con relation_aggregate y comprobar los resultados por comuna.

??? info "Para saber más · unión permanente con Procesos"

    **Procesos ▸ Unir atributos por valor de campo** crea una capa nueva con la unión ya aplicada y genera una **salida de registros no emparejados**: ideal para documentar qué quedó fuera.

---

## Inténtalo tú

!!! example "Reto 3.5 · Visitas por establecimiento"

    Con la capa `visitas` de [3.3](03-disenar-formularios-captura.md) (carga al menos 10 visitas de prueba, algunas al mismo establecimiento):

    1. Crea la relación **establecimiento (1) → visitas (N)** por `id_equip`.
    2. En `equipamientos`, crea campos virtuales con el **número de visitas** y la **fecha de la última visita** (`relation_aggregate(..., 'max', "fecha_visita")`).
    3. Simboliza los establecimientos: **nunca visitados** en gris, **visitados** en verde.
    4. Encuentra las visitas **huérfanas** (con un `id_equip` que no existe).

    **Entregable:** proyecto con la relación, los campos virtuales y un registro de conteos (visitas, establecimientos visitados, huérfanas).

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Revisión previa | Comprobaste tipo, formato y unicidad de las claves antes de unir |
| Unión 1 : 1 | Las 6 comunas tienen población; Adela Zamudio = 123 184 |
| Claves imperfectas | Detectaste las 3 sin pareja, el huérfano `C07` y el duplicado `C05`, y los resolviste sin modificar el original |
| Relación | `comuna_zonas` funciona en el formulario; Itocta = 155 zonas |
| Verificación | La suma por relación coincide con la población unida |

### Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| Todos los campos unidos vacíos | Tipos de clave distintos o formato diferente | Revisa tipo y valores; normaliza |
| Algunos vacíos | Espacios, mayúsculas, ceros a la izquierda | `upper(trim(...))`, `lpad(...)` |
| Faltan filas sin aviso | Clave repetida en la tabla de unión | Comprueba unicidad antes de unir |
| La unión desaparece en otro equipo | Es virtual y la tabla no viajó | Exporta o incluye la tabla en la entrega |
| `relation_aggregate` devuelve NULL | Nombre o id de la relación incorrecto | Usa el nombre exacto de **Relaciones** |

---

## Comprueba lo aprendido

??? question "1. ¿Por qué `C1` y `C01` no se emparejan?"

    Porque son textos distintos. Las claves deben coincidir **exactamente**.

??? question "2. ¿Qué pasa si unes una tabla con claves repetidas?"

    QGIS toma la **primera** coincidencia y descarta las demás sin aviso: pierdes información.

??? question "3. ¿Cuándo usas una relación en lugar de una unión?"

    Cuando un registro de la capa tiene **muchos** registros relacionados (1 : N), como una comuna con muchas zonas.

??? question "4. ¿La unión cambia el archivo de la capa?"

    No. Es virtual; para hacerla permanente hay que exportar o usar el algoritmo de Procesos.

??? question "5. Repaso de 2.7 · ¿Qué controles de calidad aplicaste a las claves?"

    **Unicidad**, **consistencia de formato** y **completitud** (que todas tengan pareja).

---

## Tu proyecto

Une a tus comunas la tabla de población oficial más reciente que encuentres (INE) y compárala con la de WorldPop. Si difieren mucho, ¿cuál usarías para el informe y por qué? Esta comparación es un argumento de **calidad** que debe aparecer en el informe final.

---

## Referencias

- Date, C. J. (2004). *An Introduction to Database Systems* (8.ª ed.). Addison-Wesley.
- Obe, R. O., & Hsu, L. S. (2021). *PostGIS in Action* (3.ª ed., cap. 1–2). Manning.
- QGIS Project. (s. f.). *Manual de usuario: Propiedades de uniones*. <https://docs.qgis.org/latest/es/docs/user_manual/working_with_vector/vector_properties.html#joins-properties>
- QGIS Project. (s. f.). *Manual de usuario: Crear relaciones uno a muchos*. <https://docs.qgis.org/latest/es/docs/user_manual/working_with_vector/attribute_table.html#creating-one-or-many-to-many-relations>
