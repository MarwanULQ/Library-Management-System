from dataclasses import dataclass
from datetime import datetime
from enum import Enum

@dataclass
class RoomReservation:
    reservation_id: int
    student_id: int
    staff_id: int
    room_id: int
    status: RoomStatus
    requested_at: datetime
    approved_at: datetime
    start_time: datetime
    end_time: datetime

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            reservation_id=data.get("reservation_id"),
            student_id=data.get("student_id"),
            staff_id=data.get("staff_id"),
            room_id=data.get("room_id"),
            status=data.get("status"),
            requested_at=data.get("requested_at"),
            approved_at=data.get("approved_at"),
            start_time=data.get("start_time"),
            end_time=data.get("end_time")
        )
    
    def to_json(self) -> dict:
        return {
            "reservation_id": self.reservation_id,
            "student_id": self.student_id,
            "staff_id": self.staff_id,
            "room_id": self.room_id,
            "status": self.status,
            "requested_at": self.requested_at,
            "approved_at": self.approved_at,
            "start_time": self.start_time,
            "end_time": self.end_time
        }
    
class RoomStatus(str, Enum):
    Pending = "Pending"
    Approved = "Approved"
    Rejected = "Rejected"
    Active = "Active"
    Finished = "Finished"