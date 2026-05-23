from core.lm_studio_client import LMStudioClient
from core.json_utils import extract_json


class PatchExecutor:
    def __init__(self):
        self.client = LMStudioClient()

    def generate_file_update(self, task, target_path, current_content):
        prompt = f"""
Return ONLY valid JSON.

TASK:
{task}

TARGET FILE:
{target_path}

CURRENT CONTENT:
{current_content}

Schema:
{{
  "target_path": "{target_path}",
  "new_content": "full replacement file content",
  "summary": "what changed"
}}
"""

        messages = [
            {"role": "system", "content": "You are a careful code patch generator."},
            {"role": "user", "content": prompt},
        ]

        return extract_json(self.client.chat(messages, max_tokens=2000)["content"])
