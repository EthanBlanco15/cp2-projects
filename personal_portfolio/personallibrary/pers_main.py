#Ethan Blanco, Updated Personal Library

# Personal Library Management System
# Dictionary of store book details
book_library = {
    "Harry Potter-Philosopher's Stone": {
        "Author": "J.K. Rowling",
        "Time": "1981",
        "Genre": "Comedy, Wizardry",
        "Description": "Harry Potter is a comedy about wizardry.",
        "Pages": 309
    },
    "Wonder": {
        "Author": "R.J. Palacio",
        "Time": "2012",
        "Genre": "Fiction, Individuality",
        "Description": "Wonder is a fictional book about individuality.",
        "Pages": 310
    },
    "The Amazing Spider-Man": {
        "Author": "Stan Lee",
        "Time": "2013",
        "Genre": "Balance, Heroism",
        "Description": "The Amazing Spider-man is an action book about balance.",
        "Pages": 384
    },
    "To Kill a Mockingbird":{
        "Author": "Harper Lee",
        "Time": "1933-1935",
        "Genre": "Domestic fiction, thriller",
        "Description": "To Kill a Mockingbird is an intense book about racial prejudice.",
        "Pages": 336
    }
}
# Function to add a new book
def add_book():

    #Adds a new book to the library.
    book_title = input("Enter the book title and author (e.g., Scythe, Neal Shusterman): ").strip()
    if not book_title:
        print("Book title cannot be empty.")
        return

    if book_title in book_library:
        print(f"'{book_title}' is already in your library.")
        return
    author = input("Enter the author's name: ").strip()
    publication_year = input("Enter the year it takes place: ").strip()
    genre = input("Enter the book's genre: ").strip()
    description = input("Provide a brief description of the book: ").strip()
    pages = input("Enter the number of pages: ").strip()
    if not pages.isdigit():
        print("Pages must be a valid number.")
        return

    book_library[book_title] = {
        "Author": author,
        "Publication Year": publication_year,
        "Genre": genre,
        "Description": description,
        "Pages": int(pages)
        # Store pages as an integer
    }

    print(f"'{book_title}' has been added successfully!")
    display_library(sample=True)

# Function to remove a book
def remove_book():

    #Removes a book from the library.
    book_title = input("Enter the title and author of the book to remove: ").strip()
    if not book_title:
        print("Book title cannot be empty.")
        return

    if book_title in book_library:
        del book_library[book_title]
        print(f"'{book_title}' has been removed successfully!")
        display_library(sample=True)
    else:
        print(f"'{book_title}' is not in your library. Please try again.")

# Function to search for a book
def search_books():

    #Searches for books by title, author, or genre.
    keyword = input("Enter a keyword to search (title, author, or genre): ").strip().lower()
    if not keyword:
        print("Search keyword cannot be empty.")
        return
    results = []
    for title, details in book_library.items():
        if keyword in title.lower() or any(keyword in str(value).lower() for value in details.values()):
            results.append(f"\nTitle: {title}\n" + "\n".join([f"  {k}: {v}" for k, v in details.items()]))
    if results:
        print("\nSearch Results:")
        print("\n".join(results))
    else:
        print("No matches were found.")

# Function to update book details
def update_book():

    #Allows the user to update details of an existing book.
    book_title = input("Enter the title of the book you want to update: ").strip()

    if not book_title:
        print("Book title cannot be empty.")
        return

    if book_title not in book_library:
        print(f"'{book_title}' is not in your library. Please try again.")
        return

    print("\nCurrent book details:")
    for key, value in book_library[book_title].items():
        print(f"{key}: {value}")

    print("\nWhat would you like to update?")
    options = ["Author", "Publication Year", "Genre", "Description", "Pages"]
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    choice = input("Enter the number of the field you want to update: ").strip()

    if not choice.isdigit() or not (1 <= int(choice) <= len(options)):
        print("Invalid choice. Please enter a valid number.")
        return
    field_to_update = options[int(choice) - 1]
    new_value = input(f"Enter the new value for {field_to_update}: ").strip()

    if field_to_update == "Pages" and not new_value.isdigit():
        print("Pages must be a valid number.")
        return
    book_library[book_title][field_to_update] = int(new_value) if field_to_update == "Pages" else new_value
    print(f"'{book_title}' has been updated successfully!")
    display_library(sample=True)

# Function to display the library (sample or full view)
def display_library(sample=False):

    #Displays either a sample or the full library."""
    if not book_library:
        print("Your library is currently empty.")
        return
    print("\nYour Personal Library:")
    if sample:
        # Show only the first 2 books as a sample
        count = 0
        for title, details in book_library.items():
            print(f"\nTitle: {title}")
            print(f"  Author: {details['Author']}")
            print(f"  Genre: {details['Genre']}")
            if count == 1:  # Display only two samples
                print("\n... (View full library for more)")
                break
            count += 1
    else:
        # Show full details
        for title, details in book_library.items():
            print(f"\nTitle: {title}")
            for key, value in details.items():
                print(f"  {key}: {value}")

# Function to allow the user to choose how to view the library
def view_library():

    #Allows the user to view either the full library or a summary.
    choice = input("Press 1 to view a sample of the library or 2 to see the full details: ").strip()
    if choice == "1":
        display_library(sample=True)
    elif choice == "2":
        display_library()
    else:
        print("Invalid input. Please try again.")

# Main function to run the program
def lib_main():

    #Runs the personal library
    while True:
        print("\nWelcome to your Personal Library!")
        choice = input(
            "What would you like to do?\n"
            "1. View personal library\n"
            "2. Add a book\n"
            "3. Remove a book\n"
            "4. Search for a book\n"
            "5. Update book details\n"
            "6. Exit\n"
            "Enter your choice: "

        ).strip()

        if choice == "1":
            view_library()
        elif choice == "2":
            add_book()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            search_books()
        elif choice == "5":
            update_book()
        elif choice == "6":
            print("Thank you for using your personal library. Goodbye!")
            break
        else:
            print("Invalid selection. Please enter a number from 1 to 6.")

# Run the program
if __name__ == "__main__":
    lib_main()