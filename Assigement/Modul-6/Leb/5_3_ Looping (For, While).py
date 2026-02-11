#Practical Example 3: Write a Python program to find a specific string in the list using a simple 
#for loop and if condition.

list1=['Apple','Banana','Mango']
string=input("Enter String : ")
for i in list1:
    if i == string:
        print(f"Yes I found This String : {string}")
        break
else:
    print(f"Yes I can't found This String : {string}")
        
