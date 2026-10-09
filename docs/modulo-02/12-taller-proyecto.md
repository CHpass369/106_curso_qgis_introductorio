---
title: 2.12 Taller · Construir y entregar un proyecto funcional
description: Taller integrador para organizar, revisar, documentar y entregar un proyecto QGIS funcional mediante rutas relativas, fuentes verificadas, estilos, metadatos y pruebas de portabilidad.
---

# 2.12 Taller · Construir y entregar un proyecto funcional

Es lunes y la Dirección de Planificación municipal te pide «el proyecto de equipamientos» para usarlo en una reunión el miércoles, **en otra computadora y sin que tú estés presente**. Todo lo que aprendiste en este módulo se pone a prueba en una sola entrega: datos verificados, coordenadas correctas, una lectura temática clara, documentación y un proyecto que **se abre a la primera**.

!!! abstract "En este taller"

    **Integrarás:** entorno (2.1), interfaz y marcadores (2.2), proyectos y rutas (2.3), inventario (2.4), tablas y coordenadas (2.5–2.6), lectura de datos (2.7), selecciones (2.8), simbología (2.9), ráster (2.10) y servicios (2.11).

    **Tiempo:** 3 h · **Datos:** todo `curso-qgis/` · **Producto:** `entrega_modulo2.zip`, comprobado desde otra ubicación.

---

## El encargo

> **Proyecto «Equipamientos y población de Cochabamba»**
>
> Debe permitir a una persona que **no conoce el proyecto**:
>
> 1. Ver dónde están los establecimientos de salud y educación y dónde vive la población.
> 2. Consultar los atributos de cualquier establecimiento.
> 3. Saber de dónde vienen los datos, en qué SRC están y qué limitaciones tienen.
> 4. Abrirlo en otra computadora **sin capas rotas**.

---

## Fase 1 · Organizar (40 min)

| Tarea | Lección |
|---|---|
| Crear `proyectos/entrega_modulo2.qgz` a partir del proyecto base, en EPSG:32719 y con rutas **relativas** | [2.3](03-gestionar-proyectos.md) |
| Incluir solo fuentes **validadas**: `equipamientos.gpkg` (de 2.5), `comunas_corregidas.gpkg` o `limites.gpkg`, `vias_principales.gpkg` (de 2.6), DEM y Sentinel-2 | [2.4](04-incorporar-datos.md)–[2.6](06-problemas-coordenadas.md) |
| Agrupar en `Tema`, `Referencia`, `Ráster` y `Mapas base`; nombres legibles; orden lógico | [2.2](02-orientarse-interfaz.md) |
| Quitar capas temporales, duplicadas o de prueba | [2.3](03-gestionar-proyectos.md) |

!!! captura "Captura pendiente · 2.12-01"

    - **Tipo:** Imagen (PNG) comparativa
    - **Archivo:** `assets/images/modulo-02/2-12/2-12-01-panel-capas.png`
    - **Qué mostrar:** A la izquierda un panel de capas desorganizado y a la derecha el mismo proyecto agrupado y renombrado.

## Fase 2 · Representar (40 min)

| Tarea | Lección |
|---|---|
| Densidad de población graduada (zonas habitadas) y equipamientos por subtipo | [2.9](09-simbologia-etiquetas.md) |
| Etiquetas de comunas; nombres de establecimientos solo a partir de 1:15 000 | [2.9](09-simbologia-etiquetas.md) |
| Sentinel-2 en color natural y DEM con sombreado, apagados por defecto | [2.10](10-explorar-raster.md) |
| Tres **temas del mapa**: *Población y servicios*, *Relieve*, *Imagen* | [2.2](02-orientarse-interfaz.md) |
| Seis marcadores del proyecto en dos grupos | [2.2](02-orientarse-interfaz.md) |

## Fase 3 · Documentar (40 min)

1. **Metadatos del proyecto** (**Proyecto ▸ Propiedades ▸ Metadatos**): título, autor, resumen, palabras clave, fecha.
2. **Metadatos de cada capa de trabajo** (**Propiedades de la capa ▸ Metadatos**): fuente, fecha, SRC, procesos aplicados y la expresión de selección si corresponde.
3. **`LEEME.txt`** en la raíz de la entrega:

    ```text
    PROYECTO: Equipamientos y población de Cochabamba
    ABRIR: proyectos/entrega_modulo2.qgz con QGIS 4.x (probado en 4.4.0)
    SRC DEL PROYECTO: EPSG:32719 (WGS 84 / UTM 19 S)
    FUENTES Y LICENCIAS:
      - Equipamientos, vías, ríos, comunas: © colaboradores de OpenStreetMap (ODbL), extracto 08-10-2026
      - Población: WorldPop 2020 (CC BY 4.0), estimación modelada
      - DEM: Copernicus GLO-30; imagen: Sentinel-2 L2A 16-07-2025
    PROCESOS:
      - equipamientos.csv importado (EPSG:4326) y reproyectado a 32719 (lección 2.5)
      - vías principales: SRC reasignado de 32719 a 32720 y reproyectado a 32719 (lección 2.6)
    LIMITACIONES CONOCIDAS:
      - 104 establecimientos sin nombre; capacidad no disponible
      - Comunas según OSM, no límites oficiales
    REQUIERE INTERNET: solo el mapa base OpenStreetMap
    ```

