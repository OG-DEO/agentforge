from workers.planner_worker import PlannerWorker


class PlanningStage:
    def __init__(self):
        self.worker = PlannerWorker()

    def run(self, task):
        plan = self.worker.build_plan(task)

        return {
            "plan": plan
        }
