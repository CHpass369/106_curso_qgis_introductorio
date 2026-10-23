# Revisión y plan de mejora del contenido · Curso Introductorio de QGIS

> Fecha de revisión: 8 de octubre de 2026 · Rama: `CHpass369/mejora-contenido`
> Alcance: todo `docs/` (82 archivos, ~300 000 palabras, 4 módulos, 54 lecciones), `mkdocs.yml` y recursos.

---

## Estado al retomar el trabajo · 8 de octubre de 2026

El diagnóstico que sigue describe el punto de partida, anterior a las mejoras. La rama ya contiene las fases implementadas hasta `2ead375`; este estado distingue lo verificado de lo que todavía necesita trabajo.

| Área | Estado comprobado |
|---|---|
| Plantilla y estilo | Las 51 lecciones numeradas actuales pasan `python scripts/revisar_contenido.py --estricto`: encabezados dentro del límite, sin encabezados numerados ni bloques `text` de prosa detectados, y sección de referencias presente. Esto no sustituye la revisión de cada referencia. |
| Sitio | `python -m mkdocs build --strict` termina con código 0. |
| Datos | El ZIP de estudiantes contiene 42 entradas, pasa la comprobación CRC y contiene los datos principales y el proyecto base. Falta comprobar todas las prácticas desde QGIS con el ZIP descomprimido. |
| Reproducción | Corregidos el nombre esperado del DEM, la indentación de los comandos y los pasos para generar soluciones y actualizar la descarga. La reconstrucción completa requiere QGIS y las fuentes descargadas; no se volvió a ejecutar en esta continuación. |
| Inventario manual | 138 capturas/GIF y 5 tareas manuales en `PENDIENTES.md`. El generador ahora respeta los límites de cada captura y conserva su descripción completa; cuenta con pruebas de regresión. |

**Siguiente trabajo:** producir las capturas y GIF reales de la interfaz en español, priorizando 2.1–2.3; recorrer los laboratorios con el paquete descargado; completar los recursos interactivos de la fase 2 que aún no estén implementados. La foto, los agradecimientos, los videos y la modalidad de distribución de soluciones requieren material o decisiones del instructor. La revisión técnica por especialistas y la validación con estudiantes siguen pendientes.

---

## 1. Resumen ejecutivo

El curso tiene una **base conceptual sólida y ambiciosa**: buena secuencia (fundamentos → QGIS → análisis → cartografía), enfoque en problemas territoriales reales de Bolivia, proyecto integrador, autoevaluaciones, retos y criterios de evaluación. El sitio compila sin errores (`mkdocs build --strict`).

Los problemas principales no están en *qué* se enseña, sino en **cómo se presenta y respalda**:

| Eje | Diagnóstico | Gravedad |
|---|---|---|
| **Diseño** | **0 imágenes** en las 54 lecciones (ni capturas de QGIS ni mapas, incluso en el módulo de cartografía). ~6 200 bloques ` ```text ` usados para texto corrido en M2–M4. Lecciones con 50–100 secciones `##`. | Alta |
| **Coherencia** | `programa.md` describe un Módulo 3 que no existe; la portada omite el Módulo 4; la plantilla de lección cambia en cada módulo; CRS vs SRC; páginas vacías en el menú. | Alta |
| **Contenido** | Prácticas, evaluaciones y descargas vacías; los datos que usan los laboratorios (`datos/originales/*.gpkg`, etc.) no se distribuyen; lecciones muy largas sin ruta mínima. | Alta |
| **Respaldo** | M1 tiene bibliografía académica correcta, pero M3–M4 citan casi solo el manual de QGIS y **la documentación de MkDocs** (irrelevante para el estudiante); 4.10 no tiene referencias; datos de versiones de QGIS a verificar. | Media |
| **Atractivo** | Tono correcto pero denso y "en diapositivas" (frases sueltas en bloques de código); pocas interacciones; ningún video, GIF ni mapa resultado que motive. | Media-alta |

