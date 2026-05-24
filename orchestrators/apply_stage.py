from pathlib import Path

from core.apply_engine import ApplyEngine
from core.git_guard import GitGuard
from core.path_guard import PathGuard
from core.project_registry import ProjectRegistry


class ApplyStage:
    def __init__(self, engine=None, git=None, paths=None, registry=None):
        self.engine = engine or ApplyEngine()
        self.git = git or GitGuard()
        self.paths = paths or PathGuard()
        self.registry = registry or ProjectRegistry()

    def run(self, task, patch_bundle):
        project = self.registry.ensure_allowed(task["project"])
        project_root = Path(project["path"]).resolve()
        updates = patch_bundle.get("updates", [])

        if not updates:
            return {
                "applied": False,
                "reason": "No updates found."
            }

        allowed = [
            self._resolve_allowed_file(project_root, item)
            for item in task.get("allowed_files", [])
        ]

        if not allowed:
            raise RuntimeError("Blocked: task has no allowed_files.")

        for item in updates:
            target = Path(item["target_path"]).resolve()
            self.paths.validate(target)

            if not self._is_under_project(target, project_root):
                raise RuntimeError(
                    f"Blocked: target outside project root: {target}"
                )

            if not self._is_allowed_file(target, allowed):
                raise RuntimeError(
                    f"Blocked: target not in allowed_files: {target}"
                )

        self.git.require_clean_tree(project_root)
        self.git.require_not_main(project_root)

        results = []

        for item in updates:
            result = self.engine.apply_text_update(
                item["target_path"],
                item["new_content"],
                require_clean=False,
            )
            results.append(result)

            if not result.get("applied"):
                return {
                    "applied": False,
                    "rolled_back": result.get("rolled_back", False),
                    "results": results,
                }

        return {
            "applied": True,
            "rolled_back": False,
            "results": results,
        }

    def _resolve_allowed_file(self, project_root, item):
        path = Path(item)

        if not path.is_absolute():
            path = project_root / path

        return path.resolve()

    def _is_under_project(self, target, project_root):
        try:
            target.relative_to(project_root)
        except ValueError:
            return False

        return True

    def _is_allowed_file(self, target, allowed):
        for item in allowed:
            if target == item:
                return True

            if item.exists() and item.is_dir():
                try:
                    target.relative_to(item)
                except ValueError:
                    pass
                else:
                    return True

        return False
