# OpportunityShield
# Text Evidence Analyzer v1.1

import re


class TextAnalyzer:

    def __init__(self):

        # -----------------------------------------------------
        # Financial indicators
        # -----------------------------------------------------

        self.payment_keywords = [
            "pay",
            "payment",
            "fee",
            "registration fee",
            "security deposit",
            "processing fee",
            "verification fee",
            "training fee",
            "application fee",
            "deposit"
        ]

        self.upi_keywords = [
            "upi",
            "upi id",
            "bank account",
            "bank transfer",
            "account number"
        ]

        # -----------------------------------------------------
        # Sensitive information
        # -----------------------------------------------------

        self.sensitive_data_keywords = [
            "aadhaar",
            "aadhar",
            "pan card",
            "pan number",
            "bank details",
            "bank account",
            "otp",
            "one time password",
            "password",
            "cvv",
            "card number",
            "debit card",
            "credit card"
        ]

        # -----------------------------------------------------
        # Urgency / pressure
        # -----------------------------------------------------

        self.strong_urgency_keywords = [
            "within 30 minutes",
            "within 1 hour",
            "within one hour",
            "pay immediately",
            "pay now",
            "immediately",
            "urgent",
            "today only",
            "last chance",
            "act now"
        ]

        self.mild_urgency_keywords = [
            "apply before",
            "deadline",
            "applications close",
            "apply by",
            "closing date"
        ]

        # -----------------------------------------------------
        # Scarcity
        # -----------------------------------------------------

        self.scarcity_keywords = [
            "limited seats",
            "limited slots",
            "only 2 seats",
            "only 5 seats",
            "few seats",
            "few positions",
            "limited positions",
            "only a few"
        ]

        # -----------------------------------------------------
        # Threat / consequence
        # -----------------------------------------------------

        self.threat_keywords = [
            "selection will be cancelled",
            "offer will be cancelled",
            "account will be blocked",
            "lose your seat",
            "lose your selection",
            "application will be rejected",
            "failure to pay"
        ]

        # -----------------------------------------------------
        # Reward exaggeration
        # -----------------------------------------------------

        self.exaggerated_reward_keywords = [
            "guaranteed job",
            "guaranteed placement",
            "guaranteed salary",
            "earn ₹",
            "earn rs",
            "no interview",
            "instant selection",
            "selected without interview"
        ]

        # -----------------------------------------------------
        # Authority pressure
        # -----------------------------------------------------

        self.authority_keywords = [
            "government approved",
            "government supported",
            "official government",
            "government certified",
            "ministry approved",
            "official certification"
        ]

        # -----------------------------------------------------
        # Secrecy
        # -----------------------------------------------------

        self.secrecy_keywords = [
            "don't tell anyone",
            "do not tell anyone",
            "keep this confidential",
            "keep this secret",
            "don't inform your college",
            "do not inform your college",
            "confidential"
        ]

        # -----------------------------------------------------
        # Email pattern
        # -----------------------------------------------------

        self.email_pattern = (
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        )

        # -----------------------------------------------------
        # URL pattern
        # -----------------------------------------------------

        self.url_pattern = r'https?://[^\s]+|www\.[^\s]+'


    # =========================================================
    # Helper: find keywords
    # =========================================================

    def find_keywords(self, text, keywords):

        text_lower = text.lower()

        found = []

        for keyword in keywords:

            if keyword.lower() in text_lower:
                found.append(keyword)

        return found


