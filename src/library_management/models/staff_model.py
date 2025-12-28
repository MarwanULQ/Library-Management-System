from dataclasses import dataclass
from enum import Enum

@dataclass
class Staff:
    staff_id: int
    full_name: str
    email: str
    role: StaffRole

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            staff_id=data.get("staff_id"),
            full_name=data.get("full_name"),
            email=data.get("email"),
            role=StaffRole(data.get("role"))
        )
    
    def to_json(self) -> dict:
        return {
            "staff_id": self.staff_id,
            "full_name": self.full_name,
            "email": self.email,
            "role": self.role.value
        }
    
class StaffRole(str, Enum):
    Librarian = "Librarian"
    Admin = "Admin"
