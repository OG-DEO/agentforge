from core.git_guard import GitGuard
from core.git_branch_manager import GitBranchManager
from core.path_guard import PathGuard
from core.test_runner import TestRunner

git_guard = GitGuard()
branch = GitBranchManager()
path_guard = PathGuard()
tests = TestRunner()

current = branch.current_branch()

print("\n=== PRE-APPLY CHECK ===\n")
print(f"Branch: {current}")

if current == "main":
    raise SystemExit("BLOCKED: never apply AI edits directly on main.")

git_guard.require_clean_tree()

path_guard.validate("/home/scott/projects/ultra_workers/core/example.py")

result = tests.run_script("scripts/safety_check.py")

print("Safety check return code:", result["returncode"])

if result["returncode"] != 0:
    raise SystemExit("BLOCKED: safety check failed.")

print("\nPASS: safe to consider controlled apply.")
