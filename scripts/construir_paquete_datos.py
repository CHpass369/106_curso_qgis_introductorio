"""Construye el paquete de datos del curso (caso Cochabamba).

Se ejecuta con el Python de QGIS 4.x, que trae GDAL y PROJ:

    Windows:  "C:\\Program Files\\QGIS 4.2.1\\bin\\python-qgis.bat" scripts/construir_paquete_datos.py FUENTES SALIDA
    Linux:    python3 scripts/construir_paquete_datos.py FUENTES SALIDA

FUENTES debe contener (ver docs/descargas/index.md, sección «Cómo se construyó»):

    bolivia-AAMMDD.osm.pbf            Geofabrik, extracto de OpenStreetMap para Bolivia
    cop30_S18_W067.tif                Copernicus DEM GLO-30, tesela S18 W067
    bol_ppp_2020_constrained.tif      WorldPop 2020, población 100 m (restringida)

La imagen Sentinel-2 se lee directamente desde el catálogo abierto de AWS.

SALIDA será la carpeta `curso-qgis/` lista para comprimir.
"""
import csv
import datetime
import glob
import math
import os
import random
import shutil
import sys

from osgeo import gdal, ogr, osr

gdal.UseExceptions()
ogr.UseExceptions()

FUENTES, SALIDA = (os.path.abspath(a) for a in sys.argv[1:3])
ORIG = os.path.join(SALIDA, "datos", "originales")
EJER = os.path.join(SALIDA, "datos", "ejercicios")
TMP = os.path.join(FUENTES, "_tmp")

ID_MUNICIPIO = "4503297"          # relación OSM del municipio de Cochabamba
ID_KANATA = "4582422"             # región metropolitana Kanata
BBOX = (-66.40, -17.55, -65.95, -17.20)
BBOX_IMAGEN = (-66.215, -17.435, -66.100, -17.350)   # área urbana central
S2_ESCENA = ("https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/"
             "19/K/GA/2025/7/S2C_19KGA_20250716_0_L2A/{banda}.tif")
EPSG_TRABAJO = 32719              # WGS 84 / UTM zona 19 S
random.seed(2026)


def srs(epsg):
    s = osr.SpatialReference()
    s.ImportFromEPSG(epsg)
    s.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)
    return s


def transformador(a, b):
    return osr.CoordinateTransformation(srs(a), srs(b))


def preparar_carpetas():
    if os.path.exists(SALIDA):
        shutil.rmtree(SALIDA)
    for sub in ["datos/originales", "datos/ejercicios", "datos/trabajo", "proyectos",
                "estilos", "salidas", "documentos"]:
        os.makedirs(os.path.join(SALIDA, sub))
    os.makedirs(TMP, exist_ok=True)


def extraer_osm():
    """Extrae del PBF las capas con filtro espacial a un GeoPackage temporal."""
    destino = os.path.join(TMP, "osm.gpkg")
    if os.path.exists(destino):
        return destino
    pbf = sorted(glob.glob(os.path.join(FUENTES, "bolivia-*.osm.pbf")))[-1]
    gdal.SetConfigOption("OGR_INTERLEAVED_READING", "YES")
    for capa in ["multipolygons", "lines", "points"]:
        gdal.VectorTranslate(destino, pbf, format="GPKG", layers=[capa], layerName=capa,
                             spatFilter=list(BBOX),
                             accessMode="append" if os.path.exists(destino) else None)
    return destino


def geometria_relacion(osm, osm_id):
    ds = ogr.Open(osm)
    lyr = ds.GetLayerByName("multipolygons")
    lyr.SetAttributeFilter(f"osm_id = '{osm_id}'")
    f = lyr.GetNextFeature()
    return f.GetGeometryRef().Clone()


def proyectar(geom, de=4326, a=EPSG_TRABAJO):
    g = geom.Clone()
    g.Transform(transformador(de, a))
    return g


def nueva_capa(ds, nombre, tipo_geom, epsg, campos):
    lyr = ds.CreateLayer(nombre, srs(epsg), tipo_geom, options=["FID=fid"])
    for nombre_campo, tipo, ancho in campos:
        fd = ogr.FieldDefn(nombre_campo, tipo)
        if ancho:
            fd.SetWidth(ancho)
        lyr.CreateField(fd)
    return lyr


