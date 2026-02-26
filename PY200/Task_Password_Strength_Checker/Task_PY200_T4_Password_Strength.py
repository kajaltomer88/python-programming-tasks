password = input("Enter your password: ")

has_digit = False
has_upper = False
has_lower = False

# Rule 1: Length check
if len(password) >= 8:
    
    # Loop to check characters
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True

    # Final check
    if has_digit and has_upper and has_lower:
        print("STRONG")
    else:
        print("WEAK")

else:
    print("WEAK")