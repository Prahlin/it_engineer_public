import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "sample_submission_response.json"


def load_evidence() -> dict:
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def get_step(step_key: str) -> dict:
    evidence = load_evidence()
    return evidence.get(step_key, {})


def run_step_4_check(instructor_username: str) -> dict:
    """
    Step 4 principle (per the case): test API calls with another instructor account
    to determine whether the issue is user-specific.

    This function returns the canned evidence from sample_submission_response.json
    and also echoes the instructor used for the check (so the step file can display it).
    """
    step = get_step("troubleshooting_step_4")
    # Add runtime context without changing the stored evidence structure too much
    step = dict(step)  # shallow copy
    step["checked_instructor_username"] = instructor_username
    return step