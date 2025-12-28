from models.student_model import Student
from services.frontend.api_helper import ApiHelper

class StudentService:

    @staticmethod
    def get_student(studentId: int) -> Student:

        try:
            response = ApiHelper.get(f"/db/students/{studentId}")
        except Exception as e:
            raise Exception(f"An error occurred while fetching the student: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to fetch student: {response.json().get('detail')}")

        return Student.from_json(response.json())
    
    @staticmethod
    def create_student(student: Student) -> Student:

        try:
            response = ApiHelper.post(f"/db/students", data=student.to_json())
        except Exception as e:
            raise Exception(f"An error occurred while creating the student: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to create student: {response.json().get('detail')}")

        return Student.from_json(response.json())
        
    