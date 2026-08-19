const API_URL = "http://127.0.0.1:8000/analyze";

document.addEventListener("DOMContentLoaded", () => {

    const uploadForm = document.getElementById("resumeUploadForm");
    const fileInput = document.getElementById("resumeFile");

    if (!uploadForm || !fileInput) {
        return;
    }

    uploadForm.addEventListener("submit", async (event) => {

        event.preventDefault();

        const file = fileInput.files[0];

        if (!file) {
            alert("Please select your resume first.");
            return;
        }

        const allowedExtensions = ["pdf", "docx"];

        const extension = file.name
            .split(".")
            .pop()
            .toLowerCase();

        if (!allowedExtensions.includes(extension)) {
            alert("Please upload a PDF or DOCX file.");
            return;
        }

        const formData = new FormData();

        formData.append("file", file);

        try {

            // Save loading state
            localStorage.setItem(
                "resumeAnalyzing",
                "true"
            );

            const response = await fetch(
                API_URL,
                {
                    method: "POST",
                    body: formData
                }
            );

            let data;

            try {
                data = await response.json();
            } catch (jsonError) {
                if (!response.ok) {
                    throw new Error(
                        "Unable to reach the backend server or the backend returned an invalid response."
                    );
                }
                throw new Error(
                    "The backend returned an invalid response."
                );
            }

            if (!response.ok) {
                throw new Error(
                    data?.detail || "Resume analysis failed."
                );
            }

            // Save complete analysis result
            localStorage.setItem(
                "resumeAnalysis",
                JSON.stringify(data)
            );

            localStorage.setItem(
                "resumeAnalyzing",
                "false"
            );

            // Go to analysis page
            window.location.href = "analysis.html";

        } catch (error) {

            localStorage.setItem(
                "resumeAnalyzing",
                "false"
            );

            console.error(error);

            alert(
                "Unable to analyze the resume.\n\n" +
                error.message
            );
        }
    });
});