#
# calculator.py 
#

# Asks user for 2 operands and 1 operator
# Returns output of this operation

a=input("Enter number 1 : ")
o=input("Enter operator : ")
b=input("Enter number 2 : ")

if isdigit(a) and isdigit(b):
    if o[0] in [ '+','-','*','/' ,'%','^']:
        if o[0] == '+':
            out = a + b
        elif o[0] == '-':
            out = a - b
        elif o[0] == '*':
            out = a * b
        elif o[0] == '/':
            if b==0:
                print("cannot divide by zero")
            else:
                out = a//b
        elif o[0] == '%':
            if b==0:
                print("cannot divide by zero")
            else:
                out = a % b
        elif o[0] == '^':
            out = pow(a,b)
    
        print("Output : ",out)
    else:
        print("Error : Invalid Operator")
