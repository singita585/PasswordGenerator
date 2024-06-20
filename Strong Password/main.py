import random
import string


def generate_strong_password(length):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    nums = string.digits
    symbols = string.punctuation

    # Ensure at least one character of each type
    core = [random.choice(lower), random.choice(upper),
            random.choice(nums), random.choice(symbols)]

    # Fill the rest of the password length with a mix of all character types
    if length > 4:
        core += [random.choice(lower + upper + nums + symbols) for _ in range(length - 4)]

    # Randomize the order of characters
    random.shuffle(core)

    # Join the characters into a final password string
    password = ''.join(core)

    return password


# Example usage
print(generate_strong_password(12))  # Generates a 12-character strong password
