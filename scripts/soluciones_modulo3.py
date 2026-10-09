"""Calcula las cifras de referencia de los laboratorios del Módulo 3.

Se ejecuta con el Python de QGIS 4.x sobre el paquete generado:

    python-qgis scripts/soluciones_modulo3.py PAQUETE

Escribe en PAQUETE/../soluciones/ las capas resultantes y un resumen
`cifras_modulo3.json` que sirve para verificar los resultados de los estudiantes.
"""
import json
import os
import sys
from collections import Counter, defaultdict

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from osgeo import gdal
from qgis.core import (QgsApplication, QgsVectorLayer, QgsRasterLayer, QgsProcessingFeedback,
                       QgsFeatureRequest)
from qgis.analysis import QgsNativeAlgorithms

gdal.UseExceptions()
PAQ = os.path.abspath(sys.argv[1])
ORIG = os.path.join(PAQ, "datos", "originales")
EJER = os.path.join(PAQ, "datos", "ejercicios")
SOL = os.path.join(os.path.dirname(PAQ), "soluciones")
os.makedirs(SOL, exist_ok=True)

app = QgsApplication([], False)
app.initQgis()
sys.path.append(os.path.join(QgsApplication.prefixPath(), "python", "plugins"))
import processing  # noqa: E402
from processing.core.Processing import Processing  # noqa: E402
Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
fb = QgsProcessingFeedback()


def run(alg, params):
    return processing.run(alg, params, feedback=fb)


def capa(ruta, nombre=None):
    lyr = QgsVectorLayer(ruta, nombre or os.path.basename(ruta), "ogr")
    assert lyr.isValid(), ruta
    return lyr


LIM = os.path.join(ORIG, "limites.gpkg")
cifras = {}

# ------------------------------------------------------------ 3.1 auditoría
aud = capa(os.path.join(EJER, "equipamientos_auditoria.gpkg") + "|layername=equipamientos")
feats = list(aud.getFeatures())
ids = Counter(f["id_equip"] for f in feats)
geoms = Counter(f.geometry().asWkt(2) for f in feats)
cifras["3.1"] = {
    "entidades": len(feats),
    "id_repetidos": sum(1 for v in ids.values() if v > 1),
    "geometrias_repetidas": sum(1 for v in geoms.values() if v > 1),
    "nombre_nulo": sum(1 for f in feats if not f["nombre"]),
    "grafias_tipo": sorted({f["tipo"] for f in feats}),
    "grafias_estado": sorted({str(f["estado"]) for f in feats}),
    "capacidad_valores_no_validos": dict(Counter(f["capacidad"] for f in feats
                                                 if not (str(f["capacidad"]).isdigit() and int(f["capacidad"]) > 0))),
}

# ------------------------------------------------------------ equipamientos en UTM
csv_uri = ("file:///" + os.path.join(ORIG, "equipamientos.csv").replace("\\", "/") +
           "?delimiter=;&decimalPoint=,&xField=longitud&yField=latitud&crs=EPSG:4326&encoding=UTF-8")
eq_csv = QgsVectorLayer(csv_uri, "eq", "delimitedtext")
eq = run("native:reprojectlayer", {"INPUT": eq_csv, "TARGET_CRS": "EPSG:32719",
                                   "OUTPUT": os.path.join(SOL, "equipamientos.gpkg")})["OUTPUT"]
eq = capa(eq)

# ------------------------------------------------------------ 3.5 y 3.6 conteos por comuna
comunas = capa(LIM + "|layername=comunas")
zonas = capa(LIM + "|layername=zonas_analisis")
pob_comuna = defaultdict(int)
for z in zonas.getFeatures():
    pob_comuna[z["cod_comuna"]] += z["pob_2020"]
cont = run("native:countpointsinpolygon", {"POLYGONS": comunas, "POINTS": eq, "FIELD": "n_equip",
                                           "OUTPUT": "memory:"})["OUTPUT"]
salud = run("native:extractbyattribute", {"INPUT": eq, "FIELD": "tipo", "OPERATOR": 0, "VALUE": "salud",
                                          "OUTPUT": "memory:"})["OUTPUT"]
educ = run("native:extractbyattribute", {"INPUT": eq, "FIELD": "tipo", "OPERATOR": 0, "VALUE": "educacion",
                                         "OUTPUT": "memory:"})["OUTPUT"]
