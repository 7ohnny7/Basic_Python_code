import random
import string

def generate_random_password(length=16):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
random_password = generate_random_password()
print(f"Random password: {random_password}")
