(() => {
  const revealHashTarget = () => {
    const fragment = window.location.hash.slice(1);
    if (!fragment) return;

    let id;
    try {
      id = decodeURIComponent(fragment);
    } catch {
      return;
    }
    const target = document.getElementById(id);
    if (!target) return;

    let ancestor = target;
    while (ancestor) {
      if (ancestor instanceof HTMLDetailsElement) ancestor.open = true;
      ancestor = ancestor.parentElement;
    }

    requestAnimationFrame(() => {
      target.scrollIntoView({ block: "start" });
    });
  };

  revealHashTarget();
  window.addEventListener("hashchange", revealHashTarget);
})();
