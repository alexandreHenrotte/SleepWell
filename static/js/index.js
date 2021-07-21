
/* Sélection des modes */

document.getElementById("mode1-container").addEventListener("click", mode1);
document.getElementById("mode2-container").addEventListener("click", mode2);

function mode1() {
    document.getElementById("mode1-container").style.border = "3px solid white";
    document.getElementById("mode2-container").style.border = null;
    document.getElementById("mode1-inputs").style.display = "inherit"
    document.getElementById("submit-button").hidden = false;
}

function mode2() {
    document.getElementById("mode2-container").style.border = "3px solid white";
    document.getElementById("mode1-container").style.border = null;
    document.getElementById("mode1-inputs").style.display = "none"
    document.getElementById("submit-button").hidden = false;
}


/* Gestion de l'entrée utilisateur pour les heures et minutes */

function incrementHours(inputId) {
    var input = document.getElementById(inputId);
    if (parseInt(input.value) < 23) {
        var valueIncremented = (parseInt(input.value) + 1);
        input.value = (valueIncremented < 10) ? "0" + valueIncremented : valueIncremented;
    }
}

function decrementHours(inputId) {
    var input = document.getElementById(inputId);
    if (parseInt(input.value) > 0) {
        var valueIncremented = (parseInt(input.value) - 1);
        input.value = (valueIncremented < 10) ? "0" + valueIncremented : valueIncremented;
    }
}

function incrementMinutes(inputId) {
    var input = document.getElementById(inputId);
    if (parseInt(input.value) < 50) {
        input.value = (parseInt(input.value) + 10);
    }
}

function decrementMinutes(inputId) {
    var input = document.getElementById(inputId);
    if (parseInt(input.value) > 0) {
        input.value = (parseInt(input.value) - 10);
    }
}