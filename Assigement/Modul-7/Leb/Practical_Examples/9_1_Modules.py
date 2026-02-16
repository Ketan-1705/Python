# Write a Python program to demonstrate the use of functions from the math module.
import math


num1 = float(input("Enter a number for square root, ceil, floor, and factorial: "))
num2 = float(input("Enter another number for power and log functions: "))

print("Square root of", num1, "is:", math.sqrt(num1))

print("Ceil value of", num1, "is:", math.ceil(num1))
print("Floor value of", num1, "is:", math.floor(num1))

print("Factorial of", int(num1), "is:", math.factorial(int(num1)))

print(num1, "raised to the power", num2, "is:", math.pow(num1, num2))

print("Natural log of", num1, "is:", math.log(num1))

print("Base-10 log of", num1, "is:", math.log10(num1))

angle_rad = math.radians(num1)
print("Sine of", num1, "degrees is:", math.sin(angle_rad))
print("Cosine of", num1, "degrees is:", math.cos(angle_rad))
print("Tangent of", num1, "degrees is:", math.tan(angle_rad))
