#Write a Python program to create a lambda function with two expressions.
check = lambda x: "Even" if x % 2 == 0 else "Odd"

num = int(input("Enter a number: "))
print(check(num))
