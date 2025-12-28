from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from supabase_client import supabase

router = APIRouter()

class ProfileRequest(BaseModel):
    user_id: str
    name: str
    degree: str
    year: str
    skills: str
    interests: str

@router.post("/profile")
def save_profile(profile: ProfileRequest):
    try:
        supabase.table("students").insert({
            "id": profile.user_id,
            "name": profile.name,
            "degree": profile.degree,
            "year": profile.year,
            "skills": profile.skills,
            "interests": profile.interests
        }).execute()

        return {"message": "Profile saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
