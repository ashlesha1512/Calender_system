from database.db import db

class Meeting(db.Model):
    __tablename__ = 'meetings'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=True)
    room = db.relationship('Room', backref=db.backref('meetings', lazy=True))

class MeetingParticipant(db.Model):
    __tablename__ = 'meeting_participants'
    meeting_id = db.Column(db.Integer, db.ForeignKey('meetings.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    user = db.relationship('User', backref=db.backref('meeting_participants', lazy=True))
    meeting = db.relationship('Meeting', backref=db.backref('participants', lazy=True))
