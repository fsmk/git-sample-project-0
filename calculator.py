#
# calculator.py 
#

# Asks user for 2 operands and 1 operator
# Returns output of this operation

a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
o=input("Enter operator : ")

if o[0] in [ '+','-','*','/' ]:
    if o[0] == '+':
        out = a + b
    elif o[0] == '-':
        out = a - b
    elif o[0] == '*':
        out = a * b
    elif o[0] == '/':
        if b==0:
            print("Error : Division by zero not possible")
        else:
            out = a//b
    elif o[0] == '%':
        if b==0:
            print("Error : Division by zero not possible")
        else:
            out = a%b
    print("Output : ",out)
else:
    print("Error : Invalid Operator")
