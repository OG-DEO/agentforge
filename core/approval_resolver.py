import json
import shutil
from pathlib import Path

from core.audit_logger import AuditLogger
from core.branch_archive_manager import BranchArchiveManager

ROOT = Path(__file__).resolve().parents[1]

APPROVALS = ROOT / "approvals"
APPROVED = APPROVALS / "approved"
REJECTED = APPROVALS / "rejected"

APPROVED.mkdir(exist_ok=True)
REJECTED.mkdir(exist_ok=True)


class ApprovalResolver:
    def __init__(self):
        self.audit = AuditLogger("approval_resolver")
        self.archive = BranchArchiveManager()

    def approve(self, approval_file):
        path = Path(approval_file)
        data = json.loads(path.read_text(encoding="utf-8"))

        data["status"] = "approved"

        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

        target = APPROVED / path.name
        shutil.move(str(path), target)

        self.audit.log("approval_approved", {"file": str(target)})

        return target

    def reject(self, approval_file):
        path = Path(approval_file)
        data = json.loads(path.read_text(encoding="utf-8"))

        data["status"] = "rejected"

        payload = data.get("payload", {})
        branch = payload.get("branch")

        if branch:
            self.archive.archive(branch, reason="approval_rejected")

        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

        target = REJECTED / path.name
        shutil.move(str(path), target)

        self.audit.log(
            "approval_rejected",
            {
                "file": str(target),
                "branch": branch,
            },
        )

        return target
