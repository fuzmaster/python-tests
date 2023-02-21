import random

def play_game():
    # Prompt the player to enter their name
    player_name = input("Enter your name: ")

    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Prompt the player to guess the number
    guess = int(input("Guess a number between 1 and 10: "))
    tries = 1

    # Keep looping until the player guesses the number
    while guess != secret_number:
        if guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        # Get the player's next guess
        guess = int(input("Your guess: "))
        tries += 1

    # The player has won!
    print(f"Congratulations, {player_name}! You won! It took you {tries} tries to guess the number {secret_number}.")
    
    # Prompt the player to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == '__main__':
    play_game()
