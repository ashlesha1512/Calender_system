from datetime import datetime
from sqlite3 import IntegrityError

from sqlalchemy import and_, or_
from database.db import db
from models.meeting import Meeting, MeetingParticipant
from models.room import Room

def is_room_available(room_id, start_time, end_time):
    conflicts = Meeting.query.filter(
        Meeting.room_id == room_id,
        db.or_(
            db.and_(Meeting.start_time <= start_time, Meeting.end_time > start_time),
            db.and_(Meeting.start_time < end_time, Meeting.end_time >= end_time)
        )
    ).all()
    return not conflicts

def are_participants_available(participants, start_time, end_time, exclude_meeting_id=None):
    unavailable_participants = []
    for user_id in participants:
        query = db.session.query(Meeting).join(MeetingParticipant).filter(
            MeetingParticipant.user_id == user_id,
            db.or_(
                db.and_(Meeting.start_time <= start_time, Meeting.end_time > start_time),
                db.and_(Meeting.start_time < end_time, Meeting.end_time >= end_time)
            )
        )
        if exclude_meeting_id:
            query = query.filter(Meeting.id != exclude_meeting_id)
        conflicts = query.all()
        if conflicts:
            unavailable_participants.append(user_id)
    return unavailable_participants



def is_room_available(room_id, start_time, end_time):
    conflicts = Meeting.query.filter(
        Meeting.room_id == room_id,
        or_(
            and_(Meeting.start_time <= start_time, Meeting.end_time > start_time),
            and_(Meeting.start_time < end_time, Meeting.end_time >= end_time)
        )
    ).all()
    return not conflicts

def are_participants_available(participants, start_time, end_time, exclude_meeting_id=None):
    unavailable_participants = []
    for user_id in participants:
        query = Meeting.query.join(MeetingParticipant).filter(
            MeetingParticipant.user_id == user_id,
            or_(
                and_(Meeting.start_time <= start_time, Meeting.end_time > start_time),
                and_(Meeting.start_time < end_time, Meeting.end_time >= end_time)
            )
        )
        if exclude_meeting_id:
            query = query.filter(Meeting.id != exclude_meeting_id)

        conflicts = query.all()
        if conflicts:
            unavailable_participants.append(user_id)
    return unavailable_participants

def schedule_meeting(title, start_time, end_time, room_id, participants):
    # Check if the room is available
    if not is_room_available(room_id, start_time, end_time):
        return {'error': 'Room is not available at the requested time.'}, 200
    
    # Check if participants are available
    unavailable_participants = are_participants_available(participants, start_time, end_time)
    if unavailable_participants:
        return {'error': 'One or more participants are not available at the requested time.', 'conflicts': unavailable_participants}, 200
    
    # Create a new meeting
    meeting = Meeting(title=title, start_time=start_time, end_time=end_time, room_id=room_id)
    db.session.add(meeting)
    db.session.commit()
    
    # Add participants to the meeting
    try:
        for user_id in participants:
            participant = MeetingParticipant(meeting_id=meeting.id, user_id=user_id)
            db.session.add(participant)
        db.session.commit()
        return {'message': 'Meeting is successfully scheduled.', 'meeting_id': meeting.id}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500