from core.approval_queue import ApprovalQueue


class ApprovalStage:
    def __init__(self):
        self.queue = ApprovalQueue()

    def run(
        self,
        task,
        patch_bundle,
        semantic_review,
        reason,
    ):
        path = self.queue.submit({
            "task": task,
            "patch_bundle": patch_bundle,
            "semantic_review": semantic_review,
            "reason": reason,
        })

        return {
            "approval_path": str(path)
        }
