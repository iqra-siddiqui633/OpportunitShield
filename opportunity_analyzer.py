# OpportunityShield
# End-to-End Opportunity Analyzer v1.0


from text_analyzer import TextAnalyzer
from verification import VerificationLayer
from risk_engine import RiskEngine
from report_generator import ReportGenerator
from verification_pathway import VerificationPathway

class OpportunityAnalyzer:

    def __init__(self):

        self.text_analyzer = TextAnalyzer()
        self.verifier = VerificationLayer()
        self.risk_engine = RiskEngine()
        self.report_generator = ReportGenerator()
        self.pathway = VerificationPathway()
    # =========================================================
    # Analyze an opportunity
    # =========================================================

    def analyze(
        self,
        text,
        organization_domain=None,
        opportunity_found_officially=None,
        opportunity_details_match=None
    ):

        # -----------------------------------------------------
        # STEP 1 — Extract evidence from opportunity text
        # -----------------------------------------------------

        extracted = self.text_analyzer.analyze(text)

        # -----------------------------------------------------
        # STEP 2 — Get recruiter email
        # -----------------------------------------------------

        recruiter_email = None

        if extracted.get("extracted_emails"):

            recruiter_email = (
                extracted["extracted_emails"][0]
            )

        # -----------------------------------------------------
        # STEP 3 — Get application URL
        # -----------------------------------------------------

        application_url = None

        if extracted.get("extracted_urls"):

            application_url = (
                extracted["extracted_urls"][0]
            )

        # -----------------------------------------------------
        # STEP 4 — Verification layer
        # -----------------------------------------------------

        verification = self.verifier.verify(

            organization_domain=organization_domain,

            recruiter_email=recruiter_email,

            application_url=application_url,

            opportunity_found_officially=(
                opportunity_found_officially
            ),

            opportunity_details_match=(
                opportunity_details_match
            )
        )

        # -----------------------------------------------------
        # STEP 5 — Build evidence for Risk Engine
        # -----------------------------------------------------

        evidence = {

            "organization_identity": {},

            "opportunity_authenticity": {},

            "communication_channel": {},

            "financial": (
                extracted["financial"]
            ),

            "sensitive_data": (
                extracted["sensitive_data"]
            ),

            "psychological_pressure": (
                extracted["psychological_pressure"]
            ),

            "evidence_consistency": {}
        }

        # -----------------------------------------------------
        # STEP 5A — Communication evidence
        # -----------------------------------------------------

        email_verification = verification.get(
            "email_verification",
            {}
        )

        email_status = email_verification.get(
            "status"
        )

        if email_status == "UNVERIFIED":

            evidence[
                "communication_channel"
            ]["unofficial_email"] = True

            evidence[
                "communication_channel"
            ]["recruiter_unverified"] = True

        elif email_status == "CONTRADICTED":

            evidence[
                "communication_channel"
            ]["contact_conflict"] = True

        # -----------------------------------------------------
        # STEP 5B — URL evidence
        # -----------------------------------------------------

        url_verification = verification.get(
            "url_verification",
            {}
        )

        url_status = url_verification.get(
            "status"
        )

        if url_status == "CONTRADICTED":

            evidence[
                "communication_channel"
            ]["application_url_mismatch"] = True

        # -----------------------------------------------------
        # STEP 5C — Opportunity evidence
        # -----------------------------------------------------

        opportunity_result = verification.get(
            "opportunity_verification",
            {}
        )

        opportunity_status = opportunity_result.get(
            "status"
        )

        if opportunity_status == "UNVERIFIED":

            evidence[
                "opportunity_authenticity"
            ]["opportunity_not_found"] = True

            evidence[
                "evidence_consistency"
            ]["evidence_chain_unverified"] = True

        elif opportunity_status == "CONTRADICTED":

            evidence[
                "opportunity_authenticity"
            ]["official_contradiction"] = True

            evidence[
                "evidence_consistency"
            ]["major_contradiction"] = True

        # -----------------------------------------------------
        # STEP 5D — Opportunity detail consistency
        # -----------------------------------------------------

        details_result = verification.get(
            "details_consistency",
            {}
        )

        details_status = details_result.get(
            "status"
        )

        if details_status == "CONTRADICTED":

            evidence[
                "opportunity_authenticity"
            ]["opportunity_details_mismatch"] = True

            evidence[
                "evidence_consistency"
            ]["major_contradiction"] = True

        # -----------------------------------------------------
        # STEP 5E — Count contradictions
        # -----------------------------------------------------

        contradiction_count = 0

        for verification_result in verification.values():

            if isinstance(
                verification_result,
                dict
            ):

                if verification_result.get(
                    "status"
                ) == "CONTRADICTED":

                    contradiction_count += 1

        if contradiction_count >= 2:

            evidence[
                "evidence_consistency"
            ]["multiple_inconsistencies"] = True

        # -----------------------------------------------------
        # STEP 6 — Risk Engine
        # -----------------------------------------------------

        risk_result = self.risk_engine.analyze(
            evidence
        )

        verification_pathway = self.pathway.generate(
            risk_result)

        # -----------------------------------------------------
        # STEP 7 — Generate explanation
        # -----------------------------------------------------

        explanation = (
            self.risk_engine.generate_explanation(
                risk_result
            )
        )

        # -----------------------------------------------------
        # STEP 8 — Return complete analysis
        # -----------------------------------------------------
        
        report = self.report_generator.generate_report(
            {
                "risk_analysis": risk_result,

                "verification": verification
            }
        )

        return {

            "input_text": text,

            "extracted_evidence": extracted,

            "verification": verification,

            "risk_analysis": risk_result,

            "verification_pathway": verification_pathway,

            "explanation": self.risk_engine.generate_explanation(
                risk_result
            ),

            "report": report
        }