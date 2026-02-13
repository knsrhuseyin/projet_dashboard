let lastScroll = 0;
const navbar = document.getElementById("navbar");

window.addEventListener("scroll", () => {
    const currentScroll = window.scrollY;

    if (currentScroll > lastScroll && currentScroll > 200) {
        // Scroll vers le bas → cacher
        navbar.classList.add("-translate-y-full");
    } else {
        // Scroll vers le haut → montrer
        navbar.classList.remove("-translate-y-full");
    }

    lastScroll = currentScroll;
});
