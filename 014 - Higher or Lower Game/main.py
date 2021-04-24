from art import logo, vs
from game_data import data
import random
from replit import clear

# # Data Format
# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     } ]

# Compare Function takes arguements from game.
def compare_followers(option1, option2, choice):
    a = option1['follower_count']
    b = option2['follower_count']
    # differentite between awin and bwin
    if a > b and choice == "a":
        return "win"
    elif a < b and choice == "b":
        return "win"
    elif a == b:
        return "win"
    else: 
        return "lose"

def game():
    score = 0
    # option1 outside of while loop as will contain value of previous correct guess and is not randomised again.
    option1 = random.choice(data)

    game_over = False
    while not game_over:
        print(logo)
        # Only start to show score after 1st correct guess.
        if score > 0:
            print(f"Correct! Your current score is {score}")
        option2 = random.choice(data)
        while option2 == option1:
            option2 = random.choice(data)
        print(f"Compare A: {option1['name']}, a {option1['description']}, from {option1['country']}.")
        print(vs)
        print(f"Compare B: {option2['name']}, a {option2['description']}, from {option2['country']}.")
        
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear()
        # if option A is selected and correct it will stay the same for the next game.
        # Otherwise if B was selected and correct, it become the first option in the next game.
        if compare_followers(option1, option2, choice) == "win":
            score += 1
            option1 = option2
        else:
            game_over = True
            print(logo)
            return print(f"Wrong, Game Over, your final score was {score}")

# Call game function
game()
