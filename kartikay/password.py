# Input password from the user
password = input("Enter Your Password: ")

# Initialize flags
has_upper = False
has_lower = False
has_digit = False
has_special = False
special_characters = "!@#$%^&*(),.?\":{}|<>"

# Check length
if len(password) < 8:
    print("Weak Password: Less than 8 characters")
else:
    # Check for uppercase, lowercase, digits, and special characters
    for char in password:
        if 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in special_characters:
            has_special = True

    # Determine strength
    if not has_upper:
        print("Weak Password: No uppercase letter")
    elif not has_lower:
        print("Weak Password: No lowercase letter")
    elif not has_digit:
        print("Weak Password: No digits")
    elif not has_special:
        print("Weak Password: No special characters")
    else:
        print("Strong Password")
