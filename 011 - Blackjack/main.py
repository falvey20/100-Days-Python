import random
from replit import clear
from art import logo

# List all card values and return a random card from List
def deal_card():
    cards_in_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards_in_deck)

# Determines if Blackjack is met and returns 0.
# If Ace(11) is in hand and sum is over 21, remove 11 and append 1.
def total(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0 
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

# Compare player_total and dealer_total.print.
# Called after player and dealer have finished turns in play_game()
def compare(player_total, dealer_total):
    if player_total == dealer_total:
        print("It's a Draw.")
    elif player_total == 0:
        print("You win, You got Blackjack!")
    elif dealer_total == 0:
        print("You Lose, Dealer got Blackjack.")
    elif player_total > 21:
        print("Bust! You went over 21.")
    elif dealer_total > 21:
        print("You win, Dealer went over 21.")
    elif player_total > dealer_total:
        print("You Win, you got a higher score than the Dealer.")
    elif player_total < dealer_total:
        print("You lose, the Dealer scored higher than you.")

# Play Game.
def play_game():
    print(logo)
    dealer_hand = []
    player_hand = []
    for i in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())
    # Initial deal.
    player_finished = False
    while player_finished == False:
        player_total = total(player_hand)
        dealer_total = total(dealer_hand)
        print(f"Player Hand: {player_hand} Total: {player_total}")
        print(f"Dealer's first card: {dealer_hand[0]}")
        # If player goes bust or if either player or dealer have blackjack, the game is over.
        if player_total == 0 or dealer_total == 0 or player_total > 21:
            player_finished = True
        else:
            another_card = input("Do you want another card, y or n? ")
            if another_card == "y":
                player_hand.append(deal_card())
            else:
                player_finished = True
    # Dealers turn, if blackjack was not already met or if dealer_total < 17 must deal card.
    while total(dealer_hand) != 0 and total(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        dealer_total = total(dealer_hand)
    # Print final hands and totals for player and dealer.
    print(f"Final Player Hand: {player_hand} Total: {player_total}")
    print(f"Final Dealer Hand: {dealer_hand} Total: {dealer_total}")
    # Call compare funtion which will return a print statement of the result.
    compare(player_total, dealer_total)

# If user wants ty play clear the terminal and call play_game()
while input("Would you like to play a game of Blackjack: 'y' or 'n'? ") == "y":
    clear()
    play_game()
