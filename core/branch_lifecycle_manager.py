from core.git_branch_manager import GitBranchManager


class BranchLifecycleManager:
    def __init__(self, git=None):
        self.git = git or GitBranchManager()

    def inspect(self, base="main", stale_days=14):
        current = self.git.current_branch()
        branches = self.git.list_branches()
        merged = self.git.merged_branches(base=base)
        stale = self.git.stale_branches(older_than_days=stale_days)

        protected = {base, current}

        cleanup_candidates = [
            branch for branch in merged
            if branch not in protected
        ]

        return {
            "base": base,
            "current": current,
            "branch_count": len(branches),
            "branches": branches,
            "merged": merged,
            "stale": stale,
            "cleanup_candidates": cleanup_candidates,
        }
