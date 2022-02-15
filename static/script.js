"use strict"

// ************ navbar **********************
window.onscroll = function () { myFunction() };

var navbar = document.getElementById("myP");
var sticky = navbar.offsetTop;

function myFunction() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        navbar.classList.add("sticky");
        navbar.classList.add("sticky-bg");
    } else {
        navbar.classList.remove("sticky");
        navbar.classList.remove("sticky-bg");
    }
}





// **************** book now page ************************
















// window.onclick = function (event) {
//     if (event.target == modal) {
//         modal.style.display = "none";
//     }
// }
