import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.branch_lifecycle_manager import BranchLifecycleManager


def main():
    manager = BranchLifecycleManager()
    report = manager.inspect()

    print("=== BRANCH LIFECYCLE REPORT ===")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
