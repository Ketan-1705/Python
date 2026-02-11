table_number=int(input("Enter Tabal Numbar :  "))
coustomer_name=input("Enter Coustomer Name :")
coustomer_number=int(input("Enter coustomer Mobile Number : "))

file=open("coustomer.txt","a")
file.write("\nTable Number is: " + str(table_number) + "\n")
file.close()
file=open("coustomer.txt","a")
file.write("Coustomer Name is : " + str(coustomer_name) + "\n")
file.close()
file=open("coustomer.txt","a")
file.write("coustomer Mobile Number is : " + str(coustomer_number) + "\n")
file.close()
bill=[]

while True:
    print("1. Panjabi")
    print("2. Gujrati")
    print("3. Chinis")
    print("4. Exit")

    choice=int(input("Enter Your Choice :"))

    if choice==1:
        while True:
            print("1. Shahi Paneer    --  RS. 250")
            print("2. Mutter Paneer   --  RS. 250")
            print("3. Palak Paneer    --  RS. 250")
            print("4. Kadhai Paneer   --  RS. 250")
            print("5. Paneer Butter Masal --  RS. 250")
            print("6. Paneer Handi    --  RS. 250")
            print("7. Exit")
            choicp=int(input("Enter Your Choice :"))

            if choicp==1:
                bill.append(250,)
                file=open("coustomer.txt","a")
                file.write("Shahi Paneer      --  RS. 250" "\n")
                file.close()
                
            elif choicp==2:
                bill.append(250,)
                file=open("coustomer.txt","a")
                file.write("Mutter Paneer      --  RS. 250" "\n")
                file.close()
            elif choicp==3:
                bill.append(250,)
                file=open("coustomer.txt","a")
                file.write("Kadhai Paneer     --  RS. 250" "\n")
                file.close()
            elif choicp==4:
                bill.append(250,)
                file=open("coustomer.txt","a")
                file.write("Kadhai Paneer      --  RS. 250" "\n")
                file.close()
            elif choicp==5:
                bill.append(250,)
                file=open("coustomer.txt","a")
                file.write("Paneer Butter Mas  --  RS. 250" "\n")
                file.close()
            elif choicp==6:
                bill.append(250,)
                file=open("coustomer.txt","a")
                file.write("Paneer Handi       --  RS. 250" "\n")
                file.close
            elif choicp==7:
                
                break
               
            else:
                print("invallid")
    elif choice==4:
        
        for i in bill:
            print(i)
            total = sum(bill)
        print("Total Bill =", total)
        file=open("coustomer.txt","a")
        file.write(f"Total Bill : {total}\n")
        file.close()
        file=open("coustomer.txt","a")
        file.write("*"*40)
        file.close()
        break




