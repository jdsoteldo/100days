
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    anotherOne = True
    x = float(input("First number: "))

    for symbol in operations:
        print(symbol)

    while anotherOne:
        operation_symbol = input("Pick an operation: ")
        y = float(input("Next Number: "))

        calculation = operations[operation_symbol]
        answer = calculation(x, y)
        print(f"{x} {operation_symbol} {y} = {answer}")
        keep = input(f"Type 'y' to continue calculating with {answer} or type 'n' to quit.\n")

        if keep == 'y':
            x = answer
        else:
            print("Bye")
            anotherOne = False

calculator()
