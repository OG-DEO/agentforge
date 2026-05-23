import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = ROOT / "prompts"


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/show_prompt.py commander")
        print("\nAvailable prompts:")
        for path in sorted(PROMPTS_DIR.glob("*.md")):
            print(f"- {path.stem}")
        return

    name = sys.argv[1].replace(".md", "")
    path = PROMPTS_DIR / f"{name}.md"

    if not path.exists():
        print(f"ERROR: prompt not found: {name}")
        print("\nAvailable prompts:")
        for item in sorted(PROMPTS_DIR.glob("*.md")):
            print(f"- {item.stem}")
        sys.exit(1)

    print(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
