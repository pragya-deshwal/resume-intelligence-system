def advanced_ats_score(base_score, matched_req, total_req, matched_opt, total_opt):

    # Required skills weight (70%)
    if total_req == 0:
        req_score = 0
    else:
        req_score = (matched_req / total_req) * 70

    # Optional skills weight (30%)
    if total_opt == 0:
        opt_score = 0
    else:
        opt_score = (matched_opt / total_opt) * 30

    final_score = (base_score * 0.5) + req_score + opt_score

    return round(min(final_score, 100), 2)