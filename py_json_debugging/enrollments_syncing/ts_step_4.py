import requests

# Source JSON data from GitHub raw link
json_url = (
    "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/python_json_debugging/enrollments_syncing/user_permissions.json"
)

# Retrieve JSON data
response = requests.get(json_url)

# Debugging: Print the raw response to see what we received
print("Debug: Raw response text:")
print(response.text)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON data only if the response is valid
    user_data = response.json()

    # Check user role
    if user_data.get("role") in ["admin", "instructor"]:
        print("Permission granted: user can update enrollments.")
    else:
        print(
            "Permission denied: user does not have access "
            "to update enrollments."
        )
else:
    print(f"Failed to retrieve data: HTTP {response.status_code}")