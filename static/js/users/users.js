document.addEventListener("DOMContentLoaded", (e) => {
    e.stopPropagation
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
});