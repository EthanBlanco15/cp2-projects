#Ethan Blanco, Upgrading Battle Simulator
import csv
import os
import random
from faker import Faker

#
#
#Needs new requirements
#
#

CHARACTER_FILE = "player.csv"
fake = Faker()

def main(): # The first thing the user sees, it allows you to create players and view them, start a battle and leave by inputting numbers

    #Main menu for RPG Player Management and Battle System.
    while True:
        print("\nBattle Simulator")
        print("1. Create Player")
        print("2. View Players")
        print("3. Start Battle")
        print("4. Random Player Generation")
        print("5. Player Data Analysis.")
        print("6. Player Visualization.")
        print("7. Exit")
        decision = input("Enter your decision: ").strip()
        if decision == "1":
            create_player()
        elif decision == "2":
            display_players()
        elif decision == "3":
            battle_system()
        elif decision == "4":
            rand_player_gen()
        elif decision == "5":
            player_analysis()
        elif decision == "6":
            player_visualization()
        elif decision == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid decision. Please enter a number between 1 and 4.")

def create_player():
    # Creates a new player and saves it to a CSV file.
    def get_valid_input(prompt, min_value=1, max_value=100):
        # Helper function to get valid integer input within a range.
        while True:
            try:
                value = int(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else: # Error message
                    print(f"Please enter a value between {min_value} and {max_value}.")
            except ValueError: # Error message
                print("Invalid input. Please enter a number.")

    print("\nCreate a New Player")
    use_random = input("Generate a random player? (yes/no): ").strip().lower()
    # The process of making a character, this allwos you to generate a random character with info
    if use_random == "yes":
        name = fake.name()
        description = fake.sentence()
        health = random.randint(50, 200)
        strength = random.randint(5, 50)
        defense = random.randint(5, 50)
        speed = random.randint(1, 20)
    else: # The other option allows you to create your character with a name, description, health points, strength, defense, and speed
        name = input("Enter player name: ").strip()
        description = input("Enter player description: ").strip()
        health = get_valid_input("Enter Health (50-200): ", 50, 200)
        strength = get_valid_input("Enter Strength (5-50): ", 5, 50)
        defense = get_valid_input("Enter Defense (5-50): ", 5, 50)
        speed = get_valid_input("Enter Speed (1-20): ", 1, 20)
    # Level and experience cannot be changed by user input
    level = 1   # All characters start with level 1 and 0 experience
    experience = 0

    # Saves the players info
    player = [name, description, health, strength, defense, speed, level, experience]
    save_player(player)
    print(f"Player '{name}' created successfully!")

def save_player(player): # Every new player is saved onto a csv file
    
    #Saves a player to the CSV file without overwriting existing ones.
    file_exists = os.path.isfile(CHARACTER_FILE)
    
    with open(CHARACTER_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Description", "Health", "Strength", "Defense", "Speed", "Level", "Experience"])
        writer.writerow(player)

def load_players(): # Saved players can be loaded to be viewed or brought to battle
    
    #Loads players from the CSV file, ensuring correct data format.
    if not os.path.isfile(CHARACTER_FILE):
        return []
    
    players = []
    with open(CHARACTER_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        headers = next(reader, None)  # Read headers and ignore them in data
        for row in reader:
            if len(row) == 7:
                players.append(row)
    
    return players

def display_players(): # When loaded, players can be displayed

    #Displays all saved players.
    players = load_players()
    if not players:
        print("No players found. Create one first.")
        return

    print("\nSaved Players:")
    for char in players:
        print(f"Name: {char[0]}, Health: {char[1]}, Strength: {char[2]}, Defense: {char[3]}, Speed: {char[4]}, Level: {char[5]}, XP: {char[6]}")

def rand_player_gen():
    
    print("\nThis does nothing right now.")


def player_analysis():

    #Performs statistical analysis on character attributes.
    df = load_players()
    if df.empty:
        return

    print("\nCharacter Statistics:")
    stats = df[["Health", "Strength", "Defense", "Speed"]].describe()
    print(stats)


def player_visualization():

    print("\nThere is nothing here at the moment.")


def battle_system(): # Players can fight each other if they are saved and loaded
    
    #Manages turn-based battles where players choose actions.
    players = load_players()
    if len(players) < 2:
        print("Not enough players to start a battle. Create at least two.")
        return

    print("\nSelect two players for battle:")
    for i, char in enumerate(players):
        print(f"{i+1}. {char[0]}")
    #You must have at least two player to fight, and the fight is all turn based
    try:
        p1_index = int(input("Select first player (number): ")) - 1
        p2_index = int(input("Select second player (number): ")) - 1
        if p1_index == p2_index or not (0 <= p1_index < len(players)) or not (0 <= p2_index < len(players)):
            print("Invalid selection. Please choose two different players.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    player1 = players[p1_index]
    player2 = players[p2_index]
    #All turn based code
    player1 = {key: int(value) if key not in ["Name"] else value for key, value in zip(
        ["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"], player1)}
    player2 = {key: int(value) if key not in ["Name"] else value for key, value in zip(
        ["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"], player2)}

    print(f"\n{player1['Name']} VS {player2['Name']} - Battle Start!")

    while player1["Health"] > 0 and player2["Health"] > 0:
        for attacker, defender in [(player1, player2), (player2, player1)]:
            print(f"\n{attacker['Name']}'s turn! Choose an action:")
            print("1. Attack")
            print("2. Defend")
            
            action = input("Enter your choice: ").strip()
            if action == "1":
                damage = max(1, attacker["Strength"] - defender["Defense"] // 2)
                defender["Health"] = max(0, defender["Health"] - damage)
                print(f"{attacker['Name']} attacks {defender['Name']} for {damage} damage!")
            elif action == "2":
                attacker["Defense"] += 2
                print(f"{attacker['Name']} braces for impact, increasing defense!")
            #Winner of the battle is determined if the opponents health reaches zero, winner gains experience and a level up
            if defender["Health"] == 0:
                print(f"{attacker['Name']} wins the battle!")
                attacker["Experience"] += 10
                level_up(attacker)
                update_player_stats(player1)
                update_player_stats(player2)
                return

def level_up(player): # With every level up, the player gains a stat boost
    
    #Levels up a player if they gain enough experience.
    if player["Experience"] >= player["Level"] * 10:
        player["Level"] += 1
        player["Health"] += 10
        player["Strength"] += 2
        player["Defense"] += 2
        print(f"{player['Name']} has leveled up to Level {player['Level']}!")

def update_player_stats(player): # Everytime the stats on a player is updated, the new info is saved onto the csv file
    
    #Updates an existing players stats in the CSV file after a battle.
    players = load_players()
    
    for i, char in enumerate(players):
        if char[0] == player["Name"]:  
            players[i] = [
                player["Name"], player["Health"], player["Strength"], 
                player["Defense"], player["Speed"], player["Level"], player["Experience"]
            ]
    
    with open(CHARACTER_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Health", "Strength", "Defense", "Speed", "Level", "Experience"])
        writer.writerows(players)

if __name__ == "__main__":
    main()