import re
from typing import Dict, List, Tuple


def normalize_words(text: str) -> List[str]:
    return re.findall(r"\b[a-zA-Z][a-zA-Z0-9+\-#/.]*\b", text.lower())


def keyword_overlap_score(resume_text: str, job_description: str) -> Tuple[int, List[str]]:
    resume_words = set(normalize_words(resume_text))
    jd_words = normalize_words(job_description)

    important_keywords = []
    for word in jd_words:
        if len(word) >= 4 and word not in important_keywords:
            important_keywords.append(word)

    important_keywords = important_keywords[:40]

    matched = [kw for kw in important_keywords if kw in resume_words]
    missing = [kw for kw in important_keywords if kw not in resume_words]

    if not important_keywords:
        return 0, []

    score = int((len(matched) / len(important_keywords)) * 100)
    return score, missing[:10]


def combine_scores(llm_score: int, keyword_score: int) -> int:
    weighted = int((0.7 * llm_score) + (0.3 * keyword_score))
    return max(0, min(100, weighted))