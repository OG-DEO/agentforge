import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = ROOT / "tasks"
PROJECTS_FILE = ROOT / "config" / "projects.json"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    task_file = Path(sys.argv[1]) if len(sys.argv) > 1 else TASKS_DIR / "example_task.json"

    if not task_file.exists():
        print(f"ERROR: task file not found: {task_file}")
        sys.exit(1)

    task = load_json(task_file)
    registry = load_json(PROJECTS_FILE)
    projects = {p["name"]: p for p in registry["projects"]}

    print(f"\n=== TASK CHECK: {task.get('task_id')} ===")
    print(f"Title: {task.get('title')}")
    print(f"Project: {task.get('project')}")
    print(f"Risk: {task.get('risk_level')}")
    print(f"Requires approval: {task.get('requires_approval')}")

    errors = []
    warnings = []

    project_name = task.get("project")
    project = projects.get(project_name)

    if not project:
        errors.append(f"Unknown project: {project_name}")
    else:
        if not project.get("allowed_now"):
            warnings.append(f"Project is protected: {project_name}")
        if project.get("risk_level") == "high":
            warnings.append(f"Project risk is high: {project_name}")

    if task.get("risk_level") in ["medium", "high"] and not task.get("requires_approval"):
        warnings.append("Medium/high risk task should require approval.")

    blocked = task.get("blocked_actions", [])
    if not blocked:
        warnings.append("No blocked_actions listed.")

    allowed_files = task.get("allowed_files", [])
    if not allowed_files:
        warnings.append("No allowed_files listed.")

    print("\n=== RESULT ===")
    if errors:
        print("BLOCKED")
        for e in errors:
            print(f"- ERROR: {e}")
        sys.exit(1)

    if warnings:
        print("NEEDS REVIEW")
        for w in warnings:
            print(f"- WARNING: {w}")
    else:
        print("SAFE TO PLAN")

    print("\nNo code was changed by this check.")


if __name__ == "__main__":
    main()
