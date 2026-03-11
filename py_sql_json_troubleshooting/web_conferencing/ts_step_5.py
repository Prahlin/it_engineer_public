import requests

def fetch_sync_logs():
    url = "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/py_sql_json_troubleshooting/web_conferencing/sync_logs.json"  # Replace with real raw URL once created
    response = requests.get(url)
    response.raise_for_status()  # Ensure request was successful
    return response.json()

def validate_sync(logs, session_id):
    for log in logs:
        if log['session_id'] == session_id and log['status'] == 'success':
            return True  # Sync was successful
    return False  # No successful sync found

if __name__ == "__main__":
    session_id = "conf_001"  # Example session ID

    logs = fetch_sync_logs()

    print("Step 5: Review Logs and Sync Status")
    if validate_sync(logs, session_id):
        print(f"Session {session_id} was successfully synced in the LMS.")
    else:
        print(f"Error: Session {session_id} sync failed or not logged.")