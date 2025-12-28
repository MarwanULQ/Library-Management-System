from dataclasses import dataclass

@dataclass
class Student:
    student_id: int
    full_name: str
    email: str

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            student_id=data.get("student_id"),
            full_name=data.get("full_name"),
            email=data.get("email")
        )
    
    def to_json(self) -> dict:
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "email": self.email
        }