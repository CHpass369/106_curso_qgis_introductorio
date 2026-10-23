# Guía para contribuir y guía de estilo

Este documento define **cómo se escribe y se estructura** el material del Curso Introductorio de QGIS. Toda lección nueva o revisada debe cumplirlo.

## 1. Flujo de trabajo

1. Crea una rama desde `main`.
2. Edita los archivos en `docs/`.
3. Comprueba localmente:

    ```bash
    pip install -r requirements.txt
    mkdocs serve          # vista previa en http://127.0.0.1:8000
    mkdocs build --strict # debe terminar sin advertencias
    python scripts/revisar_contenido.py   # métricas de estilo
    python -m unittest discover -s scripts -p "test_*.py"
    ```

4. Abre un *pull request*. La integración continua ejecuta `mkdocs build --strict`.

Cuando cambies un marcador `!!! captura` o `TODO-MANUAL`, regenera el inventario con `python scripts/listar_pendientes.py`. Revisa y guarda también el cambio en `PENDIENTES.md`; ese archivo se genera, no se edita a mano.

## 2. Plantilla de lección

Cada lección sigue esta secuencia. Los nombres de las secciones `##` son fijos para que el estudiante sepa siempre dónde está.

```markdown
---
title: X.Y Título orientado a la acción
description: Una oración que resume la lección.
---

# X.Y Título

Gancho: una pregunta o situación real (2–4 líneas) y, si existe, la imagen del resultado.

!!! abstract "En esta lección"
    **Aprenderás a:** 3–5 objetivos con verbos observables.
    **Tiempo:** NN min · **Datos:** archivos del paquete · **Producto:** qué obtendrás.

## Idea central          ← conceptos imprescindibles, con figura o tabla
## Hazlo conmigo         ← laboratorio guiado: pasos numerados, una acción por paso
## Inténtalo tú          ← reto autónomo sobre otro caso o variante
## ¿Lo hiciste bien?     ← cómo verificar el resultado + errores frecuentes
## Comprueba lo aprendido ← 4–8 preguntas con respuesta desplegable (??? question)
## Tu proyecto           ← aplicación al caso conductor o al proyecto propio
## Referencias           ← ver sección 6
```

- **Máximo ~15 secciones `##`** por lección. Usa `###` para subtemas.
- **No numeres** los encabezados (`## 23. …`): la numeración la da la navegación.
- El contenido avanzado, histórico u opcional va en desplegables `??? info "Para saber más"`.
- Lecciones del Módulo 1 (sin software): *Hazlo conmigo* es un ejercicio resuelto a mano y *Inténtalo tú* un ejercicio equivalente.

## 3. Estilo de redacción

| Regla | Correcto | Incorrecto |
|---|---|---|
| Trato | Tú: «Abre la tabla de atributos» | Usted / impersonal excesivo |
| Prosa, no bloques de código | «Puede cambiar la variable, los datos o la geometría.» | Frases sueltas dentro de ` ```text ` |
| Bloques de código **solo** para | expresiones QGIS, SQL, Python, rutas, contenido literal de archivos, árboles de carpetas | ideas, listas de conceptos, títulos |
| Menús | **Capa ▸ Añadir capa ▸ Añadir capa vectorial** | Capa > Añadir… / Capa -> … |
| Botones y campos | En **negrita**, tal como aparecen en la interfaz en español | Entre comillas |
| Teclas | ++ctrl+s++ | Ctrl+S en texto plano |
| Números | 1 250,5 m (coma decimal, espacio de miles) en prosa; `1250.5` en expresiones | Mezclar formatos |
| Unidades | Espacio entre número y unidad: 30 m, 15 %, 1:50 000 | 30m, 15% |
| Párrafos | 2–5 líneas. Una idea por párrafo | Frases de una línea encadenadas |

## 4. Terminología unificada

Usa siempre el término de la izquierda. El [glosario](docs/glosario.md) es la referencia.

| Usar | En lugar de | Nota |
|---|---|---|
| **SRC** (sistema de referencia de coordenadas) | CRS | Es el término de la interfaz de QGIS en español. Mencionar «CRS» una vez como equivalente inglés |
| **ráster** | raster | Con tilde, invariable en plural: «los ráster» |
| **GeoPackage** | geopackage, GPKG (en prosa) | La extensión es `.gpkg` |
| **capa vectorial** | capa vector | |
| **tabla de atributos** | tabla de datos | |
| **composición de impresión** / **diseñador de impresión** | layout, maquetador | |
| **complemento** | plugin | Mencionar «plugin» una vez |
| **Procesos** / **caja de herramientas de Procesos** | Processing, toolbox | Nombre de la interfaz en español |
| **NULL** | nulo, null | En código; en prosa «valor nulo (`NULL`)» |
| **entidad** | objeto, feature, elemento (para filas de una capa) | |

## 5. Componentes de Material for MkDocs

| Uso | Componente |
|---|---|
| Definición formal | `!!! info "Definición"` |
| Consejo práctico | `!!! tip` |
| Ejemplo o cálculo resuelto | `!!! example` |
| Error frecuente | `!!! warning` |
| Error grave o idea fundamental | `!!! danger` |
| Pregunta de autoevaluación | `??? question "N. Pregunta"` (respuesta dentro) |
| Contenido opcional | `??? info "Para saber más"` |
| Comparar alternativas | Pestañas `=== "Opción"` |
| Diagrama | Mermaid **sin colores fijos** (el tema del sitio los adapta a modo claro y oscuro) |

### Imágenes

- Carpeta: `docs/assets/images/modulo-0N/<leccion>/`, nombre `N-M-NN-descripcion.png` (o `.webp`, `.gif`, `.svg`).
- Capturas en QGIS 4.x, **tema claro**, interfaz en español, 1600 px de ancho máximo, recortadas a lo relevante.
- Siempre con texto alternativo descriptivo: `![Panel Capas con tres capas ordenadas](...)`.
- Mientras la captura no exista, deja la especificación en un recuadro `!!! captura "Captura pendiente · N.M-NN"`. Estos recuadros **no se muestran** en el sitio publicado y se listan en `PENDIENTES.md` (`python scripts/listar_pendientes.py`).
- Otras tareas manuales: comentario `<!-- TODO-MANUAL[tipo]: descripción -->`.

## 6. Referencias

- Formato **APA 7**. Cada lección incluye al menos:
    1. una fuente **académica** (libro o artículo),
    2. una fuente **oficial** (manual de QGIS, norma ISO, organismo cartográfico),
    3. la fuente de los **datos** usados.
- Enlaces a la documentación de QGIS mediante `https://docs.qgis.org/latest/es/…` (se actualiza sola con la versión vigente).
- No citar la documentación de Material for MkDocs en las lecciones: no es material para el estudiante.
- La [bibliografía general](docs/bibliografia.md) reúne las obras citadas en todo el curso.

## 7. Versiones

La información sobre versiones de QGIS vive **en un solo lugar**: `snippets/version-qgis.md`, incluido con `--8<-- "snippets/version-qgis.md"`. Actualízala allí.

## 8. Licencia

Al contribuir aceptas publicar tu aporte bajo **CC BY-SA 4.0** (ver `LICENSE`).
