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

    print("\nAPI Response:")
    print(json.dumps(data, indent=4))

    # Example logic: check if gradebook fields exist
    if "grade_status" in data:
        print("\nGradebook record found.")
        print("Grade status:", data["grade_status"])
    else:
        print("\nNo gradebook record found in API response.")

else:
    print("Error retrieving gradebook record.")
    print(response.text)