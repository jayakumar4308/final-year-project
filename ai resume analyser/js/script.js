console.log("ResumeAI Frontend Loaded");

const API_URL = "https://final-year-project-zxu5.onrender.com/analyze";

document.addEventListener("DOMContentLoaded", function () {

    const buttons = document.querySelectorAll("a");

    buttons.forEach(function (button) {
        button.addEventListener("click", function () {
            console.log("Opening:", button.textContent.trim());
        });
    });


    // =====================================================
    // FIND RESUME UPLOAD FORM
    // =====================================================

    const resumeForm = document.querySelector("form");
    const fileInput = document.querySelector(
        'input[type="file"]'
    );


    if (!resumeForm || !fileInput) {
        console.log("Resume upload form not found.");
        return;
    }


    // =====================================================
    // RESUME ANALYSIS
    // =====================================================

    resumeForm.addEventListener("submit", async function (event) {

        event.preventDefault();

        const file = fileInput.files[0];

        if (!file) {
            alert("Please upload your resume first.");
            return;
        }


        // Check file type

        const allowedExtensions = [
            ".pdf",
            ".docx"
        ];

        const fileName = file.name.toLowerCase();

        const validFile = allowedExtensions.some(
            extension => fileName.endsWith(extension)
        );


        if (!validFile) {
            alert("Please upload a PDF or DOCX file.");
            return;
        }


        // =================================================
        // SEND FILE TO FASTAPI
        // =================================================

        const formData = new FormData();

        formData.append("file", file);


        try {

            console.log("Uploading resume...");


            const response = await fetch(
                API_URL,
                {
                    method: "POST",
                    body: formData
                }
            );


            const data = await response.json();


            // =================================================
            // ERROR FROM BACKEND
            // =================================================

            if (!response.ok) {

                console.error(
                    "Backend Error:",
                    data
                );

                alert(
                    data.detail ||
                    "Resume analysis failed."
                );

                return;
            }


            // =================================================
            // SUCCESS
            // =================================================

            console.log(
                "Resume analyzed successfully:",
                data
            );


            // Save result for result page

            localStorage.setItem(
                "resumeAnalysis",
                JSON.stringify(data)
            );


            // Go to result page

            window.location.href = "result.html";


        } catch (error) {

            console.error(
                "Connection Error:",
                error
            );


            alert(
                "Could not connect to the AI Resume Analyzer backend."
            );
        }

    });

});
