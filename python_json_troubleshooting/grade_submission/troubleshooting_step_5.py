import json

from sample_submission import run_step_5_rate_limit_check


def main():
    step = run_step_5_rate_limit_check()

    print("=== Troubleshooting Step 5 ===")
    print(step.get("description", ""))
    print("Status code:", step.get("status_code"))

    print("Rate limit check results:")
    print(json.dumps(step.get("rate_limit_check", {}), indent=2))


if __name__ == "__main__":
    main()