print("India","USA","UK","Canada","Australia",sep=",")  # This prints the countries separated by commas

print("Hello Khushi",end="")  # This prints "Hello Khushi" without a newline at the end

# Multi-line comments can be done using triple quotes
"""
Python supports 3 categories of data types:

1.Basic Types - int, float, complex, bool, str
2.Containers - list, tuple, set, dict
3.User-defined - class, function, module, package

"""
#integer #Range-> 1e309
print(4)

#float #Range -> (1.7e308)
print(4.5)

#Boolean
print(True)
print(False)

#complex
print(3+4j)

#string
print('Krishna')
print("keishna")
print("""Krishna""")

#list
print([1,2,3,4,5])

#Tuple
print((1,2,3,4,5))

#sets
print({1,2,3,4,5})

#dictionary
print({"Krishna":God,"Shiva":God,"Vishnu":God})

#No variable declaration required->Dynamic Typing
name='krishna'
print(name)

#Static Typing ->Specify the type of variable
name='Krishna'
print(name)

name=10
print(name)

#Dynamic Binding->Change the type of variable
#Static Binding->Cannot change the type of variable

#Special syntax
a=9;b=8;c=5
print(a)
print(b)
print(c)

a,b,c=9,8,5
print(a)
print(b)
print(c)

a=b=c=9
print(a)
print(b)    
print(c)

'''
KEYWORDS
->Python is a case sensitive language
->In Programming a keyword is a word that is reserved by a program because the word has a special meaning.Keywords can
be commands or parameters.every programming language has a set of keywords that cannot be used a variable names
->Python has 33 keywords'''

import keyword
print(keyword.kwlist)

'''
IDENTIFIERS
-> A Python identifier is a name used to identify a variable,function,class,module or other object.
--Rules for writing identifiers
->can only start with an alphabet or _
-> followed by 0 or more letter,_ and digits
-> keywords cannot be used as identifiers'''

#Taking Input
input(prompt="Enter your name:") 

first_num=input("Enter first number:") #User input is always a string
second_num=input("Enter second number:")
result = first_num+second_num
print(result)

#type
type(first_num)
type(second_num)
type(result)

#Type Conversion
#implicit type conversion -> done by python
print(4+5.5)

#explicit type conversion -> done by user
result=int(first_num)+int(second_num)
print(result)

print(int('4')+float('5.5'))
print(list('Krishna'))

#Type conversion is not a permanent operation

'''
LITERALS
-> Literal is a raw data given in a variable.In Python there are various types of literals they are as follows:
1.Numeric Literals
2.String Literals
3.Boolean Literals
4.Special Literals'''

#Numeric Literals
a=0b1010 #Binary Literals
b=100 #Decimal Literal
c=0o310 #Octal Literal
d=0x12c #Hexadecimal Literal

#Float Literal
float_1=10.5
float_2=1.5e2 #1.5*10^2
float_3=1.5e-2 #1.5*10^-2

#Complex Literal
x=3.14j


print(a,b,c,d)
print(float_1,float_2,float_3)
print(x,x.imag,x.real)

#String Literals
strings='This is Krishna'
strings="This is Krishna"
char="C"
multiple_line_string="""This is Krishna
                        This is Keishna"""
unicode=u"\u00dcnic\u00f6de"
raw_string=r"raw \n string"
print(strings)
print(strings)
print(char)
print(multiple_line_string)
print(unicode)
print(raw_string)

#Boolean Literals

a=True + 4
b=False + 10

print("a:",a)
print("b:",b)

#Special Literals
a=None #None is used to define a null value or no value at all
print(a)


''' OPERATORS
->Operators are special symbols in Python that carry out arithmetic or logical computation.
Python has following types of operators:
1.Arithmetic Operators
2.Comparison(Relational) Operators
3.Logical(Boolean) Operators
4.Bitwise Operators
5.Assignment Operators
6.Identity Operators
7.Membership Operators
'''

x=5
y=2
print(x+y) #Addition
print(x-y) #Subtraction
print(x*y) #Multiplication
print(x/y) #Division
print(x//y) #Floor Division
print(x%y) #Modulus
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x>=y)

