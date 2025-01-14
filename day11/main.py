import random
from art import logo

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculate the score of a hand, handling Aces appropriately."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    while sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return sum(cards)

def compare_score(user_score, computer_score):
    """Compare scores and return the game outcome."""
    if user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score == computer_score:
        return "It's a draw!"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif computer_score == 0:
        return "You lose, computer has Blackjack!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print(logo)
    print("\nWelcome to Blackjack!")

    # Initial deal
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    game_over = False

    # User's turn
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if should_continue == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show final hands and outcome
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))

# Game loop
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_game()

print("\nThanks for playing!")
