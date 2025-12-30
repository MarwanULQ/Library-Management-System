import streamlit as st
from services.frontend.auth_service import AuthService

class AuthController:
    @staticmethod
    def submit(email: str, password: str):
        if not email or not password:
            st.error("Please fill all fields correctly")
            return

        if st.session_state.auth_mode == "signup":
            if "@ejust.edu.eg" not in email:
                st.error(
                    "Don't have access to the Uni Library. "
                    "You should have an E-JUST Email."
                )
                return

        try:
            if st.session_state.auth_mode == "signup":
                result = AuthService.signup(email, password)
            else:
                result = AuthService.login(email, password)

            st.session_state.logged_in = True
            st.session_state.user_id = result[0]
            st.session_state.email = email
            st.session_state.student_id = email.split("@")[0].split(".")[1] if result[1] != "Staff" else None

            st.success("Authentication successful!")
            st.switch_page("pages/home.py")

        except TypeError:
            st.error("Email already exists")
        except Exception as e:
            st.error(str(e))
