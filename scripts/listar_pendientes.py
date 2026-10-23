"""Genera PENDIENTES.md con las tareas manuales marcadas en docs/.

Marcadores reconocidos:
  !!! captura "Captura pendiente · N.M-NN"   (especificación de captura/GIF)
  <!-- TODO-MANUAL[tipo]: descripción -->
"""
import pathlib
import re

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"


def campos_captura(lineas, inicio, sangria):
    """Lee solo el cuerpo indentado de la admonición, sin límite de líneas."""
    campos, actual = {}, None
    for linea in lineas[inicio:]:
        if not linea.strip():
            continue
        ancho = len(linea) - len(linea.lstrip())
        if ancho <= sangria:
            break
        campo = re.match(r"\s*-\s*\*\*([^*]+):\*\*\s*(.*)", linea)
        if campo:
            actual = campo.group(1)
            campos[actual] = campo.group(2).strip()
        elif actual:
            campos[actual] += " " + linea.strip()
    return campos


def main():
    capturas, otros = [], []
    for p in sorted(DOCS.rglob("*.md")):
        rel = p.relative_to(RAIZ).as_posix()
        lineas = p.read_text(encoding="utf-8").splitlines()
        for i, linea in enumerate(lineas, 1):
            m = re.match(r'\s*!!! captura "(.*)"', linea)
            if m:
                sangria = len(linea) - len(linea.lstrip())
                campos = campos_captura(lineas, i, sangria)
                capturas.append((rel, i, m.group(1), campos.get("Tipo", "").strip(" ."),
                                 campos.get("Qué mostrar", "")))
            for t in re.finditer(r"TODO-MANUAL\[([^\]]+)\]:\s*(.*?)\s*-->", linea):
                otros.append((rel, i, t.group(1), t.group(2)))
    out = ["# Tareas manuales pendientes", "",
           "Generado con `python scripts/listar_pendientes.py`. No editar a mano.", "",
           f"- Capturas y GIF pendientes: **{len(capturas)}**",
           f"- Otras tareas manuales: **{len(otros)}**", "",
           "## Otras tareas manuales", "", "| Archivo | Línea | Tipo | Tarea |", "|---|---|---|---|"]
    out += [f"| `{a}` | {l} | {t} | {d} |" for a, l, t, d in otros]
    out += ["", "## Capturas y GIF", "", "| Archivo | Línea | Identificador | Tipo | Qué mostrar |", "|---|---|---|---|---|"]
    out += [f"| `{a}` | {l} | {n} | {t} | {q.replace('|', '/')} |" for a, l, n, t, q in capturas]
    (RAIZ / "PENDIENTES.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(capturas)} capturas, {len(otros)} otras tareas -> PENDIENTES.md")

if __name__ == "__main__":
    main()
