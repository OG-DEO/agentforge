from core.audit_logger import AuditLogger

logger = AuditLogger("queue")

logger.log(
    "task_started",
    {
        "task_id": "task-0018",
        "branch": "task/demo",
    }
)

logger.log(
    "task_completed",
    {
        "task_id": "task-0018",
        "status": "success",
    }
)

print("\n=== AUDIT LOG WRITTEN ===\n")
print("logs/queue.jsonl")
