from core.diff_generator import DiffGenerator

original = """
def add(a, b):
    return a + b
"""

updated = """
def add(a, b):
    print("adding values")
    return a + b
"""

generator = DiffGenerator()

diff = generator.generate(
    original,
    updated,
    filename="example.py"
)

print("\n=== GENERATED DIFF ===\n")
print(diff)
