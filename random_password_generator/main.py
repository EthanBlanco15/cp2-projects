#Ethan Blanco, Random Password Generator

import random

import string



def generate_password(length=12):

    #Generates a strong password of the given length.

    if length < 8:

        raise ValueError("Password must be at least 8 characters long.")
    # Character groups
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+"

    # Ensure at least one character from each category

    required_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest with random choices from all categories
    all_characters = lowercase + uppercase + digits + symbols
    remaining_chars = random.choices(all_characters, k=length - len(required_chars))


    # Combine required and remaining characters, then shuffle
    password_list = required_chars + remaining_chars
    random.shuffle(password_list)
    return ''.join(password_list)


def check_password_strength(password):

 #Checks the strength of a given password and provides feedback.
    if len(password) < 8:
        return "Weak: Password is too short (minimum 8 characters)."
    if not any(c.islower() for c in password):
        return "Weak: Missing a lowercase letter."
    if not any(c.isupper() for c in password):
        return "Weak: Missing an uppercase letter."
    if not any(c.isdigit() for c in password):
        return "Weak: Missing a number."
    if not any(c in "!@#$%^&*()-_=+" for c in password):
        return "Weak: Missing a special character."
    return "Strong: Password meets all security requirements."


def get_valid_password_length():

    #Asks the user for a valid password length and ensures proper input handling.
    while True:
        try:
            length = int(input("\nEnter the desired password length (minimum 8): "))
            if length < 8:
                print("Password must be at least 8 characters long.")
                continue
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():

    #Main function providing a user-friendly interface for password generation and checking.
    print("\nWelcome to the Secure Password Generator")

    while True:
        print("\nOptions:")
        print("1 - Generate a new password")
        print("2 - Check the strength of an existing password")
        print("3 - Exit")
        
        choice = input("Select an option (1-3): ").strip()
        if choice == "1":
            length = get_valid_password_length()
            password = generate_password(length)
            print(f"\nGenerated Password: {password}")
            print("Strength:", check_password_strength(password))
        elif choice == "2":
            password = input("\nEnter a password to check its strength: ").strip()
            if password:
                print("Strength:", check_password_strength(password))
            else:
                print("Password cannot be empty.")
        elif choice == "3":
            print("\nThank you for using the Secure Password Generator. Stay safe!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
# Run the program

if __name__ == "__main__":
    main()