from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

@dataclass
class RoomReservation:
    reservation_id: int
    student_id: int
    staff_id: Optional[int]
    room_id: int
    status: RoomStatus
    requested_at: datetime
    approved_at: Optional[datetime]
    start_time: datetime
    end_time: datetime

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            reservation_id=data.get("reservation_id"),
            student_id=data.get("student_id"),
            staff_id=data.get("staff_id"),
            room_id=data.get("room_id"),
            status=RoomStatus(data.get("status")),
            requested_at=datetime.fromisoformat(data.get("requested_at")),
            approved_at=datetime.fromisoformat(data.get("approved_at")) if data.get("approved_at") else None,
            start_time=datetime.fromisoformat(data.get("start_time")),
            end_time=datetime.fromisoformat(data.get("end_time"))
        )
    
    def to_json(self) -> dict:
        return {
            "reservation_id": self.reservation_id,
            "student_id": self.student_id,
            "staff_id": self.staff_id,
            "room_id": self.room_id,
            "status": self.status.value,
            "requested_at": self.requested_at.isoformat(),
            "approved_at": self.approved_at.isoformat() if self.approved_at else None,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat()
        }
    
class RoomStatus(str, Enum):
    Pending = "Pending"
    Approved = "Approved"
    Rejected = "Rejected"
    Active = "Active"
    Finished = "Finished"

@dataclass
class ReservationCreateRequest():
    student_id: int
    room_id: int
    requested_at: datetime
    start_time: datetime
    end_time: datetime 

    def to_json(self) -> dict:
        return {
            "student_id": self.student_id,
            "room_id": self.room_id,
            "requested_at": self.requested_at.isoformat(),
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat()
        }
    
class ReservationUpdateRequestType(Enum):
    Approve = "approve"
    Reject = "reject"
    Activate = "activate"
    Complete = "complete"