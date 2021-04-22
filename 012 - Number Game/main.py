from art import logo
import random

# Lives set as global variables
EASY_LIVES = 10
HARD_LIVES = 5

def run_game():
    print(logo)
    print("Welcome to the random number guessing game!")
    print("I'm thinking of a number from 1 to 100.")
    random_number = random.randint(1, 100)
    # print(f"The secret number is {random_number}")
    # Set guess variable
    guess = 0
    # Get difficulty level and assign relevant number of lives.
    choose_difficulty = input("Choose a difficulty, 'Hard' or 'Easy'?: ").lower()
    if choose_difficulty == "hard":
        lives = HARD_LIVES
    else:
        lives = EASY_LIVES

    while guess != random_number or lives != 0:
        print(f"You have {lives} attempts left.")
        guess = int(input("Guess a number: "))
        if guess > random_number:
            print("Too High")
        elif guess < random_number:
            print("Too Low")
        elif guess == random_number:
            return print(f"You got it! The number was {random_number}")
        lives -= 1
        if lives == 0:
            return print("You lose, you ran out of lives.")

# Call run_game function
run_game()
