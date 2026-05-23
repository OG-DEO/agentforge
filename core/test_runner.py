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
        module = script_path

        if module.endswith(".py"):
            module = module[:-3]

        module = module.replace("/", ".")

        result = subprocess.run(
            ["python", "-m", module],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
