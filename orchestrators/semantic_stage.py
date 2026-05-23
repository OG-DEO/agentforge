import json

from workers.semantic_reviewer import (
    SemanticReviewer
)


class SemanticStage:
    def __init__(self):
        self.worker = SemanticReviewer()

    def run(self, task, patch_bundle):
        review = self.worker.review_code(
            task,
            json.dumps(
                patch_bundle,
                indent=2
            )
        )

        return {
            "semantic_review": review
        }