# =========================================================
    # Helper: detect whether a keyword is explicitly negated
    # =========================================================

    def is_negated(self, text, keyword):

        text_lower = text.lower()
        keyword_lower = keyword.lower()

        # -----------------------------------------------------
        # IMPORTANT:
        # Do NOT split on newline.
        #
        # A visual line break can separate:
        # "applicants are not"
        # "asked to provide OTPs"
        #
        # but semantically these are the same sentence.
        # -----------------------------------------------------

        clauses = re.split(r'[.!?;]+', text_lower)

        # Support plural forms:
        # otp -> otp / otps
        # password -> password / passwords
        # card -> card / cards

        keyword_pattern = (
            r'\b'
            + re.escape(keyword_lower)
            + r's?\b'
        )

        for clause in clauses:

            clause = clause.strip()

            if keyword_lower not in clause:
                continue

            # -------------------------------------------------
            # Pattern 1:
            #
            # "not asked to provide OTP"
            # "not requested to provide password"
            # "not required to provide card number"
            # -------------------------------------------------

            negative_request_patterns = [

                rf'\b(?:not|never)\b'
                rf'[^.?!;]{{0,60}}'
                rf'\b(?:asked|requested|required|needed)\b'
                rf'[^.?!;]{{0,40}}'
                rf'\b(?:provide|share|submit|give|send|enter)\b'
                rf'[^.?!;]{{0,30}}'
                rf'{keyword_pattern}',

                # "do not provide OTP"
                # "don't share password"
                rf'\b(?:do not|don\'t|does not|doesn\'t|never)\b'
                rf'[^.?!;]{{0,50}}'
                rf'\b(?:provide|share|submit|give|send|enter)\b'
                rf'[^.?!;]{{0,30}}'
                rf'{keyword_pattern}',

                # "no need to provide OTP"
                rf'\bno need to\b'
                rf'[^.?!;]{{0,40}}'
                rf'\b(?:provide|share|submit|give|send|enter)\b'
                rf'[^.?!;]{{0,30}}'
                rf'{keyword_pattern}',

                # "without providing OTP"
                rf'\bwithout\b'
                rf'[^.?!;]{{0,40}}'
                rf'\b(?:providing|sharing|submitting|giving|sending|entering)\b'
                rf'[^.?!;]{{0,30}}'
                rf'{keyword_pattern}',
            ]

            for pattern in negative_request_patterns:

                if re.search(pattern, clause):

                    return True

            # -------------------------------------------------
            # Pattern 2:
            #
            # "no OTP"
            # "not OTP"
            # "without OTP"
            # -------------------------------------------------

            direct_before_pattern = (
                r'\b(?:no|not|never|without|don\'t|do not|'
                r'doesn\'t|does not|isn\'t|is not|aren\'t|'
                r'are not|wasn\'t|was not|were not|'
                r'will not|won\'t)\b'
                r'[^.?!;]{0,40}'
                + keyword_pattern
            )

            if re.search(
                direct_before_pattern,
                clause
            ):

                return True

            # -------------------------------------------------
            # Pattern 3:
            #
            # "OTP is not required"
            # "password not requested"
            # "card number is not needed"
            # -------------------------------------------------

            after_pattern = (
                keyword_pattern
                + r'[^.?!;]{0,40}\b'
                + r'(?:is not|are not|was not|were not|'
                r'isn\'t|aren\'t|wasn\'t|weren\'t|'
                r'not required|not requested|not needed|'
                r'not provided)\b'
            )

            if re.search(
                after_pattern,
                clause
            ):

                return True

        return False


    # =========================================================
    # Analyze financial indicators
    # =========================================================

    def analyze_financial(self, text):

        text_lower = text.lower()

        # -----------------------------------------------------
        # Detect payment-related terms
        # -----------------------------------------------------

        payment_found = self.find_keywords(
            text,
            self.payment_keywords
        )

        upi_found = self.find_keywords(
            text,
            self.upi_keywords
        )

        # -----------------------------------------------------
        # Explicitly negative payment statements
        # -----------------------------------------------------

        negative_payment_phrases = [
            "no payment",
            "no fee",
            "no registration fee",
            "no application fee",
            "no verification fee",
            "no security deposit",
            "no processing fee",
            "no training fee",
            "no deposit",
            "without payment",
            "without any payment",
            "without registration fee",
            "without any fee",
            "free of charge",
            "no payment is required",
            "no payment required",
            "no fee is required",
            "no fee required",
            "payment is not required",
            "payment not required",
            "fee is not required",
            "fee not required",
            "not required to pay",
            "not required to make a payment",
            "not required to make any payment",
            "does not require payment",
            "does not require any payment",
            "do not require payment",
            "do not require any payment",
            "doesn't require payment",
            "doesn't require any payment",
            "no registration payment",
            "no application payment",
            "no verification payment",
            "no security deposit is required",
            "no processing payment",
            "no training payment"
        ]

        fee_explicitly_negated = any(
            phrase in text_lower
            for phrase in negative_payment_phrases
        )

        # -----------------------------------------------------
        # Actual fee request
        # -----------------------------------------------------

        fee_phrases = [
            "registration fee",
            "application fee",
            "verification fee",
            "security deposit",
            "processing fee",
            "training fee"
        ]

        registration_fee = any(
            phrase in text_lower
            for phrase in fee_phrases
        )

        # A clearly negated payment statement overrides
        # simple keyword detection.
        if fee_explicitly_negated:
            registration_fee = False

        # -----------------------------------------------------
        # Personal payment account
        # -----------------------------------------------------

        personal_payment_account = any(
            keyword in text_lower
            for keyword in [
                "personal upi",
                "personal account",
                "hr's upi",
                "hr upi",
                "send to my upi"
            ]
        )

        # -----------------------------------------------------
        # Urgent payment
        # -----------------------------------------------------

        urgent_payment = (
            any(
                keyword in text_lower
                for keyword in self.strong_urgency_keywords
            )
            and not fee_explicitly_negated
            and len(payment_found) > 0
        )

        # -----------------------------------------------------
        # Unclear payment requirement
        # -----------------------------------------------------

        unclear_fee = (
            len(payment_found) > 0
            and not registration_fee
            and not fee_explicitly_negated
        )

        # -----------------------------------------------------
        # Refund claims
        # -----------------------------------------------------

        unverified_refund_claim = any(
            keyword in text_lower
            for keyword in [
                "refundable",
                "will be refunded",
                "refund after joining"
            ]
        )

        return {
            "unclear_fee": unclear_fee,
            "registration_fee": registration_fee,
            "personal_payment_account": personal_payment_account,
            "urgent_payment": urgent_payment,
            "unverified_refund_claim": unverified_refund_claim
        }


    # =========================================================
    # Analyze sensitive data
    # =========================================================

    def analyze_sensitive_data(self, text):

        sensitive_requests = []

        sensitive_keywords = [
            "otp",
            "one time password",
            "password",
            "cvv",
            "card number",
            "debit card",
            "credit card"
        ]

        for keyword in sensitive_keywords:

            if keyword in text.lower():

                if not self.is_negated(text, keyword):
                    sensitive_requests.append(keyword)

        otp_or_password = any(
            keyword in sensitive_requests
            for keyword in [
                "otp",
                "one time password",
                "password"
            ]
        )

        card_credentials = any(
            keyword in sensitive_requests
            for keyword in [
                "cvv",
                "card number",
                "debit card",
                "credit card"
            ]
        )

        bank_information = (
            (
                "bank details" in text.lower()
                or "bank account" in text.lower()
                or "account number" in text.lower()
            )
            and not (
                self.is_negated(text, "bank details")
                or self.is_negated(text, "bank account")
                or self.is_negated(text, "account number")
            )
        )

        sensitive_id = (
            (
                "aadhaar" in text.lower()
                or "aadhar" in text.lower()
                or "pan card" in text.lower()
                or "pan number" in text.lower()
            )
            and not (
                self.is_negated(text, "aadhaar")
                or self.is_negated(text, "aadhar")
                or self.is_negated(text, "pan card")
                or self.is_negated(text, "pan number")
            )
        )

        return {
            "sensitive_id_before_verification": sensitive_id,
            "bank_information": bank_information,
            "otp_or_password": otp_or_password,
            "card_credentials": card_credentials,
            "excessive_data_request": False
        }


    # =========================================================
    # Analyze psychological pressure
    # =========================================================

    def analyze_pressure(self, text):

        strong_urgency = self.find_keywords(
            text,
            self.strong_urgency_keywords
        )

        mild_urgency = self.find_keywords(
            text,
            self.mild_urgency_keywords
        )

        scarcity = self.find_keywords(
            text,
            self.scarcity_keywords
        )

        threat = self.find_keywords(
            text,
            self.threat_keywords
        )

        exaggerated_reward = self.find_keywords(
            text,
            self.exaggerated_reward_keywords
        )

        authority_pressure = self.find_keywords(
            text,
            self.authority_keywords
        )

        secrecy = self.find_keywords(
            text,
            self.secrecy_keywords
        )

        pressure_count = (
            len(strong_urgency)
            + len(scarcity)
            + len(threat)
            + len(exaggerated_reward)
            + len(authority_pressure)
            + len(secrecy)
        )

        multiple_pressure_methods = pressure_count >= 3

        return {
            "mild_urgency": len(mild_urgency) > 0,
            "strong_urgency": len(strong_urgency) > 0,
            "scarcity": len(scarcity) > 0,
            "threat": len(threat) > 0,
            "exaggerated_reward": len(exaggerated_reward) > 0,
            "authority_pressure": len(authority_pressure) > 0,
            "secrecy": len(secrecy) > 0,
            "multiple_pressure_methods": multiple_pressure_methods
        }


    # =========================================================
    # Extract emails
    # =========================================================

    def extract_emails(self, text):

        return re.findall(
            self.email_pattern,
            text
        )


    # =========================================================
    # Extract URLs
    # =========================================================

    def extract_urls(self, text):

        return re.findall(
            self.url_pattern,
            text
        )


    # =========================================================
    # Main analysis function
    # =========================================================

    def analyze(self, text):

        financial = self.analyze_financial(text)

        sensitive_data = self.analyze_sensitive_data(text)

        pressure = self.analyze_pressure(text)

        emails = self.extract_emails(text)

        urls = self.extract_urls(text)

        return {
            "financial": financial,
            "sensitive_data": sensitive_data,
            "psychological_pressure": pressure,
            "extracted_emails": emails,
            "extracted_urls": urls
        }