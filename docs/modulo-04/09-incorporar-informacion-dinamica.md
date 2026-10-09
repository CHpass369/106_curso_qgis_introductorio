---
title: 4.9 Incorporar información dinámica
description: Uso de variables, expresiones y atributos para automatizar títulos, fechas, fuentes, textos, tablas y otros elementos dentro de composiciones cartográficas en QGIS.
---

# 4.9 Incorporar información dinámica

Escribiste a mano «≈ 90 000 habitantes sin cobertura» en la lámina. El próximo año llegan datos nuevos, el número cambia… y nadie actualiza el texto. Un mapa con cifras escritas a mano **envejece mal**. Con **expresiones** en el diseñador, los textos se calculan desde los datos cada vez que exportas: la fecha, el autor, la población sin cobertura y hasta la frase del título se actualizan solos.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Insertar **variables** (`@project_title`, `@project_author`, `@layout_name`…) en etiquetas.
    - Escribir **expresiones** `[% … %]` que calculan cifras desde las capas con `aggregate()`.
    - Formatear números y fechas para el lector.
    - Agregar **tablas de atributos** dinámicas a la composición.
    - Probar que los textos cambian cuando cambian los datos.

    **Tiempo:** 75 min (20 de lectura · 55 de práctica) · **Datos:** zonas con estado de cobertura, comunas con población · **Producto:** lámina con textos dinámicos y una tabla por comuna.

---

## Idea central

### Texto fijo frente a texto dinámico

| Texto fijo | Texto dinámico | Se actualiza cuando… |
|---|---|---|
| «Elaboró: Ana Pérez» | `[% @project_author %]` | Cambias el autor en Propiedades del proyecto |
| «Octubre de 2026» | `[% format_date(now(), 'MMMM yyyy') %]` | Exportas |
| «≈ 90 000 habitantes» | `[% aggregate('zonas', 'sum', "pob_2020", "estado" = 'no_cubierta') %]` | Cambian los datos |
| «Escala 1:90 000» | `[% '1:' || format_number(item_variables('mapa_principal')['map_scale'], 0) %]` | Cambias el zoom |

### Funciones útiles

| Función | Para | Ejemplo |
|---|---|---|
| `aggregate(capa, función, expresión, filtro)` | Sumar, contar, promediar otra capa | Población sin cobertura |
| `format_number(valor, decimales)` | Separadores y decimales | `format_number(90073, 0)` |
| `round(valor, -3)` | Redondear a miles (evita falsa precisión) | 90 073 → 90 000 |
| `format_date(fecha, formato)` | Fechas legibles | `'dd/MM/yyyy'` |
| `@project_*`, `@layout_*`, `@map_*` | Metadatos del proyecto, del diseño o del mapa | `@project_title` |

!!! tip "Redondea lo que comunicas"

    Para el Concejo, «unas **90 000** personas» es más honesto que «**90 073**», porque la población es una estimación ([1.9](../modulo-01/09-escala-resolucion-precision.md)). Usa `round(…, -3)` en los textos de comunicación y el valor exacto en la ficha técnica.

---

## Hazlo conmigo

### Paso 1 · Metadatos del proyecto como variables

1. **Proyecto ▸ Propiedades ▸ Metadatos**: completa título, autor y resumen.
2. En la lámina, reemplaza el pie fijo por:

    ```text
    Elaboró: [% @project_author %] · [% format_date(now(), 'dd/MM/yyyy') %]
    Fuentes: © colaboradores de OpenStreetMap (ODbL); WorldPop 2020 (CC BY 4.0). SRC: [% @project_crs %]
    ```

