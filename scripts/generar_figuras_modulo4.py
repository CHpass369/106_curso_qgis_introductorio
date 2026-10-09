"""Genera las figuras del Módulo 4 (diseño cartográfico, composición y atlas).

    python-qgis scripts/generar_figuras_modulo4.py PAQUETE

Escribe PNG en docs/assets/images/mapas/ y, como ejemplo descargable, una
plantilla de composición (.qpt) y el atlas en PDF en PAQUETE/../soluciones/.
"""
import os
import sys

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
if sys.platform == "win32":
    os.environ.setdefault("QT_QPA_FONTDIR", os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts"))

from qgis.core import (
    Qgis, QgsApplication, QgsVectorLayer, QgsProject, QgsCoordinateReferenceSystem, QgsRectangle,
    QgsFillSymbol, QgsLineSymbol, QgsMarkerSymbol, QgsSingleSymbolRenderer, QgsCategorizedSymbolRenderer,
    QgsRendererCategory, QgsGraduatedSymbolRenderer, QgsClassificationQuantile, QgsStyle, QgsRuleBasedRenderer,
    QgsPalLayerSettings, QgsTextFormat, QgsTextBufferSettings, QgsVectorLayerSimpleLabeling, QgsMapSettings,
    QgsMapRendererParallelJob, QgsPrintLayout, QgsLayoutItemMap, QgsLayoutItemLegend, QgsLayoutItemScaleBar,
    QgsLayoutItemLabel, QgsLayoutItemPicture, QgsLayoutPoint, QgsLayoutSize, QgsUnitTypes, QgsLayoutExporter,
    QgsLayoutItemPage, QgsFeature, QgsGeometry, QgsField, QgsLayoutItemShape, QgsLayoutMeasurement,
    QgsRasterLayer, QgsFeatureRequest, QgsLayoutItemMapOverview, QgsRendererRange, QgsSymbolLayer, QgsProperty,
    QgsReadWriteContext, QgsLegendStyle,
)
from qgis.PyQt.QtCore import QSize, Qt, QRectF, QPointF, QMetaType
from qgis.PyQt.QtGui import QColor, QFont, QImage, QPainter, QPen
from qgis.PyQt.QtXml import QDomDocument

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAQ = os.path.abspath(sys.argv[1])
ORIG = os.path.join(PAQ, "datos", "originales")
SOL = os.path.join(os.path.dirname(PAQ), "soluciones")
FIG = os.path.join(REPO, "docs", "assets", "images", "mapas")
os.makedirs(SOL, exist_ok=True)
FUENTE = "Segoe UI" if sys.platform == "win32" else "DejaVu Sans"
UTM19 = QgsCoordinateReferenceSystem("EPSG:32719")

app = QgsApplication([], False)
app.initQgis()
proj = QgsProject.instance()
proj.setCrs(UTM19)


def capa(uri, nombre, prov="ogr"):
    lyr = QgsVectorLayer(uri, nombre, prov)
    assert lyr.isValid(), uri
    return lyr


def simple(lyr, sym):
    lyr.setRenderer(QgsSingleSymbolRenderer(sym))


def etiquetas(lyr, expr, tam=9, color="#1f2937", negrita=False, buf=True, mayus=False):
    s = QgsPalLayerSettings()
    s.fieldName = expr
    s.isExpression = True
    f = QgsTextFormat()
    fnt = QFont(FUENTE)
    fnt.setBold(negrita)
    f.setFont(fnt)
    f.setSize(tam)
    f.setColor(QColor(color))
    if buf:
        b = QgsTextBufferSettings()
        b.setEnabled(True)
        b.setSize(1)
        b.setColor(QColor(255, 255, 255, 220))
        f.setBuffer(b)
    s.setFormat(f)
    lyr.setLabeling(QgsVectorLayerSimpleLabeling(s))
    lyr.setLabelsEnabled(True)


def render(capas, ext, ancho=1100, alto=1000, fondo="#ffffff"):
    ms = QgsMapSettings()
    ms.setLayers(capas)
    ms.setDestinationCrs(UTM19)
    ms.setOutputSize(QSize(ancho, alto))
    ms.setOutputDpi(144)
    ms.setBackgroundColor(QColor(fondo))
    ms.setExtent(ext)
    ms.setFlag(Qgis.MapSettingsFlag.Antialiasing, True)
    job = QgsMapRendererParallelJob(ms)
    job.start()
    job.waitForFinished()
    return job.renderedImage()


def titulo(img, texto, sub=None):
    p = QPainter(img)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    f = QFont(FUENTE, 11)
    f.setBold(True)
    p.setFont(f)
    alto = 62 if sub else 38
    p.fillRect(QRectF(0, 0, img.width(), alto), QColor(255, 255, 255, 235))
    p.setPen(QColor("#111827"))
    p.drawText(QRectF(14, 6, img.width() - 28, 30), Qt.AlignmentFlag.AlignLeft, texto)
    if sub:
        p.setFont(QFont(FUENTE, 9))
        p.setPen(QColor("#4b5563"))
        p.drawText(QRectF(14, 36, img.width() - 28, 22), Qt.AlignmentFlag.AlignLeft, sub)
    p.end()
    return img


def lado_a_lado(imgs, nombre, nota=None):
    w = sum(i.width() for i in imgs) + 10 * (len(imgs) + 1)
    h = max(i.height() for i in imgs) + 20 + (26 if nota else 0)
    comp = QImage(w, h, QImage.Format.Format_ARGB32)
    comp.fill(QColor("white"))
    p = QPainter(comp)
    x = 10
    for i in imgs:
        p.drawImage(x, 10, i)
        x += i.width() + 10
    if nota:
        p.setFont(QFont(FUENTE, 9))
        p.setPen(QColor("#4b5563"))
        p.drawText(QRectF(10, h - 26, w - 20, 22), Qt.AlignmentFlag.AlignLeft, nota)
    p.end()
    comp.save(os.path.join(FIG, nombre))
    print("figura", nombre)


# ------------------------------------------------------------ datos
LIM = os.path.join(ORIG, "limites.gpkg")
comunas = capa(LIM + "|layername=comunas", "Comunas")
limite = capa(LIM + "|layername=limite_municipal", "Límite municipal")
munis = capa(LIM + "|layername=municipios_metropolitanos", "Municipios vecinos")
zonas = capa(LIM + "|layername=zonas_analisis", "Zonas")
vias = capa(os.path.join(ORIG, "vias.gpkg") + "|layername=vias", "Vías")
rios = capa(os.path.join(ORIG, "rios.shp"), "Ríos")
csv_uri = ("file:///" + os.path.join(ORIG, "equipamientos.csv").replace("\\", "/") +
           "?delimiter=;&decimalPoint=,&xField=longitud&yField=latitud&crs=EPSG:4326&encoding=UTF-8")
equip = capa(csv_uri, "Equipamientos", "delimitedtext")

# población por comuna (suma de zonas)
pob = {}
for z in zonas.getFeatures():
    pob[z["cod_comuna"]] = pob.get(z["cod_comuna"], 0) + z["pob_2020"]
com_mem = QgsVectorLayer("MultiPolygon?crs=EPSG:32719&field=cod:string&field=nombre:string&field=pob:integer&field=dens:double",
                         "Comunas (población)", "memory")
feats = []
for f in comunas.getFeatures():
    nf = QgsFeature(com_mem.fields())
    nf.setAttributes([f["cod_comuna"], f["nombre"], pob[f["cod_comuna"]], pob[f["cod_comuna"]] / f["area_km2"]])
    nf.setGeometry(f.geometry())
    feats.append(nf)
com_mem.dataProvider().addFeatures(feats)

# cobertura de salud
salud = equip.clone()
salud.setSubsetString("\"tipo\" = 'salud'")
from qgis.core import QgsCoordinateTransform
ct = QgsCoordinateTransform(QgsCoordinateReferenceSystem("EPSG:4326"), UTM19, proj)
gs = []
for f in salud.getFeatures():
    g = QgsGeometry(f.geometry())
    g.transform(ct)
    gs.append(g.buffer(1000, 16))
union = QgsGeometry.unaryUnion(gs)
z_mem = QgsVectorLayer("MultiPolygon?crs=EPSG:32719&field=cod_zona:string&field=cod_comuna:string&field=pob:integer&field=estado:string",
                       "Zonas (cobertura)", "memory")
nuevas = []
for z in zonas.getFeatures():
    e = "sin_poblacion" if z["pob_2020"] <= 0 else ("cubierta" if union.contains(z.geometry().pointOnSurface()) else "no_cubierta")
    nf = QgsFeature(z_mem.fields())
    nf.setAttributes([z["cod_zona"], z["cod_comuna"], z["pob_2020"], e])
    nf.setGeometry(z.geometry())
    nuevas.append(nf)
z_mem.dataProvider().addFeatures(nuevas)

ext_pob = QgsRectangle()
for f in zonas.getFeatures(QgsFeatureRequest().setFilterExpression('"pob_2020" > 500')):
    ext_pob.combineExtentWith(f.geometry().boundingBox())
ext_pob.scale(1.08)

GRIS_FONDO = {"color": "#f3f4f6", "outline_color": "#d1d5db", "outline_width": "0.2"}

# ------------------------------------------------------------ 4.2 dos escalas
v_lejos = vias.clone()
r = QgsRuleBasedRenderer.Rule(None)
r.appendChild(QgsRuleBasedRenderer.Rule(QgsLineSymbol.createSimple({"color": "#9a3412", "width": "0.9"}), filterExp="\"jerarquia\" = 'troncal'"))
r.appendChild(QgsRuleBasedRenderer.Rule(QgsLineSymbol.createSimple({"color": "#c2410c", "width": "0.5"}), filterExp="\"jerarquia\" = 'principal'"))
v_lejos.setRenderer(QgsRuleBasedRenderer(r))
c1 = comunas.clone()
simple(c1, QgsFillSymbol.createSimple({"color": "255,255,255,0", "outline_color": "#374151", "outline_width": "0.6"}))
etiquetas(c1, "upper(\"nombre\")", 9, mayus=True)
m1 = munis.clone()
simple(m1, QgsFillSymbol.createSimple(GRIS_FONDO))
img1 = render([c1, v_lejos, m1], QgsRectangle(limite.extent()).buffered(1500), 900, 1000)
titulo(img1, "Salida 1:100 000 · panorama municipal", "Solo vías troncales y principales; comunas rotuladas")

v_cerca = vias.clone()
r2 = QgsRuleBasedRenderer.Rule(None)
for exp, color, ancho in [("\"jerarquia\" = 'local'", "#d1d5db", 0.35), ("\"jerarquia\" = 'secundaria'", "#9ca3af", 0.7),
                          ("\"jerarquia\" = 'principal'", "#c2410c", 1.1), ("\"jerarquia\" = 'troncal'", "#9a3412", 1.5)]:
    r2.appendChild(QgsRuleBasedRenderer.Rule(QgsLineSymbol.createSimple({"color": color, "width": str(ancho)}), filterExp=exp))
v_cerca.setRenderer(QgsRuleBasedRenderer(r2))
eq_c = equip.clone()
eq_c.setRenderer(QgsCategorizedSymbolRenderer("tipo", [
    QgsRendererCategory("salud", QgsMarkerSymbol.createSimple({"color": "#dc2626", "size": "2.6", "outline_color": "white"}), "Salud"),
    QgsRendererCategory("educacion", QgsMarkerSymbol.createSimple({"color": "#2563eb", "size": "2.2", "outline_color": "white"}), "Educación")]))
etiquetas(eq_c, "\"nombre\"", 7, "#374151")
img2 = render([eq_c, v_cerca], QgsRectangle(800600, 8074200, 803400, 8077300), 900, 1000)
titulo(img2, "Salida 1:10 000 · centro de la ciudad", "Toda la red vial y establecimientos con nombre")
lado_a_lado([img1, img2], "4-2-dos-escalas.png", "Mismo territorio, dos escalas de salida: el contenido se selecciona y se simboliza según la escala. © colaboradores de OpenStreetMap")

# ------------------------------------------------------------ 4.3 total vs densidad
mal = com_mem.clone()
ren = QgsGraduatedSymbolRenderer("pob")
ren.setClassificationMethod(QgsClassificationQuantile())
ren.setSourceSymbol(QgsFillSymbol.createSimple({"outline_color": "#ffffff", "outline_width": "0.4"}))
ren.setSourceColorRamp(QgsStyle.defaultStyle().colorRamp("Blues"))
ren.updateClasses(mal, 4)
mal.setRenderer(ren)
etiquetas(mal, "\"nombre\" || '\\n' || replace(format_number(\"pob\", 0), ',', ' ')", 8)
imga = render([mal], QgsRectangle(limite.extent()).buffered(800), 800, 950)
titulo(imga, "✗ Coropleta de población total", "La comuna más grande parece la más «poblada» por su tamaño")

bien = com_mem.clone()
ren2 = QgsGraduatedSymbolRenderer("dens")
ren2.setClassificationMethod(QgsClassificationQuantile())
ren2.setSourceSymbol(QgsFillSymbol.createSimple({"outline_color": "#ffffff", "outline_width": "0.4"}))
ren2.setSourceColorRamp(QgsStyle.defaultStyle().colorRamp("YlOrRd"))
ren2.updateClasses(bien, 4)
bien.setRenderer(ren2)
circ = QgsVectorLayer("Point?crs=EPSG:32719&field=nombre:string&field=pob:integer", "pob", "memory")
cf = []
for f in com_mem.getFeatures():
    nf = QgsFeature(circ.fields())
    nf.setAttributes([f["nombre"], f["pob"]])
    nf.setGeometry(f.geometry().pointOnSurface())
    cf.append(nf)
circ.dataProvider().addFeatures(cf)
sym = QgsMarkerSymbol.createSimple({"color": "37,99,235,150", "outline_color": "#1e3a8a", "outline_width": "0.4"})
sym.setDataDefinedSize(QgsProperty.fromExpression("sqrt(\"pob\" / 125000) * 14"))
simple(circ, sym)
etiquetas(circ, "\"nombre\"", 8)
imgb = render([circ, bien], QgsRectangle(limite.extent()).buffered(800), 800, 950)
titulo(imgb, "✓ Densidad (coropleta) + población total (círculos)", "Cada variable con la representación que le corresponde")
lado_a_lado([imga, imgb], "4-3-total-vs-densidad.png", "Datos: población WorldPop 2020 agregada por comuna. Comunas: © colaboradores de OpenStreetMap")

# ------------------------------------------------------------ 4.5 jerarquía antes / después
a_z = z_mem.clone()
a_z.setRenderer(QgsCategorizedSymbolRenderer("estado", [
    QgsRendererCategory("cubierta", QgsFillSymbol.createSimple({"color": "#22c55e", "outline_color": "#000000", "outline_width": "0.4"}), "Cubierta"),
    QgsRendererCategory("no_cubierta", QgsFillSymbol.createSimple({"color": "#a855f7", "outline_color": "#000000", "outline_width": "0.4"}), "No cubierta"),
    QgsRendererCategory("sin_poblacion", QgsFillSymbol.createSimple({"color": "#eab308", "outline_color": "#000000", "outline_width": "0.4"}), "Sin población")]))
a_v = vias.clone()
a_v.setSubsetString("\"jerarquia\" <> 'local'")
simple(a_v, QgsLineSymbol.createSimple({"color": "#ef4444", "width": "0.8"}))
a_r = rios.clone()
simple(a_r, QgsLineSymbol.createSimple({"color": "#0ea5e9", "width": "0.8"}))
a_e = salud.clone()
simple(a_e, QgsMarkerSymbol.createSimple({"color": "#f97316", "size": "2.2", "outline_color": "#000000"}))
img_a = render([a_e, a_r, a_v, a_z], ext_pob, 900, 950)
titulo(img_a, "Antes · todo compite", "Colores saturados y bordes negros en todas las capas")

b_z = z_mem.clone()
b_z.setRenderer(QgsCategorizedSymbolRenderer("estado", [
    QgsRendererCategory("cubierta", QgsFillSymbol.createSimple({"color": "#e5e7eb", "outline_color": "#ffffff", "outline_width": "0.2"}), "Cubierta"),
    QgsRendererCategory("no_cubierta", QgsFillSymbol.createSimple({"color": "#ea580c", "outline_color": "#ffffff", "outline_width": "0.2"}), "No cubierta"),
    QgsRendererCategory("sin_poblacion", QgsFillSymbol.createSimple({"color": "#fafafa", "outline_color": "#ffffff", "outline_width": "0.2"}), "Sin población")]))
b_v = vias.clone()
b_v.setSubsetString("\"jerarquia\" IN ('troncal','principal')")
simple(b_v, QgsLineSymbol.createSimple({"color": "#9ca3af", "width": "0.35"}))
b_r = rios.clone()
b_r.setSubsetString("\"tipo\" = 'rio'")
simple(b_r, QgsLineSymbol.createSimple({"color": "#93c5fd", "width": "0.5"}))
b_e = salud.clone()
simple(b_e, QgsMarkerSymbol.createSimple({"color": "#1e3a8a", "size": "1.6", "outline_color": "white", "outline_width": "0.3"}))
b_c = comunas.clone()
simple(b_c, QgsFillSymbol.createSimple({"color": "255,255,255,0", "outline_color": "#6b7280", "outline_width": "0.5"}))
etiquetas(b_c, "upper(\"nombre\")", 8, "#4b5563")
img_b = render([b_e, b_c, b_r, b_v, b_z], ext_pob, 900, 950)
titulo(img_b, "Después · una figura, un fondo", "El tema (zonas sin cobertura) destaca; el contexto acompaña en grises")
lado_a_lado([img_a, img_b], "4-5-jerarquia-antes-despues.png", "Mismos datos, distinta jerarquía visual. © colaboradores de OpenStreetMap · WorldPop")

# ------------------------------------------------------------ 4.7 / 4.8 composición A4
for lyr in [b_z, b_v, b_r, b_e, b_c]:
    proj.addMapLayer(lyr, False)
loc_m = munis.clone()
simple(loc_m, QgsFillSymbol.createSimple(GRIS_FONDO))
loc_l = limite.clone()
simple(loc_l, QgsFillSymbol.createSimple({"color": "#ea580c", "outline_color": "#9a3412", "outline_width": "0.3"}))
proj.addMapLayer(loc_m, False)
proj.addMapLayer(loc_l, False)

lay = QgsPrintLayout(proj)
lay.initializeDefaults()
lay.setName("A4 horizontal · cobertura")
pag = lay.pageCollection().page(0)
pag.setPageSize("A4", QgsLayoutItemPage.Orientation.Landscape)


def etiqueta_lay(texto, x, y, w, h, tam, negrita=False, color="#111827"):
    it = QgsLayoutItemLabel(lay)
    it.setText(texto)
    f = QgsTextFormat()
    fnt = QFont(FUENTE)
    fnt.setBold(negrita)
    f.setFont(fnt)
    f.setSize(tam)
    f.setColor(QColor(color))
    it.setTextFormat(f)
    lay.addLayoutItem(it)
    it.attemptMove(QgsLayoutPoint(x, y, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    it.attemptResize(QgsLayoutSize(w, h, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    return it


mapa = QgsLayoutItemMap(lay)
mapa.setLayers([b_e, b_c, b_r, b_v, b_z])
mapa.setCrs(UTM19)
lay.addLayoutItem(mapa)
mapa.attemptMove(QgsLayoutPoint(10, 24, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
mapa.attemptResize(QgsLayoutSize(190, 176, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
mapa.zoomToExtent(ext_pob)
mapa.setFrameEnabled(True)
mapa.setFrameStrokeColor(QColor("#9ca3af"))

loc = QgsLayoutItemMap(lay)
loc.setLayers([loc_l, loc_m])
loc.setCrs(UTM19)
lay.addLayoutItem(loc)
loc.attemptMove(QgsLayoutPoint(210, 24, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
loc.attemptResize(QgsLayoutSize(77, 55, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
ext_loc = QgsRectangle(munis.extent())
ext_loc.scale(1.05)
loc.zoomToExtent(ext_loc)
loc.setFrameEnabled(True)
loc.setFrameStrokeColor(QColor("#9ca3af"))
ov = QgsLayoutItemMapOverview("marco", loc)
ov.setLinkedMap(mapa)
ov.setFrameSymbol(QgsFillSymbol.createSimple({"color": "255,255,255,0", "outline_color": "#111827", "outline_width": "0.6"}))
loc.overviews().addOverview(ov)

etiqueta_lay("¿Quién vive a más de 1 km de un establecimiento de salud?", 10, 7, 277, 10, 18, True)
etiqueta_lay("Municipio de Cochabamba · zonas de 1 km² · 2020", 10, 15, 200, 7, 10, False, "#4b5563")
etiqueta_lay("Localización en la región metropolitana", 210, 80, 77, 6, 8, False, "#4b5563")

leg = QgsLayoutItemLegend(lay)
leg.setLinkedMap(mapa)
leg.setTitle("Leyenda")
leg.setSyncMode(Qgis.LegendSyncMode.Manual)
for estilo, tam, negrita in [(QgsLegendStyle.Style.Title, 11, True), (QgsLegendStyle.Style.Group, 9, True),
                             (QgsLegendStyle.Style.Subgroup, 9, True), (QgsLegendStyle.Style.SymbolLabel, 8.5, False)]:
    tf = QgsTextFormat()
    fl = QFont(FUENTE)
    fl.setBold(negrita)
    tf.setFont(fl)
    tf.setSize(tam)
    leg.rstyle(estilo).setTextFormat(tf)
modelo = leg.model().rootGroup()
modelo.clear()
for lyr, nombre in [(b_z, "Zonas de análisis"), (b_e, "Establecimiento de salud"), (b_c, "Comuna"), (b_v, "Vía principal"), (b_r, "Río")]:
    nodo = modelo.addLayer(lyr)
    nodo.setName(nombre)
lay.addLayoutItem(leg)
leg.attemptMove(QgsLayoutPoint(210, 90, QgsUnitTypes.LayoutUnit.LayoutMillimeters))

barra = QgsLayoutItemScaleBar(lay)
barra.setStyle("Single Box")
barra.setLinkedMap(mapa)
barra.setUnits(Qgis.DistanceUnit.Kilometers)
barra.setNumberOfSegments(4)
barra.setNumberOfSegmentsLeft(0)
barra.setUnitsPerSegment(1)
barra.setUnitLabel("km")
tfb = QgsTextFormat()
tfb.setFont(QFont(FUENTE))
tfb.setSize(8)
barra.setTextFormat(tfb)
lay.addLayoutItem(barra)
barra.attemptMove(QgsLayoutPoint(14, 188, QgsUnitTypes.LayoutUnit.LayoutMillimeters))

norte = QgsLayoutItemPicture(lay)
svg = os.path.join(QgsApplication.svgPaths()[0], "arrows", "NorthArrow_02.svg")
if os.path.exists(svg):
    norte.setPicturePath(svg)
    lay.addLayoutItem(norte)
    norte.attemptMove(QgsLayoutPoint(186, 28, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    norte.attemptResize(QgsLayoutSize(10, 12, QgsUnitTypes.LayoutUnit.LayoutMillimeters))

etiqueta_lay("Zona cubierta: su punto interior está a menos de 1 km (en línea recta) de un establecimiento de salud.\n"
             "≈ 90 000 habitantes (15 %) viven en zonas no cubiertas.", 210, 162, 77, 16, 7.5, False, "#374151")
etiqueta_lay("Fuentes: © colaboradores de OpenStreetMap (ODbL), extracto 08-10-2026; WorldPop 2020 (CC BY 4.0).\n"
             "SRC: WGS 84 / UTM 19 S (EPSG:32719). Elaboración: Curso Introductorio de QGIS.", 210, 178, 77, 18, 6.5, False, "#6b7280")

exp = QgsLayoutExporter(lay)
cfg = QgsLayoutExporter.ImageExportSettings()
cfg.dpi = 110
exp.exportToImage(os.path.join(FIG, "4-7-composicion-a4.png"), cfg)
print("figura 4-7-composicion-a4.png")
lay.saveAsTemplate(os.path.join(SOL, "plantilla_a4_cobertura.qpt"), QgsReadWriteContext())

# ------------------------------------------------------------ 4.10 atlas por comuna
atlas_cov = com_mem.clone()
simple(atlas_cov, QgsFillSymbol.createSimple({"color": "255,255,255,0", "outline_color": "#111827", "outline_width": "0.8"}))
proj.addMapLayer(atlas_cov, False)
lay2 = QgsPrintLayout(proj)
lay2.initializeDefaults()
lay2.pageCollection().page(0).setPageSize("A4", QgsLayoutItemPage.Orientation.Portrait)
m2 = QgsLayoutItemMap(lay2)
m2.setLayers([atlas_cov, b_e, b_r, b_v, b_z])
m2.setCrs(UTM19)
lay2.addLayoutItem(m2)
m2.attemptMove(QgsLayoutPoint(10, 30, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
m2.attemptResize(QgsLayoutSize(190, 200, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
m2.setAtlasDriven(True)
m2.setAtlasScalingMode(QgsLayoutItemMap.AtlasScalingMode.Auto)
m2.setAtlasMargin(0.08)
m2.setFrameEnabled(True)
t2 = QgsLayoutItemLabel(lay2)
t2.setText("[% upper(\"nombre\") %]")
f2 = QgsTextFormat()
fb = QFont(FUENTE)
fb.setBold(True)
f2.setFont(fb)
f2.setSize(22)
t2.setTextFormat(f2)
lay2.addLayoutItem(t2)
t2.attemptMove(QgsLayoutPoint(10, 8, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
t2.attemptResize(QgsLayoutSize(190, 12, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
t3 = QgsLayoutItemLabel(lay2)
t3.setText("Comuna [% \"cod\" %] · Población 2020: [% replace(format_number(\"pob\", 0), ',', ' ') %] hab. · "
           "Densidad: [% replace(format_number(\"dens\", 0), ',', ' ') %] hab./km²")
f3 = QgsTextFormat()
f3.setFont(QFont(FUENTE))
f3.setSize(10)
t3.setTextFormat(f3)
lay2.addLayoutItem(t3)
t3.attemptMove(QgsLayoutPoint(10, 21, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
t3.attemptResize(QgsLayoutSize(190, 8, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
t4 = QgsLayoutItemLabel(lay2)
t4.setText("Zonas de análisis habitadas sin cobertura de salud a 1 km: "
           "[% aggregate(layer:='Zonas (cobertura)', aggregate:='count', expression:=\"cod_zona\", "
           "filter:=\"cod_comuna\" = attribute(@atlas_feature, 'cod') AND \"estado\" = 'no_cubierta') %]\n"
           "Población en esas zonas: "
           "[% replace(format_number(coalesce(aggregate(layer:='Zonas (cobertura)', aggregate:='sum', expression:=\"pob\", "
           "filter:=\"cod_comuna\" = attribute(@atlas_feature, 'cod') AND \"estado\" = 'no_cubierta'), 0), 0), ',', ' ') %] hab.\n\n"
           "Fuentes: © colaboradores de OpenStreetMap (ODbL); WorldPop 2020 (CC BY 4.0). SRC: EPSG:32719.\n"
           "Página [% @atlas_featurenumber %] de [% @atlas_totalfeatures %] · Atlas de cobertura de salud · Curso Introductorio de QGIS")
f4 = QgsTextFormat()
f4.setFont(QFont(FUENTE))
f4.setSize(10)
t4.setTextFormat(f4)
lay2.addLayoutItem(t4)
t4.attemptMove(QgsLayoutPoint(10, 190, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
t4.attemptResize(QgsLayoutSize(190, 45, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
proj.addMapLayer(z_mem, False)
atlas = lay2.atlas()
atlas.setCoverageLayer(atlas_cov)
atlas.setEnabled(True)
atlas.setSortFeatures(True)
atlas.setSortExpression("\"cod\"")
atlas.beginRender()
miniaturas = []
cfg2 = QgsLayoutExporter.ImageExportSettings()
cfg2.dpi = 40
for i in range(atlas.count()):
    atlas.seekTo(i)
    ruta = os.path.join(SOL, f"atlas_{i + 1}.png")
    QgsLayoutExporter(lay2).exportToImage(ruta, cfg2)
    miniaturas.append(QImage(ruta))
atlas.endRender()
cols = 3
w, h = miniaturas[0].width(), miniaturas[0].height()
grid = QImage(cols * w + (cols + 1) * 12, 2 * h + 3 * 12, QImage.Format.Format_ARGB32)
grid.fill(QColor("#e5e7eb"))
p = QPainter(grid)
for i, im in enumerate(miniaturas):
    p.drawImage(12 + (i % cols) * (w + 12), 12 + (i // cols) * (h + 12), im)
p.end()
grid.save(os.path.join(FIG, "4-10-atlas-miniaturas.png"))
print("figura 4-10-atlas-miniaturas.png")
atlas_pdf = QgsLayoutExporter.PdfExportSettings()
QgsLayoutExporter.exportToPdf(atlas, os.path.join(SOL, "atlas_comunas.pdf"), atlas_pdf)

app.exitQgis()
