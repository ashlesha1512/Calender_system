from seeders.seed_users import seedUsers
from seeders.seed_rooms import seedRooms
from utils.db_utils import create_session


def seed():
    session = create_session()
    seedUsers(session)
    seedRooms(session)