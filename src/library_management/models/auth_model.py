from pydantic import BaseModel, EmailStr
from enum import Enum

class AuthRequest(BaseModel):
    email: EmailStr
    password: str

class UserRole(str, Enum):
    STAFF = "Staff"
    STUDENT = "Student"