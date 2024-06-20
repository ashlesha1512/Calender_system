# streamlit_app.py
import streamlit as st
import requests
import json
from datetime import datetime

# Define API endpoint
API_URL = 'http://localhost:8000/schedule_meeting'  # Update with your actual API endpoint

# Helper function to call API
def schedule_meeting(title, start_time, end_time, room_id, participants):
    data = {
        'title': title,
        'start_time': start_time,
        'end_time': end_time,
        'room_id': room_id,
        'participants': participants
    }
    headers = {'Content-Type': 'application/json'}
    print(data)
    response = requests.post(API_URL, data=json.dumps(data), headers=headers)
    print(response)
    return response.json()

# Streamlit app code
def main():
    st.title('Meeting Scheduler')

    # Input fields
    title = st.text_input('Meeting Title')
    start_date = st.date_input('Start Date')
    start_time = st.time_input('Start Time')
    end_date = st.date_input('End Date')
    end_time = st.time_input('End Time')
    room_id = st.selectbox('Select Room ID', [6,7,8,9])  # Adjust room IDs based on your setup
    participants = st.multiselect('Select Participants', [6,7,8,9])  # Adjust participant IDs based on your setup

    # Button to schedule meeting
    if st.button('Schedule Meeting'):
        if title and start_date and start_time and end_date and end_time and room_id and participants:
            try:
                start_datetime = datetime.combine(start_date, start_time)
                end_datetime = datetime.combine(end_date, end_time)
                start_time_str = start_datetime.strftime('%Y-%m-%d %H:%M:%S')
                end_time_str = end_datetime.strftime('%Y-%m-%d %H:%M:%S')
                result = schedule_meeting(title, start_time_str, end_time_str, room_id, participants)
                if 'error' in result:
                    st.error(result['error'])
                else:
                    st.success(f"Meeting scheduled successfully with ID: {result['meeting_id']}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning('Please fill in all fields.')

if __name__ == '__main__':
    main()
