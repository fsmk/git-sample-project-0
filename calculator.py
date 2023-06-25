#
# calculator.py 
#

# Asks user for 2 operands and 1 operator
# Returns output of this operation

a=int(input("Enter number 1 : "))
o=input("Enter operator : ")
b=int(input("Enter number 2 : "))

if a or b == 0:
    print('invalid values')
     
elif o[0] in [ '+','-','*','/', '%','^']:
    if o[0] == '+':
        out = a + b
    elif o[0] == '-':
        out = a - b
    elif o[0] == '*':
        out = a * b
    elif o[0] == '/':
        out = a//b
    elif o[0] == '%':
        out = a%b
    elif o[0] == '^':
        out = pow(a,b)
    print("Output : ",out)
else:
    print("Error : Invalid Operator")
