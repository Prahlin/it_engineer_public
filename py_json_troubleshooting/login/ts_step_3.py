import json
from login_sample_submission import run_login_step_3


def main():
    step = run_login_step_3()

    print("=== TS Step 3 ===")
    print(step.get("description", ""))
    print("Status code:", step.get("status_code"))
    print("Account status check:")
    print(json.dumps(step.get("account_status_check", {}), indent=2))


if __name__ == "__main__":
    main()