from fastapi import APIRouter, HTTPException
from ..services.auth_services import signup, login
from ..models.auth_model import AuthRequest, UserRole

router = APIRouter(prefix="/auth")

@router.post("/signup")
def signup_api(data: AuthRequest):
    try:
        (user_id, role) = signup(data.email, data.password, UserRole.STUDENT.value)
        return {"userId": user_id, "role": role}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login_api(data: AuthRequest):
    try:
        (user_id, role) = login(data.email, data.password)
        return {"userId": user_id, "role": role}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
