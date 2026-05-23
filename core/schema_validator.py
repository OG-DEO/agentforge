class SchemaValidator:
    def require_fields(
        self,
        payload,
        required_fields
    ):
        missing = []

        for field in required_fields:
            if field not in payload:
                missing.append(field)

        if missing:
            raise RuntimeError(
                f"Missing required fields: {missing}"
            )

        return True

    def require_enum(
        self,
        payload,
        field,
        allowed
    ):
        value = payload.get(field)

        if value not in allowed:
            raise RuntimeError(
                f"Invalid value for '{field}': "
                f"{value} | allowed={allowed}"
            )

        return True
