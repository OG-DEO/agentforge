from core.git_guard import GitGuard
from core.git_branch_manager import GitBranchManager

guard = GitGuard()
manager = GitBranchManager()

print("\n=== AI BRANCH CREATION ===\n")

guard.require_clean_tree()

current = manager.current_branch()

print(f"Current branch: {current}")

branch = manager.create_ai_branch()

print(f"\nCreated branch: {branch}")

print("\n=== BRANCH LIST ===\n")

for item in manager.list_branches():
    print(item)
