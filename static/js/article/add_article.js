const dropdownBtn = document.getElementById("dropdownBtn");
const dropdown = document.getElementById("dropdown");
const tagList = document.getElementById("tagList");
const chipsContainer = document.getElementById("chips");
const tagsField = document.getElementById("tagsField");
const addNewTagBtn = document.getElementById("addNewTagBtn");
const newTagInput = document.getElementById("new_tag");
const tagOptions = document.querySelectorAll(".tag-option");
const submitBtn = document.getElementById("submit");
const titleInput = document.getElementById("title");
const descriptionInput = document.getElementById("description");

let selectedTags = new Map();

dropdown.classList.add(`max-w-[300px]`);

function createChip(label) {
    const chip = document.createElement("span");
    chip.className =
        "flex items-center gap-1 bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm";

    chip.innerHTML = `
      ${label}
      <button type="button" class="ml-1 hover:text-blue-900">&times;</button>
    `;

    chip.querySelector("button").addEventListener("click", () => {
        selectedTags.delete(label);
        chip.remove();
        showOption(label);
        updateHiddenField();
    });

    chips.appendChild(chip);
}

function hideOption(label) {
    const opt = document.querySelector(`.tag-option[data-label="${label}"]`);
    if (opt) opt.classList.add("hidden");
}

function showOption(label) {
    const opt = document.querySelector(`.tag-option[data-label="${label}"]`);
    if (opt) opt.classList.remove("hidden");
}

function updateHiddenField() {
    document.getElementById("tagsJson").value = JSON.stringify([
        ...selectedTags.keys(),
    ]);
}

// Existing tags
tagOptions.forEach((btn) => {
    btn.addEventListener("click", () => {
        const label = btn.dataset.label;

        if (selectedTags.has(label)) return;

        selectedTags.set(label);
        createChip(label);
        hideOption(label);
        updateHiddenField();
    });
});

dropdownBtn.addEventListener("click", () => {
    console.log(dropdown.classList.value);
    dropdown.classList.replace(
        `max-w-[300px]`,
        `max-w-[${dropdownBtn.clientWidth}px]`,
    );
    console.log(dropdown.clientWidth, dropdownBtn.clientWidth);
    dropdown.classList.toggle("hidden");
});

addNewTagBtn.addEventListener("click", () => {
    const name = newTagInput.value.trim();
    if (!name) return;

    // éviter doublons visuels
    const exists = [...selectedTags.keys()].some(
        (v) => v.toLowerCase() === name.toLowerCase(),
    );
    if (exists) {
        newTagInput.value = "";
        return;
    }

    selectedTags.set(name);
    createChip(name);
    updateHiddenField();
    const tags_exists = [...tagOptions].some(
        (btn) => btn.dataset.label.toLowerCase() === name.toLowerCase(),
    );

    if (tags_exists) {
        hideOption(name);
    }

    newTagInput.value = "";
});

submitBtn.addEventListener("click", () => {
    if (titleInput.value.size != 0 && descriptionInput.value.size < 10) {
        titleInput.value = "";
        descriptionInput.value = "";
    }
});
