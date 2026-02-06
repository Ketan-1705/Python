class Bank:
    def openAc(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",cname," Your Account Number ",acno,"Is Open with ",balance," Rs.")
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("Sorry you Need Another",amount-self.balance," Rs. To withdraw")
    def checkBalance(self):
        print("Your Current Balance Is ",self.balance)

b1=Bank()
b1.openAc(101,"Ketan,",1000)

        
