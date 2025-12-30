import streamlit as st
from assets.styles import apply_global_styles


class ProfilePage:
    def __init__(self, user_data: dict):
        self.user_data = user_data

    # ---------- Public API ----------
    def render(self):
        apply_global_styles()
        self._render_header()
        self._render_profile_card()
        self._render_tabs()

    # ---------- Header ----------
    def _render_header(self):
        st.markdown(
            """
            <div class="page-title">
                <span class="accent">P</span>rofile
            </div>
            <div class="page-subtitle">
                Manage your account and activity
            </div>
            <div class="custom-divider-center"></div>
            """,
            unsafe_allow_html=True
        )

    # ---------- Profile Card ----------
    def _render_profile_card(self):
        _, col = st.columns([1, 2])

        with col:
            st.markdown(
                f"""
                <div class="card">
                    <h3>{self.user_data.get("name", "N/A")}</h3>
                    <p><i>Member since {self.user_data.get("join_date", "N/A")}</i></p>
                    <p><b>Email:</b> {self.user_data.get("email", "N/A")}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    # ---------- Tabs ----------
    def _render_tabs(self):
        tab1, tab2, tab3 = st.tabs(
            ["📚 Borrowed Books", "⚙️ Account Settings", "📊 Activity"]
        )

        with tab1:
            self._render_borrowed_books()

        with tab2:
            self._render_account_settings()

        with tab3:
            self._render_activity()

    # ---------- Borrowed Books ----------
    def _render_borrowed_books(self):
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

    # ---------- Account Settings ----------
    def _render_account_settings(self):
        st.subheader("Account Settings")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔐 Change Password", key="change_password"):
                st.session_state.show_password_form = True

        with col2:
            if st.button("✏️ Update Profile", key="update_profile"):
                st.session_state.show_profile_form = True

    # ---------- Activity ----------
    def _render_activity(self):
        st.subheader("Activity History")
        st.caption("Recent activities will appear here")



# ---------- Sample Data ----------
user = {
    'name': st.session_state.email.split("@")[0].split(".")[0].capitalize(),
    'email': st.session_state.email,
    'member_id': st.session_state.user_id,
    'borrowed_books': []
}

page = ProfilePage(user)
page.render()
