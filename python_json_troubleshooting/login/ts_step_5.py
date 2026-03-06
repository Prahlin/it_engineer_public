import json
from login_sample_submission import run_login_step_5


def main():
    step = run_login_step_5()

    print("=== TS Step 5 ===")
    print(step.get("description", ""))
    print("Status code:", step.get("status_code"))
    print("Rate limit check:")
    print(json.dumps(step.get("rate_limit_check", {}), indent=2))


if __name__ == "__main__":
    main()