cs = run("native:countpointsinpolygon", {"POLYGONS": comunas, "POINTS": salud, "FIELD": "n", "OUTPUT": "memory:"})["OUTPUT"]
ce = run("native:countpointsinpolygon", {"POLYGONS": comunas, "POINTS": educ, "FIELD": "n", "OUTPUT": "memory:"})["OUTPUT"]
tabla = {}
for f in cont.getFeatures():
    tabla[f["cod_comuna"]] = {"nombre": f["nombre"], "area_km2": f["area_km2"], "equip": f["n_equip"],
                              "pob_2020": pob_comuna[f["cod_comuna"]]}
for f in cs.getFeatures():
    tabla[f["cod_comuna"]]["salud"] = f["n"]
for f in ce.getFeatures():
    tabla[f["cod_comuna"]]["educacion"] = f["n"]
for c in tabla.values():
    c["hab_por_salud"] = round(c["pob_2020"] / c["salud"]) if c["salud"] else None
cifras["3.6"] = {"por_comuna": tabla, "total_salud": salud.featureCount(), "total_educacion": educ.featureCount()}

# ------------------------------------------------------------ 3.7 cobertura de salud a 1 km
buf = run("native:buffer", {"INPUT": salud, "DISTANCE": 1000, "SEGMENTS": 16, "DISSOLVE": True,
                            "OUTPUT": os.path.join(SOL, "salud_buffer_1km.gpkg")})["OUTPUT"]
buf = capa(buf)
union = next(buf.getFeatures()).geometry()
pob_total = sum(z["pob_2020"] for z in zonas.getFeatures())
sin = [z for z in zonas.getFeatures() if z["pob_2020"] > 0 and not union.contains(z.geometry().pointOnSurface())]
area_muni = sum(f.geometry().area() for f in capa(LIM + "|layername=limite_municipal").getFeatures())
area_cub = union.intersection(next(capa(LIM + "|layername=limite_municipal").getFeatures()).geometry()).area()
cifras["3.7"] = {
    "zonas_habitadas_sin_cobertura": len(sin),
    "poblacion_sin_cobertura": sum(z["pob_2020"] for z in sin),
    "porcentaje_poblacion_sin_cobertura": round(100 * sum(z["pob_2020"] for z in sin) / pob_total, 1),
    "porcentaje_area_municipal_cubierta": round(100 * area_cub / area_muni, 1),
    "poblacion_total_zonas": pob_total,
}

por_comuna = defaultdict(int)
for z in sin:
    por_comuna[z["cod_comuna"]] += z["pob_2020"]
cifras["3.7"]["sin_cobertura_por_comuna"] = {c: {"pob": v, "pct": round(100 * v / pob_comuna[c], 1)}
                                             for c, v in sorted(por_comuna.items())}


def escenario(filtro, distancia):
    sub = run("native:extractbyexpression", {"INPUT": eq, "EXPRESSION": filtro, "OUTPUT": "memory:"})["OUTPUT"]
    b = run("native:buffer", {"INPUT": sub, "DISTANCE": distancia, "SEGMENTS": 16, "DISSOLVE": True,
                              "OUTPUT": "memory:"})["OUTPUT"]
    u = next(b.getFeatures()).geometry()
    p = sum(z["pob_2020"] for z in zonas.getFeatures()
            if z["pob_2020"] > 0 and not u.contains(z.geometry().pointOnSurface()))
    return {"establecimientos": sub.featureCount(), "pob_sin_cobertura": p, "pct": round(100 * p / pob_total, 1)}


cifras["3.7"]["escenarios"] = {
    "B_hosp_clin_1000": escenario("\"subtipo\" IN ('hospital','clinica')", 1000),
    "C_todos_500": escenario("\"tipo\" = 'salud'", 500),
    "D_hosp_2000": escenario("\"subtipo\" = 'hospital'", 2000),
}

# ------------------------------------------------------------ 3.8 y 3.9 relieve
dem_utm = os.path.join(SOL, "dem_utm_30m.tif")
gdal.Warp(dem_utm, os.path.join(ORIG, "dem_copernicus_30m.tif"), dstSRS="EPSG:32719", xRes=30, yRes=30,
          resampleAlg="bilinear", targetAlignedPixels=True)
