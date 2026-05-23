import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "model_backend.json"


def main():
    if not CONFIG.exists():
        print("Model backend config missing.")
        return

    data = json.loads(CONFIG.read_text(encoding="utf-8"))

    print("\n=== MODEL BACKEND STATUS ===")
    print(f"Backend: {data.get('backend')}")
    print(f"Enabled: {data.get('enabled')}")
    print(f"Base URL: {data.get('base_url')}")
    print(f"Model: {data.get('model')}")
    print(f"Notes: {data.get('notes')}")

    if not data.get("enabled"):
        print("\nStatus: DISABLED - safe planning mode only.")
    else:
        print("\nStatus: ENABLED - local model calls may be allowed.")


if __name__ == "__main__":
    main()
