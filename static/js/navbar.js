// --- MENU BURGER ---
const burgerBtn = document.getElementById("burgerBtn");
const mobileMenu = document.getElementById("mobileMenu");

burgerBtn.addEventListener("click", () => {
  mobileMenu.classList.toggle("hidden");
});

// --- ACCÈS RAPIDES MOBILE ---
const quickBtnMobile = document.getElementById("quickAccessBtnMobile");
const quickDropdownMobile = document.getElementById("quickAccessDropdownMobile");
const quickArrowMobile = document.getElementById("quickAccessArrowMobile");

quickBtnMobile.addEventListener("click", (e) => {
  e.stopPropagation();
  quickDropdownMobile.classList.toggle("hidden");
  quickArrowMobile.classList.toggle("rotate-180");
});

// --- ACCÈS RAPIDES PC ---
const btn = document.getElementById("quickAccessBtn");
const dropdown = document.getElementById("quickAccessDropdown");
const arrow = document.getElementById("quickAccessArrow");

btn.addEventListener("click", (e) => {
  e.stopPropagation();
  dropdown.classList.toggle("opacity-0");
  dropdown.classList.toggle("invisible");
  dropdown.classList.toggle("translate-y-0");
  dropdown.classList.toggle("-translate-y-2");
  arrow.classList.toggle("rotate-180");
});

// --- Fermer menus si clic en dehors ---
document.addEventListener("click", () => {
  dropdown.classList.add("opacity-0", "invisible", "-translate-y-2");
  dropdown.classList.remove("translate-y-0");
  arrow.classList.remove("rotate-180");

  quickDropdownMobile.classList.add("hidden");
  quickArrowMobile.classList.remove("rotate-180");
});
