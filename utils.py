import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True) -> str:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*_?"

    characters = ""
    required_chars = []

    if use_uppercase:
        characters += uppercase
        required_chars.append(random.choice(uppercase))
    if use_lowercase:
        characters += lowercase
        required_chars.append(random.choice(lowercase))
    if use_digits:
        characters += digits
        required_chars.append(random.choice(digits))
    if use_special:
        characters += special
        required_chars.append(random.choice(special))
    if not characters:
        return None

    if length < len(required_chars):
        length = len(required_chars)

    password_chars = required_chars.copy()

    for _ in range(length - len(required_chars)):
        password_chars.append(random.choice(characters))

    random.shuffle(password_chars)
    return ''.join(password_chars)


def generate_multiple_passwords(count=1, **kwargs):
    return [generate_password(**kwargs) for _ in range(count)]


def score_password(password):
    if not password:
        return {"score": 0, "level": "None", "color": "gray", "text": "0-0"}

    score = 0
    
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 2

    if score >= 6:
        level = "Strong"
        color = "green"
        text = ":3"
    elif score >= 4:
        level = "Medium"
        color = "yellow"
        text = ":/"
    elif score >= 2:
        level = "Weak"
        color = "orange"
        text = ":("
    else:
        level = "Very Weak"
        color = "red"
        text = "x-x"

    return {
        "score": score,
        "level": level,
        "color": color,
        "text": text,
        "length": len(password)
    }
