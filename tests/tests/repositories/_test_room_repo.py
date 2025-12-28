from src.repositories.room_repo import RoomRepo


def test_singleton_instance():
    repo1 = RoomRepo()
    repo2 = RoomRepo()

    assert repo1 is repo2


def test_rooms_data_is_not_empty():
    repo = RoomRepo()
    rooms = repo.get_all()

    assert len(rooms) >= 2


def test_add_room_increases_count():
    repo = RoomRepo()
    initial_count = len(repo.get_all())

    repo.add_room({
        "id": 99,
        "name": "Test Room",
        "capacity": 5,
        "available": True
    })

    assert len(repo.get_all()) == initial_count + 1


def test_get_by_id_returns_correct_room():
    repo = RoomRepo()
    room = repo.get_by_id(1)

    assert room["id"] == 1
    assert room["name"] == "Reading Room"


def test_get_by_id_returns_none_for_invalid_id():
    repo = RoomRepo()

    assert repo.get_by_id(-1) is None
    assert repo.get_by_id(9999) is None
