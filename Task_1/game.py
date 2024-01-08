import random

def get_valid_guess():
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit():
            return guess
        print("Invalid input. Please enter a multi-digit number.")

def compare_numbers(secret, guess):
    # Compare the secret number and the guess, and return a hint
    hint = ""
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            hint += "O"  # O means correct number at the correct position
        elif guess[i] in secret:
            hint += "X"  # X means correct number but at the wrong position
        else:
            hint += "-"  # - means incorrect number
    return hint

def player_turn(player_name):
    print(f"{player_name}'s turn.")
    secret = get_valid_guess()
    return secret

def main():
    print("Welcome to the Mastermind game!")

    # Player 1's turn
    player1_secret = player_turn("Player 1")

    # Player 2's turn
    player2_attempts = 0
    while True:
        player2_attempts += 1
        player2_guess = get_valid_guess()
        hint = compare_numbers(player1_secret, player2_guess)
        print("Hint:", hint)

        if hint == "O" * len(player1_secret):
            print("Congratulations! Player 2 wins!")
            break

    # Player 2's number has been guessed, now Player 1's turn
    print("Player 2's number has been guessed. Now, it's Player 1's turn.")
    player1_attempts = 0
    while True:
        player1_attempts += 1
        player1_guess = get_valid_guess()
        hint = compare_numbers(player2_guess, player1_guess)
        print("Hint:", hint)

        if hint == "O" * len(player2_guess):
            print("Congratulations! Player 1 wins!")
            break

    # Check who wins
    if player1_attempts == player2_attempts:
        print("It's a tie! Both players are Masterminds!")
    elif player1_attempts < player2_attempts:
        print("Player 1 is the Mastermind!")
    else:
        print("Player 2 is the Mastermind!")

if __name__ == "__main__":
    main()