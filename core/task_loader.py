import json
from pathlib import Path


class TaskLoader:
    def load(self, path):
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(path)

        return json.loads(path.read_text(encoding="utf-8"))
