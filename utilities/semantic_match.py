from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def match_bullets_to_jd(bullets, jd_text):
    jd_sentences = jd_text.split('.')

    jd_embeddings = model.encode(jd_sentences, convert_to_tensor=True)

    matched_pairs = []

    for b in bullets:
        b_embedding = model.encode(b, convert_to_tensor=True)

        scores = util.cos_sim(b_embedding, jd_embeddings)[0]

        best_idx = scores.argmax().item()
        best_match = jd_sentences[best_idx]

        matched_pairs.append((b, best_match))

    return matched_pairs