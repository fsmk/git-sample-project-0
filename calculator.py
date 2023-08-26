#
# calculator.py 
#

# Asks user for 2 operands and 1 operator
# Returns output of this operation
import math
a=int(input("Enter number 1 : "))
o=input("Enter operator : ")
b=int(input("Enter number 2 : "))

if o[0] in [ '+','-','*','/','%','^']:
    if o[0] == '+':
        out = a + b
    elif o[0] == '-':
        out = a - b
    elif o[0] == '*':
        out = a * b
    elif o[0] == '/':
        if(b==0):
            print("Invalid Input!!")
        else:
            out = a//b
    elif o[0] == '**':
        out=math.pow(a,b)
        #out=a**b
    elif o[0]=='%':
        if(b==0):
            print("Invalid Input!!")
        else:
            out = a%b
    print("Output : ",out)
else:
    print("Error : Invalid Operator")
