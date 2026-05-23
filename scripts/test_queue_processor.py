from core.task_queue import TaskQueue

queue = TaskQueue()

queue.submit({
    "id": "task-0009",
    "title": "Autonomous queue processor test",
    "risk": "low",
    "requires_approval": False,
    "objective": "Generate and review a safe planning task."
})

print("Test task queued.")
