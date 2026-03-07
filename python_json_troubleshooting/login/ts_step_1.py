import json
from login_sample_submission import run_login_step_1


def main():
    step = run_login_step_1()

    print("=== TS Step 1 ===")
    print(step.get("description", ""))
    print("Status code:", step.get("status_code"))
    print("LMS login service check:")
    print(json.dumps(step.get("login_service_check", {}), indent=2))


if __name__ == "__main__":
    main()