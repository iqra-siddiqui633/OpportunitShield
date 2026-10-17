# OpportunityShield
# Evaluation Dataset v1.0
#
# Ground truth is used ONLY for system evaluation.
# It must never be shown to participants in the later experiment.


CASES = [

    # =====================================================
    # GENUINE CASES — 11
    # =====================================================

    {
        "id": "G01",
        "category": "Internship",
        "type": "Genuine",
        "expected": "PROCEED",
        "organization_domain": "brightlabs.example",
        "opportunity_found_officially": True,
        "opportunity_details_match": True,
        "text": """
        BrightLabs Technologies is offering a software development
        internship for undergraduate students.

        The internship details and application process are available
        on the organization's official website.

        There is no registration fee or security deposit.
        Selected students will receive a completion certificate.
        """
    },

    {
        "id": "G02",
        "category": "Job",
        "type": "Genuine",
        "expected": "PROCEED",
        "organization_domain": "northstar.example",
        "opportunity_found_officially": True,
        "opportunity_details_match": True,
        "text": """
        NorthStar Systems is accepting applications for its junior
        software trainee position.

        Applications must be submitted through the official
        company website.

        There is no payment required from applicants.
        """
    },

    {
        "id": "G03",
        "category": "Scholarship",
        "type": "Genuine",
        "expected": "PROCEED",
        "organization_domain": "learnforward.example",
        "opportunity_found_officially": True,
        "opportunity_details_match": True,
        "text": """
        LearnForward Foundation has opened applications for its
        undergraduate education scholarship.

        Eligibility requirements, documents and application dates
        are published on the official website.

        Students are not required to pay any application fee.
        """
    },

    {
        "id": "G04",
        "category": "Internship",
        "type": "Genuine",
        "expected": "PROCEED",
        "organization_domain": "codebridge.example",
        "opportunity_found_officially": True,
        "opportunity_details_match": True,
        "text": """
        CodeBridge Labs is offering a six-week web development
        internship for college students.

        Applications close on 30 September 2026.

        The official application page contains the same internship
        description and eligibility requirements.
        """
    },

    {
        "id": "G05",
        "category": "Job",
        "type": "Genuine",
        "expected": "PROCEED",
        "organization_domain": "vertexdata.example",
        "opportunity_found_officially": True,
        "opportunity_details_match": True,
        "text": """
        VertexData is recruiting entry-level data analyst trainees.

        Candidates can apply through the official organization
        website.

        No registration payment is required and applicants are not
        asked to provide OTPs, passwords or card credentials.
        """
    },

    {
        "id": "G06",
        "category": "Scholarship",
        "type": "Genuine",
        "expected": "PROCEED",
        "organization_domain": "futurepath.example",
        "opportunity_found_officially": True,
        "opportunity_details_match": True,
        "text": """
        FuturePath Foundation offers a merit-based scholarship for
        undergraduate students.

        The scholarship requirements and application procedure are
        available through the official website.

        No payment is required to submit an application.
        """
    },

    {
        "id": "G07",
        "category": "Internship",
        "type": "Genuine",
        "expected": "PROCEED",
        "organization_domain": "techharbor.example",
        "opportunity_found_officially": True,
        "opportunity_details_match": True,
        "text": """
        TechHarbor is accepting applications for its student
        software engineering internship.

        The official listing contains the same duration,
        eligibility criteria and application procedure.

        Students may apply through the official website.
        """
    },

    {
        "id": "G08",
        "category": "Job",
        "type": "Genuine",
        "expected": "PROCEED",
        "organization_domain": "infocore.example",
        "opportunity_found_officially": True,
        "opportunity_details_match": True,
        "text": """
        InfoCore Solutions has published a graduate technology
        trainee position.

        The vacancy is listed on the organization's official
        careers page.

        Candidates complete the normal selection process and
        no registration fee is required.
        """
    },

    {
        "id": "G09",
        "category": "Scholarship",
        "type": "Genuine",
        "expected": "PROCEED",
        "organization_domain": "scholarbridge.example",
        "opportunity_found_officially": True,
        "opportunity_details_match": True,
        "text": """
        ScholarBridge Foundation has published its undergraduate
        scholarship program.

        The official website contains the eligibility conditions,
        required documents and application procedure.

        Applicants do not need to make any payment.
        """
    },

    {
        "id": "G10",
        "category": "Internship",
        "type": "Genuine",
        "expected": "PROCEED",
        "organization_domain": "digitalforge.example",
        "opportunity_found_officially": True,
        "opportunity_details_match": True,
        "text": """
        DigitalForge is offering a student internship in software
        testing.

        The internship description, duration and eligibility
        requirements match the official opportunity listing.

        Applications are submitted through the official website.
        """
    },

    {
        "id": "G11",
        "category": "Job",
        "type": "Genuine",
        "expected": "PROCEED",
        "organization_domain": "cloudmatrix.example",
        "opportunity_found_officially": True,
        "opportunity_details_match": True,
        "text": """
        CloudMatrix has opened applications for its graduate
        cloud support trainee position.

        The opportunity is independently available on the official
        careers page.

        No payment or sensitive authentication information is
        requested during application.
        """
    },


    # =====================================================
    # FRAUDULENT CASES — 11
    # =====================================================

    {
        "id": "F01",
        "category": "Internship",
        "type": "Fraudulent",
        "expected": "AVOID",
        "organization_domain": "brightlabs.example",
        "opportunity_found_officially": False,
        "opportunity_details_match": False,
        "text": """
        Congratulations! You have been selected for a guaranteed
        internship at BrightLabs.

        Pay a registration fee of ₹2999 within 30 minutes.
        Send the payment to hrselection@protonmail.com.

        You must provide your Aadhaar number, bank account details
        and OTP immediately.

        Only five seats remain. Failure to pay will cancel your
        selection.

        Application:
        https://brightlabs-selection.example/apply
        """
    },

    {
        "id": "F02",
        "category": "Job",
        "type": "Fraudulent",
        "expected": "AVOID",
        "organization_domain": "northstar.example",
        "opportunity_found_officially": False,
        "opportunity_details_match": False,
        "text": """
        NorthStar guaranteed job offer.

        Pay ₹1999 as a verification fee today only.
        Send your payment to a personal UPI account.

        Provide your password and OTP for verification.
        Your selection will be cancelled if payment is not made.

        Apply immediately at:
        https://northstar-careers-offer.example/apply
        """
    },

    {
        "id": "F03",
        "category": "Scholarship",
        "type": "Fraudulent",
        "expected": "AVOID",
        "organization_domain": "learnforward.example",
        "opportunity_found_officially": False,
        "opportunity_details_match": False,
        "text": """
        You have been selected for the LearnForward scholarship.

        Pay a refundable processing fee of ₹1500 immediately
        to confirm your scholarship.

        Send your bank details, card number and CVV.
        This is government approved and only a few seats remain.

        Application:
        https://learnforward-scholarship.example/claim
        """
    },

    {
        "id": "F04",
        "category": "Internship",
        "type": "Fraudulent",
        "expected": "AVOID",
        "organization_domain": "codebridge.example",
        "opportunity_found_officially": False,
        "opportunity_details_match": False,
        "text": """
        CodeBridge internship selected without interview.

        Pay a ₹2500 security deposit now.
        The amount will be refunded after joining.

        Do not tell your college about this special selection.
        Provide your OTP and debit card number for verification.

        Your offer will be cancelled if you do not act now.
        """
    },

    {
        "id": "F05",
        "category": "Job",
        "type": "Fraudulent",
        "expected": "AVOID",
        "organization_domain": "vertexdata.example",
        "opportunity_found_officially": False,
        "opportunity_details_match": False,
        "text": """
        VertexData has selected you for a guaranteed salary position.

        Pay an application fee immediately through UPI.
        Send your bank account number and password.

        Only two positions are remaining.
        Failure to pay will result in cancellation.

        https://vertexdata-job.example/apply
        """
    },

    {
        "id": "F06",
        "category": "Scholarship",
        "type": "Fraudulent",
        "expected": "AVOID",
        "organization_domain": "futurepath.example",
        "opportunity_found_officially": False,
        "opportunity_details_match": False,
        "text": """
        FuturePath government scholarship confirmation.

        Pay a ₹999 verification fee today.
        The fee is guaranteed to be refunded.

        Send your PAN number, OTP and CVV.
        Keep this confidential and do not inform your college.

        https://futurepath-scholarship.example/verify
        """
    },

    {
        "id": "F07",
        "category": "Internship",
        "type": "Fraudulent",
        "expected": "AVOID",
        "organization_domain": "techharbor.example",
        "opportunity_found_officially": False,
        "opportunity_details_match": False,
        "text": """
        TechHarbor internship offer.

        You have been selected without an interview.
        Pay ₹3000 training fee immediately.

        Send the payment to a personal account and provide
        your bank details and OTP.

        Only five seats remain.
        """
    },

    {
        "id": "F08",
        "category": "Job",
        "type": "Fraudulent",
        "expected": "AVOID",
        "organization_domain": "infocore.example",
        "opportunity_found_officially": False,
        "opportunity_details_match": False,
        "text": """
        Instant selection for InfoCore job.

        No interview is required.
        Pay ₹2000 registration fee within one hour.

        Send your card number and CVV.
        The offer will be cancelled if you delay.

        https://infocore-selection.example/apply
        """
    },

    {
        "id": "F09",
        "category": "Scholarship",
        "type": "Fraudulent",
        "expected": "AVOID",
        "organization_domain": "scholarbridge.example",
        "opportunity_found_officially": False,
        "opportunity_details_match": False,
        "text": """
        ScholarBridge scholarship selected students must pay
        a processing fee of ₹1200.

        Pay immediately to secure your seat.
        Send your Aadhaar number, bank account and OTP.

        Only a few seats remain.
        Do not tell anyone about this offer.
        """
    },

    {
        "id": "F10",
        "category": "Internship",
        "type": "Fraudulent",
        "expected": "AVOID",
        "organization_domain": "digitalforge.example",
        "opportunity_found_officially": False,
        "opportunity_details_match": False,
        "text": """
        DigitalForge guaranteed placement internship.

        A refundable security deposit of ₹2200 is required.
        Pay now or lose your selection.

        Provide your debit card number and CVV.
        The application is available at:

        https://digitalforge-placement.example/apply
        """
    },

    {
        "id": "F11",
        "category": "Job",
        "type": "Fraudulent",
        "expected": "AVOID",
        "organization_domain": "cloudmatrix.example",
        "opportunity_found_officially": False,
        "opportunity_details_match": False,
        "text": """
        CloudMatrix instant job selection.

        Pay a verification fee of ₹1800 immediately.
        Send the payment to hr@outlook.com.

        Provide your password and OTP.
        This opportunity is government certified.

        Failure to pay will cancel the offer.
        """
    },


    # =====================================================
    # AMBIGUOUS CASES — 8
    # =====================================================

    {
        "id": "A01",
        "category": "Internship",
        "type": "Ambiguous",
        "expected": "VERIFY",
        "organization_domain": "brightlabs.example",
        "opportunity_found_officially": None,
        "opportunity_details_match": None,
        "text": """
        BrightLabs internship opportunity for students.

        A refundable training fee of ₹500 is mentioned.
        Applications are closing shortly.

        Please verify the opportunity and payment details
        before proceeding.
        """
    },

    {
        "id": "A02",
        "category": "Job",
        "type": "Ambiguous",
        "expected": "VERIFY",
        "organization_domain": "northstar.example",
        "opportunity_found_officially": None,
        "opportunity_details_match": None,
        "text": """
        NorthStar student trainee opportunity.

        A recruiter contacted the applicant and shared
        an application link.

        The official opportunity has not yet been independently
        checked.
        """
    },

    {
        "id": "A03",
        "category": "Scholarship",
        "type": "Ambiguous",
        "expected": "VERIFY",
        "organization_domain": "learnforward.example",
        "opportunity_found_officially": None,
        "opportunity_details_match": None,
        "text": """
        LearnForward scholarship information received through
        a forwarded message.

        The message mentions a small application processing fee.

        The original official listing has not yet been checked.
        """
    },

    {
        "id": "A04",
        "category": "Internship",
        "type": "Ambiguous",
        "expected": "VERIFY",
        "organization_domain": "codebridge.example",
        "opportunity_found_officially": None,
        "opportunity_details_match": None,
        "text": """
        CodeBridge internship opportunity received from a
        student group.

        The message asks applicants to complete the application
        soon and provides an external application link.

        The official listing has not yet been independently verified.
        """
    },

    {
        "id": "A05",
        "category": "Job",
        "type": "Ambiguous",
        "expected": "VERIFY",
        "organization_domain": "vertexdata.example",
        "opportunity_found_officially": None,
        "opportunity_details_match": None,
        "text": """
        VertexData job opportunity shared by a recruiter.

        The recruiter has provided salary information and an
        application link.

        The opportunity and recruiter identity have not yet been
        independently verified.
        """
    },

    {
        "id": "A06",
        "category": "Scholarship",
        "type": "Ambiguous",
        "expected": "VERIFY",
        "organization_domain": "futurepath.example",
        "opportunity_found_officially": None,
        "opportunity_details_match": None,
        "text": """
        FuturePath scholarship message received through social media.

        The message appears to describe a legitimate scholarship,
        but the official opportunity listing has not been checked.

        No payment has been made.
        """
    },

    {
        "id": "A07",
        "category": "Internship",
        "type": "Ambiguous",
        "expected": "VERIFY",
        "organization_domain": "techharbor.example",
        "opportunity_found_officially": None,
        "opportunity_details_match": None,
        "text": """
        TechHarbor internship information was forwarded by another
        student.

        The message includes a deadline and asks students to apply
        soon.

        The original source and opportunity details have not yet
        been independently confirmed.
        """
    },

    {
        "id": "A08",
        "category": "Job",
        "type": "Ambiguous",
        "expected": "VERIFY",
        "organization_domain": "infocore.example",
        "opportunity_found_officially": None,
        "opportunity_details_match": None,
        "text": """
        InfoCore trainee vacancy shared through a messaging group.

        The message contains job details and a contact number.

        The official careers page and recruiter identity have not
        yet been independently verified.
        """
    }
]
