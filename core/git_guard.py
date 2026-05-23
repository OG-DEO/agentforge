import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GitGuard:
    def status(self):
        result = subprocess.run(
            ["git", "status", "--short"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        return result.stdout.strip()

    def require_clean_tree(self):
        status = self.status()

        if status:
            raise RuntimeError(
                "Working tree is not clean.\n\n"
                f"{status}"
            )

    def current_branch(self):
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        return result.stdout.strip()
