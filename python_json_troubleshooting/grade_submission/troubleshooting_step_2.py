import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "sample_submission_response.json"

def main():
    evidence = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    step = evidence["troubleshooting_step_2"]

    print("=== Troubleshooting Step 2 ===")
    print(step.get("description", ""))
    print("Status code:", step.get("status_code"))
    print("Submission event:")
    print(json.dumps(step.get("submission_event", {}), indent=2))

if __name__ == "__main__":
    main()