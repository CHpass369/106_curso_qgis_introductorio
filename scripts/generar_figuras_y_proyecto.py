"""Genera estilos, proyecto base, plano histórico simulado y figuras del curso.

Requiere haber ejecutado antes construir_paquete_datos.py. Se ejecuta con el Python de QGIS 4.x:

    "C:\\Program Files\\QGIS 4.2.1\\bin\\python-qgis.bat" scripts/generar_figuras_y_proyecto.py PAQUETE

PAQUETE es la carpeta `curso-qgis/` generada. Las figuras se escriben en
docs/assets/images/mapas/ del repositorio.
"""
import math
import os
import sys

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
if sys.platform == "win32":
    os.environ.setdefault("QT_QPA_FONTDIR", os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts"))

import numpy as np
from osgeo import gdal

from qgis.core import (
    Qgis, QgsApplication, QgsClassificationEqualInterval, QgsClassificationJenks,
    QgsClassificationQuantile, QgsCoordinateReferenceSystem, QgsFillSymbol, QgsGradientColorRamp,
    QgsGraduatedSymbolRenderer, QgsLayerTreeGroup, QgsLineSymbol, QgsMapRendererParallelJob,
    QgsMapSettings, QgsMarkerSymbol, QgsPalLayerSettings, QgsProject, QgsRasterLayer,
    QgsRectangle, QgsRuleBasedRenderer, QgsSingleBandPseudoColorRenderer, QgsStyle,
    QgsTextBufferSettings, QgsTextFormat, QgsVectorLayer, QgsVectorLayerSimpleLabeling,
    QgsCategorizedSymbolRenderer, QgsRendererCategory, QgsMultiBandColorRenderer,
    QgsContrastEnhancement, QgsHillshadeRenderer, QgsCoordinateTransform, QgsGeometry, QgsPointXY,
    QgsRendererRange, QgsFeatureRequest, QgsSymbolLayer, QgsProperty,
)
from qgis.PyQt.QtCore import QSize, Qt, QPointF, QRectF
from qgis.PyQt.QtGui import QColor, QFont, QImage, QPainter, QPen

gdal.UseExceptions()

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAQ = os.path.abspath(sys.argv[1])
ORIG = os.path.join(PAQ, "datos", "originales")
EJER = os.path.join(PAQ, "datos", "ejercicios")
ESTILOS = os.path.join(PAQ, "estilos")
FIG = os.path.join(REPO, "docs", "assets", "images", "mapas")
TMP = os.path.join(PAQ, "..", "_figtmp")
os.makedirs(FIG, exist_ok=True)
os.makedirs(TMP, exist_ok=True)

UTM19 = QgsCoordinateReferenceSystem("EPSG:32719")
FUENTE = "Segoe UI" if sys.platform == "win32" else "DejaVu Sans"

app = QgsApplication([], False)
app.initQgis()


# ------------------------------------------------------------------ capas

def vector(ruta, nombre, capa=None):
    uri = ruta + (f"|layername={capa}" if capa else "")
    lyr = QgsVectorLayer(uri, nombre, "ogr")
    assert lyr.isValid(), uri
    return lyr


def raster(ruta, nombre):
    lyr = QgsRasterLayer(ruta, nombre)
    assert lyr.isValid(), ruta
    return lyr


def etiquetar(lyr, campo, tam=9, color="#1f2937", expresion=False):
    s = QgsPalLayerSettings()
    s.fieldName = campo
    s.isExpression = expresion
    fmt = QgsTextFormat()
    fmt.setFont(QFont(FUENTE))
    fmt.setSize(tam)
    fmt.setColor(QColor(color))
    buf = QgsTextBufferSettings()
    buf.setEnabled(True)
    buf.setSize(1)
    buf.setColor(QColor(255, 255, 255, 220))
    fmt.setBuffer(buf)
    s.setFormat(fmt)
    lyr.setLabeling(QgsVectorLayerSimpleLabeling(s))
    lyr.setLabelsEnabled(True)


def estilo_comunas(lyr, relleno=None):
    props = {"color": relleno or "255,255,255,0", "outline_color": "#374151", "outline_width": "0.5"}
    lyr.setRenderer(QgsCategorizedSymbolRenderer())
    from qgis.core import QgsSingleSymbolRenderer
    lyr.setRenderer(QgsSingleSymbolRenderer(QgsFillSymbol.createSimple(props)))


def estilo_simple(lyr, sym):
    from qgis.core import QgsSingleSymbolRenderer
    lyr.setRenderer(QgsSingleSymbolRenderer(sym))


def estilo_equipamientos(lyr, tam=1.8):
    cats = []
    for valor, color, etiqueta in [("salud", "#dc2626", "Salud"), ("educacion", "#2563eb", "Educación")]:
        sym = QgsMarkerSymbol.createSimple({"name": "circle", "color": color, "outline_color": "white",
                                            "outline_width": "0.2", "size": str(tam)})
        cats.append(QgsRendererCategory(valor, sym, etiqueta))
    lyr.setRenderer(QgsCategorizedSymbolRenderer("tipo", cats))


def estilo_vias(lyr, solo_principales=False):
    raiz = QgsRuleBasedRenderer.Rule(None)
    reglas = [("troncal", "#7c2d12", 1.1), ("principal", "#b45309", 0.7), ("secundaria", "#9ca3af", 0.4)]
    if not solo_principales:
        reglas.append(("local", "#d1d5db", 0.2))
    for valor, color, ancho in reversed(reglas):
        r = QgsRuleBasedRenderer.Rule(QgsLineSymbol.createSimple({"color": color, "width": str(ancho)}),
                                      filterExp=f"\"jerarquia\" = '{valor}'", label=valor.capitalize())
        raiz.appendChild(r)
    lyr.setRenderer(QgsRuleBasedRenderer(raiz))


def estilo_rios(lyr):
    raiz = QgsRuleBasedRenderer.Rule(None)
    for valor, ancho in [("rio", 0.6), ("torrentera", 0.25), ("canal", 0.2)]:
        raiz.appendChild(QgsRuleBasedRenderer.Rule(
            QgsLineSymbol.createSimple({"color": "#0284c7", "width": str(ancho)}),
            filterExp=f"\"tipo\" = '{valor}'", label=valor.capitalize()))
    lyr.setRenderer(QgsRuleBasedRenderer(raiz))


def estilo_dem(lyr):
    r = QgsSingleBandPseudoColorRenderer(lyr.dataProvider(), 1)
    rampa = QgsStyle.defaultStyle().colorRamp("Spectral")
    rampa.invert()
    r.setClassificationMin(2500)
    r.setClassificationMax(4500)
    r.createShader(rampa, Qgis.ShaderInterpolationMethod.Linear, Qgis.ShaderClassificationMethod.Continuous, 8)
    lyr.setRenderer(r)


def estilo_rgb(lyr, bandas=(3, 2, 1), maximos=(1800, 1600, 1500)):
    r = QgsMultiBandColorRenderer(lyr.dataProvider(), *bandas)
    for i, (setter, mx) in enumerate(zip([r.setRedContrastEnhancement, r.setGreenContrastEnhancement,
                                           r.setBlueContrastEnhancement], maximos)):
        ce = QgsContrastEnhancement(lyr.dataProvider().dataType(bandas[i]))
        ce.setContrastEnhancementAlgorithm(QgsContrastEnhancement.ContrastEnhancementAlgorithm.StretchToMinimumMaximum)
        ce.setMinimumValue(100)
        ce.setMaximumValue(mx)
        setter(ce)
    lyr.setRenderer(r)


# ------------------------------------------------------------------ render

def render(capas, extension, ruta, ancho=1400, alto=1000, crs=UTM19, fondo="#ffffff", rotacion=0, dpi=144):
    ms = QgsMapSettings()
    ms.setLayers(capas)
    ms.setDestinationCrs(crs)
    ms.setOutputSize(QSize(ancho, alto))
    ms.setOutputDpi(dpi)
    ms.setBackgroundColor(QColor(fondo))
    ms.setRotation(rotacion)
    ms.setExtent(extension)
    ms.setFlag(Qgis.MapSettingsFlag.Antialiasing, True)
    job = QgsMapRendererParallelJob(ms)
    job.start()
    job.waitForFinished()
    img = job.renderedImage()
    if ruta:
        img.save(ruta)
    return img


def rotulo(img, texto, sub=None, pos="arriba"):
    p = QPainter(img)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    f = QFont(FUENTE, 13)
    f.setBold(True)
    p.setFont(f)
    caja = QRectF(14, 12, img.width() - 28, 64 if sub else 36)
    p.fillRect(caja, QColor(255, 255, 255, 225))
    p.setPen(QColor("#111827"))
    p.drawText(caja.adjusted(10, 4, -10, 0), Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop, texto)
    if sub:
        p.setFont(QFont(FUENTE, 10))
        p.setPen(QColor("#374151"))
        p.drawText(caja.adjusted(10, 32, -10, 0), Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop, sub)
    p.end()
    return img


def atribucion(img, texto):
    p = QPainter(img)
    p.setFont(QFont(FUENTE, 8))
    caja = QRectF(img.width() - 560, img.height() - 24, 552, 20)
    p.fillRect(caja, QColor(255, 255, 255, 200))
    p.setPen(QColor("#4b5563"))
    p.drawText(caja.adjusted(6, 0, -6, 0), Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter, texto)
    p.end()
    return img


def leyenda(img, items, x=None, y=None):
    """items: [(color, texto, tipo)] con tipo en {'punto','linea','area'}."""
    p = QPainter(img)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    p.setFont(QFont(FUENTE, 10))
    alto = 26 * len(items) + 16
    ancho = 230
    x = x if x is not None else 18
    y = y if y is not None else img.height() - alto - 34
    p.fillRect(QRectF(x, y, ancho, alto), QColor(255, 255, 255, 230))
    for i, (color, texto, tipo) in enumerate(items):
        cy = y + 20 + 26 * i
        c = QColor(color)
        if tipo == "punto":
            p.setPen(QPen(QColor("white"), 1))
            p.setBrush(c)
            p.drawEllipse(QPointF(x + 22, cy), 6, 6)
        elif tipo == "linea":
            p.setPen(QPen(c, 3))
            p.drawLine(QPointF(x + 10, cy), QPointF(x + 34, cy))
        else:
            p.setPen(QPen(QColor("#374151"), 1))
            p.setBrush(c)
            p.drawRect(QRectF(x + 12, cy - 8, 20, 16))
        p.setPen(QColor("#111827"))
        p.drawText(QPointF(x + 46, cy + 5), texto)
    p.end()
    return img


def guardar(img, nombre):
    img.save(os.path.join(FIG, nombre))
    print("figura", nombre)


def ampliar(rect, factor):
    r = QgsRectangle(rect)
    r.scale(factor)
    return r


# ------------------------------------------------------------------ datos base

LIM = os.path.join(ORIG, "limites.gpkg")
comunas = vector(LIM, "Comunas", "comunas")
limite = vector(LIM, "Límite municipal", "limite_municipal")
munis = vector(LIM, "Municipios metropolitanos", "municipios_metropolitanos")
zonas = vector(LIM, "Zonas de análisis", "zonas_analisis")
vias = vector(os.path.join(ORIG, "vias.gpkg"), "Vías", "vias")
rios = vector(os.path.join(ORIG, "rios.shp"), "Ríos y torrenteras")
csv_uri = ("file:///" + os.path.join(ORIG, "equipamientos.csv").replace("\\", "/") +
           "?delimiter=;&decimalPoint=,&xField=longitud&yField=latitud&crs=EPSG:4326&encoding=UTF-8")
equip = QgsVectorLayer(csv_uri, "Equipamientos", "delimitedtext")
assert equip.isValid()
dem = raster(os.path.join(ORIG, "dem_copernicus_30m.tif"), "DEM Copernicus 30 m")
s2 = raster(os.path.join(ORIG, "sentinel2_2025-07-16.tif"), "Sentinel-2 · 16-07-2025")
pob = raster(os.path.join(ORIG, "poblacion_worldpop_2020.tif"), "Población WorldPop 2020")

# DEM en UTM y derivados (solo para figuras)
dem_utm = os.path.join(TMP, "dem_utm.tif")
gdal.Warp(dem_utm, os.path.join(ORIG, "dem_copernicus_30m.tif"), dstSRS="EPSG:32719", xRes=30, yRes=30,
          resampleAlg="bilinear")
sombra = os.path.join(TMP, "sombreado.tif")
gdal.DEMProcessing(sombra, dem_utm, "hillshade", azimuth=315, altitude=45, zFactor=1.5)
pend = os.path.join(TMP, "pendiente.tif")
gdal.DEMProcessing(pend, dem_utm, "slope", slopeFormat="percent")

ext_muni = ampliar(limite.extent(), 1.08)
ext_urbano = QgsRectangle(795500, 8070500, 809500, 8081500)
ATR_OSM = "Datos: © colaboradores de OpenStreetMap (ODbL) · Copernicus DEM GLO-30"

# ------------------------------------------------------------------ estilos del paquete

estilo_comunas(comunas)
etiquetar(comunas, "nombre", 10)
estilo_simple(limite, QgsFillSymbol.createSimple({"color": "255,255,255,0", "outline_color": "#111827",
                                                  "outline_width": "0.9"}))
estilo_simple(munis, QgsFillSymbol.createSimple({"color": "#f3f4f6", "outline_color": "#9ca3af",
                                                 "outline_width": "0.3"}))
etiquetar(munis, "if(\"nombre\" = 'Cochabamba', '', \"nombre\")", 9, "#6b7280", expresion=True)
estilo_vias(vias)
estilo_rios(rios)
estilo_equipamientos(equip)
estilo_dem(dem)
estilo_rgb(s2)
for lyr, nombre in [(comunas, "comunas"), (limite, "limite_municipal"), (vias, "vias_jerarquia"),
                    (rios, "rios"), (equip, "equipamientos_tipo"), (dem, "dem_elevacion"),
                    (s2, "sentinel2_color_natural")]:
    lyr.saveNamedStyle(os.path.join(ESTILOS, nombre + ".qml"))

# ------------------------------------------------------------------ proyecto base

proy = QgsProject.instance()
proy.clear()
proy.setCrs(UTM19)
proy.setTitle("Curso QGIS · Cochabamba · proyecto base")
proy.writeEntry("Paths", "/Absolute", False)
raiz = proy.layerTreeRoot()
g_ref = raiz.addGroup("Referencia")
g_red = raiz.addGroup("Red vial e hidrografía")
g_ras = raiz.addGroup("Ráster")
for lyr, grupo in [(limite, g_ref), (comunas, g_ref), (munis, g_ref), (vias, g_red), (rios, g_red),
                   (s2, g_ras), (dem, g_ras)]:
    c = lyr.clone()
    c.setName(lyr.name())
    proy.addMapLayer(c, False)
    grupo.addLayer(c)
for lyr in proy.mapLayers().values():
    if lyr.name() in ("Municipios metropolitanos", "Sentinel-2 · 16-07-2025"):
        raiz.findLayer(lyr.id()).setItemVisibilityChecked(False)
proy.write(os.path.join(PAQ, "proyectos", "curso_qgis_base.qgz"))
proy.clear()

# ------------------------------------------------------------------ figuras

# 1. Mapa del caso
som = raster(sombra, "Sombreado")
som.renderer().setOpacity(0.55)
estilo_vias(vias, solo_principales=True)
img = render([limite, comunas, equip, vias, rios, som, munis], ext_muni, None)
rotulo(img, "Caso conductor · Municipio de Cochabamba", "Comunas, red vial principal, cursos de agua y equipamientos de salud y educación")
leyenda(img, [("#dc2626", "Salud", "punto"), ("#2563eb", "Educación", "punto"),
              ("#b45309", "Vía principal", "linea"), ("#0284c7", "Río o torrentera", "linea")])
atribucion(img, ATR_OSM)
guardar(img, "caso-cochabamba.png")

# 2. Resultado de importar el CSV (2.5)
img = render([equip, comunas], ampliar(comunas.extent(), 1.05), None, 1200, 1000)
rotulo(img, "Resultado esperado · equipamientos.csv importado", "661 puntos en EPSG:4326 dentro de las comunas de Cochabamba")
leyenda(img, [("#dc2626", "Salud", "punto"), ("#2563eb", "Educación", "punto")])
atribucion(img, "Datos: © colaboradores de OpenStreetMap (ODbL)")
guardar(img, "2-5-equipamientos-resultado.png")

# 2b. Lectura temática (2.9)
z0 = zonas.clone()
estilo_simple(z0, QgsFillSymbol.createSimple({"color": "#f3f4f6", "outline_color": "#e5e7eb", "outline_width": "0.1"}))
zt = zonas.clone()
zt.setSubsetString("\"pob_2020\" > 0")
ren_t = QgsGraduatedSymbolRenderer("\"pob_2020\" / \"area_km2\"")
ren_t.setClassificationMethod(QgsClassificationQuantile())
ren_t.setSourceSymbol(QgsFillSymbol.createSimple({"outline_color": "#ffffff", "outline_width": "0.1"}))
ren_t.setSourceColorRamp(QgsStyle.defaultStyle().colorRamp("YlOrRd"))
ren_t.updateClasses(zt, 5)
zt.setRenderer(ren_t)
zt.setOpacity(0.7)
eq_t = equip.clone()
cats_t = []
for valor, color, tam in [("hospital", "#7f1d1d", 2.6), ("clinica", "#dc2626", 1.8), ("consultorio", "#fca5a5", 1.5),
                          ("universidad", "#1e3a8a", 2.4), ("instituto", "#2563eb", 1.6), ("escuela", "#3b82f6", 1.4),
                          ("kinder", "#93c5fd", 1.3)]:
    cats_t.append(QgsRendererCategory(valor, QgsMarkerSymbol.createSimple(
        {"name": "circle", "color": color, "outline_color": "white", "outline_width": "0.35", "size": str(tam)}), valor))
eq_t.setRenderer(QgsCategorizedSymbolRenderer("subtipo", cats_t))
com_t = comunas.clone()
estilo_comunas(com_t)
etiquetar(com_t, "upper(\"nombre\")", 10, "#111827", expresion=True)
ext_t = QgsRectangle()
for f in zonas.getFeatures(QgsFeatureRequest().setFilterExpression('"pob_2020" > 500')):
    ext_t.combineExtentWith(f.geometry().boundingBox())
img = render([eq_t, com_t, limite, zt, z0], ampliar(ext_t, 1.08), None, 1200, 1200)
rotulo(img, "Primera lectura temática de Cochabamba",
       "Densidad de población por zona (cuantiles), establecimientos por subtipo y comunas")
leyenda(img, [("#7f1d1d", "Hospital", "punto"), ("#dc2626", "Clínica", "punto"), ("#1e3a8a", "Universidad", "punto"),
              ("#3b82f6", "Escuela", "punto"), ("#fee08b", "Densidad baja", "area"), ("#bd0026", "Densidad alta", "area")])
atribucion(img, "© colaboradores de OpenStreetMap · WorldPop (CC BY 4.0)")
guardar(img, "2-9-lectura-tematica.png")

# 3. Coordenadas intercambiadas: vista mundial
tierra = vector(os.path.join(REPO, "docs", "assets", "data", "ne_110m_land.geojson"), "Tierra")
estilo_simple(tierra, QgsFillSymbol.createSimple({"color": "#e5e7eb", "outline_color": "#9ca3af", "outline_width": "0.2"}))
WGS = QgsCoordinateReferenceSystem("EPSG:4326")
from qgis.core import QgsFeature, QgsField, QgsFields
from qgis.PyQt.QtCore import QMetaType
mem = QgsVectorLayer("Point?crs=EPSG:4326&field=caso:string", "puntos", "memory")
prov = mem.dataProvider()
feats = []
for caso, x, y in [("correcto", -66.157, -17.394), ("intercambiado", -17.394, -66.157)]:
    f = QgsFeature(mem.fields())
    f.setAttribute("caso", caso)
    f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(x, y)))
    feats.append(f)