**Recomendación:** antes de escribir contenido nuevo, **unificar la plantilla y aligerar** (fase 1), luego **producir lo visual y los datos** (fase 2), y finalmente **completar prácticas/evaluaciones y respaldo** (fases 3–4).

---

## 2. Diagnóstico detallado (con evidencia)

### 2.1 Métricas del repositorio

| Módulo | Palabras | Lecciones | Bloques ` ```text ` | Imágenes | `##` por lección | "Checkpoint" |
|---|---|---|---|---|---|---|
| M1 · Fundamentos SIG | ~85 000 | 15 | 58 | 0 | 10–17 | 0 |
| M2 · Introducción a QGIS | ~90 000 | 12 | 1 408 | 0 | 12–69 | 0 |
| M3 · Edición y análisis | ~81 000 | 12 | 2 602 | 0 | 29–99 | 47 |
| M4 · Diseño cartográfico | ~48 000 | 12 | 2 213 | 0 | 21–102 | 28 |

Lectura estimada a 180–200 palabras/min: **~25 h solo de texto**, sin contar práctica.

### 2.2 Contenido

**Fortalezas**

- M1 explica conceptos con ejemplos territoriales concretos (centros de salud, torrenteras, catastro) y localiza la teoría en Bolivia (MARGEN-SIRGAS, zonas UTM 19–21).
- Se trabaja el "por qué" (asignar vs reproyectar, falsa precisión, propagación del error), algo que muchos cursos omiten.
- Cada lección de M2–M4 tiene laboratorio guiado, reto, criterios de evaluación, errores frecuentes y autoevaluación.
- M2.1 ya contempla la transición a QGIS 4 / Qt 6.

**Problemas**

1. **Secciones vacías enlazadas desde el menú:** `syllabus.md`, `material.md`, `videos.md`, `acerca.md`, `agradecimientos.md` (0 palabras); `practicas/`, `evaluaciones/`, `descargas/` y `modulo-01/practica.md` (1 frase).
2. **Datos inexistentes:** los laboratorios citan `datos/originales/limites.gpkg`, `equipamientos.csv`, `mapa_historico_1985.tif`, `dem.tif`, etc., pero no hay paquete de datos. Un estudiante autodidacta **no puede hacer ninguna práctica**.
3. **Extensión y granularidad:** lecciones como 2.11 (~9 500 palabras) o 3.11 (96 secciones) no tienen una "ruta mínima"; todo pesa igual.
4. **Contenido inflado por fragmentación:** p. ej. 4.4 dedica secciones separadas a "Ventajas de intervalos iguales", "Problema con datos sesgados", "Ventajas de cuantiles", "Problemas de cuantiles"… que caben en una tabla comparativa.
5. **Falta de resultados visibles:** ninguna lección muestra el mapa o la capa que el estudiante debería obtener.
6. **`instructor.md`** usa una imagen de relleno (`dummyimage.com`).

### 2.3 Diseño de la documentación

1. **Cero recursos visuales reales.** En un curso de SIG, la ausencia de capturas de QGIS, mapas antes/después, diagramas de proyecciones o ejemplos de clasificación es el principal factor de "aburrimiento" y de dificultad (el estudiante no puede verificar si va bien). Los referentes (Spatial Thoughts, QGIS Training Manual, Bolstad) incluyen una captura casi por paso.
2. **Abuso de bloques ` ```text `.** Ejemplo típico (4.4):

    ````markdown
    Dos mapas pueden utilizar:
    ```text
    la misma variable
    los mismos datos
    ```
    ````

    Consecuencias: lectura entrecortada, botón "copiar" sin sentido, fuente monoespaciada, peor accesibilidad (lectores de pantalla) y peor búsqueda. Deben convertirse en prosa, listas, tablas o *admonitions*. Reservar bloques de código para expresiones QGIS, rutas, SQL y Python.
3. **Numeración excesiva** (`## 71. Consistencia editorial`): el índice lateral (TOC) se vuelve inutilizable.
4. **Diagramas Mermaid con colores fijos de tema oscuro** (p. ej. `fill:#132034` en 1.1): se ven mal en modo claro.
5. **Diagrama "concept-snake" de M1** con un orden (Territorio → … → SIG → Análisis) distinto al de los temas reales (1.1 es SIG).
6. **Buenas bases ya presentes:** tarjetas, pestañas, desplegables, widget interactivo de lat/lon en 1.3 (`assets/js/latlon.js`). Hay que **extender ese tipo de interacción**, no inventar otro estilo.

