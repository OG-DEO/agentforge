import json
import sys
from pathlib import Path

from core.apply_guard import ApplyGuard
from core.diff_preview import render_patch_preview

guard = ApplyGuard()

if len(sys.argv) < 2:
    raise SystemExit(
        "Usage: python scripts/dry_run_apply.py <patch.json>"
    )

patch_file = Path(sys.argv[1])

payload = json.loads(
    patch_file.read_text(encoding="utf-8")
)

patch = payload["patch"]

print("\n=== DRY RUN APPLY ===\n")

preview = render_patch_preview(patch)

print(preview)

print("\n=== VALIDATING TARGETS ===\n")

for target in patch.get("target_files", []):
    guard.validate_target(target)
    print(f"SAFE: {target}")

print("\n=== RESULT ===")
print("Dry-run successful.")
print("No files were modified.")
