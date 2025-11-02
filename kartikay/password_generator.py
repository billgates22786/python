import random
import string
import pyperclip
# import pyperclip
def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "No character types selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- User Inputs ---
length = int(input("Enter password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# --- Generate and Display Password ---
password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
print(f"\nGenerated Password: {password}")


pyperclip.copy(password)
print("Password copied to clipboard!")


