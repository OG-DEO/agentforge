import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GitBranchManager:
    def run(self, cmd):
        result = subprocess.run(
            cmd,
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip())

        return result.stdout.strip()

    def current_branch(self):
        return self.run(
            ["git", "branch", "--show-current"]
        )

    def create_ai_branch(self, prefix="ai"):
        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        branch = f"{prefix}/{timestamp}"

        self.run(
            ["git", "checkout", "-b", branch]
        )

        return branch

    def checkout(self, branch):
        self.run(
            ["git", "checkout", branch]
        )

    def list_branches(self):
        output = self.run(["git", "branch"])

        return [
            line.strip()
            for line in output.splitlines()
        ]
