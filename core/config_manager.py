import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONFIG_PATH = (
    ROOT /
    "config" /
    "system_config.json"
)


class ConfigManager:
    def __init__(self):
        self.data = json.loads(
            CONFIG_PATH.read_text(
                encoding="utf-8"
            )
        )

    def get(
        self,
        section,
        key=None,
        default=None
    ):
        block = self.data.get(
            section,
            {}
        )

        if key is None:
            return block

        return block.get(
            key,
            default
        )
