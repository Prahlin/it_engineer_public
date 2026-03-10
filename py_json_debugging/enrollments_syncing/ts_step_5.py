import requests

# Source JSON data from GitHub raw link
json_url = (
    "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/python_json_debugging/enrollments_syncing/enrollment_sync_status.json"
)

# Retrieve updated roster status
response = requests.get(json_url)

# Debugging: Print the raw response to see what we received
print("Debug: Raw response text:")
print(response.text)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON data only if the response is valid
    updated_status = response.json()

    # Debug: Check the updated status payload
    print("Debug: Updated LTI Response Payload:")
    print(updated_status)

    # Confirm the status
    if updated_status.get("status") == "synced":
        print(
            f"Debug: Club roster sync confirmed for "
            f"{updated_status['club']}. Members updated: "
            f"{updated_status['updated_members']}."
        )
    else:
        print(f"Sync issue: Status is {updated_status.get('status')}")
        print(
            "Debug: Roster sync did not succeed, "
            "further investigation needed."
        )
else:
    print(f"Failed to retrieve data: HTTP {response.status_code}")