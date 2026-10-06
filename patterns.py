import re

# A lightweight embedded list of top common passwords for demonstration
COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123", 
    "admin", "welcome", "monkey", "dragon", "password123", "letmein"
}

KEYBOARD_PATTERNS = [
    "qwertyuiop", "asdfghjkl", "zxcvbnm",
    "1234567890", "qazwsx", "edcrfv"
]

def check_common_password(password: str) -> bool:
    """Check if the password matches known leaked or common passwords."""
    return password.lower().strip() in COMMON_PASSWORDS

def check_repeated_characters(password: str) -> int:
    """Count instances of 3 or more consecutive repeating characters (e.g., 'aaa')."""
    pattern = r"(.){2,}"
    matches = re.findall(pattern, password)
    return len(matches)

def check_sequential_patterns(password: str) -> int:
    """Detect simple alphabetical or numerical sequences (e.g., '123', 'abc')."""
    sequences = ["0123456789", "abcdefghijklmnopqrstuvwxyz"]
    count = 0
    lower_pwd = password.lower()
    
    for seq in sequences:
        for i in range(len(seq) - 2):
            sub = seq[i:i+3]
            if sub in lower_pwd or sub[::-1] in lower_pwd:
                count += 1
    return count

def check_keyboard_patterns(password: str) -> bool:
    """Detect standard keyboard layout patterns."""
    lower_pwd = password.lower()
    for pattern in KEYBOARD_PATTERNS:
        for i in range(len(pattern) - 2):
            sub = pattern[i:i+3]
            if sub in lower_pwd or sub[::-1] in lower_pwd:
                return True
    return False

def check_personal_info(password: str, context_words: list) -> int:
    """Check if user-provided contextual words (name, pet, DOB) appear in the password."""
    if not context_words:
        return 0
    matches = 0
    lower_pwd = password.lower()
    for word in context_words:
        if word and word.strip().lower() in lower_pwd:
            matches += 1
    return matches
