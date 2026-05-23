from pathlib import Path


class PathGuard:
    ALLOWED_ROOTS = [
        "/home/scott/projects/ultra_workers",
    ]

    BLOCKED_PATTERNS = [
        "trading_ai_terminal",
        "/mnt/c",
        "/etc/",
        "/usr/",
    ]

    def is_allowed(self, target_path):
        target = str(Path(target_path).resolve())

        for blocked in self.BLOCKED_PATTERNS:
            if blocked.lower() in target.lower():
                return False

        for root in self.ALLOWED_ROOTS:
            if target.startswith(root):
                return True

        return False

    def validate(self, target_path):
        if not self.is_allowed(target_path):
            raise RuntimeError(
                f"Blocked path: {target_path}"
            )

        return True
