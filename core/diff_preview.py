def render_patch_preview(patch):
    lines = []

    lines.append("=== PATCH PREVIEW ===")
    lines.append("")

    lines.append(f"Summary: {patch.get('summary')}")
    lines.append(f"Risk Level: {patch.get('risk_level')}")
    lines.append(
        f"Requires Approval: {patch.get('requires_approval')}"
    )

    lines.append("")
    lines.append("Target Files:")

    for item in patch.get("target_files", []):
        lines.append(f"  - {item}")

    lines.append("")
    lines.append("Operations:")

    for item in patch.get("operations", []):
        lines.append(f"  - {item}")

    return "\n".join(lines)
