def skill_gap_analysis(matched_req, total_req, matched_opt, total_opt):
    gaps = []

    missing_req = total_req - matched_req
    missing_opt = total_opt - matched_opt

    # High priority
    if missing_req > 0:
        gaps.append(("HIGH", f"{missing_req} required skills missing"))

    # Medium
    if missing_opt > 0:
        gaps.append(("MEDIUM", f"{missing_opt} optional skills missing"))

    # Low
    if missing_req == 0 and missing_opt == 0:
        gaps.append(("LOW", "Strong skill coverage"))

    return gaps