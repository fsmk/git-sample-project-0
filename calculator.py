# calculator.py 

# Asks user for 2 operands and 1 operator
# Returns output of this operation

a = input("Enter number 1: ")
o = input("Enter operator: ")
b = input("Enter number 2: ")

# Convert input to numerical values
try:
    a = float(a)
    b = float(b)
except ValueError:
    print("Error: Invalid input. Please enter numerical values.")
    exit()

if o[0] in ['+', '-', '*', '/']:
    if o[0] == '+':
        out = a + b
    elif o[0] == '-':
        out = a - b
    elif o[0] == '*':
        out = a * b
    elif o[0] == '/':
        # Check for division by zero
        if b == 0:
            print("Error: Division by zero is not allowed.")
            exit()
        out = a / b
    print("Output: ", out)
else:
    print("Error: Invalid Operator")
