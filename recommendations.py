def generate_recommendations(analysis_results: dict) -> list:
    recs = []
    
    if analysis_results["length"] < 12:
        recs.append("Increase length to at least 12–16 characters. Length is your best defense against brute-force attacks.")
    
    if analysis_results["is_common"]:
        recs.append("CRITICAL: This password is found in common breach dictionaries. Change it immediately.")
    
    if analysis_results["keyboard_pattern"]:
        recs.append("Avoid standard keyboard walks (e.g., 'qwerty', 'asdfgh') as attackers test these first.")
    
    if analysis_results["repeated_chars"] > 0:
        recs.append("Reduce consecutive repeating characters (e.g., 'aaa', '111').")
    
    if analysis_results["sequential_patterns"] > 0:
        recs.append("Remove predictable sequences like '123' or 'abc'.")
        
    if analysis_results["personal_match"] > 0:
        recs.append("Warning: Your password contains personal context data (name/pet/birth year). Attackers use social engineering to guess these.")

    if not recs:
        recs.append("Great job! Your password follows strong defensive principles. Consider using a reputable Password Manager to store it securely.")
        
    return recs

def get_educational_guide() -> dict:
    return {
        "passphrase": "Use a sequence of 4 or more random words (e.g., 'correct-horse-battery-staple'). They are easier for humans to remember and exponentially harder for computers to guess.",
        "hygiene": [
            "Never reuse passwords across multiple services.",
            "Enable Multi-Factor Authentication (MFA) wherever available.",
            "Use a zero-knowledge password manager (e.g., Bitwarden, 1Password).",
            "Avoid substituting numbers for letters in predictable ways (e.g., P@ssw0rd)."
        ]
    }
