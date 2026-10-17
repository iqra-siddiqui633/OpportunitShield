from opportunity_analyzer import OpportunityAnalyzer


analyzer = OpportunityAnalyzer()


# ============================================================
# TEST OPPORTUNITY
# ============================================================

opportunity = """

Congratulations!

You have been selected for the ABC Technologies
Summer Internship.

Pay ₹1,999 registration fee within 30 minutes
to confirm your seat.

Failure to pay will result in cancellation.

Only 5 seats remain.

Please send your Aadhaar card and bank account
details to complete verification.

Contact HR at abc.hr@gmail.com.

Apply here:
https://abc-careers.example/apply
"""


# ============================================================
# RUN COMPLETE ANALYSIS
# ============================================================

result = analyzer.analyze(

    text=opportunity,

    organization_domain="abctech.example",

    opportunity_found_officially=False,

    opportunity_details_match=False
)


# ============================================================
# DISPLAY RESULT
# ============================================================

print("=" * 65)
print("OPPORTUNITYSHIELD — END-TO-END ANALYSIS")
print("=" * 65)

print()

print("FINAL RECOMMENDATION:")
print(
    result["risk_analysis"]["recommendation"]
)

print()

print("TOTAL RISK SCORE:")
print(
    result["risk_analysis"]["total_score"]
)

print()

print("CRITICAL FLAGS:")
print(
    result["risk_analysis"]["critical_flags"]
)

print()

print("=" * 65)
print("EXTRACTED EVIDENCE")
print("=" * 65)

print()

print("Emails:")
print(
    result["extracted_evidence"]["extracted_emails"]
)

print()

print("URLs:")
print(
    result["extracted_evidence"]["extracted_urls"]
)

print()

print("Financial:")
print(
    result["extracted_evidence"]["financial"]
)

print()

print("Sensitive Data:")
print(
    result["extracted_evidence"]["sensitive_data"]
)

print()

print("Psychological Pressure:")
print(
    result["extracted_evidence"]["psychological_pressure"]
)

print()

print("=" * 65)
print("VERIFICATION RESULTS")
print("=" * 65)

for key, value in result["verification"].items():

    print()
    print(key)
    print(value)

print()

print("=" * 65)
print("FINAL EXPLANATION")
print("=" * 65)

print()

print(result["explanation"])