# ---------------------------------------------------------------- límites

def construir_limites(osm):
    muni = geometria_relacion(osm, ID_MUNICIPIO)
    kanata = geometria_relacion(osm, ID_KANATA)
    ruta = os.path.join(ORIG, "limites.gpkg")
    ds = ogr.GetDriverByName("GPKG").CreateDataSource(ruta)
    ds_osm = ogr.Open(osm)
    src = ds_osm.GetLayerByName("multipolygons")

    # Municipios de la región metropolitana (contexto)
    lyr = nueva_capa(ds, "municipios_metropolitanos", ogr.wkbMultiPolygon, EPSG_TRABAJO,
                     [("osm_id", ogr.OFTString, 20), ("nombre", ogr.OFTString, 80)])
    src.SetAttributeFilter("boundary = 'administrative' AND admin_level = '8'")
    for f in src:
        g = f.GetGeometryRef()
        if g.Centroid().Within(kanata):
            nf = ogr.Feature(lyr.GetLayerDefn())
            nf.SetField("osm_id", f.GetField("osm_id"))
            nf.SetField("nombre", f.GetField("name"))
            nf.SetGeometry(ogr.ForceToMultiPolygon(proyectar(g)))
            lyr.CreateFeature(nf)

    # Límite municipal
    lyr = nueva_capa(ds, "limite_municipal", ogr.wkbMultiPolygon, EPSG_TRABAJO,
                     [("nombre", ogr.OFTString, 80), ("departamento", ogr.OFTString, 40),
                      ("area_km2", ogr.OFTReal, 0)])
    g = ogr.ForceToMultiPolygon(proyectar(muni))
    nf = ogr.Feature(lyr.GetLayerDefn())
    nf.SetField("nombre", "Cochabamba")
    nf.SetField("departamento", "Cochabamba")
    nf.SetField("area_km2", round(g.GetArea() / 1e6, 2))
    nf.SetGeometry(g)
    lyr.CreateFeature(nf)

    # Comunas (subdivisión municipal, admin_level 9)
    lyr = nueva_capa(ds, "comunas", ogr.wkbMultiPolygon, EPSG_TRABAJO,
                     [("cod_comuna", ogr.OFTString, 6), ("nombre", ogr.OFTString, 60),
                      ("area_km2", ogr.OFTReal, 0)])
    src.SetAttributeFilter("boundary = 'administrative' AND admin_level = '9'")
    comunas = []
    for f in src:
        gg = f.GetGeometryRef()
        if gg.Centroid().Within(muni) and gg.Intersection(muni).GetArea() > 0.5 * gg.GetArea():
            comunas.append((f.GetField("name"), proyectar(gg)))
    comunas.sort(key=lambda c: c[0])
    for i, (nombre, gg) in enumerate(comunas, 1):
        nf = ogr.Feature(lyr.GetLayerDefn())
        nf.SetField("cod_comuna", f"C{i:02d}")
        nf.SetField("nombre", nombre)
        nf.SetField("area_km2", round(gg.GetArea() / 1e6, 2))
        nf.SetGeometry(ogr.ForceToMultiPolygon(gg))
        lyr.CreateFeature(nf)
    ds = None
    return muni, proyectar(muni), comunas


def solo_poligonos(g):
    """Conserva solo las partes poligonales de una intersección."""
    if g is None or g.IsEmpty():
        return None
    if g.GetGeometryType() in (ogr.wkbPolygon, ogr.wkbMultiPolygon):
        return g
    mp = ogr.Geometry(ogr.wkbMultiPolygon)
    for i in range(g.GetGeometryCount()):
        parte = g.GetGeometryRef(i)
        if parte.GetGeometryType() == ogr.wkbPolygon:
            mp.AddGeometry(parte)
        elif parte.GetGeometryType() == ogr.wkbMultiPolygon:
            for j in range(parte.GetGeometryCount()):
                mp.AddGeometry(parte.GetGeometryRef(j))
    return mp if mp.GetGeometryCount() else None


