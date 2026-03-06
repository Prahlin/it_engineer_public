import json
from login_sample_submission import run_login_step_4


def main():
    step = run_login_step_4()

    print("=== TS Step 4 ===")
    print(step.get("description", ""))
    print("Status code:", step.get("status_code"))
    print("Authentication attempt result:")
    print(json.dumps(step.get("auth_attempt", {}), indent=2))


if __name__ == "__main__":
    main()