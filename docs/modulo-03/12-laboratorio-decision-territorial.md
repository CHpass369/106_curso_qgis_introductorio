---
title: 3.12 Laboratorio · Justificar una decisión territorial
description: Laboratorio integrador para formular, analizar, validar y justificar una decisión territorial mediante datos vectoriales y ráster, indicadores, relaciones espaciales y procedimientos reproducibles en QGIS.
---

# 3.12 Laboratorio · Justificar una decisión territorial

El Gobierno Municipal tiene presupuesto para **un** nuevo centro de salud de primer nivel. La pregunta es tuya: **¿dónde?** No basta con señalar un punto en el mapa. Tienes que mostrar qué criterios usaste, de dónde salen los datos, qué zonas descartaste y por qué, y qué pasaría si los criterios cambiaran. Este laboratorio integra todo el Módulo 3 en una **decisión defendible**.

!!! abstract "En este laboratorio"

    **Integrarás:** auditoría (3.1), digitalización (3.2), indicadores (3.4), uniones y relaciones (3.5–3.6), proximidad (3.7), ráster y relieve (3.8–3.9) y modelos (3.11).

    **Tiempo:** 4 h · **Datos:** todo el paquete y tus capas de `datos/trabajo/` · **Producto:** `datos/trabajo/decision_salud.gpkg`, un mapa de candidatas y una **memoria técnica** de 2 páginas.

---

## Idea central

### Criterio, indicador, regla

| Nivel | Ejemplo |
|---|---|
| **Criterio** (qué importa) | La población debe estar lejos de los servicios actuales |
| **Indicador** (cómo se mide) | Distancia del centro de la zona al establecimiento de salud más cercano |
| **Regla** (cómo se decide) | Más de 1 000 m → zona elegible |

### Restricciones y criterios

| Tipo | Funciona como | Ejemplo |
|---|---|---|
| **Restricción** (absoluta) | Filtro: sí o no | Pendiente media ≥ 15 % → descartada |
| **Criterio** (relativo) | Puntaje: más o menos | Más población → mejor |

### Del dato a la preferencia

Un **índice compuesto** suma criterios normalizados con **pesos**. Los datos son objetivos; **los pesos no**: expresan prioridades. Por eso deben ser explícitos y someterse a un **análisis de sensibilidad**.

!!! danger "Un índice no crea objetividad"

    Si cambiando los pesos cambia la zona ganadora, el resultado **depende de una decisión política**, no solo técnica. Tu trabajo es mostrarlo con claridad, no ocultarlo.

---

## El procedimiento

### Fase 1 · Matriz metodológica (30 min)

Antes de abrir QGIS, completa:

| Criterio | Tipo | Indicador | Fuente | Regla o normalización | Lección |
|---|---|---|---|---|---|
| Sin cobertura actual | Restricción | Punto interior a > 1 000 m de un establecimiento de salud | equipamientos auditado | Elegible si se cumple | 3.7 |
| Demanda | Restricción + criterio | Densidad y población de la zona | zonas_analisis (WorldPop) | Densidad ≥ 3 000 hab./km²; más población = mejor | 3.4 |
| Terreno | Restricción + criterio | Pendiente media | DEM en UTM | < 15 %; menos pendiente = mejor | 3.9 |
| Acceso | Restricción + criterio | Distancia a vía troncal o principal | vias.gpkg | Zona a ≤ 500 m; más cerca = mejor | 3.6–3.7 |
| Lejanía del servicio actual | Criterio | Distancia al establecimiento más cercano | equipamientos | Más lejos = más necesidad | 3.7 |

### Fase 2 · Preparar (45 min)

1. Crea `decision_salud.gpkg` y copia las capas de trabajo validadas.
2. Comprueba SRC (EPSG:32719), conteos y calidad (usa tu informe de 3.1).
3. Calcula en `zonas` los campos: `cubierta` (3.7), `densidad` (3.4), `pendiente_media` (3.9), `dist_salud_m` y `dist_via_m`, y crea la capa `vias_principales_500m`.

!!! tip "Distancias desde un punto interior"

    ```sql
    -- distancia al establecimiento de salud más cercano
    distance(point_on_surface($geometry),
             array_first(overlay_nearest('equipamientos_salud', $geometry)))
    ```

    Más simple: **Procesos ▸ Distancia al centro más cercano (línea al centro)** desde los puntos interiores de las zonas hacia los establecimientos.

### Fase 3 · Aplicar restricciones (45 min)

Selecciona las zonas que cumplen **todas** las restricciones:

```sql
"pob_2020" > 0
AND NOT "cubierta"
AND "pob_2020" / ($area / 1000000) >= 3000
AND "pendiente_media" < 15
AND overlay_intersects('vias_principales_500m')
```

`vias_principales_500m` es un buffer **disuelto** de 500 m alrededor de las vías troncales y principales (3.7).

Resultado esperado: **6 zonas candidatas**.

| Zona | Comuna | Población | Pendiente media | Distancia a salud | Distancia a vía principal* |
|---|---|---|---|---|---|
| Z156 | Itocta | 5 238 | 2,2 % | 1 177 m | 101 m |
| Z306 | Alejo Calatayud | 4 905 | 10,9 % | 1 033 m | 967 m |
| Z158 | Alejo Calatayud | 4 496 | 1,5 % | 1 010 m | 200 m |
| Z123 | Tunari | 3 535 | 10,3 % | 1 371 m | 641 m |
| Z206 | Itocta | 3 200 | 3,5 % | 1 019 m | 305 m |
| Z266 | Tunari | 1 696 | 14,9 % | 1 251 m | 827 m |

