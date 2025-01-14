var selectedTheme = localStorage.getItem("theme");
if (selectedTheme) {
  document.documentElement.setAttribute("data-theme", selectedTheme);
}
