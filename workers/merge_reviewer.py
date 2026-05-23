from core.lm_studio_client import LMStudioClient
from core.json_utils import extract_json
from core.schema_validator import SchemaValidator


class MergeReviewer:
    def __init__(self):
        self.client = LMStudioClient()
        self.validator = SchemaValidator()

    def evaluate(self, payload):
        prompt = f"""
Return ONLY valid JSON.

MERGE PAYLOAD:
{payload}

Schema:
{{
  "merge_recommendation": "approve",
  "confidence_score": 0,
  "rollback_risk": "low",
  "review_urgency": "low",
  "reasons": [
    "reason"
  ]
}}

Allowed merge_recommendation:
- approve
- review
- reject

Allowed rollback_risk:
- low
- medium
- high

Allowed review_urgency:
- low
- medium
- high

You MUST choose exactly one allowed enum value.
"""

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a cautious AI merge governance reviewer."
                )
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

        result = extract_json(response)

        self.validator.require_fields(
            result,
            [
                "merge_recommendation",
                "confidence_score",
                "rollback_risk",
                "review_urgency",
                "reasons",
            ]
        )

        self.validator.require_enum(
            result,
            "merge_recommendation",
            [
                "approve",
                "review",
                "reject",
            ]
        )

        self.validator.require_enum(
            result,
            "rollback_risk",
            [
                "low",
                "medium",
                "high",
            ]
        )

        self.validator.require_enum(
            result,
            "review_urgency",
            [
                "low",
                "medium",
                "high",
            ]
        )

        return result
