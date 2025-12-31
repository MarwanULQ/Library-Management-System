from assets.styles import apply_global_styles
from ui.components.staff_header import StaffHeader
from ui.components.staff_tabs import StaffTabs
import streamlit as st

if st.session_state.logged_in and st.session_state.role == "Staff":
    apply_global_styles()
    StaffHeader().render()
    StaffTabs().render()
else:
    st.error("You should Login as an Admin to access this page. You shouldn't be here, Nigga")