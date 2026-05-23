import json

from core.task_queue import TaskQueue
from core.queue_lock import QueueLock
from core.approval_gate import ApprovalGate

from orchestrators.branch_stage import BranchStage
from orchestrators.planning_stage import PlanningStage
from orchestrators.review_stage import ReviewStage
from orchestrators.patch_stage import PatchStage
from orchestrators.semantic_stage import SemanticStage
from orchestrators.apply_decision_stage import (
    ApplyDecisionStage
)
from orchestrators.approval_stage import ApprovalStage
from orchestrators.report_stage import ReportStage

print("\n=== TASK QUEUE PROCESSOR ===\n")

lock = QueueLock()

if not lock.acquire():
    print("Queue is already locked. Exiting.")
    raise SystemExit(0)

queue = TaskQueue()
gate = ApprovalGate()

branch_stage = BranchStage()
planning_stage = PlanningStage()
review_stage = ReviewStage()
patch_stage = PatchStage()
semantic_stage = SemanticStage()

decision_stage = ApplyDecisionStage()
approval_stage = ApprovalStage()
report_stage = ReportStage()

tasks = queue.pending()

if not tasks:
    print("No pending tasks.")
    lock.release()
    raise SystemExit(0)

for task_path in tasks:
    print(f"\nProcessing: {task_path.name}")

    try:
        task = json.loads(
            task_path.read_text(
                encoding="utf-8"
            )
        )

        if gate.requires_approval(task):
            result = approval_stage.run(
                task=task,
                patch_bundle=None,
                semantic_review=None,
                reason="Task requires approval before processing."
            )

            print(
                f"Approval required: "
                f"{result['approval_path']}"
            )

            queue.mark_done(task_path)
            continue

        branch_result = branch_stage.run(task)
        branch = branch_result["branch"]

        print(f"Branch: {branch}")

        planning_result = planning_stage.run(task)
        plan = planning_result["plan"]

        review_result = review_stage.run(
            task,
            plan
        )

        review = review_result["review"]

        patch_result = patch_stage.run(task)
        patch_bundle = patch_result["patch_bundle"]

        semantic_result = semantic_stage.run(
            task,
            patch_bundle
        )

        semantic_review = (
            semantic_result["semantic_review"]
        )

        decision_result = decision_stage.run(
            semantic_review
        )

        safe_to_apply = (
            decision_result["safe_to_apply"]
        )

        if not safe_to_apply:
            approval_result = approval_stage.run(
                task=task,
                patch_bundle=patch_bundle,
                semantic_review=semantic_review,
                reason="Patch requires human approval."
            )

            print(
                f"Approval queued: "
                f"{approval_result['approval_path']}"
            )

        report_payload = {
            "task": task,
            "branch": branch,
            "plan": plan,
            "review": review,
            "patch_bundle": patch_bundle,
            "semantic_review": semantic_review,
            "safe_to_apply": safe_to_apply,
        }

        report_result = report_stage.run(
            task["id"],
            report_payload
        )

        print(
            f"Saved report: "
            f"{report_result['report_path']}"
        )

        queue.mark_done(task_path)

        print("Marked DONE.")

    except Exception as e:
        print(f"FAILED: {e}")

        queue.mark_failed(task_path)

        print("Marked FAILED.")

lock.release()
