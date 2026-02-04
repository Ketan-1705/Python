def myfun():
    print(name)
name="Ketan"

myfun()

def myfun1():
    global name1
    print("1st ",name1)
    name1="Python Language"
    print("2nd ",name1)

name1="Python"
myfun1()

print("3rd",name1)