def malla_hexagonal(muni_utm, comunas, poblacion_utm_tif):
    """Zonas de análisis: hexágonos de 1 km² recortados al municipio, con población estimada."""
    area = 1_000_000.0
    lado = math.sqrt(2 * area / (3 * math.sqrt(3)))
    w, h = 2 * lado, math.sqrt(3) * lado
    xmin, xmax, ymin, ymax = muni_utm.GetEnvelope()
    ruta = os.path.join(ORIG, "limites.gpkg")
    ds = ogr.Open(ruta, 1)
    lyr = nueva_capa(ds, "zonas_analisis", ogr.wkbMultiPolygon, EPSG_TRABAJO,
                     [("cod_zona", ogr.OFTString, 8), ("cod_comuna", ogr.OFTString, 6),
                      ("area_km2", ogr.OFTReal, 0), ("pob_2020", ogr.OFTInteger, 0)])
    rast = gdal.Open(poblacion_utm_tif)
    gt = rast.GetGeoTransform()
    banda = rast.GetRasterBand(1).ReadAsArray()
    n = 0
    col = 0
    x = xmin
    while x < xmax + w:
        y = ymin - (h / 2 if col % 2 else 0)
        while y < ymax + h:
            anillo = ogr.Geometry(ogr.wkbLinearRing)
            for k in range(7):
                ang = math.radians(60 * k)
                anillo.AddPoint_2D(x + lado * math.cos(ang), y + lado * math.sin(ang))
            hexa = ogr.Geometry(ogr.wkbPolygon)
            hexa.AddGeometry(anillo)
            recorte = solo_poligonos(hexa.Intersection(muni_utm))
            if recorte and not recorte.IsEmpty() and recorte.GetArea() > 50_000:
                n += 1
                cod = ""
                c = recorte.PointOnSurface()
                for i, (_, gc) in enumerate(comunas, 1):
                    if c.Within(gc):
                        cod = f"C{i:02d}"
                # población: suma de celdas cuyo centro cae en la zona
                exmin, exmax, eymin, eymax = recorte.GetEnvelope()
                c0 = max(0, int((exmin - gt[0]) / gt[1]))
                c1 = min(banda.shape[1], int((exmax - gt[0]) / gt[1]) + 1)
                f0 = max(0, int((eymax - gt[3]) / gt[5]))
                f1 = min(banda.shape[0], int((eymin - gt[3]) / gt[5]) + 1)
                pob = 0.0
                for fi in range(f0, f1):
                    for ci in range(c0, c1):
                        v = banda[fi, ci]
                        if v > 0:
                            p = ogr.Geometry(ogr.wkbPoint)
                            p.AddPoint_2D(gt[0] + (ci + .5) * gt[1], gt[3] + (fi + .5) * gt[5])
                            if p.Within(recorte):
                                pob += float(v)
                nf = ogr.Feature(lyr.GetLayerDefn())
                nf.SetField("cod_zona", f"Z{n:03d}")
                nf.SetField("cod_comuna", cod)
                nf.SetField("area_km2", round(recorte.GetArea() / 1e6, 3))
                nf.SetField("pob_2020", int(round(pob)))
                nf.SetGeometry(ogr.ForceToMultiPolygon(recorte))
                lyr.CreateFeature(nf)
            y += h
        x += 1.5 * lado
        col += 1
    ds = None
    return n


# ---------------------------------------------------------------- equipamientos

SUBTIPOS = {
    "hospital": ("salud", "hospital"), "clinic": ("salud", "clinica"),
    "doctors": ("salud", "consultorio"), "health_post": ("salud", "puesto_salud"),
    "school": ("educacion", "escuela"), "kindergarten": ("educacion", "kinder"),
    "college": ("educacion", "instituto"), "university": ("educacion", "universidad"),
}


