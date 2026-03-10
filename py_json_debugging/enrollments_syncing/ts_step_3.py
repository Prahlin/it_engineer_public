import requests

# Source JSON data from GitHub raw link
json_url = (
    "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/python_json_debugging/enrollments_syncing/enrollment_debug_status.json"
)

# Retrieve JSON data
response = requests.get(json_url)
status_data = response.json()

# Debugging: Check the raw payload
print("Debug: Full LTI Response Payload:")
print(status_data)

# Check if the status is synced
if status_data.get("status") == "synced":
    # Debug: Confirm what club we received
    print(f"Debug: Club name received: {status_data['club']}")
    # Debug: Confirm number of updated members
    print(f"Debug: Members updated: {status_data['updated_members']}")
    
    # Additional logic: Check if roster update function is called
    print("Debug: Logic verified—ready to update roster (if implemented).")
else:
    print(f"Sync issue: Status is {status_data.get('status')}")
    # Debug: Log any additional errors or unexpected statuses
    print("Debug: No update performed due to failed sync status.")