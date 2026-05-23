from core.approval_queue import ApprovalQueue

queue = ApprovalQueue()

payload = {
    "task": {
        "id": "task-0007",
        "objective": "Test approval queue."
    },
    "summary": "Pending approval test."
}

path = queue.submit(payload)

print("\n=== APPROVAL SUBMITTED ===\n")
print(path)

print("\n=== PENDING ITEMS ===\n")
for item in queue.list_pending():
    print(item["path"])
