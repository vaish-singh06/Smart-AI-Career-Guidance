from ai_config.groq_llm import get_llm
from tools.skill_gap_tool import analyze_skill_gap


def run_skill_analysis(profile: dict):
    llm = get_llm()

    # Deterministic skill gap analysis
    skill_gap_result = analyze_skill_gap(
        profile["skills"],
        profile["interests"]
    )

    prompt = f"""
You are a career guidance AI.

Student Profile:
Degree: {profile['degree']}
Year: {profile['year']}
Skills: {profile['skills']}
Interests: {profile['interests']}

Skill Gap Analysis (calculated by system):
{skill_gap_result}

Tasks:
1. Identify strengths
2. Identify weaknesses
3. Clearly explain missing skills
4. Use simple student-friendly language
"""

    response = llm.invoke(prompt)
    return response.content


def extract_skill_gaps(profile: dict):
    analysis = analyze_skill_gap(
        profile["skills"],
        profile["interests"]
    )
    return analysis["missing_skills"]
