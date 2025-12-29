from models.room_reservation_model import RoomReservation, RoomStatus
from services.frontend.api_helper import ApiHelper
from typing import Optional
from datetime import datetime

class RoomReservationService:

    @staticmethod
    def get_room_reservation_by_Id(roomReservationId: int) -> RoomReservation:

        try:
            response = ApiHelper.get(f"/db/room_reservations/{roomReservationId}")
        except Exception as e:
            raise Exception(f"An error occurred while fetching the room reservation: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to fetch room reservation: {response.json().get('detail')}")

        return RoomReservation.from_json(response.json())
    
    @staticmethod
    def get_all_room_reservations() -> list[RoomReservation]:

        try:
            response = ApiHelper.get(f"/db/room_reservations")
        except Exception as e:
            raise Exception(f"An error occurred while fetching the room reservation: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to fetch room reservation: {response.json().get('detail')}")

        return [RoomReservation.from_json(r) for r in response.json()]

    @staticmethod
    def create_room_reservation(roomReservation: RoomReservation) -> bool:

        try:
            response = ApiHelper.post(f"/db/room_reservation", data=roomReservation.to_json())
        except Exception as e:
            raise Exception(f"An error occurred while creating the room reservation: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to create room reservation: {response.json().get('detail')}")

        return True
    
    @staticmethod
    def update_room_reservation(roomReservationId, status: Optional[RoomStatus] = None, approved_at: Optional[datetime]=None, staff_id: Optional[int]=None) -> RoomReservation:
        
        roomReservationPatches = {}

        if status is not None:
            roomReservationPatches["status"] = status.value
        if approved_at is not None:
            roomReservationPatches["approved_at"] = approved_at.isoformat()
        if staff_id is not None:
            roomReservationPatches["staff_id"] = staff_id

        try:
            response = ApiHelper.patch(f"/db/room_reservation/{roomReservationId}", data=roomReservationPatches)
        except Exception as e:
            raise Exception(f"An error occurred while updating the room reservation: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to update room reservation: {response.json().get('detail')}")

        return RoomReservation.from_json(response.json())
        
    