### 2.4 Coherencia

| Incoherencia | Dónde | Corrección |
|---|---|---|
| El programa dice que M3 es "Sistemas de referencia de coordenadas" | `programa.md` | Reescribir con los 4 módulos reales |
| La portada lista solo 3 módulos | `index.md` | Añadir M4 y rediseñar portada |
| "En el Módulo 3 aplicaremos… sistemas de referencia" | `modulo-01/index.md` | Esto ocurre en 2.5–2.6 |
| Comentario "títulos provisionales" | `mkdocs.yml` (nav M3) | Eliminar |
| Plantilla distinta por módulo: M1 (Objetivos → Desarrollo → Ideas clave → Autoevaluación → Actividad → Referencias), M2 (+ Reto), M3 (Misión, Mapa de aprendizaje, Checkpoints, Desafío de 5 minutos…), M4 (Misión, Checkpoints, Cierre, Lo que viene) | todas | Plantilla única (sección 5) |
| **CRS** en M1 (111 usos) vs **SRC** en M2–M4 (~580) | todas | Usar **SRC** (término de la interfaz QGIS en español) y presentar "CRS" una vez como equivalente inglés |
| `ráster` / `raster` mezclados | todas | Glosario + guía de estilo |
| Grupos de navegación con mayúsculas irregulares ("Diseñar Formularios", "Raster y Geoprocesamiento") | `mkdocs.yml` | Normalizar |
| Proyecto integrador de M1 (problema propio) no continúa explícitamente en M2–M4 (que usan "equipamientos/distritos") | M2–M4 | Hilo conductor común (ver 4.3) |
| `docs.zip` (2 MB) versionado en la raíz | repo | Retirar o mover a *Releases* |

### 2.5 Respaldo (fuentes y vigencia)

- **M1:** bibliografía apropiada (Longley et al., Burrough, Kraak & Ormeling, Snyder, Olaya, Torge). Falta citar **fuentes oficiales bolivianas** con enlace (IGM, GeoBolivia, INE) y normas (ISO 19157 para calidad, ISO 19115 para metadatos).
- **M3–M4:** las referencias son mayoritariamente enlaces al manual QGIS y a **Material for MkDocs** (cómo se construyó el sitio). Faltan autores clave de cartografía y análisis: Brewer (*Designing Better Maps*; ColorBrewer), Slocum et al. (*Thematic Cartography*), Tyner, Krygier & Wood (*Making Maps*), Monmonier (*How to Lie with Maps*, muy útil en 4.4), de Smith–Goodchild–Longley (*Geospatial Analysis*).
- **4.10** no tiene sección de referencias.
- **Versiones de QGIS (2.1):** el texto afirma que la próxima LTR será **4.4 (30/10/2026)**. El blog oficial de QGIS (oct. 2025) anunciaba **4.2 como primera LTR 4.x en octubre de 2026**, y en agosto de 2026 la lista de la PSC seguía discutiendo 4.2.4 vs 4.4. **Hay que verificarlo contra la hoja de ruta oficial y dejarlo en un único lugar** (un *snippet* reutilizable) para que no quede desactualizado en 190 menciones a "QGIS 3.44".
- Los enlaces de documentación apuntan a `docs.qgis.org/3.44/`; definir si el curso es **3.44 LTR o 4.x** y apuntar todo a esa versión.
- No hay licencia de contenido declarada (recomendado: CC BY-SA 4.0) ni créditos/licencias de datos.

---

## 3. Referentes revisados y qué adoptar

