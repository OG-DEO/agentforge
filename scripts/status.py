import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_FILE = ROOT / "config" / "projects.json"


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)


def main():
    print("\n=== ULTRAWORKERS STATUS ===\n")

    objective = ROOT / "ULTRAWORKERS_OBJECTIVE.md"
    if objective.exists():
        lines = objective.read_text(encoding="utf-8").splitlines()
        for line in lines[:8]:
            print(line)
    else:
        print("[missing objective]")

    print("\n=== REGISTERED PROJECTS ===")
    data = json.loads(PROJECTS_FILE.read_text(encoding="utf-8"))

    for p in data["projects"]:
        allowed = "ALLOWED" if p["allowed_now"] else "PROTECTED"
        print(f"- {p['name']} | {allowed} | risk={p['risk_level']}")
        print(f"  path: {p['path']}")
        print(f"  notes: {p['notes']}")

    print("\n=== GIT STATUS ===")
    result = run(["git", "status", "--short"])
    print(result.stdout.strip() or "clean")


if __name__ == "__main__":
    main()
