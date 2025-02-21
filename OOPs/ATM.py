
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

#Static/Class variable:ek aesa variable  jiski value har object k liye same h
Static variable is always defined outside constructor

'''

class Atm:
    #Static/class variable
    __counter=1


    def __init__(self):
        self.__pin=""
        self.__balance=0
        self.sno=Atm.counter
        Atm.__counter=Atm.__counter+1
        #self.menu()
    #Static Method
    @staticmethod
    def get_counter():
        return Atm.__counter
    @staticmethod
    def set_counter(new):
        if type(new)==int:
            Atm.__counter=new
        else:
            print("Not allowed")
    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("Pin changed")
        else:
            print("Not allowed")
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
        self.__pin= input("Enter your pin")
        print("Pin set successfully")

    def deposit(self):
        temp=input("enter your pin")
        if temp==self.__pin:
            amount=int(input("Enter the amount"))
            self.__balance=self.__balance+amount
            print("Deposit Successfully")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp=input("enter your pin")
        if temp==self.__pin:
            amount=int(input("enter the amount"))
            if amount<self.balance:
                self.__balance=self.__balance-amount
                print("Operation Successful")
            else:
                print("Insufficient amount")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp=input("Enter the pin")
        if temp==self.__pin:
            print(self.__balance)
        else:
            print("Invalid Pin")
sbi=Atm()

#Create our own data type
class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    def __add__(self,other):
        temp_num=self.num*other.den + other.num*self.den
        temp_den=self.den *other.den
        return "{}/{}".format(temp_num,temp_den)
from fraction import Fraction
x=Fraction(4,5)
type(x)

'''
#Instance variable:It is a variable whose value is different for different object
sbi.balance is also accessible,Data koo open chhodna is not a good practice
#Encapsulation: double underscore lagake method koo b and variable koo b hide kr sakte h
sbi.__balance will still accessible 
Nothing in python is truly private

--Getter and Setter Methods
--Object create krte time object koo jis variable m store krte h voh reference variable
for ex: sbi=Atm(),here sbi is reference variable


'''
class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
def greet(customer):
    if customer.gender=="Male":
        print("Hello",customer.name,"sir")
    else:
        print("Hello",customer.name,"ma'am")
cust=Customer("Krishna","Male")
greet(cust) #Object pass kr rhe,Function koo object b de sakte h

class Customerr:
    def __init__(self,name):
        self.name=name
    def greet(customer):
        print(id(customer))
        customer.name="Nistish"
        print(customer.name)
cust=Customerr("Radha")
print(id(cust))

greet(cust) 

print(cust.name)
#class ke objects are also mutable like lists,dict and sets

class Buyer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print("I am",self.name,"and I am",self.age)
c1=Buyer("Nitish",34)
c2=Buyer("Ankit",45)
c3=Buyer("Neha",32)
L=[c1,c2,c3]
for i in L:
    i.intro()
'''
Relationship->Aggregation and Inheritance
Aggregation-> has a relationship Ex: Customer has a address
Inheritance-> is a relationship'''

class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.new_name=new_name
        self.address.change_address(new_city,new_pin,new_state)

    
class address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
    def change_address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pincode=new_pin
        self.state=new_state

add=address("Kolkata",98089,"WB")
cust=Customer("Nitish","Male",add)
cust.edit_profile("Ayushman","Gurgaon",122011,"haryana")

print(cust.address.pincode)

#Private members are not inherited
class User:
    def login(self):
        print("login")
    def register(self):
        print("Register")
class Student(User):
    def enroll(self):
        print("Enroll")
    def review(self):
        print("Review")

stu=Student()
stu.enroll()
stu.review()
stu.login()
stu.register()

#Reverse Inheritance is not possible 

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone condtructor")
        self.price=price
        self.brand=brand
        self.camera=camera
class SmartPhone(Phone):
    pass

s=SmartPhone(20000,"Apple",13)
print(s.brand )

#Polymorphism->Method Overriding,Method overloading,Operator Overloading
#Method Overriding
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a phone")
class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
s=SmartPhone(20000,"Apple",13)
s.buy()

class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
class Child(Parent):
    def show(self):
        print("This is in child class")
son=Child(100)
print(son.get_num())
son.show()

class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self,val,num):
        self.__val=val
    def get_val(self):
        return self.__val
    
son=Child(100,10)
print("Parent:num",son.get_num())

#Example of Super->Super keyword parent k method and constructor koo invoke kr sakte h

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a phone")
class smartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        super().buy()
s=smartPhone(20000,"Apple",13)
s.buy()
s.super().buy()#error









     