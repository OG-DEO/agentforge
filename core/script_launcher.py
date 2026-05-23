import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ScriptLauncher:
    def run(self, module_name, timeout=120):
        try:
            result = subprocess.run(
                ["python", "-m", module_name],
                cwd=ROOT,
                text=True,
                capture_output=True,
                timeout=timeout,
            )

            return {
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "timed_out": False,
            }

        except subprocess.TimeoutExpired as e:
            return {
                "returncode": 124,
                "stdout": e.stdout or "",
                "stderr": e.stderr or "Timed out.",
                "timed_out": True,
            }
