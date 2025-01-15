import random
from art import logo

def guess_the_number():
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    print(logo)
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    # Ask the user for difficulty
    difficulty = input("Choose difficulty - 'easy' or 'hard': ").lower()
    attempts = 10 if difficulty == 'easy' else 5

    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))

        if guess == number_to_guess:
            print(f"🎉 Correct! The number was {number_to_guess}. You win!")
            break
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Too low!")

        attempts -= 1

        if attempts == 0:
            print(f"Game over! The number was {number_to_guess}.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        guess_the_number()
    else:
        print("Thanks for playing! Goodbye. 😊")

# Start the game
guess_the_number()
