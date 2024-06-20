# Calender_system

A calendar system to schedule meetings, check for room and participant availability, and avoid scheduling conflicts. The system includes a backend API built with Flask and SQLAlchemy, and try to create simple UI using Streamlit.

## Requirements

1. **Python Packages**

   Ensure you have Python 3.10+ installed. Install the required packages using `requirements.txt`.

   ```bash
   pip install -r requirements.txt

2. Database Setup

  Ensure you have MySQL installed and running. Create a database named calendar_db.

  CREATE DATABASE calendar_db;

3. Update your config.py with the correct database credentials.

  class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost/calendar_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

Steps to Run
  1. Run Seeder Script
  Seed the users and rooms tables with initial data.

  python run_seeder_file.py
  
  2. Run the Flask Application
  Start the Flask application on port 8000.

  python app.py

  3.  Schedule Meeting
    POST /schedule_meeting
    Content-Type: application/json
    {
        "title": "Meeting Title",
        "start_time": "YYYY-MM-DD HH:MM:SS",
        "end_time": "YYYY-MM-DD HH:MM:SS",
        "room_id": room_id,
        "participants": [user_id1, user_id2, ...]
    }
example :
curl --location 'http://127.0.0.1:8000///schedule_meeting' \
--header 'Content-Type: application/json' \
--data '{
    "title":"UI DIscussion",
    "start_time" :"2024-06-23 10:00:00",
    "end_time" : "2024-06-23 11:00:00",
    "room_id" : 7,
    "participants" : [1,2]
}'

   4. For run streamlit app :
      streamlit run streamlit_app.py



