import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]

MERGE_QUEUE = ROOT / "merge_approvals"

MERGE_QUEUE.mkdir(exist_ok=True)


class MergeApprovalManager:
    def submit(self, payload):
        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        branch = payload.get(
            "branch",
            "unknown_branch"
        ).replace("/", "_")

        path = (
            MERGE_QUEUE /
            f"{timestamp}_{branch}_merge.json"
        )

        record = {
            "status": "pending_merge_review",
            "payload": payload,
        }

        path.write_text(
            json.dumps(record, indent=2),
            encoding="utf-8"
        )

        return path

    def pending(self):
        return sorted(
            MERGE_QUEUE.glob("*.json")
        )
