class UserRepo:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserRepo, cls).__new__(cls)
            cls._instance.users = []
        return cls._instance

    def load_users(self):
        # Mock data مؤقت
        self.users = [
            {
                "id": 120230129,
                "name": "Ali",
                "books": ["Berserk"]
            },
            {
                "id": 120230102,
                "name": "Marwan",
                "books": ["Star wars"]
            }
        ]

    def get_users(self):
        return self.users
