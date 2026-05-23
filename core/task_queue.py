import json
import shutil
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "queue"
DONE = QUEUE / "done"
FAILED = QUEUE / "failed"

QUEUE.mkdir(exist_ok=True)
DONE.mkdir(exist_ok=True)
FAILED.mkdir(exist_ok=True)


class TaskQueue:
    def submit(self, task):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        task_id = task.get("id", "unknown")
        path = QUEUE / f"{timestamp}_{task_id}.json"
        path.write_text(json.dumps(task, indent=2), encoding="utf-8")
        return path

    def pending(self):
        return sorted(
            p for p in QUEUE.glob("*.json")
            if p.is_file()
        )

    def mark_done(self, path):
        shutil.move(str(path), DONE / path.name)

    def mark_failed(self, path):
        shutil.move(str(path), FAILED / path.name)
