table_number=int(input("Enter Tabal Numbar :  "))
coustomer_name=input("Enter Coustomer Name :")
coustomer_number=int(input("Enter coustomer Mobile Number : "))

menu=[]
order=[]


file=open("coustomer.txt","w")
file.write("Table Number is: " + str(table_number) + "\n")
file.close()
file=open("coustomer.txt","a")
file.write("Coustomer Name is : " + str(coustomer_name) + "\n")
file.close()
file=open("coustomer.txt","a")
file.write("coustomer Mobile Number is : " + str(coustomer_number) + "\n")
file.close()
