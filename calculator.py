a=int(input("Enter number 1 : "))
o=input("Enter operator : ")
b=int(input("Enter number 2 : "))

if o[0] in [ '+','-','*','/' ]:
    if o[0] == '+':
        out = a + b
    elif o[0] == '-':
        out = a - b
    elif o[0] == '*':
        out = a * b
    elif o[0] == '/':
            if(b==0):
                print("cannot devide by zero")
            else:
                out = a//b
    print("Output : ",out)
else:
    print("Error : Invalid Operator")
