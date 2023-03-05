import random

def play_game(player1_name=None, player2_name=None):
    # Prompt the players to enter their names, if not already provided
    if not player1_name:
        player1_name = input("Enter Player 1 name: ")
    if not player2_name:
        player2_name = input("Enter Player 2 name: ")

    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Initialize the first player
    current_player = 1
    guess = int(input(f"{player1_name}, guess a number between 1 and 10: "))
    tries = 1

    # Keep looping until a player guesses the number
    while guess != secret_number:
        if guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        # Get the next player's guess
        if current_player == 1:
            guess = int(input(f"{player2_name}, guess a number between 1 and 10: "))
            current_player = 2
        else:
            guess = int(input(f"{player1_name}, guess a number between 1 and 10: "))
            current_player = 1
        tries += 1

    # The player has won!
    if current_player == 1:
        winner_name = player1_name
    else:
        winner_name = player2_name
    print(f"Congratulations, {winner_name}! You won! It took you {tries} tries to guess the number {secret_number}.")
    
    # Prompt the players to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        play_game(player1_name, player2_name)
    else:
        print("Thanks for playing!")
        
if __name__ == '__main__':
    play_game()