#Logical Operators
a=True
b=False
print(a and b)
print(a or b)
print(not a)

#Bitwise Operators->Image Processing
a=10
b=4 
print(a&b) #value=0
print(a|b) #value=14
print(x>>2) #value=1
print(x<<2) #value=20
print(~x) #value=-6

#Assignment Operators
a=5
a+=5
a-=5
a*=5
a/=5
a//=5

# a++,++a,--a,a-- are not supported in python

#Identity Operators
a=5
b=5
print(a is b) #True->Both are at same memory location
#If false then both are at different memory location

print(a is not b)

#Membership Operators -> Used to test if a sequence is presented in an object
a=[1,2,3,4,5]
print(1 in a)
print(6 not in a)

#If-Else
#correct email:Krishna@gmail.com
#password-1234

email=input("Enter your email:")
password=input("Enter your password:")
if '@' in email:
    password=input("Enter your password:")
    if email=="Krishna@gmail.com" and password=="1234":
        print("Login Successful")
    elif email=="Krishna@gmail.com" and password!="1234":
        print("Invalid Password")
        password=input("Enter your password:")
        if password=="1234":
            print("Login Successful")
        else:
            print("Login Failed")
    else:
        print("Login Failed")
else:
    print("Invalid email")

#Loops->
#while,for,do-while

# while condition:
#     code

number=int(input("Enter a number:"))
while number<10:
    print(number)
    number+=1

#Guessing Game
import random
jackpot=random.randint(1,100)
guess=int(input("Enter your guess:"))
counter=1
while guess != jackpot:
    if(guess>jackpot):
        print("Guess lower")
    else:
        print("Guess higher")
    
    guess=int(input("Enter your guess:"))
    counter+=1
print("You guessed it right")
print("Number of attempts:",counter)

#For Loop
# for i in range(start,stop,step):

#range function
range(1,11) #1,2,3,4,5,6,7,8,9,10
range(1,11,2) #1,3,5,7,9

for i in range(10,0,-1):
    print(i)

for i in [1,2],[3,4],[5,6]:
    print(i)

for i in (1,2,3,4,5):
    print(i)

#Nested Loop
for i in range(1,rows+1):
    for j in range(0,i):
        print("*",end="")
    print("")

#Break
for i in range(1,11):
    if i==5:
        break
    print(i)

#Continue -> Skip the current iteration wher condition met

for i in range(1,11):
    if i==5:
        continue
    print(i)

for i in range(1,11):
    pass #Do nothing

#Built-in Functions

#Print
print("Hello World")

#input
name=input("Enter your name:")
print(name)

#type
print(type(10))

#int etc.
print(int(5.5))

#abs->modulus function
print(abs(-5))

#pow->power function
print(pow(2,3))

#min,max
print(min(1,2,3,4,5))
print(max(1,2,3,4,5))

#round
print(round(5.5))

#divmod(x//y,x%y)
print(divmod(9,2))

#bin,oct,hex
print(bin(10))
print(oct(10))
print(hex(10))

#id-> Memory m address
a=10
print(id(a))

#ord->ASCII value
print(ord('A'))

#len
print(len("Krishna"))

#sum
print(sum([1,2,3,4,5]))

#help->Documentation padhna hoo
help(print)

#Built-in Modules
'''
MODULES-> same as a code library
A file containing a set of functions you want to include in your application
Examples of python modules
1.math
2.random
3.os
4.time
'''
help('modules')#List of all modules
import math
math.factorial(5)
math.sqrt(25)
math.pow(2,3)
math.pi
math.e

random.shuffle([1,2,3,4,5]) #permantely shuffle the list

import time
time.time() #current time in seconds from 1 jan 1970 

time.ctime() #current time

print("Hello")
time.sleep(5)   #wait for 5 seconds
print("World")

import os
os.getcwd() #current working directory  
os.listdir() #list of all files and folders in the current directory
os.mkdir("Test") #create a directory

