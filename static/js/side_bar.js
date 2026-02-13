const burgerBtn = document.getElementById("burgerBtn");
const closeBtn = document.getElementById("closeBtn");
const mobileMenu = document.getElementById("sidebar");

const articleBtn = document.getElementById("articleBtn");
const articleContent = document.getElementById("articleContent");
const articleBtnArrow = document.getElementById("articleBtnArrow");

const usersBtn = document.getElementById("usersBtn");
const usersContent = document.getElementById("usersContent");
const usersBtnArrow = document.getElementById("usersBtnArrow");

burgerBtn.addEventListener("click", () => {
    mobileMenu.classList.toggle("-translate-x-full");
});

closeBtn.addEventListener("click", () => {
    mobileMenu.classList.toggle("-translate-x-full");
});

articleBtn.addEventListener("click", (e) => {
    e.stopPropagation();

    if (
        articleContent.style.maxHeight &&
        articleContent.style.maxHeight !== "0px"
    ) {
        articleContent.style.maxHeight = "0px";
        articleContent.style.padding = "0px";
        articleBtn.classList.add("rounded-b-xl");
        articleBtn.classList.remove("rounded-b-none");
    } else {
        articleContent.style.maxHeight =
            articleContent.scrollHeight + 50 + "px";
        articleContent.style.padding = "1rem";
        articleBtn.classList.remove("rounded-b-xl");
        articleBtn.classList.add("rounded-b-none");
    }
    articleBtn.classList.toggle("bg-blue-800");
    articleBtn.classList.toggle("text-white");
    articleBtnArrow.classList.toggle("rotate-180");
});

usersBtn.addEventListener("click", (e) => {
    e.stopPropagation();

    if (
        usersContent.style.maxHeight &&
        usersContent.style.maxHeight !== "0px"
    ) {
        usersContent.style.maxHeight = "0px";
        usersContent.style.padding = "0px";
        usersBtn.classList.add("rounded-b-xl");
        usersBtn.classList.remove("rounded-b-none");
    } else {
        usersContent.style.maxHeight =
            usersContent.scrollHeight + 50 + "px";
        usersContent.style.padding = "1rem";
        usersBtn.classList.remove("rounded-b-xl");
        usersBtn.classList.add("rounded-b-none");
    }
    usersBtn.classList.toggle("bg-blue-800");
    usersBtn.classList.toggle("text-white");
    usersBtnArrow.classList.toggle("rotate-180");
});
