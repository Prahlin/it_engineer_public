import requests

# Source JSON data from GitHub raw link
json_url = (
    "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/python_json_debugging/user_permissions.json"
)

# Retrieve JSON data
response = requests.get(json_url)
user_data = response.json()

# Check user role
if user_data.get("role") in ["admin", "instructor"]:
    print("Permission granted: user can update enrollments.")
    # Here, you would proceed with the logic to update the roster
else:
    print("Permission denied: user does not have access to update enrollments.")