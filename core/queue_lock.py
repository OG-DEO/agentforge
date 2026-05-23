from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LOCK_FILE = ROOT / "queue.lock"


class QueueLock:
    def acquire(self):
        if LOCK_FILE.exists():
            return False

        LOCK_FILE.write_text(
            "locked",
            encoding="utf-8"
        )

        return True

    def release(self):
        if LOCK_FILE.exists():
            LOCK_FILE.unlink()

    def is_locked(self):
        return LOCK_FILE.exists()
