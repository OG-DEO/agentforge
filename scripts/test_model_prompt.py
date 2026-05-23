from pathlib import Path

from core.lm_studio_client import LMStudioClient
from core.report_writer import save_report

ROOT = Path(__file__).resolve().parents[1]

objective = (
    ROOT / "ULTRAWORKERS_OBJECTIVE.md"
).read_text(encoding="utf-8")

client = LMStudioClient()

messages = [
    {
        "role": "system",
        "content": "You are a careful AI planning assistant."
    },
    {
        "role": "user",
        "content": f"""
Summarize this UltraWorkers objective clearly.

OBJECTIVE:

{objective}
"""
    }
]

result = client.chat(messages)

report_path = save_report(
    "objective_summary",
    result["content"]
)

print("\n=== MODEL USED ===\n")
print(result["model"])

print("\n=== RESPONSE ===\n")
print(result["content"])

print(f"\nSaved report: {report_path}")
