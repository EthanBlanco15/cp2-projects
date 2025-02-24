#Ethan Blanco, Movie Recommender

import pandas as pd
#Load the dataset

df = pd.movie_recommender/movies.csv("movies.csv")
df["Length (min)"] = pd.to_numeric(df["Length (min)"], errors="coerce")
#Ensure 'Length (min)' is properly converted to numeric values (handling errors)

def display_full_list():

    #Displays the entire movie list.
    print("\nFull Movie List:")
    print(df.to_string(index=False))


def recommend_movies():

    #Provides movie recommendations based on at least two selected filters.
    print("\nMovie Recommender")
    print("Choose at least two filters: Genre, Director, Length, or Actor.")

    #Available filters
    filters = {
        "1": "Genre",
        "2": "Director",
        "3": "Length (max runtime in minutes)",
        "4": "Actor"
    }

    #Display filter options
    print("\nAvailable filters:")
    for key, value in filters.items():
        print(f"{key}: {value}")

    #User selects at least two filters
    selected_filters = []
    while len(selected_filters) < 2:
        choices = input("\nEnter at least two filter numbers, separated by spaces (e.g., 1 3): ").split()
        selected_filters = [filters.get(choice) for choice in choices if choice in filters]

        if len(selected_filters) < 2:
            print("Invalid selection. You must select at least two filters.")

    #Collect user input for selected filters
    filter_values = {}
    for filter_type in selected_filters:
        value = input(f"Enter a value for {filter_type} (or leave blank to skip): ").strip().lower()
        if value:
            filter_values[filter_type] = value

    #Apply filters
    filtered_df = df.copy()

    if "Genre" in filter_values:
        filtered_df = filtered_df[filtered_df["Genre"].str.lower().str.contains(filter_values["Genre"], na=False, regex=False)]
    if "Director" in filter_values:
        filtered_df = filtered_df[filtered_df["Director"].str.lower().str.contains(filter_values["Director"], na=False, regex=False)]
    if "Length (max runtime in minutes)" in filter_values and filter_values["Length (max runtime in minutes)"].isdigit():
        max_length = int(filter_values["Length (max runtime in minutes)"])
        filtered_df = filtered_df[filtered_df["Length (min)"] <= max_length]
    if "Actor" in filter_values:
        filtered_df = filtered_df[filtered_df["Notable Actors"].str.lower().str.contains(filter_values["Actor"], na=False, regex=False)]

    #Display results
    if filtered_df.empty:
        print("\nNo movies match the selected criteria.")
    else:
        print("\nRecommended Movies:")
        print(filtered_df[["Title", "Director", "Genre", "Rating", "Length (min)", "Notable Actors"]].to_string(index=False))

#Main menu
while True:
    print("\nMovie Recommendation System")
    print("1: Get Movie Recommendations")
    print("2: Print Full Movie List")
    print("3: Exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        recommend_movies()
    elif choice == "2":
        display_full_list()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")