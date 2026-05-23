from workers.multi_file_patch_executor import MultiFilePatchExecutor
from core.batch_apply_engine import BatchApplyEngine

task = {
    "id": "task-0005",
    "objective": "Create two tiny helper Python files in workspaces for testing batch AI patching."
}

executor = MultiFilePatchExecutor()
engine = BatchApplyEngine()

bundle = executor.generate_patch_bundle(task)

print("\n=== BUNDLE SUMMARY ===\n")
print(bundle["summary"])

result = engine.apply_batch(bundle["updates"])

print("\n=== BATCH APPLY RESULT ===\n")
print(result)
