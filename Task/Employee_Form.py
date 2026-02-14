from tkinter import *
import mysql.connector
import tkinter.messagebox as msg
def creat_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ketan"
        )

def insert_data():
    if e_name.get()=="" or e_number=="" or e_age=="" or e_department=="" or e_join=="" or e_salary=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        conn=creat_conn()
        cursor=conn.cursor()
        query="Insert into employee(name,number,age,department,join_date,salary) values(%s,%s,%s,%s,%s,%s)"
        args=(e_name.get(),e_number.get(),e_age.get(),e_department.get(),e_join.get(),e_salary.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_name.delete(0,'end')
        e_number.delete(0,'end')
        e_age.delete(0,'end')
        e_department.delete(0,'end')
        e_join.delete(0,'end')
        e_salary.delete(0,'end')
        msg.showinfo("Insert Status","Data Successfully")
def search_data():
    e_name.delete(0,'end')
    e_number.delete(0,'end')
    e_age.delete(0,'end')
    e_department.delete(0,'end')
    e_join.delete(0,'end')
    e_salary.delete(0,'end')
    
    if e_id.get()=="":
        msg.showinfo("search Status","id is Mandatory")
    else:
        conn=creat_conn()
        cursor=conn.cursor()
        query="select * from employee where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            e_name.insert(0,row[0][1])
            e_number.insert(0,row[0][2])
            e_age.insert(0,row[0][3])
            e_department.insert(0,row[0][4])
            e_join.insert(0,row[0][5])
            e_salary.insert(0,row[0][6])
        else:
            msg.showinfo("Search Status","Id not Found")
            
        conn.close()
        
def update_data():
    if e_name.get()=="" or e_number=="" or e_age=="" or e_department=="" or e_join=="" or e_salary=="":
        msg.showinfo("update Status","All Fields Are Mandatory")
    else:
        conn=creat_conn()
        cursor=conn.cursor()
        query="update employee set name=%s,number=%s,age=%s,department=%s,join_date=%s,salary=%s"
        args=(e_name.get(),e_number.get(),e_age.get(),e_department.get(),e_join.get(),e_salary.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_name.delete(0,'end')  
        e_number.delete(0,'end')
        e_age.delete(0,'end')
        e_department.delete(0,'end')
        e_join.delete(0,'end')
        e_salary.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Successfully")
def delete_data():
     if e_id.get()=="":
        msg.showinfo("Delete Status","Id is Mandatory")
     else:
        conn=creat_conn()
        cursor=conn.cursor()
        query="delete from employee where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_name.delete(0,'end')
        e_number.delete(0,'end')
        e_age.delete(0,'end')
        e_department.delete(0,'end')
        e_join.delete(0,'end')
        e_salary.delete(0,'end')
        msg.showinfo("Delete Status","Data Deleted Successfully")
    
    
root=Tk()
root.geometry("500x500")
root.title("Employee Details")
root.resizable(width=False,height=False)

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

e_name=Entry(root)
e_name.place(x=170,y=100,width=250,height=25)

e_number=Entry(root)
e_number.place(x=170,y=150,width=250,height=25)

e_age=Entry(root)
e_age.place(x=170,y=200,width=250,height=25)

e_department=Entry(root)
e_department.place(x=170,y=250,width=250,height=25)

e_join=Entry(root)
e_join.place(x=170,y=300,width=250,height=25)

e_salary=Entry(root)
e_salary.place(x=170,y=350,width=250,height=25)

insert=Button(root,text="INSERT",bg="#6699ff",fg="white",font=("Arial Rounded MT Bold",10),command=insert_data)
insert.place(y=400,x=50)

search=Button(root,text="SEARCH",bg="#6699ff",fg="white",font=("Arial Rounded MT Bold",10),command=search_data)
search.place(y=400,x=120)

update=Button(root,text="UPDATE",bg="#6699ff",fg="white",font=("Arial Rounded MT Bold",10),command=update_data)
update.place(y=400,x=200)

delete=Button(root,text="DELETE",bg="#6699ff",fg="white",font=("Arial Rounded MT Bold",10),command=delete_data)
delete.place(y=400,x=280)
