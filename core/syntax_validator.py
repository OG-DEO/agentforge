import py_compile
from pathlib import Path


class SyntaxValidator:
    def validate_python_file(self, path):
        path = Path(path)

        try:
            py_compile.compile(str(path), doraise=True)
            return {"valid": True, "error": None}
        except Exception as e:
            return {"valid": False, "error": str(e)}