prov.addFeatures(feats)
mem.setRenderer(QgsCategorizedSymbolRenderer("caso", [
    QgsRendererCategory("correcto", QgsMarkerSymbol.createSimple({"color": "#16a34a", "size": "4", "outline_color": "white"}), "Correcto"),
    QgsRendererCategory("intercambiado", QgsMarkerSymbol.createSimple({"color": "#dc2626", "size": "4", "outline_color": "white"}), "Intercambiado"),
]))
etiquetar(mem, "if(\"caso\"='correcto','Cochabamba (−66,16 ; −17,39)','Intercambiado (−17,39 ; −66,16)')", 10, expresion=True)
img = render([mem, tierra], QgsRectangle(-110, -80, 10, 10), None, 1400, 1000, crs=WGS, fondo="#f0f9ff")
rotulo(img, "Longitud y latitud intercambiadas", "El mismo registro termina frente a la Antártida en lugar de Cochabamba")
atribucion(img, "Tierra: Natural Earth (dominio público)")
guardar(img, "2-5-coordenadas-intercambiadas.png")

# 4. SRC asignado erróneamente (2.6)
vias_mal = vector(os.path.join(EJER, "vias_principales_src_erroneo.gpkg"), "Vías (SRC erróneo)", "vias_principales")
estilo_simple(vias_mal, QgsLineSymbol.createSimple({"color": "#dc2626", "width": "0.8"}))
estilo_simple(limite, QgsFillSymbol.createSimple({"color": "#16a34a", "outline_color": "#166534", "outline_width": "0.6"}))
from qgis.core import QgsRectangle as R
img = render([vias_mal, limite, tierra], QgsRectangle(-75, -21.5, -63, -14), None, 1400, 900, crs=WGS, fondo="#f0f9ff")
rotulo(img, "Un SRC mal asignado desplaza los datos cientos de kilómetros",
       "Vías en UTM 20 S declaradas como UTM 19 S (rojo): aparecen unos 650 km al oeste, en el océano Pacífico")
