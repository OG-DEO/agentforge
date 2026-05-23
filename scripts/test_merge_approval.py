from core.merge_approval_manager import (
    MergeApprovalManager
)

manager = MergeApprovalManager()

path = manager.submit({
    "task_id": "task-0014",
    "branch": "task/task-0014/demo",
    "summary": "Safe autonomous patch completed.",
    "auto_applied": True,
})

print("\n=== MERGE APPROVAL CREATED ===\n")
print(path)

print("\n=== PENDING MERGE REVIEWS ===\n")

for item in manager.pending():
    print(item)
