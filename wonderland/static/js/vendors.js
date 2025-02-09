import "htmx.org";
import Alpine from "alpinejs";
//import htmx from "./htmx.js";

window.htmx = htmx.default;
window.Alpine = Alpine;

document.addEventListener("DOMContentLoaded", async () => {
  Alpine.start();
});
