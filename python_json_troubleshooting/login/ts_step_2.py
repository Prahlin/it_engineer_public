import json
from login_sample_submission import run_login_step_2


def main():
    step = run_login_step_2()

    print("=== TS Step 2 ===")
    print(step.get("description", ""))
    print("Status code:", step.get("status_code"))
    print("LMS user lookup result:")
    print(json.dumps(step.get("user_lookup", {}), indent=2))


if __name__ == "__main__":
    main()