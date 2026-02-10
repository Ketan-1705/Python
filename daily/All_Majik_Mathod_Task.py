class Point:
    def __init__(self,x,y):
        print("init Called")
        self.x=x
        self.y=y
    def __str__(self):
        print("str Called")
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,obj):
        print("add Called")
        x=self.x+obj.x
        y=self.y+obj.y
        return Point(x,y)
    def __sub__(self,obj):
        print("sub Called")
        x=self.x-obj.x
        y=self.y-obj.y
        return Point(x,y)
    def __mul__(self,obj):
        print("mul Called")
        x=self.x*obj.x
        y=self.y*obj.y
        return Point(x,y)
    def __div__(self,obj):
        print("add Called")
        x=self.x/obj.x
        y=self.y/obj.y
        return Point(x,y)

p1=Point(10,20)
print(p1)
p2=Point(30,40)
print(p2)
print("Addition of 2 object : ",p1+p2)
print("Subtraction of 2 object : ",p1-p2)
print("Multiplication of 2 object : ",p1*p2)
print("Division of 2 object : ",p1/p2)


