---
title: Prácticas y laboratorios
description: Índice de todos los laboratorios guiados, retos y talleres del curso, con tiempo, datos, producto y nivel, y una ruta exprés de un día.
---

# Prácticas y laboratorios

Todas las prácticas usan el **[paquete de datos del curso](../descargas/index.md)** (caso Cochabamba). Cada lección tiene un laboratorio guiado (**Hazlo conmigo**) y un reto autónomo (**Inténtalo tú**); los módulos cierran con un taller integrador.

**Nivel:** ●○○ inicial · ●●○ intermedio · ●●● integrador

---

## Ruta exprés

¿Necesitas resultados en un día? Estos seis laboratorios te llevan de un CSV a un mapa publicado (≈ 7 horas):

| Orden | Lección | Qué logras | Tiempo |
|---|---|---|---|
| 1 | [2.1 Preparar un entorno de trabajo](../modulo-02/01-entorno-trabajo.md) | QGIS instalado, carpeta del curso y proyecto base | 45 min |
| 2 | [2.5 Convertir una tabla en información geográfica](../modulo-02/05-tablas-coordenadas.md) | 661 establecimientos en el mapa, validados | 75 min |
| 3 | [2.6 Resolver problemas de coordenadas](../modulo-02/06-problemas-coordenadas.md) | Asignar frente a reproyectar, sin miedo | 60 min |
| 4 | [2.9 Representar y etiquetar](../modulo-02/09-simbologia-etiquetas.md) | Primera lectura temática | 60 min |
| 5 | [3.7 Analizar proximidad y superposición](../modulo-03/07-proximidad-superposicion.md) | ¿Quién vive lejos de un servicio de salud? | 90 min |
| 6 | [4.7 Diseñar una composición reutilizable](../modulo-04/07-disenar-composicion-reutilizable.md) | Lámina A4 lista para imprimir | 75 min |

!!! warning "La ruta exprés no reemplaza el curso"

    Te da resultados rápidos, pero se salta la calidad de datos (2.7, 3.1), la clasificación honesta (4.4) y la reproducibilidad (3.11). Vuelve a ellas antes de usar tus resultados para decidir.

---

## Módulo 1 · Fundamentos (sin software)

| Tema | Ejercicio resuelto | Producto del proyecto | Nivel |
|---|---|---|---|
| [1.1](../modulo-01/01-sistemas-informacion-geografica.md) | Clasificar preguntas espaciales | Problema y preguntas | ●○○ |
| [1.3](../modulo-01/03-fundamentos-geodesia.md) | Grados ↔ metros; GMS | Coordenadas del área | ●○○ |
| [1.4](../modulo-01/04-sistemas-referencia.md) | Identificar el SRC de una coordenada | Inventario de SRC | ●●○ |
| [1.6](../modulo-01/06-sistema-utm.md) | Calcular zonas UTM de Bolivia | Zona y EPSG | ●○○ |
| [1.8](../modulo-01/08-escala-cartografica.md) | Distancias, áreas y escalas | Escala de trabajo | ●○○ |
| [1.9](../modulo-01/09-escala-resolucion-precision.md) | Calcular un RMSE | Aptitud de cada dato | ●●○ |
| [1.13](../modulo-01/13-calidad-informacion.md) | Propagación del error | Plan de calidad | ●●○ |
| [Práctica integradora](../modulo-01/practica.md) | Diagnóstico de un paquete de datos sin software | Informe de diagnóstico | ●●● |

## Módulo 2 · Introducción a QGIS

| Lección | Reto | Datos | Producto | Nivel |
|---|---|---|---|---|
| [2.1](../modulo-02/01-entorno-trabajo.md) | Entorno reproducible | Paquete del curso | Ficha del entorno | ●○○ |
| [2.2](../modulo-02/02-orientarse-interfaz.md) | Preparar la reunión del equipo | Proyecto base | 6 marcadores | ●○○ |
| [2.3](../modulo-02/03-gestionar-proyectos.md) | Entrega portable | Proyecto + datos | ZIP comprobado | ●●○ |
| [2.4](../modulo-02/04-incorporar-datos.md) | Inventario de datos | `datos/originales/` | `inventario_datos.csv` | ●○○ |
| [2.5](../modulo-02/05-tablas-coordenadas.md) | La planilla con errores | `equipamientos_errores.csv` | Tabla de diagnóstico | ●●○ |
| [2.6](../modulo-02/06-problemas-coordenadas.md) | Ficha de diagnóstico de SRC | `comunas_sin_prj.shp`, `vias_principales_src_erroneo.gpkg` | Capas corregidas | ●●○ |
| [2.7](../modulo-02/07-leer-datos.md) | Matriz de control | CSV con errores | `control_calidad_*.csv` | ●●○ |
| [2.8](../modulo-02/08-seleccionar-filtrar.md) | Dos subconjuntos reproducibles | Equipamientos, zonas | GeoPackage + expresiones | ●●○ |
| [2.9](../modulo-02/09-simbologia-etiquetas.md) | Lectura temática | Zonas, equipamientos | Mapa + 3 estilos | ●○○ |
| [2.10](../modulo-02/10-explorar-raster.md) | Cuatro miradas | DEM, Sentinel-2 | 4 vistas + NDVI a mano | ●●○ |
| [2.11](../modulo-02/11-servicios-web.md) | Ficha de servicios | Servicios en línea | Ficha | ●○○ |
| [2.12](../modulo-02/12-taller-proyecto.md) | **Taller · proyecto funcional** | Todo | Entrega comprobada | ●●● |

