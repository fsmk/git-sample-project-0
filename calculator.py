a = input("Enter number 1: ")
o = input("Enter operator: ")
b = input("Enter number 2: ")

# Convert inputs to float
a = float(a)
b = float(b)

if o[0] in ['+', '-', '*', '/', '%', '^']:  # Add support for modulus (%) and exponent (^)
    if o[0] == '+':
        out = a + b
    elif o[0] == '-':
        out = a - b
    elif o[0] == '*':
        out = a * b
    elif o[0] == '/':
        if b != 0:  # Check for divide by zero
            out = a / b
        else:
            print("Error: Division by zero")
            exit()  # Exit program if divide by zero occurs
    elif o[0] == '%':
        out = a % b
    elif o[0] == '^':
        out = a ** b
    print("Output:", out)
else:
    print("Error: Invalid Operator")
