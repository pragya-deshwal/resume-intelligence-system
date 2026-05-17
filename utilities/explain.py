def generate_explanation(score, matched_req, total_req, matched_opt, total_opt):
    reasons = []

    # Score based reasoning
    if score < 50:
        reasons.append("Low semantic similarity with job description.")
    elif score < 75:
        reasons.append("Partial alignment with job description.")
    else:
        reasons.append("Strong alignment with job description.")

    # Required skills
    if matched_req < total_req:
        reasons.append(f"Missing {total_req - matched_req} required skills.")

    # Optional skills
    if matched_opt < total_opt:
        reasons.append("Some optional skills are missing.")

    return reasons