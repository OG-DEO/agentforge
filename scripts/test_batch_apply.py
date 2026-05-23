from core.batch_apply_engine import BatchApplyEngine

engine = BatchApplyEngine()

updates = [
    {
        "target_path": "/home/scott/projects/ultra_workers/workspaces/batch1.py",
        "new_content": "value = 1\n"
    },
    {
        "target_path": "/home/scott/projects/ultra_workers/workspaces/batch2.py",
        "new_content": "value = 2\n"
    }
]

result = engine.apply_batch(updates)

print("\n=== BATCH RESULT ===\n")
print(result)
