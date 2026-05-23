from workers.reviewer_worker import ReviewerWorker


class ReviewStage:
    def __init__(self):
        self.worker = ReviewerWorker()

    def run(self, task, plan):
        review = self.worker.review_plan(
            task,
            plan
        )

        return {
            "review": review
        }
