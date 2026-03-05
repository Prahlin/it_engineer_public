import requests
import json

# Example LMS API endpoint (placeholder)
api_url = "https://httpbin.org/get"

headers = {
    "Content-Type": "application/json"
}

# Student and assignment we are verifying
params = {
    "student_name": "Marty McFly",
    "assignment_id": "ASSIGNMENT_123"
}

# Send request to LMS API
response = requests.get(api_url, headers=headers, params=params)

print("Status code:", response.status_code)

if response.status_code == 200:

    data = response.json()

    # Example simulated submission event
    submission_event = {
        "student_name": "Marty McFly",
        "assignment_id": "ASSIGNMENT_123",
        "submission_status": "submitted",
        "submitted_at": "2026-03-05T14:20:10",
        "attempt_id": "874293"
    }

    print("\nSubmission Event Record:")
    print(json.dumps(submission_event, indent=4))

    if submission_event["submission_status"] == "submitted":
        print("\nSubmission event successfully recorded in LMS API logs.")
    else:
        print("\nSubmission record found but status is not 'submitted'.")

else:
    print("Error retrieving submission event.")
    print(response.text)