leyenda(img, [("#16a34a", "Municipio de Cochabamba", "area"), ("#dc2626", "Vías con SRC erróneo", "linea")])
atribucion(img, "© colaboradores de OpenStreetMap · Natural Earth")
guardar(img, "2-6-src-erroneo.png")
estilo_simple(limite, QgsFillSymbol.createSimple({"color": "255,255,255,0", "outline_color": "#111827", "outline_width": "0.9"}))

# 5. Ráster: DEM, color natural y falso color (2.10)
img = render([limite, dem], ext_muni, None, 1200, 1000)
rotulo(img, "DEM · pseudocolor monobanda", "Elevación de 2 500 m (azul) a más de 4 500 m (rojo) en la cordillera del Tunari")
atribucion(img, "Copernicus DEM GLO-30 © DLR e.V. 2010-2014 y © Airbus 2017-2018 (ESA)")
guardar(img, "2-10-dem-pseudocolor.png")
img = render([s2], s2.extent(), None, 1236, 922)
rotulo(img, "Sentinel-2 · color natural (4-3-2)", "16 de julio de 2025 · 10 m de resolución")
atribucion(img, "Contiene datos modificados de Copernicus Sentinel (2025)")
guardar(img, "2-10-sentinel-color-natural.png")
estilo_rgb(s2, (4, 3, 2), (4000, 1600, 1500))
img = render([s2], s2.extent(), None, 1236, 922)
rotulo(img, "Sentinel-2 · falso color infrarrojo (8-4-3)", "La vegetación sana aparece en rojo intenso")
atribucion(img, "Contiene datos modificados de Copernicus Sentinel (2025)")
guardar(img, "2-10-sentinel-falso-color.png")
s2.saveNamedStyle(os.path.join(ESTILOS, "sentinel2_falso_color.qml"))

