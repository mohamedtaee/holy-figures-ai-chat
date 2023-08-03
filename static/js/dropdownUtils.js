function updateSecondaryDropdown() {
    var initialDropdown = document.getElementById("initialDropdown");
    var secondaryDropdown = document.getElementById("secondaryDropdown");

    // Clear previous options
    secondaryDropdown.innerHTML = "";

    // Get the selected option from the initial dropdown
    var selectedOption = initialDropdown.value;

    // Populate the secondary dropdown based on the selected option
    if (selectedOption === "bible") {
        addOption(secondaryDropdown, "God", "god");
        addOption(secondaryDropdown, "Jesus Christ", "jesus");
    } else if (selectedOption === "quran") {
        addOption(secondaryDropdown, "Allah", "allah");
        addOption(secondaryDropdown, "Muhammad", "muhammad");
    } else if (selectedOption === "torah") {
        addOption(secondaryDropdown, "God", "god");
        addOption(secondaryDropdown, "Moses", "moses");

    } else if (selectedOption === "vedas") {
        addOption(secondaryDropdown, "Brahma", "brahma");
        addOption(secondaryDropdown, "Krishna", "krishna");
    } else if (selectedOption === "book_of_mormon") {
        addOption(secondaryDropdown, "God", "god");
        addOption(secondaryDropdown, "Jesus Christ", "jesus");
        addOption(secondaryDropdown, "Joseph Smith", "joseph_smith");
        addOption(secondaryDropdown, "Brigham Young", "brigham_young");
    } else if (selectedOption === "iliad") {
        addOption(secondaryDropdown, "Zeus", "zeus");
        addOption(secondaryDropdown, "Poseidon", "poseidon");
        addOption(secondaryDropdown, "Hermes", "hermes");
        addOption(secondaryDropdown, "Apollo", "apollo");
    } else if (selectedOption === "book_of_the_dead") {
        addOption(secondaryDropdown, "Ra", "ra");
        addOption(secondaryDropdown, "Osiris", "osiris");
        addOption(secondaryDropdown, "Anubis", "anubis");
        addOption(secondaryDropdown, "Horus", "horus");

    } else if (selectedOption === "scientology") {
        addOption(secondaryDropdown, "L. Ron Hubbard", "l_ron_hubbard");
    }

}

function addOption(selectElement, optionText, optionValue) {
    var option = document.createElement("option");
    option.text = optionText;
    option.value = optionValue;
    selectElement.add(option);
}