import streamlit as st
from assets.styles import apply_global_styles

# ---------------------- Global Styling -----------------
apply_global_styles()

# ------------------- Local Styling ----------------------
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


class RoomUI:
    """Handles room display and user interface"""
    def __init__(self, manager):
        self.manager = manager
    
    def display_rooms(self):
        st.title("📚 Library Room Reservation System")
        st.markdown("---")
        
        cols = st.columns(2)
        col_idx = 0
        
        for room_id, room in self.manager.get_all_rooms().items():
            with cols[col_idx % 2]:
                self._display_room(room)
            col_idx += 1
    
    def _display_room(self, room):
        st.markdown(
            f"""
            <div class="room-card">
                <div class="room-title">Room {room.room_id}</div>
                <div class="room-meta">Capacity: {room.capacity} persons</div>
            """,
            unsafe_allow_html=True
        )
        
        period_cols = st.columns(3)
        for idx, period in enumerate(room.periods.keys()):
            with period_cols[idx]:
                is_reserved = room.is_reserved(period)
                button_label = f"{period}\n{'✓ Reserved' if is_reserved else 'Available'}"
                
                if st.button(button_label, disabled=is_reserved, key=f"{room.room_id}_{period}"):
                    st.session_state.selected_room = room.room_id
                    st.session_state.selected_period = period
        
        st.markdown("</div>", unsafe_allow_html=True)

    
    def display_modal(self):
        if 'selected_room' in st.session_state:
            room_id = st.session_state.selected_room
            period = st.session_state.selected_period
            room = self.manager.get_room(room_id)
            
            with st.form("reservation_form"):
                st.write(f"### Reserving {room_id} for {period}")
                st.write(f"Room Capacity: {room.capacity} persons")
                
                student_id = st.text_input("Student ID:")
                college = st.text_input("College:")
                level_year = st.selectbox("Level/Year:", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
                
                if st.form_submit_button("Confirm Reservation", type= "primary"):
                    if student_id and college and level_year:
                        room.reserve(period, {
                            'student_id': student_id,
                            'college': college,
                            'level_year': level_year
                        })
                        st.success(f"✓ Room {room_id} reserved for {period}")
                        del st.session_state.selected_room
                        del st.session_state.selected_period
                        st.rerun()
                    else:
                        st.error("Please fill all fields")
                
                if st.form_submit_button("Cancel"):
                    del st.session_state.selected_room
                    del st.session_state.selected_period
                    st.rerun()


# Initialize and run
if 'room_manager' not in st.session_state:
    st.session_state.room_manager = RoomManager()

ui = RoomUI(st.session_state.room_manager)
ui.display_rooms()
ui.display_modal()