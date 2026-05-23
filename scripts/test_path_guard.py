from core.path_guard import PathGuard

guard = PathGuard()

tests = [
    "/home/scott/projects/ultra_workers/core/test.py",
    "/home/scott/projects/trading_ai_terminal/main.py",
    "/etc/passwd",
]

print("\n=== PATH GUARD TEST ===\n")

for path in tests:
    try:
        guard.validate(path)
        print(f"ALLOWED: {path}")

    except Exception as e:
        print(f"BLOCKED: {path}")
        print(f"  Reason: {e}")
