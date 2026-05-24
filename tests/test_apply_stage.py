from pathlib import Path

import pytest

from orchestrators.apply_stage import ApplyStage


PROJECT_ROOT = Path("/home/scott/projects/ultra_workers")


class FakeRegistry:
    def __init__(self, allowed=True):
        self.allowed = allowed

    def ensure_allowed(self, name):
        if not self.allowed:
            raise RuntimeError(f"Project is protected: {name}")

        return {
            "name": name,
            "path": str(PROJECT_ROOT),
            "allowed_now": True,
        }


class FakeGit:
    def __init__(self, dirty=False, branch="task/test"):
        self.dirty = dirty
        self.branch = branch

    def require_clean_tree(self, repo_root=None):
        if self.dirty:
            raise RuntimeError("Working tree is not clean.")

    def require_not_main(self, repo_root=None):
        if self.branch == "main":
            raise RuntimeError("Blocked: cannot apply on main branch.")


class FakePaths:
    def validate(self, target_path):
        return True


class FakeEngine:
    def __init__(self):
        self.calls = []

    def apply_text_update(self, path, new_content, require_clean=True):
        self.calls.append(
            {
                "path": path,
                "new_content": new_content,
                "require_clean": require_clean,
            }
        )

        return {
            "applied": True,
            "rolled_back": False,
        }


def make_stage(engine=None, git=None, registry=None):
    return ApplyStage(
        engine=engine or FakeEngine(),
        git=git or FakeGit(),
        paths=FakePaths(),
        registry=registry or FakeRegistry(),
    )


def test_apply_stage_applies_only_allowed_files():
    engine = FakeEngine()
    stage = make_stage(engine=engine)
    target = PROJECT_ROOT / "workspaces" / "controlled_apply_smoke.txt"

    result = stage.run(
        {
            "project": "UltraWorkers",
            "allowed_files": [str(target)],
        },
        {
            "updates": [
                {
                    "target_path": str(target),
                    "new_content": "ok\n",
                }
            ]
        },
    )

    assert result["applied"] is True
    assert engine.calls == [
        {
            "path": str(target),
            "new_content": "ok\n",
            "require_clean": False,
        }
    ]


def test_apply_stage_blocks_files_outside_allowed_files():
    stage = make_stage()

    with pytest.raises(RuntimeError, match="not in allowed_files"):
        stage.run(
            {
                "project": "UltraWorkers",
                "allowed_files": [
                    str(PROJECT_ROOT / "workspaces" / "allowed.txt")
                ],
            },
            {
                "updates": [
                    {
                        "target_path": str(
                            PROJECT_ROOT / "workspaces" / "blocked.txt"
                        ),
                        "new_content": "blocked\n",
                    }
                ]
            },
        )


def test_apply_stage_blocks_dirty_git_tree():
    stage = make_stage(git=FakeGit(dirty=True))
    target = PROJECT_ROOT / "workspaces" / "controlled_apply_smoke.txt"

    with pytest.raises(RuntimeError, match="Working tree is not clean"):
        stage.run(
            {
                "project": "UltraWorkers",
                "allowed_files": [str(target)],
            },
            {
                "updates": [
                    {
                        "target_path": str(target),
                        "new_content": "ok\n",
                    }
                ]
            },
        )


def test_apply_stage_blocks_main_branch():
    stage = make_stage(git=FakeGit(branch="main"))
    target = PROJECT_ROOT / "workspaces" / "controlled_apply_smoke.txt"

    with pytest.raises(RuntimeError, match="main branch"):
        stage.run(
            {
                "project": "UltraWorkers",
                "allowed_files": [str(target)],
            },
            {
                "updates": [
                    {
                        "target_path": str(target),
                        "new_content": "ok\n",
                    }
                ]
            },
        )


def test_apply_stage_blocks_protected_projects():
    stage = make_stage(registry=FakeRegistry(allowed=False))
    target = PROJECT_ROOT / "workspaces" / "controlled_apply_smoke.txt"

    with pytest.raises(RuntimeError, match="Project is protected"):
        stage.run(
            {
                "project": "Trading AI Terminal",
                "allowed_files": [str(target)],
            },
            {
                "updates": [
                    {
                        "target_path": str(target),
                        "new_content": "blocked\n",
                    }
                ]
            },
        )