def leer_equipamientos(osm, muni):
    ds = ogr.Open(osm)
    vistos, filas = set(), []
    for capa in ["points", "multipolygons"]:
        lyr = ds.GetLayerByName(capa)
        if capa == "multipolygons":
            lyr.SetAttributeFilter("amenity IS NOT NULL")
        else:
            lyr.SetAttributeFilter("other_tags LIKE '%\"amenity\"=>%'")
        for f in lyr:
            otras = f.GetField("other_tags") or ""
            amen = f.GetField("amenity") if capa == "multipolygons" else None
            if not amen and '"amenity"=>"' in otras:
                amen = otras.split('"amenity"=>"')[1].split('"')[0]
            if amen not in SUBTIPOS:
                continue
            g = f.GetGeometryRef()
            p = g.PointOnSurface() if g.GetDimension() == 2 else g.Clone()
            if not p.Within(muni):
                continue
            nombre = (f.GetField("name") or "").strip()
            if capa == "multipolygons":
                oid = f.GetField("osm_id") or f.GetField("osm_way_id")
            else:
                oid = f.GetField("osm_id")
            clave = (nombre.lower(), amen) if nombre else oid
            if clave in vistos:
                continue
            vistos.add(clave)
            tipo, subtipo = SUBTIPOS[amen]
            filas.append({"osm_id": oid, "nombre": nombre, "tipo": tipo, "subtipo": subtipo,
                          "lon": p.GetX(), "lat": p.GetY()})
    filas.sort(key=lambda r: (r["tipo"], r["subtipo"], r["nombre"], r["lon"]))
    for i, r in enumerate(filas, 1):
        r["id_equip"] = f"EQ-{i:04d}"
    return filas


