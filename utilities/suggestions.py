def generate_suggestions(score, matched_req, total_req, matched_opt, total_opt, section_scores):
    suggestions = []

    # Overall score
    if score < 50:
        suggestions.append("Overall match is low. Improve alignment with job description.")

    # Required skills
    if matched_req < total_req:
        suggestions.append("You are missing some required skills. Try adding relevant experience or keywords.")

    # Optional skills
    if matched_opt < total_opt:
        suggestions.append("Adding optional skills can improve your profile strength.")

    # Section feedback
    if section_scores.get("projects", 0) < 60:
        suggestions.append("Improve your project descriptions with more relevant technologies.")

    if section_scores.get("experience", 0) < 60:
        suggestions.append("Add measurable achievements in your experience section.")

    return suggestions

def generate_advanced_suggestions(missing_skills, weak_bullets):
    suggestions = []

    if missing_skills:
        suggestions.append(
            f"Add projects using: {', '.join(missing_skills[:3])}"
        )

    for bullet, score in weak_bullets[:2]:
        suggestions.append(
            f"Improve this bullet: '{bullet[:60]}...' → add metrics or tech details"
        )

    return suggestions