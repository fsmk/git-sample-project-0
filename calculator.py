#
# calculator.py 
#

# Asks user for 2 operands and 1 operator
# Returns output of this operation

a=int(input("Enter number 1 : "))
o=(input("Enter operator : "))
b=int(input("Enter number 2 : "))
out=0
if o[0] in [ '+','-','*','/' ]:
    if o[0] == '+':
        out = a + b
    elif o[0] == '-':
        out = a - b
    elif o[0] == '*':
        out = a * b
    elif o[0] == '/':
        if b==0:
            print("error: divide by zero isnt possible.")
        else:
            out = a//b
    print("Output (it is 0 by default): ",out)
else:
    print("Error : Invalid Operator")
