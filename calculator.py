#
# calculator.py
#

# Asks user for 2 operands and 1 operator
# Returns output of this operation

import sys

a = int(input("Enter number 1 : "))
o = input("Enter operator : ")
b = int(input("Enter number 2 : "))

if o[0] in ['+', '-', '*', '/']:
    if o[0] == '+':
        out = a + b
    elif o[0] == '-':
        out = a - b
    elif o[0] == '*':
        out = a * b
    elif o[0] == '/':
        try:
            assert b != 0, "Divide by Zero!"
            out = a // b
        except AssertionError as err:
            print(err)
            sys.exit()
    print("Output : ", out)
else:
    print("Error : Invalid Operator")