pend = os.path.join(SOL, "pendiente_pct.tif")
gdal.DEMProcessing(pend, dem_utm, "slope", slopeFormat="percent")
zs = run("native:zonalstatisticsfb", {"INPUT": comunas, "INPUT_RASTER": pend, "RASTER_BAND": 1,
                                      "COLUMN_PREFIX": "p_", "STATISTICS": [2, 3, 5, 6],
                                      "OUTPUT": os.path.join(SOL, "comunas_pendiente.gpkg")})["OUTPUT"]
zs = capa(zs)
cifras["3.9"] = {f["nombre"]: {"media": round(f["p_mean"], 1), "mediana": round(f["p_median"], 1),
                               "max": round(f["p_max"], 1)} for f in zs.getFeatures()}
ds = gdal.Open(pend)
arr = ds.GetRasterBand(1).ReadAsArray()
valid = arr[arr >= 0]
cifras["3.9"]["pct_celdas_pendiente_mayor_15"] = round(100 * float((valid > 15).sum()) / valid.size, 1)
zz = run("native:zonalstatisticsfb", {"INPUT": zonas, "INPUT_RASTER": pend, "RASTER_BAND": 1,
                                      "COLUMN_PREFIX": "p_", "STATISTICS": [2], "OUTPUT": "memory:"})["OUTPUT"]
pend_zona = {f["cod_zona"]: f["p_mean"] for f in zz.getFeatures()}

planas = sorted([(z["cod_zona"], z["cod_comuna"], z["pob_2020"], round(pend_zona[z["cod_zona"]], 1))
                 for z in sin if (pend_zona.get(z["cod_zona"]) or 99) < 15], key=lambda t: -t[2])
cifras["3.9"]["reto_sin_cobertura_planas"] = {"n": len(planas), "top5": planas[:5]}

# ------------------------------------------------------------ 3.12 decisión territorial
vias = capa(os.path.join(ORIG, "vias.gpkg") + "|layername=vias")
princ = run("native:extractbyexpression", {"INPUT": vias, "EXPRESSION": "\"jerarquia\" IN ('troncal','principal')",
                                           "OUTPUT": "memory:"})["OUTPUT"]
vbuf = run("native:buffer", {"INPUT": princ, "DISTANCE": 500, "DISSOLVE": True, "OUTPUT": "memory:"})["OUTPUT"]
vgeom = next(vbuf.getFeatures()).geometry()
cand = []
for z in sin:
    dens = z["pob_2020"] / z["area_km2"]
    if dens >= 3000 and (pend_zona.get(z["cod_zona"]) or 99) < 15 and vgeom.intersects(z.geometry()):
        cand.append((z["cod_zona"], z["cod_comuna"], z["pob_2020"], round(pend_zona[z["cod_zona"]], 1)))
cand.sort(key=lambda t: -t[2])
# Criterios de cada candidata: distancia al establecimiento de salud más cercano y a vía principal
salud_geoms = [f.geometry() for f in salud.getFeatures()]
princ_geom = next(run("native:dissolve", {"INPUT": princ, "OUTPUT": "memory:"})["OUTPUT"].getFeatures()).geometry()
zgeom = {z["cod_zona"]: z.geometry() for z in zonas.getFeatures()}
detalle = []
for cod, com, pob, pe in cand:
    c = zgeom[cod].pointOnSurface()
    detalle.append({"zona": cod, "comuna": com, "pob": pob, "pendiente": pe,
                    "dist_salud_m": round(min(c.distance(g) for g in salud_geoms)),
                    "dist_via_m": round(c.distance(princ_geom))})
cifras["3.12_detalle"] = detalle
cifras["3.12"] = {"criterios": "sin cobertura 1 km, densidad >= 3000 hab/km2, pendiente media < 15 %, a <= 500 m de vía principal",
                  "zonas_candidatas": len(cand), "top5": cand[:5]}

with open(os.path.join(SOL, "cifras_modulo3.json"), "w", encoding="utf-8") as fh:
    json.dump(cifras, fh, ensure_ascii=False, indent=2)
print(json.dumps(cifras, ensure_ascii=False, indent=1))
app.exitQgis()
