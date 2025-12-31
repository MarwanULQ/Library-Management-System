import streamlit as st
import pandas as pd
from assets.styles import apply_global_styles
from ui.components.staff_header import StaffHeader
from ui.components.staff_tabs import StaffTabs
class MockDatabase:
    def __init__(self):
        self.room_reservations = pd.DataFrame({
            "Room ID": [101, 102],
            "Room Name": ["Conference Room", "Study Room"],
            "Reserved By": ["Alice", "Bob"],
            "Date": ["2023-10-01", "2023-10-02"],
            "Time Slot": ["10:00-12:00", "14:00-16:00"],
            "Status": ["Confirmed", "Pending"]
        })

        self.borrowed_books = pd.DataFrame({
            "Book ID": [1, 2],
            "Title": ["Python Programming", "Data Science"],
            "Author": ["John Doe", "Jane Smith"],
            "Borrowed By": ["Alice", "Bob"],
            "Borrow Date": ["2023-09-25", "2023-09-26"],
            "Due Date": ["2023-10-25", "2023-10-26"],
            "Status": ["Borrowed", "Borrowed"]
        })

        self.student_requests = [
            {"id": 1, "details": "Request for additional study materials"},
            {"id": 2, "details": "Request for room extension"}
        ]

    def get_room_reservations(self):
        return self.room_reservations

    def get_borrowed_books(self):
        return self.borrowed_books

    def get_student_requests(self):
        return self.student_requests

    def approve_request(self, request_id):
        self.student_requests = [
            r for r in self.student_requests if r["id"] != request_id
        ]


# ---------- Persist DB ----------
if "db" not in st.session_state:
    st.session_state.db = MockDatabase()

db = st.session_state.db


apply_global_styles()
StaffHeader().render()
StaffTabs(db).render()