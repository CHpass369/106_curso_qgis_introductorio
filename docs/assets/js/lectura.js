/* Las figuras mantienen sus etiquetas legibles y pueden ampliarse. */
(() => {
  function prepararDiagramas() {
    document.querySelectorAll(".md-typeset div.mermaid").forEach(diagram => {
      if (diagram.parentElement.classList.contains("mermaid-scroll")) return;
      const scroll = document.createElement("div");
      scroll.className = "mermaid-scroll";
      scroll.tabIndex = 0;
      scroll.setAttribute("role", "region");
      scroll.setAttribute("aria-label", "Diagrama conceptual; puedes desplazarlo horizontalmente.");
      diagram.before(scroll);
      scroll.append(diagram);
      const hint = document.createElement("small");
      hint.className = "figure-hint";
      hint.textContent = "Desliza horizontalmente para ver el diagrama completo.";
      scroll.after(hint);
      new ResizeObserver(() => {
        hint.hidden = scroll.scrollWidth <= scroll.clientWidth + 1;
      }).observe(scroll);
    });
  }

  function prepararLectura() {
    prepararDiagramas();
    document.querySelectorAll(".md-typeset figure.figura > svg").forEach(svg => {
      const figure = svg.parentElement;
      const label = svg.getAttribute("aria-label") || "Figura de la lección";
      const width = svg.viewBox.baseVal.width || 720;
      const scroll = document.createElement("div");
      scroll.className = "figure-scroll";
      scroll.tabIndex = 0;
      scroll.setAttribute("role", "region");
      scroll.setAttribute("aria-label", `${label}. Desplazamiento horizontal disponible.`);
      svg.before(scroll);
      scroll.append(svg);
      svg.style.minWidth = `${Math.min(width, 960)}px`;
      const hint = document.createElement("small");
      hint.className = "figure-hint";
      hint.textContent = "Desliza horizontalmente para ver la figura completa.";
      scroll.after(hint);
      const updateHint = () => { hint.hidden = scroll.scrollWidth <= scroll.clientWidth + 1; };
      new ResizeObserver(updateHint).observe(scroll);

      const button = document.createElement("button");
      button.type = "button";
      button.className = "figure-expand";
      button.textContent = "Ampliar figura";
      button.setAttribute("aria-label", `Ampliar: ${label}`);
      button.addEventListener("click", () => {
        const dialog = document.createElement("dialog");
        dialog.className = "figure-dialog";
        dialog.setAttribute("aria-label", label);
        const close = document.createElement("button");
        close.type = "button";
        close.className = "figure-dialog__close";
        close.textContent = "Cerrar";
        const enlarged = scroll.cloneNode(true);
        // Evita identificadores duplicados en clipPath, gradients y referencias.
        const ids = new Map();
        enlarged.querySelectorAll("[id]").forEach(node => {
          const original = node.id;
          const unique = `ampliada-${original}`;
          ids.set(original, unique);
          node.id = unique;
        });
        enlarged.querySelectorAll("*").forEach(node => {
          [...node.attributes].forEach(attr => {
            let value = attr.value;
            ids.forEach((unique, original) => {
              value = value.replaceAll(`url(#${original})`, `url(#${unique})`);
              if (value === `#${original}`) value = `#${unique}`;
              if (attr.name === "aria-labelledby" || attr.name === "aria-describedby") {
                value = value.split(" ").map(id => id === original ? unique : id).join(" ");
              }
            });
            if (value !== attr.value) node.setAttribute(attr.name, value);
          });
        });
        const dialogHint = hint.cloneNode(true);
        dialogHint.hidden = false;
        dialog.append(close, dialogHint, enlarged);
        document.body.append(dialog);
        close.addEventListener("click", () => dialog.close());
        dialog.addEventListener("close", () => {
          dialog.remove();
          button.focus();
        });
        dialog.showModal();
        close.focus();
      });
      hint.after(button);
    });

    document.querySelectorAll(".md-typeset__table").forEach(table => {
      if (table.dataset.readingReady) return;
      table.dataset.readingReady = "true";
      table.setAttribute("role", "region");
      table.setAttribute("aria-label", "Tabla de la lección; puedes desplazarla horizontalmente si es necesario.");
      new ResizeObserver(() => {
        if (table.scrollWidth > table.clientWidth + 1) table.tabIndex = 0;
        else table.removeAttribute("tabindex");
      }).observe(table);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", prepararLectura);
  } else {
    prepararLectura();
  }
  if (typeof document$ !== "undefined") document$.subscribe(prepararLectura);
  new MutationObserver(prepararDiagramas).observe(document.body, { childList: true, subtree: true });
})();