# 6. Pendiente (3.9)
pl = raster(pend, "Pendiente (%)")
r = QgsSingleBandPseudoColorRenderer(pl.dataProvider(), 1)
rampa = QgsStyle.defaultStyle().colorRamp("YlOrRd")
r.setClassificationMin(0)
r.setClassificationMax(60)
r.createShader(rampa, Qgis.ShaderInterpolationMethod.Discrete, Qgis.ShaderClassificationMethod.EqualInterval, 6)
pl.setRenderer(r)
pl.renderer().setOpacity(0.85)
img = render([limite, comunas, pl, som], ext_muni, None, 1200, 1000)
rotulo(img, "Pendiente del terreno (%)", "Derivada del DEM de 30 m reproyectado a UTM 19 S")
atribucion(img, "Copernicus DEM GLO-30 · cálculo: GDAL")
guardar(img, "3-9-pendiente.png")

# 7. Cobertura de salud: 1 km alrededor de establecimientos de salud (3.7)
salud = equip.clone()
salud.setSubsetString("\"tipo\" = 'salud'")
estilo_simple(salud, QgsMarkerSymbol.createSimple({"color": "#dc2626", "size": "1.6", "outline_color": "white"}))
buf = QgsVectorLayer("Polygon?crs=EPSG:32719", "Área a 1 km", "memory")
ct = QgsCoordinateTransform(WGS, UTM19, QgsProject.instance())
geoms = []
for f in salud.getFeatures():
    g = QgsGeometry(f.geometry())
    g.transform(ct)
    geoms.append(g.buffer(1000, 24))
