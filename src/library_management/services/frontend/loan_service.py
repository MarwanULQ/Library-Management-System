from models.loan_model import Loan, LoanRequestType, LoanCreate
from services.frontend.api_helper import ApiHelper

class LoanService:

    @staticmethod
    def get_loans() -> list[Loan]:
        
        try:
            response = ApiHelper.get(f"/db/loans")
        except Exception as e:
            raise Exception(f"Failed to fetch loan: {e}")

        if response.status_code != 200:
            raise Exception(f"Error fetching loan: {response.json().get('detail')}")

        return [Loan.from_json(l) for l in response.json()]
    
    @staticmethod
    def create_loan(student_id: int, book_id: int) -> Loan:
        l = LoanCreate(
            student_id=student_id,
            book_id=book_id
        )
        
        try:
            response = ApiHelper.post("/db/loans", query_params=l.to_json())
        except Exception as e:
            raise Exception(f"Failed to create loan: {e}")  
        
        if response.status_code != 200:
            raise Exception(f"Error creating loan: {response.json().get('detail')}")
        
        return Loan.from_json(response.json())
    
    @staticmethod
    def loan_request(loan_id: int, request: LoanRequestType) -> Loan:
        try:
            response = ApiHelper.patch(f"/db/loans/{loan_id}/{request.value}")
        except Exception as e:
            raise Exception(f"Failed to {request.value} loan: {e}")  
        
        if response.status_code != 200:
            raise Exception(f"Error {request.value} loan: {response.json().get('detail')}")
        
        return Loan.from_json(response.json())
    