from core.lm_studio_client import LMStudioClient
from core.json_utils import extract_json


class ExecutionWorker:
    def __init__(self):
        self.client = LMStudioClient()

    def propose_patch(self, task):
        prompt = f"""
You are the UltraWorkers execution planning system.

Return ONLY valid JSON.

TASK:
{task}

Generate a SAFE proposed patch plan.

Schema:

{{
  "summary": "what this patch would do",
  "target_files": [
    "path/file.py"
  ],
  "operations": [
    "create function",
    "update config"
  ],
  "risk_level": "low",
  "requires_approval": true
}}

Do NOT generate real code yet.
Do NOT assume permission to edit files.
"""

        messages = [
            {
                "role": "system",
                "content": "You are a cautious execution planning worker."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = self.client.chat(messages)["content"]

        return extract_json(response)
