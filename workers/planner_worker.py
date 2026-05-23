from core.lm_studio_client import LMStudioClient
from core.json_utils import extract_json


class PlannerWorker:
    def __init__(self):
        self.client = LMStudioClient()

    def build_plan(self, task):
        prompt = f"""
You are the UltraWorkers planning system.

Return ONLY valid JSON.

TASK:
{task}

Required schema:

{{
  "summary": "short summary",
  "steps": [
    "step 1",
    "step 2"
  ],
  "risks": [
    "risk 1"
  ],
  "requires_approval": false
}}
"""

        messages = [
            {
                "role": "system",
                "content": "You are a careful AI planning worker that outputs strict JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = self.client.chat(messages)["content"]

        return extract_json(response)
