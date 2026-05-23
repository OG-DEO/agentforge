from difflib import unified_diff


class DiffGenerator:
    def generate(self, original, updated, filename="file.py"):
        diff = unified_diff(
            original.splitlines(keepends=True),
            updated.splitlines(keepends=True),
            fromfile=f"{filename}.before",
            tofile=f"{filename}.after",
        )

        return "".join(diff)
