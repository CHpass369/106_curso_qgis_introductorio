---
title: Cuestionario · Módulo 1
description: Diez preguntas de autoevaluación sobre fundamentos de SIG, geodesia, sistemas de referencia, UTM, escala, precisión y calidad.
---

# Cuestionario · Módulo 1

Responde en tu cuaderno **antes** de abrir cada respuesta. Objetivo: 8 de 10.

??? question "1. Un registro dice «Hospital Viedma, X = 802 110, Y = 8 075 114». ¿Es una ubicación completa?"

    **No.** Faltan el **sistema de referencia** y su datum. Los valores sugieren UTM 19 S, pero sin declararlo podrían ser PSAD56 / UTM 19 S (≈ 400 m de diferencia) u otro sistema. → [1.4](../modulo-01/04-sistemas-referencia.md)

??? question "2. ¿Qué diferencia hay entre altura elipsoidal y altura ortométrica?"

    La **elipsoidal** (*h*) se mide sobre el elipsoide (la da el GNSS); la **ortométrica** (*H*) sobre el geoide (≈ nivel del mar). Se relacionan con la ondulación del geoide: *h* = *H* + *N*. → [1.3](../modulo-01/03-fundamentos-geodesia.md)

??? question "3. ¿En qué zona UTM está Sucre (longitud −65,26°)? ¿Cuál es su meridiano central?"

    Zona **20 S**; meridiano central **63° O**. (−65,26 + 180) / 6 = 19,12 → 19 + 1 = 20. → [1.6](../modulo-01/06-sistema-utm.md)

??? question "4. ¿Por qué no se deben medir superficies en EPSG:3857?"

    Porque Pseudo-Mercator **no es equivalente**: agranda las áreas con la latitud (≈ 10 % en Cochabamba, mucho más lejos del ecuador). → [1.5](../modulo-01/05-proyecciones-cartograficas.md)

??? question "5. En un mapa 1:25 000 mides 6 cm. ¿Cuánto es en el terreno?"

    6 × 25 000 = 150 000 cm = **1,5 km**. → [1.8](../modulo-01/08-escala-cartografica.md)

??? question "6. ¿Qué escala es mayor: 1:10 000 o 1:100 000? ¿Cuál muestra más detalle?"

    **1:10 000** es la escala mayor (la fracción es más grande) y muestra **más detalle** en un área menor. → [1.8](../modulo-01/08-escala-cartografica.md)

??? question "7. Una coordenada tiene 9 decimales y fue tomada con un celular. ¿Es muy exacta?"

    No. Los decimales expresan **precisión numérica**; la **exactitud** del celular es de varios metros. Es **falsa precisión**. → [1.9](../modulo-01/09-escala-resolucion-precision.md)

??? question "8. ¿Qué tolerancia de simplificación es razonable para un mapa 1:50 000?"

    ≈ 0,2 mm × 50 000 = **10 m**. → [1.10](../modulo-01/10-generalizacion-cartografica.md)

??? question "9. ¿Qué modelo usarías para la pendiente del terreno y cuál para los medidores de agua?"

    Pendiente: **ráster** (fenómeno continuo). Medidores: **vectorial de puntos** (objetos discretos). → [1.11](../modulo-01/11-modelos-representacion.md)

??? question "10. Tres capas con 90 % de exactitud temática se combinan. ¿Qué exactitud cabe esperar?"

    0,9³ ≈ **73 %**, si los errores son independientes: combinar capas **reduce** la exactitud. → [1.13](../modulo-01/13-calidad-informacion.md)