!!! captura "Captura pendiente · 4.9-02"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-04/4-9/4-9-02-insertar-expresion.png`
    - **Qué mostrar:** El cuadro de propiedades de una etiqueta con el botón Insertar o editar expresión y la expresión del pie.

### Paso 2 · Cifras desde los datos

1. Asegúrate de que la capa de zonas con el campo `estado` (de 3.7) se llame `zonas` en el proyecto.
2. En la nota de lectura:

    ```text
    Unas [% format_number(round(aggregate('zonas', 'sum', "pob_2020", filter:="estado" = 'no_cubierta'), -3), 0) %] personas
    ([% round(100 * aggregate('zonas', 'sum', "pob_2020", filter:="estado" = 'no_cubierta')
             / aggregate('zonas', 'sum', "pob_2020"), 0) %] %) viven en zonas sin cobertura de salud a 1 km.
    ```

3. Comprueba en la vista previa: «Unas 90 000 personas (15 %)…».

### Paso 3 · Probar que es dinámico

Cambia temporalmente el estado de una zona poblada (o vuelve a calcular la cobertura con 800 m, [3.11](../modulo-03/11-procedimientos-reproducibles.md)) y actualiza la vista del diseño: la cifra debe cambiar **sin tocar el texto**. Luego deshaz el cambio.

!!! captura "Captura pendiente · 4.9-05"

    - **Tipo:** GIF
    - **Archivo:** `assets/images/modulo-04/4-9/4-9-05-texto-dinamico.gif`
    - **Qué mostrar:** Cambiar un dato de la capa y ver cómo se actualiza la cifra en la composición.

### Paso 4 · Tabla dinámica por comuna

1. **Añadir tabla de atributos** · capa `Comunas` con los campos de población y población sin cobertura (de 3.7, por unión o relación).
2. **Atributos…**: elige columnas, renómbralas («Comuna», «Población», «Sin cobertura», «%»), ordena por «%» descendente.
3. Formatea los números con el editor de expresiones de cada columna.

!!! captura "Captura pendiente · 4.9-07"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-04/4-9/4-9-07-tabla-atributos.png`
    - **Qué mostrar:** La tabla de atributos de la composición con columnas renombradas, ordenadas y formateadas.

---

## Inténtalo tú

!!! example "Reto 4.9 · Una ficha que se actualiza sola"

    Diseña en la plantilla vertical de 4.7 una **ficha** de la comuna **Itocta** con:

    - Título con el nombre de la comuna obtenido del dato (no escrito a mano).
    - Población, densidad, número de establecimientos de salud y población sin cobertura, todos calculados con `aggregate()` y filtros por `cod_comuna`.
    - Fecha de elaboración y fuentes como variables.

    Luego cambia el filtro a **Alejo Calatayud** y verifica que **todo** se actualiza. Ese es el puente hacia el atlas (4.10).

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Variables | Autor, fecha, título y SRC provienen de variables |
| Cifras | Ningún número del texto está escrito a mano |
| Formato | Separadores de miles, redondeo adecuado, unidades |
| Prueba | Demostraste que la cifra cambia al cambiar los datos |
| Tabla | Columnas con nombres claros, ordenadas y formateadas |

### Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| Aparece el texto `[% … %]` literal | Error de sintaxis | Prueba la expresión en el editor; revisa comillas |
| `aggregate` devuelve NULL | Nombre de capa distinto | Usa el nombre exacto del panel Capas o su id |
| Números con «,» y «.» mezclados | Configuración regional | `format_number` y revisa el idioma de QGIS |
| La cifra no se actualiza | Vista del diseño en caché | **Actualizar vista** en el diseñador |

---

## Comprueba lo aprendido

??? question "1. ¿Por qué evitar cifras escritas a mano en una composición?"

    Porque **envejecen** sin aviso cuando cambian los datos; las expresiones se recalculan al exportar.

??? question "2. ¿Qué hace `aggregate('zonas', 'sum', \"pob_2020\", filter:=\"estado\" = 'no_cubierta')`?"

    Suma la población de las zonas de la capa `zonas` cuyo estado es «no cubierta».

??? question "3. ¿Por qué redondear a miles en una lámina de comunicación?"

    Porque la población es una estimación: mostrar unidades exactas transmite una precisión que no existe.

??? question "4. Repaso de 3.4 · ¿Qué ventaja tiene separar el valor de un indicador de su texto de presentación?"

    El valor se calcula una vez y con precisión; el texto puede redondearlo y formatearlo según el público.

---

## Tu proyecto

Convierte todas las cifras de la lámina del Concejo en expresiones. Si en 2027 se actualizan los datos, bastará con reemplazar las capas y volver a exportar.

---

## Referencias

- QGIS Project. (s. f.). *Manual de usuario: Expresiones en el diseñador de impresión*. <https://docs.qgis.org/latest/es/docs/user_manual/print_composer/composer_items/composer_label.html>
- QGIS Project. (s. f.). *Manual de usuario: Variables*. <https://docs.qgis.org/latest/es/docs/user_manual/introduction/general_tools.html#variables>
- QGIS Project. (s. f.). *Manual de usuario: Funciones de agregación*. <https://docs.qgis.org/latest/es/docs/user_manual/expressions/functions_list.html#aggregates-functions>
- Peterson, G. N. (2020). *GIS Cartography* (3.ª ed.). CRC Press.
