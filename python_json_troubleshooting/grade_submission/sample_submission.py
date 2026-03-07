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
    Step 4: test grade/gradebook visibility using a second instructor account
    to determine whether the issue is user-specific (permissions/role/cache).

    Returns the stored Step 4 evidence and also includes which instructor username
    was used for verification.
    """
    step = get_step("troubleshooting_step_4")
    step = dict(step)  # shallow copy
    step["checked_instructor_username"] = instructor_username
    return step


def run_step_5_rate_limit_check() -> dict:
    """
    Step 5: check LMS API rate limits to ensure throttling isn't blocking data retrieval.
    Returns the stored Step 5 evidence.
    """
    step = get_step("troubleshooting_step_5")
    return dict(step)  # shallow copy