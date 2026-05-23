import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ScriptLauncher:
    def run(self, module_name):
        result = subprocess.run(
            ["python", "-m", module_name],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
