import re


# =========================================================
# SKILLS DATABASE
# =========================================================

SKILLS_DATABASE = {
    "Programming": [
        "python",
        "java",
        "c",
        "c++",
        "c#",
        "javascript",
        "typescript",
        "php"
    ],

    "Data Science": [
        "data science",
        "data analysis",
        "data analytics",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "statistics",
        "eda",
        "data visualization"
    ],

    "Data Tools": [
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "excel",
        "tableau",
        "power bi"
    ],

    "Database": [
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "oracle",
        "database",
        "dbms"
    ],

    "Web Development": [
        "html",
        "css",
        "javascript",
        "react",
        "angular",
        "node.js",
        "nodejs",
        "fastapi",
        "flask",
        "django"
    ],

    "Cloud": [
        "aws",
        "azure",
        "google cloud",
        "gcp",
        "firebase"
    ],

    "Tools": [
        "git",
        "github",
        "vs code",
        "visual studio code",
        "google colab",
        "jupyter",
        "docker"
    ],

    "Soft Skills": [
        "communication",
        "teamwork",
        "leadership",
        "problem solving",
        "critical thinking",
        "time management"
    ]
}


# =========================================================
# CLEAN TEXT
# =========================================================

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# =========================================================
# DETECT SKILLS
# =========================================================

def detect_skills(resume_text):

    text = clean_text(resume_text)

    detected_skills = []

    for category, skills in SKILLS_DATABASE.items():

        for skill in skills:

            skill_lower = skill.lower()

            if skill_lower in text:

                if skill not in detected_skills:

                    detected_skills.append(skill)

    return detected_skills


# =========================================================
# DETECT RESUME SECTIONS
# =========================================================

def detect_sections(resume_text):

    text = clean_text(resume_text)

    sections = {

        "contact": False,
        "summary": False,
        "education": False,
        "skills": False,
        "experience": False,
        "projects": False,
        "certifications": False
    }


    # Contact
    if (
        "@" in text
        or re.search(
            r"\+?\d[\d\s\-]{8,}",
            text
        )
    ):
        sections["contact"] = True


    # Summary
    if any(word in text for word in [
        "profile summary",
        "professional summary",
        "career objective",
        "objective",
        "summary"
    ]):
        sections["summary"] = True


    # Education
    if any(word in text for word in [
        "education",
        "university",
        "college",
        "degree",
        "b.sc",
        "b.tech",
        "bachelor"
    ]):
        sections["education"] = True


    # Skills
    if any(word in text for word in [
        "skills",
        "technical skills",
        "programming"
    ]):
        sections["skills"] = True


    # Experience
    if any(word in text for word in [
        "experience",
        "work experience",
        "internship",
        "intern"
    ]):
        sections["experience"] = True


    # Projects
    if any(word in text for word in [
        "project",
        "projects"
    ]):
        sections["projects"] = True


    # Certifications
    if any(word in text for word in [
        "certification",
        "certifications",
        "certificate"
    ]):
        sections["certifications"] = True


    return sections


# =========================================================
# CALCULATE RESUME SCORE
# =========================================================

def calculate_score(
    resume_text,
    skills,
    sections
):

    score = 0

    word_count = len(
        resume_text.split()
    )


    # Resume content
    if word_count >= 300:
        score += 15

    elif word_count >= 200:
        score += 12

    elif word_count >= 100:
        score += 8

    else:
        score += 4


    # Skills
    skill_count = len(skills)

    if skill_count >= 10:
        score += 20

    elif skill_count >= 7:
        score += 17

    elif skill_count >= 4:
        score += 13

    elif skill_count >= 2:
        score += 8

    else:
        score += 3


    # Sections
    section_points = {

        "contact": 10,
        "summary": 10,
        "education": 10,
        "skills": 10,
        "experience": 10,
        "projects": 10,
        "certifications": 5
    }


    for section, points in section_points.items():

        if sections.get(section):

            score += points


    return min(score, 100)


# =========================================================
# SUGGESTIONS
# =========================================================

def generate_suggestions(
    resume_text,
    skills,
    sections
):

    suggestions = []


    if not sections["contact"]:

        suggestions.append(
            "Add your phone number and professional email address."
        )


    if not sections["summary"]:

        suggestions.append(
            "Add a short professional summary or career objective."
        )


    if not sections["skills"]:

        suggestions.append(
            "Add a dedicated Technical Skills section."
        )


    if not sections["education"]:

        suggestions.append(
            "Add your educational qualifications."
        )


    if not sections["projects"]:

        suggestions.append(
            "Add relevant academic or personal projects."
        )


    if not sections["experience"]:

        suggestions.append(
            "Add internship, training, or practical experience if available."
        )


    if not sections["certifications"]:

        suggestions.append(
            "Add relevant certifications to strengthen your resume."
        )


    if len(skills) < 5:

        suggestions.append(
            "Add more relevant technical skills related to your target job."
        )


    word_count = len(
        resume_text.split()
    )


    if word_count < 150:

        suggestions.append(
            "Your resume contains limited information. Add more details about skills, projects, education, and achievements."
        )


    if not suggestions:

        suggestions.append(
            "Your resume has a good structure. Continue improving your skills and project descriptions."
        )


    return suggestions


# =========================================================
# MAIN ANALYZER FUNCTION
# =========================================================

def analyze_resume(resume_text):

    skills = detect_skills(
        resume_text
    )

    sections = detect_sections(
        resume_text
    )

    score = calculate_score(
        resume_text,
        skills,
        sections
    )

    suggestions = generate_suggestions(
        resume_text,
        skills,
        sections
    )


    return {

        "score": score,

        "skills": skills,

        "sections": sections,

        "suggestions": suggestions,

        "word_count": len(
            resume_text.split()
        )
    }