import shutil
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
WORKSPACES = ROOT / "workspaces"

WORKSPACES.mkdir(exist_ok=True)


class WorkspaceManager:
    def create(self, source_dir="core"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        source = ROOT / source_dir
        target = WORKSPACES / f"workspace_{timestamp}"

        shutil.copytree(source, target)

        return target
