import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "model_backend.json"


def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


def main():
    if not CONFIG.exists():
        fail("config/model_backend.json missing")

    data = json.loads(CONFIG.read_text(encoding="utf-8"))

    backend = data.get("backend")
    enabled = data.get("enabled")
    base_url = str(data.get("base_url", "")).rstrip("/")

    print("=== LM STUDIO CONNECTION TEST ===")
    print(f"Backend: {backend}")
    print(f"Enabled: {enabled}")
    print(f"Base URL: {base_url}")

    if backend != "lm_studio":
        fail("backend is not lm_studio")

    if enabled:
        fail("backend is enabled; expected disabled for safe connector test")

    if not base_url:
        fail("base_url missing")

    models_url = f"{base_url}/models"
    print(f"Checking: {models_url}")

    request = urllib.request.Request(models_url, headers={"Accept": "application/json"})

    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            status = response.status
            body = response.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as e:
        print("Connection result: NOT REACHABLE")
        print(f"Reason: {e}")
        print("\nThis is OK if LM Studio server is not running yet.")
        sys.exit(0)

    print(f"HTTP status: {status}")

    try:
        payload = json.loads(body)
    except json.JSONDecodeError:
        print("Connection result: REACHABLE BUT NON-JSON RESPONSE")
        print(body[:500])
        sys.exit(1)

    models = payload.get("data", [])
    print(f"Connection result: REACHABLE")
    print(f"Models reported: {len(models)}")

    for item in models[:10]:
        print(f"- {item.get('id', 'unknown')}")

    if not models:
        print("\nLM Studio is reachable, but no loaded/available models were reported.")

    print("\nPASS: connector can reach LM Studio API without enabling model calls.")


if __name__ == "__main__":
    main()
