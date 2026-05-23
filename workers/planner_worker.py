from core.lm_studio_client import LMStudioClient


class PlannerWorker:
    def __init__(self):
        self.client = LMStudioClient()

    def build_plan(self, task):
        prompt = f"""
You are the UltraWorkers planning system.

Create a concise execution plan.

TASK:
{task}

Requirements:
- Be structured
- Be cautious
- Do not assume permission for destructive actions
- Prefer reversible operations
"""

        messages = [
            {
                "role": "system",
                "content": "You are a careful AI planning worker."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        return self.client.chat(messages)["content"]
