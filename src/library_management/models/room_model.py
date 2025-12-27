from dataclasses import dataclass

@dataclass
class Room:
    room_id: int
    capacity: int
    floor: int

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            room_id=data.get("room_id"),
            capacity=data.get("capacity"),
            floor=data.get("floor")
        )
    
    def to_json(self) -> dict:
        return {
            "room_id": self.room_id,
            "capacity": self.capacity,
            "floor": self.floor
        }