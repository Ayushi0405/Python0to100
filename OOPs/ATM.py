
'''Function Vs Methods:Methods are a special function written inside class

Ex:len(L)->Function
L.append()->Method

Constructor is a special method joo automatically execute hota h jab uss class kaa object bnate h

Jab b method bnao toh input m self

Magic method apne aap trigger hoo jaata h


//Utility of constructor method:__init__:iska control user k pass nhi h

 Jis bhi object k saath current m kaam kr rhe hoo wahi self h
// Class m data and function hote h aur in dono koo access class kaa object kr sakta h
// Class ek method apne class ke dusre method koo access nhi kr sakta uske liye object chahiye
nd yeh self k through aata h

'''
class Atm:


    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
    def menu(self):
        while True:
    
            user_input=input("""
            Hello,how would you like to proceed?
            1.Enter 1 to create pin
            2.Enter 2 to deposit
            3.Enter 3 to withdraw
            4.Enter 4 to check balance
            5.Enter 5 to exit
            """ )
            if user_input=="1":
                self.create_pin()
            elif user_input=="2":
                self.deposit()
            elif user_input=="3":
                self.withdraw()
            elif user_input=="4":
                self.check_balance()
            else:
                print("bye")


    def create_pin(self):
        self.pin= input("Enter your pin")
        print("Pin set successfully")

    def deposit(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            self.balance=self.balance+amount
            print("Deposit Successfully")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter the amount"))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Operation Successful")
            else:
                print("Insufficient amount")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp=input("Enter the pin")
        if temp==self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")
sbi=Atm()

#Create our own data type
class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
from fraction import Fraction
x=Fraction(4,5)
type(x)


    