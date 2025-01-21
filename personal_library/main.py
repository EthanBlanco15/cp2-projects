#Ethan Blanco, Personal Library Program

library = {"Harry Potter, by J. K. Rowling", "Wonder, R. J. Palacio", "The Amazing Spider-Man, Stan Lee"}
genre = ("Harry Potter is a comedy book about wizardry", "Wonder is a fiction book about individuality", "The Amazing Spider-Man is an action book about balance")

def addition(book_addition, book_genre): #This function is supposed to allow the user to add any type of book with the title, author and one type of genre.
    book_addition = input("What book would you like to add onto your library? Example; Scythe, Neal Shusterman")
    library.add(book_addition)
    book_genre = input("What is that book about and its genre? Example; Scythe is a science fiction book about loss and immortality")
    library.add(book_genre)
    print(f"Here's you updated library! {library}")
    return(addition)

def removal(book_removal): #The function here allows the user to remove any type of book, removes the title, author, and type of genre by default.

    pass

removal()

def search_bar(book_search): #Lets you search for a specific known book by title, author, and genre.

    pass

search_bar()

def main(): #Main user interface

    while True:
        pers_libr = int(input("""Welcome to your personal library! What would you like to do?"
        Type 1 to view your library.
        Type 2 to add items into your library.
        Type 3 to remove items from your library.
        Type 4 to search up an item from your library.
        Type 5 to leave.\n"""))
        pass
        if pers_libr == 1:
            print(f"Here's your personal library, take a look! {library}")
        elif pers_libr == 2:
            upd_libr = addition(book_addition=, book_genre=)
            print("Here's your updated library")
        elif pers_libr == 3:
            pass
        elif pers_libr == 4:
            pass
        elif pers_libr == 5:
            print("Thank you for using your personal library, goodbye!")
            break
        elif pers_libr == "":
            print("You wrote nothing, try again.")
        else:
            print("This doesn't work, try again.")

main()