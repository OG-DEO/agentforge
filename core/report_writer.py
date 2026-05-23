from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"

REPORTS.mkdir(exist_ok=True)


def save_report(name, content):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    path = REPORTS / f"{timestamp}_{name}.txt"

    path.write_text(content, encoding="utf-8")

    return path
