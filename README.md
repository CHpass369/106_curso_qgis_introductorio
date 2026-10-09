# Curso Introductorio de QGIS

Documentación del **Curso Introductorio de QGIS**: fundamentos de SIG, manejo de QGIS 4.x, análisis espacial y diseño cartográfico, con un caso conductor real (acceso a servicios de salud y educación en **Cochabamba, Bolivia**).

Sitio publicado: <https://chpass369.github.io/106_curso_qgis_introductorio/>

## Estructura

```text
docs/                     contenido del sitio (MkDocs + Material)
├── modulo-01 … modulo-04 lecciones
├── practicas/, evaluaciones/, descargas/
└── assets/images/mapas/  mapas generados con scripts/
snippets/                 fragmentos reutilizables (versión de QGIS)
scripts/                  construcción del paquete de datos, figuras, soluciones y métricas
CONTRIBUTING.md           guía de estilo y plantilla de lección
PENDIENTES.md             tareas manuales pendientes (capturas, videos…)
PLAN_MEJORA_CONTENIDO.md  diagnóstico y plan de mejora
```

## Vista previa local

```bash
pip install -r requirements.txt
mkdocs serve
```

## Paquete de datos y figuras

El paquete `docs/descargas/curso-qgis-cochabamba.zip` y los mapas de `docs/assets/images/mapas/` se generan con QGIS 4.x a partir de OpenStreetMap, Copernicus y WorldPop. Las instrucciones están en la página [Descargas](docs/descargas/index.md).

## Licencia

Contenido: [CC BY-SA 4.0](LICENSE). Los datos conservan la licencia de su fuente (OpenStreetMap: ODbL).
