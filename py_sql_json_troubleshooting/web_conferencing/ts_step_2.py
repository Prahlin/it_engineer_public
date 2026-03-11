import requests

def fetch_conference(course_id):
    url = "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/py_sql_json_troubleshooting/web_conferencing/conference_session.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def validate_session(data, expected_course_id, expected_conference_id):
    if (data['course_id'] == expected_course_id and data['conference_id'] == expected_conference_id):
        return data  # Session matches
    return None  # No match

if __name__ == "__main__":
    course_id = "course_101"
    data = fetch_conference(course_id)

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