4. **Exporta** la vista *Población y servicios* a `salidas/vista_general.png`.

!!! captura "Captura pendiente · 2.12-03"

    - **Tipo:** Imagen (PNG)
    - **Archivo:** `assets/images/modulo-02/2-12/2-12-03-metadatos-proyecto.png`
    - **Qué mostrar:** La pestaña de metadatos de las propiedades del proyecto completada.

## Fase 4 · Comprobar y entregar (40 min)

Aplica esta lista **antes** de comprimir:

- [ ] Cada capa local apunta a un archivo **dentro** de la entrega (**Propiedades ▸ Información**).
- [ ] No hay capas temporales (ícono de memoria) ni filtros olvidados (ícono de embudo).
- [ ] Recuento de equipamientos: **661**; comunas: **6**.
- [ ] Ninguna capa aparece desplazada respecto de las demás.
- [ ] Los estilos usados están en `estilos/`.
- [ ] `LEEME.txt` y metadatos completos.

Luego:

1. Cierra QGIS y comprime la carpeta como `entrega_modulo2.zip`.
2. Extráela en **otra** ubicación (o en otra computadora).
3. Abre el proyecto **desde la extracción** y repite la lista.
4. Desconecta internet: solo debe faltar el mapa base.

!!! captura "Captura pendiente · 2.12-05"

    - **Tipo:** GIF animado
    - **Archivo:** `assets/images/modulo-02/2-12/2-12-05-prueba-portabilidad.gif`
    - **Qué mostrar:** Copiar la carpeta completa a otra ubicación, abrir el QGZ desde allí y comprobar la ruta de una capa.

---

## Evaluación del taller

| Criterio | Excelente (4) | Suficiente (2) | Insuficiente (0) |
|---|---|---|---|
| **Portabilidad** | Se abre desde la extracción sin ninguna capa rota | Una capa rota fácil de reparar | Varias capas rotas o fuentes fuera de la entrega |
| **Exactitud** | Todas las capas en su lugar; conteos correctos | Un error menor de SRC o conteo | Capas desplazadas o duplicadas |
| **Representación** | Lectura temática clara, jerarquía y escalas bien resueltas | Correcta pero recargada | Colores sin lógica o ilegible |
| **Documentación** | LEEME, metadatos y limitaciones completos | Faltan algunos elementos | Sin documentación |
| **Organización** | Grupos, nombres, temas y marcadores claros | Organización parcial | Desorden |

**Aprobación:** 12 de 20 puntos y ningún criterio en «Insuficiente».

---

## Errores frecuentes en la entrega

| Síntoma al abrir | Causa | Prevención |
|---|---|---|
| «Capas no disponibles» | Fuentes fuera de la carpeta o rutas absolutas | Revisa el origen de cada capa antes de comprimir |
| Capa vacía | Capa temporal que nunca se guardó | Hazla permanente en `datos/trabajo/` |
| Faltan entidades | Filtro activo olvidado | Revisa los embudos |
| Mapa base en blanco | Sin internet | Documenta la dependencia |
| Estilo distinto | El estilo estaba solo en tu perfil | Guarda el estilo en el proyecto o en `estilos/` |

---

## Comprueba lo aprendido

??? question "1. ¿Por qué hay que comprobar la entrega **desde otra ubicación**?"

    Porque en tu carpeta original las capas pueden estar leyendo archivos que **no** van en la entrega. Solo al abrir la copia se revelan las rutas rotas.

??? question "2. ¿Qué diferencia hay entre los metadatos del proyecto y los de cada capa?"

    Los del proyecto describen el **trabajo**; los de cada capa, la **procedencia, fecha, SRC y procesos** de esa fuente.

??? question "3. ¿Por qué incluir «limitaciones conocidas» en el LEEME?"

    Para que quien use el proyecto **no saque conclusiones** que los datos no permiten (por ejemplo, sobre capacidad hospitalaria).

??? question "4. Repaso del módulo · Ordena los pasos para incorporar una tabla de coordenadas desconocida."

    Inspeccionar el archivo → identificar delimitador, codificación y tipos → identificar X, Y y SRC de origen → importar → validar cantidad, extensión y posición → diagnosticar y documentar → exportar a GeoPackage.

---

## Lo que viene

En el **[Módulo 3](../modulo-03/index.md)** dejarás de solo mirar los datos: los corregirás, crearás nuevos y harás análisis espaciales para responder la pregunta del caso conductor: **¿dónde es peor el acceso a los servicios?**

---

## Referencias

- Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLOS Computational Biology, 13*(6), e1005510. <https://doi.org/10.1371/journal.pcbi.1005510>
- International Organization for Standardization. (2014). *ISO 19115-1:2014 Geographic information — Metadata — Part 1: Fundamentals*. ISO.
- QGIS Project. (s. f.). *Manual de usuario: Propiedades del proyecto y metadatos*. <https://docs.qgis.org/latest/es/docs/user_manual/introduction/qgis_configuration.html#project-properties>
- QGIS Project. (s. f.). *Manual de usuario: Trabajar con archivos de proyecto*. <https://docs.qgis.org/latest/es/docs/user_manual/introduction/project_files.html>
