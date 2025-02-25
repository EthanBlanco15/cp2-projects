#Ethan Blanco, Movie Recommender

import csv
import os

#Load movies from the CSV file
def load_movies(filename):

    movies = []
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return movies  #Return an empty list to prevent crashes
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            #Ensure all expected fields exist in each row
            if "Title" in row and "Director" in row and "Genre" in row and "Rating" in row and "Length (min)" in row and "Notable Actors" in row:
                movies.append(row)
    return movies


#Filter movies based on user-selected criteria
def filter_movies(movies, filters):

    filtered_movies = movies
    for key, value in filters.items():
        if key == "Length (min)":
            try:
                max_length = int(value)
                filtered_movies = [movie for movie in filtered_movies if movie[key].isdigit() and int(movie[key]) <= max_length]
            except ValueError:
                print("Invalid length input. Please enter a number.")
                return []
        else:
            filtered_movies = [movie for movie in filtered_movies if value.lower() in movie[key].lower()]
    return filtered_movies


# Display movies in a readable format
def display_movies(movies):
    if not movies:
        print("\nNo movies match your filters.")
        return
    print("\nRecommended Movies:")
    for movie in movies:
        print(f"- {movie['Title']} ({movie['Director']}, {movie['Genre']}, {movie['Length (min)']} min)")

#Main program function
def main():

    filename = "movie_recommender/movies.csv"
    movies = load_movies(filename)
    if not movies:
        print("No movies loaded. Please check the file and try again.")
        return

    print("Welcome to the Movie Recommender!")
    while True:

        print("\nChoose at least two filters to refine your search:")
        print("1. Genre")
        print("2. Director")
        print("3. Maximum Length (min)")
        print("4. Notable Actors")
        print("5. Print full movie list")
        print("6. Exit")

        choice = input("\nEnter your choices (separate by commas, e.g., 1,3): ").split(',')
        choice = [c.strip() for c in choice]
        if "6" in choice:
            print("Goodbye!")
            break
        if "5" in choice:
            display_movies(movies)
            continue
        filters = {}
        if "1" in choice:
            genre = input("Enter the genre: ").strip()
            filters["Genre"] = genre
        if "2" in choice:
            director = input("Enter the director's name: ").strip()
            filters["Director"] = director
        if "3" in choice:
            length = input("Enter maximum movie length (in minutes): ").strip()
            filters["Length (min)"] = length  #Length validation is handled in filtering
        if "4" in choice:
            actor = input("Enter the actor's name: ").strip()
            filters["Notable Actors"] = actor
        if len(filters) < 2:
            print("\nPlease select at least two filters.")
            continue
        results = filter_movies(movies, filters)
        display_movies(results)
    main()