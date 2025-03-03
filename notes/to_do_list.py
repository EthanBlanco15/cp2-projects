#Ethan Blanco, To Do List Notes

def check_input(user_text):

    return not any(char.isdigit() for char in user_text)


def hello(name):

    if check_input(name):
        print(f"hello {name}!")
    else:
        print("Please input only letters.")
        user = input("What is your name:\n").strip().capitalize()
        #8. Recursion is when you call a function inside of itself
        hello(user)
        #9. Recursion runs the function itself again.

user = input("What is your name:\n").strip().capitalize()
hello(user)