<small>* Distancia desde el punto interior; la restricción se aplicó a la **zona**, que basta con que toque la franja de 500 m.</small>

!!! captura "Captura pendiente · 3.12-05"

    - **Tipo:** PNG
    - **Archivo:** `assets/images/modulo-03/3-12/3-12-05-candidatas.png`
    - **Qué mostrar:** Mapa de las seis zonas candidatas sobre las zonas sin cobertura, la red vial principal y el sombreado.

### Fase 4 · Índice compuesto (45 min)

1. **Normaliza** cada criterio entre 0 y 1 dentro de las candidatas:
    - Beneficio (más es mejor): `("x" - minimum("x")) / (maximum("x") - minimum("x"))`
    - Costo (menos es mejor): `1 - (…)`
2. **Pondera** y suma. Ejemplo con pesos población 0,40 · lejanía 0,30 · pendiente 0,15 · acceso 0,15:

| Pesos (pob · lejanía · pendiente · acceso) | 1.º | 2.º | 3.º |
|---|---|---|---|
| 0,40 · 0,30 · 0,15 · 0,15 | **Z156** (0,83) | Z123 (0,62) | Z158 (0,60) |
| 0,25 · 0,25 · 0,25 · 0,25 | **Z156** (0,85) | Z158 (0,67) | Z123 (0,56) |
| 0,20 · 0,60 · 0,10 · 0,10 | **Z123** (0,78) | Z156 (0,67) | Z266 (0,42) |

!!! example "Lo que muestra la sensibilidad"

    **Z156** (Itocta) gana con pesos equilibrados o centrados en la población: es la zona más poblada, plana y junto a una vía principal. Pero si se prioriza la **lejanía** del servicio actual, gana **Z123** (Tunari). La recomendación debe decir ambas cosas.

### Fase 5 · Validar (30 min)

- Mira Z156 y Z123 sobre **Sentinel-2** y el mapa base: ¿hay terreno libre? ¿Es zona residencial?
- Revisa los datos de entrada en esas zonas: ¿algún establecimiento omitido en OSM? (Busca en el mapa base o en fuentes del SEDES.)
- Documenta lo que **no** pudiste verificar.

### Fase 6 · Comunicar (45 min)

**Memoria técnica (2 páginas):**

1. Pregunta y contexto.
2. Datos y calidad (con limitaciones).
3. Método: matriz, restricciones, normalización, pesos (con el modelo `.model3` de 3.11 si lo usaste).
4. Resultados: mapa de candidatas, tabla y ranking.
5. **Sensibilidad**: qué cambia con otros pesos.
6. Recomendación y próximos pasos (verificación en terreno, consulta a la comunidad, análisis de red vial).

---

## Evaluación

| Criterio | Excelente (4) | Suficiente (2) | Insuficiente (0) |
|---|---|---|---|
| **Formulación** | Criterios, indicadores y reglas explícitos y justificados | Explícitos pero poco justificados | Implícitos |
| **Datos y calidad** | Fuentes, SRC y limitaciones documentadas | Parcial | Sin documentar |
| **Análisis** | Restricciones y criterios correctos; 6 candidatas | Errores menores | Errores que cambian el resultado |
| **Sensibilidad** | Al menos 3 escenarios de pesos, interpretados | Un solo escenario alternativo | Sin sensibilidad |
| **Reproducibilidad** | Modelo o pasos que otro puede repetir | Pasos incompletos | No reproducible |
| **Comunicación** | Mapa claro y memoria concisa con recomendación honesta | Comprensible | Confusa |

**Aprobación:** 14 de 24 puntos y ningún criterio en «Insuficiente».

---

## Comprueba lo aprendido

??? question "1. ¿Qué diferencia hay entre una restricción y un criterio?"

    La restricción **excluye** (sí/no); el criterio **ordena** (más/menos).

??? question "2. ¿Por qué normalizar antes de sumar criterios?"

    Porque están en unidades distintas (habitantes, metros, porcentaje): sin normalizar, el de números más grandes dominaría.

??? question "3. Si cambiar los pesos cambia la zona ganadora, ¿el análisis falló?"

    No. Revela que la decisión depende de **prioridades** que deben discutirse abiertamente.

??? question "4. ¿Qué limitaciones de los datos podrían invalidar la recomendación?"

    Establecimientos omitidos en OSM, población modelada (WorldPop), distancia en línea recta en lugar de por calles, y la falta de datos sobre tamaño y tipo de cada servicio.

??? question "5. Repaso del módulo · Ordena: indicadores, auditoría, proximidad, restricciones, sensibilidad."

    Auditoría → indicadores → proximidad → restricciones → índice → sensibilidad.

---

## Lo que viene

En el **[Módulo 4](../modulo-04/index.md)** convertirás este resultado en mapas que un concejo municipal pueda entender en dos minutos: encargo, clasificación honesta, jerarquía visual, composición y un atlas por comuna.

---

## Referencias

- Malczewski, J., & Rinner, C. (2015). *Multicriteria Decision Analysis in Geographic Information Science*. Springer. <https://doi.org/10.1007/978-3-540-74757-4>
- Eastman, J. R. (1999). Multi-criteria evaluation and GIS. En P. A. Longley, M. F. Goodchild, D. J. Maguire & D. W. Rhind (Eds.), *Geographical Information Systems* (2.ª ed., pp. 493–502). Wiley.
- Higgs, G. (2004). A literature review of the use of GIS-based measures of access to health care services. *Health Services and Outcomes Research Methodology, 5*(2), 119–139. <https://doi.org/10.1007/s10742-005-4304-7>
- QGIS Project. (s. f.). *Manual de usuario: Procesos*. <https://docs.qgis.org/latest/es/docs/user_manual/processing/index.html>
