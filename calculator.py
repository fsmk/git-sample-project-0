#
# calculator.py 
#

# Asks user for 2 operands and 1 operator
# Returns output of this operation

a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
o=input("Enter operator : ")
if 0 == '/' and b == 0:
    print("Any number cannot be divided with zero")
    exit
if o[0] in [ '+','-','*','/' ]:
    if o[0] == '+':
        out = a + b
    elif o[0] == '-':
        out = a - b
    elif o[0] == '*':
        out = a * b
    elif o[0] == '/':
        out = a//b
    print("Output : ",out)
else:
    print("Error : Invalid Operator")
