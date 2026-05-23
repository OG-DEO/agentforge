from pathlib import Path

from core.requeue_manager import RequeueManager

manager = RequeueManager()

approved = sorted(
    Path("approvals/approved").glob("*_approval.json")
)

if not approved:
    print("No approved tasks found.")
    raise SystemExit(0)

target = approved[0]

print("\n=== REQUEUE TARGET ===\n")
print(target)

result = manager.requeue(target)

print("\n=== RESULT ===\n")
print(result)
