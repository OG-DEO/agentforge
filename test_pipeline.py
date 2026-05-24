from core.app_pipeline import AppPipeline

# dummy workers (temporary)
class Dummy:
    def __init__(self, name): self.name = name
    def run(self, *args): return f"{self.name} output: {args}"

workers = {
    "planner": Dummy("planner"),
    "coder": Dummy("coder"),
    "tester": Dummy("tester"),
    "reviewer": Dummy("reviewer"),
}

pipeline = AppPipeline(workers)

job_id = pipeline.create_job("build a trading dashboard")
job = pipeline.run(job_id)

print(job.result)

