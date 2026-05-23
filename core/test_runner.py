from core.script_launcher import ScriptLauncher


class TestRunner:
    def __init__(self):
        self.launcher = ScriptLauncher()

    def run_pytest(self, timeout=120):
        return self.launcher.run(
            "pytest",
            timeout=timeout
        )

    def run_script(self, script_path, timeout=120):
        module = script_path

        if module.endswith(".py"):
            module = module[:-3]

        module = module.replace("/", ".")

        return self.launcher.run(
            module,
            timeout=timeout
        )
