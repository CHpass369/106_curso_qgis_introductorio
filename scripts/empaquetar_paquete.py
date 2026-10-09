"""Empaqueta la carpeta curso-qgis/ en curso-qgis-cochabamba.zip.

Se ejecuta al final, en un proceso aparte (sin QGIS abierto sobre los datos):

    python scripts/empaquetar_paquete.py PAQUETE

Devuelve los GeoPackage al modo de diario DELETE y elimina archivos auxiliares
(-wal, -shm, .aux.xml) antes de comprimir.
"""
import glob
import os
import shutil
import sqlite3
import sys

PAQ = os.path.abspath(sys.argv[1])

for gpkg in glob.glob(os.path.join(PAQ, "**", "*.gpkg"), recursive=True):
    con = sqlite3.connect(gpkg)
    con.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    con.execute("PRAGMA journal_mode=DELETE")
    con.close()
restos = (glob.glob(os.path.join(PAQ, "**", "*.gpkg-*"), recursive=True)
          + glob.glob(os.path.join(PAQ, "**", "*.aux.xml"), recursive=True))
for resto in restos:
    os.remove(resto)
zip_base = os.path.join(os.path.dirname(PAQ), "curso-qgis-cochabamba")
shutil.make_archive(zip_base, "zip", os.path.dirname(PAQ), os.path.basename(PAQ))
print("paquete", zip_base + ".zip", round(os.path.getsize(zip_base + ".zip") / 1e6, 1), "MB")