| Referente | Qué hace bien | Qué adoptamos |
|---|---|---|
| **Spatial Thoughts** (Ujaval Gandhi) — cursos de QGIS gratuitos, CC | Paquete de datos único descargable; pasos numerados de **una acción** con **captura por paso**; producto final visible (mapa, GIF, PDF); datos reales con una pregunta concreta; pre-trabajo con video + quiz. | Paquete de datos `curso-qgis-datos.zip`; capturas por paso; "producto esperado" al inicio de cada laboratorio. |
| **QGIS Training Manual** (oficial) | Ciclo fijo *Follow Along* → *Try Yourself* → *In Conclusion* → *What's Next*. | Plantilla "Hazlo conmigo → Inténtalo tú → Comprueba → Siguiente". |
| **Penn State GEOG 486** (Cartography and Visualization, CC BY-NC-SA) | Lecciones cortas por página; **crítica de mapas** entre pares; laboratorio + resumen; secuencia color → clasificación → coropletas → símbolos proporcionales. | Actividades de "crítica de mapas" en M4; resumen breve de cierre. |
| **ITC – Univ. de Twente** (ejercicios GIScience con QGIS + *Living Textbook*) | "Cada concepto debe demostrarse y operacionalizarse"; el software está al servicio del concepto; mapa conceptual navegable. | Cada concepto de M1 con una mini-demostración en QGIS o widget; glosario enlazado. |
| **Paul Bolstad – QGIS3 Labs** (*GIS Fundamentals*) | Labs secuenciales, datos en zip, **videos cortos** por lab. | Videos de 3–6 min por laboratorio (página `videos.md`). |
| **Brown Univ. – Intro to GIS with QGIS** | Taller de un día, actualizado a la versión vigente. | "Ruta exprés" de 1 día para quien necesita resultados rápidos. |
| **MappingGIS / Geoinnova** (español, certificados QGIS) | Temario práctico en 60 h / 4 semanas; certificación oficial QGIS. | Estimar horas por lección; evaluar certificación como organización QGIS a futuro. |

**Evidencia didáctica a aplicar**

- **Mayer – aprendizaje multimedia:** *segmentación* (bloques cortos controlados por el estudiante), *señalización* (resaltar lo esencial), *coherencia* (quitar lo accesorio), *pre-entrenamiento* (conceptos antes del procedimiento — M1 ya lo hace).
- **Dunlosky et al. (2013):** la **práctica de recuperación** (auto-tests) y la **práctica espaciada** tienen alta utilidad; releer y subrayar, baja. → quizzes cortos frecuentes y repaso de conceptos de módulos anteriores en los retos.

---

## 4. Plan de mejora

### Principios rectores

1. **Mostrar antes que contar:** cada lección abre con el *resultado* (mapa o captura) y una pregunta real.
2. **Ruta mínima + profundización:** lo esencial visible; lo avanzado en desplegables `???` o "Para saber más".
3. **Una sola plantilla** y una sola guía de estilo.
4. **Hacer > leer:** todo concepto se aplica en ≤ 10 min.
5. **Todo dato y afirmación con fuente.**

### Fase 0 · Correcciones rápidas (1 semana)

| # | Tarea | Archivos |
|---|---|---|
| 0.1 | Reescribir `programa.md` con los 4 módulos reales, horas estimadas y productos | `programa.md` |
| 0.2 | Rediseñar `index.md`: 4 tarjetas de módulo, "¿Por dónde empiezo?", requisitos, imagen de portada | `index.md` |
| 0.3 | Ocultar del menú o completar mínimamente las páginas vacías | `mkdocs.yml`, `syllabus.md`, `videos.md`, `material.md`, `acerca.md`, `agradecimientos.md` |
| 0.4 | Corregir referencias cruzadas erróneas (M1 → "Módulo 3 SRC") y comentarios provisionales | `modulo-01/index.md`, `mkdocs.yml` |
| 0.5 | Verificar estado de LTR 4.2/4.4 y centralizarlo en `docs/_snippets/version-qgis.md` (incluido con `pymdownx.snippets`) | `modulo-02/01-entorno-trabajo.md` |
| 0.6 | Foto real del instructor; retirar `docs.zip` del repo | `instructor.md`, raíz |
| 0.7 | Añadir licencia de contenido y `CONTRIBUTING`/guía de estilo | raíz |

