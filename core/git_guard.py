import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GitGuard:
    def _root(self, repo_root=None):
        return Path(repo_root).resolve() if repo_root else ROOT

    def status(self, repo_root=None):
        result = subprocess.run(
            ["git", "status", "--short"],
            cwd=self._root(repo_root),
            text=True,
            capture_output=True,
        )

        return result.stdout.strip()

    def require_clean_tree(self, repo_root=None):
        status = self.status(repo_root)

        if status:
            raise RuntimeError(
                "Working tree is not clean.\n\n"
                f"{status}"
            )

    def current_branch(self, repo_root=None):
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=self._root(repo_root),
            text=True,
            capture_output=True,
        )

        return result.stdout.strip()

    def require_not_main(self, repo_root=None):
        current = self.current_branch(repo_root)

        if current == "main":
            raise RuntimeError(
                "Blocked: cannot apply on main branch."
            )
