const existingTags = JSON.parse(
    document.getElementById("tags-data").textContent
);

document.addEventListener("DOMContentLoaded", () => {
    existingTags.forEach(tagName => {
        selectedTags.set(tagName);
        createChip(tagName);
        hideOption(tagName);
        updateHiddenField();
    });
});