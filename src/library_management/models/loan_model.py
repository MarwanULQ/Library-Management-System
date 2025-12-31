from dataclasses import dataclass
from enum import Enum
from datetime import datetime
# class LoanRead(SQLModel):
#     loan_id: int
#     student_id: int
#     copy_id: int
#     staff_id: int | None
#     status: LoanStatus 
#     created_at: datetime
#     approved_at: datetime | None
#     returned_at: datetime | None

@dataclass
class Loan:
    loan_id: int
    student_id: int
    copy_id: int
    staff_id: int | None
    status: LoanStatus
    created_at: datetime
    approved_at: datetime | None
    returned_at: datetime | None

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            loan_id=data.get("loan_id"),
            student_id=data.get("student_id"),
            copy_id=data.get("copy_id"),
            staff_id=data.get("staff_id"),
            status=LoanStatus(data.get("status")),
            created_at=datetime.fromisoformat(data.get("created_at")),
            approved_at=datetime.fromisoformat(data["approved_at"]) if data.get("approved_at") else None,
            returned_at=datetime.fromisoformat(data["returned_at"]) if data.get("returned_at") else None
        )

    def to_json(self) -> dict:
        return {
            "loan_id": self.loan_id,
            "student_id": self.student_id,
            "copy_id": self.copy_id,
            "staff_id": self.staff_id,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "approved_at": self.approved_at.isoformat() if self.approved_at else None,
            "returned_at": self.returned_at.isoformat() if self.returned_at else None
        }

class LoanStatus(str, Enum):
    Pending = "Pending"
    Rejected = "Rejected"
    Active = "Active"
    Returned = "Returned"

class LoanRequestType(Enum):
    Accept = "accept"
    Reject = "reject"
    Return = "return"