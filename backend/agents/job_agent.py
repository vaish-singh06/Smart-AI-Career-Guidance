from ai_config.groq_llm import get_llm
from tools.job_matching_tool import match_jobs


def run_job_matching(skills: list):
    llm = get_llm()

    # Deterministic job matching
    matched_jobs = match_jobs(skills)

    prompt = f"""
You are a career guidance AI.

Student has the following skills:
{skills}

Based on these skills, the system matched the following
internship and entry-level job roles:
{matched_jobs}

Tasks:
1. Group roles into Internships and Entry-Level Jobs
2. Explain why each role is suitable for the student
3. Suggest which roles to apply for first
4. Keep language simple and student-friendly
"""

    response = llm.invoke(prompt)
    return response.content
