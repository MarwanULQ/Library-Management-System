from models.room_model import Room
from services.frontend.api_helper import ApiHelper

class RoomService:

    @staticmethod
    def get_room_by_Id(roomId: int) -> Room:

        try:
            response = ApiHelper.get(f"/db/rooms/{roomId}")
        except Exception as e:
            raise Exception(f"An error occurred while fetching the room: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to fetch room: {response.json().get('detail')}")

        return Room.from_json(response.json())
    
    @staticmethod
    def get_all_rooms() -> list[Room]:

        try:
            response = ApiHelper.get(f"/db/rooms")
        except Exception as e:
            raise Exception(f"An error occurred while fetching the rooms: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to fetch rooms: {response.json().get('detail')}")

        return [Room.from_json(r) for r in response.json()]

    @staticmethod
    def create_room(room: Room) -> Room:

        try:
            response = ApiHelper.post(f"/db/rooms", data=room.to_json())
        except Exception as e:
            raise Exception(f"An error occurred while creating the room: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to create room: {response.json().get('detail')}")

        return Room.from_json(response.json())
        
    