'''STRINGS

-> strings are sequence of characters
-> In Python specifically,strings are a sequence of Unicode Characters
-> creating a string
-> Accessing Strings
-> Adding Chars to strings
-> Editing strings
-> Deleting strings
->Operations on stringd
->String Functions
'''
#creating
x="Krishna"
"It's a beautiful day"
c='''This is Krishna
    This is Keishna'''
print(x)
print(c)
c=str("Hello")

#Accessing Substrings from a String

#Concept of indexing
c="hello"
print(c[0])
print(c[1]) #positive indexing
print(c[-1]) #negative indexing->from right to left
print(c[-2])

#Slicing
c="Hello World"
print(c[0:5]) #Hello
print(c[6:]) #World
print(c[2:6:2])#lo
print(c[0:6:-1])# never take negative step with positive numbers\
print(c[::-1])#reverse the string

#Editing and Deleting Strings
#Strings are immutable

del c #delete the string-> partially delete not possible and reassign possible

'''Operations on Strings
1.Arithmetic Operations
2.Relational Operations
3.Logical Operations
4.Loops on strings
5.Membership Operations'''

"hello"+"world" #concatenation
"hello"*3 #hellohellohello
"hello" in "hello world" #True
print("*"*50)
print("Hello"*5)
"Mumbai">"Pune"#Comparison in Lexicographical order->False
"kol"<"KOL"# small letters baad m aate h
"hello" and "world" #world
#Empty string is always false
#Non-empty string is always true
"hello" or "world" #hello
'h' in c #True

#String Functions
'''Commonly used string functions
1.len()
2.count()
3.max
4.min
5.sorted'''

c="kolkata"
len(c)#7

max(c)#t
min(c)#a
sorted(c)#['a','k','k','l','o','t','a']-> in ascending order wrt ASCII value

#Capitalize/Title/Lower/Swapcase

"He is krishna".capitalize() #He is krishna
"He is krishna".title() #He Is Krishna
"He is krishna".lower() #he is krishna
"He is krishna".upper() #HE IS KRISHNA
"He is krishna".swapcase() #hE IS KRISHNA

#Count->Find the frequency of substring
"hello world".count('l') #3

#Find->Find the index of substring->first occurence
"hello world".find('l') #2->if not found then -1

#Index->Find the index of substring->first occurence
"hello world".index('l') #2->if not found then error

#endswith,startswith
"hello world".endswith('d') #True
"hello world".startswith('h') #True 

#format
"Hello my name is {} and I am {}".format("Krishna","God")

"Hello my name is {1} and I am {0}".format("Krishna","God")

"Hello my name is {name} and I am {status}".format(name="Krishna",status="God")

#isalnum->check if all characters are alphanumeric
"hello123".isalnum() #True

#isalpha->check if all characters are alphabets
"hello".isalpha() #True

#isdigit->check if all characters are digits
"123".isdigit() #True

#isdecimal->check if all characters are decimals
"123".isdecimal() #True

#isidentifier->check if string is a valid identifier
"hello".isidentifier() #True    

#Split->Split the string into a list
"Hello World".split() #['Hello','World']

"Hello,World".split(",") #['Hello','World']

"This is Krishna".split("is") #['Th',' Kr','hna']

#Join->Join the list into a string
" ".join(['Hello','World']) #Hello World

"/".join(['Hello','World']) #Hello/World

#Replace->Replace the substring with another substring
"Hello World".replace("World","Krishna") #Hello Krishna

#Strip->Remove the leading and trailing whitespaces
name="   Krishna   "
name.strip() #Krishna

'''
LISTS may or may not be homogeneous while array is homogeneous
Array stores data on contiguous memory locations
List stores data on non-contiguous memory locations
Arrays are much faster while lists are programmer friendly
Lists are mutable
'''
L=[1,2,3,4,5]
L=[1,2,3,4,5,'Krishna']

#Multidimensional List
#2D
L=[[1,2,3],[4,5,6],[7,8,9]]
#3D
L=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]

L=list("Krishna") #['K','r','i','s','h','n','a']

