---
title: 4.11 Revisar y exportar para distintos usos
description: Revisión final y exportación de productos cartográficos en PDF, SVG e imágenes, considerando resolución, vectorización, ráster, fuentes, tamaño de archivo y soporte de destino.
---

# 4.11 Revisar y exportar para distintos usos

La lámina se ve perfecta en tu pantalla. Pero en la imprenta el texto sale pixelado, en el proyector los grises desaparecen, en WhatsApp el archivo de 48 MB no se envía, y en el informe Word la imagen se ve borrosa. **Exportar es diseñar para el destino.** Esta lección te da una lista de revisión final y la receta de exportación para cada uso.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Revisar una composición con una **lista de control** antes de exportar.
    - Elegir **formato** (PDF, PNG, JPG, SVG) y **resolución** según el destino.
    - Entender qué se exporta como **vector** y qué como **ráster**.
    - Controlar **tamaño de archivo**, **fuentes** y **colores**.
    - Nombrar y versionar las salidas.

    **Tiempo:** 60 min (20 de lectura · 40 de práctica) · **Datos:** la lámina del Concejo (4.7–4.9) · **Producto:** una «familia» de salidas para cuatro usos.

---

## Idea central

### Formato según el destino

| Destino | Formato | Resolución | Por qué |
|---|---|---|---|
| **Impresión** (imprenta, plotter) | PDF vectorial | 300 dpi para lo ráster | Texto y líneas nítidos a cualquier tamaño |
| **Informe** (Word, LibreOffice) | PNG | 200–300 dpi al tamaño final | Buena calidad, sin artefactos |
| **Presentación / pantalla** | PNG | 150 dpi (o ancho de 1920 px) | Liviano y nítido en proyector |
| **Web / mensajería** | PNG o JPG optimizado | 96–150 dpi; < 1 MB | Carga rápida |
| **Edición posterior** (Inkscape, Illustrator) | SVG o PDF con capas | — | Elementos editables |

!!! warning "JPG no es para mapas con texto"

    La compresión JPG crea «ruido» alrededor de letras y líneas finas. Úsalo solo para imágenes satelitales o fotografías; para mapas, **PNG**.

### Vector y ráster dentro del PDF

| Se exporta como **vector** | Se exporta como **ráster** |
|---|---|
| Textos, líneas, polígonos con estilos simples | Capas ráster (Sentinel-2, DEM, sombreado) |
| Leyenda, escala, marcos | Efectos (sombras, desenfoques), modos de mezcla |

Si un elemento usa efectos o mezcla, QGIS puede **rasterizar toda la composición**: el texto pierde nitidez. Revisa la opción **Exportar siempre como vectores** y evita efectos innecesarios en impresión.

### dpi y tamaño

Un A4 a 300 dpi son **3 508 × 2 480 píxeles**: suficiente para imprimir. A 600 dpi, cuatro veces más pesado sin mejora visible. Elige los dpi por el **tamaño final** del uso, no «el máximo».

---

## Hazlo conmigo

### Paso 1 · Lista de control antes de exportar

- [ ] Título, subtítulo, leyenda, escala, norte, fuentes, fecha, autoría, SRC.
- [ ] Ninguna etiqueta importante sin colocar ([4.6](06-resolver-etiquetado-mapas-complejos.md)).
- [ ] Ningún texto menor de 6 pt al tamaño final.
- [ ] Cifras dinámicas actualizadas (4.9) y redondeadas.
- [ ] Leyenda sin capas sobrantes y con unidades.
- [ ] Ortografía (títulos, nombres propios, tildes).
- [ ] Prueba de escala de grises y daltonismo (4.4).
- [ ] Atribuciones obligatorias (OpenStreetMap, WorldPop, Copernicus).

### Paso 2 · PDF para imprenta

**Diseño ▸ Exportar como PDF…** · **Resolución:** 300 dpi · marca **Exportar siempre como vectores** (si no usas efectos) · **Compresión de imagen:** sin pérdida · **Exportación de texto:** *Siempre exportar texto como objetos de texto*. Abre el PDF y amplía al 400 %: el texto debe seguir nítido.

