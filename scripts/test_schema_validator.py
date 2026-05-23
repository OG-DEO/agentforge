from core.schema_validator import SchemaValidator

validator = SchemaValidator()

payload = {
    "merge_recommendation": "approve",
    "rollback_risk": "low",
}

validator.require_fields(
    payload,
    [
        "merge_recommendation",
        "rollback_risk",
    ]
)

validator.require_enum(
    payload,
    "merge_recommendation",
    [
        "approve",
        "review",
        "reject",
    ]
)

validator.require_enum(
    payload,
    "rollback_risk",
    [
        "low",
        "medium",
        "high",
    ]
)

print("\nSchema validation passed.")
