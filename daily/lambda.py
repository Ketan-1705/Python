def cube(x):
    return x*x*x
ans=cube(5)
print("Cube of ",5,"is : ",ans)

ans1=lambda y:y*y*y
print("Cube of ",5,"is : ",ans1(5))

x=lambda a,b:a*b
print(x(10,20))

result=lambda num:"even" if num%2==0 else "odd"
print(result(2))
