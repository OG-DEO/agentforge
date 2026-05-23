from core.lm_studio_client import LMStudioClient


class ReviewerWorker:
    def __init__(self):
        self.client = LMStudioClient()

    def review_plan(self, task, plan):
        prompt = f"""
You are the UltraWorkers review system.

Review this AI-generated execution plan.

TASK:
{task}

PLAN:
{plan}

Your job:
- Identify risks
- Identify weak assumptions
- Suggest safer alternatives
- Identify missing validation steps
- Identify possible failure points

Be concise but thorough.
"""

        messages = [
            {
                "role": "system",
                "content": "You are a cautious AI review worker."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        return self.client.chat(messages)["content"]
