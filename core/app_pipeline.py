# core/app_pipeline.py

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
import time
import uuid


@dataclass
class PipelineStep:
    name: str
    status: str = "pending"
    output: Optional[Any] = None
    error: Optional[str] = None


@dataclass
class PipelineJob:
    id: str
    goal: str
    context: Dict[str, Any] = field(default_factory=dict)
    steps: List[PipelineStep] = field(default_factory=list)
    status: str = "queued"
    result: Optional[Dict[str, Any]] = None


class AppPipeline:
    """
    Core orchestration engine for UltraWorkers.
    Turns a goal into structured execution steps.
    """

    def __init__(self, workers: Dict[str, Any]):
        self.workers = workers
        self.jobs: Dict[str, PipelineJob] = {}

    def create_job(self, goal: str, context: Dict[str, Any] = None) -> str:
        job_id = str(uuid.uuid4())

        job = PipelineJob(
            id=job_id,
            goal=goal,
            context=context or {},
            steps=[
                PipelineStep("plan"),
                PipelineStep("code"),
                PipelineStep("test"),
                PipelineStep("review"),
            ],
        )

        self.jobs[job_id] = job
        return job_id

    def run(self, job_id: str):
        job = self.jobs[job_id]
        job.status = "running"

        try:
            # 1. PLAN
            job.steps[0].status = "running"
            plan = self.workers["planner"].run(job.goal, job.context)
            job.steps[0].output = plan
            job.steps[0].status = "done"

            # 2. CODE
            job.steps[1].status = "running"
            code = self.workers["coder"].run(plan, job.context)
            job.steps[1].output = code
            job.steps[1].status = "done"

            # 3. TEST
            job.steps[2].status = "running"
            test_result = self.workers["tester"].run(code)
            job.steps[2].output = test_result
            job.steps[2].status = "done"

            # 4. REVIEW
            job.steps[3].status = "running"
            review = self.workers["reviewer"].run(code, test_result)
            job.steps[3].output = review
            job.steps[3].status = "done"

            job.result = {
                "plan": plan,
                "code": code,
                "test": test_result,
                "review": review,
            }

            job.status = "completed"

        except Exception as e:
            job.status = "failed"
            job.steps[-1].error = str(e)

        return job

    def get_job(self, job_id: str) -> PipelineJob:
        return self.jobs[job_id]

