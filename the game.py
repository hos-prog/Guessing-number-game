# AdemHosama
# Final Day 12 project from Angela Yu

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    """Asks the user to choose a difficulty and returns the number of attempts."""
    level = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input, defaulting to 'easy'.")
        return EASY_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = randint(1, 100)
    attempts = set_difficulty()
    won = False

    while attempts > 0:
        print(f"\nYou have {attempts} attempt(s) remaining.")
        guess = int(input("Make a guess: "))

        if guess > answer:
            print("Too high.")
        elif guess < answer:
            print("Too low.")
        else:
            print(f"You got it! The answer was {answer}.")
            won = True
            break

        attempts -= 1
        if attempts > 0:
            print("Guess again.")

    if not won:
        print(f"You've run out of guesses. You lose! The number was {answer}.")

# Start the game
game()
