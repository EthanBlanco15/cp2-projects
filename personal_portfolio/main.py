#Ethan Blanco, Personal Portfolio

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from InquirerPy import inquirer

args = ["----------Personal Portfolio----------"]
def main(): #Main user interface
    while True:
        print(args[0])
        intro = inquirer.text(message="Welcome to your personal portfolio! What was your name?").execute()
        print(f"Welcome {intro}.") #Repeats the username with a welcome message.
        pers_finan_opt = inquirer.select( #Main prompt
            message="What would you like to do or know?:", #Questions
            choices= ["What is this portfolio about?", "First Project", "Second Project", "Third Project", "Fourth Project", "Fifth Project", "Sixth Project", "Exit"],
                filter=lambda result: result.split()[0].lower() #Allows the user to be able to input their response correctly.
        ).execute()
        if pers_finan_opt == "what": #Different choices that go into the different functions.
            print("\nThis portfolio was made for showcasing Ethan Blancos top 6 python projects done in the same earliest repository.")
            print("This can also act as a resume! Neat right?\n")
            print("The python projects you'll be seeing (in order) are;")
            print("Simple Morse Code Translator, To Do List, Random Password Generator, Movie recommender, Personal Library, and Financial Calculator.\n")
            proceed = inquirer.text(message="We're going back now! Or did you want to exit? (Y/N to exit)").execute()
            if proceed == "N":
                print("Okay! Back to the menu then!")
                continue
            elif proceed == "Y":
                print("That's okay too, goodbye!")
                break
        elif pers_finan_opt == "first": #Is the first program
            print("This is the Simple Morse Code Translator, it is a program that allows you to input either English or morse code words and convert it accordingly!")
            confirmation = inquirer.text(message="Would you like to try the program out? (Y/N to select)").execute()
            if confirmation == "Y": #Goes into the separate code.
                break
            elif confirmation == "N": #Sends the user back to main.
                print("Okay! I'll send you back to the starting interface.")
                continue
        elif pers_finan_opt == "second": #Is the second program.
            print("This is the To Do List, it is a program that allows a user to add, remove, and check things from a list, like having computer post-it notes!")
            continuation = inquirer.text(message="Would you like to try the program out? (Y/N to select)").execute()
            if continuation == "Y": #Goes into the separate imported code.
                break
            elif continuation == "N": #Sends the user back to main.
                print("No problem! Sending you back to the starting interface.")
                continue
        elif pers_finan_opt == "third": #Is the third program
            print("This is the Random Password Generator, it is a program that produces random passwords that fit the users requirements and needs.")
            follow_up = inquirer.text(message="Would you like to try the program out? (Y/N to select)").execute()
            if follow_up == "Y": #Goes into the separate imported code.
                break
            elif follow_up == "N": #Sends the user back to main.
                print("That's all right! Sending you back to the starting interface.")
                continue
        elif pers_finan_opt == "fourth": #Is the fourth program.
            print("This is the Movie Recommender, it allows a user to search movies in a CSV file and suggests a movie based on their inputs.")
            question = inquirer.text(message="Would you like to try the program out? (Y/N to select)").execute()
            if question == "Y": #Goes into the separate imported code.
                break
            elif question == "N": #Sends the user back to main.
                print("Thank you for your time! Sending you back to the starting interface.")
                continue
        elif pers_finan_opt == "fifth": #Is the fifth program.
            print("This is the Personal Library, it's a program that lets a user add, remove, search, and see the full library of books stored into a CSV file.")
            go = inquirer.text(message="Would you like to try the program out? (Y/N to select)").execute()
            if go == "Y": #Goes into the separate imported code.
                break
            elif go == "N": #Sends the user back to main.
                print("Great! Sending you back to the starting interface.")
                continue
        elif pers_finan_opt == "sixth": #Is the sixth program.
            print("This is the Financial Calculator, it is a program that allows the user to, as the name implies, use a financial calculator for things such as budgetting.")
            now = inquirer.text(message="Would you like to try the program out? (Y/N to select)").execute()
            if now == "Y": #Goes into the separate imported code.
                break
            elif now == "N": #Sends the user back to main.
                print("Ok, come back soon! Sending you back to the starting interface.")
                continue
        elif pers_finan_opt == "exit":
            print("Goodbye!")
            break

main()