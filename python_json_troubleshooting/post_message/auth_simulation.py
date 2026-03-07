import json

def load_auth_response():
    with open('mock_auth_response.json', 'r') as file:
        response = json.load(file)
    return response

def main():
    auth_response = load_auth_response()
    if auth_response.get("status") == "success":
        print("Authentication successful.")
        print("User:", auth_response.get("user"))
        print("Token:", auth_response.get("token"))
    else:
        print("Authentication failed.")
        print("Response:", auth_response)

if __name__ == "__main__":
    main()