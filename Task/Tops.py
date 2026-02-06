class Tops:
    def admin(self, s_name, s_number):
        self.s_name = s_name
        self.s_number = s_number
        print("Hello", s_name, ", Student Phone number:", s_number)

    def admission(self, c_name, c_fees):
        self.c_name = c_name
        self.c_fees = c_fees
        print("Your Course Is:", self.c_name)
        print("Your Course Fees Is:", self.c_fees, "RS")
        self.feesin()

    def feesin(self):
        while True:
            print("1. Full Payment")
            print("2. Installment (5 Installments)")
            print("*" * 40)

            choice2 = int(input("Enter Your Choice: "))

            if choice2 == 1:
                print("Full payment of", self.c_fees, "RS successful")
                break

            elif choice2 == 2:
                installment_amount = self.c_fees / 5
                print("You selected 5 Installments")
                print("Each Installment Amount:", installment_amount, "RS")
                print("Installment payment setup successful")
                break

            else:
                print("Invalid Choice")


t1 = Tops()
t1.admin("Ketan", 9725666808)

while True:
    print("1. Java")
    print("2. Python")
    print("3. Web Designing")
    print("4. UI/UX")
    print("5. Exit")
    print("*" * 40)

    choice = int(input("Enter Your Choice: "))
    print("*" * 40)

    if choice == 1:
        t1.admission("Java", 60000)

    elif choice == 2:
        t1.admission("Python", 65000)

    elif choice == 3:
        t1.admission("Web Designing", 95000)

    elif choice == 4:
        t1.admission("UI/UX", 60000)

    elif choice == 5:
        print("Thank you for choosing TOPS")
        break

    else:
        print("Invalid Choice")

