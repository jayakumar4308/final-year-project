# =========================================================
# JOB DATABASE
# =========================================================

JOB_DATABASE = {

    "Python Developer": [
        "python",
        "git",
        "github"
    ],

    "Data Analyst": [
        "python",
        "pandas",
        "numpy",
        "excel",
        "sql",
        "data analysis",
        "data visualization"
    ],

    "Data Scientist": [
        "python",
        "pandas",
        "numpy",
        "machine learning",
        "statistics",
        "scikit-learn",
        "data science"
    ],

    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "numpy",
        "pandas"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node.js"
    ],

    "Backend Developer": [
        "python",
        "fastapi",
        "flask",
        "django",
        "sql",
        "mongodb"
    ],

    "Database Developer": [
        "sql",
        "mysql",
        "postgresql",
        "oracle",
        "database",
        "dbms"
    ],

    "Business Analyst": [
        "excel",
        "sql",
        "data analysis",
        "communication",
        "problem solving"
    ]
}


# =========================================================
# RECOMMEND JOBS
# =========================================================

def recommend_jobs(skills):

    user_skills = set(
        skill.lower()
        for skill in skills
    )

    recommendations = []


    for job, required_skills in JOB_DATABASE.items():

        required = set(
            skill.lower()
            for skill in required_skills
        )

        matched = user_skills.intersection(
            required
        )


        if len(matched) > 0:

            percentage = (
                len(matched)
                / len(required)
            ) * 100


            recommendations.append({

                "job": job,

                "match_percentage": round(
                    percentage,
                    2
                ),

                "matched_skills": sorted(
                    list(matched)
                )
            })


    # Highest match first
    recommendations.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )


    return recommendations[:5]