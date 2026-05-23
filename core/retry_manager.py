class RetryManager:
    def should_retry(
        self,
        task,
        max_retries=3
    ):
        retries = task.get(
            "_retry_count",
            0
        )

        return retries < max_retries

    def increment(self, task):
        retries = task.get(
            "_retry_count",
            0
        )

        task["_retry_count"] = retries + 1

        return task
