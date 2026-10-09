---
title: Cuestionario · Módulo 4
description: Diez preguntas de autoevaluación sobre encargo, escala, representación temática, clasificación, color, jerarquía, etiquetado, composición, atlas y exportación, con repaso de módulos anteriores.
---

# Cuestionario · Módulo 4

Responde **antes** de abrir cada respuesta. Objetivo: 8 de 10. Las preguntas 9 y 10 son de **repaso**.

??? question "1. ¿Qué tres preguntas definen el encargo de un mapa?"

    **¿Para quién?**, **¿para qué?** y **¿qué mensaje?** (además del soporte, la escala y las restricciones). → [4.1](../modulo-04/01-definir-encargo-cartografico.md)

??? question "2. ¿Por qué no hacer una coropleta de la población total por comuna?"

    Porque el color de un área se lee como intensidad y las áreas grandes dominan: hay que **normalizar** (densidad, %) o usar **símbolos proporcionales**. → [4.3](../modulo-04/03-elegir-representacion-tematica.md)

??? question "3. ¿Qué método de clasificación exagera diferencias pequeñas en datos sesgados?"

    **Cuantiles**: obliga a repartir las entidades por igual entre las clases. → [4.4](../modulo-04/04-evaluar-clasificaciones-colores.md)

??? question "4. ¿Cuándo usar una paleta divergente?"

    Cuando hay un **centro con significado** (cero, la media, una meta) y valores por encima y por debajo. → [4.4](../modulo-04/04-evaluar-clasificaciones-colores.md)

??? question "5. ¿Qué hace la «prueba de entrecerrar los ojos»?"

    Revela qué ve primero el lector: debería ser la **figura** (el mensaje). → [4.5](../modulo-04/05-construir-jerarquia-visual.md)

??? question "6. ¿Qué diferencia hay entre un búfer de etiqueta y una máscara?"

    El búfer tapa **todo** lo que hay debajo; la máscara oculta solo las capas que elijas. → [4.6](../modulo-04/06-resolver-etiquetado-mapas-complejos.md)

??? question "7. ¿Para qué sirve una vista general (*overview*) en el diseñador?"

    Para mostrar en un mapa (el localizador) el **marco** de la extensión de otro mapa de la composición. → [4.8](../modulo-04/08-coordinar-mapas-elementos-complementarios.md)

??? question "8. ¿Cómo obtienes en un atlas el nombre de la entidad actual?"

    `attribute(@atlas_feature, 'nombre')` (o el campo directamente si el texto toma la capa de cobertura). → [4.10](../modulo-04/10-producir-atlas-territorial.md)

??? question "9. Repaso · ¿Qué tolerancia de simplificación usarías para la lámina municipal a 1:100 000?"

    ≈ 0,2 mm × 100 000 = **20 m**. → [4.2](../modulo-04/02-preparar-informacion-escala-salida.md) · [1.10](../modulo-01/10-generalizacion-cartografica.md)

??? question "10. Repaso · ¿Por qué redondear «90 073 personas» a «unas 90 000» en la lámina del Concejo?"

    Porque la población es una **estimación**: mostrar unidades exactas comunica una precisión inexistente. → [4.9](../modulo-04/09-incorporar-informacion-dinamica.md) · [1.9](../modulo-01/09-escala-resolucion-precision.md)
