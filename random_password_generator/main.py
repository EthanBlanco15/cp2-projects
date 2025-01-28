#Ethan Blanco, Random Password Generator

import random
import string
def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    
    #Generates a secure password based on user preferences.
    char_groups = {
        "uppercase": string.ascii_uppercase if use_uppercase else "",
        "lowercase": string.ascii_lowercase if use_lowercase else "",
        "numbers": string.digits if use_numbers else "",
        "special": "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" if use_special else ""
    }
    
    all_chars = "".join(char_groups.values())
    if not all_chars:
        raise ValueError("At least one character type must be selected.")
    # Guarantee at least one character from each selected group
    password = [random.choice(chars) for chars in char_groups.values() if chars]
    # Fill the rest of the password randomly
    password += random.choices(all_chars, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)

generate_password()

def check_password_strength(password):

    #Evaluates password strength.
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for char in password)
    
    criteria_met = sum([has_upper, has_lower, has_digit, has_special])
    if len(password) >= 12 and criteria_met == 4:
        return "Strong"
    elif len(password) >= 8 and criteria_met >= 3:
        return "Medium"
    else:
        return "Weak"
if __name__ == "__main__":
    print("Password Generator")
    try:
        length = int(input("Enter password length (min 4): "))
        if length < 4:
            raise ValueError("Length must be at least 4.")
        
        use_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
        use_lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
        use_numbers = input("Include numbers (y/n)? ").lower() == 'y'
        use_special = input("Include special characters (y/n)? ").lower() == 'y'
        if not (use_uppercase or use_lowercase or use_numbers or use_special):
            raise ValueError("At least one character type must be selected.")
        
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        print(f"\nGenerated Password: {password}")
        print(f"Password Strength: {check_password_strength(password)}")
    except ValueError as e:
        print(f"Error: {e}")