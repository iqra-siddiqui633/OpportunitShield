# OpportunityShield
# Risk Engine v1.0

from rules import (
    RISK_RULES,
    CRITICAL_INDICATORS,
    DECISION_THRESHOLDS
)


class RiskEngine:

    def __init__(self):
        self.results = {}

    # ---------------------------------------------------------
    # Calculate risk for one dimension
    # ---------------------------------------------------------

    def calculate_dimension(self, dimension, evidence):

        dimension_rules = RISK_RULES[dimension]["rules"]
        max_score = RISK_RULES[dimension]["max_score"]

        score = 0
        triggered_rules = []

        for rule_name, is_triggered in evidence.items():

            if is_triggered and rule_name in dimension_rules:

                rule_score = dimension_rules[rule_name]

                score += rule_score

                triggered_rules.append({
                    "rule": rule_name,
                    "score": rule_score
                })

        # Prevent the dimension from exceeding its maximum
        score = min(score, max_score)

        return {
            "name": RISK_RULES[dimension]["name"],
            "score": score,
            "max_score": max_score,
            "triggered_rules": triggered_rules
        }

    # ---------------------------------------------------------
    # Analyze complete opportunity
    # ---------------------------------------------------------

    def analyze(self, evidence):

        self.results = {}

        total_score = 0
        critical_flags = []

        # Calculate all seven dimensions
        for dimension in RISK_RULES:

            dimension_evidence = evidence.get(
                dimension,
                {}
            )

            result = self.calculate_dimension(
                dimension,
                dimension_evidence
            )

            self.results[dimension] = result

            total_score += result["score"]

        # -----------------------------------------------------
        # Check critical indicators
        # -----------------------------------------------------

        for indicator in sorted(CRITICAL_INDICATORS):

            for dimension_data in self.results.values():

                for rule in dimension_data["triggered_rules"]:

                    if rule["rule"] == indicator:
                        critical_flags.append(indicator)

        # Remove duplicates while keeping deterministic order
        critical_flags = sorted(set(critical_flags))

        # -----------------------------------------------------
        # Determine final recommendation
        # -----------------------------------------------------

        recommendation = self.get_recommendation(
            total_score,
            critical_flags
        )

        return {
            "total_score": total_score,
            "recommendation": recommendation,
            "critical_flags": critical_flags,
            "dimensions": self.results
        }

    # ---------------------------------------------------------
    # Determine recommendation
    # ---------------------------------------------------------

    def get_recommendation(self, score, critical_flags):

        # -----------------------------------------------------
        # Critical indicators require at least verification.
        # They do not automatically mean the opportunity
        # is fraudulent.
        # -----------------------------------------------------

        if critical_flags:

            if score > DECISION_THRESHOLDS["verify_max"]:
                return "AVOID"

            return "VERIFY"

        # -----------------------------------------------------
        # Normal scoring
        # -----------------------------------------------------

        if score <= DECISION_THRESHOLDS["low_max"]:
            return "PROCEED"

        elif score <= DECISION_THRESHOLDS["verify_max"]:
            return "VERIFY"

        else:
            return "AVOID"

    # ---------------------------------------------------------
    # Generate human-readable explanation
    # ---------------------------------------------------------

    def generate_explanation(self, analysis):

        explanation = []

        explanation.append(
            "Recommendation: "
            + analysis["recommendation"]
        )

        explanation.append(
            "Risk Score: "
            + str(analysis["total_score"])
        )

        # -----------------------------------------------------
        # Critical indicators
        # -----------------------------------------------------

        if analysis["critical_flags"]:

            explanation.append(
                "Critical Indicators: "
                + ", ".join(
                    analysis["critical_flags"]
                )
            )

        # -----------------------------------------------------
        # Dimension-by-dimension explanation
        # -----------------------------------------------------

        for dimension, data in analysis["dimensions"].items():

            if data["triggered_rules"]:

                explanation.append(
                    f"\n{data['name']}: "
                    f"{data['score']}/{data['max_score']}"
                )

                for rule in data["triggered_rules"]:

                    explanation.append(
                        f"- {rule['rule']} "
                        f"(+{rule['score']})"
                    )

        return "\n".join(explanation)