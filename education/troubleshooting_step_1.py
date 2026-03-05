import requests

# Test API endpoint that echoes query parameters
api_url = "https://httpbin.org/get"

headers = {
    "Content-Type": "application/json"
}

# Student and assignment we want to verify
params = {
    "student_name": "Marty McFly",
    "assignment_id": "ASSIGNMENT_1"
}

# Send GET request
response = requests.get(api_url, headers=headers, params=params)

# Print status code
print("Status code:", response.status_code)

# Show only the parameters returned by the server
if response.status_code == 200:
    data = response.json()
    print("Student:", data["args"].get("student_name"))
    print("Assignment:", data["args"].get("assignment_id"))
else:
    print("Error:", response.text)