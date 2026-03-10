import requests

# Source JSON data from GitHub raw link
json_url = "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/python_json_debugging/enrollments_syncing/enrollment_sync_status.json"

# Retrieve JSON data
response = requests.get(json_url)
status_data = response.json()

# Check sync status
if status_data.get("status") == "synced":
    print(f"Enrollment sync confirmed for {status_data['club']}. Members updated: {status_data['updated_members']}.")
else:
    print(f"Sync issue: Status is {status_data.get('status')}.")