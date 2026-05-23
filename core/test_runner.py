from core.script_launcher import ScriptLauncher


class TestRunner:
    def __init__(self):
        self.launcher = ScriptLauncher()

    def run_pytest(self):
        return self.launcher.run("pytest")

    def run_script(self, script_path):
        module = script_path

        if module.endswith(".py"):
            module = module[:-3]

        module = module.replace("/", ".")

        return self.launcher.run(module)
