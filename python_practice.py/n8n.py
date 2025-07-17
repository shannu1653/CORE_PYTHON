import re

def process_resumes(items):
    results = []

    keywords = {
        "frontend": ["html", "css", "javascript", "reactjs"],
        "backend": ["nodejs", "express", "mongodb", "mysql"],
        "general": ["git", "graphql", "aws", "ci", "cd"]
    }

    for item in items:
        text = item.get('json', {}).get("text", "").lower()
        text = re.sub(r'[^a-z0-9@.\s]', ' ', text)  # keep email dots/@
        text = re.sub(r'\s+', ' ', text)

        # Extract email from resume
        match = re.search(r'[a-z0-9\._%+-]+@[a-z0-9.-]+\.[a-z]{2,}', text)
        email = match.group(0) if match else "notfound@example.com"

        found_keywords = []
        total_keywords = sum(len(words) for words in keywords.values())
        matched_keywords = 0

        for category_words in keywords.values():
            for word in category_words:
                if re.search(rf'\b{re.escape(word)}\b', text):
                    matched_keywords += 1
                    found_keywords.append(word)

        score = round((matched_keywords / total_keywords) * 100) if total_keywords else 0
        is_shortlisted = score >= 60

        result_message = (
            f"❌ Not shortlisted. Your resume score is {score}%. Good job! Found: {', '.join(found_keywords)}."
            if is_shortlisted else
            f"✅ Shortlisted! Your resume score is {score}%. Found: {', '.join(found_keywords)}. Improve with more full stack skills."
        )

        results.append({
            "json": {
                "email": email,
                "score": score,
                "foundKeywords": found_keywords,
                "resultMessage": result_message
            }
        })

    return results 
