#Ethan Blanco, Personal Library Program

library = ["Harry Potter, by J. K. Rowling, comedy"]

def add(): #This function is supposed to allow the user to add any type of book with the title, author and one type of genre.

    pass

add()

def remove(): #The handy dandy function here allows the user to remove any type of book, removes the title, author, and type of genre by default.

    pass

remove()

def search_bar(): #Lets you search for a specific known book by title, author, and genre.

    pass

search_bar()

def main(): #Main user interface

    while True:
        pers_libr = int(input("""Welcome to your personal library! What would you like to do?"
        Type 1 to view your library.
        Type 2 to add items into your library.
        Type 3 to remove items from your library.
        Type 4 to search the details about an item from your library.
        Type 5 to leave.\n"""))
        pass
        if pers_libr == 1:
            print(f"Here's your personal library, take a look! {library}")
        if pers_libr == 2:
            pass
        if pers_libr == 3:
            pass
        if pers_libr == 4:
            pass
        if pers_libr == 5:
            pass

main()