from workers.merge_reviewer import MergeReviewer

reviewer = MergeReviewer()

payload = {
    "task_id": "task-0015",
    "branch": "task/task-0015/demo",
    "summary": "Low-risk helper utility update.",
    "auto_applied": True,
    "pytest_passed": True,
}

result = reviewer.evaluate(payload)

print("\n=== MERGE REVIEW ===\n")
print(result)
