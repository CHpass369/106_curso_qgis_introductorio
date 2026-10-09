# Paquete de datos · Curso Introductorio de QGIS

Caso conductor: **acceso a servicios de salud y educación en el municipio de Cochabamba (Bolivia)**.

## Estructura

```text
curso-qgis/
├── datos/
│   ├── originales/   ← datos tal como se recibieron (ver originales/LEEME.md)
│   ├── ejercicios/   ← datos con errores intencionales para practicar diagnósticos
│   └── trabajo/      ← aquí guardas tus copias y resultados intermedios
├── proyectos/        ← curso_qgis_base.qgz (rutas relativas) y tus proyectos
├── estilos/          ← estilos .qml listos para reutilizar
├── salidas/          ← mapas y tablas exportados
└── documentos/       ← ficha del entorno, notas, metadatos
```

## Cómo empezar

1. Descomprime esta carpeta en una ubicación **local y corta** (por ejemplo `C:\curso-qgis\`), **fuera** de OneDrive, Google Drive o Dropbox.
2. Abre `proyectos/curso_qgis_base.qgz` con QGIS 4.x.
3. Sigue la lección 2.1 del curso.

## Datos de ejercicios

| Archivo | Problema intencional | Lección |
|---|---|---|
| `equipamientos_errores.csv` | Codificación Latin-1, coordenadas intercambiadas, valores `S/D`, filas duplicadas, tipos inconsistentes | 2.5, 2.7 |
| `comunas_sin_prj.shp` | Shapefile sin archivo `.prj`: SRC desconocido | 2.6 |
| `vias_principales_src_erroneo.gpkg` | Coordenadas en UTM 20 S declaradas como UTM 19 S | 2.6 |
| `poblacion_comunas_claves.csv` | Claves con formatos distintos (`C1`, ` C02`, `c03`), una comuna inexistente y una fila duplicada | 3.5 |
| `equipamientos_auditoria.gpkg` | Identificadores repetidos, geometrías duplicadas, nulos, categorías escritas de varias formas | 3.1 |

## Licencias

- Documentación del curso: CC BY-SA 4.0.
- Datos: conservan la licencia de su fuente (ver `datos/originales/LEEME.md`).

Paquete generado con `scripts/construir_paquete_datos.py` y `scripts/generar_figuras_y_proyecto.py` del repositorio del curso.
