"""Comprueba que el inventario respete los límites de cada captura."""
import pathlib
import tempfile
import unittest
from unittest.mock import patch

import listar_pendientes


class InventarioTests(unittest.TestCase):
    def generar(self, contenido):
        with tempfile.TemporaryDirectory() as carpeta:
            raiz = pathlib.Path(carpeta)
            docs = raiz / "docs"
            docs.mkdir()
            (docs / "leccion.md").write_text(contenido, encoding="utf-8")
            with patch.object(listar_pendientes, "RAIZ", raiz), patch.object(listar_pendientes, "DOCS", docs):
                listar_pendientes.main()
            return (raiz / "PENDIENTES.md").read_text(encoding="utf-8")

    def test_no_incluye_el_bloque_siguiente(self):
        salida = self.generar('''    !!! captura "Captura pendiente · 2.1-02"

        - **Tipo:** GIF animado
        - **Qué mostrar:** Abrir QGIS.

    ??? info "Sección siguiente"
        Texto ajeno a la captura.
''')
        fila = next(l for l in salida.splitlines() if "2.1-02" in l)
        self.assertIn("GIF animado | Abrir QGIS. |", fila)
        self.assertNotIn("Sección siguiente", fila)

    def test_descripcion_multilinea_y_campos_tardios(self):
        salida = self.generar('''!!! captura "Captura pendiente · 3.1-01"

    - **Archivo:** `ejemplo.png`

    - **Sugerencia:** Texto opcional.

    - **Tipo:** PNG anotado
    - **Qué mostrar:** Dos capas:
      vías | comunas.
    - **Sugerencia:** No incluir esta instrucción.

## Otra sección
''')
        fila = next(l for l in salida.splitlines() if "3.1-01" in l)
        self.assertIn("PNG anotado | Dos capas: vías / comunas. |", fila)
        self.assertNotIn("No incluir", fila)


if __name__ == "__main__":
    unittest.main()
