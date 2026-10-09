---
title: Cuestionario · Módulo 2
description: Diez preguntas de autoevaluación sobre proyectos, formatos, coordenadas, selección, simbología, ráster y servicios web en QGIS, con repaso del Módulo 1.
---

# Cuestionario · Módulo 2

Responde **antes** de abrir cada respuesta. Objetivo: 8 de 10. Las preguntas 9 y 10 son de **repaso** del Módulo 1.

??? question "1. Envías solo el `.qgz` a un colega y ve «capas no disponibles». ¿Por qué?"

    Porque el proyecto guarda **referencias** a los datos, no los datos. Hay que enviar la carpeta completa con rutas relativas. → [2.3](../modulo-02/03-gestionar-proyectos.md)

??? question "2. ¿Qué archivos mínimos necesita un Shapefile?"

    `.shp` (geometría), `.shx` (índice) y `.dbf` (atributos); conviene también `.prj` (SRC) y `.cpg` (codificación). → [2.4](../modulo-02/04-incorporar-datos.md)

??? question "3. Importas un CSV y todos los puntos aparecen frente a la Antártida. ¿Qué revisas primero?"

    Si elegiste **X = latitud, Y = longitud** (intercambiadas) en la importación. Si fueran solo **algunos** puntos, el error estaría en esas filas. → [2.5](../modulo-02/05-tablas-coordenadas.md)

??? question "4. Una capa declara EPSG:32719 pero aparece 650 km al oeste. ¿Asignas o reproyectas?"

    Primero **asignas** el SRC correcto (probablemente 32720, según sus coordenadas) y, si la quieres en 32719, **reproyectas** después. → [2.6](../modulo-02/06-problemas-coordenadas.md)

??? question "5. ¿Por qué `\"capacidad\" IS NULL` no encuentra las celdas que dicen `S/D`?"

    Porque `S/D` es un **texto**, no la ausencia de valor. Hay que buscarlo explícitamente o normalizarlo a `NULL`. → [2.7](../modulo-02/07-leer-datos.md)

??? question "6. ¿Qué diferencia hay entre filtrar una capa y seleccionar entidades?"

    Seleccionar **marca** sin ocultar; filtrar **oculta** lo que no cumple la condición y afecta a todo lo que se haga con la capa. → [2.8](../modulo-02/08-seleccionar-filtrar.md)

??? question "7. ¿Qué simbología usarías para la densidad de población por zona?"

    **Graduada** con una paleta **secuencial** de claro a oscuro. → [2.9](../modulo-02/09-simbologia-etiquetas.md)

??? question "8. ¿Por qué la vegetación aparece roja en la composición 4-3-2 de Sentinel-2?"

    Porque refleja mucho **infrarrojo cercano** (banda 8 → banda 4 del archivo del curso), que se asigna al canal rojo de la pantalla. → [2.10](../modulo-02/10-explorar-raster.md)

??? question "9. Repaso · ¿Cuántos metros es 0,0001° de latitud en Cochabamba?"

    ≈ **11 m**. → [1.3](../modulo-01/03-fundamentos-geodesia.md)

??? question "10. Repaso · ¿Por qué un WMS de límites municipales no sirve para calcular superficies?"

    Porque entrega una **imagen**: no hay geometrías vectoriales que medir (modelo ráster de una representación, no el dato). → [2.11](../modulo-02/11-servicios-web.md) · [1.11](../modulo-01/11-modelos-representacion.md)
