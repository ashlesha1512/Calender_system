from flask import Blueprint

meeting_blueprint = Blueprint('meeting', __name__)

from . import meeting_api
