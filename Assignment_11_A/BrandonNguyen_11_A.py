# Name: Brandon Nguyen
# Date Created: 11/11/24
# Assignment: Exercise 11A

# Simulates a poker game where a user is dealt a hand of five cards.
# The user can replace a selected card by entering their number or press 'S' to stay and keep all cards.

import random
import time

# CONSTANT for the number of cards in a Poker hand
HAND_SIZE = 5


class Deck:
    def __init__(self):
        # Initialize a standard deck of 52 cards with suits and ranks
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [f"{rank} of {suit}" for suit in suits for rank in ranks]
        self.shuffle()

    def shuffle(self):
        # Shuffle the deck
        random.shuffle(self.cards)

    def deal(self, num_cards=HAND_SIZE):
        # Deal 5 cards from the top of the deck
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards


def display_hand(hand, message):
    # Display the hand of cards
    print(message)
    for i, card in enumerate(hand, 1):
        print(f"{i}: {card}")
    print()


# Function to replace selected cards in the user's hand
def replace_cards(deck, hand):
    while True:  # Loop until valid input is provided
        # Prompt the user to replace a card or to stay
        replace_input = input(
            "Enter a card number (1-5) to be replaced, or press 'S' to stay: "
        ).strip().upper()

        if replace_input == 'S':
            print("\nYou chose to stay. No cards were replaced.\n")
            return

        try:
            # Convert user input
            get_user_input = [
                int(num) - 1 for num in replace_input.split(',') if num.strip()
            ]

            # Validate that all entered numbers are within the valid range
            if not all(0 <= index < len(hand) for index in get_user_input):
                raise IndexError

            # Reshuffle the deck before dealing the new card
            print("\nReshuffling the deck and dealing new cards...\n")
            time.sleep(2)
            deck.shuffle()

            # Replace the specified card with a new card from the deck
            new_cards = deck.deal(len(get_user_input))
            for old_card, new_card in zip(get_user_input, new_cards):
                hand[old_card] = new_card

            return  # Exit the loop and function after successful replacement

        except (ValueError, IndexError):
            # Prompt user if input is invalid
            print("\nError! Invalid input. Please enter a valid card number.\n")


# Main function to play the Poker game
def main():
    # Greet the user and set up the initial game state
    print("Welcome to the Poker Table!")
    print("Shuffling the deck and dealing your hand...\n")
    time.sleep(2)  # Simulate shuffling and dealing

    # Create a new deck and deal the starting hand
    deck = Deck()
    hand = deck.deal()

    # Display the user's initial hand
    display_hand(hand, "Your starting hand:")

    # Allow the user to replace cards or stay
    replace_cards(deck, hand)

    # Display the user's final hand after replacement
    display_hand(hand, "Your final hand:")
    print("Thanks for playing!")  # Thank the user for playing


# Run the main function
main()
