#Write a Python program to create a calculator using functions.

def getdata():
    a=int(input("Emter Number : "))
    b=int(input("Emter Number : "))
    c=input("Enter Operatar +,-,*,/ :")
    if c == "+":
        print("Sum is :",a+b)
    elif c== "-":
        print("Sub is :",a-b)
getdata()
