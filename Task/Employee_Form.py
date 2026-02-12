from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Employee Details")
root.resizable(width=False,height=False)

def insert_data():
    print("Insert")
def search_data():
    print("Search")
def update_data():
    print("Update")
def delete_data():
    print("Delete")

l_id=Label(root,text="Id :", font=("Arial",10))
l_id.place(x=50,y=50)

l_name=Label(root,text="Name :",font=("Arial",10))
l_name.place(x=50,y=100)

l_number=Label(root,text="Phone Number :",font=("Arial",10))
l_number.place(x=50,y=150)

l_age=Label(root,text="Age :",font=("Arial",10))
l_age.place(x=50,y=200)

l_department=Label(root,text="Department :",font=("Arial",10))
l_department.place(x=50,y=250)

l_join=Label(root,text="Joining Data :",font=("Arial",10))
l_join.place(x=50,y=300)

l_salary=Label(root,text="Salary :",font=("Arial",10))
l_salary.place(x=50,y=350)

e_id=Entry(root)
e_id.place(x=170,y=50,width=250,height=25)

e_id=Entry(root)
e_id.place(x=170,y=100,width=250,height=25)

e_id=Entry(root)
e_id.place(x=170,y=150,width=250,height=25)

e_id=Entry(root)
e_id.place(x=170,y=200,width=250,height=25)

e_id=Entry(root)
e_id.place(x=170,y=250,width=250,height=25)

e_id=Entry(root)
e_id.place(x=170,y=300,width=250,height=25)

e_id=Entry(root)
e_id.place(x=170,y=350,width=250,height=25)

insert=Button(root,text="INSERT",bg="#6699ff",fg="white",font=("Arial Rounded MT Bold",10),command=insert_data)
insert.place(y=400,x=50)

search=Button(root,text="SEARCH",bg="#6699ff",fg="white",font=("Arial Rounded MT Bold",10),command=search_data)
search.place(y=400,x=120)

update=Button(root,text="UPDATE",bg="#6699ff",fg="white",font=("Arial Rounded MT Bold",10),command=update_data)
update.place(y=400,x=200)

delete=Button(root,text="DELETE",bg="#6699ff",fg="white",font=("Arial Rounded MT Bold",10),command=delete_data)
delete.place(y=400,x=280)
