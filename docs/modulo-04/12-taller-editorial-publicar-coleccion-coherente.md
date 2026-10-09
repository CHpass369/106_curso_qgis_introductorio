---
title: 4.12 Taller editorial · Publicar una colección coherente
description: Integración de diseño, simbología, composición, automatización, exportación y control editorial para publicar una colección cartográfica coherente y verificable.
---

# 4.12 Taller editorial · Publicar una colección coherente

Llegó el momento de cerrar el caso. La Dirección de Planificación quiere publicar los resultados: una **lámina** para el Concejo, el **atlas** por comuna para la red de salud y una **ficha técnica** que explique cómo se hizo. Tres productos que deben verse como **una familia**: mismos colores para lo mismo, misma tipografía, mismas fuentes citadas, mismas cifras. Y que cualquier persona pueda **verificar** de dónde salió cada número.

!!! abstract "En este taller"

    **Integrarás:** encargo (4.1), escala (4.2), representación y color (4.3–4.4), jerarquía (4.5), etiquetado (4.6), composición (4.7–4.8), textos dinámicos (4.9), atlas (4.10) y exportación (4.11), sobre los resultados del Módulo 3.

    **Tiempo:** 4 h · **Producto:** la colección publicada en `salidas/coleccion_v01/` con su manual de estilo y su memoria técnica.

---

## La colección

| Producto | Destinatario | Formato | Mensaje |
|---|---|---|---|
| **1 · Lámina síntesis** | Concejo Municipal | A4 horizontal, PDF + PNG | «Unas 90 000 personas viven lejos de un servicio de salud; más de la mitad en Itocta» |
| **2 · Atlas por comuna** | Red de salud | A4 vertical, PDF de 6 páginas | «Estas son las zonas sin cobertura de tu comuna» |
| **3 · Lámina de propuesta** | Concejo y Dirección | A4 horizontal | «Seis zonas candidatas para un nuevo centro; la elección depende de las prioridades» |
| **4 · Ficha técnica** | Técnicos y auditores | PDF, 2 páginas | Datos, métodos, supuestos, limitaciones |

---

## Fase 1 · Manual de estilo (45 min)

Antes de tocar las composiciones, escribe `documentos/manual_estilo.md`:

| Elemento | Decisión |
|---|---|
| Paleta del tema | Sin cobertura `#ea580c` · Cubierta `#e5e7eb` · Sin población `#fafafa` |
| Paleta de apoyo | Establecimientos `#1e3a8a` · Comunas borde `#6b7280` |
| Fondo | Vías `#9ca3af` · Ríos `#93c5fd` |
| Tipografía | Una familia libre (p. ej., *Noto Sans* u *Open Sans*): títulos 18 pt negrita, subtítulos 10 pt, pie 6,5 pt |
| Clasificación | Clases fijas de densidad: 0–1 000–3 000–5 000–8 000 hab./km² |
| Cifras | Redondeadas a miles en textos de comunicación; exactas en la ficha técnica |
| Atribución | «© colaboradores de OpenStreetMap (ODbL); WorldPop 2020 (CC BY 4.0); Copernicus» |
| Nombres de archivo | `AAAA-MM_producto_formato_vNN` |

Guarda los estilos (`.qml`) y las plantillas (`.qpt`) que materializan este manual en `estilos/` y `plantillas/`.

## Fase 2 · Producir (90 min)

1. **Lámina síntesis**: plantilla horizontal (4.7) + localizador (4.8) + cifras dinámicas (4.9).
2. **Atlas**: plantilla vertical + atlas por comuna con resaltado y escalas predefinidas (4.10).
3. **Lámina de propuesta**: las 6 zonas candidatas de [3.12](../modulo-03/12-laboratorio-decision-territorial.md) con su ranking en una tabla, y una nota sobre la **sensibilidad** a los pesos.
4. **Ficha técnica**: texto (no mapa) con datos, SRC, métodos, reglas, supuestos y limitaciones.

## Fase 3 · Control editorial (45 min)

Revisa la colección **como conjunto** con esta tabla:

