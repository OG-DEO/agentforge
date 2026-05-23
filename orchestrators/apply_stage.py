from core.batch_apply_engine import BatchApplyEngine


class ApplyStage:
    def __init__(self):
        self.engine = BatchApplyEngine()

    def run(self, patch_bundle):
        updates = patch_bundle.get("updates", [])

        if not updates:
            return {
                "applied": False,
                "reason": "No updates found."
            }

        result = self.engine.apply_batch(updates)

        return {
            "applied": result.get("success", False),
            "result": result,
        }
