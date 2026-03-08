import requests

def fetch_conferences(course_id):
    url = f"https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/python_sql_troubleshooting/conference_session.json"  # Replace with real endpoint
    response = requests.get(url)
    response.raise_for_status()  # Ensure we got a 200 OK

    data = response.json()
    return data

def validate_session(data, expected_course_id, expected_conference_id):
    for session in data:
        if (session['course_id'] == expected_course_id and
            session['conference_id'] == expected_conference_id):
            return session  # Session found
    return None  # Session not found

if __name__ == "__main__":
    course_id = "course_101"  # The course we're troubleshooting
    data = fetch_conferences(course_id)

    print("Step 2: Verify API Response")
    session = validate_session(data, expected_course_id="course_101", expected_conference_id="conf_001")

    if session:
        print("Session found:")
        print("Course ID:", session["course_id"])
        print("Conference ID:", session["conference_id"])
        print("Session Name:", session["session_name"])
        print("Status:", session["status"])
    else:
        print("Error: Session not found in API response.")