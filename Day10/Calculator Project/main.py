import art

print(art.logo)

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
    "/": divide,
}

def calculator():
    continue_calc = True
    num1 = int(input("Enter first number "))
    while continue_calc:
        op = input("Enter operation */+- ")
        num2 = int(input("Enter second number "))
        result = operations[op](num1, num2)
        print(result)

        cont = input("Do you want to continue (y/n/x)? ")
        if cont == "y":
            num1 = result
        elif cont == "x":
            continue_calc = False
        elif cont == "n":
            num1 = int(input("Enter first number "))

calculator()
