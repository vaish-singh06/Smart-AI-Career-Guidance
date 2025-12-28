def recommend_courses(missing_skills: list):
    course_map = {
        "Python": [
            "FreeCodeCamp – Python for Beginners",
            "NPTEL – Programming in Python"
        ],
        "Machine Learning": [
            "Andrew Ng ML (YouTube – Free)",
            "NPTEL – Machine Learning"
        ],
        "Statistics": [
            "Khan Academy – Statistics",
            "NPTEL – Probability & Statistics"
        ],
        "Deep Learning": [
            "DeepLearning.AI YouTube",
            "NPTEL – Deep Learning"
        ],
        "SQL": [
            "FreeCodeCamp – SQL",
            "Khan Academy – SQL Basics"
        ]
    }

    recommendations = {}

    for skill in missing_skills:
        if skill in course_map:
            recommendations[skill] = course_map[skill]

    return recommendations
