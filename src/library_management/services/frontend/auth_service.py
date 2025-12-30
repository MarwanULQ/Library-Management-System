from typing import Optional
from services.frontend.api_helper import ApiHelper
from models.auth_model import UserRole

class AuthService:

    @staticmethod
    def login(email: str, password: str):
        data = {
            "email": email,
            "password": password,
            "role": ""
        }

        try:
            response = ApiHelper.post("/auth/login", data=data)
        except Exception as e:
            print(f"An error occurred during login: {e}")
            return None

        if response.status_code != 200:
            raise Exception(f"Login failed: {response.json().get('detail')}")

        result = (response.json().get("userId"), response.json().get("role"))

        return result

    @staticmethod
    def signup(email: str, password: str, role: UserRole):
        data = {
            "email": email,
            "password": password,
            "role": role.value
        }

        try:
            response = ApiHelper.post("/auth/signup", data=data)
        except Exception as e:
            raise Exception(f"Signup failed: {e}")

        if response.status_code != 200:
            print(f"Signup failed: {response.json().get('detail')}")
            return None
        
        result = (response.json().get("userId"), response.json().get("role"))

        return result
    
    @staticmethod
    def logout() -> bool:
        # TODO: Implement logout functionality if needed
        return True
    