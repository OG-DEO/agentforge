import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd):
    print(f"\n$ {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=ROOT, text=True)
    if result.returncode != 0:
        sys.exit(result.returncode)


def main():
    task_file = sys.argv[1] if len(sys.argv) > 1 else "tasks/example_task.json"

    print("\n=== ULTRAWORKERS PRE-RUN CHECK ===")

    run(["python", "scripts/status.py"])
    run(["python", "scripts/check_task.py", task_file])
    run(["python", "scripts/model_status.py"])
    run(["git", "status", "--short"])

    print("\n=== CHECK COMPLETE ===")
    print("No project code was changed.")


if __name__ == "__main__":
    main()
