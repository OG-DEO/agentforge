from pathlib import Path

from workers.patch_executor import PatchExecutor
from core.apply_engine import ApplyEngine

target = Path("/home/scott/projects/ultra_workers/workspaces/ai_generated_test.py")

current = """def hello():
    return "hello"
"""

target.write_text(current, encoding="utf-8")

task = {
    "id": "task-0004",
    "objective": "Improve this tiny test module by adding a main guard that prints hello()."
}

executor = PatchExecutor()
engine = ApplyEngine()

patch = executor.generate_file_update(task, target, current)

print("\n=== AI PATCH SUMMARY ===\n")
print(patch["summary"])

result = engine.apply_text_update(
    patch["target_path"],
    patch["new_content"]
)

print("\n=== APPLY RESULT ===\n")
print(result["applied"])
print("Rolled back:", result["rolled_back"])

print("\n=== DIFF ===\n")
print(result["diff"])
