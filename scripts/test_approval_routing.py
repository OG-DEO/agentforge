from core.task_queue import TaskQueue

queue = TaskQueue()

queue.submit({
    "id": "task-0010",
    "title": "Approval routing test",
    "risk": "high",
    "requires_approval": True,
    "objective": "Confirm high-risk tasks route to approval queue."
})

print("Approval-routing test task queued.")
