import random
import os
from game_data import data
from art import logo, vs

# Clear the console screen for better visibility.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Format the account data into a printable string.
def format_data(account):
    return f"{account['name']}, a {account['description']} from {account['country']}"

# Get a random account, avoiding the previous one if specified.
def get_random_account(previous=None):
    candidate = random.choice(data)
    while previous and candidate == previous:
        candidate = random.choice(data)
    return candidate

# Display the versus screen with current score.
def display_vs(a_account, b_account, score=0):
    clear_screen()
    # print(logo)
    if score > 0:
        print(f"\nCurrent score: {score}")
    print(f"\nCompare A: {format_data(a_account)}")
    print(vs)
    print(f"Compare B: {format_data(b_account)}")

# Get and validate user input.
def get_user_guess():
    while True:
        guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()
        if guess in ['A', 'B']:
            return guess
        print("Invalid input. Please type 'A' or 'B'.")

# Check if user's guess is correct and return comparison details.
def check_answer(guess, a_account, b_account):
    a_followers = a_account['follower_count']
    b_followers = b_account['follower_count']

    is_correct = (guess == 'A' and a_followers >= b_followers) or \
                 (guess == 'B' and b_followers > a_followers)

    return is_correct, a_followers, b_followers

# Display round results with follower counts.
def display_result(is_correct, score, a_followers, b_followers):
    print(f"\nA has {a_followers:,} followers")
    print(f"B has {b_followers:,} followers")

    if is_correct:
        print(f"\nCorrect! Your score is: {score}")
    else:
        print(f"\nSorry, that's wrong. Final score: {score}")

# Main game loop
def play_game():
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account(account_a)

    while game_should_continue:
        display_vs(account_a, account_b, score)
        guess = get_user_guess()

        is_correct, a_followers, b_followers = check_answer(guess, account_a, account_b)

        if is_correct:
            score += 1
            account_a = account_b
            account_b = get_random_account(account_a)
        else:
            game_should_continue = False

        display_result(is_correct, score, a_followers, b_followers)

    return score

# Main program with game loop and play again feature.
def main():
    while True:
        clear_screen()
        print(logo)
        print("\nWelcome to Higher or Lower!")
        print("Guess which social media account has more followers.")

        final_score = play_game()

        print(f"\nGame Over! Final Score: {final_score}")

        if input("\nPlay again? (y/n): ").lower() != 'y':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
