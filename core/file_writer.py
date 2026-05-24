from pathlib import Path
from datetime import datetime
import shutil

from core.git_guard import GitGuard
from core.git_branch_manager import GitBranchManager
from core.path_guard import PathGuard

ROOT = Path(__file__).resolve().parents[1]
BACKUP_DIR = ROOT / "workspaces" / "backups"

BACKUP_DIR.mkdir(parents=True, exist_ok=True)


class ControlledFileWriter:
    def __init__(self):
        self.git = GitGuard()
        self.branch = GitBranchManager()
        self.paths = PathGuard()

    def backup_file(self, target):
        if not target.exists():
            return None

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        backup = BACKUP_DIR / f"{timestamp}_{target.name}"

        shutil.copy2(target, backup)

        return backup

    def write_text(self, path, content, require_clean=True):
        current = self.branch.current_branch()

        if current == "main":
            raise RuntimeError(
                "Blocked: cannot write on main branch."
            )

        target = Path(path).resolve()

        self.paths.validate(str(target))

        if require_clean:
            self.git.require_clean_tree()

        backup = self.backup_file(target)

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

        return {
            "target": str(target),
            "backup": str(backup) if backup else None,
        }
