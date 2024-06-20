# seeders/seed_users.py
from models.user import User

def seedUsers(session):
    if not session.query(User).first():
        users = [
            User(name='Aditi'),
            User(name='Abhi'),
            User(name='Neha'),
            User(name='Alex')
        ]
        session.bulk_save_objects(users)
        session.commit()
        print("Users table seeded successfully.")
    else:
        print("Users table already seeded.")
