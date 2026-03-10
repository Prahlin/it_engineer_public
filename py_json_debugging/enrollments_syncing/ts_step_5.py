import requests

# Source JSON data from GitHub raw link (updated roster or results)
json_url = (
    "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/python_json_debugging/enrollments_syncing/enrollment_sync_status.json"
)

# Retrieve updated roster status
response = requests.get(json_url)
updated_status = response.json()

# Debug: Check the updated status payload
print("Debug: Updated LTI Response Payload:")
print(updated_status)

# Confirm the status
if updated_status.get("status") == "synced":
    print(f"Debug: Club roster sync confirmed for {updated_status['club']}. Members updated: {updated_status['updated_members']}.")
    # Additional logic: Validate that roster matches expectations (e.g., compare against a known list)
else:
    print(f"Sync issue: Status is {updated_status.get('status')}")
    # Debug: Log any errors if the update failed
    print("Debug: Roster sync did not succeed, further investigation needed.")