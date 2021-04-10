print("Welcome to the bill splitter!")

bill = float(input("How much is the total bill? : \n$"))
tip_percentage = float(input("What percentage tip would you like to give? eg. 5, 10, 20:\n"))
num_of_people = int(input("How many people are splitting the bill? :\n"))

tip_dollar_value = bill * (tip_percentage / 100)
total_bill = bill + tip_dollar_value
each_pay = round(total_bill / num_of_people, 2)

print(f"Each person should pay ${each_pay}")
