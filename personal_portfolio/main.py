#Ethan Blanco, Personal Portfolio

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from InquirerPy import inquirer
import simple_morse_code_translator.main

args = ["----------Personal Portfolio----------"]
def main(): #Main user interface
    while True:
        print(args[0])
        intro = inquirer.text(message="Welcome to your personal portfolio! What was your name?").execute()
        print(f"Welcome {intro}.") #Repeats the username with a welcome message.
        pers_finan_opt = inquirer.select( #Main prompt
            message="What would you like to do or know?:", #Questions
            choices= ["What is this portfolio about?", "First Project", "Second Project", "Third Project", "Fourth Project", "Fifth Project", "Sixth Project", "Personal Optimization", "Exit"],
                filter=lambda result: result.split()[0].lower() #Allows the user to be able to input their response correctly.
        ).execute()
        if pers_finan_opt == "what": #Different choices that go into the different functions.
            print("\nThis portfolio was made for showcasing Ethan Blancos top 6 python projects done in the same earliest repository.")
            print("This can also act as a resume! Neat right?\n")
            print("The python projects you'll be seeing (in order) are;")
            print("Simple Morse Code Translator, To Do List, Random Password Generator, Movie recommender, Personal Library, and Financial Calculator.\n")
            proceed = inquirer.text(message="We're going back now! Did you enjoy the short description?").execute()
            if proceed == "go":
                print("Okay! Back to the menu then!")
                continue
            elif proceed == "exit":
                print("That's okay too, goodbye!")
                break
        elif pers_finan_opt == "first":
            simple_morse_code_translator
            continue
        elif pers_finan_opt == "second":
            print()
            continue
        elif pers_finan_opt == "third":
            print("guh")
            continue
        elif pers_finan_opt == "fourth":
            print()
            continue
        elif pers_finan_opt == "fifth":
            print()
            continue
        elif pers_finan_opt == "sixth":
            print()
            continue
        elif pers_finan_opt == "personal":
            print()
            continue
        elif pers_finan_opt == "exit":
            print("Goodbye!")
            break

main()