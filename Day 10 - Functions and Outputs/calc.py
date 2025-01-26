import calc_art

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Todo - Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operation to perform the calculation. Multiply 4 * 8 using the dictionary.

# print(f"{operations['*'](4,8)}")

def calculator():
    print(calc_art.logo)
    should_accumulate = True

    num1 = float(input("What's the first number:? "))

    while should_accumulate:
        
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number:? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()