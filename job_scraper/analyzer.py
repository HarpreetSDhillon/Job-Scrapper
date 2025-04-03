from rapidfuzz import fuzz

def is_relevant(job_title, keywords):
    return any(fuzz.partial_ratio(k.lower(), job_title.lower()) > 70 for k in keywords)