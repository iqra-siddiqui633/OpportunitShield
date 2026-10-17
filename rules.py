# OpportunityShield
# Risk-Factor Taxonomy v1.0

RISK_RULES = {

    "organization_identity": {
        "name": "Organization Identity Risk",
        "max_score": 3,
        "rules": {
            "organization_unverified": 2,
            "domain_mismatch": 3,
            "contact_mismatch": 3,
            "independent_presence_unverified": 1,
            "lookalike_domain": 3
        }
    },

    "opportunity_authenticity": {
        "name": "Opportunity Authenticity Risk",
        "max_score": 4,
        "rules": {
            "opportunity_not_found": 2,
            "opportunity_details_mismatch": 3,
            "reference_unverified": 1,
            "official_contradiction": 4
        }
    },

    "communication_channel": {
        "name": "Communication Channel Risk",
        "max_score": 3,
        "rules": {
            "unofficial_email": 2,
            "recruiter_unverified": 2,
            "application_url_mismatch": 3,
            "lookalike_domain": 3,
            "contact_conflict": 3
        }
    },

    "financial": {
        "name": "Financial Risk",
        "max_score": 4,
        "rules": {
            "unclear_fee": 2,
            "registration_fee": 3,
            "personal_payment_account": 3,
            "urgent_payment": 2,
            "unverified_refund_claim": 2
        }
    },

    "sensitive_data": {
        "name": "Sensitive Data Risk",
        "max_score": 4,
        "rules": {
            "sensitive_id_before_verification": 2,
            "bank_information": 3,
            "otp_or_password": 4,
            "card_credentials": 4,
            "excessive_data_request": 2
        }
    },

    "psychological_pressure": {
        "name": "Psychological Pressure Risk",
        "max_score": 3,
        "rules": {
            "mild_urgency": 1,
            "strong_urgency": 2,
            "scarcity": 2,
            "threat": 3,
            "exaggerated_reward": 2,
            "authority_pressure": 2,
            "secrecy": 3,
            "multiple_pressure_methods": 0
        }
    },

    "evidence_consistency": {
        "name": "Evidence Consistency Risk",
        "max_score": 3,
        "rules": {
            "minor_inconsistency": 1,
            "multiple_inconsistencies": 0,
            "evidence_chain_unverified": 2,
            "major_contradiction": 3
        }
    }
}


# Critical indicators
# These should force additional verification
# regardless of the normal numerical score.

CRITICAL_INDICATORS = {
    "otp_or_password",
    "card_credentials",
    "official_contradiction",
    "lookalike_domain",
    "major_contradiction"
}


# Initial decision thresholds.
# These are provisional and will be calibrated later
# using our evaluation dataset.

DECISION_THRESHOLDS = {
    "low_max": 2,
    "verify_max": 10
}