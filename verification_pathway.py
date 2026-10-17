# OpportunityShield
# Verification Pathway Generator v1.0


class VerificationPathway:

    def __init__(self):
        pass

    # =========================================================
    # Generate verification actions
    # =========================================================

    def generate(self, analysis):

        actions = []
        priority = []

        critical_flags = analysis.get(
            "critical_flags", []
        )

        dimensions = analysis.get(
            "dimensions", {}
        )

        # -----------------------------------------------------
        # CRITICAL INDICATORS
        # -----------------------------------------------------

        if "otp_or_password" in critical_flags:

            actions.append(
                "Do not share OTPs, passwords, or authentication codes."
            )

            priority.append(
                "Protect account credentials"
            )

        if "card_credentials" in critical_flags:

            actions.append(
                "Do not provide card number, CVV, PIN, or other card credentials."
            )

            priority.append(
                "Protect payment credentials"
            )

        if "lookalike_domain" in critical_flags:

            actions.append(
                "Do not use the provided link. Independently open the organization's official website."
            )

            priority.append(
                "Verify website domain"
            )

        if "official_contradiction" in critical_flags:

            actions.append(
                "Treat the official contradiction as unresolved until independently verified."
            )

            priority.append(
                "Resolve official contradiction"
            )

        if "major_contradiction" in critical_flags:

            actions.append(
                "Do not proceed until the conflicting evidence is resolved."
            )

            priority.append(
                "Resolve evidence conflict"
            )

        # -----------------------------------------------------
        # ORGANIZATION IDENTITY
        # -----------------------------------------------------

        organization_risk = dimensions.get(
            "organization_identity", {}
        )

        if organization_risk.get("triggered_rules"):

            actions.append(
                "Verify the organization's identity using an independently accessed official source."
            )

            priority.append(
                "Verify organization identity"
            )

        # -----------------------------------------------------
        # OPPORTUNITY AUTHENTICITY
        # -----------------------------------------------------

        opportunity_risk = dimensions.get(
            "opportunity_authenticity", {}
        )

        if opportunity_risk.get("triggered_rules"):

            actions.append(
                "Search for the exact opportunity on the organization's official website or verified opportunity portal."
            )

            priority.append(
                "Verify opportunity authenticity"
            )

        # -----------------------------------------------------
        # COMMUNICATION CHANNEL
        # -----------------------------------------------------

        communication_risk = dimensions.get(
            "communication_channel", {}
        )

        if communication_risk.get("triggered_rules"):

            actions.append(
                "Verify the recruiter's email, contact details, and application channel through an independent official source."
            )

            priority.append(
                "Verify communication channel"
            )

        # -----------------------------------------------------
        # FINANCIAL RISK
        # -----------------------------------------------------

        financial_risk = dimensions.get(
            "financial", {}
        )

        if financial_risk.get("triggered_rules"):

            actions.append(
                "Do not make a payment until the opportunity, organization, and payment recipient are independently verified."
            )

            priority.append(
                "Verify payment requirement"
            )

        # -----------------------------------------------------
        # SENSITIVE DATA
        # -----------------------------------------------------

        data_risk = dimensions.get(
            "sensitive_data", {}
        )

        if data_risk.get("triggered_rules"):

            actions.append(
                "Do not submit identity, banking, card, or other sensitive information until authenticity is established."
            )

            priority.append(
                "Protect sensitive information"
            )

        # -----------------------------------------------------
        # PSYCHOLOGICAL PRESSURE
        # -----------------------------------------------------

        pressure_risk = dimensions.get(
            "psychological_pressure", {}
        )

        if pressure_risk.get("triggered_rules"):

            actions.append(
                "Ignore urgency or scarcity pressure and independently verify the opportunity before acting."
            )

            priority.append(
                "Pause before acting"
            )

        # -----------------------------------------------------
        # EVIDENCE CONSISTENCY
        # -----------------------------------------------------

        consistency_risk = dimensions.get(
            "evidence_consistency", {}
        )

        if consistency_risk.get("triggered_rules"):

            actions.append(
                "Compare the organization, opportunity, contact, URL, and offer details for consistency."
            )

            priority.append(
                "Resolve evidence consistency"
            )

        # -----------------------------------------------------
        # DEFAULT PATH
        # -----------------------------------------------------

        if not actions:

            actions.append(
                "No significant risk indicators were detected. Continue normal verification practices before submitting sensitive information."
            )

            priority.append(
                "Routine verification"
            )

        # -----------------------------------------------------
        # REMOVE DUPLICATES
        # -----------------------------------------------------

        actions = list(dict.fromkeys(actions))
        priority = list(dict.fromkeys(priority))

        # -----------------------------------------------------
        # FINAL RESULT
        # -----------------------------------------------------

        return {

            "priority_checks": priority,

            "recommended_actions": actions,

            "action_count": len(actions)

        }