def escribir_tablas_comunas():
    """Tabla sin geometría para la lección 3.5 (uniones) y su versión con problemas de claves."""
    ds = ogr.Open(os.path.join(ORIG, "limites.gpkg"))
    nombres = {f.GetField("cod_comuna"): f.GetField("nombre") for f in ds.GetLayerByName("comunas")}
    pob = {}
    for f in ds.GetLayerByName("zonas_analisis"):
        pob[f.GetField("cod_comuna")] = pob.get(f.GetField("cod_comuna"), 0) + f.GetField("pob_2020")
    ds = None
    with open(os.path.join(ORIG, "poblacion_comunas.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["cod_comuna", "comuna", "pob_2020", "fuente"])
        for cod in sorted(nombres):
            w.writerow([cod, nombres[cod], pob.get(cod, 0), "WorldPop 2020 agregado por zonas de análisis"])
    claves = {"C01": "C1", "C02": " C02", "C03": "c03", "C04": "C04", "C05": "C05", "C06": "C06"}
    with open(os.path.join(EJER, "poblacion_comunas_claves.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["codigo", "comuna", "pob_2020"])
        for cod in sorted(nombres):
            w.writerow([claves[cod], nombres[cod].upper(), pob.get(cod, 0)])
        w.writerow(["C07", "SIN COMUNA", 1250])
        w.writerow(["C05", "TUNARI", pob.get("C05", 0)])


def escribir_mercados(osm, muni):
    """Mercados en GeoJSON (RFC 7946, WGS 84) para practicar ese formato."""
    ds = ogr.Open(osm)
    ruta = os.path.join(ORIG, "mercados.geojson")
    out = ogr.GetDriverByName("GeoJSON").CreateDataSource(ruta)
    lyr = out.CreateLayer("mercados", srs(4326), ogr.wkbPoint, options=["RFC7946=YES"])
    for nombre, tipo, ancho in [("nombre", ogr.OFTString, 120), ("osm_id", ogr.OFTString, 20)]:
        fd = ogr.FieldDefn(nombre, tipo)
        fd.SetWidth(ancho)
        lyr.CreateField(fd)
    for capa, filtro in [("points", "other_tags LIKE '%\"amenity\"=>\"marketplace\"%'"),
                         ("multipolygons", "amenity = 'marketplace'")]:
        src = ds.GetLayerByName(capa)
        src.SetAttributeFilter(filtro)
        for f in src:
            g = f.GetGeometryRef()
            p = g.PointOnSurface() if g.GetDimension() == 2 else g.Clone()
            if not p.Within(muni):
                continue
            nf = ogr.Feature(lyr.GetLayerDefn())
            nf.SetField("nombre", f.GetField("name"))
            nf.SetField("osm_id", f.GetField("osm_id") or (f.GetField("osm_way_id") if capa == "multipolygons" else None))
            nf.SetGeometry(p)
            lyr.CreateFeature(nf)
    out = None


def escribir_csv_equipamientos(filas, fecha):
    ruta = os.path.join(ORIG, "equipamientos.csv")
    with open(ruta, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["id_equip", "nombre", "tipo", "subtipo", "longitud", "latitud", "fuente", "fecha"])
        for r in filas:
            w.writerow([r["id_equip"], r["nombre"] or "", r["tipo"], r["subtipo"],
                        f"{r['lon']:.6f}".replace(".", ","), f"{r['lat']:.6f}".replace(".", ","),
                        "OpenStreetMap", fecha])


def escribir_csv_errores(filas, fecha):
    """Versión con errores típicos para las lecciones 2.5 y 2.7."""
    ruta = os.path.join(EJER, "equipamientos_errores.csv")
    muestra = [dict(r) for r in filas]
    n = len(muestra)
    intercambiadas = random.sample(range(n), max(5, n // 30))
    sin_coord = random.sample([i for i in range(n) if i not in intercambiadas], 3)
    for i in intercambiadas:
        muestra[i]["lon"], muestra[i]["lat"] = muestra[i]["lat"], muestra[i]["lon"]
    duplicados = random.sample(range(n), 4)
    with open(ruta, "w", newline="", encoding="latin-1", errors="replace") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["Código", "Nombre del establecimiento", "Tipo", "Subtipo", "Longitud", "Latitud", "Capacidad"])
        for i, r in enumerate(muestra):
            lon = "" if i in sin_coord else f"{r['lon']:.6f}".replace(".", ",")
            lat = "S/D" if i in sin_coord else f"{r['lat']:.6f}".replace(".", ",")
            tipo = random.choice([r["tipo"], r["tipo"].upper(), r["tipo"].capitalize() + " "])
            capacidad = random.choice(["", "S/D", str(random.randint(20, 900)), "0"])
            fila = [r["id_equip"], r["nombre"], tipo, r["subtipo"], lon, lat, capacidad]
            w.writerow(fila)
            if i in duplicados:
                w.writerow(fila)


def escribir_auditoria(filas):
    """GeoPackage con problemas de calidad para la lección 3.1."""
    ruta = os.path.join(EJER, "equipamientos_auditoria.gpkg")
    ds = ogr.GetDriverByName("GPKG").CreateDataSource(ruta)
    lyr = nueva_capa(ds, "equipamientos", ogr.wkbPoint, EPSG_TRABAJO,
                     [("id_equip", ogr.OFTString, 10), ("nombre", ogr.OFTString, 200),
                      ("tipo", ogr.OFTString, 20), ("subtipo", ogr.OFTString, 20),
                      ("capacidad", ogr.OFTString, 10), ("estado", ogr.OFTString, 20)])
    t = transformador(4326, EPSG_TRABAJO)
    n = len(filas)
    ids_repetidos = set(random.sample(range(1, n), 3))
    geom_repetidas = set(random.sample(range(n), 4))
    for i, r in enumerate(filas):
        p = ogr.Geometry(ogr.wkbPoint)
        p.AddPoint_2D(r["lon"], r["lat"])
        p.Transform(t)
        copias = 2 if i in geom_repetidas else 1
        for _ in range(copias):
            f = ogr.Feature(lyr.GetLayerDefn())
            f.SetField("id_equip", filas[i - 1]["id_equip"] if i in ids_repetidos else r["id_equip"])
            if r["nombre"] and random.random() > 0.04:
                f.SetField("nombre", r["nombre"])
            f.SetField("tipo", random.choice([r["tipo"], r["tipo"].upper(), " " + r["tipo"]]))
            f.SetField("subtipo", r["subtipo"])
            f.SetField("capacidad", random.choice(["", "S/D", str(random.randint(20, 900)), "-1"]))
            f.SetField("estado", random.choice(["ACTIVO", "Activo", "activo", "CERRADO", None]))
            f.SetGeometry(p)
            lyr.CreateFeature(f)
    ds = None


# ---------------------------------------------------------------- vías y ríos

JERARQUIA = {
    "motorway": "troncal", "trunk": "troncal", "primary": "principal", "secondary": "principal",
    "tertiary": "secundaria", "unclassified": "local", "residential": "local", "living_street": "local",
    "motorway_link": "troncal", "trunk_link": "troncal", "primary_link": "principal",
    "secondary_link": "principal", "tertiary_link": "secundaria",
}


def construir_vias_rios(osm, muni):
    ds = ogr.Open(osm)
    zona = muni.Buffer(0.005)
    # Vías -> GeoPackage en UTM 19 S
    out = ogr.GetDriverByName("GPKG").CreateDataSource(os.path.join(ORIG, "vias.gpkg"))
    lv = nueva_capa(out, "vias", ogr.wkbMultiLineString, EPSG_TRABAJO,
                    [("osm_id", ogr.OFTString, 20), ("nombre", ogr.OFTString, 200),
                     ("clase_osm", ogr.OFTString, 20), ("jerarquia", ogr.OFTString, 12)])
    lyr = ds.GetLayerByName("lines")
    lyr.SetAttributeFilter("highway IS NOT NULL")
    for f in lyr:
        clase = f.GetField("highway")
        if clase not in JERARQUIA:
            continue
        g = f.GetGeometryRef()
        if not g.Intersects(zona):
            continue
        g = g.Intersection(zona)
        nf = ogr.Feature(lv.GetLayerDefn())
        nf.SetField("osm_id", f.GetField("osm_id"))
        nf.SetField("nombre", f.GetField("name"))
        nf.SetField("clase_osm", clase)
        nf.SetField("jerarquia", JERARQUIA[clase])
        nf.SetGeometry(ogr.ForceToMultiLineString(proyectar(g)))
        lv.CreateFeature(nf)
    out = None

    # Ríos -> Shapefile en geográficas (como suele recibirse)
    drv = ogr.GetDriverByName("ESRI Shapefile")
    out = drv.CreateDataSource(os.path.join(ORIG, "rios.shp"))
    lr = out.CreateLayer("rios", srs(4326), ogr.wkbLineString, options=["ENCODING=UTF-8"])
    for nombre, tipo, ancho in [("osm_id", ogr.OFTString, 20), ("nombre", ogr.OFTString, 80),
                                ("tipo", ogr.OFTString, 12)]:
        fd = ogr.FieldDefn(nombre, tipo)
        fd.SetWidth(ancho)
        lr.CreateField(fd)
    lyr.SetAttributeFilter("waterway IN ('river', 'stream', 'canal', 'drain')")
    for f in lyr:
        g = f.GetGeometryRef()
        if not g.Intersects(zona):
            continue
        g = g.Intersection(zona)
        partes = [g] if g.GetGeometryType() == ogr.wkbLineString else [g.GetGeometryRef(i) for i in range(g.GetGeometryCount())]
        for parte in partes:
            if parte.GetGeometryType() != ogr.wkbLineString:
                continue
            nf = ogr.Feature(lr.GetLayerDefn())
            nf.SetField("osm_id", f.GetField("osm_id"))
            nf.SetField("nombre", f.GetField("name"))
            nf.SetField("tipo", {"river": "rio", "stream": "torrentera", "canal": "canal", "drain": "canal"}[f.GetField("waterway")])
            nf.SetGeometry(parte)
            lr.CreateFeature(nf)
    out = None


# ---------------------------------------------------------------- ráster

def construir_raster(muni):
    xmin, xmax, ymin, ymax = muni.Buffer(0.01).GetEnvelope()
    # DEM en geográficas, tal como se distribuye
    gdal.Warp(os.path.join(ORIG, "dem_copernicus_30m.tif"), os.path.join(FUENTES, "cop30_S18_W067.tif"),
              outputBounds=(xmin, ymin, xmax, ymax), creationOptions=["COMPRESS=DEFLATE", "PREDICTOR=3", "TILED=YES"])
    # Población WorldPop 100 m
    pob = os.path.join(ORIG, "poblacion_worldpop_2020.tif")
    gdal.Warp(pob, os.path.join(FUENTES, "bol_ppp_2020_constrained.tif"),
              outputBounds=(xmin, ymin, xmax, ymax), creationOptions=["COMPRESS=DEFLATE", "PREDICTOR=3"])
    # Copia en UTM, solo para calcular población por zona (no se distribuye)
    pob_utm = os.path.join(TMP, "pob_utm.tif")
    gdal.Warp(pob_utm, pob, dstSRS=f"EPSG:{EPSG_TRABAJO}", xRes=100, yRes=100, resampleAlg="near",
              dstNodata=-99999)
    # Sentinel-2: azul, verde, rojo, infrarrojo cercano a 10 m (nativo en UTM 19 S)
    t = transformador(4326, EPSG_TRABAJO)
    x0, y0, _ = t.TransformPoint(BBOX_IMAGEN[0], BBOX_IMAGEN[1])
    x1, y1, _ = t.TransformPoint(BBOX_IMAGEN[2], BBOX_IMAGEN[3])
    bandas = []
    for b in ["B02", "B03", "B04", "B08"]:
        destino = os.path.join(TMP, f"{b}.tif")
        if not os.path.exists(destino):
            gdal.Translate(destino, "/vsicurl/" + S2_ESCENA.format(banda=b),
                           projWin=[round(x0, -1), round(y1, -1), round(x1, -1), round(y0, -1)])
        bandas.append(destino)
    vrt = gdal.BuildVRT(os.path.join(TMP, "s2.vrt"), bandas, separate=True)
    vrt = None
    gdal.Translate(os.path.join(ORIG, "sentinel2_2025-07-16.tif"), os.path.join(TMP, "s2.vrt"),
                   creationOptions=["COMPRESS=DEFLATE", "PREDICTOR=2", "TILED=YES", "PHOTOMETRIC=MINISBLACK"])
    ds = gdal.Open(os.path.join(ORIG, "sentinel2_2025-07-16.tif"), 1)
    for i, d in enumerate(["B02 azul (490 nm)", "B03 verde (560 nm)", "B04 rojo (665 nm)",
                           "B08 infrarrojo cercano (842 nm)"], 1):
        ds.GetRasterBand(i).SetDescription(d)
    ds = None
    return pob_utm


# ---------------------------------------------------------------- ejercicios de SRC

def ejercicios_src():
    # 1. Comunas en Shapefile sin .prj (SRC desconocido)
    gdal.VectorTranslate(os.path.join(EJER, "comunas_sin_prj.shp"), os.path.join(ORIG, "limites.gpkg"),
                         layers=["comunas"], format="ESRI Shapefile", layerName="comunas_sin_prj",
                         layerCreationOptions=["ENCODING=UTF-8"])
    os.remove(os.path.join(EJER, "comunas_sin_prj.prj"))
    # 2. Vías principales en UTM 20 S pero declaradas como UTM 19 S (asignación errónea)
    tmp = os.path.join(TMP, "vias_20.gpkg")
    gdal.VectorTranslate(tmp, os.path.join(ORIG, "vias.gpkg"), dstSRS="EPSG:32720",
                         where="jerarquia IN ('troncal', 'principal')", layerName="vias_principales")
    gdal.VectorTranslate(os.path.join(EJER, "vias_principales_src_erroneo.gpkg"), tmp,
                         options=["-a_srs", f"EPSG:{EPSG_TRABAJO}"], layerName="vias_principales")


def main():
    fecha = datetime.date.today().isoformat()
    preparar_carpetas()
    osm = extraer_osm()
    muni, muni_utm, comunas = construir_limites(osm)
    pob_utm = construir_raster(muni)
    n_zonas = malla_hexagonal(muni_utm, comunas, pob_utm)
    escribir_tablas_comunas()
    filas = leer_equipamientos(osm, muni)
    escribir_csv_equipamientos(filas, fecha)
    escribir_mercados(osm, muni)
    escribir_csv_errores(filas, fecha)
    escribir_auditoria(filas)
    construir_vias_rios(osm, muni)
    ejercicios_src()
    plantillas = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plantillas_paquete")
    shutil.copytree(plantillas, SALIDA, dirs_exist_ok=True)
    print(f"comunas={len(comunas)} zonas={n_zonas} equipamientos={len(filas)}")


if __name__ == "__main__":
    main()
