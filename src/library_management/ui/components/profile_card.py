import streamlit as st
from ui.components.base import BaseComponent

class ProfileCard(BaseComponent):
    def __init__(self, user_data: dict):
        self.user_data = user_data

    def render(self):
        _, col = st.columns([1, 2])

        with col:
            st.markdown(
                f"""
                <div class="card">
                    <h3>{self.user_data.get("name", "N/A")}</h3>
                    <p><b>Email:</b> {self.user_data.get("email", "N/A")}</p>
                    <p><b>ID:</b> {self.user_data.get("student_id", "N/A")}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
