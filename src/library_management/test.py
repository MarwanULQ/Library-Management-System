from services.frontend.loan_service import LoanService
from services.frontend.room_reservation_service import RoomReservationService   
from models.room_reservation_model import ReservationCreateRequest, RoomSlot
from datetime import datetime,date
r = ReservationCreateRequest(
    student_id=1,
    room_id=1,
    slot=RoomSlot.Morning,
    date=date.today()
)

try:
    x= LoanService.create_loan(1,2)
except Exception as e:
    print(f"An error occurred: {e}")
else:

    print(x)