union = QgsGeometry.unaryUnion(geoms)
fb = QgsFeature()
fb.setGeometry(union)
buf.dataProvider().addFeatures([fb])
estilo_simple(buf, QgsFillSymbol.createSimple({"color": "255,255,255,0", "outline_color": "#1d4ed8",
                                               "outline_width": "0.5", "outline_style": "dash"}))
dens = QgsVectorLayer("MultiPolygon?crs=EPSG:32719&field=estado:string", "Zonas", "memory")
nuevas = []
for f in zonas.getFeatures():
    g = f.geometry()
    if f["pob_2020"] <= 0:
        estado = "sin_poblacion"
    elif union.contains(g.pointOnSurface()):
        estado = "cubierta"
    else:
        estado = "no_cubierta"
    nf = QgsFeature(dens.fields())
    nf.setAttribute("estado", estado)
    nf.setGeometry(g)
    nuevas.append(nf)
dens.dataProvider().addFeatures(nuevas)
cats = []
for valor, color in [("cubierta", "#d1fae5"), ("no_cubierta", "#f97316"), ("sin_poblacion", "#f9fafb")]:
    cats.append(QgsRendererCategory(valor, QgsFillSymbol.createSimple({"color": color, "outline_color": "#d1d5db", "outline_width": "0.1"}), valor))
