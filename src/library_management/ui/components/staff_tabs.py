import streamlit as st
from ui.components.base import BaseComponent

class RoomReservationsTab(BaseComponent):
    def __init__(self, db):
        self.db = db

    def render(self):
        st.subheader("Room Reservation Status")
        reservations = self.db.get_room_reservations()

        if not reservations.empty:
            st.dataframe(reservations, use_container_width=True)
        else:
            st.info("No room reservations found")


class BorrowedBooksTab(BaseComponent):
    def __init__(self, db):
        self.db = db

    def render(self):
        st.subheader("Books Borrowed")
        borrowed_books = self.db.get_borrowed_books()

        if not borrowed_books.empty:
            st.dataframe(borrowed_books, use_container_width=True)
        else:
            st.info("No books currently borrowed")


class ApproveRequestsTab(BaseComponent):
    def __init__(self, db):
        self.db = db

    def render(self):
        st.subheader("Approve Student Requests")
        requests = self.db.get_student_requests()

        if not requests:
            st.info("No requests to approve")
            return

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


class StaffTabs(BaseComponent):
    def __init__(self, db):
        self.db = db

    def render(self):
        tabs = st.tabs(
            ["🏢 Room Reservations", "📚 Books Borrowed", "✅ Approve Requests"]
        )

        with tabs[0]:
            RoomReservationsTab(self.db).render()

        with tabs[1]:
            BorrowedBooksTab(self.db).render()

        with tabs[2]:
            ApproveRequestsTab(self.db).render()
