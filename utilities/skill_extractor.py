from utilities.similarity import compute_similarity

IMPORTANT_KEYWORDS = ["must", "required", "mandatory"]
OPTIONAL_KEYWORDS = ["preferred", "good to have", "plus"]

STOPWORDS = ["looking", "candidate", "experience", "role", "job", "work"]

# Extract weighted skills dynamically from JD
def extract_weighted_skills(jd_text):
    jd_text = jd_text.lower()
    lines = jd_text.split('\n')

    required = []
    optional = []

    for line in lines:
        line = line.strip()

        if any(k in line for k in IMPORTANT_KEYWORDS):
            required.append(line)
        elif any(k in line for k in OPTIONAL_KEYWORDS):
            optional.append(line)
        else:
            optional.append(line)

    # clean noise
    required = [l for l in required if not any(w in l for w in STOPWORDS)]
    optional = [l for l in optional if not any(w in l for w in STOPWORDS)]

    return required, optional


# Semantic matching (fixes keyword problem)
def weighted_skill_matching(resume_text, required, optional):
    matched_req = 0
    matched_opt = 0

    for skill in required:
        score = compute_similarity(resume_text, skill)
        if score > 65:
            matched_req += 1

    for skill in optional:
        score = compute_similarity(resume_text, skill)
        if score > 60:
            matched_opt += 1

    return matched_req, len(required), matched_opt, len(optional)