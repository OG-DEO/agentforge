from pathlib import Path

from core.file_writer import ControlledFileWriter
from core.diff_generator import DiffGenerator
from core.test_runner import TestRunner
from core.rollback_manager import RollbackManager
from core.syntax_validator import SyntaxValidator


class ApplyEngine:
    def __init__(self):
        self.writer = ControlledFileWriter()
        self.diff = DiffGenerator()
        self.tests = TestRunner()
        self.rollback = RollbackManager()
        self.syntax = SyntaxValidator()

    def apply_text_update(self, path, new_content, test_script="scripts/safety_check.py"):
        target = Path(path).resolve()

        original = (
            target.read_text(encoding="utf-8")
            if target.exists()
            else ""
        )

        preview = self.diff.generate(
            original,
            new_content,
            filename=str(target)
        )

        result = self.writer.write_text(
            target,
            new_content
        )

        if target.suffix == ".py":
            syntax = self.syntax.validate_python_file(target)

            if not syntax["valid"]:
                self.rollback.hard_reset()

                return {
                    "applied": False,
                    "rolled_back": True,
                    "syntax_error": syntax,
                    "diff": preview,
                }

        test_result = self.tests.run_script(
            test_script
        )

        if test_result["returncode"] != 0:
            self.rollback.hard_reset()

            return {
                "applied": False,
                "rolled_back": True,
                "test_result": test_result,
                "diff": preview,
            }

        return {
            "applied": True,
            "rolled_back": False,
            "test_result": test_result,
            "diff": preview,
        }
