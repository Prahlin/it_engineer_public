import requests

# Source JSON data from GitHub raw link
json_url = (
    "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/python_json_debugging/enrollments_syncing/enrollment_debug_status.json"
)

# Retrieve JSON data
response = requests.get(json_url)

# Debugging: Print the raw response to see what we received
print("Debug: Raw response text:")
print(response.text)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON data only if the response is valid
    status_data = response.json()

    # Debugging: Check the raw payload
    print("Debug: Full LTI Response Payload:")
    print(status_data)

    # Check if the status is synced
    if status_data.get("status") == "synced":
        # Debug: Confirm what club we received
        print(f"Debug: Club name received: {status_data['club']}")

        # Debug: Confirm number of updated members
        print(
            f"Debug: Members updated: "
            f"{status_data['updated_members']}"
        )

        # Additional logic: Check if roster update function is called
        print(
            "Debug: Logic verified—ready to update roster "
            "(if implemented)."
        )
    else:
        print(f"Sync issue: Status is {status_data.get('status')}")
        print(
            "Debug: No update performed due to failed "
            "sync status."
        )
else:
    print(f"Failed to retrieve data: HTTP {response.status_code}")