import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
PATCH_DIR = ROOT / "reports" / "patches"

PATCH_DIR.mkdir(parents=True, exist_ok=True)


class PatchWriter:
    def save_patch(self, task_id, payload):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        path = PATCH_DIR / f"{timestamp}_{task_id}_patch.json"

        path.write_text(
            json.dumps(payload, indent=2),
            encoding="utf-8"
        )

        return path
