import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]

LOG_DIR = ROOT / "logs"

LOG_DIR.mkdir(exist_ok=True)


class AuditLogger:
    def __init__(self, name="system"):
        self.name = name

        self.path = (
            LOG_DIR /
            f"{name}.jsonl"
        )

    def log(self, event_type, payload):
        record = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "payload": payload,
        }

        with open(
            self.path,
            "a",
            encoding="utf-8"
        ) as f:
            f.write(
                json.dumps(record) + "\n"
            )

        return record
