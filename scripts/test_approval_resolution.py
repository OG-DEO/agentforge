from pathlib import Path

from core.approval_resolver import ApprovalResolver

resolver = ApprovalResolver()

approval_files = sorted(
    Path("approvals").glob("*_approval.json")
)

if not approval_files:
    print("No approval files found.")
    raise SystemExit(0)

target = approval_files[0]

print("\n=== APPROVING ===\n")
print(target)

result = resolver.approve(target)

print("\n=== MOVED TO ===\n")
print(result)
