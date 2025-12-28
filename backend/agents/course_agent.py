from ai_config.groq_llm import get_llm
from tools.course_tool import recommend_courses


def run_course_recommendation(skill_gaps: list):
    llm = get_llm()

    course_data = recommend_courses(skill_gaps)

    prompt = f"""
You are a career guidance AI.

The student is missing the following skills:
{skill_gaps}

Here are FREE learning resources available:
{course_data}

Tasks:
1. Recommend courses skill-wise
2. Explain why each course is useful
3. Suggest a learning order
4. Keep explanation simple for a student
"""

    response = llm.invoke(prompt)
    return response.content
