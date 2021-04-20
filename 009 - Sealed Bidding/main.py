from replit import clear
from art import logo

print(logo) 

bids = {}
    
run_auction = True
while run_auction:
    name = input("Hello, what is your name?:\n")
    bid = int(input("How much would you like to bid?:\n£"))
    bids[name] = bid
    continue_bidding = input("Is there anybody else that would like to bid? Type 'Yes' or 'No':\n").lower()
    if continue_bidding == "no":
        run_auction = False
    else:
        clear()

#Determine Winner and print.
highest_bid = 0
winner = ""
for bid in bids:
    if bids[bid] > highest_bid:
        highest_bid = bids[bid]
        winner = bid
clear()
print(f"The winner is {winner} with a bid of £{highest_bid}")
