import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "config" / "projects.json"


class ProjectRegistry:
    def __init__(self):
        self.data = json.loads(
            PROJECTS.read_text(encoding="utf-8")
        )

    def get_project(self, name):
        for project in self.data["projects"]:
            if project["name"] == name:
                return project

        return None

    def ensure_allowed(self, name):
        project = self.get_project(name)

        if not project:
            raise RuntimeError(
                f"Unknown project: {name}"
            )

        if not project["allowed_now"]:
            raise RuntimeError(
                f"Project is protected: {name}"
            )

        return project
