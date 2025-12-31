import streamlit as st
from ui.components.base import BaseComponent
from services.frontend.loan_service import LoanService

class BorrowButton(BaseComponent):
    def __init__(self, *, can_borrow: bool, student_id: int, book_id: int):
        self.can_borrow = can_borrow
        self.student_id = student_id
        self.book_id = book_id

    def render(self):
        if not self.can_borrow:
            st.button("✅ Already Borrowed", disabled=True)
            return

        if st.button("📥 Borrow Book"):
            try:
                LoanService.create_loan(
                    student_id=self.student_id,
                    book_id=self.book_id
                )
                st.success("Loan created successfully.")
                st.rerun()
            except Exception as e:
                st.error(str(e))
