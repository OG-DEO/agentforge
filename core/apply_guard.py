from pathlib import Path


class ApplyGuard:
    BLOCKED = [
        "trading_ai_terminal",
    ]

    def validate_target(self, target_path):
        target = str(Path(target_path)).lower()

        for blocked in self.BLOCKED:
            if blocked in target:
                raise RuntimeError(
                    f"Blocked protected target: {blocked}"
                )

        return True