dens.setRenderer(QgsCategorizedSymbolRenderer("estado", cats))
ext_pob = QgsRectangle()
for f in zonas.getFeatures(QgsFeatureRequest().setFilterExpression('"pob_2020" > 500')):
    ext_pob.combineExtentWith(f.geometry().boundingBox())
img = render([salud, buf, comunas, dens], ampliar(ext_pob, 1.06), None, 1200, 1200)
rotulo(img, "¿Quién vive a más de 1 km de un establecimiento de salud?",
       "Zonas habitadas de 1 km² según si su centro queda a menos de 1 km de un establecimiento")
leyenda(img, [("#dc2626", "Establecimiento de salud", "punto"), ("#1d4ed8", "Límite de 1 km", "linea"),
              ("#d1fae5", "Zona cubierta", "area"), ("#f97316", "Zona habitada sin cobertura", "area")])
atribucion(img, "© colaboradores de OpenStreetMap · WorldPop (CC BY 4.0)")
guardar(img, "3-7-cobertura-salud.png")

# 8. Tres clasificaciones del mismo dato (4.4)
paneles = []
urbanas = zonas.clone()
urbanas.setSubsetString("\"pob_2020\" > 0")
expr = "\"pob_2020\" / \"area_km2\""
for metodo, titulo in [(QgsClassificationEqualInterval(), "Intervalos iguales"),
                       (QgsClassificationQuantile(), "Cuantiles"),
                       (QgsClassificationJenks(), "Rupturas naturales (Jenks)")]:
    capa = urbanas.clone()
    ren = QgsGraduatedSymbolRenderer(expr)
    ren.setClassificationMethod(metodo)
    ren.setSourceSymbol(QgsFillSymbol.createSimple({"outline_color": "#ffffff", "outline_width": "0.15"}))
    ren.setSourceColorRamp(QgsStyle.defaultStyle().colorRamp("YlOrRd"))
    ren.updateClasses(capa, 5)
    capa.setRenderer(ren)
    im = render([limite, capa], ampliar(urbanas.extent(), 1.04), None, 700, 760)
    p = QPainter(im)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    f = QFont(FUENTE, 13)
    f.setBold(True)
    p.setFont(f)
    p.fillRect(QRectF(0, 0, 700, 40), QColor(255, 255, 255, 235))
    p.setPen(QColor("#111827"))
    p.drawText(QRectF(12, 6, 680, 30), Qt.AlignmentFlag.AlignLeft, titulo)
    p.setFont(QFont(FUENTE, 9))
    y0 = 560
    p.fillRect(QRectF(8, y0 - 8, 230, 5 * 24 + 30), QColor(255, 255, 255, 235))
    p.setPen(QColor("#374151"))
    p.drawText(QPointF(16, y0 + 8), "hab./km²")
    for i, rr in enumerate(ren.ranges()):
        yy = y0 + 18 + 24 * i
        p.setBrush(rr.symbol().color())
        p.setPen(QPen(QColor("#9ca3af"), 1))
        p.drawRect(QRectF(16, yy, 22, 16))
        p.setPen(QColor("#111827"))
        p.drawText(QPointF(46, yy + 13), f"{rr.lowerValue():,.0f} – {rr.upperValue():,.0f}".replace(",", " "))
    p.end()
    paneles.append(im)
