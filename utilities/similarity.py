from sklearn.metrics.pairwise import cosine_similarity
from models.model import get_embedding

def compute_similarity(text1, text2):
    emb1 = get_embedding(text1[:1000])
    emb2 = get_embedding(text2)
    
    score = cosine_similarity([emb1], [emb2])[0][0]
    return round(score * 100, 2)
def section_scores(resume_sections, jd_text):
    scores = {}

    for section, content in resume_sections.items():
        if content.strip():
            scores[section] = compute_similarity(content, jd_text)
        else:
            scores[section] = 0

    return scores
def bullet_analysis(bullets, jd_text):
    results = []

    for bullet in bullets:
        score = compute_similarity(bullet, jd_text)
        results.append((bullet, score))

    results = sorted(results, key=lambda x: x[1], reverse=True)
    return results[:5], results[-5:]  # best + worst