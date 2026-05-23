import time
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_once():
    return subprocess.run(
        ["python", "-m", "scripts.process_task_queue"],
        cwd=ROOT,
        text=True,
    )


def main():
    print("\n=== ULTRAWORKERS QUEUE DAEMON ===\n")
    print("Press Ctrl+C to stop.")

    while True:
        run_once()
        time.sleep(10)


if __name__ == "__main__":
    main()
