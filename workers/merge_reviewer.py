from core.lm_studio_client import LMStudioClient
from core.json_utils import extract_json


class MergeReviewer:
    def __init__(self):
        self.client = LMStudioClient()

    def evaluate(self, payload):
        prompt = f"""
Return ONLY valid JSON.

MERGE PAYLOAD:
{payload}

Schema:
{{
  "merge_recommendation": "approve_or_review",
  "confidence_score": 0,
  "rollback_risk": "low_medium_high",
  "review_urgency": "low_medium_high",
  "reasons": [
    "reason"
  ]
}}

Evaluate:
- implementation safety
- rollback likelihood
- complexity
- governance confidence
"""

        messages = [
            {
                "role": "system",
                "content": "You are a cautious AI merge governance reviewer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = self.client.chat(
            messages,
            max_tokens=2000
        )["content"]

        return extract_json(response)
