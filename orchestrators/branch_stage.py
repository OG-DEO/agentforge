from core.task_branch_manager import TaskBranchManager


class BranchStage:
    def __init__(self):
        self.manager = TaskBranchManager()

    def run(self, task):
        branch = self.manager.create_for_task(task)

        return {
            "branch": branch
        }
