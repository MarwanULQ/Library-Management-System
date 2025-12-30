import streamlit as st
from assets.styles import apply_global_styles
from ui.components.profile_header import ProfileHeader
from ui.components.profile_card import ProfileCard
from ui.components.profile_tabs import ProfileTabs


user_data = {
    "name": st.session_state.email.split("@")[0].split(".")[0].capitalize(),
    "email": st.session_state.email,
    "student_id": st.session_state.email.split("@")[0].split(".")[1]
}

apply_global_styles()

ProfileHeader().render()
ProfileCard(user_data).render()
ProfileTabs(user_data).render()
