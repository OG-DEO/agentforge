import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "model_backend.json"


class LMStudioClient:
    def __init__(self):
        self.config = json.loads(CONFIG.read_text(encoding="utf-8"))
        self.base_url = self.config["base_url"].rstrip("/")

    def list_models(self):
        url = f"{self.base_url}/models"

        with urllib.request.urlopen(url, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))

        return payload.get("data", [])

    def select_model(self):
        models = self.list_models()

        for model in models:
            model_id = model.get("id", "")

            if "coder" in model_id and "uncensored" not in model_id:
                return model_id

        if models:
            return models[0]["id"]

        raise RuntimeError("No available models.")

    def chat(self, messages, temperature=0.2, max_tokens=600):
        model = self.select_model()

        body = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )

        with urllib.request.urlopen(request, timeout=180) as response:
            result = json.loads(response.read().decode("utf-8"))

        return {
            "model": model,
            "content": result["choices"][0]["message"]["content"]
        }
