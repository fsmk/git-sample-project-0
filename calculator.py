#
# calculator.py 
#

# Asks user for 2 operands and 1 operator
# Returns output of this operation

# Checks the operands type is integer
a = int(input("Enter number 1: "))
o = input("Enter operator: ")
b = int(input("Enter number 2: "))

if o[0] in ['+', '-', '*', '/']:
    if o[0] == '+':
        out = a + b
    elif o[0] == '-':
        out = a - b
    elif o[0] == '*':
        out = a * b
    elif o[0] == '/':
        if b != 0:
            out = a / b
        else:
            out = "Division by Zero Error"  # Handles the division by zero error
    print("Output: ", out)
else:
    print("Error: Invalid Operator")
