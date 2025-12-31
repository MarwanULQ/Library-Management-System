import streamlit as st
from ui.components.base import BaseComponent
from models.loan_model import Loan, LoanStatus, LoanRequestType
from services.frontend.loan_service import LoanService
from services.cache_helper import Cache


#-------------- Cache Helper ------------#

cache = Cache()

def get_all_loans(force_refresh=False) -> list[Loan]:
    if force_refresh or cache.get("all_loans") is None:
        try:
            loans = LoanService.get_loans()
            cache.set("all_loans", loans)
        except Exception as e:
            st.error(f"⚠️ Failed to load loans: {e}")
            return []

    return cache.get("all_loans")

import streamlit as st

class PendingLoansTab:
    def render(self):
        st.subheader("📥 Pending Loan Requests")

        loans = get_all_loans()
        pending_loans = [
            l for l in loans if l.status == LoanStatus.Pending
        ]

        if not pending_loans:
            st.info("No pending loan requests.")
            return

        for loan in pending_loans:
            with st.container(border=True):
                st.markdown(f"""
                **Loan ID:** {loan.loan_id}  
                **Student ID:** {loan.student_id}  
                **Copy ID:** {loan.copy_id}  
                **Requested At:** {loan.created_at.strftime("%Y-%m-%d %H:%M")}
                """)

                col1, col2 = st.columns(2)

                with col1:
                    if st.button("✅ Approve", key=f"approve_{loan.loan_id}"):
                        LoanService.loan_request(
                            loan.loan_id,
                            LoanRequestType.Accept
                        )
                        cache.delete("all_loans")
                        st.success("Loan approved.")
                        st.rerun()

                with col2:
                    if st.button("❌ Reject", key=f"reject_{loan.loan_id}"):
                        LoanService.loan_request(
                            loan.loan_id,
                            LoanRequestType.Reject
                        )
                        cache.delete("all_loans")
                        st.warning("Loan rejected.")
                        st.rerun()

class ActiveLoansTab:
    def render(self):
        st.subheader("📚 Active Loans")

        loans = get_all_loans()
        active_loans = [
            l for l in loans if l.status == LoanStatus.Active
        ]

        if not active_loans:
            st.info("No active loans.")
            return

        for loan in active_loans:
            with st.container(border=True):
                approved_at = (
                    loan.approved_at.strftime("%Y-%m-%d %H:%M")
                    if loan.approved_at is not None
                    else "Not approved yet"
                )
                st.markdown(f"""
                **Loan ID:** {loan.loan_id}  
                **Student ID:** {loan.student_id}  
                **Copy ID:** {loan.copy_id}  
                **Approved At:** {approved_at}
                """)

                if st.button(
                    "📦 Mark as Returned",
                    key=f"return_{loan.loan_id}"
                ):
                    LoanService.loan_request(
                        loan.loan_id,
                        LoanRequestType.Return
                    )
                    cache.delete("all_loans")
                    st.success("Book marked as returned.")
                    st.rerun()

class LoanHistoryTab:
    def render(self):
        st.subheader("📦 Loan History")

        loans = get_all_loans()
        history = [
            l for l in loans
            if l.status in (LoanStatus.Returned, LoanStatus.Rejected)
        ]

        if not history:
            st.info("No completed loans.")
            return

        for loan in history:
            with st.container(border=True):
                st.markdown(f"""
                **Loan ID:** {loan.loan_id}  
                **Student ID:** {loan.student_id}  
                **Copy ID:** {loan.copy_id}  
                **Status:** `{loan.status.value}`  
                **Created:** {loan.created_at.strftime("%Y-%m-%d")}
                """)


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


class StaffTabs:
    def render(self):
        tabs = st.tabs([
            "📥 Pending Requests",
            "📚 Active Loans",
            "📦 Loan History"
        ])

        with tabs[0]:
            PendingLoansTab().render()

        with tabs[1]:
            ActiveLoansTab().render()

        with tabs[2]:
            LoanHistoryTab().render()

