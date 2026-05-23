import sys

from core.task_loader import TaskLoader
from core.approval_gate import ApprovalGate
from core.report_writer import save_report
from workers.planner_worker import PlannerWorker


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python scripts/run_task_pipeline.py <task.json>")

    task_path = sys.argv[1]

    loader = TaskLoader()
    gate = ApprovalGate()
    planner = PlannerWorker()

    task = loader.load(task_path)

    print("\n=== TASK LOADED ===\n")
    print(task)

    if gate.requires_approval(task):
        print("\n=== APPROVAL REQUIRED ===")
        print("Pipeline stopped before execution.")
        return

    print("\n=== GENERATING PLAN ===")

    plan = planner.build_plan(task)

    report = save_report(
        f"{task['id']}_plan",
        plan
    )

    print("\n=== PLAN ===\n")
    print(plan)

    print(f"\nSaved report: {report}")


if __name__ == "__main__":
    main()
