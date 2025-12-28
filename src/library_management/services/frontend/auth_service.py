from typing import Optional
from services.frontend.api_helper import ApiHelper

class AuthService:

    @staticmethod
    def login(email: str, password: str) -> Optional[str]:
        data = {
            "email": email,
            "password": password
        }

        try:
            response = ApiHelper.post("/auth/login", data=data)
        except Exception as e:
            print(f"An error occurred during login: {e}")
            return None

        if response.status_code != 200:
            raise Exception(f"Login failed: {response.json().get('detail')}")

        return response.json().get("userId")

    @staticmethod
    def signup(email: str, password: str) -> Optional[str]:
        data = {
            "email": email,
            "password": password
        }

        try:
            response = ApiHelper.post("/auth/signup", data=data)
        except Exception as e:
            raise Exception(f"Signup failed: {e}")

        if response.status_code != 200:
            print(f"Signup failed: {response.json().get('detail')}")
            return None

        return response.json().get("userId")
    
    @staticmethod
    def logout() -> bool:
        # TODO: Implement logout functionality if needed
        return True
    