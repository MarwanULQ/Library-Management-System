import streamlit as st
from ui.components.base import BaseComponent

class RoomReservationModal(BaseComponent):
    def __init__(self, manager):
        self.manager = manager

    def render(self):
        if "selected_room" not in st.session_state:
            return

        room_id = st.session_state.selected_room
        period = st.session_state.selected_period
        room = self.manager.get_room(room_id)

        with st.form(key=f"reservation_form_{room_id}_{period}"):
            st.write(f"### Reserving {room_id} for {period}")
            st.write(f"Room Capacity: {room.capacity} persons")

            student_id = st.text_input("Student ID")
            college = st.text_input("College")
            level_year = st.selectbox(
                "Level/Year",
                ["1st Year", "2nd Year", "3rd Year", "4th Year"]
            )

            submit = st.form_submit_button("Confirm Reservation")
            cancel = st.form_submit_button("Cancel")

            if submit:
                if student_id and college and level_year:
                    room.reserve(period, {
                        "student_id": student_id,
                        "college": college,
                        "level_year": level_year
                    })
                    st.success(f"✓ Room {room_id} reserved for {period}")
                    self._clear()
                    st.rerun()
                else:
                    st.error("Please fill all fields")

            if cancel:
                self._clear()
                st.rerun()

    @staticmethod
    def _clear():
        del st.session_state.selected_room
        del st.session_state.selected_period
