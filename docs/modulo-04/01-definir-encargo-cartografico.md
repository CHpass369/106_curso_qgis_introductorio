---
title: 4.1 Definir el encargo cartográfico
description: Definición del destinatario, propósito, mensaje, soporte, escala y restricciones de un producto cartográfico antes de iniciar su diseño en QGIS.
---

# 4.1 Definir el encargo cartográfico

El análisis del Módulo 3 está listo: unas 90 000 personas viven lejos de un establecimiento de salud. Ahora dos personas te piden «un mapa». La **concejala** quiere algo que entienda en dos minutos en la sesión del jueves. La **jefa de la red de salud** quiere saber, comuna por comuna, qué zonas atender. Es el mismo dato… y **dos mapas completamente distintos**. Antes de abrir el diseñador de impresión, hay que definir el **encargo**.

!!! abstract "En esta lección"

    **Aprenderás a:**

    - Identificar **destinatario**, **propósito** y **mensaje** de un mapa.
    - Elegir **soporte**, **formato** y **escala** de salida.
    - Reconocer las **restricciones** (tiempo, datos, impresión, accesibilidad).
    - Redactar un **brief cartográfico** y usarlo para evaluar el resultado.

    **Tiempo:** 60 min (20 de lectura · 40 de práctica) · **Datos:** resultados de [3.7](../modulo-03/07-proximidad-superposicion.md) y [3.12](../modulo-03/12-laboratorio-decision-territorial.md) · **Producto:** dos briefs en `documentos/`.

---

## Idea central

### Un mapa responde a alguien

| Pregunta del encargo | Por qué importa |
|---|---|
| **¿Para quién?** | Define el vocabulario, el nivel de detalle y lo que se puede dar por sabido |
| **¿Para qué?** | Informar, convencer, decidir, consultar, archivar |
| **¿Qué mensaje?** | Una frase que el lector debe recordar al mirar el mapa |
| **¿Dónde se verá?** | Papel A4, proyector, celular, informe PDF |
| **¿A qué escala?** | Qué cabe y qué se puede leer |
| **¿Con qué restricciones?** | Plazo, datos disponibles, impresión en blanco y negro, daltonismo |

!!! danger "El mapa que lo muestra todo no comunica nada"

    Si no puedes escribir el **mensaje** en una frase, el mapa tendrá demasiadas capas y ninguna jerarquía. El encargo decide **qué se deja fuera**.

### Tipos de propósito

| Propósito | El lector… | Diseño típico |
|---|---|---|
| **Comunicar** un hallazgo | Mira 30 segundos | Un tema, títulos que afirman, pocas clases |
| **Analizar** | Explora y compara | Más variables, leyendas detalladas |
| **Consultar** | Busca un lugar concreto | Índices, nombres, atlas por unidad |
| **Registrar** | Archiva o usa como prueba | Metadatos completos, fecha, fuente, escala exacta |

### Título que afirma frente a título que describe

| Título descriptivo | Título que comunica el mensaje |
|---|---|
| «Cobertura de establecimientos de salud» | «90 000 personas viven a más de 1 km de un establecimiento de salud» |
| «Densidad de población por zona» | «La población se concentra al norte del río Rocha» |

Ambos son válidos: el primero para un **atlas de consulta**; el segundo para una **presentación de decisión**.

---

## Hazlo conmigo

### Un mismo territorio, dos públicos

| Elemento | Encargo A · Concejo Municipal | Encargo B · Red de salud |
|---|---|---|
| **Destinatario** | Concejales, sin formación técnica | Equipo técnico de salud |
| **Propósito** | Decidir dónde invertir | Planificar visitas y servicios por comuna |
| **Mensaje** | «Itocta concentra más de la mitad de la población sin cobertura» | «Estas son las zonas sin cobertura de tu comuna» |
| **Soporte** | Impreso A4 horizontal + proyector | PDF de 6 páginas, una por comuna |
| **Escala** | ≈ 1:100 000 (todo el municipio) | ≈ 1:25 000–1:60 000 (cada comuna) |
| **Contenido** | Zonas sin cobertura, comunas, establecimientos | Lo anterior + vías, nombres, indicadores por comuna |
| **Restricciones** | Impresión en blanco y negro posible; 2 minutos de atención | Debe actualizarse cada año |
| **Producto** | Lámina ([4.7](07-disenar-composicion-reutilizable.md)) | Atlas ([4.10](10-producir-atlas-territorial.md)) |

