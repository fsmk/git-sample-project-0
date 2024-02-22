a = float(input("Enter number 1: "))
o = input("Enter operator: ")
b = float(input("Enter number 2: "))

if o in ['+', '-', '*', '/']:
    if o == '+':
        out = a + b
    elif o == '-':
        out = a - b
    elif o == '*':
        out = a * b
    elif o == '/':
        if b != 0:  # Check if denominator is not zero
            out = a / b
        else:
            print("Error: Division by zero")
            exit()
    print("Output:", out)
else:
    print("Error: Invalid Operator")
