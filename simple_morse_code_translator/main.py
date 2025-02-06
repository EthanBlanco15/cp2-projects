#Ethan Blanco

# List of Morse Code translations (English letter -> Morse code)
morse_code_list = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'),
    ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
    ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
    ('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
    ('Y', '-.--'), ('Z', '--..'), ('1', '.----'), ('2', '..---'), ('3', '...--'),
    ('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'), ('8', '---..'),
    ('9', '----.'), ('0', '-----'), (' ', '/')  # Space is represented as '/'
]

# Convert the list into dictionaries for efficient lookups
morse_code_dict = dict(morse_code_list)  # English words to Morse code
english_dict = {morse: letter for letter, morse in morse_code_list}  # Morse -> English

def display_morse_list():

#Displays the list of Morse code translations.
    print("\nMorse Code Reference List:")
    for letter, code in morse_code_list:
        print(f"{letter}: {code}")

def get_valid_input(prompt):

#Gets user input and ensures it's not empty.
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("You entered nothing. Please try again.")

def morse_code_translator():

#Translates an English word or phrase into Morse code.
    display_morse_list()
    
    user_input = get_valid_input("\nEnter a word or phrase in uppercase English to convert into Morse code: ").upper()
    
    # Convert to Morse code, using '?' for unknown characters
    morse_translation = ' '.join(morse_code_dict.get(char, '?') for char in user_input)

    print("\nHere is your Morse code translation:")
    print(morse_translation)

def english_translator():

#Translates Morse code into English.
    display_morse_list()

    user_input = get_valid_input("\nEnter Morse code to convert into English (separate letters with spaces and words with '/'): ")
    
    # Convert Morse code to English, using '?' for unknown symbols
    english_translation = ''.join(english_dict.get(code, '?') for code in user_input.split())

    print("\nHere is your English translation:")
    print(english_translation)

def main():

#Main function that allows users to choose different translation options.
    menu_options = {
        "1": morse_code_translator,
        "2": english_translator,
        "3": display_morse_list,
        "4": lambda: print("Goodbye! Thank you for using the Morse Code Translator.")
    }

    while True:
        print("\nWelcome to the Morse Code Translator!")
        print("1: Translate English to Morse code")
        print("2: Translate Morse code to English")
        print("3: View the Morse code reference list")
        print("4: Exit the program")

        user_choice = get_valid_input("Enter your choice: ")

        if user_choice in menu_options:
            if user_choice == "4":
                menu_options[user_choice]()
                break
            menu_options[user_choice]()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()