"use strict";

const btnAdd = document.getElementById("add");
const btnView = document.getElementById("view");
const btnHome =document.getElementById("home");

btnView.addEventListener("click", () => {
    //open new window to a table of certificates
    navCert();
    addCertificateToTable();
});

btnHome.addEventListener("click", () => {
    //open new window to a table of certificates
    navHome();
});

const homeDiv = document.getElementById("homeDiv");
const certDiv = document.getElementById("certDiv");

/**
 * navigate to the home page on the single page application
 */
function navHome() {
    homeDiv.classList.add("displayed");
    homeDiv.classList.remove("not-displayed");

    certDiv.classList.remove("displayed");
    certDiv.classList.add("not-displayed");
}

/**
 * navigate to the view certificate on the single page application
 */
function navCert() {
    certDiv.classList.add("displayed");
    certDiv.classList.remove("not-displayed");

    homeDiv.classList.remove("displayed");
    homeDiv.classList.add("not-displayed");    
}
