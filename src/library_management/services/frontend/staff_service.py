from models.staff_model import Staff
from services.frontend.api_helper import ApiHelper

class StaffService:

    @staticmethod
    def get_staff(staffId: int) -> Staff:

        try:
            response = ApiHelper.get(f"/db/staff/{staffId}")
        except Exception as e:
            raise Exception(f"An error occurred while fetching the staff: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to fetch staff: {response.json().get('detail')}")

        return Staff.from_json(response.json())
    
    @staticmethod
    def create_staff(staff: Staff) -> Staff:

        try:
            response = ApiHelper.post(f"/db/staff", data=staff.to_json())
        except Exception as e:
            raise Exception(f"An error occurred while creating the staff: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to create staff: {response.json().get('detail')}")

        return Staff.from_json(response.json())
        
    