def calculator():
    print("****Welcome to Basic Arithmetic Calculator****")
    Number1 = eval(input("Enter first number: "))
    Number2 = eval(input("Enter second number: "))
    Operation = input("Which Operation you want to perform\n Type + for Addition,\n Type - for Subtraction,\n Type x for Multiplication,\n Type / for Division\n Enter Value :")

    if Operation == "+":
        print("The addition of Number 1 and Number 2 is:", Number1 + Number2)

    elif Operation == "-":
        print("The subtraction of Number 2 from Number 1 is:", Number1 - Number2)

    elif Operation == "x":
        print("The multiplication of Number 1 and Number 2 is:", Number1 * Number2)

    elif Operation == "/":
        print("The division of Number 1 by Number 2 is:", Number1/Number2)

    else:
        print("OOPS! You entered wrong symbol:)")

    again = input("DO YOU WANT TO CALCULATE FOR ANOTHER VALUE, TYPE Y for YES and N for NO :")
    if again == "Y" or "y":
        return calculator()
    else:
        print("I hope you like it!")

calculator()