## Módulo 3 · Edición, integración y análisis

| Lección | Reto | Producto | Cifra de control | Nivel |
|---|---|---|---|---|
| [3.1](../modulo-03/01-preparar-datos-confiables.md) | Informe de auditoría | GeoPackage auditado | 661 entidades, 0 códigos repetidos | ●●○ |
| [3.2](../modulo-03/02-digitalizar-editar-precision.md) | Áreas verdes | `digitalizacion.gpkg` | Topología sin errores | ●●○ |
| [3.3](../modulo-03/03-disenar-formularios-captura.md) | Formulario de áreas verdes | Estilo con formulario | 5 casos inválidos bloqueados | ●●○ |
| [3.4](../modulo-03/04-construir-indicadores-expresiones.md) | Indicador de educación | Ficha técnica | 62 / 140 / 125 zonas por estado | ●●○ |
| [3.5](../modulo-03/05-integrar-tablas.md) | Visitas por establecimiento | Relación 1:N | 6/6 comunas emparejadas | ●●○ |
| [3.6](../modulo-03/06-relaciones-espaciales.md) | Matriz pregunta → predicado | Conteos por comuna | 113 / 10 establecimientos de salud | ●●○ |
| [3.7](../modulo-03/07-proximidad-superposicion.md) | Sensibilidad de la cobertura | `cobertura.gpkg` | ≈ 90 000 hab. (15 %) | ●●● |
| [3.8](../modulo-03/08-preparar-combinar-raster.md) | Máscara urbanizable | Ráster alineados | Total de población 1 145 726 conservado | ●●● |
| [3.9](../modulo-03/09-relieve-estadisticas-zonales.md) | Zonas planas sin cobertura | Pendiente por zona | 45 zonas | ●●○ |
| [3.10](../modulo-03/10-georreferenciar-mapas-historicos.md) | Informe de georreferenciación | Plano georreferenciado | RMSE < 3 m | ●●○ |
| [3.11](../modulo-03/11-procedimientos-reproducibles.md) | Modelo de prioridad | `.model3` | Reproduce 3.7 | ●●● |
| [3.12](../modulo-03/12-laboratorio-decision-territorial.md) | **Laboratorio · decisión territorial** | Memoria técnica | 6 zonas candidatas | ●●● |

## Módulo 4 · Diseño cartográfico

| Lección | Reto | Producto | Nivel |
|---|---|---|---|
| [4.1](../modulo-04/01-definir-encargo-cartografico.md) | Dos briefs, dos bocetos | Briefs | ●○○ |
| [4.2](../modulo-04/02-preparar-informacion-escala-salida.md) | Tres escalas | Temas del mapa | ●●○ |
| [4.3](../modulo-04/03-elegir-representacion-tematica.md) | Tres variables, tres representaciones | 3 mapas | ●●○ |
| [4.4](../modulo-04/04-evaluar-clasificaciones-colores.md) | Cambiar la interpretación | Clasificación justificada | ●●○ |
| [4.5](../modulo-04/05-construir-jerarquia-visual.md) | Jerarquía para el atlas | 3 estilos | ●●○ |
| [4.6](../modulo-04/06-resolver-etiquetado-mapas-complejos.md) | El centro a 1:10 000 | Ficha sin etiquetas pendientes | ●●○ |
| [4.7](../modulo-04/07-disenar-composicion-reutilizable.md) | Plantillas del curso | 2 plantillas `.qpt` | ●●○ |
| [4.8](../modulo-04/08-coordinar-mapas-elementos-complementarios.md) | Dos mapas comparables | Lámina A3 | ●●○ |
| [4.9](../modulo-04/09-incorporar-informacion-dinamica.md) | Ficha que se actualiza sola | Ficha dinámica | ●●○ |
| [4.10](../modulo-04/10-producir-atlas-territorial.md) | Atlas de prioridades | Atlas PDF | ●●● |
| [4.11](../modulo-04/11-revisar-exportar-distintos-usos.md) | Familia de salidas | PDF, PNG, SVG | ●○○ |
| [4.12](../modulo-04/12-taller-editorial-publicar-coleccion-coherente.md) | **Taller editorial** | Colección publicada | ●●● |

---

## Para docentes

Las **cifras de control** de esta página y de cada sección «¿Lo hiciste bien?» se calcularon con los scripts del repositorio (`scripts/soluciones_modulo3.py`, `scripts/generar_figuras_modulo4.py`) sobre el mismo paquete de datos. Al ejecutarlos se generan, además, capas de solución, una plantilla de composición y el atlas en PDF que pueden usarse como referencia de corrección.

<!-- TODO-MANUAL[soluciones]: decidir si se publica un paquete de soluciones (.qgz por laboratorio) solo para docentes o abierto. -->
