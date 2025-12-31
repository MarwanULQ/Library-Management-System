from assets.styles import apply_global_styles
from ui.components.staff_header import StaffHeader
from ui.components.staff_tabs import StaffTabs
import streamlit as st

if st.session_state.logged_in and st.session_state.role == "Staff":
    apply_global_styles()
    StaffHeader().render()
    StaffTabs().render()
else:
    st.error("You must Sign in and better to be an admin to access staff dashboard")