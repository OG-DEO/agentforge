import json

from core.task_queue import TaskQueue
from core.approval_gate import ApprovalGate
from core.approval_queue import ApprovalQueue
from core.task_branch_manager import TaskBranchManager
from workers.planner_worker import PlannerWorker
from workers.reviewer_worker import ReviewerWorker
from workers.semantic_reviewer import SemanticReviewer
from workers.multi_file_patch_executor import MultiFilePatchExecutor
from core.report_writer import save_report

queue = TaskQueue()
gate = ApprovalGate()
approvals = ApprovalQueue()
branches = TaskBranchManager()

planner = PlannerWorker()
reviewer = ReviewerWorker()
semantic = SemanticReviewer()
patcher = MultiFilePatchExecutor()

print("\n=== TASK QUEUE PROCESSOR ===\n")

tasks = queue.pending()

if not tasks:
    print("No pending tasks.")
    raise SystemExit(0)

for task_path in tasks:
    print(f"\nProcessing: {task_path.name}")

    try:
        task = json.loads(task_path.read_text(encoding="utf-8"))

        if gate.requires_approval(task):
            approval_path = approvals.submit({
                "task": task,
                "reason": "Task requires approval before processing."
            })
            print(f"Approval required. Queued: {approval_path}")
            queue.mark_done(task_path)
            continue

        print("Creating isolated task branch...")
        branch = branches.create_for_task(task)
        print(f"Branch: {branch}")

        print("Generating plan...")
        plan = planner.build_plan(task)

        print("Reviewing plan...")
        review = reviewer.review_plan(task, plan)

        print("Generating patch bundle proposal...")
        patch_bundle = patcher.generate_patch_bundle(task)

        print("Semantic review...")
        semantic_review = semantic.review_code(
            task,
            json.dumps(patch_bundle, indent=2)
        )

        report = {
            "task": task,
            "branch": branch,
            "plan": plan,
            "review": review,
            "patch_bundle": patch_bundle,
            "semantic_review": semantic_review,
            "auto_applied": False,
        }

        path = save_report(
            f"{task['id']}_queue_result",
            json.dumps(report, indent=2)
        )

        print(f"Saved report: {path}")
        print("Patch generated but NOT applied.")

        queue.mark_done(task_path)
        print("Marked DONE.")

    except Exception as e:
        print(f"FAILED: {e}")
        queue.mark_failed(task_path)
        print("Marked FAILED.")
