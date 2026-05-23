import subprocess
from datetime import datetime, timezone
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
        return self.run(["git", "branch", "--show-current"])

    def create_ai_branch(self, prefix="ai"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        branch = f"{prefix}/{timestamp}"
        self.run(["git", "checkout", "-b", branch])
        return branch

    def checkout(self, branch):
        self.run(["git", "checkout", branch])

    def list_branches(self):
        output = self.run(["git", "branch", "--format=%(refname:short)"])
        return [line.strip() for line in output.splitlines() if line.strip()]

    def branch_last_commit_iso(self, branch):
        return self.run(["git", "log", "-1", "--format=%cI", branch])

    def branch_age_days(self, branch):
        iso = self.branch_last_commit_iso(branch)
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        return (now - dt).days

    def merged_branches(self, base="main"):
        output = self.run(["git", "branch", "--merged", base, "--format=%(refname:short)"])
        return [b.strip() for b in output.splitlines() if b.strip() and b.strip() != base]

    def stale_branches(self, older_than_days=14, prefixes=("task/", "ai/")):
        stale = []
        for branch in self.list_branches():
            if not branch.startswith(prefixes):
                continue
            age = self.branch_age_days(branch)
            if age >= older_than_days:
                stale.append({"branch": branch, "age_days": age})
        return stale

    def delete_branch(self, branch, force=False):
        flag = "-D" if force else "-d"
        return self.run(["git", "branch", flag, branch])
