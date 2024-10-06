import random

# Function to simulate rolling a die
def roll():
    #  values provide karo ji
    min_value = 1
    max_value = 6
    # a random number will be given
    return random.randint(min_value, max_value)

# Input validation for number of players (between 2 and 4)
while True:
    players = input("Enter the number of players (2 - 4): ")
    # Check if the user is playing with us by giving wrong digit
    if players.isdigit():
        players = int(players)
        # Ensure the number of players is between 2 and 4
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

# The score needed to win
max_score = 50
# Initialize scores for all players 0
player_scores = [0 for _ in range(players)]

# Game loop: continue until one player's score reaches or exceeds the max_score
while max(player_scores) < max_score:
    # Iterate over each player
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn has started!")
        print(f"Your current total score is: {player_scores[player_idx]}\n")

        current_score = 0  # Reset score for current turn

        # Inner loop: keep rolling until the player decides to stop or rolls a 1
        while True:
            should_roll = input("Would you like to roll (y)? ")
            # If the player chooses not to roll, end the turn
            if should_roll.lower() != "y":
                break

            value = roll()  # Simulate the dice roll
            if value == 1:
                print("You rolled a 1! Turn over, no points added.")
                break  # End the turn if a 1 is rolled
            else:
                current_score += value  # Add the rolled value to the current turn's score
                print(f"You rolled a: {value}")
                print(f"Your current score this turn is: {current_score}")

        # Add the turn's score to the player's total score
        player_scores[player_idx] += current_score
        print(f"Player {player_idx + 1}'s total score is now: {player_scores[player_idx]}")

# Determine the winner
max_score = max(player_scores)  # Find the maximum score
winning_idx = player_scores.index(max_score)  # Get the index of the winning player
print(f"Player {winning_idx + 1} is the winner with a score of: {max_score}!") 