L.append(6) #Add an element at the end of the list
L.insert(2,5) #Add an element at a specific index
L.extend([7,8,9]) #Add multiple elements at the end of the list  

#Delete
del L
del L[2]
del L[-4]
del L[-3:]

L.remove("hello") # we use remove if we don't know the index position

L.pop() # remove last element

L.clear() #List koo empty krta h

L=[1,2,3,4]
L1=[5,6,7,8]

L+L1
for i in L1:
    print(i)
4 in L1

#Functions in List
len(L)
min(L)
max(L)
sorted(L)#[1,2,3,4]
#Sorted is not a permanent operation
sorted(L,reverse=True) #[4,3,2,1]
L.sort() # sort is a permanent operation

L.index[3]

sample="today has been great for me"
print(sample.split())
L=[]
for i in sample.split():
    print(i.capitalize())
    L.append(i.capitalize())
print(L)
print("".join(L))
 
 #Tuples

 #Creating
T1=()
T2=(1,2,3,4,5)
T3=("Hello",2,3,4,5)
#Single Item Tuple
T4=("hello",)
T6=tuple("Goa")

#Access
T2[0] #1
T2[1] # 2

#Edit
T2[0]=100 #Tupel does not support editing.Tuples are immutable
del T1 #deleting whole tuple is possible
T2=(1,2,3,4,5)
T3=("Hello",4,5,6)
T2+T3
T2*3
for i in T2:
    print(i)

1 in T2 #True
len[T2] #5
min[T2]#1
max[T2] #5
sum[T2] #15
sorted[T2] #[1,2,3,4,5]

#Tuples are read onli data types

#Sets '''
# 1->Sets do not allow duplicates
# 2-> Sets have no indexing/slicing
# 3->Sets don't allow mutable data types
# 4->Sets itself is mutable data type'''

#Empty set creation
s1={}#Not empty set
type(s1) #dict
s1=set() #empty set
s2={"hello",4.5,True}
S3={1,1,2,2,3,3} #{1,2,3}
s4={[1,2,3],"Hello"} #Error
s4={(1,2,3),"Hello"} #{'Hello',(1,2,3)}
#Sets have no indexing
#They follow Hashing
s5={{1},{2}}

#Access Items
s1[0]#Sets do not support indexing

#Add Items
S1={2,3,100,5,4}
S1.add(6)#{2,3,100,5,4,6}

#Delete items->del,remove,pop
del s2 #Delete whole set
s1.remove(100) #{2,3,5,4}

s1.pop()#2
s1.pop()#3

#Sets doesn't support concatenation and multiplication but looping and membership functions are available

for i in s1:
    print(i)

#Functions
len(S1) #5
min(S1) #1
max(S1) #5
sum(S1) #15
sorted(S1) #[1,2,3,4,5]
sorted(S1,reverse=True)

#Functions specific to set
S1={1,2,3,4,5}
S2={3,4,5,6,7}
S1.union(S2) #{1,2,3,4,5,6,7}
S1.Intersection(S2) #{3,4,5}
S1.difference(S2)#{1,2}
S2.difference(S1)#{6,7}
S1.symmetric_difference(S2)#{1,2,6,7}
S1.isdisjoint(S2)#False

#Dictionary

{"Name":"Nitish","Gender":"Male"}

#Dictionary has no indexing
# Dictionary is a mutable types
# Keys->immutable,values->They can be mutable
# Keys should be unique
# Mutable ->List/Sets/Dictionary
#Immutable ->Strings/tuples/int/float/Boolean/complex

D1={[1,2,3]:"Nitish"} #Error as list is mutable
D1={(1,2,3):"Nitish"} # {(1,2,3):"Nitish"}
D2={"Name":"Rahul","Name":"Rohit"} #{'Name':'Rohit'}
D3={"Name":"Krishna","College":"CMU","Marks":{"AI":56,"DS":54}}

#Access item from a dict->from keys
D3['Marks']
D3['Marks']['DS']
D3['Marks']['DS']=64
D3.get('Name')


del D3
del D3['College']
D3.clear()





 























