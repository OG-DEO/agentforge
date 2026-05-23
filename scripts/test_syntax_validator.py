from pathlib import Path
from core.syntax_validator import SyntaxValidator

target = Path("/home/scott/projects/ultra_workers/workspaces/syntax_test.py")
target.write_text("def ok():\n    return True\n", encoding="utf-8")

validator = SyntaxValidator()
print(validator.validate_python_file(target))
