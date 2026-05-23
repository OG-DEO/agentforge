import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

APPROVALS = ROOT / "approvals"
APPROVED = APPROVALS / "approved"
REJECTED = APPROVALS / "rejected"

APPROVED.mkdir(exist_ok=True)
REJECTED.mkdir(exist_ok=True)


class ApprovalResolver:
    def approve(self, approval_file):
        path = Path(approval_file)

        data = json.loads(
            path.read_text(encoding="utf-8")
        )

        data["status"] = "approved"

        path.write_text(
            json.dumps(data, indent=2),
            encoding="utf-8"
        )

        target = APPROVED / path.name

        shutil.move(str(path), target)

        return target

    def reject(self, approval_file):
        path = Path(approval_file)

        data = json.loads(
            path.read_text(encoding="utf-8")
        )

        data["status"] = "rejected"

        path.write_text(
            json.dumps(data, indent=2),
            encoding="utf-8"
        )

        target = REJECTED / path.name

        shutil.move(str(path), target)

        return target
