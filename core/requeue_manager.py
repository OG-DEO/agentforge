import json
import shutil
from pathlib import Path

from core.task_queue import TaskQueue

ROOT = Path(__file__).resolve().parents[1]
APPROVED = ROOT / "approvals" / "approved"


class RequeueManager:
    def __init__(self):
        self.queue = TaskQueue()

    def requeue(self, approval_file):
        path = Path(approval_file)

        data = json.loads(
            path.read_text(encoding="utf-8")
        )

        payload = data.get("payload", {})
        task = payload.get("task")

        if not task:
            raise RuntimeError(
                "Approval file missing task payload."
            )

        queued = self.queue.submit(task)

        archived = path.with_suffix(".processed.json")

        shutil.move(str(path), archived)

        return {
            "queued": str(queued),
            "archived": str(archived),
        }
