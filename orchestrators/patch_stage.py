from workers.multi_file_patch_executor import (
    MultiFilePatchExecutor
)


class PatchStage:
    def __init__(self):
        self.worker = MultiFilePatchExecutor()

    def run(self, task):
        patch_bundle = (
            self.worker.generate_patch_bundle(task)
        )

        return {
            "patch_bundle": patch_bundle
        }
