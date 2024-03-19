import random
import sys

# Creating Random numbers between 1 to 6
def roll():
    """Rolls a die and returns a random number between 1 and 6."""
    return random.randint(1, 6)

# Function to validate player input and return number of players
def get_number_of_players():
    """Validates user input for the number of players (2-4)."""
    while True:
        players = input('Number of players (2-4): ')
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                return players
            else:
                print('Must be between 2 and 4 players.')
        else:
            print('Invalid! Please enter a number between 2 and 4.')

# Main game loop
def play_pig_dice():
    """Manages the entire Pig Dice game."""

    total_game_score = 100  # Target score to win
    players = get_number_of_players()
    player_scores = [0] * players  # List to store player scores

    while max(player_scores) < total_game_score:
        for player_idx in range(players):
            print(f'\nPlayer {player_idx + 1} turn has started')
            print(f'Your total score: {player_scores[player_idx]} \n')

            current_player_score = 0  # Initialize current score to 0 for each player's turn
            while True:
                should_roll = input('Do you want to roll again (y), hold (h), or quit (q)? ')
                should_roll = should_roll.lower()

                if should_roll == 'y':
                    value = roll()
                    if value == 1:
                        print('Oops! Rolled a 1. Turn ends!')
                        current_player_score = 0  # Reset current score to 0
                        break
                    else:
                        current_player_score += value
                        print(f'Current score: {value}')
                elif should_roll == 'h':
                    player_scores[player_idx] += current_player_score
                    print(f'Your total score is: {player_scores[player_idx]}')
                    break
                elif should_roll == 'q':
                    sys.exit()
                else:
                    print('Invalid input. Please enter y, h, or q.')

    winning_player = player_scores.index(max(player_scores))
    print(f'Player {winning_player + 1} is the winner with score: {max(player_scores)}')

# Start the game
play_pig_dice()