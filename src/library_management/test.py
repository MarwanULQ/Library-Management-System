from models.student_model import Student
from models.staff_model import Staff, StaffRole
from models.room_model import Room

from services.frontend.student_service import StudentService
from services.frontend.staff_service import StaffService
from services.frontend.room_service import RoomService


print("\n========== STUDENT SERVICE ==========")

student = Student(
    student_id=1,
    full_name="Test Student",
    email="dskf@gmail.com"
)

try:
    created_student = StudentService.create_student(student)
    print("Create student:", created_student)
except Exception as e:
    print("Create student error:", e)

try:
    fetched_student = StudentService.get_student(1)
    print("Get student:", fetched_student)
except Exception as e:
    print("Get student error:", e)


print("\n========== STAFF SERVICE ==========")

staff = Staff(
    staff_id=1,
    full_name="Test Staff",
    role=StaffRole.Librarian,
    email="staff@test.com"
)

try:
    created_staff = StaffService.create_staff(staff)
    print("Create staff:", created_staff)
except Exception as e:
    print("Create staff error:", e)

try:
    fetched_staff = StaffService.get_staff(1)
    print("Get staff:", fetched_staff)
except Exception as e:
    print("Get staff error:", e)


print("\n========== ROOM SERVICE ==========")

room = Room(
    room_id=1,
    capacity=4,
    floor=2
)

try:
    created_room = RoomService.create_room(room)
    print("Create room:", created_room)
except Exception as e:
    print("Create room error:", e)

try:
    fetched_room = RoomService.get_room_by_Id(1)
    print("Get room:", fetched_room)
except Exception as e:
    print("Get room error:", e)

try:
    all_rooms = RoomService.get_all_rooms()
    print("All rooms:", all_rooms)
except Exception as e:
    print("Get all rooms error:", e)