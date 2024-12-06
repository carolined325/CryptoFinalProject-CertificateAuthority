"use strict";

// let arrAddGrades = [];
// const tBodyAddGrades = document.getElementById("tableDiv");
// let valid = 0;
// let addPointsE = 0;
// let addTotalP = 0;
// let idIndex = 0;

// const inputAssignment = document.getElementById("assignment-name");
// const inputPointsE = document.getElementById("points-earned");
// const inputTotalP = document.getElementById("total-points");
const btnAdd = document.getElementById("add");
const btnView = document.getElementById("view");
const btnHome =document.getElementById("home");
// const additionTotals = document.getElementById("addition");

btnView.addEventListener("click", () => {
    //open new window to a table of certificates
    navCert();
    addCertificateToTable();
});

btnHome.addEventListener("click", () => {
    //open new window to a table of certificates
    navHome();
});

// btnRenew.addEventListener("click", () => {
//     //open new window to a table of certificates
//     navRen();
// });

/**
 * when the add button is clicked, input the values from the array into the table
 */
// btnAdd.addEventListener("click", () => {
//     add.classList.add("hide");
//     add.classList.remove("available");
//     arrAddGrades.push({
//         assignment: inputAssignment.value,
//         points: inputPointsE.value,
//         total: inputTotalP.value,
//         id: idIndex
//     });
//     //hold it in local storage
//     try {
//         localStorage.setItem("grade", JSON.stringify(arrAddGrades));
//     } catch (error) {
//         console.log(error.message);
//     }
//     idIndex++;
//     inputAssignment.value = "";
//     inputPointsE.value = "";
//     inputTotalP.value = "";

//     addGradeToTable();
// });

// inputAssignment.addEventListener("input", () => {
//     validate();
// });

// inputPointsE.addEventListener("input", () => {
//     validate();
// });

// inputTotalP.addEventListener("input", () => {
//     validate();
// });
/**
 * make sure that all 3 fields are filled in before allowing to add to the table
 */
// function validate() {
//     if (inputAssignment.value && inputPointsE.value && inputTotalP.value) {
//         add.classList.add("available");
//         add.classList.remove("hide");
//     } else {
//         add.classList.add("hide");
//         add.classList.remove("available");
//     }
// }

/**
 * add the assignment name, points earned, and total points to the table
 */
// function addCertificateToTable() {
//     tBodyAddGrades.innerHTML = "";
//     arrAddGrades.map((grade) => {
//         //creating tr
//         const row = tBodyAddGrades.insertRow(-1);
//         //creating td
//         const cellAssignment = row.insertCell(0);
//         const cellPointsE = row.insertCell(1);
//         const cellTotalP = row.insertCell(2);
//         const cellAction = row.insertCell(3);
//         //referencing object instead of strings
//         cellAssignment.innerText = grade.assignment;
//         cellPointsE.innerText = grade.points;
//         cellTotalP.innerText = grade.total;
//         cellAction.innerHTML = `<button onclick="deleteGrade(${grade.id})">Delete</>`;
//     });
//     mathematics();
// }

// /**
//  * delete specific row when the delete button is selected and confirmed through the alert(confirm)
//  * (id) accepts location of row to only remove that one
//  */
// function deleteGrade(id) {
//     if (confirm("You are trying to delete this row") === true) {
//         arrAddGrades = arrAddGrades.filter((grade) => {
//             return grade.id != id;
//         });
//     }
//     addGradeToTable();
//     mathematics();
//     try {
//         localStorage.setItem("grade", JSON.stringify(arrAddGrades));
//     } catch (error) {
//         console.log(error.message);
//     }
// }

// /**
//  * add up the totals of the points earned and total points
//  * calculate percentages and assign a letter grade to each
//  */
// function mathematics() {
//     addPointsE = 0;
//     addTotalP = 0;
//     arrAddGrades.map((grade) => {
//         addPointsE += parseInt(grade.points);
//         addTotalP += parseInt(grade.total);
//     });
//     let math = 0;
//     if (addPointsE === 0) {
//         math = "";
//     } else if (addTotalP === 0) {
//         math = "";
//     } else {
//         math = addPointsE / addTotalP;
//         math = math * 100;
//         math = Math.round(math);
//     }

//     if (math === null) {
//         math = "";
//         alert(`math= ${math}`);
//     }
//     let letterGrade = "";
//     if (math > 90 && (math <= 100 || math > 100)) {
//         letterGrade = "A";
//     } else if (math > 80 && math <= 90) {
//         letterGrade = "B";
//     } else if (math > 70 && math <= 80) {
//         letterGrade = "C";
//     } else if (math > 60 && math <= 70) {
//         letterGrade = "D";
//     } else if (math > 0 && math <= 60) {
//         letterGrade = "F";
//     } else if (math === null) {
//         letterGrade = " ";
//     }

//     //display the percentage and grade and reset variables
//     additionTotals.innerText = `Percentage: ${math} Grade: ${letterGrade}`;
//     addPointsE = 0;
//     addTotalP = 0;
// }

const homeDiv = document.getElementById("homeDiv");
const certDiv = document.getElementById("certDiv");
// const renDiv = document.getElementById("renewCert");

/**
 * navigate to the home page on the single page application
 */
function navHome() {
    homeDiv.classList.add("displayed");
    homeDiv.classList.remove("not-displayed");

    certDiv.classList.remove("displayed");
    certDiv.classList.add("not-displayed");

    // renDiv.classList.remove("displayed");
    // renDiv.classList.add("not-displayed");
}

/**
 * navigate to the view certificate on the single page application
 */
function navCert() {
    certDiv.classList.add("displayed");
    certDiv.classList.remove("not-displayed");

    homeDiv.classList.remove("displayed");
    homeDiv.classList.add("not-displayed");

    // renDiv.classList.remove("displayed");
    // renDiv.classList.add("not-displayed");

    
}

/**
 * navigate to renew certificate on the single page application
 */
// function navRen() {
//     certDiv.classList.remove("displayed");
//     certDiv.classList.add("not-displayed");

//     homeDiv.classList.remove("displayed");
//     homeDiv.classList.add("not-displayed");

//     renDiv.classList.add("displayed");
//     renDiv.classList.remove("not-displayed");
// }

// const theme = document.getElementById("theme");

// //change the theme color of the page
// theme.addEventListener("click", () => {
//     const body = document.body;
//     if (!body.getAttribute("data-bs-theme") || body.getAttribute("data-bs-theme").includes("light")) {
//         body.setAttribute("data-bs-theme", "dark");
//     } else {
//         body.setAttribute("data-bs-theme", "light");
//     }
// });

// window.addEventListener("load", () => {
//     const gradeStorage = localStorage.getItem("grade");
//     if (gradeStorage) {
//         try {
//             arrAddGrades = JSON.parse(gradeStorage);
//             //addGradesToTable();
//         } catch (error) {
//             console.log(error.message);
//         }
//     }
//     try {
//         localStorage.setItem("grade", JSON.stringify(arrAddGrades));
//     } catch (error) {
//         console.log(error.message);
//     }
//     addGradeToTable();
// });
