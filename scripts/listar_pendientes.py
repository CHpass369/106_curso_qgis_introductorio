"""Genera PENDIENTES.md con las tareas manuales marcadas en docs/.

Marcadores reconocidos:
  !!! captura "Captura pendiente · N.M-NN"   (especificación de captura/GIF)
  <!-- TODO-MANUAL[tipo]: descripción -->
"""
import pathlib
import re

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"

def main():
    capturas, otros = [], []
    for p in sorted(DOCS.rglob("*.md")):
        rel = p.relative_to(RAIZ).as_posix()
        lineas = p.read_text(encoding="utf-8").splitlines()
        for i, linea in enumerate(lineas, 1):
            m = re.match(r'\s*!!! captura "(.*)"', linea)
            if m:
                bloque = " ".join(l.strip() for l in lineas[i:i + 6])
                tipo = re.search(r"\*\*Tipo:\*\*\s*([^-*]+)", bloque)
                que = re.search(r"\*\*Qué mostrar:\*\*\s*(.+?)(?: - \*\*|$)", bloque)
                capturas.append((rel, i, m.group(1), tipo.group(1).strip(" .") if tipo else "",
                                 que.group(1).strip()[:140] if que else ""))
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
