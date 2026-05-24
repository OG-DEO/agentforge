import sys

from core.task_loader import TaskLoader
from core.approval_gate import ApprovalGate
from core.report_writer import save_report
from orchestrators.apply_stage import ApplyStage
from workers.planner_worker import PlannerWorker
from workers.reviewer_worker import ReviewerWorker


def main():
    if len(sys.argv) < 2:
        raise SystemExit(
            "Usage: python scripts/run_task_pipeline.py <task.json> [--apply]"
        )

    task_path = sys.argv[1]
    should_apply = "--apply" in sys.argv[2:]

    loader = TaskLoader()
    gate = ApprovalGate()

    planner = PlannerWorker()
    reviewer = ReviewerWorker()
    apply_stage = ApplyStage()

    task = loader.load(task_path)

    print("\n=== TASK LOADED ===\n")
    print(task)

    if gate.requires_approval(task):
        print("\n=== APPROVAL REQUIRED ===")
        print("Pipeline stopped before execution.")
        return

    print("\n=== GENERATING PLAN ===")

    plan = planner.build_plan(task)

    print("\n=== REVIEWING PLAN ===")

    review = reviewer.review_plan(task, plan)

    apply_result = None

    if should_apply:
        print("\n=== CONTROLLED APPLY ===")

        patch_bundle = task.get("patch_bundle", task)
        apply_result = apply_stage.run(task, patch_bundle)

        print(apply_result)

    combined = f"""
=== TASK ===

{task}

=== PLAN ===

{plan}

=== REVIEW ===

{review}

=== APPLY RESULT ===

{apply_result if apply_result is not None else "Apply not requested."}
"""

    report = save_report(
        f"{task['id']}_pipeline",
        combined
    )

    print("\n=== PLAN ===\n")
    print(plan)

    print("\n=== REVIEW ===\n")
    print(review)

    print(f"\nSaved report: {report}")


if __name__ == "__main__":
    main()
