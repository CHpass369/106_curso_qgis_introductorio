"""Métricas de estilo de las lecciones (ver CONTRIBUTING.md).

Uso: python scripts/revisar_contenido.py [--estricto]
Con --estricto termina con código 1 si alguna lección supera los límites.
"""
import pathlib
import re
import sys

DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"
MAX_H2 = 15
MAX_TEXT_BLOCKS = 10

def separar_codigo(texto):
    """Devuelve (lineas_fuera_de_codigo, lista_de_bloques[(lenguaje, lineas)])."""
    fuera, bloques, abierto = [], [], None
    for linea in texto.splitlines():
        m = re.match(r"^\s*(`{3,}|~{3,})\s*([\w-]*)", linea)
        if abierto is None:
            if m:
                abierto = (m.group(1)[0], len(m.group(1)), m.group(2), [])
            else:
                fuera.append(linea)
        else:
            if m and m.group(1)[0] == abierto[0] and len(m.group(1)) >= abierto[1] and not m.group(2):
                bloques.append((abierto[2], abierto[3]))
                abierto = None
            else:
                abierto[3].append(linea)
    return fuera, bloques


def es_prosa(lineas):
    """Un bloque ```text es «prosa» si casi ninguna línea parece cálculo, código, ruta o árbol."""
    utiles = [l for l in lineas if l.strip()]
    if not utiles:
        return False
    tecnicas = sum(1 for l in utiles if re.search(r"[0-9=/×÷+*<>├└│_.:;\[\]{}()@\"']", l))
    return tecnicas / len(utiles) < 0.3


def metricas(texto):
    fuera, bloques = separar_codigo(texto)
    prosa = "\n".join(fuera)
    return {
        "h2": len(re.findall(r"^## ", prosa, re.M)),
        "h2_num": len(re.findall(r"^## \d+\.", prosa, re.M)),
        "text": sum(1 for lang, lineas in bloques if lang == "text" and es_prosa(lineas)),
        "img": len(re.findall(r"!\[[^\]]*\]\(", prosa)) + prosa.count("<svg"),
        "capt": len(re.findall(r"^\s*!!! captura", prosa, re.M)),
        "refs": int(bool(re.search(r"^## Referencias", prosa, re.M))),
        "crs": len(re.findall(r"\bCRS\b", prosa)),
        "palabras": len(prosa.split()),
    }


def main():
    estricto = "--estricto" in sys.argv
    fallos = 0
    cab = f"{'leccion':48} {'pal':>6} {'##':>4} {'##N':>4} {'text':>5} {'img':>4} {'capt':>5} {'refs':>5} {'CRS':>4}"
    print(cab)
    for p in sorted(DOCS.glob("modulo-0*/[0-9]*.md")):
        m = metricas(p.read_text(encoding="utf-8"))
        marca = ""
        if m["h2"] > MAX_H2 or m["h2_num"] or m["text"] > MAX_TEXT_BLOCKS or not m["refs"]:
            marca = "  <-"
            fallos += 1
        print(f"{p.relative_to(DOCS).as_posix():48} {m['palabras']:6} {m['h2']:4} {m['h2_num']:4} {m['text']:5} "
              f"{m['img']:4} {m['capt']:5} {m['refs']:5} {m['crs']:4}{marca}")
    print(f"\nLecciones fuera de norma: {fallos}")
    if estricto and fallos:
        sys.exit(1)

if __name__ == "__main__":
    main()
