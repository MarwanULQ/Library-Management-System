import streamlit as st
import pandas as pd
from assets.styles import apply_global_styles

apply_global_styles()


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


class StaffPage:
    def __init__(self, db):
        self.db = db

    def render(self):
        st.markdown(
            """
            <div class="page-title">
                <span class="accent">S</span>taff Dashboard
            </div>
            <div class="custom-divider-center"></div>
            """,
            unsafe_allow_html=True
        )

        tabs = st.tabs(
            ["🏢 Room Reservations", "📚 Books Borrowed", "✅ Approve Requests"]
        )

        with tabs[0]:
            self.show_room_reservations()

        with tabs[1]:
            self.show_books_borrowed()

        with tabs[2]:
            self.approve_requests()

    def show_room_reservations(self):
        st.subheader("Room Reservation Status")
        reservations = self.db.get_room_reservations()

        if not reservations.empty:
            st.dataframe(reservations, use_container_width=True)
        else:
            st.info("No room reservations found")

    def show_books_borrowed(self):
        st.subheader("Books Borrowed")
        borrowed_books = self.db.get_borrowed_books()

        if not borrowed_books.empty:
            st.dataframe(borrowed_books, use_container_width=True)
        else:
            st.info("No books currently borrowed")

    def approve_requests(self):
        st.subheader("Approve Student Requests")
        requests = self.db.get_student_requests()

        if requests:
            for request in requests:
                st.markdown(
                    f"""
                    <div class="card">
                        <b>Request #{request['id']}</b><br>
                        {request['details']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    f"Approve Request {request['id']}",
                    key=f"approve_{request['id']}"
                ):
                    self.db.approve_request(request["id"])
                    st.success(f"Request {request['id']} approved!")
                    st.rerun()
        else:
            st.info("No requests to approve")


page = StaffPage(db)
page.render()
