import streamlit as st
from ui.components.base import BaseComponent

class CTAButtons(BaseComponent):
    def render(self):
        st.markdown(
            """
            <style>
                .stButton > button:hover {
                    background-color: #AEBFD4 !important;
                }

                .stButton > button {
                    font-family: inherit;
                    background-color: #BCCCDC;
                    color: #000000;
                    border: 1px solid #4b5563;
                    border-radius: 4px;
                    font-size: 18px;
                    padding: 20px 20px;
                    width: 140%;
                    font-weight: 800;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown('<div class="home-cta">', unsafe_allow_html=True)

        _, col2, _= st.columns([1, 3, 1])
        with col2:
            left, _, middle, _, right = st.columns(5)

            with left:
                if st.button("📚 Browse Books"):
                    st.switch_page("pages/browse.py")

            with middle:
                if st.button("🏫 Room Reservation"):
                    st.switch_page("pages/room.py")

            with right:
                if st.button("👤 Profile"):
                    st.switch_page("pages/profile.py")

        st.markdown("</div>", unsafe_allow_html=True)
