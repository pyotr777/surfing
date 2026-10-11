/* Sorting for the comparison table.
 *
 * The table itself is written during the build; this only reorders rows the
 * server already sent, so the page works fine with JavaScript switched off.
 */
(function () {
  "use strict";

  var table = document.getElementById("compare");
  if (!table) return;

  var tbody = table.tBodies[0];
  var headers = Array.prototype.slice.call(table.tHead.rows[0].cells);
  var compassDegrees = {
    N: 0, NNE: 22.5, NE: 45, ENE: 67.5,
    E: 90, ESE: 112.5, SE: 135, SSE: 157.5,
    S: 180, SSW: 202.5, SW: 225, WSW: 247.5,
    W: 270, WNW: 292.5, NW: 315, NNW: 337.5
  };

  function directionCenter(text) {
    var ends = text.split("-");
    var start = compassDegrees[ends[0]];
    var end = compassDegrees[ends[ends.length - 1]];
    if (start === undefined || end === undefined) return Infinity;
    if (end < start) end += 360;
    return (start + (end - start) / 2) % 360;
  }

  function cellValue(row, index, kind) {
    var cell = row.cells[index];
    var text = (cell.textContent || "").trim();
    if (kind === "number") {
      var n = parseFloat(text.replace(",", "."));
      return isNaN(n) ? -Infinity : n;
    }
    if (kind === "direction") return directionCenter(text);
    return text.toLocaleLowerCase();
  }

  function sortBy(index) {
    var th = headers[index];
    var kind = th.dataset.sort || "text";
    var ascending = th.getAttribute("aria-sort") !== "ascending";

    var rows = Array.prototype.slice.call(tbody.rows);
    rows.sort(function (a, b) {
      var x = cellValue(a, index, kind);
      var y = cellValue(b, index, kind);
      if (x < y) return ascending ? -1 : 1;
      if (x > y) return ascending ? 1 : -1;
      return 0;
    });

    headers.forEach(function (h) { h.removeAttribute("aria-sort"); });
    th.setAttribute("aria-sort", ascending ? "ascending" : "descending");
    rows.forEach(function (row) { tbody.appendChild(row); });
  }

  headers.forEach(function (th, index) {
    var button = th.querySelector("button");
    if (button) button.addEventListener("click", function () { sortBy(index); });
  });
})();
