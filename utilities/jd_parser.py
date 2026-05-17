import re

def extract_jd_keywords(jd_text):
    words = re.findall(r'\b[a-zA-Z]{3,}\b', jd_text.lower())

    #remove common words
    stopwords = [
        "the","and","with","for","are","you","will","this","that",
        "data","experience","learning","work","team","skills",
        "strong","science","statistics","knowledge","ability"
    ]

    keywords = [w for w in words if w not in stopwords]

    #keep only meaningful words
    useful_patterns = [
        "python","java","sql","react","api","ml","nlp","model",
        "backend","frontend","flask","django","seo","content",
        "analysis","analytics","database","cloud","docker"
    ]

    final_keywords = []

    for word in keywords:
        if any(p in word for p in useful_patterns):
            final_keywords.append(word)

    #remove duplicates
    final_keywords = list(set(final_keywords))

    return final_keywords[:5]