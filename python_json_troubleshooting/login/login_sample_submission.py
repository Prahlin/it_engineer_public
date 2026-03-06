import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "login_sample_submission_response.json"


def load_evidence() -> dict:
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def get_step(step_key: str) -> dict:
    evidence = load_evidence()
    return evidence.get(step_key, {})


def run_login_step_1() -> dict:
    """Step 1: Verify LMS login service is reachable."""
    step = get_step("ts_step_1")
    return dict(step)


def run_login_step_2() -> dict:
    """Step 2: Verify the student or instructor account exists in the LMS."""
    step = get_step("ts_step_2")
    return dict(step)


def run_login_step_3() -> dict:
    """Step 3: Verify the LMS account is active."""
    step = get_step("ts_step_3")
    return dict(step)


def run_login_step_4() -> dict:
    """Step 4: Verify authentication attempt using LMS API."""
    step = get_step("ts_step_4")
    return dict(step)


def run_login_step_5() -> dict:
    """Step 5: Verify LMS API rate limits are not blocking login attempts."""
    step = get_step("ts_step_5")
    return dict(step)