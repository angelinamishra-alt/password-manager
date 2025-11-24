import re

def check_strength(password: str):
    score = 0

    if len(password) >= 8:
        score += 20
    if re.search(r'[a-z]', password):
        score += 20
    if re.search(r'[A-Z]', password):
        score += 20
    if re.search(r'\d', password):
        score += 20
    if re.search(r'[^A-Za-z0-9]', password):
        score += 20

    if score >= 80:
        return "Very Strong", score
    elif score >= 60:
        return "Strong", score
    elif score >= 40:
        return "Moderate", score
    else:
        return "Weak", score
    