class ApplyDecisionStage:
    def run(self, semantic_review):
        risk = semantic_review.get(
            "risk_level",
            "high"
        ).lower()

        quality = semantic_review.get(
            "quality_status",
            ""
        ).lower()

        safe_to_apply = (
            risk == "low"
            and "approved" in quality
        )

        return {
            "safe_to_apply": safe_to_apply,
            "risk": risk,
            "quality": quality,
        }
