from core.approval_queue import ApprovalQueue

queue = ApprovalQueue()

items = queue.list_pending()

print("\n=== PENDING APPROVALS ===\n")

if not items:
    print("No pending approvals.")
    raise SystemExit(0)

for item in items:
    data = item["data"]

    print(f"FILE: {item['path']}")
    print(f"STATUS: {data['status']}")

    payload = data.get("payload", {})
    task = payload.get("task", {})

    print(f"TASK ID: {task.get('id')}")
    print(f"TITLE: {task.get('title')}")
    print(f"OBJECTIVE: {task.get('objective')}")
    print("-" * 60)
