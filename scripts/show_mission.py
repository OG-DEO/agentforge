from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = [
    "ULTRAWORKERS_OBJECTIVE.md",
    "ULTRAWORKERS_RULES.md",
    "ULTRAWORKERS_ROADMAP.md",
    "ULTRAWORKERS_AGENT_ROLES.md",
    "ULTRAWORKERS_APPROVAL_GATES.md",
]

def main():
    print("\n=== ULTRAWORKERS CURRENT MISSION ===\n")

    for name in FILES:
        path = ROOT / name
        print(f"\n--- {name} ---")
        if path.exists():
            print(path.read_text(encoding="utf-8").strip())
        else:
            print("[missing]")

if __name__ == "__main__":
    main()
