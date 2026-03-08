import requests

def fetch_enrollments():
    url = "https://raw.githubusercontent.com/Prahlin/it_engineer_public/main/python_sql_troubleshooting/enrollments.json"  # Raw endpoint for enrollments
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    return response.json()

def validate_enrollment(data, student_id, course_id):
    for enrollment in data:
        if enrollment['student_id'] == student_id and enrollment['course_id'] == course_id:
            return enrollment['enrollment_status']  # Return status (e.g., active, inactive)
    return None  # No match found

if __name__ == "__main__":
    student_id = "student_123"  # Example student
    course_id = "course_101"  # Example course

    enrollments = fetch_enrollments()

    print("Step 3: Check Student Enrollment")
    status = validate_enrollment(enrollments, student_id, course_id)

    if status:
        print(f"Student {student_id} enrollment status in course {course_id}: {status}")
    else:
        print(f"Error: Student {student_id} not found in course {course_id}.")