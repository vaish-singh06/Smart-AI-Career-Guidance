def match_jobs(skills: list):
    job_map = {
        "Python": [
            "Python Developer Intern",
            "Junior Python Developer"
        ],
        "Machine Learning": [
            "ML Intern",
            "Machine Learning Engineer (Entry-Level)"
        ],
        "Data Science": [
            "Data Analyst Intern",
            "Data Scientist (Entry-Level)"
        ],
        "Deep Learning": [
            "AI Research Intern",
            "Deep Learning Engineer"
        ],
        "SQL": [
            "Data Analyst Intern",
            "Business Intelligence Analyst"
        ]
    }

    matched_roles = set()

    for skill in skills:
        if skill in job_map:
            for role in job_map[skill]:
                matched_roles.add(role)

    return list(matched_roles)
