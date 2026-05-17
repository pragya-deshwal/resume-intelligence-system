import random

def intelligent_rewrite(matched_pairs):
    improved = []

    patterns = [
        "Enhanced {bullet} by aligning with {context}, achieving measurable impact",
        "Developed {bullet} focusing on {context}, improving performance and efficiency",
        "Designed {bullet} incorporating {context}, delivering strong results"
    ]

    action_words = [
        "built","developed","implemented","designed",
        "created","analyzed","trained","optimized",
        "deployed","engineered"
    ]

    for b, context in matched_pairs:
        text = b.lower()

        # filter junk
        if (
            len(b) < 40 or
            any(x in text for x in [
                "@","linkedin","university","school","gpa","cbse"
            ])
        ):
            continue

        if not any(word in text for word in action_words):
            continue

        # clean bullet
        clean_bullet = (
            b.replace("PROJECTS", "")
             .replace("●", "")
             .replace("", "")
             .strip()
        )

        # clean context
        context = context.strip()

        pattern = random.choice(patterns)

        improved_text = pattern.format(
            bullet=clean_bullet,
            context=context
        )

        improved.append({
            "original": clean_bullet,
            "improved": improved_text
        })

        if len(improved) == 3:
            break

    if len(improved) == 0:
        improved.append({
            "original": "No strong bullet points detected",
            "improved": "Add action-based bullet points aligned with job requirements"
        })

    return improved