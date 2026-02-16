# Write a Python program to convert two lists into one dictionary using a for loop.

list1=[1,2,3]
list2=["IT","Computer","DA"]

d={}

for i in range(len(list1)):
    d[list1[i]]=list2[i]

print(d)
