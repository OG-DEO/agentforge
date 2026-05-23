import json
from pathlib import Path
from datetime import datetime

from core.git_branch_manager import GitBranchManager
from core.audit_logger import AuditLogger
from core.branch_status_index import BranchStatusIndex

ROOT = Path(__file__).resolve().parents[1]

ARCHIVE_DIR = ROOT / "branch_archive"

ARCHIVE_DIR.mkdir(exist_ok=True)


class BranchArchiveManager:
    def __init__(
        self,
        git=None,
        audit=None,
    ):
        self.git = git or GitBranchManager()

        self.audit = (
            audit or
            AuditLogger("branch_archive")
        )

        self.status_index = BranchStatusIndex()

    def archive(
        self,
        branch,
        reason="rejected",
    ):
        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        metadata = {
            "branch": branch,
            "reason": reason,
            "timestamp": timestamp,
        }

        path = (
            ARCHIVE_DIR /
            f"{timestamp}_{branch.replace('/', '_')}.json"
        )

        path.write_text(
            json.dumps(metadata, indent=2),
            encoding="utf-8",
        )

        self.audit.log(
            "branch_archived",
            metadata,
        )

	        self.status_index.set_status(
            branch,
            "archived",
            {
                "reason": reason,
                "archive_file": str(path),
            },
        )

        return metadata
