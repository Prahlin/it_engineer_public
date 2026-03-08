import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "sample_submission_response.json"

def main():
    evidence = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    step = evidence["troubleshooting_step_3"]

    print("=== Troubleshooting Step 3 ===")
    print(step.get("description", ""))
    print("Status code:", step.get("status_code"))
    print("Gradebook record:")
    print(json.dumps(step.get("gradebook_record", {}), indent=2))

if __name__ == "__main__":
    main()