class RoomRepo:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RoomRepo, cls).__new__(cls)
            cls._instance._rooms = [
                {
                    "id": 1,
                    "name": "Reading Room",
                    "capacity": 20,
                    "available": True
                },
                {
                    "id": 2,
                    "name": "Study Room",
                    "capacity": 10,
                    "available": False
                }
            ]
        return cls._instance

    def get_all(self):
        return self._rooms

    def get_by_id(self, room_id):
        for room in self._rooms:
            if room["id"] == room_id:
                return room
        return None

    def add_room(self, room):
        self._rooms.append(room)
        return room
