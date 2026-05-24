ALLOWED_TRANSITIONS = {
    "executing": ["awaiting_review", "rejected"],
    "awaiting_review": ["approved_for_apply", "rejected"],
    "approved_for_apply": ["merged", "archived"],
    "rejected": ["archived"],
    "merged": [],
    "archived": [],
}


class BranchStateMachine:
    def validate(self, current, new):
        if current is None:
            return True  # first-time set

        allowed = ALLOWED_TRANSITIONS.get(current, [])

        return new in allowed

    def enforce(self, current, new):
        if not self.validate(current, new):
            raise RuntimeError(
                f"Invalid transition: {current} -> {new}"
            )

        return True
