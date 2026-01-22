rno=int(input("Enter Student Roll Number : "))
sname=input("Enter Student Name : ")
s1=float(input("Enter Marks of Subject 1 : "))
s2=float(input("Enter Marks of Subject 2 : "))
s3=float(input("Enter Marks of subject 3 : "))

total=s1+s2+s3
per=total/3

print("Student Name : ",sname)
print("Student Roll Number : ",rno)
print("Student Total Marks : ",total)
print("Student Percentage : ",per)

if per>=70:
    print("Distinction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second class")
elif per>=40:
        print("Pass class")
else:
    print("Fail")