### Fase 1 · Plantilla única y aligeramiento (2–4 semanas)

**Plantilla de lección propuesta** (máx. ~10–15 secciones `##`):

```markdown
---
title: X.Y Título orientado a la acción
description: …
tiempo: 60 min (30 lectura · 30 práctica)
nivel: ●○○
---
# X.Y Título

<!-- 1. Gancho -->
![Resultado de la lección](img/xy-resultado.png)
> Pregunta real: "¿Qué barrios están a más de 3 km de un centro de salud?"

!!! abstract "En esta lección"  ← objetivos (3–5) · tiempo · datos · producto

## 1. Idea central            ← 1–3 conceptos, con figura
## 2. Hazlo conmigo           ← pasos numerados, 1 acción + 1 captura por paso
## 3. Inténtalo tú            ← misma tarea, datos distintos, sin pasos
## 4. ¿Lo hiciste bien?       ← captura del resultado esperado + verificación
## 5. Errores frecuentes      ← tabla síntoma → causa → solución
## 6. Comprueba lo aprendido  ← 4–6 preguntas (quiz)
## 7. Tu proyecto             ← aplicación al proyecto integrador
??? info "Para saber más"     ← contenido avanzado/histórico
## Referencias                ← académicas + oficiales + datos
```

| # | Tarea | Criterio de "hecho" |
|---|---|---|
| 1.1 | Guía de estilo: SRC (no CRS), ráster, `Menú ▸ Submenú`, teclas con `++ctrl+c++`, nombres de botones en **negrita**, voz "tú" | Documento aprobado |
| 1.2 | **Convertir bloques ` ```text ` de prosa** a texto, listas, tablas o *admonitions* (script de detección + revisión manual) | < 300 bloques `text` en todo el sitio, solo para código/rutas/expresiones |
| 1.3 | Fusionar secciones atomizadas (p. ej. "Ventajas/Problemas de X" → tabla comparativa) y eliminar numeración de `##` | ≤ 15 `##` por lección |
| 1.4 | Mover contenido avanzado a desplegables `???` | Ruta mínima ≤ 30 min de lectura por lección |
| 1.5 | Aplicar la plantilla a las 54 lecciones (empezar por M2, el más usado) | Checklist de plantilla en cada lección |
| 1.6 | Mermaid neutro de tema (sin colores fijos) o clases CSS con variables de Material | Legibles en claro y oscuro |
| 1.7 | Alinear el diagrama de secuencia de M1 con el orden real de temas | — |

### Fase 2 · Recursos visuales, datos e interactividad (4–6 semanas)

| # | Tarea | Detalle |
|---|---|---|
| 2.1 | **Paquete de datos del curso** | Un municipio boliviano real (p. ej. límites INE/GeoBolivia, equipamientos de OSM, DEM Copernicus GLO-30, imagen Sentinel-2, plano histórico de dominio público) en GeoPackage + GeoTIFF, con `LEEME.md`, licencias y SRC documentados. Publicar en *GitHub Releases* y enlazar en `descargas/`. Incluir versión "con errores" para los laboratorios de diagnóstico (coordenadas intercambiadas, codificación, geometrías inválidas). |
| 2.2 | **Capturas de QGIS** | Una por paso en "Hazlo conmigo", misma versión, tema claro, recortadas, con anotaciones numeradas. Carpeta `docs/modulo-0X/img/`, nombres `xy-paso-01.png`, formato WebP, texto `alt` descriptivo. Activar `glightbox` para ampliar. |
| 2.3 | **Mapas de resultado** | Al menos 1 por lección; en M4, galerías "mapa malo vs mapa bueno" (clasificaciones, jerarquía visual, etiquetado). |
| 2.4 | **Figuras conceptuales** de M1 | Geoide/elipsoide, superficies desarrollables, zonas UTM en Bolivia, vector vs ráster, precisión vs exactitud (diana). SVG propios o de fuentes con licencia libre. |
| 2.5 | **Widgets interactivos** (reutilizar la base de `latlon.js` + D3) | Calculadora de escala, conversor geográficas ↔ UTM con zona automática, comparador de clasificaciones (iguales/cuantiles/Jenks sobre el mismo histograma), simulador de proyecciones (distorsión de Tissot). |
| 2.6 | **Videos cortos** (3–6 min) por laboratorio, con subtítulos | Completar `videos.md` como índice. |
| 2.7 | **GIF animados** para acciones de interfaz breves (arrastrar capas, activar edición) | — |

