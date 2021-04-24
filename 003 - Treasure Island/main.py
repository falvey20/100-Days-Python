print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

left_or_right = input("You come to a fork in the road do you want to go 'Left' or 'Right'?\n").lower()
if left_or_right == "right":
  print("You fell down a hole, GAME OVER!")
else:
  wait_or_swim = input("You reach a dock, there is a boat in the distance, do you want to 'Wait' or 'Swim'?\n").lower()
  if wait_or_swim == "swim":
    print("A strong current got hold of you, GAME OVER!")
  else:
    door_choice = input("You get off the boat on the other side, there are three doors. Do you enter the 'Red', 'Blue' or 'Yellow' door?\n").lower()
    if door_choice == "red" or door_choice == "blue":
      print("It was a trap, GAME OVER!")
    else:
      print("Congratulations, you found the treasure! YOU WIN!")
