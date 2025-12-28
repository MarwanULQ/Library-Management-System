import pytest
from src.repositories.room_repo import RoomRepo


def test_get_all_rooms():
    repo = RoomRepo()
    rooms = repo.get_all()

    assert rooms is not None
    assert isinstance(rooms, list)
    assert len(rooms) > 0


def test_get_room_by_id_found():
    repo = RoomRepo()
    room = repo.get_by_id(1)

    assert room is not None
    assert room["id"] == 1
    assert "name" in room


def test_get_room_by_id_not_found():
    repo = RoomRepo()
    room = repo.get_by_id(999)

    assert room is None


def test_add_room():
    repo = RoomRepo()
    new_room = {
        "id": 3,
        "name": "Conference Room",
        "capacity": 15,
        "available": True
    }

    repo.add_room(new_room)
    room = repo.get_by_id(3)

    assert room is not None
    assert room["name"] == "Conference Room"
