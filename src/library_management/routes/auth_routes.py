from fastapi import APIRouter, HTTPException
from ..services.auth_services import signup, login

router = APIRouter(prefix="/auth")

@router.post("/signup")
def signup(email: str, password: str):
    try:
        user_id = signup(email, password)
        return {"userId": user_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(email: str, password: str):
    try:
        user_id = login(email, password)
        return {"userId": user_id}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
