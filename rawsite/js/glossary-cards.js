(function () {
  "use strict";

  var lastTrigger = null;
  var tooltip = document.createElement("div");
  tooltip.className = "glossary-tooltip";
  tooltip.id = "glossary-tooltip";
  tooltip.setAttribute("role", "tooltip");
  tooltip.hidden = true;
  document.body.appendChild(tooltip);

  function supportsHover() {
    return window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  }

  function cardFor(trigger) {
    return document.getElementById("glossary-card-" + trigger.dataset.glossaryCard);
  }

  function showTooltip(trigger) {
    if (!supportsHover()) return;
    var card = cardFor(trigger);
    if (!card) return;

    tooltip.textContent = card.querySelector("p").textContent;
    tooltip.hidden = false;
    trigger.setAttribute("aria-describedby", tooltip.id);

    var triggerBox = trigger.getBoundingClientRect();
    var left = Math.max(8, Math.min(triggerBox.left, window.innerWidth - tooltip.offsetWidth - 8));
    var top = triggerBox.top - tooltip.offsetHeight - 8;
    if (top < 8) top = triggerBox.bottom + 8;
    tooltip.style.left = left + "px";
    tooltip.style.top = top + "px";
  }

  function hideTooltip(trigger) {
    tooltip.hidden = true;
    if (trigger) trigger.removeAttribute("aria-describedby");
  }

  document.addEventListener("pointerover", function (event) {
    var trigger = event.target.closest("a[data-glossary-card]");
    if (trigger) showTooltip(trigger);
  });

  document.addEventListener("pointerout", function (event) {
    var trigger = event.target.closest("a[data-glossary-card]");
    if (trigger) hideTooltip(trigger);
  });

  document.addEventListener("focusin", function (event) {
    var trigger = event.target.closest("a[data-glossary-card]");
    if (trigger) showTooltip(trigger);
  });

  document.addEventListener("focusout", function (event) {
    var trigger = event.target.closest("a[data-glossary-card]");
    if (trigger) hideTooltip(trigger);
  });

  document.addEventListener("click", function (event) {
    var trigger = event.target.closest("a[data-glossary-card]");
    if (!trigger) return;

    if (supportsHover()) return;

    var card = cardFor(trigger);
    if (!card || typeof card.showModal !== "function") return;

    event.preventDefault();
    hideTooltip(trigger);
    lastTrigger = trigger;
    card.showModal();
  });

  document.querySelectorAll(".glossary-card").forEach(function (card) {
    var close = card.querySelector(".glossary-card-close");
    if (close) close.addEventListener("click", function () { card.close(); });

    card.addEventListener("click", function (event) {
      if (event.target === card) card.close();
    });

    card.addEventListener("close", function () {
      if (lastTrigger) lastTrigger.focus();
      lastTrigger = null;
    });
  });
}());
