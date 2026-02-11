from tkinter import *
import mysql.connector

def creat_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ketan"
        )
print(creat_conn)
def insert_data():
    print("Insert Data")
def search_data():
    print("Search Data")
def update_data():
    print("Update Data")
def delete_data():
    print("Delete Data")

root=Tk()
root.geometry("350x400")
root.title("Registration Form")
root.resizable(width=False,height=False)

l_id=Label(root,text="Id : ")
l_id.place(x=50,y=50)

l_fname=Label(root,text="First Name : ")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="Last Name : ")
l_lname.place(x=50,y=150)

l_email=Label(root,text="Email : ")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="Mobile Number : ")
l_mobile.place(x=50,y=250)


e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Arial Rounded MT Bold",10),command=insert_data)
insert.place(x=50,y=300)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Arial Rounded MT Bold",10),command=search_data)
search.place(x=115,y=300)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Arial Rounded MT Bold",10),command=update_data)
update.place(x=187,y=300)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Arial Rounded MT Bold",10),command=delete_data)
delete.place(x=258,y=300)
