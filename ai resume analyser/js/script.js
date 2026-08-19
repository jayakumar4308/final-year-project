console.log("ResumeAI Frontend Loaded");

document.addEventListener("DOMContentLoaded", function () {

    const buttons = document.querySelectorAll("a");

    buttons.forEach(function (button) {

        button.addEventListener("click", function () {
            console.log("Opening:", button.textContent.trim());
        });

    });

});