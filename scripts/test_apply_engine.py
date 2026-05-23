from pathlib import Path

from core.apply_engine import ApplyEngine

target = Path("/home/scott/projects/ultra_workers/workspaces/apply_engine_test.txt")

engine = ApplyEngine()

result = engine.apply_text_update(
    target,
    "Apply engine test successful.\n"
)

print("\n=== APPLY RESULT ===\n")
print(result)
