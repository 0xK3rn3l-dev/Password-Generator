import random
import string

def _generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True) -> str:
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
    return [_generate_password(**kwargs) for _ in range(count)]


