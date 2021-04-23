# Corrected indents.

for number in range(1, 101):
    # Corrected or to and to chekc that both conditions are met for FizzBuzz.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        # Corrected arguement (taken out of list brackets)
        print(number)
