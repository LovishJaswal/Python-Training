print("Welcome to the calculator!")
while(True):
    terminate = input("Type 'quit' to quit or press any key to continue: ")
    if(terminate == "quit"):
        break
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    op = input("Enter the operand: ")
    if(op == "+"):
        print(num1+num2)
    elif(op == "-"):
        print(num1-num2)
    elif(op == "*"):
        print(num1*num2)
    elif(op == "/"):
        print(num1/num2)
    elif(op == "%"):
        print(num1%num2)
    elif(op == "**"):
        print(num1**num2)