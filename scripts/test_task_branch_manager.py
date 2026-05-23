from core.task_branch_manager import TaskBranchManager

manager = TaskBranchManager()

task = {
    "id": "task-0011"
}

branch = manager.create_for_task(task)

print("\n=== TASK BRANCH CREATED ===\n")
print(branch)
