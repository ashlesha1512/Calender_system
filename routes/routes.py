from flask import Blueprint
from api.meeting_api import meeting_api

def register_blueprint(app):
    base = Blueprint('base',__name__)
    base.register_blueprint(meeting_api)
    app.register_blueprint(base)