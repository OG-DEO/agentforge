from core.lm_studio_client import LMStudioClient
from core.json_utils import extract_json


class PatchReviewer:
    def __init__(self):
        self.client = LMStudioClient()

    def review_patch(self, patch):
        prompt = f"""
You are the UltraWorkers patch review system.

Return ONLY valid JSON.

PATCH:
{patch}

Schema:

{{
  "approval_status": "approved_or_needs_review",
  "concerns": [
    "concern"
  ],
  "recommended_safety_checks": [
    "check"
  ]
}}
"""

        messages = [
            {
                "role": "system",
                "content": "You are a careful AI patch reviewer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = self.client.chat(messages)["content"]

        return extract_json(response)
