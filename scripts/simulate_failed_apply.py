from pathlib import Path

from core.file_writer import ControlledFileWriter
from core.rollback_manager import RollbackManager

writer = ControlledFileWriter()
rollback = RollbackManager()

target = Path(
    "/home/scott/projects/ultra_workers/workspaces/failure_test.txt"
)

print("\n=== WRITING TEST FILE ===\n")

result = writer.write_text(
    target,
    "This simulates a risky AI modification.\n"
)

print(result)

print("\n=== SIMULATED TEST FAILURE ===\n")

failed = True

if failed:
    print("Failure detected.")
    print("Rolling back git state...")

    rollback.hard_reset()

    print("Rollback complete.")
else:
    print("Tests passed.")
