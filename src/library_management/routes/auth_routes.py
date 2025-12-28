from fastapi import APIRouter, HTTPException
from ..services.auth_services import signup, login
from ..models.auth_model import AuthRequest  

router = APIRouter(prefix="/auth")

@router.post("/signup")
def signup_api(data: AuthRequest):
    try:
        user_id = signup(data.email, data.password)
        return {"userId": user_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login_api(data: AuthRequest):
    try:
        user_id = login(data.email, data.password)
        return {"userId": user_id}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
