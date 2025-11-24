import secrets
import string

def generate_password(length=12, uppercase=True, numbers=True, symbols=True):
    characters = string.ascii_lowercase
    
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += "!@#$%^&*()-_=+[]{};<>?/|"

    # strong secure random
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password