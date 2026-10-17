# OpportunityShield
# Verification Layer v1.0

import re


class VerificationLayer:

    def __init__(self):

        # Common free email providers.
        # These are NOT automatically fraudulent.
        self.free_email_domains = {
            "gmail.com",
            "yahoo.com",
            "outlook.com",
            "hotmail.com",
            "rediffmail.com"
        }

    # =========================================================
    # Extract email domain
    # =========================================================

    def get_email_domain(self, email):

        if "@" not in email:
            return None

        return email.split("@")[-1].lower().strip()

    # =========================================================
    # Normalize a domain
    # =========================================================

    def normalize_domain(self, domain):

        if not domain:
            return None

        domain = domain.lower().strip()

        # Remove protocol
        domain = re.sub(r"^https?://", "", domain)

        # Remove www.
        domain = re.sub(r"^www\.", "", domain)

        # Remove anything after /
        domain = domain.split("/")[0]

        return domain

    # =========================================================
    # Check whether two domains match
    # =========================================================

    def domains_match(self, domain1, domain2):

        domain1 = self.normalize_domain(domain1)
        domain2 = self.normalize_domain(domain2)

        if not domain1 or not domain2:
            return False

        return domain1 == domain2

    # =========================================================
    # Check whether email uses a free provider
    # =========================================================

    def is_free_email(self, email):

        domain = self.get_email_domain(email)

        if not domain:
            return False

        return domain in self.free_email_domains

    # =========================================================
    # Calculate simple domain similarity
    # =========================================================

    def domain_similarity(self, domain1, domain2):

        domain1 = self.normalize_domain(domain1)
        domain2 = self.normalize_domain(domain2)

        if not domain1 or not domain2:
            return 0

        if domain1 == domain2:
            return 1.0

        # Remove common TLDs for simple comparison
        base1 = domain1.split(".")[0]
        base2 = domain2.split(".")[0]

        if base1 == base2:
            return 0.8

        # Simple character overlap
        common = set(base1) & set(base2)

        if len(base1) == 0 or len(base2) == 0:
            return 0

        similarity = (
            2 * len(common)
            / (len(set(base1)) + len(set(base2)))
        )

        return round(similarity, 2)

    # =========================================================
    # Analyze email against claimed official domain
    # =========================================================

    def verify_email(self, email, official_domain):

        email_domain = self.get_email_domain(email)

        official_domain = self.normalize_domain(
            official_domain
        )

        if not email_domain:
            return {
                "status": "UNVERIFIED",
                "reason": "Invalid or missing email address."
            }

        if not official_domain:
            return {
                "status": "UNVERIFIED",
                "reason": "Official organization domain was not provided."
            }

        # Exact match
        if self.domains_match(
            email_domain,
            official_domain
        ):
            return {
                "status": "SUPPORTED",
                "reason": "Email domain matches the claimed official domain.",
                "email_domain": email_domain
            }

        # Free provider
        if self.is_free_email(email):

            return {
                "status": "UNVERIFIED",
                "reason": (
                    "Email uses a public email provider. "
                    "This does not prove fraud, but the recruiter "
                    "identity requires independent verification."
                ),
                "email_domain": email_domain
            }

        # Different organizational domain
        similarity = self.domain_similarity(
            email_domain,
            official_domain
        )

        if similarity >= 0.5:

            return {
                "status": "CONTRADICTED",
                "reason": (
                    "Email domain resembles the claimed organization "
                    "but does not match its official domain."
                ),
                "email_domain": email_domain,
                "similarity": similarity
            }

        return {
            "status": "CONTRADICTED",
            "reason": (
                "Email domain does not match the claimed "
                "official organization domain."
            ),
            "email_domain": email_domain,
            "similarity": similarity
        }

    # =========================================================
    # Analyze application URL
    # =========================================================

    def verify_url(self, url, official_domain):

        if not url:
            return {
                "status": "UNVERIFIED",
                "reason": "No application URL provided."
            }

        url_domain = self.normalize_domain(url)

        official_domain = self.normalize_domain(
            official_domain
        )

        if not url_domain or not official_domain:

            return {
                "status": "UNVERIFIED",
                "reason": "Unable to determine URL domain."
            }

        if self.domains_match(
            url_domain,
            official_domain
        ):

            return {
                "status": "SUPPORTED",
                "reason": "Application URL matches the official domain.",
                "url_domain": url_domain
            }

        similarity = self.domain_similarity(
            url_domain,
            official_domain
        )

        if similarity >= 0.5:

            return {
                "status": "CONTRADICTED",
                "reason": (
                    "Application domain resembles the official "
                    "domain but does not match it."
                ),
                "url_domain": url_domain,
                "similarity": similarity
            }

        return {
            "status": "CONTRADICTED",
            "reason": (
                "Application URL does not match the "
                "claimed official organization domain."
            ),
            "url_domain": url_domain,
            "similarity": similarity
        }

    # =========================================================
    # Complete verification
    # =========================================================

    def verify(
        self,
        organization_domain=None,
        recruiter_email=None,
        application_url=None,
        opportunity_found_officially=None,
        opportunity_details_match=None
    ):

        evidence = {}

        # -----------------------------------------------------
        # Email verification
        # -----------------------------------------------------

        if recruiter_email:

            email_result = self.verify_email(
                recruiter_email,
                organization_domain
            )

            evidence["email_verification"] = email_result

        # -----------------------------------------------------
        # URL verification
        # -----------------------------------------------------

        if application_url:

            url_result = self.verify_url(
                application_url,
                organization_domain
            )

            evidence["url_verification"] = url_result

        # -----------------------------------------------------
        # Opportunity verification
        # -----------------------------------------------------

        if opportunity_found_officially is True:

            evidence["opportunity_verification"] = {
                "status": "SUPPORTED",
                "reason": (
                    "The specific opportunity was independently "
                    "located on the official source."
                )
            }

        elif opportunity_found_officially is False:

            evidence["opportunity_verification"] = {
                "status": "UNVERIFIED",
                "reason": (
                    "The specific opportunity could not be "
                    "verified through the official source."
                )
            }

        else:

            evidence["opportunity_verification"] = {
                "status": "UNVERIFIED",
                "reason": (
                    "No independent opportunity verification "
                    "evidence was supplied."
                )
            }

        # -----------------------------------------------------
        # Opportunity detail consistency
        # -----------------------------------------------------

        if opportunity_details_match is True:

            evidence["details_consistency"] = {
                "status": "SUPPORTED",
                "reason": (
                    "Opportunity details are consistent "
                    "with the verified listing."
                )
            }

        elif opportunity_details_match is False:

            evidence["details_consistency"] = {
                "status": "CONTRADICTED",
                "reason": (
                    "Opportunity details conflict with "
                    "the verified listing."
                )
            }

        else:

            evidence["details_consistency"] = {
                "status": "UNVERIFIED",
                "reason": (
                    "Opportunity details could not "
                    "be independently compared."
                )
            }

        return evidence