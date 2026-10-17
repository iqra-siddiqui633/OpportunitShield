# OpportunityShield
# Flask Application v1.0

from flask import Flask, render_template, request, jsonify

from opportunity_analyzer import OpportunityAnalyzer


# =========================================================
# CREATE FLASK APPLICATION
# =========================================================

app = Flask(__name__)


# =========================================================
# INITIALIZE OPPORTUNITY ANALYZER
# =========================================================

analyzer = OpportunityAnalyzer()


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():

    return render_template("index.html")


# =========================================================
# ANALYZE OPPORTUNITY
# =========================================================

@app.route("/analyze", methods=["POST"])
def analyze_opportunity():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data received."
            }), 400

        text = data.get("text", "").strip()

        organization_domain = data.get(
            "organization_domain"
        )

        opportunity_found_officially = data.get(
            "opportunity_found_officially"
        )

        opportunity_details_match = data.get(
            "opportunity_details_match"
        )

        # -------------------------------------------------
        # Validate input
        # -------------------------------------------------

        if not text:

            return jsonify({
                "error": "Please provide an opportunity message."
            }), 400

        # -------------------------------------------------
        # Run OpportunityShield analysis
        # -------------------------------------------------

        result = analyzer.analyze(

            text=text,

            organization_domain=
                organization_domain,

            opportunity_found_officially=
                opportunity_found_officially,

            opportunity_details_match=
                opportunity_details_match
        )

        # -------------------------------------------------
        # Return analysis to frontend
        # -------------------------------------------------

        return jsonify(result)

    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 500


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(host="0.0.0.0" , port=5000, debug=True
    )