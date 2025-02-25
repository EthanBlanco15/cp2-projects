#Ethan Blanco, Movie Recommender

import csv

#Load movies from the CSV file
def load_movies(filename):
    movies = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append(row)
    return movies

#Filter movies based on user preferences
def filter_movies(movies, filters):
    filtered_movies = movies
    for key, value in filters.items():
        filtered_movies = [movie for movie in filtered_movies if value.lower() in movie[key].lower()]
    return filtered_movies

#Display movies in a formatted way
def display_movies(movies):
    if not movies:
        print("\nNo movies match your filters.")
        return
    print("\nRecommended Movies:")
    for movie in movies:
        print(f"- {movie['Title']} ({movie['Director']}, {movie['Genre']}, {movie['Length (min)']} min)")

#Main function to run the program
def main():
    filename = "movies.csv"  # Change this if your file has a different name
    movies = load_movies(filename)
    print("Welcome to the Movie Recommender!")
    while True:
        print("\nChoose at least two filters to refine your search:")
        print("1. Genre")
        print("2. Director")
        print("3. Length (min)")
        print("4. Notable Actors")
        print("5. Print full movie list")
        print("6. Exit")

        choice = input("\nEnter your choice (separate by commas, e.g., 1,3): ").split(',')
        choice = [c.strip() for c in choice]

        if "6" in choice:
            print("Goodbye!")
            break

        if "5" in choice:
            display_movies(movies)
            continue

        filters = {}
        if "1" in choice:
            genre = input("Enter the genre: ")
            filters["Genre"] = genre
        if "2" in choice:
            director = input("Enter the director's name: ")
            filters["Director"] = director
        if "3" in choice:
            length = input("Enter maximum movie length (in minutes): ")
            try:
                filters["Length (min)"] = str(int(length))  # Ensure input is a valid number
            except ValueError:
                print("Invalid length input. Please enter a number.")
                continue
        if "4" in choice:
            actor = input("Enter the actor's name: ")
            filters["Notable Actors"] = actor

        if len(filters) < 2:
            print("\nPlease select at least two filters.")
            continue

        results = filter_movies(movies, filters)
        display_movies(results)
    main()
