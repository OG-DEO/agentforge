import json

from core.report_writer import save_report


class ReportStage:
    def run(self, task_id, payload):
        path = save_report(
            f"{task_id}_queue_result",
            json.dumps(payload, indent=2)
        )

        return {
            "report_path": str(path)
        }
