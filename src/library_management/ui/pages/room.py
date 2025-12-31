import streamlit as st
from assets.styles import apply_global_styles
from ui.components.room_header import RoomHeader
from ui.components.room_grid import RoomGrid
from ui.components.room_modal import RoomReservationModal

class Room:
    """Represents a single room"""
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity
        self.periods = {
            '9-11 AM': None,
            '11 AM-1 PM': None,
            '1-3 PM': None
        }
    
    def is_reserved(self, period):
        return self.periods[period] is not None
    
    def reserve(self, period, student_data):
        self.periods[period] = student_data
    
    def cancel_reservation(self, period):
        self.periods[period] = None


class RoomManager:
    """Manages room operations"""
    def __init__(self):
        self.rooms = {}
        self._initialize_rooms()
    
    def _initialize_rooms(self):
        for floor in range(1, 3):
            for room in range(1, 6):
                room_id = f"F{floor}-R{room}"
                self.rooms[room_id] = Room(room_id, 2 + room)
    
    def get_room(self, room_id):
        return self.rooms.get(room_id)
    
    def get_all_rooms(self):
        return self.rooms


if st.session_state.logged_in:

    apply_global_styles()
    st.markdown(
        """
        <style>
            /* ===== FIX: form submit button visibility ===== */
            .stFormSubmitButton > button {
                background-color: #EEEEEE; 
                color: white;              /* White text */
                padding: 10px 24px;        /* Add padding */
                border-radius: 8px;        /* Rounded corners */
                font-size: 20px;           /* Larger font */
                margin: 10px 0px;          /* Add margin */
            }

            .stFormSubmitButton > button:hover {
                background-color: #FFFFFF;
            }


            /* ===== Room cards ===== */
            .room-card {
                background-color: #E5EAF0;
                border: 1px solid #4b5563;
                border-radius: 6px;
                padding: 18px 20px;
                margin-bottom: 22px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            }

            .room-title {
                font-size: 20px;
                font-weight: 800;
                margin-bottom: 6px;
            }

            .room-meta {
                font-style: italic;
                color: #444;
                margin-bottom: 14px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    if "room_manager" not in st.session_state:
        st.session_state.room_manager = RoomManager()
    manager = st.session_state.room_manager
    RoomHeader().render()
    RoomGrid(manager).render()
    RoomReservationModal(manager).render()
else:
    st.error("You must Log in to reserve a room")