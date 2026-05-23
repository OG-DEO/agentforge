from core.script_launcher import ScriptLauncher

launcher = ScriptLauncher()

result = launcher.run(
    "scripts.safety_check"
)

print("\n=== LAUNCH RESULT ===\n")
print("Return code:", result["returncode"])

print("\nSTDOUT:\n")
print(result["stdout"])

if result["stderr"]:
    print("\nSTDERR:\n")
    print(result["stderr"])
