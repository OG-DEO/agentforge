from core.task_queue import TaskQueue

queue = TaskQueue()

queue.submit({
    "id": "task-0012",
    "title": "Branch-integrated queue test",
    "risk": "low",
    "requires_approval": False,
    "objective": "Verify queue processor creates isolated task branches automatically."
})

print("Task queued.")