![Resultado del encargo A: lámina A4 para el Concejo](../assets/images/mapas/4-7-composicion-a4.png){ loading=lazy }

### Redactar el brief

Crea `documentos/brief_concejo.md` con esta plantilla:

```text
BRIEF CARTOGRÁFICO
Encargo: 
Destinatario (quién, qué sabe, cuánto tiempo mirará):
Propósito (informar / decidir / consultar / registrar):
Mensaje principal (una frase):
Mensajes secundarios (máximo dos):
Soporte y formato (papel, pantalla, tamaño, orientación):
Escala o extensión:
Datos (capas, fecha, fuente):
Elementos obligatorios (título, leyenda, escala, norte, fuentes, fecha):
Restricciones (color, impresión, accesibilidad, plazo):
Cómo sabré que funcionó (prueba con un lector):
```

!!! tip "La prueba de los 30 segundos"

    Muestra el mapa a alguien que no participó del trabajo durante 30 segundos y pídele que diga qué entendió. Si no coincide con tu mensaje, el diseño (no el lector) tiene que cambiar.

---

## Inténtalo tú

!!! example "Reto 4.1 · Dos briefs, dos bocetos"

    1. Completa el brief del **encargo B** (red de salud).
    2. Para cada encargo, dibuja a mano (o en una diapositiva) un **boceto** de la página: dónde va el mapa, el título, la leyenda, los textos.
    3. Escribe tres diferencias concretas de diseño entre ambos productos y justifícalas con el brief.

---

## ¿Lo hiciste bien?

| Criterio | Se cumple si… |
|---|---|
| Mensaje | Cada brief tiene un mensaje en **una** frase |
| Coherencia | Soporte, escala y contenido son consistentes con el destinatario |
| Selección | El brief dice explícitamente qué **no** se incluirá |
| Evaluación | Define cómo comprobar que el mapa funciona |
| Bocetos | Muestran jerarquía: lo importante ocupa más espacio |

### Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| El mapa tiene diez capas encendidas | No hay mensaje definido | Escribe el mensaje y elimina lo que no lo apoya |
| La concejala pregunta «¿qué es una zona de análisis?» | Vocabulario técnico | Explica o reemplaza términos en la leyenda |
| El mapa impreso es ilegible | Diseñado para pantalla | Define el soporte antes de diseñar |
| Nadie sabe de cuándo son los datos | Falta fecha y fuente | Inclúyelas siempre |

---

## Comprueba lo aprendido

??? question "1. ¿Por qué el mismo análisis necesita dos mapas distintos?"

    Porque cambian el **destinatario**, el **propósito** y el **soporte**, y con ellos el mensaje, la escala y el contenido.

??? question "2. ¿Cuándo conviene un título que afirma un hallazgo?"

    Cuando el propósito es **comunicar** o **decidir** y el lector tiene poco tiempo.

??? question "3. ¿Qué elementos debe tener casi cualquier mapa?"

    Título, leyenda, escala, fuente de los datos, fecha y, cuando la orientación no es obvia, indicación del norte.

??? question "4. Repaso de 1.7 · ¿Qué significa que un mapa sea un modelo y un lenguaje?"

    Que **simplifica** la realidad según un propósito (modelo) y **comunica** mediante signos con reglas (lenguaje).

---

## Tu proyecto

Los dos briefs guían todo el módulo: cada lección te pedirá revisar si tus decisiones de diseño responden a ellos. Guárdalos en `documentos/` y actualízalos si el encargo cambia.

---

## Referencias

- Kraak, M.-J., & Ormeling, F. (2020). *Cartography: Visualization of Geospatial Data* (4.ª ed., cap. 1–2). CRC Press.
- Krygier, J., & Wood, D. (2016). *Making Maps: A Visual Guide to Map Design for GIS* (3.ª ed.). Guilford Press.
- Tyner, J. A. (2010). *Principles of Map Design*. Guilford Press.
- Field, K. (2018). *Cartography.* Esri Press.
