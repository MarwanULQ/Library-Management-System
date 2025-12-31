import streamlit as st
from ui.components.base import BaseComponent

class BorrowedBooksTab(BaseComponent):
    def __init__(self, user_data: dict):
        self.user_data = user_data

    def render(self):
        st.subheader("Currently Borrowed")
        borrowed = self.user_data.get("borrowed_books", [])

        if borrowed:
            for book in borrowed:
                st.markdown(
                    f"""
                    <div class="card" style="margin-bottom:10px">
                        <b>{book['title']}</b><br>
                        <small>Due: {book['due_date']}</small>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.info("No books borrowed")


class AccountSettingsTab(BaseComponent):
    def render(self):
        st.subheader("Account Settings")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔐 Change Password", key="change_password"):
                st.session_state.show_password_form = True

        with col2:
            if st.button("✏️ Update Profile", key="update_profile"):
                st.session_state.show_profile_form = True



class ActivityTab(BaseComponent):
    def render(self):
        st.subheader("Activity History")
        st.caption("Recent activities will appear here")


class ProfileTabs(BaseComponent):
    def __init__(self, user_data: dict):
        self.user_data = user_data

    def render(self):
        tab1, tab2, tab3 = st.tabs(
            ["📚 Borrowed Books", "⚙️ Account Settings", "📊 Activity"]
        )

        with tab1:
            BorrowedBooksTab(self.user_data).render()

        with tab2:
            AccountSettingsTab().render()

        with tab3:
            ActivityTab().render()
