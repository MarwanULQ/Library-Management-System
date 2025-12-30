import streamlit as st
from ui.components.base import BaseComponent

class BorrowButton(BaseComponent):
    def __init__(self, borrow_key: str):
        self.borrow_key = borrow_key

    def render(self):
        if not st.session_state[self.borrow_key]:
            if st.button("📥 Borrow Book"):
                st.session_state[self.borrow_key] = True
                st.rerun()
        else:
            st.button("✅ Already Borrowed", disabled=True)
