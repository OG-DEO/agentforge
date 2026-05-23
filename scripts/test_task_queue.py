from core.task_queue import TaskQueue

queue = TaskQueue()

task = {
    "id": "task-0008",
    "title": "Queue smoke test",
    "risk": "low",
    "requires_approval": False,
}

path = queue.submit(task)

print("\n=== TASK SUBMITTED ===\n")
print(path)

print("\n=== PENDING TASKS ===\n")
for item in queue.pending():
    print(item)
