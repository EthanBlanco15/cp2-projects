#Ethan Blanco, Personal Portfolio

from simplemorsecodetranslator import simple_main
from todolist import todo_main
from randompasswordgen import ran_main
from movierecommender import movie_main
from personallibrary import pers_main
from financialcalculator import finance_main

def main(): #Main user interface
    while True:
        print("----------Personal Portfolio----------")
        print("Welcome User.") #Repeats the username with a welcome message.
        print("What would you like to do or know?:") #Questions
        pers_finan_opt = int(input("What is this portfolio about? (0)\nSimple Morse Code Translator (1)\nTo Do List (2)\nRandom Password Generator (3)\nMovie recommender (4)\nPersonal Library (5)\nFinancial Calculator (6)\nExit (7)\n")) #Main Prompt
        if pers_finan_opt == 0: #Different choices that go into the different functions.
            print("\nThis portfolio was made for showcasing Ethan Blancos top 6 python projects done in the same earliest repository.")
            print("This can also act as a resume! Neat right?\n")
            print("The python projects you'll be seeing (in order) are;")
            print("Simple Morse Code Translator, To Do List, Random Password Generator, Movie recommender, Personal Library, and Financial Calculator.\n")
            proceed = int(input("We're going back now! Or did you want to exit? (1 to return, 2 to exit)"))
            if proceed == 1:
                print("Okay! Back to the menu then!")
                continue
            elif proceed == 2:
                print("That's okay too, goodbye!")
                break
        elif pers_finan_opt == 1: #Is the first program
            print("This is the Simple Morse Code Translator, it is a program that allows you to input either English or morse code words and convert it accordingly! You'll be given two choices to translate into, morse code into English or English to morse code, as well as the morse code alphabet in English will be given.")
            confirmation = int(input("Would you like to try the program out? (1 to select, 2 to return)"))
            if confirmation == 1: #Goes into the separate code.
                simple_main.morse_main()
            elif confirmation == 2: #Sends the user back to main.
                print("Okay! I'll send you back to the starting interface.")
                continue
        elif pers_finan_opt == 2: #Is the second program.
            print("This is the To Do List, it is a program that allows a user to add, remove, and check things from a list, like having computer post-it notes!")
            continuation = int(input("Would you like to try the program out? (1 to select, 2 to return)"))
            if continuation == 1: #Goes into the separate imported code.
                todo_main.list_main()
            elif continuation == 2: #Sends the user back to main.
                print("No problem! Sending you back to the starting interface.")
                continue
        elif pers_finan_opt == 3: #Is the third program
            print("This is the Random Password Generator, it is a program that produces random passwords that fit the users requirements and needs while also grading on how weak or powerful that password is.")
            follow_up = int(input("Would you like to try the program out? (1 to select, 2 to return)"))
            if follow_up == 1: #Goes into the separate imported code.
                ran_main.gen_main()
            elif follow_up == 2: #Sends the user back to main.
                print("That's all right! Sending you back to the starting interface.")
                continue
        elif pers_finan_opt == 4: #Is the fourth program.
            print("This is the Movie Recommender, it allows a user to search movies in a CSV file and suggests a movie based on their specific inputs.")
            question = int(input("Would you like to try the program out? (1 to select, 2 to return)"))
            if question == 1: #Goes into the separate imported code.
                movie_main.rec_main()
            elif question == 2: #Sends the user back to main.
                print("Thank you for your time! Sending you back to the starting interface.")
                continue
        elif pers_finan_opt == 5: #Is the fifth program.
            print("This is the Personal Library, it's a program that lets a user add, remove, search, and see the full library of books stored onto a CSV file. There are already books and examples given out for the user to start with.")
            go = int(input("Would you like to try the program out? (1 to select, 2 to return)"))
            if go == 1: #Goes into the separate imported code.
                pers_main.lib_main()
            elif go == 2: #Sends the user back to main.
                print("Great! Sending you back to the starting interface.")
                continue
        elif pers_finan_opt == 6: #Is the sixth program.
            print("This is the Financial Calculator, it is a program that allows the user to, as the name implies, use a financial calculator to help with complex problems for things such as budgetting, saving, and accounting.")
            now = int(input("Would you like to try the program out? (1 to select, 2 to return)"))
            if now == 1: #Goes into the separate imported code.
                finance_main.fin_main()
            elif now == 2: #Sends the user back to main.
                print("Ok, come back soon! Sending you back to the starting interface.")
                continue
        elif pers_finan_opt == 7:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()