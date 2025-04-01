#Ethan Blanco, Personal Portfolio

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

args = ["----------Personal Portfolio----------"]

def main(): #Main user interface
    while True:
        print(args[0])
        try:
            intro = inquirer.text(message="Welcome ot your personal portfolio! What's your name?").execute()
            print(f"Welcome {intro}.") #Repeats the username with a welcome message.
            pers_finan_opt = inquirer.select( #Main prompt
                message="What would you like to do or know?:", #Questions
                choices= ["What is this portfolio about?", "First Project", "Second Project", "Third Project", "Fourth Project", "Fifth Project", "Sixth Project", "Personal Optimization", "Exit"],
                filter=lambda result: result.split()[0].lower() #Allows the user to be able to input their response correctly.
            ).execute()
            if pers_finan_opt == "what": #Different choices that go into the different functions.
                print("\nThis portfolio was made for showcasing Ethan Blancos top 6 python projects done in the same earliest repository.")
                print("This can also act as a resume! Neat right?\n")
                proceed = inquirer.select(
                    message="Would you like to go back, or exit?",
                    option= ["Go back", "Exit"],
                    filter=lambda result: result.split()[0].lower()
                ).execute()
                if proceed == "go":
                    print("Okay! Back to the menu then!")
                    continue
                elif proceed == "exit":
                    print("That's okay too, goodbye!")
                    break
            elif pers_finan_opt == "first":
                print()
                continue
            elif pers_finan_opt == "second":
                print()
                continue
            elif pers_finan_opt == "third":
                print()
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
        except:
            ValueError
            print("This doesn't work! Please choose a correct input (what, first, second, third, fourth, fifth, sixth, exit)")

main()