from core.lm_studio_client import LMStudioClient
from core.json_utils import extract_json


class MultiFilePatchExecutor:
    def __init__(self):
        self.client = LMStudioClient()

    def generate_patch_bundle(self, task):
        prompt = f"""
Return ONLY valid JSON.

TASK:
{task}

Create a small safe multi-file patch bundle.

Schema:
{{
  "summary": "what the bundle does",
  "updates": [
    {{
      "target_path": "/home/scott/projects/ultra_workers/workspaces/example.py",
      "new_content": "full file content"
    }}
  ]
}}

Rules:
- Use only /home/scott/projects/ultra_workers/workspaces/
- Generate simple valid Python files
- No protected project paths
"""

        messages = [
            {"role": "system", "content": "You are a careful multi-file patch generator."},
            {"role": "user", "content": prompt},
        ]

        return extract_json(self.client.chat(messages, max_tokens=2500)["content"])
