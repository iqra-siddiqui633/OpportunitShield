# OpportunityShield
# 30-Case Software Validation
# Validation Dataset v1.0

from opportunity_analyzer import OpportunityAnalyzer
from cases import CASES
import csv


analyzer = OpportunityAnalyzer()




# =========================================================
# RUN VALIDATION
# =========================================================

results = []

correct = 0

category_results = {
    "Genuine": {"total": 0, "correct": 0},
    "Fraudulent": {"total": 0, "correct": 0},
    "Ambiguous": {"total": 0, "correct": 0}
}


for case in CASES:

    result = analyzer.analyze(
        text=case["text"],
        organization_domain=case["organization_domain"],
        opportunity_found_officially=(
            case["opportunity_found_officially"]
        ),
        opportunity_details_match=(
            case["opportunity_details_match"]
        )
    )

    actual = result["risk_analysis"]["recommendation"]

    is_correct = actual == case["expected"]

    if is_correct:
        correct += 1

    category_results[
        case["type"]
    ]["total"] += 1

    if is_correct:
        category_results[
            case["type"]
        ]["correct"] += 1

    results.append({
        "id": case["id"],
        "category": case["category"],
        "type": case["type"],
        "expected": case["expected"],
        "actual": actual,
        "correct": is_correct,
        "risk_score": result["risk_analysis"]["total_score"],
        "critical_flags": ", ".join(
            result["risk_analysis"]["critical_flags"]
        )
    })


# =========================================================
# PRINT RESULTS
# =========================================================

total_cases = len(CASES)

accuracy = (
    correct / total_cases * 100
)


print("\n========================================")
print("OPPORTUNITYSHIELD VALIDATION")
print("========================================")

print(f"Total Cases: {total_cases}")
print(f"Correct Decisions: {correct}")
print(f"Incorrect Decisions: {total_cases - correct}")
print(f"Decision Accuracy: {accuracy:.2f}%")

print("\n----------------------------------------")
print("CATEGORY RESULTS")
print("----------------------------------------")

for category, data in category_results.items():

    category_accuracy = (
        data["correct"] / data["total"] * 100
    )

    print(
        f"{category}: "
        f"{data['correct']}/{data['total']} "
        f"({category_accuracy:.2f}%)"
    )


print("\n----------------------------------------")
print("CASE RESULTS")
print("----------------------------------------")

for row in results:

    status = "PASS" if row["correct"] else "FAIL"

    print(
        f"{row['id']} | "
        f"{row['type']} | "
        f"Expected: {row['expected']} | "
        f"Actual: {row['actual']} | "
        f"Score: {row['risk_score']} | "
        f"{status}"
    )


# =========================================================
# SAVE CSV
# =========================================================

with open(
    "validation_results.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "id",
            "category",
            "type",
            "expected",
            "actual",
            "correct",
            "risk_score",
            "critical_flags"
        ]
    )

    writer.writeheader()

    writer.writerows(results)


print("\n========================================")
print("Results saved to validation_results.csv")
print("========================================\n")