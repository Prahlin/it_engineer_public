import requests

def fetch_session_data():
    url = "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/python_sql_troubleshooting/conference_session.json"  # Example URL
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    return response.json()

data = fetch_session_data()

print("Step 1: Confirm Conference Session Exists")
print("Course ID:", data["course_id"])
print("Conference ID:", data["conference_id"])
print("Session Name:", data["session_name"])
print("Status:", data["status"])

if data["status"] == "active":
    print("Result: Conference session is active.")
else:
    print("Result: Conference session is not active.")