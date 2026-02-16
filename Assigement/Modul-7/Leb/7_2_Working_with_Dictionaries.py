#Write a Python program to merge two lists into one dictionary using a loop.
l1=[1,2,3,4,5]
l2=["Ketan","Bhavesh","Uma","Kinjal","Jay"]

d={}

for i in range(len(l1)):
   d[l1[i]]=l2[i]


print("Dictionary :",d)
