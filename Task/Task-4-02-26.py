list1=[1,2,3,4,5,6]
list2=[]
even=[]
def cube(x):
    return x*x*x
for i in list1:
    list2.append(cube(i))
print(list2)
even=list(filter(lambda j:j%2 == 0,list2)) 
print(even)
