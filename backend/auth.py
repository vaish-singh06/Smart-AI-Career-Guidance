from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from supabase_client import supabase

router = APIRouter()

class AuthRequest(BaseModel):
    email: str
    password: str

@router.post("/register")
def register_user(data: AuthRequest):
    try:
        supabase.auth.sign_up({
            "email": data.email,
            "password": data.password
        })
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login_user(data: AuthRequest):
    try:
        res = supabase.auth.sign_in_with_password({
            "email": data.email,
            "password": data.password
        })
        return {
            "message": "Login successful",
            "access_token": res.session.access_token,
            "user_id": res.user.id
        }
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid credentials")
