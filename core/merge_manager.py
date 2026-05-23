import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class MergeManager:
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

    def checkout(self, branch):
        return self.run(
            ["git", "checkout", branch]
        )

    def merge(self, source_branch):
        return self.run(
            ["git", "merge", source_branch]
        )