### Fase 3 · Prácticas, evaluación y proyecto integrador (3–4 semanas)

| # | Tarea | Detalle |
|---|---|---|
| 3.1 | **Hilo conductor único** | Un caso que recorre los 4 módulos (p. ej. "Plan de cobertura de servicios del municipio X"): M1 lo modela, M2 lo carga, M3 lo analiza, M4 lo publica como atlas. El estudiante puede sustituirlo por su propio problema. |
| 3.2 | **Página de prácticas** (`practicas/index.md`) | Tabla de todos los laboratorios y retos con tiempo, datos, producto y nivel. |
| 3.3 | **Práctica integradora de M1** (`modulo-01/practica.md`) | Ejercicio de lápiz y papel + widget: identificar SRC, zona UTM, escala y calidad de un conjunto de datos reales. |
| 3.4 | **Evaluaciones** (`evaluaciones/index.md`) | Rúbricas comunes (ya existen criterios por lección: consolidarlos), quiz por módulo, entregables por módulo, evaluación final. |
| 3.5 | **Quizzes interactivos** | Preguntas de opción múltiple con retroalimentación inmediata (`??? question` con respuesta, o un pequeño componente JS sin dependencias). Repaso espaciado: cada quiz incluye 1–2 preguntas de módulos anteriores. |
| 3.6 | **Soluciones** | Proyectos `.qgz` resueltos por laboratorio en el paquete de datos (para autoaprendizaje). |
| 3.7 | **Crítica de mapas** en M4 | Actividad entre pares con lista de cotejo (inspirado en GEOG 486). |
| 3.8 | **Insignias / hitos** | "Ya puedo…" al final de cada bloque; certificado de finalización opcional. |

### Fase 4 · Respaldo y mantenimiento (continuo)

| # | Tarea |
|---|---|
| 4.1 | Referencias en formato APA uniforme en todas las lecciones: ≥ 1 fuente académica + ≥ 1 oficial (manual QGIS de la versión del curso) + fuentes de datos. Eliminar referencias a Material for MkDocs (moverlas a `CONTRIBUTING`). |
| 4.2 | Añadir referencias faltantes: Brewer, Slocum et al., Krygier & Wood, Monmonier, de Smith et al., ISO 19115/19157, IGM Bolivia, GeoBolivia, INE. Crear `bibliografia.md` global. |
| 4.3 | Revisión técnica por un segundo especialista de M1 (geodesia/UTM) y M4 (cartografía). |
| 4.4 | Fijar versión del curso (3.44 LTR o 4.x LTR) y actualizar enlaces `docs.qgis.org/<versión>/es/`. |
| 4.5 | CI: `mkdocs build --strict` en PR + comprobación de enlaces externos (p. ej. `lychee`) mensual. |
| 4.6 | Fecha de "última revisión" por página (plugin `git-revision-date-localized`). |
| 4.7 | Plataforma: Material for MkDocs anunció que MkDocs 2.0 romperá plugins/temas; fijar versiones en `requirements.txt` (ya están) y evaluar migración a **Zensical** a mediano plazo. |
| 4.8 | Recoger retroalimentación de estudiantes (encuesta por módulo; plugin de *feedback* de Material "¿Te fue útil esta página?"). |

---

## 5. Ideas concretas para que no sea aburrido

