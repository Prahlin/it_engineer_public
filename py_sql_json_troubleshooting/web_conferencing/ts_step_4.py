import requests

def fetch_permissions():
    url = "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/py_sql_json_troubleshooting/web_conferencing/permissions.json"  # Example endpoint for permissions
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def validate_access(data, student_id, course_id):
    for permission in data:
        if permission['student_id'] == student_id and permission['course_id'] == course_id:
            return permission['role']  # Return the role of the student
    return None  # No match found

if __name__ == "__main__":
    student_id = "student_123"  # Example student
    course_id = "course_101"  # Example course

    permissions = fetch_permissions()

    print("Step 4: Verify Access Permissions")
    role = validate_access(permissions, student_id, course_id)

    if role:
        print(f"Student {student_id} has role {role} for course {course_id}.")
    else:
        print(f"Error: No access permission found for student {student_id} in course {course_id}.")