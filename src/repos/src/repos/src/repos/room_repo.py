class RoomRepo:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RoomRepo, cls).__new__(cls)
            cls._instance.rooms = []
        return cls._instance

    def load_rooms(self):
        self.rooms = [
            {"id": 120230129, "Ali": "Room A"},
            {"id": 120230102, "Marwan": "Room B"}
        ]

    def get_rooms(self):
        return self.rooms
