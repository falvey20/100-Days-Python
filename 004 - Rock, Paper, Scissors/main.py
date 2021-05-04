import random

options = ["rock 🗿", "paper 🧾", "scissors 🔪"]
num_of_options = len(options)

user_input = (int(input("Type 1 for rock, 2 for paper, 3 for scissors\n")) - 1)
computer_random = (random.randint(0, num_of_options) - 1)

user_choice = options[user_input]
computer_choice = options[computer_random]

print(f"You chose {user_choice}")
print(f"The computer chose {computer_choice}")

if user_input == computer_random:
  print("You picked the same, it's a draw!")
elif user_input == 0 and computer_random == 1:
  print("Computer Wins, paper beats rock.")
elif user_input == 0 and computer_random == 2:
  print("You win! Rock beats Scissors.")
elif user_input == 1 and computer_random == 0:
  print("You win! Paper beats Rock.")
elif user_input == 1 and computer_random == 2:
  print("Computer Wins, Scissors beat Paper.")
elif user_input == 2 and computer_random == 0:
  print("Computer Wins, Rock beats Scissors.")
elif user_input == 2 and computer_random == 1:
  print("You win! Scissors beat Paper.")
