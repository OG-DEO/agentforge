import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
APPROVALS = ROOT / "approvals"

APPROVALS.mkdir(exist_ok=True)


class ApprovalQueue:
    def submit(self, payload):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        task_id = payload.get("task", {}).get("id", "unknown")
        path = APPROVALS / f"{timestamp}_{task_id}_approval.json"

        record = {
            "status": "pending",
            "created_at": timestamp,
            "payload": payload,
        }

        path.write_text(json.dumps(record, indent=2), encoding="utf-8")
        return path

    def list_pending(self):
        items = []

        for path in sorted(APPROVALS.glob("*_approval.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("status") == "pending":
                items.append({"path": str(path), "data": data})

        return items
