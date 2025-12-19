class BookRepo:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BookRepo, cls).__new__(cls)
            cls._instance.books = []
        return cls._instance

    def load_books(self):
      
        self.books = [
            {"id": 1, "title": "CleanUnityPython", "room": "Room A"},
            {"id": 2, "title": "AdvProg", "room": "Room B"}
        ]

    def get_books(self):
        return self.books
