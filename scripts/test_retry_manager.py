from core.retry_manager import RetryManager

manager = RetryManager()

task = {
    "id": "task-0017"
}

for i in range(5):
    allowed = manager.should_retry(task)

    print(
        f"retry={task.get('_retry_count', 0)} "
        f"allowed={allowed}"
    )

    if allowed:
        manager.increment(task)