comp = QImage(2130, 800, QImage.Format.Format_ARGB32)
comp.fill(QColor("white"))
p = QPainter(comp)
for i, im in enumerate(paneles):
    p.drawImage(10 + i * 710, 30, im)
p.setFont(QFont(FUENTE, 10))
p.setPen(QColor("#4b5563"))
p.drawText(QRectF(10, 4, 2100, 22), Qt.AlignmentFlag.AlignLeft,
           "Mismo dato (densidad WorldPop 2020 por zona de 1 km²), mismas 5 clases y misma paleta: solo cambia el método de clasificación.")
p.end()
guardar(comp, "4-4-tres-clasificaciones.png")

# ------------------------------------------------------------------ plano histórico simulado

centro = QgsRectangle(799300, 8073700, 803300, 8077200)
vias_p = vias.clone()
raiz_r = QgsRuleBasedRenderer.Rule(None)
for exp, ancho in [("\"jerarquia\" IN ('troncal','principal')", 0.9), ("\"jerarquia\" = 'secundaria'", 0.55),
                   ("\"jerarquia\" = 'local'", 0.35)]:
    raiz_r.appendChild(QgsRuleBasedRenderer.Rule(QgsLineSymbol.createSimple({"color": "#3f2d1c", "width": str(ancho)}), filterExp=exp))
