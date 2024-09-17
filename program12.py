a=int(input("Enter a number"))
b=int(input("Enter another number"))
choice=input("Enter operands(+,-,/,*)=")
if(choice=="+"):
    print(a+b)
elif(choice=="-"):
    print(a-b)
elif(choice=="/"):
    print(a/b)
elif(choice=="*"):
    print(a*b)
else:
    print("Invalid ")
