#Practical Example 6: Write a Python program to check if a number is prime using if_else.
num=int(input("Enter Number : "))


if num<=0:
    print("Not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("Not Prime")
            break
    else:
        print("Is Prime")
