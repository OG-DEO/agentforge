import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RollbackManager:
    def run(self, cmd):
        result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip())
        return result.stdout.strip()

    def snapshot(self, message="AI safety snapshot"):
        self.run(["git", "add", "-A"])
        status = self.run(["git", "status", "--short"])
        if not status:
            return "No changes to snapshot."
        self.run(["git", "commit", "-m", message])
        return "Snapshot committed."

    def hard_reset(self):
        self.run(["git", "reset", "--hard", "HEAD"])
        return "Reset to HEAD."
