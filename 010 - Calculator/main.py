from art import logo

#Add
def add(n1, n2):
    return n1 + n2
#Substract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2

calculations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?:\n"))
    
    want_to_continue = True
    while want_to_continue:
        operation_symbol = input("Pick one of the operations +, -, *, / :\n")
        num2 = float(input("What is the next number?:\n"))
        calculation_function = calculations[operation_symbol]
        result = calculation_function(num1, num2)
        # Print calculation as string, the result is rounded to 2 decimal points wihtout affectting float value stored in result.
        print(f"{num1} {operation_symbol} {num2} = {result: .2f}")
        
        if input((f"Type 'y' to contine calculating with {result}, otherwise type 'n' to restart calculator:\n").lower()) == "y":
            num1 = result
        else:
            want_to_continue = False
            calculator()

calculator()
