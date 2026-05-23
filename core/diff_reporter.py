from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
DIFF_DIR = ROOT / "reports" / "diffs"

DIFF_DIR.mkdir(parents=True, exist_ok=True)


class DiffReporter:
    def save(self, name, diff_text):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = DIFF_DIR / f"{timestamp}_{name}.diff"
        path.write_text(diff_text, encoding="utf-8")
        return path