!!! captura "Captura pendiente · 4.11-03"

    - **Tipo:** PNG anotado
    - **Archivo:** `assets/images/modulo-04/4-11/4-11-03-opciones-pdf.png`
    - **Qué mostrar:** El diálogo de exportación PDF con resolución, vectores, compresión y exportación de texto.

### Paso 3 · PNG para informe y pantalla

**Exportar como imagen…** · formato PNG · 200 dpi (informe) y otra a 150 dpi (proyector). Compara peso y nitidez.

### Paso 4 · Versión web

PNG a 1 200 px de ancho. Si pesa más de 1 MB, reduce los dpi u optimízalo. Comprueba que el texto sigue siendo legible en un celular.

### Paso 5 · SVG para edición

**Exportar como SVG…** con **Exportar capas de mapa como grupos SVG**. Ábrelo en Inkscape: cada capa es un grupo editable (útil para ajustes finos de diseño).

### Paso 6 · Nombrar las salidas

```text
salidas/
├── 2026-10_concejo_cobertura_A4_imprenta_v01.pdf
├── 2026-10_concejo_cobertura_A4_informe_200dpi_v01.png
├── 2026-10_concejo_cobertura_A4_pantalla_150dpi_v01.png
├── 2026-10_concejo_cobertura_web_1200px_v01.png
└── 2026-10_concejo_cobertura_A4_editable_v01.svg
```

Fecha, producto, formato y versión: nadie más tendrá que preguntar cuál es el «final_final».

---

## Inténtalo tú

!!! example "Reto 4.11 · Familia de salidas"

    Exporta la lámina del Concejo y el atlas (4.10) para los cuatro destinos (imprenta, informe, pantalla, web). Completa:

    | Archivo | Formato | dpi / px | Peso | ¿Texto vectorial? | Prueba realizada |
    |---|---|---|---|---|---|

    Imprime (o simula a tamaño real) la versión de imprenta y verifica el texto de 6,5 pt del pie.

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Revisión | Lista de control aplicada y sin pendientes |
| Formatos | Cada destino con el formato y la resolución adecuados |
| Calidad | Texto nítido en el PDF al 400 %; PNG web < 1 MB y legible |
| Nombres | Convención con fecha, producto, formato y versión |
| Registro | Tabla del reto completa |

### Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| Texto pixelado en el PDF | Composición rasterizada por efectos | Quita efectos o modos de mezcla; exporta como vectores |
| PDF de 80 MB | Ráster a dpi excesivos | 300 dpi bastan; comprime la imagen |
| Colores distintos impresos | Pantalla RGB frente a impresión | Prueba de impresión; evita colores muy saturados |
| Imagen borrosa en Word | Exportada a 96 dpi y ampliada | Exporta a 200–300 dpi al tamaño final |
| Letras raras en otra computadora | Fuente no incrustada | Exporta texto como contornos o usa fuentes comunes |

---

## Comprueba lo aprendido

??? question "1. ¿Por qué PNG y no JPG para un mapa con texto?"

    Porque JPG comprime con pérdida y crea artefactos alrededor de letras y líneas finas.

??? question "2. ¿Qué causa que un PDF salga rasterizado?"

    Efectos de dibujo, modos de mezcla u otras opciones que obligan a convertir la composición en imagen.

??? question "3. ¿Cuántos píxeles tiene un A4 a 300 dpi?"

    Unos 3 508 × 2 480 píxeles.

??? question "4. Repaso de 2.3 · ¿Por qué los productos exportados van en `salidas/` y no junto a los datos?"

    Para separar **datos**, **proyecto** y **productos**: cada uno tiene su función y su ciclo de vida.

---

## Tu proyecto

Tienes la familia de salidas de la lámina y del atlas. En el taller 4.12 los reunirás en una **colección coherente** con su memoria técnica.

---

## Referencias

- Peterson, G. N. (2020). *GIS Cartography* (3.ª ed., cap. sobre producción). CRC Press.
- QGIS Project. (s. f.). *Manual de usuario: Crear una salida*. <https://docs.qgis.org/latest/es/docs/user_manual/print_composer/create_output.html>
- Adobe. (s. f.). *PDF/X para impresión*. <https://helpx.adobe.com/acrobat/using/pdf-x-pdf-a-pdf.html>
