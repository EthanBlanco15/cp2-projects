#Ethan Blanco, Updated Personal Library

# Initialize library and genre database 
"""
library_dict = {{"Harry Potter-Philosophers Stone":
                
                "author": "J. K. Rowling",
                "genre": "Harry Potter is a comedy book about wizardry",
                "pages": "309"}
                {
                "Wonder":
                "author": "R. J. Palacio"
                "genre": "Wonder is a fiction book about individuality"
                }
                }"""
genres = { "Harry Potter, by J. K. Rowling": "Harry Potter is a comedy book about wizardry", "Wonder, R. J. Palacio": "Wonder is a fiction book about individuality", "The Amazing Spider-Man, Stan Lee": "The Amazing Spider-Man is an action book about balance" } 

def add_book():

    #Adds a new book and its description to the library. Prompts the user to input a book title, author, and a brief description with its genre.
    book_title = input("Enter the book title and author (e.g., Scythe, Neal Shusterman):\n") 
    if book_title in library_dict:
        return f"'{book_title}' is already in your library."
    book_description = input(f"Provide a brief description of '{book_title}' along with its genre:\n")
    library_dict.add(book_title)
    genres[book_title] = book_description
    return f"Book added successfully! Here's your updated library: {library_dict}"

add_book()

def remove_book(): #Removes a book and its description from the library. Prompts the user to specify the book title and author for removal.
    
    book_title = input("Enter the title and author of the book to remove (e.g., Scythe, Neal Shusterman):\n") 
    if book_title in library_dict: 
        library_dict.remove(book_title) 
        genres.pop(book_title, None) 
        return f"'{book_title}' has been removed. Here's your updated library: {library_dict}" 
    else:
        return f"'{book_title}' is not in your library. Please try again." 
    
remove_book()

def search_library(): #Searches for books in the library based on a keyword. The user can search by title, author, or genre keyword.
    
    keyword = input("Enter a keyword to search (title, author, or genre):\n").lower()
    results = [] 
    for book in library_dict: 
        if keyword in book.lower() or keyword in genres.get(book, "").lower(): 
            results.append(f"{book}: {genres[book]}") 
            if results:
                return "Search results:\n" + "\n".join(results) 
        else: 
            return "No books found matching your search. Please try again." 
        
search_library()

def library_def():

    #Lets the user pick to choose whether they want a detailed or simplified version of the library dictionary
    pass

def main(): #Main menu for the personal library program. Allows the user to view, add, remove, or search for books, or exit the program.
    while True:
        print("Welcome to your Personal Library!")  
        choice = int(input(""" What would you like to do? Please choose an option:
            1. View your library
            2. Add a book 
            3. Remove a book 
            4. Search your library 
            5. Exit Enter your choice:\n""")) 
        if choice == 1: 
                library_def()
        elif choice == 2: 
            print(add_book()) 
        elif choice == 3: 
            print(remove_book()) 
        elif choice == 4: 
            print(search_library()) 
        elif choice == 5: 
            print("Thank you for using your personal library. Goodbye!")
        else:
            print("This doesn't work")
        break 

main() #Run the program