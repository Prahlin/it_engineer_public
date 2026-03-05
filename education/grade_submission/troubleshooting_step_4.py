import json

from sample_submission import run_step_4_check


def main():
    # “another instructor account” per step 4 description in the case
    instructor_username = "instructor_alt_account"

    step = run_step_4_check(instructor_username)

    print("=== Troubleshooting Step 4 ===")
    print(step.get("description", ""))
    print("Status code:", step.get("status_code"))

    print("Instructor used for verification:", step.get("checked_instructor_username"))

    print("User-specific check results:")
    print(json.dumps(step.get("instructor_visibility_check", {}), indent=2))


if __name__ == "__main__":
    main()