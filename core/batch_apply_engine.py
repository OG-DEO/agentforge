from pathlib import Path

from core.apply_engine import ApplyEngine
from core.rollback_manager import RollbackManager


class BatchApplyEngine:
    def __init__(self):
        self.engine = ApplyEngine()
        self.rollback = RollbackManager()

    def apply_batch(self, updates):
        results = []

        for item in updates:
            result = self.engine.apply_text_update(
                item["target_path"],
                item["new_content"]
            )

            results.append(result)

            if not result["applied"]:
                self.rollback.hard_reset()

                return {
                    "success": False,
                    "rolled_back": True,
                    "results": results,
                }

        return {
            "success": True,
            "rolled_back": False,
            "results": results,
        }
