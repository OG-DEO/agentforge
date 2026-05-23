import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestRunner:
    def run_pytest(self):
        result = subprocess.run(
            ["pytest", "-q"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }

    def run_script(self, script_path):
        result = subprocess.run(
            ["python", script_path],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
