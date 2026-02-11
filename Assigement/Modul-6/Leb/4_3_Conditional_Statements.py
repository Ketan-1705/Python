#Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder
s1=int(input("Enter Subject 1 Marks : "))
s2=int(input("Enter Subject 2 Marks : "))
s3=int(input("Enter Subject 2 Marks : "))

total=s1+s2+s3
div=total/300
per=div*100

print("percentage : ",per)


if per > 101 or per < 0:
    print("Enter Valid Number")
elif per > 80:
    print("A Grad")
elif per > 60:
    print("B Grad")
elif per > 45:
    print("C Grad")
elif per > 35:
    print("D Grad")
else:
    print("Fail..")
