import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = ROOT / "tasks"
PROJECTS_FILE = ROOT / "config" / "projects.json"


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:50] or "task"


def load_projects():
    data = json.loads(PROJECTS_FILE.read_text(encoding="utf-8"))
    return {p["name"]: p for p in data["projects"]}


def main():
    if len(sys.argv) < 4:
        print("Usage:")
        print('  python scripts/create_task.py "Project Name" "Task title" "Task objective"')
        sys.exit(1)

    project_name = sys.argv[1]
    title = sys.argv[2]
    objective = sys.argv[3]

    projects = load_projects()
    project = projects.get(project_name)

    if not project:
        print(f"ERROR: Unknown project: {project_name}")
        print("Known projects:")
        for name in projects:
            print(f"- {name}")
        sys.exit(1)

    now = datetime.now().strftime("%Y%m%d-%H%M%S")
    task_id = f"task-{now}-{slugify(title)}"
    path = TASKS_DIR / f"{task_id}.json"

    risk_level = project.get("risk_level", "medium")
    requires_approval = not project.get("allowed_now", False) or risk_level in ["medium", "high"]

    task = {
        "task_id": task_id,
        "title": title,
        "project": project_name,
        "objective": objective,
        "status": "draft",
        "risk_level": risk_level,
        "requires_approval": requires_approval,
        "allowed_files": [],
        "blocked_actions": [
            "delete files",
            "install dependencies",
            "edit protected projects without approval",
            "push to GitHub",
            "run long background jobs",
            "enable live trading"
        ],
        "definition_of_done": [
            "Task is clearly described.",
            "Allowed files are listed before execution.",
            "Blocked actions are respected.",
            "Safety check passes before work begins."
        ]
    }

    path.write_text(json.dumps(task, indent=2) + "\n", encoding="utf-8")
    print(f"Created task: {path}")
    print(f"Requires approval: {requires_approval}")


if __name__ == "__main__":
    main()
