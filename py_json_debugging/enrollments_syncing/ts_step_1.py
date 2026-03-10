import requests

# Source JSON data from GitHub raw link
json_url = "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/python_json_debugging/enrollments_syncing/club_enrollment_lti.json"

# Retrieve JSON data
response = requests.get(json_url)
data = response.json()

# Validate LTI launch
if data.get("lti_launch"):
    print(f"LTI launch confirmed for {data['club']}.")

    # Verify club name matches expectations
    if data.get("club") == "Robotics Club":
        print("Robotics Club verified.")

        # Perform API POST request for enrollment
        api_url = "https://httpbin.org/post"
        post_response = requests.post(api_url, json=data)

        if post_response.status_code == 200:
            print("Enrollment successful.")
        else:
            print(f"Enrollment failed: {post_response.status_code}")
    else:
        print("Club name mismatch.")
else:
    print("LTI launch failed.")