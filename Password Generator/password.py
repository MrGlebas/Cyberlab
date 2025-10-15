import random
import string

def generate_password(length=12):
    """Generate a random password of given length."""
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols

    # Ensure at least one of each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password)
    return ''.join(password)

def evaluate_strength(password):
    """Evaluate password strength and return a score 0-5."""
    categories = [
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password)
    ]
    score = sum(categories)

    # Bonus point for long passwords
    if len(password) >= 12:
        score += 1
    return min(score, 5)

def strength_bar(score):
    """Return a visual bar and strength label."""
    total_blocks = 5
    filled = "#" * score
    empty = "-" * (total_blocks - score)

    if score <= 2:
        label = "Weak"
    elif score in [3, 4]:
        label = "Medium"
    else:
        label = "Strong"

    return f"[{filled}{empty}] {label}"

def print_signature():
    """Print a simple, readable signature."""
    signature = """
========================
     Coded by Mantvydas
========================
"""
    print(signature)

if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")

        score = evaluate_strength(password)
        print("Password Strength:", strength_bar(score))
        
        # Signature
        print_signature()
    except ValueError:
        print("Please enter a valid number for password length.")
