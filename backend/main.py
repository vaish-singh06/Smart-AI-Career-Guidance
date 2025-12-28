from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from auth import router as auth_router
from profile import router as profile_router
from agents.skill_agent import run_skill_analysis, extract_skill_gaps
from agents.course_agent import run_course_recommendation
from agents.job_agent import run_job_matching


load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(profile_router, prefix="/student")

@app.get("/")
def root():
    return {"status": "Backend running successfully"}

@app.post("/ai/skill-analysis")
def skill_analysis(profile: dict):
    return {"analysis": run_skill_analysis(profile)}

@app.post("/ai/career-guidance")
def career_guidance(profile: dict):
    skill_analysis = run_skill_analysis(profile)
    skill_gaps = extract_skill_gaps(profile)
    course_recommendations = run_course_recommendation(skill_gaps)

    return {
        "skill_analysis": skill_analysis,
        "skill_gaps": skill_gaps,
        "course_recommendations": course_recommendations
    }

@app.post("/ai/full-career-guidance")
def full_career_guidance(profile: dict):

    # 1️⃣ Skill Analysis
    skill_analysis = run_skill_analysis(profile)

    # 2️⃣ Extract gaps
    skill_gaps = extract_skill_gaps(profile)

    # 3️⃣ Course Recommendation
    course_recommendations = run_course_recommendation(skill_gaps)

    # 4️⃣ Job & Internship Matching
    current_skills = [s.strip() for s in profile["skills"].split(",")]
    job_recommendations = run_job_matching(current_skills)

    return {
        "skill_analysis": skill_analysis,
        "skill_gaps": skill_gaps,
        "courses": course_recommendations,
        "jobs": job_recommendations
    }