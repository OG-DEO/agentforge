from core.branch_lifecycle_manager import BranchLifecycleManager


def main():
    manager = BranchLifecycleManager()
    report = manager.inspect()

    print("=== BRANCH LIFECYCLE REPORT ===")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
