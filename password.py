import random
import string

def generate_password(length=12):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    all_chars = lower + upper + digits
    password += random.choices(all_chars, k=length - 3)

    return ''.join(password)

print("Generated Password:", generate_password())
