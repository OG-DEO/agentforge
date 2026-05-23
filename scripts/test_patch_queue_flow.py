from core.task_queue import TaskQueue

queue = TaskQueue()

queue.submit({
    "id": "task-0013",
    "title": "Patch queue flow test",
    "risk": "low",
    "requires_approval": False,
    "objective": "Generate a safe patch bundle proposal for two tiny helper files."
})

print("Patch queue test task queued.")
