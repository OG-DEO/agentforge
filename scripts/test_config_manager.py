from core.config_manager import ConfigManager

config = ConfigManager()

print("\n=== CONFIG ===\n")

print(
    "timeout:",
    config.get(
        "timeouts",
        "default_script_timeout"
    )
)

print(
    "max retries:",
    config.get(
        "retries",
        "max_task_retries"
    )
)

print(
    "temperature:",
    config.get(
        "llm",
        "temperature"
    )
)
