from flask import request, jsonify , Blueprint
from . import meeting_blueprint
from utils.scheduler import schedule_meeting
from database.db import db
from models.user import User
from models.room import Room
from datetime import datetime


meeting_api = Blueprint("meeting_apis",__name__)

'''@meeting_api.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    name = data['name']
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id})

@meeting_api.route('/add_room', methods=['POST'])
def add_room():
    data = request.json
    name = data['name']
    room = Room(name=name)
    db.session.add(room)
    db.session.commit()
    return jsonify({'id': room.id})'''

@meeting_api.route('/schedule_meeting', methods=['POST'])
def schedule():
    data = request.json
    title = data['title']
    start_time = datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M:%S')
    room_id = data['room_id']
    participants = data['participants']
    
    result, status = schedule_meeting(title, start_time, end_time, room_id, participants)
    return jsonify(result), status
