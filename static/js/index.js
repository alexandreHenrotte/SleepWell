console.log(document.getElementById("mode1"));
document.getElementById("mode1").addEventListener("click", mode1);
document.getElementById("mode2").addEventListener("click", mode2);
console.log("salut");


function mode1() {
    document.getElementById("input-hour").style.display = "inherit"
    document.getElementById("input-minutes").style.display = "inherit"
}

function mode2() {
    document.getElementById("input-hour").style.display = "none"
    document.getElementById("input-minutes").style.display = "none"
}