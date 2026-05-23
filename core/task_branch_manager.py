from core.git_branch_manager import GitBranchManager


class TaskBranchManager:
    def __init__(self):
        self.git = GitBranchManager()

    def create_for_task(self, task):
        task_id = task.get("id", "unknown")

        safe_id = (
            task_id
            .replace(" ", "_")
            .replace("/", "_")
            .lower()
        )

        branch = self.git.create_ai_branch(
            prefix=f"task/{safe_id}"
        )

        return branch
