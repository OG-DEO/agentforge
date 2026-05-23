from core.patch_writer import PatchWriter
from workers.execution_worker import ExecutionWorker
from workers.patch_reviewer import PatchReviewer

task = {
    "id": "task-0003",
    "objective": "Add a reusable logging utility to UltraWorkers safely."
}

executor = ExecutionWorker()
reviewer = PatchReviewer()
writer = PatchWriter()

print("\n=== GENERATING PATCH PROPOSAL ===")

patch = executor.propose_patch(task)

print("\n=== PATCH PROPOSAL ===\n")
print(patch)

print("\n=== REVIEWING PATCH ===")

review = reviewer.review_patch(patch)

print("\n=== PATCH REVIEW ===\n")
print(review)

payload = {
    "task": task,
    "patch": patch,
    "review": review,
}

path = writer.save_patch(
    task["id"],
    payload
)

print(f"\nSaved patch proposal: {path}")