- **Abrir con un misterio:** "Estos puntos de pozos aparecen en el océano Índico. ¿Por qué?" (coordenadas intercambiadas, 2.5).
- **Antes/después:** el mismo mapa con 3 clasificaciones (4.4), con deslizador.
- **Retos de 5 minutos** con temporizador y solución desplegable (M3 ya tiene "Desafío de 5 minutos": extenderlo a todos).
- **Casos bolivianos reconocibles:** torrenteras de La Paz, crecimiento de Santa Cruz, salar de Uyuni en imágenes satelitales, mapas históricos de Potosí.
- **"Detective de errores":** dar un proyecto roto (rutas, SRC, codificación) para repararlo.
- **Galería de proyectos** de estudiantes (con permiso) al final de M4.
- **Tarjetas de resumen** imprimibles (una por módulo) y una **hoja de atajos** de QGIS.
- **Progreso visible:** barra o lista "Ya puedo…" por módulo.

---

## 6. Métricas de éxito

| Indicador | Hoy | Meta |
|---|---|---|
| Imágenes por lección práctica | 0 | ≥ 8 |
| Bloques ` ```text ` de prosa | ~6 200 | < 300 |
| `##` por lección (máx.) | 102 | 15 |
| Páginas vacías en el menú | 8 | 0 |
| Lecciones con referencias académicas | ~15/54 | 54/54 |
| Laboratorios ejecutables con datos publicados | 0 | 100 % |
| Tasa de finalización / satisfacción (encuesta) | — | línea base en la primera cohorte |

---

## 7. Priorización sugerida

1. **Fase 0 completa** (impacto inmediato, bajo esfuerzo).
2. **Paquete de datos (2.1)** — desbloquea todas las prácticas.
3. **M2 piloto:** aplicar plantilla + capturas + quiz a 2.1–2.3, validar con 3–5 estudiantes, ajustar.
4. Extender a M2 completo → M3 → M4 → M1 (M1 es el más sólido; requiere sobre todo figuras).
5. Fases 3 y 4 en paralelo.

---

## 8. Fuentes consultadas

- Spatial Thoughts – Spatial Data Visualization with QGIS: <https://courses.spatialthoughts.com/spatial-data-viz.html>
- Geography Realm – Self-Guided QGIS Courses: <https://www.geographyrealm.com/self-guided-qgis-courses/>
- QGIS Training Manual (estructura de lecciones): <https://docs.qgis.org/3.28/pdf/it/QGIS-3.28-TrainingManual-it.pdf>
- Penn State GEOG 486 – Cartography and Visualization: <https://courses.ems.psu.edu/geog486/>
- ITC – Principles and Applications of GIS and EO (ejercicios QGIS): <https://principles-and-applications-of-rs-and-gis.readthedocs.io/en/latest/introduction_oer.html>
- ITC – FOSS4G 2023, diseño del curso online: <https://talks.osgeo.org/foss4g-2023/talk/KYQG9K/>
- Paul Bolstad – QGIS3 Labs: <https://www.paulbolstad.org/web6th/QGIS3Labs.html>
- Brown University – Intro to GIS with QGIS: <https://libguides.brown.edu/gis_data_tutorials/intro_qgis>
- MappingGIS – Programa curso QGIS: <https://mappinggis.com/wp-content/uploads/2026/09/MappingGIS-Programa-curso-QGIS.pdf>
- QGIS – Organizaciones certificadoras (Geoinnova): <https://changelog.qgis.org/en/qgis/certifyingorganisation/asociacion-geoinnova/course/qgis_curso-de-qgis-introduccion-los-sig_2024-03-15-2024-05-08>
- QGIS Blog – Update on QGIS 4.0 Release Schedule and LTR Plans: <https://blog.qgis.org/2025/10/07/update-on-qgis-4-0-release-schedule-and-ltr-plans/>
- QGIS PSC – "Next 4.x LTR" (agosto 2026): <https://lists.osgeo.org/pipermail/qgis-psc/2026-August/010820.html>
- Dartmouth – Mayer's 12 Principles of Multimedia Learning: <https://services.dartmouth.edu/TDClient/1806/Portal/KB/PrintArticle?ID=171655>
- Dunlosky et al. (2013), *Improving Students' Learning With Effective Learning Techniques*, PSPI 14(1). DOI: 10.1177/1529100612453266 — resumen APS: <https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html>
- Material for MkDocs – sobre MkDocs 2.0: <https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/>
