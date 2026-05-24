import json
from pathlib import Path
from core.app_spec import AppSpec

ROOT = Path(__file__).resolve().parents[1]
APP_DIR = ROOT / "apps"
APP_DIR.mkdir(exist_ok=True)


class AppRegistry:
    def save(self, spec: AppSpec):
        path = APP_DIR / f"{spec.app_id}.json"
        path.write_text(json.dumps(spec.to_dict(), indent=2))
        return path

    def load(self, app_id: str):
        path = APP_DIR / f"{app_id}.json"
        if not path.exists():
            return None
        return json.loads(path.read_text())

    def list_apps(self):
        return [
            p.stem for p in APP_DIR.glob("*.json")
        ]
