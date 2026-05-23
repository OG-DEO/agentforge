from core.task_branch_manager import TaskBranchManager
from core.branch_status_index import BranchStatusIndex


class BranchStage:
    def __init__(self):
        self.manager = TaskBranchManager()
        self.status_index = BranchStatusIndex()

    def run(self, task):
        branch = self.manager.create_for_task(task)

        self.status_index.set_status(
            branch,
            "executing",
            {
                "task_id": task.get("id", "unknown"),
                "stage": "branch_created",
            },
        )

        return {
            "branch": branch
        }
