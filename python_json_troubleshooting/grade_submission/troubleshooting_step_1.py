import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "sample_submission_response.json"

def main():
    evidence = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    step = evidence["troubleshooting_step_1"]

    print("=== Troubleshooting Step 1 ===")
    print(step.get("description", ""))
    print("Status code:", step.get("status_code"))
    print("Request parameters:")
    print(json.dumps(step.get("request_parameters", {}), indent=2))

if __name__ == "__main__":
    main()