from core.lm_studio_client import LMStudioClient
from core.json_utils import extract_json


class ReviewerWorker:
    def __init__(self):
        self.client = LMStudioClient()

    def review_plan(self, task, plan):
        prompt = f"""
You are the UltraWorkers review system.

Return ONLY valid JSON.

TASK:
{task}

PLAN:
{plan}

Required schema:

{{
  "approval_status": "approved_or_needs_review",
  "concerns": [
    "concern 1"
  ],
  "recommendations": [
    "recommendation 1"
  ]
}}
"""

        messages = [
            {
                "role": "system",
                "content": "You are a cautious AI review worker that outputs strict JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = self.client.chat(messages)["content"]

        return extract_json(response)
