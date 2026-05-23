from core.path_guard import PathGuard
from core.git_branch_manager import GitBranchManager


def test_path_guard_allows_ultraworkers():
    guard = PathGuard()
    assert guard.is_allowed("/home/scott/projects/ultra_workers/core/x.py")


def test_path_guard_blocks_trading_project():
    guard = PathGuard()
    assert not guard.is_allowed("/home/scott/projects/trading_ai_terminal/main.py")


def test_not_empty_branch():
    manager = GitBranchManager()
    assert manager.current_branch()
