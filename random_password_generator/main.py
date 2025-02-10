#Ethan Blanco, Random Password Generator

import random
import string

def get_password_requirements():
    """Asks the user for password settings and ensures valid input."""
    print("\nPassword Requirements (y/n):")
    use_uppercase = input("Include uppercase letters? ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? ").strip().lower() == 'y'
    use_numbers = input("Include numbers? ").strip().lower() == 'y'
    use_special = input("Include special characters? ").strip().lower() == 'y'

    if not (use_uppercase or use_lowercase or use_numbers or use_special):
        print("Error: Select at least one character type.\n")
        return get_password_requirements()  
    return use_uppercase, use_lowercase, use_numbers, use_special


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    """Creates a random password based on user preferences."""
    char_types = {
        "uppercase": string.ascii_uppercase if use_uppercase else "",
        "lowercase": string.ascii_lowercase if use_lowercase else "",
        "numbers": string.digits if use_numbers else "",
        "special": "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" if use_special else ""
    }



    all_chars = "".join(char_types.values())
    if not all_chars:
        raise ValueError("Error: No character types selected.")
    # Ensure at least one character from each chosen type
    password = [random.choice(chars) for chars in char_types.values() if chars]
    password += random.choices(all_chars, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)


def check_password_strength(password):
    """Rates password strength as Weak, Medium, or Strong."""
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for char in password)

    criteria_met = sum([has_upper, has_lower, has_digit, has_special])

    if len(password) >= 12 and criteria_met == 4:
        return "Strong"
    elif len(password) >= 8 and criteria_met >= 3:
        return "Medium"
    return "Weak"


if __name__ == "__main__":
    print("===== Secure Password Generator =====")
    try:
        #Get valid password length
        while True:
            try:
                length = int(input("\nEnter password length (min 4): "))
                if length >= 4:
                    break
                print("Error: Minimum length is 4.")
            except ValueError:
                print("Error: Enter a valid number.")

        #Get password requirements
        use_uppercase, use_lowercase, use_numbers, use_special = get_password_requirements()

        #Generate and display four passwords
        print("\n===== Generated Passwords =====")
        for i in range(4):
            password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
            strength = check_password_strength(password)
            print(f"{i+1}. {password}  (Strength: {strength})")
        print("\n")
    except ValueError as error:
        print(error)