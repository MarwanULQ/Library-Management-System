import streamlit as st
from ui.components.base import BaseComponent

class RoomCard(BaseComponent):
    def __init__(self, room):
        self.room = room

    def render(self):
        st.markdown(
            f"""
            <div class="room-card">
                <div class="room-title">Room {self.room.room_id}</div>
                <div class="room-meta">Capacity: {self.room.capacity} persons</div>
            """,
            unsafe_allow_html=True
        )

        cols = st.columns(3)
        for idx, period in enumerate(self.room.periods.keys()):
            with cols[idx]:
                is_reserved = self.room.is_reserved(period)
                label = f"{period}\n{'✓ Reserved' if is_reserved else 'Available'}"

                if st.button(
                    label,
                    key=f"{self.room.room_id}_{period}",
                    disabled=is_reserved
                ):
                    st.session_state.selected_room = self.room.room_id
                    st.session_state.selected_period = period

        st.markdown("</div>", unsafe_allow_html=True)
