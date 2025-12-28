def analyze_skill_gap(skills: str, interest: str):
    required_skills_map = {
        "AIML": ["Python", "Machine Learning", "Statistics", "Deep Learning"],
        "Data Science": ["Python", "SQL", "Statistics", "Data Visualization"],
        "Software": ["Python", "DSA", "OOP", "Databases"]
    }

    required_skills = required_skills_map.get(interest, [])
    user_skills = [s.strip() for s in skills.split(",")]

    missing_skills = [s for s in required_skills if s not in user_skills]

    return {
        "required_skills": required_skills,
        "user_skills": user_skills,
        "missing_skills": missing_skills
    }