vias_p.setRenderer(QgsRuleBasedRenderer(raiz_r))
rios_p = rios.clone()
estilo_simple(rios_p, QgsLineSymbol.createSimple({"color": "#4b6a88", "width": "0.7", "line_style": "dash"}))
img = render([vias_p, rios_p], centro, None, 2400, 2100, fondo="#efe3c8", rotacion=4.0, dpi=150)
p = QPainter(img)
f = QFont("Georgia", 26)
f.setItalic(True)
p.setFont(f)
p.fillRect(QRectF(1500, 1780, 860, 270), QColor("#efe3c8"))
p.setPen(QPen(QColor("#3f2d1c"), 3))
p.drawRect(QRectF(1500, 1780, 860, 270))
p.drawText(QRectF(1500, 1795, 860, 60), Qt.AlignmentFlag.AlignCenter, "Plano de la Ciudad de Cochabamba")
p.setFont(QFont("Georgia", 16))
p.drawText(QRectF(1500, 1860, 860, 40), Qt.AlignmentFlag.AlignCenter, "Levantado en 1985 · Escala 1:20 000")
p.setFont(QFont("Georgia", 11))
p.drawText(QRectF(1500, 1920, 860, 110), Qt.AlignmentFlag.AlignCenter | Qt.TextFlag.TextWordWrap,
           "Reproducción simulada con fines didácticos.\nGenerada a partir de OpenStreetMap; no es un documento histórico.")
p.end()
tmp_png = os.path.join(TMP, "plano.png")
img.save(tmp_png)
ds = gdal.Open(tmp_png)
arr = ds.ReadAsArray().astype(np.float32)[:3]
rng_np = np.random.default_rng(1985)
ruido = rng_np.normal(0, 9, arr.shape[1:]).astype(np.float32)
mancha = np.zeros(arr.shape[1:], np.float32)
yy, xx = np.mgrid[0:arr.shape[1], 0:arr.shape[2]]
for _ in range(6):
    cy, cx, rr = rng_np.integers(0, arr.shape[1]), rng_np.integers(0, arr.shape[2]), rng_np.integers(80, 260)
    mancha += 22 * np.exp(-((yy - cy) ** 2 + (xx - cx) ** 2) / (2 * rr ** 2))
arr = np.clip(arr + ruido - mancha, 0, 255).astype(np.uint8)
drv = gdal.GetDriverByName("GTiff")
out = drv.Create(os.path.join(ORIG, "plano_historico_1985.tif"), arr.shape[2], arr.shape[1], 3, gdal.GDT_Byte,
                 ["COMPRESS=JPEG", "JPEG_QUALITY=85", "PHOTOMETRIC=YCBCR", "TILED=YES"])
for i in range(3):
    out.GetRasterBand(i + 1).WriteArray(arr[i])
out = None
vista = QImage(os.path.join(TMP, "plano.png")).scaledToWidth(1200, Qt.TransformationMode.SmoothTransformation)
guardar(vista, "3-10-plano-historico-simulado.png")

# ------------------------------------------------------------------ zip final

import shutil
for nombre in os.listdir(os.path.join(ORIG)):
    if nombre.endswith(".aux.xml"):
        os.remove(os.path.join(ORIG, nombre))
zip_base = os.path.join(os.path.dirname(PAQ), "curso-qgis-cochabamba")
shutil.make_archive(zip_base, "zip", os.path.dirname(PAQ), os.path.basename(PAQ))
print("paquete", zip_base + ".zip", round(os.path.getsize(zip_base + ".zip") / 1e6, 1), "MB")

app.exitQgis()
