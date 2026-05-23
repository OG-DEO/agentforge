from core.merge_manager import MergeManager

manager = MergeManager()

print("\n=== MERGE WORKFLOW TEST ===\n")

current = manager.current_branch()

print("Current branch:")
print(current)

print("\nThis is a dry workflow check only.")
print("No merge executed.")
