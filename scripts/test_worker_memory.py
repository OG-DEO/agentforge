from core.worker_memory import WorkerMemory

memory = WorkerMemory(
    "planner_worker"
)

memory.update(
    "last_task",
    "task-0016"
)

memory.update(
    "last_status",
    "success"
)

print("\n=== MEMORY CONTENTS ===\n")
print(memory.load())
