from patterns import (
    check_common_password, 
    check_repeated_characters, 
    check_sequential_patterns, 
    check_keyboard_patterns,
    check_personal_info
)
from entropy import calculate_entropy

def analyze_password(password: str, context_words: list = None) -> dict:
    if context_words is None:
        context_words = []

    length = len(password)
    is_common = check_common_password(password)
    repeated_chars = check_repeated_characters(password)
    sequential_patterns = check_sequential_patterns(password)
    keyboard_pattern = check_keyboard_patterns(password)
    personal_match = check_personal_info(password, context_words)
    entropy = calculate_entropy(password)

    # Scoring Logic (0 to 100 scale)
    score = 100

    if length < 8:
        score -= 40
    elif length < 12:
        score -= 20
    elif length >= 16:
        score += 10

    if is_common:
        score = 0
    if keyboard_pattern:
        score -= 25
    score -= (repeated_chars * 10)
    score -= (sequential_patterns * 15)
    score -= (personal_match * 25)

    # Entropy penalties
    if entropy < 30:
        score -= 30
    elif entropy < 50:
        score -= 15

    score = max(0, min(100, score))

    # Classification
    if score == 0 or is_common:
        classification = "VERY WEAK"
    elif score < 40:
        classification = "WEAK"
    elif score < 70:
        classification = "MODERATE"
    elif score < 90:
        classification = "STRONG"
    else:
        classification = "VERY STRONG"

    return {
        "password_length": length,
        "score": score,
        "classification": classification,
        "length": length,
        "is_common": is_common,
        "repeated_chars": repeated_chars,
        "sequential_patterns": sequential_patterns,
        "keyboard_pattern": keyboard_pattern,
        "personal_match": personal_match,
        "entropy": entropy
    }