| Control | Lámina | Atlas | Propuesta | Ficha |
|---|---|---|---|---|
| Misma paleta para «sin cobertura» | | | | — |
| Misma tipografía y tamaños | | | | |
| Mismas cifras (90 000; 15 %; Itocta 49 714) | | | | |
| Fuentes y fecha completas | | | | |
| Ninguna etiqueta crítica sin colocar | | | | — |
| Legible en gris y con daltonismo | | | | — |
| Nombre de archivo según el manual | | | | |

Pide a un compañero que haga la **revisión cruzada** con la misma tabla: los errores propios se ven peor.

## Fase 4 · Publicar (30 min)

1. Exporta según 4.11 a `salidas/coleccion_v01/`.
2. Incluye `LEEME.txt` con la lista de productos, su propósito y su fecha.
3. Empaqueta el proyecto (`proyectos/`), los estilos, las plantillas y los datos de trabajo para que la colección sea **reproducible**.
4. Prueba la portabilidad como en [2.12](../modulo-02/12-taller-proyecto.md).

---

## Rúbrica integradora

| Criterio | Excelente (4) | Suficiente (2) | Insuficiente (0) |
|---|---|---|---|
| **Encargo** | Cada producto responde a su brief y lo demuestra | Responde parcialmente | Productos genéricos |
| **Representación** | Datos normalizados, clasificación justificada, paletas accesibles | Algún error menor | Coropletas de totales o arcoíris |
| **Jerarquía y legibilidad** | Mensaje evidente en 30 s; etiquetado limpio | Mensaje identificable con esfuerzo | Mapa confuso |
| **Coherencia de la colección** | Paleta, tipografía, cifras y fuentes idénticas | Pequeñas inconsistencias | Productos que no parecen de la misma serie |
| **Automatización** | Cifras y atlas dinámicos, sin números a mano | Parcial | Todo manual |
| **Honestidad** | Supuestos, limitaciones y sensibilidad explícitos | Mencionados de pasada | Ausentes |
| **Producción** | Formatos y resoluciones correctos; nombres según manual | Algún formato inadecuado | Archivos ilegibles o mal nombrados |

**Aprobación:** 18 de 28 puntos y ningún criterio en «Insuficiente».

---

## Comprueba lo aprendido

??? question "1. ¿Qué hace que una colección sea «coherente»?"

    Que todos sus productos usen las **mismas decisiones** (paleta, tipografía, clasificación, cifras, fuentes) para representar lo mismo.

??? question "2. ¿Por qué escribir un manual de estilo antes de producir?"

    Porque fija las decisiones una vez; producir sin él genera inconsistencias que luego hay que corregir producto por producto.

??? question "3. ¿Qué debe contener la ficha técnica que no está en los mapas?"

    El detalle de **datos, métodos, reglas, supuestos y limitaciones**, para que otra persona pueda verificar o rehacer el trabajo.

??? question "4. Repaso del curso · ¿Qué decisión del Módulo 1 sigue presente en cada mapa de la colección?"

    Por ejemplo, el **SRC** de trabajo (EPSG:32719), la **escala** adecuada al uso y la declaración de la **calidad** de los datos.

---

## Cierre del curso

Empezaste preguntando **qué es un SIG**. Terminas con una colección cartográfica que responde una pregunta real sobre tu territorio, con datos verificados, análisis reproducible y mapas honestos. Ese recorrido —**entender, manejar, analizar, comunicar**— es el oficio. QGIS es solo la herramienta.

!!! success "¿Y ahora?"

    - Repite el caso con **tu municipio** o con otro servicio (educación, áreas verdes, mercados).
    - Explora el **análisis de redes** (distancias por calles) y **QField** para verificar en terreno.
    - Publica tus mapas en la web con **QGIS Cloud**, **qgis2web** o un servidor institucional.
    - Comparte tu trabajo: la comunidad de QGIS y OpenStreetMap crece con cada persona que aporta.

---

## Referencias

- Kraak, M.-J., & Ormeling, F. (2020). *Cartography: Visualization of Geospatial Data* (4.ª ed.). CRC Press.
- Brewer, C. A. (2016). *Designing Better Maps* (2.ª ed.). Esri Press.
- Monmonier, M. (2018). *How to Lie with Maps* (3.ª ed.). University of Chicago Press.
- Field, K. (2018). *Cartography.* Esri Press.
- QGIS Project. (s. f.). *Manual de usuario: Diseños de impresión*. <https://docs.qgis.org/latest/es/docs/user_manual/print_composer/index.html>
