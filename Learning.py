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







