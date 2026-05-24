import json
from pathlib import Path
from datetime import datetime

from core.branch_state_machine import BranchStateMachine

ROOT = Path(__file__).resolve().parents[1]
STATE_DIR = ROOT / "state"
STATE_DIR.mkdir(exist_ok=True)

STATUS_PATH = STATE_DIR / "branch_status.json"


class BranchStatusIndex:
    def __init__(self):
        self.sm = BranchStateMachine()

    def load(self):
        if not STATUS_PATH.exists():
            return {}
        return json.loads(STATUS_PATH.read_text(encoding="utf-8"))

    def save(self, data):
        STATUS_PATH.write_text(
            json.dumps(data, indent=2),
            encoding="utf-8"
        )

    def set_status(self, branch, status, metadata=None):
        data = self.load()

        current = data.get(branch, {}).get("status")

        # enforce transition rules
        self.sm.enforce(current, status)

        data[branch] = {
            "status": status,
            "updated_at": datetime.now().isoformat(),
            "metadata": metadata or {},
        }

        self.save(data)
        return data[branch]

    def get_status(self, branch):
        return self.load().get(branch)

    def all(self):
        return self.load()
