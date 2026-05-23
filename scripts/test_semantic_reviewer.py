from workers.semantic_reviewer import SemanticReviewer

task = {
    "id": "task-0006",
    "objective": "Review a small Python change."
}

diff_text = """
--- before.py
+++ after.py
@@
 def add(a, b):
+    print("debug")
     return a + b
"""

reviewer = SemanticReviewer()

result = reviewer.review_code(
    task,
    diff_text
)

print("\n=== SEMANTIC REVIEW ===\n")
print(result)
