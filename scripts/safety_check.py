import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.git_guard import GitGuard
from core.project_registry import ProjectRegistry

git_guard = GitGuard()
registry = ProjectRegistry()

print("\n=== GIT STATUS ===")
print(git_guard.status() or "clean")

print("\n=== CURRENT BRANCH ===")
print(git_guard.current_branch())

print("\n=== PROJECT ACCESS TEST ===")

for name in ["UltraWorkers", "EZ-PICKENS"]:
    project = registry.ensure_allowed(name)
    print("Allowed:")
    print(project["name"])
    print(project["path"])
    
print("\n=== SAFETY CHECK PASSED ===")
