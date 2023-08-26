# calculator.py

# Asks the user for 2 operands and 1 operator
# Returns the output of this operation

a = int(input("Enter number 1: "))
o = input("Enter operator: ")
b = int(input("Enter number 2: "))

out = None  # Initialize the out variable

if o in ['+', '-', '*', '/', '%', '**']:
    if o == '+':
        out = a + b
    elif o == '-':
        out = a - b
    elif o == '*':
        out = a * b
    elif o == '/':
        if b == 0:
            print('Division by zero error.')
        else:
            out = a / b  # Use "/" for floating-point division
    elif o == '%':
        if b == 0:
            print('Division by zero error.')
        else:
            out = a % b
    elif o == '**':
        out = a ** b  # Use "**" for exponentiation

if out is not None:
    print("Output:", out)
else:
    print("Error: Invalid Operator")

