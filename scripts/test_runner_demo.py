from core.test_runner import TestRunner

runner = TestRunner()

result = runner.run_script(
    "scripts/safety_check.py"
)

print("\n=== TEST RESULT ===\n")

print("Return code:")
print(result["returncode"])

print("\nSTDOUT:\n")
print(result["stdout"])

if result["stderr"]:
    print("\nSTDERR:\n")
    print(result["stderr"])
