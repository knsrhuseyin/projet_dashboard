document.addEventListener("DOMContentLoaded", (e) => {
    e.stopPropagation
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
});


function openModal(slug, title) {
    document.getElementById("confirmModal").classList.remove("hidden");
    document.getElementById("confirmModal").classList.add("flex");

    document.getElementById("modalText").innerText =
        "Tu es sûr de vouloir supprimer l'article dont le titre est \"" +
        title +
        '" ?';

    document.getElementById("deleteForm").action =
        "/admin/article/delete/" + slug;
}

function closeModal() {
    document.getElementById("confirmModal").classList.add("hidden");
    document.getElementById("confirmModal").classList.remove("flex");
}
