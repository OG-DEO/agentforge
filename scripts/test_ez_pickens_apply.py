from pathlib import Path

from core.apply_engine import ApplyEngine

target = Path("/home/scott/projects/ez_pickens/frontend/index.html")

original = target.read_text(encoding="utf-8")

marker = "<!-- UltraWorkers apply test passed -->"

if marker not in original:
    new_content = original.replace(
        "</body>",
        f"    {marker}\n</body>"
    )
else:
    new_content = original

engine = ApplyEngine()

result = engine.apply_text_update(
    target,
    new_content
)

print("\n=== EZ-PICKENS APPLY RESULT ===\n")
print(result)
