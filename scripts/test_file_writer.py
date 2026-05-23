from pathlib import Path

from core.file_writer import ControlledFileWriter

writer = ControlledFileWriter()

target = Path("/home/scott/projects/ultra_workers/workspaces/file_writer_test.txt")

result = writer.write_text(
    target,
    "Controlled writer test successful.\n"
)

print(f"Wrote: {result}")
