HIGH_RISK = {
    "high",
    "critical",
}


class ApprovalGate:
    def requires_approval(self, task):
        if task.get("requires_approval"):
            return True

        risk = str(task.get("risk", "low")).lower()

        return risk in HIGH_RISK
