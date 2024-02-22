#
# calculator.py 
#

# Asks user for 2 operands and 1 operator
# Returns output of this operation

a=int(input("Enter number 1 : "))
o=input("Enter operator : ")
b=int(input("Enter number 2 : "))

if o in [ '+','-','*','/' ]:
    if o == '+':
        out = a + b
    elif o == '-':
        out = a - b
    elif o == '*':
        out = a * b
    elif o == '/':
        if b != 0:
          out = a / b
    else:
        print("Error : division by zero")
        exit()
    print("Output:", out)
else:
    print("Error: Invalid operator")
