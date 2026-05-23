import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MEMORY_DIR = ROOT / "memory"

MEMORY_DIR.mkdir(exist_ok=True)


class WorkerMemory:
    def __init__(self, worker_name):
        self.worker_name = worker_name

        self.path = (
            MEMORY_DIR /
            f"{worker_name}.json"
        )

        if not self.path.exists():
            self.path.write_text(
                json.dumps({}, indent=2),
                encoding="utf-8"
            )

    def load(self):
        return json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )

    def save(self, data):
        self.path.write_text(
            json.dumps(data, indent=2),
            encoding="utf-8"
        )

    def update(self, key, value):
        data = self.load()
        data[key] = value
        self.save(data)

    def get(self, key, default=None):
        data = self.load()
        return data.get(key, default)
