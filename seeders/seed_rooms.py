# seeders/seed_rooms.py
from models.room import Room

def seedRooms(session):
    if not session.query(Room).first():
        rooms = [
            Room(name='Conference Room A'),
            Room(name='Conference Room B'),
            Room(name='Meeting Room 1'),
            Room(name='Meeting Room 2'),
            Room(name='Meeting Room 3')
        ]
        session.bulk_save_objects(rooms)
        session.commit()
        print("Rooms table seeded successfully.")
    else:
        print("Rooms table already seeded.")
