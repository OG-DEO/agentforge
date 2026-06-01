import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONFIG_PATH = (
    ROOT /
    "config" /
    "system_config.json"
)


class ConfigManager:
    """
    Manages configuration settings for the application.
    """

    def __init__(self):
        """
        Initializes the ConfigManager by loading the configuration data from a JSON file.
        """
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
        """
        Retrieves a value from the configuration.

        :param section: The section of the configuration to retrieve.
        :param key: The specific key within the section to retrieve. If None, returns the entire section.
        :param default: The default value to return if the key is not found.
        :return: The value associated with the key or the entire section if no key is specified.
        """
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
