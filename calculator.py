# calculator.py

# Asks user for 2 operands and 1 operator
# Returns output of this operation

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
        if b == 0:
            print("Error: Division by zero")
        else:
            out = a / b
    print("Output:", out)
else:
    print("Error: Invalid Operator")
