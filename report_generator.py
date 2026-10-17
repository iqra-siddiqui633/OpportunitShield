# OpportunityShield
# Evidence-Based Report Generator v1.0


class ReportGenerator:

    def __init__(self):
        pass

    # =========================================================
    # Generate complete report
    # =========================================================

    def generate_report(self, analysis):

        risk_analysis = analysis["risk_analysis"]
        verification = analysis["verification"]

        report = {
            "recommendation": risk_analysis["recommendation"],
            "risk_score": risk_analysis["total_score"],
            "critical_flags": risk_analysis["critical_flags"],
            "risk_dimensions": [],
            "verification_evidence": [],
            "recommended_actions": []
        }

        # -----------------------------------------------------
        # STEP 1 — Risk dimensions
        # -----------------------------------------------------

        for dimension, data in risk_analysis[
            "dimensions"
        ].items():

            dimension_report = {
                "dimension": data["name"],
                "score": data["score"],
                "max_score": data["max_score"],
                "triggered_rules": []
            }

            for rule in data["triggered_rules"]:

                dimension_report[
                    "triggered_rules"
                ].append({
                    "rule": rule["rule"],
                    "score": rule["score"]
                })

            report[
                "risk_dimensions"
            ].append(dimension_report)

        # -----------------------------------------------------
        # STEP 2 — Verification evidence
        # -----------------------------------------------------

        for verification_name, result in verification.items():

            if not isinstance(result, dict):
                continue

            status = result.get("status")

            reason = result.get("reason")

            if status:

                report[
                    "verification_evidence"
                ].append({
                    "check": verification_name,
                    "status": status,
                    "reason": reason
                })

        # -----------------------------------------------------
        # STEP 3 — Recommended actions
        # -----------------------------------------------------

        recommendation = risk_analysis[
            "recommendation"
        ]

        if recommendation == "PROCEED":

            report[
                "recommended_actions"
            ] = [
                "Opportunity shows no major risk indicators.",
                "Proceed while maintaining normal verification."
            ]

        elif recommendation == "VERIFY":

            report[
                "recommended_actions"
            ] = [
                "Verify the opportunity through an official source.",
                "Do not make payment until verification is complete.",
                "Do not share sensitive information unnecessarily."
            ]

        elif recommendation == "AVOID":

            report[
                "recommended_actions"
            ] = [
                "Do not proceed with the opportunity.",
                "Do not make any payment.",
                "Do not share sensitive information.",
                "Verify the organization through its official channel."
            ]

        return report

    # =========================================================
    # Convert report to readable text
    # =========================================================

    def format_report(self, report):

        lines = []

        lines.append(
            "========================================"
        )

        lines.append(
            "       OPPORTUNITYSHIELD REPORT"
        )

        lines.append(
            "========================================"
        )

        lines.append("")

        lines.append(
            "Recommendation: "
            + report["recommendation"]
        )

        lines.append(
            "Risk Score: "
            + str(report["risk_score"])
        )

        lines.append("")

        # -----------------------------------------------------
        # Critical indicators
        # -----------------------------------------------------

        if report["critical_flags"]:

            lines.append(
                "CRITICAL INDICATORS"
            )

            for flag in report["critical_flags"]:

                lines.append(
                    "- " + flag
                )

            lines.append("")

        # -----------------------------------------------------
        # Risk dimensions
        # -----------------------------------------------------

        lines.append(
            "RISK DIMENSIONS"
        )

        for dimension in report[
            "risk_dimensions"
        ]:

            lines.append(
                f"\n{dimension['dimension']}: "
                f"{dimension['score']}/"
                f"{dimension['max_score']}"
            )

            for rule in dimension[
                "triggered_rules"
            ]:

                lines.append(
                    f"  - {rule['rule']} "
                    f"(+{rule['score']})"
                )

        lines.append("")

        # -----------------------------------------------------
        # Verification evidence
        # -----------------------------------------------------

        lines.append(
            "VERIFICATION EVIDENCE"
        )

        for evidence in report[
            "verification_evidence"
        ]:

            lines.append(
                f"\n{evidence['check']}: "
                f"{evidence['status']}"
            )

            if evidence["reason"]:

                lines.append(
                    "  "
                    + str(evidence["reason"])
                )

        lines.append("")

        # -----------------------------------------------------
        # Recommended actions
        # -----------------------------------------------------

        lines.append(
            "RECOMMENDED ACTIONS"
        )

        for action in report[
            "recommended_actions"
        ]:

            lines.append(
                "- " + action
            )

        lines.append("")

        lines.append(
            "========================================"
        )

        return "\n".join(lines)