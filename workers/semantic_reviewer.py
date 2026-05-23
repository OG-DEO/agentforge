from core.lm_studio_client import LMStudioClient
from core.json_utils import extract_json


class SemanticReviewer:
    def __init__(self):
        self.client = LMStudioClient()

    def review_code(self, task, diff_text):
        prompt = f"""
Return ONLY valid JSON.

TASK:
{task}

DIFF:
{diff_text}

Schema:
{{
  "quality_status": "approved_or_revision_needed",
  "issues": [
    "issue"
  ],
  "recommendations": [
    "recommendation"
  ],
  "risk_level": "low_medium_high"
}}

Review for:
- maintainability
- safety
- readability
- unnecessary complexity
- dangerous patterns
"""

        messages = [
            {
                "role": "system",
                "content": "You are a cautious senior software reviewer."
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
