from flask import Flask
from database.db import db
from config import Config
from flask_cors import CORS
from models.user import User
from models.room import Room
from routes.routes import register_blueprint

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app,resources={r"/*":{"origins":"*","allow_headers":"*","expose_headers":"*"}})
    app.config.from_object('config.Config')

    db.init_app(app)
    with app.app_context():
        db.create_all()

        # if not User.query.first():
        #     users = [
        #         User(name='Aditi'),
        #         User(name='Abhi'),
        #         User(name='Neha'),
        #         User(name='Alex')
        #     ]
        #     db.session.bulk_save_objects(users)
        #     db.session.commit()

        # if not Room.query.first():
        #     rooms = [
        #         Room(name='Conference Room A'),
        #         Room(name='Conference Room B'),
        #         Room(name='Meeting Room 1'),
        #         Room(name='Meeting Room 2'),
        #         Room(name='Meeting romm 3')
        #     ]
        #     db.session.bulk_save_objects(rooms)
        #     db.session.commit()

    register_blueprint(app)
    


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,port=8000)
